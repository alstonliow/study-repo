---
title: "Independent Components Analysis"
sources: [cs229-13]
requires: [ai/unsupervised-learning/k-means, math/linear-algebra/matrix-methods/matrix-derivatives, math/calculus/multivariable/multiple-integrals/change-of-variables, math/probability/estimation/jointly-gaussian]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS229 lecture notes (version of 23 August 2026), Chapter 13 (the cocktail party problem, ambiguities of ICA, densities under linear transformations, the maximum likelihood ICA algorithm with a logistic source model), in our own wording. The proofs and the gradient derivation are written out in steps. -->

Two microphones in a room record two people talking at once; each recording is a different mixture of the two voices. *Independent components analysis* (ICA) recovers the voices from the recordings alone, using only the assumption that the speakers are independent.

::: {#def-ica .definition name="The ICA model"}

A *source* vector $\mathbf{s}\in\mathbb{R}^d$ has independent coordinates $s_1,\dots,s_d$. We observe $\mathbf{x}=A\mathbf{s}$ for an unknown invertible *mixing matrix* $A$, for many independent draws $\mathbf{x}^{(i)}=A\mathbf{s}^{(i)}$. The goal is the *unmixing matrix* $W=A^{-1}$, which recovers $\mathbf{s}^{(i)}=W\mathbf{x}^{(i)}$. Write $\mathbf{w}_j^{\mathsf T}$ for the $j$th row of $W$, so that $s_j=\mathbf{w}_j^{\mathsf T}\mathbf{x}$.

:::

::: {#prp-ica-ambiguities .proposition name="What ICA cannot recover"}

1. If $P$ is a permutation matrix and $D$ an invertible diagonal matrix, the sources $PD\mathbf{s}$ are independent and the mixing matrix $A(PD)^{-1}$ produces the same observations. So the order, the scale and the sign of the sources cannot be recovered.
2. If the sources are $N(\mathbf{0},I)$, then for every orthogonal $R$ the mixing matrices $A$ and $AR$ give observations with the same distribution. So Gaussian sources cannot be unmixed beyond a rotation.

:::

::: {.proof}

1. The coordinates of $PD\mathbf{s}$ are the $s_j$ scaled and reordered, still independent, and $A(PD)^{-1}(PD\mathbf{s})=A\mathbf{s}$.

2. With $\mathbf{s}\sim N(\mathbf{0},I)$, $A\mathbf{s}\sim N(\mathbf{0},AA^{\mathsf T})$ and $AR\mathbf{s}\sim N(\mathbf{0},ARR^{\mathsf T}A^{\mathsf T})=N(\mathbf{0},AA^{\mathsf T})$ (@thm-jointly-gaussian-properties). A Gaussian vector's distribution is determined by its mean and covariance, so the two observation distributions coincide.

:::

So ICA needs non-Gaussian sources, and recovers them up to order and scale; for audio, scale and sign hardly matter.

::: {#prp-density-linear-map .proposition name="Density under an invertible linear map"}

If $\mathbf{s}$ has density $p_{\mathbf{s}}$ and $\mathbf{x}=A\mathbf{s}$ with $A$ invertible, then with $W=A^{-1}$,

$$
p_{\mathbf{x}}(\mathbf{x})=p_{\mathbf{s}}(W\mathbf{x})\,\lvert\det W\rvert.
$$

:::

::: {.proof}

1. For a region $B$, $P(\mathbf{x}\in B)=P(\mathbf{s}\in WB)=\int_{WB}p_{\mathbf{s}}(\mathbf{u})\,d\mathbf{u}$.

2. Substitute $\mathbf{u}=W\mathbf{x}$, whose Jacobian determinant is $\det W$ (@thm-change-of-variables): the integral becomes $\int_Bp_{\mathbf{s}}(W\mathbf{x})\,\lvert\det W\rvert\,d\mathbf{x}$.

3. Since this holds for every $B$, the integrand is the density of $\mathbf{x}$.

:::

The factor $\lvert\det W\rvert$ is not optional: for $s$ uniform on $[0,1]$ and $x=2s$, the density of $x$ is $\tfrac12$ on $[0,2]$, not $1$.

::: {#def-ica-algorithm .definition name="Maximum likelihood ICA"}

Model each source with the density $g'$ of the logistic distribution, where $g(u)=1/(1+e^{-u})$ is the sigmoid (a heavy-tailed, non-Gaussian choice that works well for speech). By @prp-density-linear-map the log-likelihood of $W$ is

$$
\ell(W)=\sum_{i=1}^N\Bigl(\sum_{j=1}^d\log g'\bigl(\mathbf{w}_j^{\mathsf T}\mathbf{x}^{(i)}\bigr)+\log\lvert\det W\rvert\Bigr).
$$

*ICA by stochastic gradient ascent* updates, for one example $\mathbf{x}$ at a time,

$$
W\leftarrow W+\alpha\Bigl(\bigl(\mathbf 1-2g(W\mathbf{x})\bigr)\mathbf{x}^{\mathsf T}+(W^{\mathsf T})^{-1}\Bigr),
$$

where $g$ is applied entrywise and $\mathbf 1$ is the vector of ones. The recovered sources are $W\mathbf{x}^{(i)}$.

:::

::: {#thm-ica-gradient .theorem name="Gradient of the ICA log-likelihood"}

The term of $\ell$ for one example has gradient $\bigl(\mathbf 1-2g(W\mathbf{x})\bigr)\mathbf{x}^{\mathsf T}+(W^{\mathsf T})^{-1}$ with respect to $W$, so @def-ica-algorithm is stochastic gradient ascent on $\ell$.

:::

::: {.proof}

1. Since $g'=g(1-g)$ (@prp-logistic-function), $\log g'(u)=\log g(u)+\log(1-g(u))$, and its derivative is $\dfrac{g'}{g}-\dfrac{g'}{1-g}=(1-g)-g=1-2g(u)$.

2. The term $\log g'(\mathbf{w}_j^{\mathsf T}\mathbf{x})$ depends only on row $j$ of $W$, with gradient $\bigl(1-2g(\mathbf{w}_j^{\mathsf T}\mathbf{x})\bigr)\mathbf{x}^{\mathsf T}$ in that row. Stacking the rows gives $\bigl(\mathbf 1-2g(W\mathbf{x})\bigr)\mathbf{x}^{\mathsf T}$.

3. For $\log\lvert\det W\rvert$, let $\epsilon\in\{\pm1\}$ be the sign of $\det W$; near $W$ the function equals $\log(\epsilon\det W)$. As in part 3 of @prp-matrix-gradient-rules, $\partial\det W/\partial W_{ij}$ is the cofactor $C_{ij}$, so the partial derivative is $\epsilon C_{ij}/(\epsilon\det W)=C_{ij}/\det W=(W^{-1})_{ji}$. The gradient is $(W^{-1})^{\mathsf T}=(W^{\mathsf T})^{-1}$.

:::

::: {#rmk-ica-1 .remark name="Practical points" editor="No figure: unmixing shows only on long signals or large samples; a candidate is two mixed waveforms and their recovery, generated from simulated sources."}

The data are usually centred first, so that the sources have mean $0$ (the logistic density is symmetric about $0$). The examples should be visited in random order, since consecutive audio samples are not independent; this affects only the speed of convergence, not the objective. ICA contrasts with PCA (@def-principal-components): PCA finds orthogonal directions of large variance, which for a Gaussian is all there is to find, while ICA uses higher-order structure to find non-orthogonal independent directions.

:::
