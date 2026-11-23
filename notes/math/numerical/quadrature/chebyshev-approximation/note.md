---
title: "Chebyshev Approximation"
sources: [mit18335-35]
requires: [math/numerical/quadrature/trapezoidal-rule-convergence]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 35 (Chebyshev approximation), in our own wording; proofs written out in steps; interpolation errors computed with numpy. -->

Polynomial interpolation at equally spaced points can diverge, as Runge's example shows. Interpolating at Chebyshev points instead converges for every smooth function, exponentially for analytic ones. The reason is the substitution $x=\cos\theta$, which turns a smooth function on $[-1,1]$ into a smooth *periodic* function of $\theta$ and a polynomial into a cosine series.

::: {#def-chebyshev-polynomials .definition name="Chebyshev polynomials and Chebyshev points"}

The *Chebyshev polynomial* of degree $n$ is defined on $[-1,1]$ by
$$T_n(\cos\theta)=\cos(n\theta),$$
and satisfies $T_0=1$, $T_1=x$, $T_{n+1}=2xT_n-T_{n-1}$. The *Chebyshev points* (of the second kind) are the $n+1$ extreme points of $T_n$,
$$x_k=\cos\frac{k\pi}n,\qquad k=0,\dots,n,$$
the projections onto the $x$-axis of $n+1$ equally spaced points on the upper half of the unit circle.

:::

::: {#prp-chebyshev-polynomial-properties .proposition name="Basic properties"}

1. $T_n$ is a polynomial of degree $n$ with leading coefficient $2^{n-1}$ ($n\ge1$), and $\lvert T_n(x)\rvert\le1$ on $[-1,1]$ with value $\pm1$ at the $n+1$ points $x_k$.

2. The $T_n$ are orthogonal with respect to the weight $1/\sqrt{1-x^2}$: $\int_{-1}^1T_jT_k\,\frac{dx}{\sqrt{1-x^2}}=0$ for $j\ne k$.

3. Every $f$ that is Lipschitz on $[-1,1]$ has an absolutely convergent *Chebyshev series* $f=\sum_{k\ge0}a_kT_k$, namely the cosine series of $g(\theta)=f(\cos\theta)$.

:::

::: {.proof}

1. $\cos((n+1)\theta)+\cos((n-1)\theta)=2\cos\theta\cos(n\theta)$ gives the recurrence; by induction $T_n$ is a polynomial with leading coefficient $2^{n-1}$. The bound and the extreme values are those of $\cos(n\theta)$, attained at $\theta=k\pi/n$.

2. Substitute $x=\cos\theta$, $dx/\sqrt{1-x^2}=-d\theta$: the integral becomes $\int_0^\pi\cos(j\theta)\cos(k\theta)\,d\theta=0$ for $j\ne k$ (@prp-trigonometric-orthogonality).

3. $g(\theta)=f(\cos\theta)$ is even, $2\pi$-periodic and Lipschitz, so its Fourier series is a cosine series $\sum a_k\cos(k\theta)$ converging absolutely (by the standard result for Lipschitz periodic functions); substituting back gives $\sum a_kT_k(x)$.

:::

::: {#fig-chebyshev-approximation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=2.2]
\draw[faint] (1,0) arc (0:180:1);
\draw[faint, ->] (-1.2,0) -- (1.25,0);
\foreach \k in {0,...,8} {\coordinate (p\k) at ({cos(\k*22.5)},{sin(\k*22.5)}); \fill[primary] (p\k) circle (0.9pt); \draw[faint, dashed] (p\k) -- ({cos(\k*22.5)},0); \fill[accent] ({cos(\k*22.5)},0) circle (1.1pt);}
\node[tick, below] at (-1,0) {$-1$}; \node[tick, below] at (1,0) {$1$};
\begin{scope}[yshift=-1.55cm]
\draw[faint, ->] (-1.2,0) -- (1.25,0);
\draw[emph, domain=-1:1, samples=120] plot (\x,{0.55*cos(4*acos(\x))});
\node[tick, right] at (1.0,0.55) {$T_4$};
\draw[emph, dashed, domain=-1:1, samples=120] plot (\x,{0.55*cos(5*acos(\x))});
\node[tick, right] at (1.0,-0.45) {$T_5$};
\end{scope}
\end{tikzpicture}
\end{center}
```

Top: the Chebyshev points for $n=8$ are equally spaced points on the semicircle projected down; they cluster near $\pm1$. Bottom: $T_4$ and $T_5$ (vertically scaled) oscillate between $\pm1$ with equal ripples, $T_n(\cos\theta)=\cos n\theta$.

:::

::: {#def-chebyshev-interpolation .definition name="Chebyshev interpolation"}

The *Chebyshev interpolant* $p_n$ of $f$ is the polynomial of degree $\le n$ with $p_n(x_k)=f(x_k)$ at the $n+1$ Chebyshev points. Writing $p_n=\sum_{k=0}^n\tilde a_kT_k$, the coefficients are a discrete cosine transform of the samples,
$$\tilde a_k=\frac{c_k}{n}\sum_{j=0}^{n}{}^{''}f(x_j)\cos\frac{jk\pi}n,\qquad c_0=c_n=1,\ c_k=2\ \text{otherwise},$$
where $\sum''$ halves the first and last terms. This is the trapezoidal rule applied to the cosine coefficients of $f(\cos\theta)$, and it costs $O(n\log n)$ by the FFT.

:::

::: {#thm-chebyshev-interpolation-convergence .theorem name="Convergence of Chebyshev interpolation"}

If $f=\sum_ka_kT_k$ with $\sum\lvert a_k\rvert<\infty$, the Chebyshev interpolant satisfies
$$\max_{[-1,1]}\lvert f-p_n\rvert\le2\sum_{k>n}\lvert a_k\rvert .$$
Hence if $f$ has $\nu$ derivatives of bounded variation the error is $O(n^{-\nu})$, and if $f$ is analytic on $[-1,1]$ the error decreases exponentially in $n$.

:::

::: {.proof}

1. *Aliasing.* On the grid $\theta_j=j\pi/n$, $\cos(k\theta_j)$ for $k>n$ coincides with $\cos(k'\theta_j)$ for a unique $k'\in\{0,\dots,n\}$ (reduce $k$ modulo $2n$ and reflect $k\mapsto2n-k$), so $T_k(x_j)=T_{k'}(x_j)$.

2. Hence the polynomial $q=\sum_{k\le n}a_kT_k+\sum_{k>n}a_kT_{k'}$ has degree $\le n$ and agrees with $f$ at all $n+1$ points; by uniqueness of interpolation $p_n=q$.

3. $f-p_n=\sum_{k>n}a_k(T_k-T_{k'})$, and $\lvert T_k-T_{k'}\rvert\le2$ on $[-1,1]$, giving the bound.

4. The decay of $a_k$ is the decay of the cosine coefficients of the periodic function $f(\cos\theta)$: $O(k^{-\nu-1})$ under the smoothness assumption (integration by parts, as in @thm-trapezoid-periodic-aliasing) and geometric for analytic $f$ (contour shift). Summing the tail gives the stated rates.

:::

::: {#exm-runge-phenomenon .example name="Runge's function"}

Interpolate $f(x)=1/(1+25x^2)$ on $[-1,1]$. At equally spaced points the maximum error *grows*: $0.44$ for $n=4$, $3.7$ for $n=12$, $257$ for $n=24$, with wild oscillations near the ends. At Chebyshev points it decreases steadily: $0.46$, $0.084$, $0.0082$ for the same $n$, by a factor about $0.82$ per degree. That factor is $1/\rho$ where the ellipse with foci $\pm1$ and parameter $\rho$ passes through the poles $\pm i/5$ of $f$: $\rho=\tfrac15+\sqrt{1+\tfrac1{25}}\approx1.22$.

:::

::: {#fig-chebyshev-approximation-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.5cm, y=0.8cm]
\draw[->, faint] (0,0) -- (25.5,0) node[lab, right] {$n$};
\draw[->, faint] (0,-2.5) -- (0,2.8) node[lab, above] {$\log_{10}\max\lvert f-p_n\rvert$};
\foreach \x in {4,8,...,24} {\draw[faint] (\x,-0.08) -- (\x,0.08); \node[tick, below] at (\x,-0.08) {$\x$};}
\foreach \y in {-2,-1,1,2} {\draw[faint] (-0.2,\y) -- (0.2,\y); \node[tick, left] at (-0.2,\y) {$\y$};}
\draw[hl] plot coordinates {(4,-0.36) (8,0.02) (12,0.56) (16,1.16) (20,1.78) (24,2.41)};
\draw[emph] plot coordinates {(4,-0.34) (8,-0.69) (12,-1.07) (16,-1.44) (20,-1.75) (24,-2.09)};
\node[lab] at (17,2.0) {equispaced};
\node[lab] at (19,-1.15) {Chebyshev};
\end{tikzpicture}
\end{center}
```

Maximum interpolation error for Runge's function $1/(1+25x^2)$ in @exm-runge-phenomenon: exponential divergence at equally spaced points, exponential convergence at Chebyshev points.

:::
