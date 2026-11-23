---
title: "Convergence of the Trapezoidal Rule"
sources: [mit18335-33]
requires: [math/calculus/single-variable/applications-of-integrals/numerical-integration, math/linear-algebra/orthogonality/fourier-series, math/numerical/floating-point/conditioning]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 33 (numerical integration and the convergence of the trapezoidal rule) and its two notes (numerical integration; Fourier cosine series examples), in our own wording; proofs written out in steps; errors computed in Python. -->

The trapezoidal rule (@def-numerical-rules) is usually presented as a second-order method whose error falls like $1/N^2$. For smooth *periodic* functions integrated over a full period it is far better: the error falls faster than any power of $1/N$, exponentially for analytic integrands. Both facts follow from one computation with Fourier series, which also explains how Clenshaw–Curtis quadrature turns any smooth integrand into a periodic one.

::: {#def-quadrature-rule .definition name="Quadrature rule"}

A *quadrature rule* approximates $I(f)=\int_a^bf(x)\,dx$ by $Q_N(f)=\sum_{k}w_kf(x_k)$ with *nodes* $x_k$ and *weights* $w_k$. The *composite trapezoidal rule* with $N$ intervals of width $h=(b-a)/N$ has nodes $x_k=a+kh$, $k=0,\dots,N$, weights $h$ except $h/2$ at the two ends. For a $2\pi$-periodic $f$ on $[0,2\pi]$ the two end values coincide and the rule is simply $\frac{2\pi}N\sum_{k=0}^{N-1}f(2\pi k/N)$: equal weights at equally spaced points.

:::

::: {#prp-quadrature-conditioning .proposition name="Positive weights make quadrature well-conditioned"}

If all $w_k\ge0$ and the rule integrates constants exactly, then $\lvert Q_N(f)-Q_N(\tilde f)\rvert\le(b-a)\max_k\lvert f(x_k)-\tilde f(x_k)\rvert$: errors in the function values are not amplified.

:::

::: {.proof}

1. $\lvert Q_N(f-\tilde f)\rvert\le\sum_k\lvert w_k\rvert\,\lvert f(x_k)-\tilde f(x_k)\rvert\le\bigl(\sum_kw_k\bigr)\max_k\lvert f(x_k)-\tilde f(x_k)\rvert$.

2. Exactness for $f=1$ gives $\sum_kw_k=b-a$.

:::

::: {#thm-trapezoid-periodic-aliasing .theorem name="Trapezoidal rule error by aliasing"}

Let $f$ be $2\pi$-periodic with an absolutely convergent Fourier series $f(x)=\sum_{j\in\mathbb Z}c_je^{ijx}$. Then the $N$-point periodic trapezoidal rule satisfies
$$Q_N(f)-\int_0^{2\pi}f\,dx=2\pi\sum_{\ell\ne0}c_{\ell N}.$$
If $f$ has $p$ continuous derivatives the error is $o(N^{-p})$, and if $f$ is analytic in a strip $\lvert\operatorname{Im}x\rvert<\sigma$ the error is $O(e^{-\sigma'N})$ for every $\sigma'<\sigma$.

:::

::: {.proof}

1. The exact integral is $2\pi c_0$, since $\int_0^{2\pi}e^{ijx}\,dx=0$ for $j\ne0$.

2. For a single mode, $\frac{2\pi}N\sum_{k=0}^{N-1}e^{ij2\pi k/N}$ is a geometric sum with ratio $e^{2\pi ij/N}$: it equals $2\pi$ if $N$ divides $j$ and $0$ otherwise.

3. Summing over the absolutely convergent series term by term, $Q_N(f)=2\pi\sum_\ell c_{\ell N}$, so the error is $2\pi\sum_{\ell\ne0}c_{\ell N}$: only the modes that *alias* to the constant on the grid contribute.

4. *Smooth $f$.* Integrating by parts $p$ times, $c_j=(ij)^{-p}\frac1{2\pi}\int_0^{2\pi}f^{(p)}(x)e^{-ijx}dx$ (the boundary terms cancel by periodicity), and the last integral tends to zero by the Riemann–Lebesgue lemma. So $\lvert c_{\ell N}\rvert=o((\ell N)^{-p})$, and summing over $\ell$ gives $o(N^{-p})$ for $p\ge2$.

5. *Analytic $f$.* Shifting the contour of $c_j=\frac1{2\pi}\int_0^{2\pi}f(x)e^{-ijx}dx$ to $\operatorname{Im}x=\mp\sigma'$ (the vertical sides cancel by periodicity) gives $\lvert c_j\rvert\le Me^{-\sigma'\lvert j\rvert}$, and $\sum_{\ell\ne0}e^{-\sigma'\lvert\ell\rvert N}=O(e^{-\sigma'N})$.

:::

::: {#thm-trapezoid-nonperiodic .theorem name="Second-order error for non-periodic integrands"}

If $f\in C^2[a,b]$, the composite trapezoidal rule with step $h$ satisfies
$$Q_N(f)-\int_a^bf\,dx=\frac{h^2}{12}\bigl(f'(b)-f'(a)\bigr)+o(h^2).$$

:::

::: {.proof}

1. On one interval $[x_k,x_k+h]$, expand $f$ about the midpoint $m$: $f(m\pm\tfrac h2)=f(m)\pm\tfrac h2f'(m)+\tfrac{h^2}8f''(m)+o(h^2)$. The trapezoid gives $\tfrac h2\bigl(f(m-\tfrac h2)+f(m+\tfrac h2)\bigr)=hf(m)+\tfrac{h^3}8f''(m)+o(h^3)$.

2. The exact integral is $\int_{-h/2}^{h/2}\bigl(f(m)+tf'(m)+\tfrac{t^2}2f''(m)\bigr)dt+o(h^3)=hf(m)+\tfrac{h^3}{24}f''(m)+o(h^3)$.

3. The local error is $\tfrac{h^3}{12}f''(m)+o(h^3)$. Summing over the $N=(b-a)/h$ intervals, $\tfrac{h^2}{12}\sum_khf''(m_k)+o(h^2)=\tfrac{h^2}{12}\int_a^bf''+o(h^2)=\tfrac{h^2}{12}(f'(b)-f'(a))+o(h^2)$, since $\sum_khf''(m_k)$ is a Riemann sum.

:::

The leading term depends only on derivatives at the endpoints. For a periodic function they cancel, and so do all the higher Euler–Maclaurin terms $h^{2k}(f^{(2k-1)}(b)-f^{(2k-1)}(a))$, consistent with @thm-trapezoid-periodic-aliasing.

::: {#exm-trapezoid-periodic-vs-not .example name="Two integrands"}

For the periodic $f(x)=e^{\cos x}$ on $[0,2\pi]$ the trapezoidal error is $3.5\times10^{-2}$ with $N=4$, $1.3\times10^{-6}$ with $N=8$ and at the level of rounding ($10^{-15}$) with $N=16$. For $f(x)=e^x$ on $[0,1]$ it is $8.9\times10^{-3}$ at $N=4$ and falls by a factor $4$ each time $N$ doubles, still $3.5\times10^{-5}$ at $N=64$, in agreement with $\tfrac{h^2}{12}(e-1)$.

:::

::: {#fig-trapezoidal-rule-convergence-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.4cm, y=0.36cm]
\draw[->, faint] (0.8,0.8) -- (6.4,0.8) node[lab, right] {$\log_2N$};
\draw[->, faint] (0.8,0.8) -- (0.8,-16) node[lab, below] {$\log_{10}\lvert\text{error}\rvert$};
\foreach \x in {1,...,6} {\draw[faint] (\x,0.65) -- (\x,0.95); \node[tick, above] at (\x,0.95) {$\x$};}
\foreach \y in {-4,-8,-12} {\draw[faint] (0.76,\y) -- (0.84,\y); \node[tick, left] at (0.76,\y) {$\y$};}
\draw[hl] plot coordinates {(1,0.24) (2,-1.46) (3,-5.90) (4,-15.05) (5,-15.05) (6,-15.05)};
\draw[emph] plot coordinates {(1,-1.45) (2,-2.05) (3,-2.65) (4,-3.25) (5,-3.85) (6,-4.46)};
\node[lab] at (5.0,-2.7) {$e^x$ on $[0,1]$: slope $-2$};
\node[lab] at (4.9,-13.6) {$e^{\cos x}$, periodic};
\end{tikzpicture}
\end{center}
```

Trapezoidal-rule errors in @exm-trapezoid-periodic-vs-not. For the non-periodic integrand the error falls like $N^{-2}$ (a straight line of slope $-2\log_{10}2$ per doubling); for the periodic analytic integrand it falls exponentially, the number of correct digits roughly doubling with $N$, until it hits machine precision at $N=16$.

:::

::: {#fig-trapezoidal-rule-convergence-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm, y=0.9cm]
\draw[->, faint] (-0.2,0) -- (6.7,0) node[lab, right] {$x$};
\draw[emph, domain=0:6.283, samples=80] plot (\x,{sin(3*\x r)});
\foreach \k in {0,1,2,3} {\fill[accent] ({\k*6.283/3},0) circle (2pt);}
\draw[faint, domain=0:6.283, samples=40] plot (\x,{0});
\node[note] at (3.1,-1.4) {$\sin3x$ sampled at $N=3$ points looks like $0$};
\end{tikzpicture}
\end{center}
```

Aliasing: on a grid of $N$ points the mode $e^{iNx}$ is indistinguishable from the constant $1$ (here the imaginary part $\sin3x$ for $N=3$ vanishes at every node). The trapezoidal error consists exactly of such aliased modes, which are tiny for smooth periodic $f$.

:::
