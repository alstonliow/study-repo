---
title: "Randomized Matrix Multiplication"
sources: [mit18065-13]
requires: [math/linear-algebra/matrix-methods/matrix-norms]
status: draft
---

<!-- Added 2026-11-20 from MIT 18.065 (Spring 2018), Lecture 13 (video lecture and problem set; no written lecture notes), in our own wording; proofs written out in steps. Numbers checked by hand and with numpy. -->

For very large matrices an exact product may be too expensive, while an unbiased estimate with controlled variance is good enough. Columns times rows (@thm-four-ways-to-multiply) writes $AB$ as a sum of $n$ rank one pieces; sampling a few pieces, with the right probabilities, gives such an estimate. Here $A$ is $m\times n$ with columns $\mathbf{a}_1,\dots,\mathbf{a}_n$ and $B$ is $n\times p$ with rows $\mathbf{b}_1^{\mathsf T},\dots,\mathbf{b}_n^{\mathsf T}$, so $AB=\sum_k\mathbf{a}_k\mathbf{b}_k^{\mathsf T}$.

::: {#def-sampled-matrix-product .definition name="Sampled matrix product"}

Choose probabilities $p_1,\dots,p_n>0$ with $\sum p_k=1$. For $t=1,\dots,s$ independently draw an index $k_t$ with $\Pr(k_t=k)=p_k$, and return
$$C=\frac1s\sum_{t=1}^{s}\frac{\mathbf{a}_{k_t}\mathbf{b}_{k_t}^{\mathsf T}}{p_{k_t}} .$$

:::

::: {#fig-randomized-matrix-multiplication-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.0,0) rectangle (0.25,-1.0); \draw[cell frame] (0.35,0) rectangle (1.25,-0.25);
\node[lab, tick] at (0.6,-1.25) {$\mathbf a_1\mathbf b_1^{\mathsf T}$};
\node[lab] at (1.48,-0.5) {$+$};
\draw[cell frame] (1.7,0) rectangle (1.95,-1.0); \draw[cell frame] (2.05,0) rectangle (2.95,-0.25);
\node[lab, tick] at (2.3,-1.25) {$\mathbf a_2\mathbf b_2^{\mathsf T}$};
\node[lab] at (3.18,-0.5) {$+$};
\draw[hl cell] (3.4,0) rectangle (3.65,-1.0); \draw[hl cell] (3.75,0) rectangle (4.65,-0.25);
\node[lab, tick] at (4.0,-1.25) {$\mathbf a_3\mathbf b_3^{\mathsf T}$};
\node[lab] at (4.88,-0.5) {$+$};
\draw[cell frame] (5.1,0) rectangle (5.35,-1.0); \draw[cell frame] (5.45,0) rectangle (6.35,-0.25);
\node[lab, tick] at (5.70,-1.25) {$\mathbf a_4\mathbf b_4^{\mathsf T}$};
\node[lab, note, anchor=west, align=left] at (6.9,-0.5) {pick term $k$ with probability $p_k$,\\use $\frac1{p_k}\mathbf a_k\mathbf b_k^{\mathsf T}$; on average this is $AB$};
\end{tikzpicture}
\end{center}
```

$AB$ is a sum of column-times-row layers. Sampling only some layers (highlighted) and rescaling them gives an unbiased estimate of $AB$ at a fraction of the cost.

:::

```{=latex}
\begin{algorithm}
\caption{Sampled matrix product}
\begin{algorithmic}
\INPUT $A$ ($m\times n$), $B$ ($n\times p$), probabilities $p_1,\dots,p_n$, sample size $s$
\OUTPUT An unbiased estimate $C$ of $AB$
\STATE $C\gets 0$ \COMMENT{an $m\times p$ zero matrix}
\FOR{$t=1$ to $s$}
    \STATE draw $k$ with probability $p_k$
    \STATE $C\gets C+\mathbf{a}_k\mathbf{b}_k^{\mathsf T}/(s\,p_k)$
\ENDFOR
\RETURN $C$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-sampled-product-unbiased .theorem name="Mean and variance of the sampled product"}

$C$ is unbiased, $\operatorname{E}[C]=AB$, and
$$\operatorname{E}\lVert C-AB\rVert_F^2=\frac1s\Big(\sum_{k=1}^n\frac{\lVert\mathbf{a}_k\rVert^2\lVert\mathbf{b}_k\rVert^2}{p_k}-\lVert AB\rVert_F^2\Big).$$
The cost is $s$ outer products, $O(smp)$, instead of $O(nmp)$.

:::

::: {.proof}

1. One draw $X=\mathbf{a}_k\mathbf{b}_k^{\mathsf T}/p_k$ has $\operatorname{E}[X]=\sum_kp_k\,\mathbf{a}_k\mathbf{b}_k^{\mathsf T}/p_k=AB$. By linearity (@thm-linearity-of-expectation), $\operatorname{E}[C]=AB$.

2. $\lVert\mathbf{a}\mathbf{b}^{\mathsf T}\rVert_F=\lVert\mathbf{a}\rVert\lVert\mathbf{b}\rVert$ (a rank one matrix has the single singular value $\lVert\mathbf{a}\rVert\lVert\mathbf{b}\rVert$). So $\operatorname{E}\lVert X\rVert_F^2=\sum_kp_k\lVert\mathbf{a}_k\rVert^2\lVert\mathbf{b}_k\rVert^2/p_k^2$.

3. Entry by entry, $\operatorname{E}\lVert X-AB\rVert_F^2=\operatorname{E}\lVert X\rVert_F^2-\lVert AB\rVert_F^2$, the matrix form of $\operatorname{Var}=\operatorname{E}[X^2]-(\operatorname{E}X)^2$.

4. The $s$ draws are independent, so variances of the entries add; dividing the sum by $s$ divides the variance by $s$.

:::

::: {#thm-optimal-sampling-probabilities .theorem name="Best sampling probabilities"}

The variance in @thm-sampled-product-unbiased is smallest when
$$p_k=\frac{\lVert\mathbf{a}_k\rVert\,\lVert\mathbf{b}_k\rVert}{\sum_j\lVert\mathbf{a}_j\rVert\,\lVert\mathbf{b}_j\rVert},$$
and then $\sum_k\lVert\mathbf{a}_k\rVert^2\lVert\mathbf{b}_k\rVert^2/p_k=\big(\sum_k\lVert\mathbf{a}_k\rVert\lVert\mathbf{b}_k\rVert\big)^2$.

:::

::: {.proof}

1. Write $c_k=\lVert\mathbf{a}_k\rVert\lVert\mathbf{b}_k\rVert$. We minimise $\sum c_k^2/p_k$ subject to $\sum p_k=1$.

2. Cauchy–Schwarz: $\big(\sum c_k\big)^2=\big(\sum\frac{c_k}{\sqrt{p_k}}\sqrt{p_k}\big)^2\le\sum\frac{c_k^2}{p_k}\sum p_k=\sum\frac{c_k^2}{p_k}$.

3. Equality holds when $c_k/\sqrt{p_k}$ is proportional to $\sqrt{p_k}$, that is $p_k\propto c_k$. These $p_k$ give the value $(\sum c_k)^2$.

:::

::: {#exm-sampled-product .example name="Norm sampling beats uniform sampling"}

Take $A=\operatorname{diag}(1,3)$ and $B=I$, so $AB=A$ and $\lVert AB\rVert_F^2=10$. The products of norms are $c=(1,3)$. With one sample ($s=1$):

- uniform $p=(\frac12,\frac12)$: variance $2(1+9)-10=10$;
- optimal $p=(\frac14,\frac34)$: variance $(1+3)^2-10=6$.

:::

::: {#fig-randomized-matrix-multiplication-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, muted] (0,0) -- (3.4,0); \draw[->, muted] (0,0) -- (0,2.4) node[above, lab, tick] {variance};
\draw[cell, fill=accentLight] (0.4,0) rectangle (1.2,2.0); \node[lab, tick] at (0.8,2.2) {$10$}; \node[lab, tick, align=center] at (0.8,-0.35) {uniform\\$p=(\frac12,\frac12)$};
\draw[bar] (2.0,0) rectangle (2.8,1.2); \node[lab, tick] at (2.4,1.4) {$6$}; \node[lab, tick, align=center] at (2.4,-0.35) {by norms\\$p=(\frac14,\frac34)$};
\end{tikzpicture}
\end{center}
```

@exm-sampled-product with one sample: choosing the larger layer more often, in proportion to $\lVert\mathbf a_k\rVert\lVert\mathbf b_k\rVert$, lowers the variance from $10$ to $6$.

:::

::: {#fig-randomized-matrix-multiplication-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (0,0) -- (6.6,0) node[lab, right] {$s$};
\draw[->, faint] (0,0) -- (0,4.0) node[lab, above] {$\lVert C-AB\rVert_F$};
\draw[faint] (1.5,0.06) -- (1.5,-0.06) node[lab, below] {10};
\draw[faint] (3.0,0.06) -- (3.0,-0.06) node[lab, below] {20};
\draw[faint] (4.5,0.06) -- (4.5,-0.06) node[lab, below] {30};
\draw[faint] (6.0,0.06) -- (6.0,-0.06) node[lab, below] {40};
\draw[faint] (0.06,0.9) -- (-0.06,0.9) node[lab, left] {1};
\draw[faint] (0.06,1.8) -- (-0.06,1.8) node[lab, left] {2};
\draw[faint] (0.06,2.7) -- (-0.06,2.7) node[lab, left] {3};
\draw[faint] (0.06,3.6) -- (-0.06,3.6) node[lab, left] {4};
\draw[faint] (0.15,2.85) -- (0.3,2.01) -- (0.45,1.64) -- (0.6,1.42) -- (0.75,1.27) -- (0.90,1.16) -- (1.05,1.08) -- (1.2,1.01) -- (1.35,0.95) -- (1.5,0.9) -- (1.65,0.86) -- (1.80,0.82) -- (1.95,0.79) -- (2.1,0.76) -- (2.25,0.73) -- (2.4,0.71) -- (2.55,0.69) -- (2.70,0.67) -- (2.85,0.65) -- (3.0,0.64) -- (3.15,0.62) -- (3.3,0.61) -- (3.45,0.59) -- (3.60,0.58) -- (3.75,0.57) -- (3.9,0.56) -- (4.05,0.55) -- (4.2,0.54) -- (4.35,0.53) -- (4.5,0.52) -- (4.65,0.51) -- (4.8,0.50) -- (4.95,0.50) -- (5.1,0.49) -- (5.25,0.48) -- (5.40,0.47) -- (5.55,0.47) -- (5.7,0.46) -- (5.85,0.46) -- (6.0,0.45);
\fill[faint] (0.15,2.85) circle (1pt);
\fill[faint] (0.3,0.0) circle (1pt);
\fill[faint] (0.45,0.95) circle (1pt);
\fill[faint] (0.6,0.0) circle (1pt);
\fill[faint] (0.75,0.57) circle (1pt);
\fill[faint] (0.90,0.95) circle (1pt);
\fill[faint] (1.05,0.41) circle (1pt);
\fill[faint] (1.2,0.0) circle (1pt);
\fill[faint] (1.35,0.32) circle (1pt);
\fill[faint] (1.5,0.57) circle (1pt);
\fill[faint] (1.65,0.26) circle (1pt);
\fill[faint] (1.80,0.47) circle (1pt);
\fill[faint] (1.95,0.22) circle (1pt);
\fill[faint] (2.1,0.41) circle (1pt);
\fill[faint] (2.25,0.57) circle (1pt);
\fill[faint] (2.4,0.36) circle (1pt);
\fill[faint] (2.55,0.50) circle (1pt);
\fill[faint] (2.70,0.32) circle (1pt);
\fill[faint] (2.85,0.15) circle (1pt);
\fill[faint] (3.0,0.28) circle (1pt);
\fill[faint] (3.15,0.41) circle (1pt);
\fill[faint] (3.3,0.26) circle (1pt);
\fill[faint] (3.45,0.12) circle (1pt);
\fill[faint] (3.60,0.24) circle (1pt);
\fill[faint] (3.75,0.34) circle (1pt);
\fill[faint] (3.9,0.44) circle (1pt);
\fill[faint] (4.05,0.53) circle (1pt);
\fill[faint] (4.2,0.61) circle (1pt);
\fill[faint] (4.35,0.69) circle (1pt);
\fill[faint] (4.5,0.76) circle (1pt);
\fill[faint] (4.65,0.83) circle (1pt);
\fill[faint] (4.8,0.89) circle (1pt);
\fill[faint] (4.95,0.95) circle (1pt);
\fill[faint] (5.1,1.00) circle (1pt);
\fill[faint] (5.25,1.06) circle (1pt);
\fill[faint] (5.40,1.11) circle (1pt);
\fill[faint] (5.55,1.00) circle (1pt);
\fill[faint] (5.7,0.90) circle (1pt);
\fill[faint] (5.85,0.80) circle (1pt);
\fill[faint] (6.0,0.85) circle (1pt);
\draw[hl] (0.15,2.20) -- (0.3,1.56) -- (0.45,1.27) -- (0.6,1.10) -- (0.75,0.99) -- (0.90,0.9) -- (1.05,0.83) -- (1.2,0.78) -- (1.35,0.73) -- (1.5,0.70) -- (1.65,0.66) -- (1.80,0.64) -- (1.95,0.61) -- (2.1,0.59) -- (2.25,0.57) -- (2.4,0.55) -- (2.55,0.53) -- (2.70,0.52) -- (2.85,0.51) -- (3.0,0.49) -- (3.15,0.48) -- (3.3,0.47) -- (3.45,0.46) -- (3.60,0.45) -- (3.75,0.44) -- (3.9,0.43) -- (4.05,0.42) -- (4.2,0.42) -- (4.35,0.41) -- (4.5,0.40) -- (4.65,0.40) -- (4.8,0.39) -- (4.95,0.38) -- (5.1,0.38) -- (5.25,0.37) -- (5.40,0.37) -- (5.55,0.36) -- (5.7,0.36) -- (5.85,0.35) -- (6.0,0.35);
\fill[hl] (0.15,1.27) circle (1pt);
\fill[hl] (0.3,1.27) circle (1pt);
\fill[hl] (0.45,0.42) circle (1pt);
\fill[hl] (0.6,0.0) circle (1pt);
\fill[hl] (0.75,0.25) circle (1pt);
\fill[hl] (0.90,0.42) circle (1pt);
\fill[hl] (1.05,0.55) circle (1pt);
\fill[hl] (1.2,0.64) circle (1pt);
\fill[hl] (1.35,0.71) circle (1pt);
\fill[hl] (1.5,0.76) circle (1pt);
\fill[hl] (1.65,0.81) circle (1pt);
\fill[hl] (1.80,0.85) circle (1pt);
\fill[hl] (1.95,0.88) circle (1pt);
\fill[hl] (2.1,0.91) circle (1pt);
\fill[hl] (2.25,0.93) circle (1pt);
\fill[hl] (2.4,0.95) circle (1pt);
\fill[hl] (2.55,0.67) circle (1pt);
\fill[hl] (2.70,0.42) circle (1pt);
\fill[hl] (2.85,0.47) circle (1pt);
\fill[hl] (3.0,0.51) circle (1pt);
\fill[hl] (3.15,0.30) circle (1pt);
\fill[hl] (3.3,0.35) circle (1pt);
\fill[hl] (3.45,0.39) circle (1pt);
\fill[hl] (3.60,0.42) circle (1pt);
\fill[hl] (3.75,0.46) circle (1pt);
\fill[hl] (3.9,0.49) circle (1pt);
\fill[hl] (4.05,0.52) circle (1pt);
\fill[hl] (4.2,0.55) circle (1pt);
\fill[hl] (4.35,0.57) circle (1pt);
\fill[hl] (4.5,0.59) circle (1pt);
\fill[hl] (4.65,0.62) circle (1pt);
\fill[hl] (4.8,0.48) circle (1pt);
\fill[hl] (4.95,0.35) circle (1pt);
\fill[hl] (5.1,0.37) circle (1pt);
\fill[hl] (5.25,0.40) circle (1pt);
\fill[hl] (5.40,0.42) circle (1pt);
\fill[hl] (5.55,0.45) circle (1pt);
\fill[hl] (5.7,0.33) circle (1pt);
\fill[hl] (5.85,0.36) circle (1pt);
\fill[hl] (6.0,0.38) circle (1pt);
\draw[faint] (3.6,3.5) -- (4.1,3.5) node[lab, right] {uniform $p$};
\draw[hl] (3.6,3.1) -- (4.1,3.1) node[lab, right] {optimal $p$};
\end{tikzpicture}
\end{center}
```

The sampled product for $A=\operatorname{diag}(1,3)$, $B=I$. Curves: root-mean-square error $\sqrt{\text{variance}/s}$ after $s$ samples, $\sqrt{10/s}$ for uniform and $\sqrt{6/s}$ for norm-based probabilities. Dots: one simulated run of each.

:::

::: {#rmk-randomized-matrix-multiplication-1 .remark name="Randomized range finders"}

The same idea drives randomized SVD: multiply $A$ by a random $n\times(k+q)$ matrix $G$, orthonormalise $Y=AG$ to $Q$, and compute the SVD of the small matrix $Q^{\mathsf T}A$. When the singular values of $A$ decay fast (@sec-math-linear-algebra-matrix-methods-low-rank-approximation), $QQ^{\mathsf T}A$ is close to the best rank $k$ approximation with high probability.

:::
