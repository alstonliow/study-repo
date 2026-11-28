---
title: "The Riesz Representation Theorem for Hilbert Spaces"
sources: [camii-lan-4]
requires: [math/analysis/hilbert-spaces/hilbert-spaces]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Linear Analysis (lecture notes), Section 4.2, in our own wording; proofs written out in steps. The finite-dimensional case is lem-riesz-finite-dimensional. -->

In a Hilbert space the dual is the space itself: every bounded functional is "take the inner product with a fixed vector". The abstract dual of the Banach-space chapter becomes concrete.

::: {#thm-riesz-representation .theorem name="Riesz representation theorem" generalizes="lem-riesz-finite-dimensional"}

Let $H$ be a Hilbert space. For every $\varphi\in H^*$ there is a unique $y\in H$ with $\varphi(x)=\langle x,y\rangle$ for all $x$, and $\|\varphi\|=\|y\|$. Thus $y\mapsto\langle\cdot,y\rangle$ is a conjugate-linear isometric bijection $H\to H^*$.

:::

::: {.proof}

1. *Uniqueness and norm.* If $\langle x,y\rangle=\langle x,y'\rangle$ for all $x$ then $y=y'$ (take $x=y-y'$). By Cauchy–Schwarz $\|\langle\cdot,y\rangle\|\le\|y\|$, and testing on $x=y$ gives equality.

2. *Existence.* If $\varphi=0$ take $y=0$. Otherwise $N=\ker\varphi$ is a proper closed subspace (kernel of a continuous functional), so $N^\perp\ne0$ by @thm-projection: pick $z\in N^\perp$ with $\|z\|=1$.

3. For any $x$, $\varphi(x)z-\varphi(z)x\in N$, since $\varphi$ of it is $\varphi(x)\varphi(z)-\varphi(z)\varphi(x)=0$. Take the inner product with $z$:
$$0=\varphi(x)\langle z,z\rangle-\varphi(z)\langle x,z\rangle,\qquad\text{so}\qquad\varphi(x)=\langle x,\overline{\varphi(z)}z\rangle.$$

4. Put $y=\overline{\varphi(z)}\,z$.

:::

::: {#fig-riesz-representation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[emph] (-2.5,0) -- (2.5,0) node[lab, right] {$\ker\varphi$};
\draw[hl, ->] (0,0) -- (0,1.8) node[lab, above] {$y$};
\draw[faint, dashed] (-2.5,1) -- (2.5,1); \node[lab, right] at (2.5,1) {$\varphi=\|y\|^2$};
\draw[faint] (0,0.15) -- (0.15,0.15) -- (0.15,0);
\end{tikzpicture}
\end{center}
```

$\varphi=\langle\cdot,y\rangle$: its kernel is the hyperplane orthogonal to $y$.

:::

::: {#cor-hilbert-reflexive .corollary name="Hilbert spaces are reflexive"}

Every Hilbert space is reflexive: $J:H\to H^{**}$ is onto.

:::

::: {.proof}

1. By @thm-riesz-representation, $H^*$ is itself a Hilbert space with the inner product $\langle\varphi_x,\varphi_y\rangle=\langle y,x\rangle$, and so $H^{**}$ is represented by $H^*$ again.

2. Let $\psi\in H^{**}$. Then $\varphi_x\mapsto\overline{\psi(\varphi_x)}$ is a bounded linear functional of $x\in H$ (the map $x\mapsto\varphi_x$ is conjugate-linear and isometric), so by the theorem there is $y\in H$ with $\overline{\psi(\varphi_x)}=\langle x,y\rangle$ for all $x$, i.e. $\psi(\varphi_x)=\langle y,x\rangle=\varphi_x(y)=(Jy)(\varphi_x)$. So $\psi=Jy$.

:::

::: {#def-hilbert-adjoint .definition name="Adjoint of a bounded operator on Hilbert spaces" related="def-adjoint"}

For $T\in B(H_1,H_2)$ there is a unique $T^*\in B(H_2,H_1)$ with $\langle Tx,y\rangle=\langle x,T^*y\rangle$ for all $x,y$, and $\|T^*\|=\|T\|$. It exists because for fixed $y$, $x\mapsto\langle Tx,y\rangle$ is a bounded functional, represented by a unique vector $T^*y$ (@thm-riesz-representation); linearity, boundedness and $\|T^*\|=\|T\|$ follow. Also $T^{**}=T$, $(ST)^*=T^*S^*$ and $\|T^*T\|=\|T\|^2$.

:::

::: {.proof}

1. $|\langle Tx,y\rangle|\le\|T\|\|x\|\|y\|$, so $\|T^*y\|\le\|T\|\|y\|$ and $\|T^*\|\le\|T\|$.

2. By symmetry $\|T\|=\|T^{**}\|\le\|T^*\|$.

3. $\|Tx\|^2=\langle T^*Tx,x\rangle\le\|T^*T\|\|x\|^2$ gives $\|T\|^2\le\|T^*T\|\le\|T^*\|\|T\|=\|T\|^2$.

:::

::: {#def-normal-operator .definition name="Self-adjoint, normal and unitary operators"}

$T\in B(H)$ is *self-adjoint* if $T=T^*$, *normal* if $TT^*=T^*T$, and *unitary* if $T^*T=TT^*=I$ (a surjective isometry). Self-adjoint and unitary operators are normal.

:::

::: {#prp-normal-norm .proposition name="Normal operators"}

$T\in B(H)$ is normal if and only if $\|Tx\|=\|T^*x\|$ for all $x$.

:::

::: {.proof}

1. $\|Tx\|^2-\|T^*x\|^2=\langle(T^*T-TT^*)x,x\rangle$.

2. $S=T^*T-TT^*$ is self-adjoint, so $\langle Sx,x\rangle=0$ for all $x$ iff $S=0$ (by the polarisation fact in @prp-polarisation-isometry in the complex case; in the real case use that $S$ is symmetric: $\langle S(x+y),x+y\rangle=2\langle Sx,y\rangle$).

:::
