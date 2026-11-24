---
title: "Derivatives of Eigenproblems"
sources: [mit18s096-13]
requires: [math/calculus/matrix/derivatives/hessians-and-bilinear-maps]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.S096 Matrix Calculus (IAP 2023), course notes Chapter 13 (differentiating on the unit sphere and on orthogonal matrices, the symmetric eigendecomposition, second derivatives of eigenvalues), in our own wording; the example is ours, checked in Python; proofs written out in steps. The first-order eigenvalue formula is @prp-eigenvalue-sensitivity (from MIT 18.335, derived there with an adjoint); here it is the diagonal of a matrix identity that also gives the eigenvectors. -->

Eigenvectors are normalized, and eigenvector matrices of symmetric matrices are orthogonal. Differentiating under such constraints means the change $dx$ is not arbitrary: it must keep the constraint to first order. With that one idea, the symmetric eigendecomposition $S=Q\Lambda Q^{\mathsf T}$ can be differentiated in a few lines.

::: {#prp-sphere-tangent-gradient .proposition name="Gradients on the unit sphere"}

On the unit sphere $x^{\mathsf T}x=1$, every first-order change satisfies $x^{\mathsf T}dx=0$. If $f$ is defined near the sphere with $df=g(x)^{\mathsf T}dx$, then for such $dx$

$$
df=\bigl((I-xx^{\mathsf T})g(x)\bigr)^{\mathsf T}dx,
$$

so $(I-xx^{\mathsf T})g(x)$, the component of $g$ tangent to the sphere, is the gradient of $f$ on the sphere.

:::

::: {.proof}

1. Differentiating $x^{\mathsf T}x=1$ gives $2x^{\mathsf T}dx=0$.

2. $I-xx^{\mathsf T}$ is the orthogonal projection onto the vectors perpendicular to $x$, so $(I-xx^{\mathsf T})dx=dx$ when $x^{\mathsf T}dx=0$.

3. Hence $df=g^{\mathsf T}dx=g^{\mathsf T}(I-xx^{\mathsf T})dx=\bigl((I-xx^{\mathsf T})g\bigr)^{\mathsf T}dx$, using that the projection is symmetric.

:::

::: {#fig-derivatives-of-eigenproblems-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.5cm, y=1.5cm]
\draw[set] (0,0) circle (1);
\draw[map] (0,0) -- (0.6,0.8) node[lab, above left] {$x$};
\draw[hl] (-0.2,1.1) -- (1.4,-0.1);
\draw[map, emph] (0.6,0.8) -- (1.6,1.4) node[lab, right] {$g$};
\draw[map, hl] (0.6,0.8) -- (1.0,0.5) node[lab, below right] {$(I-xx^{\mathsf T})g$};
\draw[faint, dashed] (1.6,1.4) -- (1.0,0.5);
\node[lab] at (-0.45,1.25) {$x^{\mathsf T}dx=0$};
\end{tikzpicture}
\end{center}
```

At a point $x$ of the sphere the allowed changes $dx$ form the tangent plane $x^{\mathsf T}dx=0$. Only the tangent part of the ordinary gradient $g$ changes $f$ along the sphere.

:::

::: {#prp-orthogonal-differential .proposition name="Differentials of orthogonal matrices"}

If $Q(t)$ is a differentiable family of orthogonal matrices, then $Q^{\mathsf T}dQ$ is antisymmetric: $(Q^{\mathsf T}dQ)^{\mathsf T}=-Q^{\mathsf T}dQ$. In particular its diagonal is zero.

:::

::: {.proof}

1. Differentiate $Q^{\mathsf T}Q=I$ with the product rule: $dQ^{\mathsf T}Q+Q^{\mathsf T}dQ=0$.

2. The first term is $(Q^{\mathsf T}dQ)^{\mathsf T}$, so $(Q^{\mathsf T}dQ)^{\mathsf T}=-Q^{\mathsf T}dQ$.

3. A diagonal entry $m_{ii}$ of an antisymmetric matrix satisfies $m_{ii}=-m_{ii}$, so it is $0$.

:::

The antisymmetric $n\times n$ matrices form a space of dimension $n(n-1)/2$, so this is the number of free directions in which an orthogonal matrix can move: one angle for $n=2$, three for $n=3$.

::: {#thm-symmetric-eigendecomposition-differential .theorem name="Differentiating the symmetric eigendecomposition" related="prp-eigenvalue-sensitivity"}

Let $S=Q\Lambda Q^{\mathsf T}$ be a differentiable family of real symmetric matrices with simple eigenvalues $\lambda_1,\dots,\lambda_n$ and orthonormal eigenvectors $q_1,\dots,q_n$ (the columns of $Q$). Then

$$
d\lambda_i=q_i^{\mathsf T}\,dS\,q_i,\qquad \nabla\lambda_i=q_iq_i^{\mathsf T},
$$

and for $i\neq j$

$$
(Q^{\mathsf T}dQ)_{ij}=\frac{q_i^{\mathsf T}\,dS\,q_j}{\lambda_j-\lambda_i},\qquad dQ=Q\,(Q^{\mathsf T}dQ).
$$

:::

::: {.proof}

1. By the product rule, $dS=dQ\,\Lambda Q^{\mathsf T}+Q\,d\Lambda\,Q^{\mathsf T}+Q\Lambda\,dQ^{\mathsf T}$.

2. Multiply by $Q^{\mathsf T}$ on the left and $Q$ on the right, and put $M=Q^{\mathsf T}dQ$, so $dQ^{\mathsf T}Q=M^{\mathsf T}=-M$ by @prp-orthogonal-differential:

   $$Q^{\mathsf T}dS\,Q=M\Lambda-\Lambda M+d\Lambda .$$

3. *Diagonal entries.* $(M\Lambda-\Lambda M)_{ii}=m_{ii}\lambda_i-\lambda_im_{ii}=0$, so $d\lambda_i=(Q^{\mathsf T}dS\,Q)_{ii}=q_i^{\mathsf T}dS\,q_i$.

4. Writing $q_i^{\mathsf T}dS\,q_i=\operatorname{tr}\bigl((q_iq_i^{\mathsf T})^{\mathsf T}dS\bigr)$ gives the Frobenius gradient $q_iq_i^{\mathsf T}$.

5. *Off-diagonal entries.* $(M\Lambda-\Lambda M)_{ij}=m_{ij}(\lambda_j-\lambda_i)$ and $d\Lambda$ is diagonal, so $m_{ij}=(Q^{\mathsf T}dS\,Q)_{ij}/(\lambda_j-\lambda_i)$, which needs $\lambda_i\neq\lambda_j$.

6. $M$ has zero diagonal, so $M$ is now known completely, and $dQ=QM$ since $Q$ is orthogonal.

:::

::: {#cor-eigenvalue-second-derivative .corollary name="Second derivative of an eigenvalue along a line"}

Let $S(t)=\Lambda+tE$ with $\Lambda$ diagonal with simple entries and $E$ symmetric. At $t=0$,

$$
\frac{d^2\lambda_i}{dt^2}=2\sum_{k\neq i}\frac{E_{ik}^2}{\lambda_i-\lambda_k}.
$$

:::

::: {.proof}

1. By @thm-symmetric-eigendecomposition-differential, $\dfrac{d\lambda_i}{dt}=q_i^{\mathsf T}Eq_i$ for all $t$. Differentiate again with the product rule: $\dfrac{d^2\lambda_i}{dt^2}=2\,q_i^{\mathsf T}E\,\dfrac{dq_i}{dt}$, using that $E$ is symmetric and constant.

2. At $t=0$, $Q=I$ and $q_i=e_i$. Column $i$ of $dQ/dt=M$ has entries $m_{ki}=E_{ki}/(\lambda_i-\lambda_k)$ for $k\neq i$ and $m_{ii}=0$.

3. So $q_i^{\mathsf T}E\,\dfrac{dq_i}{dt}=\sum_{k\neq i}E_{ik}\dfrac{E_{ki}}{\lambda_i-\lambda_k}$, and $E_{ik}=E_{ki}$.

:::

::: {#exm-derivatives-of-eigenproblems-1 .example name="Two eigenvalues repel"}

Let $S(t)=\begin{bmatrix}1&t\\t&3\end{bmatrix}$, so $\Lambda=\operatorname{diag}(1,3)$ and $E=\begin{bmatrix}0&1\\1&0\end{bmatrix}$. The eigenvalues are $\lambda_{1,2}(t)=2\mp\sqrt{1+t^2}$.

1. At $t=0$, $d\lambda_1/dt=e_1^{\mathsf T}Ee_1=0$, matching $\lambda_1'(0)=-t/\sqrt{1+t^2}\big|_0=0$.

2. @cor-eigenvalue-second-derivative gives $\lambda_1''(0)=2\cdot1^2/(1-3)=-1$ and $\lambda_2''(0)=+1$. Directly, $\lambda_1(t)=1-\tfrac12t^2+O(t^4)$.

3. The eigenvector changes by $(Q^{\mathsf T}dQ)_{21}=E_{21}/(\lambda_1-\lambda_2)\,dt=-\tfrac12dt$: $q_1$ tilts towards $-e_2$. Indeed the exact eigenvector is proportional to $\bigl(t,\,1-\sqrt{1+t^2}\bigr)$, whose second component divided by the first is $-\tfrac12t+O(t^3)$.

:::

::: {#fig-derivatives-of-eigenproblems-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.3cm, y=0.9cm]
\draw[->] (-2.2,0) -- (2.4,0) node[lab, right] {$t$};
\draw[->] (0,-0.4) -- (0,4.4) node[lab, above] {$\lambda$};
\draw[hl, domain=-2:2, samples=40] plot (\x, {2-sqrt(1+\x*\x)});
\draw[hl, domain=-2:2, samples=40] plot (\x, {2+sqrt(1+\x*\x)});
\draw[faint, dashed] (-2,1) -- (2,1); \draw[faint, dashed] (-2,3) -- (2,3);
\node[lab, left] at (0,1) {$1$}; \node[lab, left] at (0,3) {$3$};
\node[lab] at (1.6,0.2) {$\lambda_1(t)$}; \node[lab] at (1.6,3.6) {$\lambda_2(t)$};
\end{tikzpicture}
\end{center}
```

The eigenvalues of $\begin{bmatrix}1&t\\t&3\end{bmatrix}$. Their first derivatives vanish at $t=0$, and the second derivatives have opposite signs: the coupling $E_{12}$ pushes the two eigenvalues apart, more strongly the closer they are.

:::
