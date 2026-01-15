#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
from statistics import NormalDist


def _non_negative_int(value: str) -> int:
    try:
        parsed = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"Expected an integer, got {value!r}") from exc
    if parsed < 0:
        raise argparse.ArgumentTypeError(f"Expected >= 0, got {parsed}")
    return parsed


def _prob(value: str) -> float:
    try:
        parsed = float(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"Expected a number, got {value!r}") from exc
    if not (0 < parsed < 1):
        raise argparse.ArgumentTypeError(f"Expected 0 < p < 1, got {parsed}")
    return parsed


def srm_p_value_two_buckets(*, observed_a: int, observed_b: int, expected_a: float) -> tuple[float, float]:
    total = observed_a + observed_b
    if total == 0:
        raise ValueError("Total observations must be > 0")

    expected_b = 1 - expected_a
    exp_a = total * expected_a
    exp_b = total * expected_b

    chi2 = ((observed_a - exp_a) ** 2) / exp_a + ((observed_b - exp_b) ** 2) / exp_b

    # For df=1, chi-square survival function equals P(Z^2 >= chi2) = 2*(1 - Phi(sqrt(chi2))).
    normal = NormalDist()
    p_value = 2 * (1 - normal.cdf(math.sqrt(chi2)))
    return chi2, p_value


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check sample ratio mismatch (SRM) for a two-bucket split using a chi-square test (df=1).",
    )
    parser.add_argument("observed_a", type=_non_negative_int, help="Observed count in bucket A (e.g. control)")
    parser.add_argument("observed_b", type=_non_negative_int, help="Observed count in bucket B (e.g. treatment)")
    parser.add_argument(
        "--expected-a",
        type=_prob,
        default=0.5,
        help="Expected fraction in A (default: 0.5 for a 50/50 split).",
    )
    parser.add_argument(
        "--alpha",
        type=_prob,
        default=0.001,
        help="Alert threshold (default: 0.001; SRM should be rare under a correct split).",
    )

    args = parser.parse_args()

    chi2, p_value = srm_p_value_two_buckets(
        observed_a=args.observed_a,
        observed_b=args.observed_b,
        expected_a=args.expected_a,
    )

    total = args.observed_a + args.observed_b
    obs_a = args.observed_a / total
    exp_a = args.expected_a

    print("SRM check (two buckets)")
    print(f"- Observed: A={args.observed_a:,} ({obs_a:.4f}), B={args.observed_b:,} ({1 - obs_a:.4f})")
    print(f"- Expected: A={exp_a:.4f}, B={1 - exp_a:.4f}")
    print(f"- Chi-square: {chi2:.4f} (df=1)")
    print(f"- P-value:    {p_value:.6g}")
    if p_value < args.alpha:
        print(f"- Result:     FAIL (p < {args.alpha}; investigate SRM before trusting experiment results)")
        return 2

    print(f"- Result:     PASS (p >= {args.alpha})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
