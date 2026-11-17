---
title: "Buffon's Needle"
sources: [cs70-20.6]
requires: [math/probability/continuous/continuous-random-variables, math/probability/discrete/indicator-variables]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 20 (cs70-20.6, optional section), in our own wording; proofs written out in steps. -->

A needle of length $\ell$ is thrown at random onto a floor ruled with parallel lines at distance $\ell$ apart. The probability that it crosses a line turns out to be $\frac2\pi$, so the fraction of crossings in many throws estimates $\pi$ (@thm-law-of-large-numbers). We prove the value twice.

::: {#thm-buffons-needle .theorem name="Buffon's needle"}

A needle of length $\ell$ thrown at random onto a floor with parallel lines at distance $\ell$ apart crosses a line with probability $\dfrac2\pi$.

:::

::: {.proof}

*First proof: integrating a joint density.*

1. The position of the needle relative to the lines is given by two random variables: the distance $Y$ from its midpoint to the nearest line, in $[0,\frac\ell2]$, and the angle $\Theta$ between the needle and the normal to the lines, in $[-\frac\pi2,\frac\pi2]$. A random throw means that $(Y,\Theta)$ is uniform on this rectangle, whose area is $\frac{\pi\ell}2$: its joint density is $f(y,\theta)=\frac2{\pi\ell}$ there and $0$ elsewhere.

2. The two ends of the needle lie at distance $\frac\ell2\cos\Theta$ from the midpoint, measured along the normal. So the needle crosses a line exactly when $Y\le\frac\ell2\cos\Theta$.

3. Integrate the density over this region (@def-joint-density):
   $$\Pr\Bigl(Y\le\tfrac\ell2\cos\Theta\Bigr)=\int_{-\pi/2}^{\pi/2}\int_0^{(\ell/2)\cos\theta}\frac2{\pi\ell}\,dy\,d\theta=\int_{-\pi/2}^{\pi/2}\frac{\cos\theta}\pi\,d\theta=\frac1\pi\Bigl[\sin\theta\Bigr]_{-\pi/2}^{\pi/2}=\frac2\pi.$$

:::

::: {#rmk-buffons-needle-noodle .remark name="Second proof: Buffon's noodle"}

Take lines at distance $1$, and let $p$ be the crossing probability for a needle of length $1$. A needle crosses at most one line except with probability $0$, so $p$ is also the expected number $E[X]$ of crossings (@prp-expectation-of-indicator).

1. *Expected crossings are proportional to length.* Cut a needle of length $1$ into $m$ equal pieces and let $I_k$ count the crossings of piece $k$. All pieces are thrown in the same random way, so the $E[I_k]$ are equal, and by @thm-linearity-of-expectation $E[X]=mE[I_1]$. So a piece of length $\frac1m$ has $\frac1m E[X]$ expected crossings, and by additivity again a needle of length $\frac km$ has $\frac kmE[X]$. Approximating any length $\ell$ by rationals, a needle of length $\ell$ has $\ell\,E[X]$ expected crossings.

2. *Bent needles.* Join needles of lengths $\ell_1,\dots,\ell_n$ end to end at hinges into a "noodle". Linearity of expectation still applies, even though the pieces are dependent, so the noodle has $(\ell_1+\dots+\ell_n)E[X]$ expected crossings. Letting the pieces become short, the same holds for any curve: the expected number of crossings is its length times $E[X]$.

3. *A circle.* A circle of diameter $1$ has length $\pi$ and, except with probability $0$, crosses the lines exactly twice. So $\pi E[X]=2$, and $p=E[X]=\frac2\pi$.

The limits in steps 1 and 2 need a continuity argument, which we do not give; the first proof is complete.

:::
