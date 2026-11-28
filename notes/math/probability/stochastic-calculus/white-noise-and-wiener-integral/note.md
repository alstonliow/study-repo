---
title: "Gaussian White Noise and the Wiener Integral"
sources: [camiii-sc-0]
requires: [math/probability/martingales/lp-and-l1-martingale-convergence]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Stochastic Calculus and Applications (lecture notes), Section 0, in our own wording; proofs written out in steps. -->

The equation $\dot x=F(x)+\eta$ with a noise $\eta$ that is independent at distinct times has no classical meaning, because such a noise is not a function. Integrating it in time, however, gives a perfectly good Gaussian object, and this is the simplest case of a stochastic integral.

::: {#def-gaussian-space .definition name="Gaussian space"}

A *Gaussian space* is a closed linear subspace $S\subseteq L^2(\Omega,\mathcal F,\Pr)$ in which every element is a centred Gaussian random variable.

:::

::: {#prp-gaussian-isometry .proposition name="Isometry from a Hilbert space onto a Gaussian space"}

For every separable Hilbert space $H$ there are a probability space and a Gaussian space $S$ with a linear isometry $I:H\to S$. Thus $I(f)\sim N\big(0,\lVert f\rVert_H^2\big)$ and
$$E[I(f)I(g)]=\langle f,g\rangle_H .$$

:::

::: {.proof}

1. Choose an orthonormal basis $(e_i)_{i\ge1}$ of $H$ and a probability space carrying independent $X_i\sim N(0,1)$.

2. Send $e_i\mapsto X_i$ and extend by linearity and continuity. Linear combinations of independent centred Gaussians are centred Gaussian, and $L^2$-limits of centred Gaussians are centred Gaussian, so the image is a Gaussian space; the map preserves inner products because the $X_i$ are orthonormal in $L^2$.

:::

::: {#def-white-noise .definition name="Gaussian white noise"}

A *Gaussian white noise* on $\mathbb R_+$ is an isometry $\mathrm{WN}:L^2(\mathbb R_+)\to S$ into a Gaussian space. For a set $A$ write $\mathrm{WN}(A)=\mathrm{WN}(\mathbf 1_A)$.

:::

::: {#fig-white-noise-and-wiener-integral-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (H) at (0,0) {$L^2(\mathbb R_+)$};
\node[box] (S) at (5,0) {Gaussian space $S\subseteq L^2(\Omega)$};
\draw[hl, ->] (H) -- node[above, lab] {$\mathrm{WN}$} (S);
\node[lab] at (0,-1.0) {$\mathbf 1_{(s,t]}$};
\node[lab] at (5,-1.0) {$B_t-B_s\sim N(0,t-s)$};
\draw[faint, ->] (0.9,-1.0) -- (3.1,-1.0);
\end{tikzpicture}
\end{center}
```

The white noise is an isometry from $L^2(\mathbb R_+)$ onto a Gaussian space; the indicator of $(s,t]$ is sent to the increment $B_t-B_s$ of a Brownian motion.

:::

::: {#prp-white-noise-properties .proposition name="White noise acts like a random measure, almost"}

1. If $|A|<\infty$ then $\mathrm{WN}(A)\sim N(0,|A|)$.

2. If $A,B$ are disjoint then $\mathrm{WN}(A)$ and $\mathrm{WN}(B)$ are independent (they are jointly Gaussian and uncorrelated).

3. If $A=\bigsqcup_{i\ge1}A_i$ with $|A|<\infty$, then $\mathrm{WN}(A)=\sum_i\mathrm{WN}(A_i)$ in $L^2$ and almost surely.

:::

::: {.proof}

Parts 1 and 2 follow from the isometry. For part 3:

1. $M_n=\sum_{i\le n}\mathrm{WN}(A_i)$ is a martingale in $n$, being a sum of independent centred variables.

2. $E[M_n^2]=\sum_{i\le n}|A_i|\le|A|$, so $M_n$ is bounded in $L^2$.

3. By martingale convergence in $L^2$ (@thm-lp-martingale-convergence), $M_n$ converges a.s. and in $L^2$; the limit is $\mathrm{WN}(A)$ because $\mathbf 1_{A}=\sum_i\mathbf 1_{A_i}$ in $L^2(\mathbb R_+)$.

:::

::: {#rmk-white-noise-not-a-measure .remark name="Why this is not yet a stochastic integral"}

The almost-sure convergence in part 3 holds off a null set that depends on the sequence $(A_i)$. There is no single null set outside which $A\mapsto\mathrm{WN}(A)$ is a signed measure, so $\int f\,d\mathrm{WN}$ cannot be a Lebesgue integral. Setting $B_t=\mathrm{WN}([0,t])$ gives a centred Gaussian process with $E[B_sB_t]=s\wedge t$ and independent increments, i.e. a Brownian motion except for path continuity (@def-brownian-motion; a good choice of basis makes the paths continuous). For a step function $f=\sum_if_i\mathbf 1_{(s_i,t_i]}$ one has $\mathrm{WN}(f)=\sum_if_i(B_{t_i}-B_{s_i})$, which suggests the notation $\int f\,dB$. Extending it beyond step functions is the work of the following notes: first for deterministic $f$ via the isometry above (the *Wiener integral*), then for random previsible integrands (@sec-math-probability-stochastic-calculus-ito-integral).

:::
