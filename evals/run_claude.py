#!/usr/bin/env python3
"""Run skill eval prompts against Claude in a clean context (one prompt per process)."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shlex
import subprocess
from pathlib import Path


DEFAULT_PROMPTS = "evals/prompts/skill-prompts.yaml"
DEFAULT_TEMPLATE = "evals/templates/feedback.md"
DEFAULT_OUTDIR = "evals/runs"
ENV_CMD = "CLAUDE_CMD"


def parse_value(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith('"') and raw.endswith('"'):
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return raw.strip('"')
    return raw


def load_prompts(path: Path) -> list[dict]:
    skills = []
    current_skill = None
    current_prompt = None

    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip(" "))
        stripped = line.strip()

        if stripped.startswith("- id:") and indent == 2:
            skill_id = stripped.split(":", 1)[1].strip()
            current_skill = {"id": skill_id, "title": "", "prompts": []}
            skills.append(current_skill)
            current_prompt = None
            continue

        if stripped.startswith("title:") and indent == 4 and current_skill is not None:
            current_skill["title"] = parse_value(stripped.split(":", 1)[1])
            continue

        if stripped.startswith("- id:") and indent == 6 and current_skill is not None:
            prompt_id = stripped.split(":", 1)[1].strip()
            current_prompt = {"id": prompt_id, "text": ""}
            current_skill["prompts"].append(current_prompt)
            continue

        if stripped.startswith("text:") and indent == 8 and current_prompt is not None:
            current_prompt["text"] = parse_value(stripped.split(":", 1)[1])
            continue

    return skills


def extract_claude_result(output: str) -> str | None:
    for line in reversed(output.strip().splitlines()):
        if not line:
            continue
        try:
            payload = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(payload, dict) and "result" in payload:
            value = payload["result"]
            if isinstance(value, str):
                return value.strip()
    return None


def run_prompt(cmd_template: str, model: str, prompt: str) -> tuple[int, str]:
    cmd = cmd_template.format(
        model=shlex.quote(model),
        prompt=shlex.quote(prompt),
    )
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        stderr = result.stderr.strip()
        stdout = result.stdout.strip()
        message = stderr or stdout or f"[error exit_code={result.returncode}]"
        return result.returncode, message

    stdout = result.stdout.strip()
    extracted = extract_claude_result(stdout)
    if extracted:
        return result.returncode, extracted
    if stdout:
        return result.returncode, stdout
    return result.returncode, f"[no output] exit_code={result.returncode}"


def sanitize_segment(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-")


def render_template(template_path: Path, skill_id: str, agent: str, model: str, date: str, prompt_set: str) -> str:
    template = template_path.read_text(encoding="utf-8")
    template = template.replace("<skill-id>", skill_id)
    template = template.replace("<agent-name>", agent)
    template = template.replace("<model-id>", model)
    template = template.replace("<YYYY-MM-DD>", date)
    template = template.replace("evals/prompts/skill-prompts.yaml", prompt_set)
    return template.rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Run skill eval prompts against Claude.")
    parser.add_argument("--model", required=True, help="Model identifier, used in output path and command template.")
    parser.add_argument("--agent", default="claude", help="Agent name used in output path.")
    parser.add_argument("--prompts", default=DEFAULT_PROMPTS, help="Path to prompt YAML.")
    parser.add_argument("--template", default=DEFAULT_TEMPLATE, help="Feedback template path.")
    parser.add_argument("--outdir", default=DEFAULT_OUTDIR, help="Output base directory.")
    parser.add_argument("--cmd", default=os.environ.get(ENV_CMD, ""), help="Command template with {model} and {prompt} placeholders.")
    parser.add_argument("--skill", action="append", help="Skill id to run. Repeat to run multiple. Defaults to all.")
    parser.add_argument("--date", default=dt.date.today().isoformat(), help="Date string for output filename.")

    args = parser.parse_args()

    if not args.cmd:
        raise SystemExit(f"Missing --cmd or {ENV_CMD} environment variable.")

    prompt_path = Path(args.prompts)
    template_path = Path(args.template)
    outdir = Path(args.outdir)

    skills = load_prompts(prompt_path)
    if args.skill:
        skill_filter = set(args.skill)
        skills = [s for s in skills if s["id"] in skill_filter]

    if not skills:
        raise SystemExit("No skills found for the given filters.")

    safe_model = sanitize_segment(args.model)

    total_skills = len(skills)
    total_prompts = sum(len(s.get("prompts", [])) for s in skills)
    prompt_counter = 0

    print(f"\n{'='*60}")
    print(f"  CLAUDE EVAL: {total_skills} skills, {total_prompts} prompts")
    print(f"  Model: {args.model}")
    print(f"{'='*60}\n")

    for skill_idx, skill in enumerate(skills, 1):
        skill_id = skill["id"]
        skill_title = skill.get("title", skill_id)
        skill_prompts = skill.get("prompts", [])

        print(f"[{skill_idx}/{total_skills}] {skill_title}")

        out_path = outdir / skill_id / args.agent / safe_model / f"{args.date}.md"
        out_path.parent.mkdir(parents=True, exist_ok=True)

        content = render_template(template_path, skill_id, args.agent, args.model, args.date, str(prompt_path))
        content += "\n## Raw Output\n\n"

        for prompt_idx, prompt in enumerate(skill_prompts, 1):
            prompt_id = prompt.get("id", "prompt")
            prompt_text = prompt.get("text", "")
            prompt_counter += 1

            print(f"    [{prompt_counter}/{total_prompts}] {prompt_id}...", end=" ", flush=True)

            _, response = run_prompt(args.cmd, args.model, prompt_text)

            print("✓")

            content += f"### {prompt_id}\n\n"
            content += "Prompt:\n\n```\n"
            content += prompt_text.strip() + "\n```\n"
            content += "\nResponse:\n\n```\n"
            content += response.strip() + "\n```\n"
            content += "\n\n"

        out_path.write_text(content, encoding="utf-8")
        print(f"    → Saved: {out_path}\n")

    print(f"{'='*60}")
    print(f"  COMPLETE: {prompt_counter} prompts processed")
    print(f"{'='*60}\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
