---
title: "Standard Distributions"
sources: []
requires: [math/probability/uniform-distribution, math/probability/poisson-distribution, math/probability/geometric-distribution]
status: draft
---

<!-- Overview kept after the split of 2026-11-16 (SPEC §2.6): the four distributions now have their own notes. The comparison is our own; no external source. -->

Four standard distributions, each in its own note: @sec-math-probability-uniform-distribution, @sec-math-probability-binomial-distribution, @sec-math-probability-poisson-distribution and @sec-math-probability-geometric-distribution. This note compares them.

## Comparing the four

The plots in the four notes use the same axes and have mean about $3$, so the shapes can be compared directly.

| | $X$ is | $E[X]$ | $\mathrm{Var}(X)$ | use when |
|---|---|---|---|---|
| $\mathrm{Unif}(a,b)$ | one of $a,\dots,b$ | $\frac{a+b}2$ | $\frac{(b-a+1)^2-1}{12}$ | all outcomes equally likely |
| $\mathrm{Bin}(n,p)$ | successes in $n$ trials | $np$ | $np(1-p)$ | a fixed number of trials |
| $\mathrm{Poisson}(\mu)$ | events in an interval | $\mu$ | $\mu$ | a steady rate, no fixed number of trials |
| $\mathrm{Geom}(p)$ | trials to first success | $\frac1p$ | $\frac{1-p}{p^2}$ | repeat until the first success |

Binomial and Poisson count *how many* successes; Geometric counts *how long* until one. Binomial is bounded by $n$, while Poisson and Geometric have no upper limit. For large $n$ and small $p$, $\mathrm{Bin}(n,p)\approx\mathrm{Poisson}(np)$ (@thm-poisson-as-a-limit-of). Only Geometric is memoryless.
