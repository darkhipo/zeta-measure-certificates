# Zeta irrationality-measure bounds: exact rational certificate

This repository packages the final exact rational arithmetic behind the current
best bounds from

> Elyasheev Leibtag, Hila Barkan, Rotem Kalisch, Shachar Weinbaum, Michael
> Shalyt, Ido Kaminer, *New Directions in Irrationality*, arXiv:2610.27799v1
> (20 October 2026), Theorem 2:

    mu(zeta(2)) < 4.62675
    mu(zeta(3)) < 5.4197

The exact values certified here are

    mu(zeta(2)) <= 62636575/13537936 = 4.626744800684536...
    mu(zeta(3)) <= 3760250/693817    = 5.419656768283279...

with approximation exponents

    delta(zeta(2)) > 13537936/49098639 = 0.2757293537...
    delta(zeta(3)) > 693817/3066433    = 0.2262619140...

## What is whose

- **Leibtag, Barkan, Kalisch, Weinbaum, Shalyt, Kaminer** — the conservative
  matrix field construction, the analytic and arithmetic arguments, the
  public computational supplement, and the Lean formalization.
- **RamanujanMachine** — the public supplement repository and the pinned Lean
  projects at
  https://github.com/RamanujanMachine/new-directions-in-irrationality.
- **MultiAgency / darkhipo** — this independent packaging of the final
  rational arithmetic and reproduction of the supplement's checks.

This artifact is a numerical certificate, not a new proof and not a Lean
formalization. The paper's analytic, prime-number-theorem, and
irrationality-criterion inputs remain the cited paper's arguments.

## Reproduction

The source supplement was checked out at commit
`3ca026c31396b26c1d804ff8a800b9979d7e4200` and run with Python 3.12.14:

    python verify_release.py
    python run_all.py --timeout 600

`verify_release.py` reported `PASS: 311 source and fixed-data files match the
release manifest`. `run_all.py` passed all nine Section 6 notebooks and all
eight additional script checks. The run receipt is in `receipt.json`.

The local `check_bounds.py` is stdlib-only and re-derives the displayed exact
rational inequalities from the paper's reported `g` and `h` rates:

    python3 check_bounds.py

## Evidence level

Exact-rational certificate plus a reproduced public computational supplement.
This is **not** a Lean proof and does not establish the paper's analytic,
prime-number-theorem, or irrationality-criterion inputs. The upstream Lean
formalizations are separately pinned in the supplement's `lean/README.md`; the
zeta(2) project explicitly assumes the prime number theorem as an axiom.
