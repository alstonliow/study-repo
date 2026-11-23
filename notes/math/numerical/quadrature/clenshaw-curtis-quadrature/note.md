---
title: "Clenshaw–Curtis Quadrature"
sources: [mit18335-34]
requires: [math/numerical/quadrature/chebyshev-approximation]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 34 (Clenshaw–Curtis quadrature), in our own wording; proofs written out in steps; weights and errors computed in Python. -->

To integrate a smooth non-periodic function on $[-1,1]$ we can interpolate it at Chebyshev points and integrate the interpolant exactly. Equivalently, we substitute $x=\cos\theta$ and apply the trapezoidal rule to the resulting periodic integrand. This *Clenshaw–Curtis* rule inherits the exponential convergence of both ideas.

::: {#def-clenshaw-curtis .definition name="Clenshaw–Curtis quadrature"}

The $(n+1)$-point *Clenshaw–Curtis rule* is
$$\int_{-1}^1f(x)\,dx\approx\int_{-1}^1p_n(x)\,dx=\sum_{k=0}^n w_kf(x_k),\qquad x_k=\cos\frac{k\pi}n,$$
where $p_n=\sum_{k\le n}\tilde a_kT_k$ is the Chebyshev interpolant (@def-chebyshev-interpolation). Since
$$\int_{-1}^1T_k(x)\,dx=\begin{cases}\dfrac{2}{1-k^2},&k\text{ even},\\0,&k\text{ odd},\end{cases}$$
the rule is $\sum_{k\text{ even}}2\tilde a_k/(1-k^2)$, computable in $O(n\log n)$ operations by a fast cosine transform; equivalently the weights $w_k$ can be tabulated once.

:::

```{=latex}
\begin{algorithm}
\caption{Clenshaw--Curtis quadrature on $[-1,1]$}
\begin{algorithmic}
\INPUT $f$, degree $n$ (even)
\STATE $f_j\gets f(\cos(j\pi/n))$ for $j=0,\dots,n$
\STATE $\tilde a_k\gets\frac{c_k}{n}\sum''_jf_j\cos(jk\pi/n)$ for even $k\le n$ \COMMENT{DCT, $O(n\log n)$}
\STATE \textbf{return} $\sum_{k\text{ even}}2\tilde a_k/(1-k^2)$
\end{algorithmic}
\end{algorithm}
```

::: {#prp-chebyshev-integral .proposition name="Integrals of Chebyshev polynomials"}

$\int_{-1}^1T_k\,dx=2/(1-k^2)$ for even $k$ and $0$ for odd $k$.

:::

::: {.proof}

1. With $x=\cos\theta$, $\int_{-1}^1T_k(x)\,dx=\int_0^\pi\cos(k\theta)\sin\theta\,d\theta$.

2. $\cos(k\theta)\sin\theta=\tfrac12\bigl(\sin((k+1)\theta)-\sin((k-1)\theta)\bigr)$, and $\int_0^\pi\sin(j\theta)\,d\theta=(1-\cos j\pi)/j$, which is $2/j$ for odd $j$ and $0$ for even $j$.

3. For even $k$, $k\pm1$ are odd: the integral is $\tfrac12\bigl(\tfrac2{k+1}-\tfrac2{k-1}\bigr)=\tfrac{2}{1-k^2}$ (for $k=0$ read $\tfrac12(2+2)=2$). For odd $k$ both terms vanish.

:::

::: {#thm-clenshaw-curtis-convergence .theorem name="Accuracy of Clenshaw–Curtis"}

The $(n+1)$-point rule integrates polynomials of degree $\le n$ exactly, its weights are positive and sum to $2$, and for $f=\sum a_kT_k$ with $\sum\lvert a_k\rvert<\infty$
$$\Bigl\lvert\int_{-1}^1f\,dx-\sum_kw_kf(x_k)\Bigr\rvert\le4\sum_{k>n}\lvert a_k\rvert .$$
So the error is $O(n^{-\nu})$ for $f$ with $\nu$ derivatives of bounded variation and exponentially small for analytic $f$.

:::

::: {.proof}

1. *Exactness.* For $\deg f\le n$ the interpolant is $f$ itself, and it is integrated exactly.

2. *Error.* $\bigl\lvert\int(f-p_n)\bigr\rvert\le2\max\lvert f-p_n\rvert\le4\sum_{k>n}\lvert a_k\rvert$ by @thm-chebyshev-interpolation-convergence. The rates follow as there.

3. *Weights.* Positivity of the $w_k$ is a classical computation from their explicit cosine-sum formula (Imhof); we only use it through @prp-quadrature-conditioning, which shows that it makes the rule insensitive to errors in the samples. Their sum is the integral of $1$, namely $2$.

:::

::: {#exm-clenshaw-curtis-weights .example name="Weights for nine points"}

For $n=8$ the nodes are $\cos(k\pi/8)$ and the weights, from the end to the middle, are $0.0159,\ 0.1462,\ 0.2794,\ 0.3617,\ 0.3937$, symmetric and summing to $2$. The $9$-point Gauss–Legendre rule (@sec-math-numerical-quadrature-gaussian-quadrature) has nodes $0,\pm0.324,\pm0.613,\pm0.836,\pm0.968$ and weights $0.3302,\ 0.3123,\ 0.2606,\ 0.1806,\ 0.0813$. Both put more nodes near the ends, with smaller weights there.

:::

::: {#fig-clenshaw-curtis-quadrature-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=3cm, y=4cm]
\draw[->, faint] (-1.15,0) -- (1.2,0) node[lab, right] {$x$};
\draw[->, faint] (0,0) -- (0,0.47) node[lab, above] {weight};
\foreach \x/\w in {1/0.0159,0.924/0.1462,0.707/0.2794,0.383/0.3617,0/0.3937,-0.383/0.3617,-0.707/0.2794,-0.924/0.1462,-1/0.0159} {\draw[hl] (\x,0) -- (\x,\w); \fill[accent] (\x,\w) circle (1.4pt);}
\foreach \x/\w in {0.968/0.0813,0.836/0.1806,0.613/0.2606,0.324/0.3123,0/0.3302,-0.324/0.3123,-0.613/0.2606,-0.836/0.1806,-0.968/0.0813} {\draw[emph, dashed] (\x,0) -- (\x,\w); \fill (\x,\w) circle (1.2pt);}
\node[tick, below] at (-1,0) {$-1$}; \node[tick, below] at (1,0) {$1$};
\node[lab] at (0.62,0.42) {Clenshaw--Curtis};
\node[lab] at (-0.7,0.42) {Gauss (dashed)};
\end{tikzpicture}
\end{center}
```

Nodes and weights of the $9$-point Clenshaw–Curtis rule (solid) and the $9$-point Gauss–Legendre rule (dashed) from @exm-clenshaw-curtis-weights.

:::

::: {#exm-clenshaw-curtis-vs-gauss .example name="Is Gauss better?"}

Integrate $f(x)=1/(1+16x^2)$ over $[-1,1]$ (exact value $\tfrac12\arctan4$). With $n+1$ points the errors are:

| $n$ | Gauss | Clenshaw–Curtis | trapezoid |
|---|---|---|---|
| $8$ | $1.4\times10^{-2}$ | $3.1\times10^{-2}$ | $1.8\times10^{-3}$ |
| $16$ | $2.7\times10^{-4}$ | $5.8\times10^{-4}$ | $2.8\times10^{-4}$ |
| $32$ | $9.9\times10^{-8}$ | $2.3\times10^{-7}$ | $7.2\times10^{-5}$ |
| $64$ | $1.5\times10^{-14}$ | $9.5\times10^{-13}$ | $1.8\times10^{-5}$ |

Gauss is exact for polynomials of twice the degree, yet for this integrand (analytic, with poles near the interval at $\pm i/4$) it is only modestly ahead of Clenshaw–Curtis: both converge at a geometric rate set by the poles, and the factor of two in polynomial degree shows up only for functions analytic in a large region. The trapezoidal rule converges only like $n^{-2}$, its small-$n$ advantage reflecting a lucky constant.

:::

::: {#fig-clenshaw-curtis-quadrature-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.6cm, y=0.38cm]
\draw[->, faint] (1.8,0.5) -- (6.4,0.5) node[lab, right] {$\log_2n$};
\draw[->, faint] (1.8,0.5) -- (1.8,-14.5) node[lab, below] {$\log_{10}\lvert\text{error}\rvert$};
\foreach \x in {2,...,6} {\draw[faint] (\x,0.35) -- (\x,0.65); \node[tick, above] at (\x,0.65) {$\x$};}
\foreach \y in {-4,-8,-12} {\draw[faint] (1.77,\y) -- (1.83,\y); \node[tick, left] at (1.77,\y) {$\y$};}
\draw[emph, dashed] plot coordinates {(2,-0.96) (3,-1.84) (4,-3.57) (5,-7.01) (6,-13.83)};
\draw[hl] plot coordinates {(2,-0.58) (3,-1.51) (4,-3.24) (5,-6.64) (6,-12.02)};
\draw[emph] plot coordinates {(2,-1.18) (3,-2.75) (4,-3.55) (5,-4.14) (6,-4.74)};
\node[lab] at (5.6,-3.4) {trapezoid};
\node[lab] at (5.0,-9.6) {Clenshaw--Curtis};
\node[lab] at (6.0,-14.6) {Gauss};
\end{tikzpicture}
\end{center}
```

Errors from @exm-clenshaw-curtis-vs-gauss on a log scale against $\log_2n$. Gauss and Clenshaw–Curtis curve downward together (geometric convergence: the error exponent doubles when $n$ doubles); the trapezoid is a straight line of slope $-2\log_{10}2$.

:::
