---
title: "Adjoints, Orthogonal and Unitary Maps"
sources: [camib-la-8]
requires: [math/linear-algebra/inner-product-spaces/gram-schmidt-and-orthogonal-complements]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 8.3, in our own wording; examples ours; proofs written out in steps. MIT 18.06 defines orthogonal, Hermitian and unitary matrices (def-orthogonal-matrix, def-hermitian-unitary); the map versions here carry generalizes=. -->

Throughout, $V$ and $W$ are finite-dimensional inner product spaces over $F=\mathbb R$ or $\mathbb C$.

::: {#lem-riesz-finite-dimensional .lemma name="Functionals are inner products"}

For every linear functional $\theta\in V^*$ there is exactly one $u\in V$ with $\theta(v)=\langle v,u\rangle$ for all $v$.

:::

::: {.proof}

1. Existence: take an orthonormal basis $e_1,\dots,e_n$ (@cor-orthonormal-basis-exists) and $u=\sum_i\overline{\theta(e_i)}\,e_i$. Then $\langle e_j,u\rangle=\theta(e_j)$ for each $j$, and both sides are linear in $v$, so they agree everywhere (@thm-linear-map-from-basis).

2. Uniqueness: if $\langle v,u\rangle=\langle v,u'\rangle$ for all $v$, take $v=u-u'$: $\lVert u-u'\rVert^2=0$.

:::

In the real case $u\mapsto\langle\cdot,u\rangle$ is an isomorphism $V\to V^*$ that needs no basis; in the complex case it is conjugate-linear.

::: {#def-adjoint .definition name="Adjoint, self-adjoint"}

The *adjoint* of a linear map $\alpha:V\to W$ is the map $\alpha^*:W\to V$ with
$$\langle\alpha v,w\rangle=\langle v,\alpha^*w\rangle\qquad\text{for all }v\in V,\ w\in W.$$
$\alpha\in\operatorname{End}(V)$ is *self-adjoint* if $\alpha^*=\alpha$ (*symmetric* in the real case, *Hermitian* in the complex case).

:::

::: {#thm-adjoint-exists .theorem name="The adjoint exists and is the conjugate transpose"}

Every linear $\alpha:V\to W$ has a unique adjoint, which is linear. If $\mathcal B$ and $\mathcal C$ are orthonormal bases of $V$ and $W$ and $A=[\alpha]_{\mathcal B,\mathcal C}$, then
$$[\alpha^*]_{\mathcal C,\mathcal B}=A^{\mathsf H}=\bar A^{\mathsf T}.$$
So $\alpha$ is self-adjoint exactly when its matrix in an orthonormal basis is symmetric (real) or Hermitian (complex).

:::

::: {.proof}

1. For fixed $w$, $v\mapsto\langle\alpha v,w\rangle$ is a linear functional, so by @lem-riesz-finite-dimensional there is a unique vector $\alpha^*w$ with $\langle\alpha v,w\rangle=\langle v,\alpha^*w\rangle$.

2. Linearity: $\langle v,\alpha^*(\lambda w+\mu w')\rangle=\langle\alpha v,\lambda w+\mu w'\rangle=\bar\lambda\langle\alpha v,w\rangle+\bar\mu\langle\alpha v,w'\rangle=\langle v,\lambda\alpha^*w+\mu\alpha^*w'\rangle$ for all $v$; uniqueness in @lem-riesz-finite-dimensional gives $\alpha^*(\lambda w+\mu w')=\lambda\alpha^*w+\mu\alpha^*w'$.

3. Matrix: by @prp-parseval the $(i,j)$ entry of $[\alpha^*]$ is $\langle\alpha^*f_j,e_i\rangle=\overline{\langle e_i,\alpha^*f_j\rangle}=\overline{\langle\alpha e_i,f_j\rangle}=\bar a_{ji}$.

:::

Under the identification of @lem-riesz-finite-dimensional the adjoint is the dual map $\alpha'$ (@def-dual-map); in the real case @thm-dual-map-matrix and @thm-adjoint-exists say the same thing. Directly from the definition: $(\alpha\beta)^*=\beta^*\alpha^*$, $\alpha^{**}=\alpha$, $(\lambda\alpha)^*=\bar\lambda\alpha^*$. In orthonormal bases only: in a basis that is not orthonormal the matrix of $\alpha^*$ is not $A^{\mathsf H}$.

::: {#def-orthogonal-unitary-map .definition name="Orthogonal and unitary maps" generalizes="def-orthogonal-matrix"}

$\alpha\in\operatorname{End}(V)$ is an *isometry* if $\langle\alpha v,\alpha w\rangle=\langle v,w\rangle$ for all $v,w\in V$; it is called *orthogonal* if $V$ is real and *unitary* if $V$ is complex. The isometries form the *orthogonal group* $O(V)$, respectively the *unitary group* $U(V)$.

:::

::: {#thm-isometry-characterisations .theorem name="Characterisations of isometries" generalizes="prp-orthonormal-columns-preserve-length"}

For $\alpha\in\operatorname{End}(V)$ the following are equivalent:

1. $\alpha$ is an isometry;
2. $\lVert\alpha v\rVert=\lVert v\rVert$ for all $v$;
3. $\alpha^*\alpha=\iota$, that is, $\alpha$ is invertible with $\alpha^{-1}=\alpha^*$;
4. $\alpha$ maps some (equivalently, every) orthonormal basis to an orthonormal basis;
5. in an orthonormal basis, $[\alpha]$ satisfies $A^{\mathsf T}A=I$ (real) or $A^{\mathsf H}A=I$ (complex).

:::

::: {.proof}

1. (1)⇒(2): take $w=v$.

2. (2)⇒(1): the inner product is determined by the norm through polarization (@prp-polarization-identity in the real case, @prp-hermitian-polarization in the complex case), applied to the forms $\langle\alpha v,\alpha w\rangle$ and $\langle v,w\rangle$.

3. (1)⇔(3): $\langle\alpha v,\alpha w\rangle=\langle\alpha^*\alpha v,w\rangle$, which equals $\langle v,w\rangle$ for all $v,w$ iff $\alpha^*\alpha v=v$ for all $v$ (by the uniqueness in @lem-riesz-finite-dimensional). Then $\alpha$ is injective, hence invertible (@cor-injective-iff-surjective), with inverse $\alpha^*$.

4. (1)⇒(4): $\langle\alpha e_i,\alpha e_j\rangle=\delta_{ij}$, and $n$ orthonormal vectors form a basis.

5. (4)⇒(1): if $e_i$ and $\alpha e_i$ are both orthonormal bases and $v=\sum\lambda_ie_i$, $w=\sum\mu_ie_i$, then by @prp-parseval $\langle\alpha v,\alpha w\rangle=\sum\lambda_i\bar\mu_i=\langle v,w\rangle$.

6. (3)⇔(5): by @thm-adjoint-exists, $[\alpha^*\alpha]=A^{\mathsf H}A$ in an orthonormal basis.

:::

So, once an orthonormal basis $e_1,\dots,e_n$ is fixed, $\alpha\mapsto(\alpha e_1,\dots,\alpha e_n)$ is a bijection between $O(V)$ (or $U(V)$) and the set of orthonormal bases of $V$; and $O(V)\cong O(n)=\{A\in\operatorname{Mat}_n(\mathbb R):A^{\mathsf T}A=I\}$, $U(V)\cong U(n)=\{A\in\operatorname{Mat}_n(\mathbb C):A^{\mathsf H}A=I\}$. Taking determinants, $\det A=\pm1$ for $A\in O(n)$ and $\lvert\det A\rvert=1$ for $A\in U(n)$.

::: {#exm-isometries .example name="Isometries of the plane"}

The matrices in $O(2)$ have orthonormal columns: the first is $(\cos\theta,\sin\theta)^{\mathsf T}$ and the second is $\pm(-\sin\theta,\cos\theta)^{\mathsf T}$. With $+$ this is the rotation by $\theta$ ($\det=1$); with $-$ it is $\begin{bmatrix}\cos\theta&\sin\theta\\\sin\theta&-\cos\theta\end{bmatrix}$, the reflection in the line at angle $\theta/2$ ($\det=-1$). On $\mathbb C^1$, the unitary maps are multiplication by $e^{i\phi}$.

:::

::: {#fig-adjoints-and-isometries-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[xshift=0cm]
\draw[->, faint] (-0.4,0) -- (1.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.4) -- (0,1.6) node[lab, above] {$y$};
\draw[->, faint] (0,0) -- (1.2,0) node[lab, tick, below] {$e_1$};
\draw[->, faint] (0,0) -- (0,1.2) node[lab, tick, left] {$e_2$};
\draw[->, hl] (0,0) -- (0.600,1.039) node[lab, above right] {$Ae_1$};
\draw[->, emph] (0,0) -- (-1.039,0.600) node[lab, left] {$Ae_2$};

\node[lab, below] at (0.6,-0.9) {rotation, $\det=1$};
\end{scope}
\begin{scope}[xshift=4cm]
\draw[->, faint] (-0.4,0) -- (1.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.4) -- (0,1.6) node[lab, above] {$y$};
\draw[->, faint] (0,0) -- (1.2,0) node[lab, tick, below] {$e_1$};
\draw[->, faint] (0,0) -- (0,1.2) node[lab, tick, left] {$e_2$};
\draw[->, hl] (0,0) -- (0.600,1.039) node[lab, above right] {$Ae_1$};
\draw[->, emph] (0,0) -- (1.039,-0.600) node[lab, left] {$Ae_2$};
\draw[dashed] (-0.7,-0.404) -- (1.6,0.924) node[lab, right] {angle $\theta/2$};
\node[lab, below] at (0.6,-0.9) {reflection, $\det=-1$};
\end{scope}
\end{tikzpicture}
\end{center}
```

The two kinds of $2\times2$ orthogonal matrix, here with $\theta=60^\circ$: both keep the columns orthonormal; the rotation keeps the order of $e_1,e_2$, the reflection in the dashed line reverses it.

:::
