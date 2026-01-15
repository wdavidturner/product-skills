#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
from statistics import NormalDist


def _positive_float(value: str) -> float:
    try:
        parsed = float(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"Expected a number, got {value!r}") from exc
    if parsed <= 0:
        raise argparse.ArgumentTypeError(f"Expected > 0, got {parsed}")
    return parsed


def _prob(value: str) -> float:
    parsed = _positive_float(value)
    if not (0 < parsed < 1):
        raise argparse.ArgumentTypeError(f"Expected 0 < p < 1, got {parsed}")
    return parsed


def two_proportion_sample_size_per_group(
    *,
    baseline_rate: float,
    treatment_rate: float,
    alpha: float,
    power: float,
    two_sided: bool,
) -> int:
    if treatment_rate == baseline_rate:
        raise ValueError("treatment_rate must differ from baseline_rate")

    normal = NormalDist()
    z_alpha = normal.inv_cdf(1 - alpha / 2) if two_sided else normal.inv_cdf(1 - alpha)
    z_beta = normal.inv_cdf(power)

    p1 = baseline_rate
    p2 = treatment_rate
    p_bar = (p1 + p2) / 2
    effect = abs(p2 - p1)

    term1 = z_alpha * math.sqrt(2 * p_bar * (1 - p_bar))
    term2 = z_beta * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    n = ((term1 + term2) ** 2) / (effect**2)
    return math.ceil(n)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Estimate sample size for a two-variant conversion A/B test (normal approximation).",
    )
    parser.add_argument("--baseline", type=_prob, required=True, help="Baseline conversion rate, e.g. 0.10")

    mde = parser.add_mutually_exclusive_group(required=True)
    mde.add_argument("--mde-absolute", type=_positive_float, help="Minimum detectable effect, absolute (e.g. 0.005)")
    mde.add_argument(
        "--mde-relative",
        type=_positive_float,
        help="Minimum detectable effect, relative (e.g. 0.05 means +5%% over baseline)",
    )

    parser.add_argument("--alpha", type=_prob, default=0.05, help="Significance level (default: 0.05)")
    parser.add_argument("--power", type=_prob, default=0.80, help="Statistical power (default: 0.80)")
    parser.add_argument(
        "--one-sided",
        action="store_true",
        help="Use a one-sided test (default: two-sided).",
    )

    parser.add_argument(
        "--daily-eligible-users",
        type=_positive_float,
        help="Optional: eligible users per day (to estimate runtime).",
    )
    parser.add_argument(
        "--allocation",
        type=_prob,
        default=1.0,
        help="Optional: fraction of eligible users included in experiment (default: 1.0).",
    )

    args = parser.parse_args()

    baseline_rate = args.baseline
    if args.mde_absolute is not None:
        treatment_rate = baseline_rate + args.mde_absolute
    else:
        treatment_rate = baseline_rate * (1 + args.mde_relative)

    if not (0 < treatment_rate < 1):
        raise SystemExit(
            f"Computed treatment rate {treatment_rate:.6f} is outside (0,1); "
            "adjust baseline/MDE."
        )

    per_group = two_proportion_sample_size_per_group(
        baseline_rate=baseline_rate,
        treatment_rate=treatment_rate,
        alpha=args.alpha,
        power=args.power,
        two_sided=not args.one_sided,
    )
    total = per_group * 2

    print("Sample size estimate (two-variant conversion test)")
    print(f"- Baseline rate:   {baseline_rate:.6f}")
    print(f"- Treatment rate:  {treatment_rate:.6f}")
    print(f"- Alpha:           {args.alpha:.4f} ({'one-sided' if args.one_sided else 'two-sided'})")
    print(f"- Power:           {args.power:.2f}")
    print(f"- Needed per arm:  {per_group:,}")
    print(f"- Needed total:    {total:,}")

    if args.daily_eligible_users is not None:
        included_per_day = args.daily_eligible_users * args.allocation
        days = total / included_per_day if included_per_day > 0 else float("inf")
        print(f"- Est. days (@ {args.daily_eligible_users:,.0f}/day, allocation {args.allocation:.2f}): {days:.1f}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
