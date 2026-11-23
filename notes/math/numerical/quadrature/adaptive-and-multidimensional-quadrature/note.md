---
title: "Adaptive and Multidimensional Quadrature"
sources: [mit18335-37]
requires: [math/numerical/quadrature/gaussian-quadrature, math/probability/continuous/central-limit-theorem]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 37 (adaptive and multidimensional quadrature), in our own wording; proofs written out in steps; the adaptive Simpson and Monte Carlo experiments were run in Python. -->

The rules so far use a fixed set of nodes and assume the integrand is smooth on the whole interval. Real integrands have endpoint singularities, kinks or sharp peaks, and real integrals are often over many dimensions. Adaptivity spends function evaluations where the error is, and in high dimensions random sampling beats any tensor-product rule.

::: {#def-adaptive-quadrature .definition name="Adaptive quadrature"}

Given a rule $Q$ and an error estimate $E$ for it (the difference between two rules of different accuracy on the same interval), recursively: compute $Q$ and $E$ on $[a,b]$; if $\lvert E\rvert\le\text{tol}$, accept; otherwise split $[a,b]$ into halves and apply the procedure to each with tolerance $\text{tol}/2$ (*local* strategy), or keep all intervals in a priority queue and always split the one with the largest estimated error until the total estimate is below tolerance (*global* strategy). Common pairs are Simpson's rule on $[a,b]$ versus on its two halves, and Gauss–Kronrod pairs, where a $(2n+1)$-point Kronrod rule reuses the $n$ Gauss nodes.

:::

```{=latex}
\begin{algorithm}
\caption{Adaptive Simpson quadrature $\mathrm{AS}(a,b,\text{tol})$}
\begin{algorithmic}
\INPUT $f$, interval $[a,b]$, tolerance
\STATE $m\gets(a+b)/2$; \quad $S\gets$ Simpson on $[a,b]$; \quad $S_2\gets$ Simpson on $[a,m]$ plus Simpson on $[m,b]$
\IF{$\lvert S_2-S\rvert\le15\,\text{tol}$}
    \STATE \textbf{return} $S_2+(S_2-S)/15$ \COMMENT{Richardson correction}
\ENDIF
\STATE \textbf{return} $\mathrm{AS}(a,m,\text{tol}/2)+\mathrm{AS}(m,b,\text{tol}/2)$
\end{algorithmic}
\end{algorithm}
```

::: {#prp-simpson-error-estimate .proposition name="Why the Simpson error estimate works"}

If $f\in C^4$ and $f^{(4)}$ is nearly constant on $[a,b]$ (true on short intervals), then with $S$ and $S_2$ as in the algorithm, $I-S_2\approx(S_2-S)/15$.

:::

::: {.proof}

1. Simpson's rule on an interval of length $h$ has error $-\tfrac{h^5}{2880}f^{(4)}(\xi)$ for some $\xi$ in it (a standard Taylor computation, analogous to @thm-trapezoid-nonperiodic).

2. With $f^{(4)}\approx c$ constant, $I-S\approx-\tfrac{c\,h^5}{2880}$ and $I-S_2\approx-2\cdot\tfrac{c(h/2)^5}{2880}=\tfrac1{16}(I-S)$.

3. Subtract: $S_2-S=(I-S)-(I-S_2)\approx15(I-S_2)$, which is the claim. Adding the estimate to $S_2$ gives a rule of higher order (Boole's rule).

:::

::: {#exm-adaptive-sqrt .example name="An endpoint singularity"}

$\int_0^1\sqrt x\,dx=\tfrac23$, but $\sqrt x$ has an infinite derivative at $0$, so Simpson's rule on a uniform grid converges only like $h^{3/2}$. Adaptive Simpson with tolerance $10^{-6}$ uses $105$ function values in $26$ intervals and achieves error $2\times10^{-8}$. Its intervals halve repeatedly towards $0$: the smallest is $[0,5\times10^{-7}]$. Uniform Simpson with the same $105$ values has error $8\times10^{-5}$.

:::

::: {#fig-adaptive-and-multidimensional-quadrature-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.6cm]
\draw[faint] (-6.5,0) -- (0.2,0);
\foreach \b in {-6.3,-6.0,-5.72,-5.42,-5.12,-4.82,-4.52,-4.21,-3.91,-3.61,-3.31,-3.01,-2.71,-2.41,-2.11,-1.81,-1.51,-1.2,-1.03,-0.9,-0.73,-0.6,-0.43,-0.3,-0.12,0} {\draw[hl] (\b,-0.15) -- (\b,0.15);}
\foreach \x in {-6,-4,-2,0} {\node[tick, below=5pt] at (\x,0) {$10^{\x}$};}
\node[note] at (-3,0.55) {right endpoints of the accepted intervals (log scale)};
\end{tikzpicture}
\end{center}
```

The $26$ intervals chosen by adaptive Simpson for $\sqrt x$ on $[0,1]$ in @exm-adaptive-sqrt, on a logarithmic axis: below $0.03$ each interval is half the previous one, a geometric grading towards the singularity at $0$; near $1$, where $\sqrt x$ is smooth, intervals of length $1/4$ suffice.

:::

::: {#prp-tensor-product-cost .proposition name="The curse of dimensionality"}

A tensor-product rule on $[0,1]^d$ built from a one-dimensional rule with $n$ nodes and error $O(n^{-p})$ uses $N=n^d$ nodes and has error $O(n^{-p})=O(N^{-p/d})$.

:::

::: {.proof}

1. The tensor rule is $\sum_{k_1,\dots,k_d}w_{k_1}\cdots w_{k_d}f(x_{k_1},\dots,x_{k_d})$, with $n^d$ terms.

2. Apply the one-dimensional rule in one variable at a time. Each application introduces an error $O(n^{-p})$ (uniformly, for $f$ smooth in all variables), and the remaining rules have positive weights summing to $1$, which do not amplify it (@prp-quadrature-conditioning). Summing the $d$ contributions gives $O(dn^{-p})$.

3. With $n=N^{1/d}$ the error is $O(N^{-p/d})$: for fixed accuracy the cost grows exponentially in $d$.

:::

::: {#thm-monte-carlo-rate .theorem name="Monte Carlo integration"}

Let $X_1,\dots,X_N$ be independent and uniform on $[0,1]^d$ and $f$ square-integrable with variance $\sigma^2=\int f^2-(\int f)^2$. The estimate $\hat I_N=\frac1N\sum_if(X_i)$ is unbiased with root-mean-square error $\sigma/\sqrt N$, whatever the dimension $d$.

:::

::: {.proof}

1. $\mathbb E f(X_i)=\int_{[0,1]^d}f=I$, so $\mathbb E\hat I_N=I$.

2. The $f(X_i)$ are independent with variance $\sigma^2$, so $\operatorname{Var}\hat I_N=\sigma^2/N$, and the RMS error is $\sqrt{\operatorname{Var}\hat I_N}=\sigma/\sqrt N$.

3. By the central limit theorem (@thm-central-limit-theorem), $\hat I_N-I$ is approximately normal, which gives error bars $\pm2\sigma/\sqrt N$ with $\sigma$ estimated from the samples.

:::

::: {#fig-adaptive-and-multidimensional-quadrature-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.2cm, y=1.0cm]
\draw[->, faint] (0.8,-0.8) -- (6.5,-0.8) node[lab, right] {$\log_{10}N$};
\draw[->, faint] (0.8,-0.8) -- (0.8,-4.4) node[lab, below] {$\log_{10}$ RMS error};
\foreach \x in {1,...,6} {\draw[faint] (\x,-0.86) -- (\x,-0.74); \node[tick, above] at (\x,-0.74) {$\x$};}
\foreach \y in {-2,-3,-4} {\draw[faint] (0.76,\y) -- (0.84,\y); \node[tick, left] at (0.76,\y) {$\y$};}
\draw[hl] plot coordinates {(1,-1.46) (2,-1.84) (3,-2.23) (4,-2.84) (5,-3.47) (6,-3.86)};
\foreach \p in {(1,-1.46),(2,-1.84),(3,-2.23),(4,-2.84),(5,-3.47),(6,-3.86)} {\fill[accent] \p circle (2pt);}
\draw[faint, dashed] (1,-1.2) -- (6,-3.7) node[lab, right] {slope $-\tfrac12$};
\end{tikzpicture}
\end{center}
```

Monte Carlo estimate of $\int_{[0,1]^5}e^{-\lvert\mathbf{x}\rvert^2}d\mathbf{x}$: the RMS error over $20$ repetitions falls like $N^{-1/2}$. A tensor-product Simpson rule with the same $10^6$ points would have only $16$ nodes per dimension.

:::

::: {#rmk-adaptive-and-multidimensional-quadrature-1 .remark name="Between the extremes"}

The $N^{-1/2}$ rate is slow but dimension-free, so Monte Carlo wins once $p/d<\tfrac12$. *Quasi-Monte Carlo* replaces random points by low-discrepancy sequences (Halton, Sobol) and achieves nearly $N^{-1}$ for smooth integrands of moderate dimension. *Sparse grids* (Smolyak) combine one-dimensional rules of different orders so that the cost grows like $N(\log N)^{d-1}$ instead of $n^d$. *Variance reduction* (importance sampling, control variates) lowers $\sigma$ in the Monte Carlo rate. Adaptive methods in several dimensions subdivide boxes, as in the one-dimensional @def-adaptive-quadrature, and work well up to perhaps $d\approx7$.

:::
