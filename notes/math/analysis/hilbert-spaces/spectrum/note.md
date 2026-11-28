---
title: "The Spectrum of a Bounded Operator"
sources: [camii-lan-4, camii-lans-4]
requires: [math/analysis/hilbert-spaces/riesz-representation, math/analysis/banach-spaces/hahn-banach, math/analysis/banach-spaces/open-mapping]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Linear Analysis (lecture notes), Section 4.5, and Example Sheet 4 (questions 3-7), in our own wording; proofs written out in steps. Liouville's theorem for scalar entire functions is taken from complex analysis and not proved here. -->

For a matrix the spectrum is the set of eigenvalues. For an operator on an infinite-dimensional space, $T-\lambda I$ can fail to be invertible without having a kernel, so the spectrum is larger than the set of eigenvalues.

::: {#def-spectrum .definition name="Spectrum, resolvent, point and approximate point spectrum"}

Let $X$ be a complex Banach space and $T\in B(X)$. The *resolvent set* is $\rho(T)=\{\lambda\in\mathbb C:T-\lambda I\text{ is invertible in }B(X)\}$ and the *spectrum* is $\sigma(T)=\mathbb C\setminus\rho(T)$. For $\lambda\in\rho(T)$ the *resolvent* is $R(\lambda)=(T-\lambda I)^{-1}$. The *point spectrum* $\sigma_p(T)$ is the set of eigenvalues ($\ker(T-\lambda I)\ne0$), and the *approximate point spectrum* $\sigma_{ap}(T)$ is the set of $\lambda$ for which there are unit vectors $x_n$ with $\|(T-\lambda)x_n\|\to0$ (approximate eigenvalues). Then $\sigma_p(T)\subseteq\sigma_{ap}(T)\subseteq\sigma(T)$.

:::

::: {#exm-shift-spectrum .example name="The shift operators"}

On $\ell^2$ let $S(x_1,x_2,\dots)=(0,x_1,x_2,\dots)$ (right shift) and $S^*(x_1,x_2,\dots)=(x_2,x_3,\dots)$ (left shift). $S$ has no eigenvalues. For $|\lambda|<1$, $x=(1,\lambda,\lambda^2,\dots)\in\ell^2$ satisfies $S^*x=\lambda x$, so $\sigma_p(S^*)\supseteq\{|\lambda|<1\}$. By @prp-adjoint-spectrum the spectrum of $S$ contains the open unit disc, and by @prp-spectrum-compact it is closed and contained in $\{|\lambda|\le\|S\|\}=\{|\lambda|\le1\}$. So $\sigma(S)=\{|\lambda|\le1\}$. On $\ell^2(\mathbb Z)$ the bilateral shift $Te_n=e_{n+1}$ is unitary with $\sigma(T)=\{|\lambda|=1\}$, with $\sigma_p(T)=\emptyset$ and $\sigma_{ap}(T)=\sigma(T)$.

:::

::: {#lem-neumann .lemma name="Neumann series"}

If $\|A\|<1$ then $I-A$ is invertible with $(I-A)^{-1}=\sum_{n\ge0}A^n$ and $\|(I-A)^{-1}\|\le(1-\|A\|)^{-1}$. If $S$ is invertible and $\|A\|<\|S^{-1}\|^{-1}$ then $S-A$ is invertible too.

:::

::: {.proof}

1. $\|A^n\|\le\|A\|^n$, so the series converges absolutely in the Banach space $B(X)$ (@thm-operator-space-complete).

2. $(I-A)\sum_{n\le N}A^n=I-A^{N+1}\to I$, and similarly on the other side. So the sum is the inverse.

3. For the second claim, $S-A=S(I-S^{-1}A)$ with $\|S^{-1}A\|<1$.

:::

::: {#prp-spectrum-compact .proposition name="The spectrum is closed and bounded"}

For $T\in B(X)$, $\sigma(T)$ is a compact subset of $\{|\lambda|\le\|T\|\}$.

:::

::: {.proof}

1. If $|\lambda|>\|T\|$ then $T-\lambda=-\lambda(I-T/\lambda)$ is invertible by @lem-neumann, so $\sigma(T)\subseteq\{|\lambda|\le\|T\|\}$.

2. If $\lambda_0\in\rho(T)$ and $|\lambda-\lambda_0|<\|R(\lambda_0)\|^{-1}$, then $T-\lambda=(T-\lambda_0)-(\lambda-\lambda_0)I$ is invertible by the second part of @lem-neumann. So $\rho(T)$ is open and $\sigma(T)$ is closed.

:::

::: {#fig-spectrum-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-3.2,0) -- (3.4,0); \draw[->, faint] (0,-3) -- (0,3.2);
\draw[faint, dashed] (0,0) circle (2.8); \node[lab] at (2.2,2.2) {$|\lambda|=\|T\|$};
\draw[regionA] (-0.6,0.4) .. controls (0.5,1.9) and (1.7,1.2) .. (1.4,-0.2) .. controls (1.2,-1.3) and (-0.5,-1.5) .. (-0.6,0.4);
\node[lab] at (0.5,0) {$\sigma(T)$};
\end{tikzpicture}
\end{center}
```

The spectrum is a compact subset of the disc of radius $\|T\|$.

:::

::: {#thm-spectrum-nonempty .theorem name="The spectrum is non-empty"}

If $X\ne0$ is a complex Banach space and $T\in B(X)$, then $\sigma(T)\ne\emptyset$.

:::

::: {.proof}

1. Suppose $\sigma(T)=\emptyset$. For every $\varphi\in B(X)^*$ the function $f(\lambda)=\varphi(R(\lambda))$ is defined on $\mathbb C$.

2. *It is entire.* For $\lambda,\mu\in\rho(T)$ the resolvent identity $R(\lambda)-R(\mu)=(\lambda-\mu)R(\lambda)R(\mu)$ holds, and $R$ is continuous (@lem-neumann), so $R(\mu)\to R(\lambda)$ as $\mu\to\lambda$ and $\frac{R(\mu)-R(\lambda)}{\mu-\lambda}\to R(\lambda)^2$. Hence $f$ is complex differentiable everywhere.

3. *It is bounded and tends to $0$.* For $|\lambda|>2\|T\|$, $R(\lambda)=-\lambda^{-1}(I-T/\lambda)^{-1}$ has $\|R(\lambda)\|\le|\lambda|^{-1}\cdot2\to0$. So $f(\lambda)\to0$ as $|\lambda|\to\infty$, and $f$ is bounded on the compact remainder by continuity.

4. By Liouville's theorem $f$ is constant, hence $0$. This holds for every $\varphi$, so by the Hahn–Banach theorem (@cor-hahn-banach-separates) applied in $B(X)$, $R(\lambda)=0$. But $R(\lambda)$ is invertible, contradiction since $X\ne0$.

:::

::: {#prp-adjoint-spectrum .proposition name="Spectrum of the adjoint on a Hilbert space"}

For $T\in B(H)$ on a complex Hilbert space, $\sigma(T^*)=\{\bar\lambda:\lambda\in\sigma(T)\}$. If $T$ is unitary, $\sigma(T)\subseteq\{|\lambda|=1\}$. If $T$ is self-adjoint, $\sigma(T)\subseteq\mathbb R$.

:::

::: {.proof}

1. $T-\lambda$ is invertible iff $(T-\lambda)^*=T^*-\bar\lambda$ is (invert the adjoint of the inverse).

2. Unitary: $\|T\|=\|T^{-1}\|=1$, so $\sigma(T)\subseteq\{|\lambda|\le1\}$ and for $\lambda\in\sigma(T)$, $\lambda^{-1}\in\sigma(T^{-1})\subseteq\{|\mu|\le1\}$ (since $T-\lambda=-\lambda T(T^{-1}-\lambda^{-1})$), so $|\lambda|\ge1$.

3. Self-adjoint: $T$ is normal, so $\sigma(T)=\sigma_{ap}(T)$ by @prp-normal-spectrum. If $\|(T-\lambda)x_n\|\to0$ for unit $x_n$ then $\langle Tx_n,x_n\rangle-\lambda\to0$, and $\langle Tx_n,x_n\rangle$ is real since $T=T^*$, so $\lambda\in\mathbb R$ as a limit of reals.

:::

::: {#prp-normal-spectrum .proposition name="For normal operators the spectrum is the approximate point spectrum"}

If $T\in B(H)$ is normal, then $\sigma(T)=\sigma_{ap}(T)$, and $\ker(T-\lambda)=\ker(T^*-\bar\lambda)$.

:::

::: {.proof}

1. $T-\lambda$ is normal for every $\lambda$, so by @prp-normal-norm, $\|(T-\lambda)x\|=\|(T^*-\bar\lambda)x\|$. This gives the equality of kernels.

2. If $\lambda\notin\sigma_{ap}(T)$ there is $c>0$ with $\|(T-\lambda)x\|\ge c\|x\|$ for all $x$. So $T-\lambda$ is injective, and its range is closed (an image sequence that is Cauchy has a Cauchy preimage sequence). The range is dense: its orthogonal complement is $\ker(T^*-\bar\lambda)=\ker(T-\lambda)=0$. So $T-\lambda$ is a bijection, with bounded inverse by the inverse mapping theorem or directly from the bound. Hence $\lambda\in\rho(T)$.

3. Conversely $\sigma_{ap}\subseteq\sigma$, always.

:::
