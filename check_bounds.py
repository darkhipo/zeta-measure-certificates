#!/usr/bin/env python3
"""Exact rational checks for the current zeta(2), zeta(3) irrationality-measure bounds.

This is a numerical certificate for the final rational arithmetic of:

  Elyasheev Leibtag, Hila Barkan, Rotem Kalisch, Shachar Weinbaum,
  Michael Shalyt, Ido Kaminer, "New Directions in Irrationality",
  arXiv:2610.27799v1, Theorem 2.

It does not prove the paper's analytic, prime-number-theorem, or
irrationality-criterion inputs. Those are the cited paper's arguments and
the accompanying public computational supplement.
"""
from fractions import Fraction as Q
import json

# Exact values printed by the supplement's final rational arithmetic.
ZETA2 = {
    "g": Q("62.636575"),
    "h": Q("49.098639"),
    "delta_claim": Q("0.2757"),
    "mu_claim": Q("4.62675"),
    "delta": Q(13537936, 49098639),
    "mu": Q(62636575, 13537936),
}
ZETA3 = {
    "g": Q("112.8075"),
    "h": Q("91.992990"),
    "delta_claim": Q("0.2262"),
    "mu_claim": Q("5.4197"),
    "delta": Q(693817, 3066433),
    "mu": Q(3760250, 693817),
}


def check(label, d):
    assert d["g"] > d["h"] > 0
    assert d["delta"] == d["g"] / d["h"] - 1
    assert d["mu"] == d["g"] / (d["g"] - d["h"])
    assert d["delta"] > d["delta_claim"]
    assert d["mu"] < d["mu_claim"]
    return {
        "target": label,
        "g": str(d["g"]),
        "h": str(d["h"]),
        "delta_exact": str(d["delta"]),
        "mu_exact": str(d["mu"]),
        "delta_decimal": float(d["delta"]),
        "mu_decimal": float(d["mu"]),
    }


if __name__ == "__main__":
    rows = [check("zeta(2)", ZETA2), check("zeta(3)", ZETA3)]
    print(json.dumps(rows, indent=2))
