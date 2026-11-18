---
title: "Improper Integrals"
sources: [mit1801-35, mit1801n-INT]
requires: [math/calculus/applications-of-derivatives/lhopitals-rule, math/calculus/integration-techniques/integration-by-parts]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 35 and Supplementary Notes INT, in our own wording; proofs written out in steps. -->

::: {#def-improper-integral .definition name="Improper integral"}

$$\int_a^\infty f(x)\,dx=\lim_{N\to\infty}\int_a^Nf(x)\,dx .$$
The integral converges if the limit exists (and is finite) and diverges otherwise. If $f$ is unbounded near $a$, likewise $\int_a^bf=\lim_{c\to a^+}\int_c^bf$. An integral over $(-\infty,\infty)$, or with several bad points, is split into pieces that each have one bad end; it converges only if every piece does.

:::

::: {#exm-improper-basic .example name="Basic examples"}

- $\int_0^\infty e^{-kx}dx=\lim_N\frac{1-e^{-kN}}k=\frac1k$ for $k>0$.
- $\int_{-\infty}^\infty\frac{dx}{1+x^2}=\lim\tan^{-1}x\big|_{-N}^{N}=\pi$.
- $\int_1^\infty\frac{dx}x=\lim\ln N=\infty$: diverges.

:::

::: {#thm-p-integrals .theorem name="Powers"}

$$\int_1^\infty\frac{dx}{x^p}\ \text{converges}\iff p>1\ \ \big(\text{value }\tfrac1{p-1}\big),\qquad \int_0^1\frac{dx}{x^p}\ \text{converges}\iff p<1\ \ \big(\text{value }\tfrac1{1-p}\big).$$

:::

::: {.proof}

1. For $p\neq1$, $\int_1^Nx^{-p}dx=\dfrac{N^{1-p}-1}{1-p}$. As $N\to\infty$, $N^{1-p}\to0$ if $p>1$ and $\to\infty$ if $p<1$.

2. Similarly $\int_c^1x^{-p}dx=\dfrac{1-c^{1-p}}{1-p}$, and as $c\to0^+$, $c^{1-p}\to0$ if $p<1$ and $\to\infty$ if $p>1$.

3. For $p=1$ both integrals are $\pm\ln$ of something tending to $\infty$, so both diverge.

:::

::: {#thm-comparison-integrals .theorem name="Comparison tests"}

Let $f,g\ge0$ on $[a,\infty)$.

1. (Direct comparison) If $f\le g$ and $\int_a^\infty g$ converges, so does $\int_a^\infty f$; if $\int_a^\infty f$ diverges, so does $\int_a^\infty g$.
2. (Limit comparison) If $f(x)/g(x)\to L$ with $0<L<\infty$ as $x\to\infty$, the two integrals both converge or both diverge.

:::

::: {.proof}

1. $F(N)=\int_a^Nf$ is non-decreasing in $N$ and bounded by $\int_a^\infty g$, so it has a limit (a bounded monotone function converges, by completeness of $\mathbb R$). The second half is the contrapositive.

2. For $x$ large, $\tfrac L2g\le f\le2Lg$; apply part 1 on $[b,\infty)$ for some large $b$, the piece over $[a,b]$ being finite.

:::

::: {#exm-improper-comparison .example name="Using comparison"}

- $\int_1^\infty\frac{dx}{\sqrt{x^3+1}}$ converges: the integrand behaves like $x^{-3/2}$ (limit comparison, $p=\frac32>1$).
- $\int_0^\infty e^{-x^2}dx$ converges: $e^{-x^2}\le e^{-x}$ for $x\ge1$. (Its value is $\sqrt\pi/2$, see @prp-gaussian-integral.)
- $\int_0^\infty x^ne^{-x}dx$ converges: $x^ne^{-x}\le x^{-2}$ for large $x$, because $x^{n+2}e^{-x}\to0$ by @exm-lhopital.

:::
