---
title: "Dual Maps and the Double Dual"
sources: [camib-la-3]
requires: [math/linear-algebra/duality/dual-spaces]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 3.2, in our own wording; examples ours; proofs written out in steps. The course writes the dual map as alpha*; here it is alpha' so that alpha* is free for the adjoint (meta/notation.md). -->

::: {#def-dual-map .definition name="Dual map"}

The *dual map* of a linear map $\alpha:V\to W$ is
$$\alpha':W^*\to V^*,\qquad \alpha'(\theta)=\theta\circ\alpha.$$

:::

::: {#fig-dual-maps-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab] (U) at (0,0) {$U$}; \node[lab] (V) at (2.6,0) {$V$}; \node[lab] (K) at (5.2,0) {$F$};
\draw[map] (U) -- node[lab, above] {$\alpha$} (V);
\draw[map] (V) -- node[lab, above] {$\theta\in V^*$} (K);
\draw[map, hl] (U) to[bend right=30] node[lab, below] {$\alpha'(\theta)=\theta\circ\alpha\in U^*$} (K);
\end{tikzpicture}
\end{center}
```

The dual map goes backwards: a functional $\theta$ on $V$ is pulled back along $\alpha$ to the functional $\theta\circ\alpha$ on $U$, so $\alpha':V^*\to U^*$.

:::

$\alpha'(\theta)$ is linear as a composition of linear maps, and $\alpha'$ is linear in $\theta$. Directly from the definition, $(\beta\alpha)'=\alpha'\beta'$ and $\iota'=\iota$; so the dual of an isomorphism is an isomorphism with $(\alpha^{-1})'=(\alpha')^{-1}$.

::: {#thm-dual-map-matrix .theorem name="The dual map is the transpose"}

Let $V,W$ have bases $\mathcal B,\mathcal C$, with dual bases $\mathcal B^*,\mathcal C^*$. Then
$$[\alpha']_{\mathcal C^*,\mathcal B^*}=\big([\alpha]_{\mathcal B,\mathcal C}\big)^{\mathsf T}.$$

:::

::: {.proof}

1. Let $A=[\alpha]_{\mathcal B,\mathcal C}$, so $\alpha(e_j)=\sum_ka_{kj}f_k$, and let $\eta_i\in\mathcal C^*$ be dual to $f_i$.

2. By @thm-dual-basis, $\alpha'(\eta_i)=\sum_j\alpha'(\eta_i)(e_j)\,\varepsilon_j$, and $\alpha'(\eta_i)(e_j)=\eta_i(\alpha(e_j))=a_{ij}$.

3. So column $i$ of $[\alpha']$ is $(a_{i1},\dots,a_{im})^{\mathsf T}$, row $i$ of $A$.

:::

::: {#fig-dual-maps-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,1.100) rectangle (0.550,1.650);
\node[lab] at (0.275,1.375) {$0$};
\draw[cell, fill=primaryLight] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$1$};
\draw[cell frame] (1.100,1.100) rectangle (1.650,1.650);
\node[lab] at (1.375,1.375) {$0$};
\draw[cell frame] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$0$};
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$0$};
\draw[cell, fill=primaryLight] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$2$};
\draw[cell frame] (0.000,-0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$0$};
\draw[cell frame] (0.550,-0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$0$};
\draw[cell frame] (1.100,-0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$0$};
\node[lab, note] at (0.825,-0.350) {$[D]$ on $1,t,t^2$};
\draw[->] (1.9,0.825) -- (2.9,0.825) node[midway, above, lab, note] {${}^{\mathsf T}$};
\draw[cell frame] (3.100,1.100) rectangle (3.650,1.650);
\node[lab] at (3.375,1.375) {$0$};
\draw[cell frame] (3.650,1.100) rectangle (4.200,1.650);
\node[lab] at (3.925,1.375) {$0$};
\draw[cell frame] (4.200,1.100) rectangle (4.750,1.650);
\node[lab] at (4.475,1.375) {$0$};
\draw[cell, fill=primaryLight] (3.100,0.550) rectangle (3.650,1.100);
\node[lab] at (3.375,0.825) {$1$};
\draw[cell frame] (3.650,0.550) rectangle (4.200,1.100);
\node[lab] at (3.925,0.825) {$0$};
\draw[cell frame] (4.200,0.550) rectangle (4.750,1.100);
\node[lab] at (4.475,0.825) {$0$};
\draw[cell frame] (3.100,-0.000) rectangle (3.650,0.550);
\node[lab] at (3.375,0.275) {$0$};
\draw[cell, fill=primaryLight] (3.650,-0.000) rectangle (4.200,0.550);
\node[lab] at (3.925,0.275) {$2$};
\draw[cell frame] (4.200,-0.000) rectangle (4.750,0.550);
\node[lab] at (4.475,0.275) {$0$};
\node[lab, note] at (3.925,-0.350) {$[D']$ on $\varepsilon_0,\varepsilon_1,\varepsilon_2$};
\node[lab, note, anchor=west, align=left] at (5.1,0.825) {$D'\varepsilon_0=\varepsilon_0\circ D=\varepsilon_1$\\(the constant term of $p'$ is the\\$t$-coefficient of $p$);\\$D'\varepsilon_1=2\varepsilon_2$,\ \ $D'\varepsilon_2=0$};
\end{tikzpicture}
\end{center}
```

The matrix of the dual map in the dual bases is the transpose, for differentiation on $F[t]_{\le2}$ (@exm-dual-map). For example $\varepsilon_2\circ D$ reads the coefficient of $t^2$ in $p'$, which is $0$, so the last column of $[D']$ is zero.

:::

::: {#thm-dual-map-kernel-image .theorem name="Kernel and image of the dual map"}

Let $\alpha:V\to W$ be linear with $V,W$ finite-dimensional. Then

1. $\ker\alpha'=(\operatorname{im}\alpha)^0$;
2. $\operatorname{im}\alpha'=(\ker\alpha)^0$.

:::

::: {.proof}

1. $\theta\in\ker\alpha'$ $\iff$ $\theta(\alpha(v))=0$ for all $v$ $\iff$ $\theta\in(\operatorname{im}\alpha)^0$.

2. If $\phi=\theta\alpha\in\operatorname{im}\alpha'$ and $v\in\ker\alpha$, then $\phi(v)=\theta(0)=0$; so $\operatorname{im}\alpha'\le(\ker\alpha)^0$.

3. Dimensions: by rank–nullity for $\alpha'$, item 1 and @thm-dimension-of-annihilator, $\dim\operatorname{im}\alpha'=\dim W^*-\dim(\operatorname{im}\alpha)^0=\dim\operatorname{im}\alpha=r(\alpha)$. Also $\dim(\ker\alpha)^0=\dim V-n(\alpha)=r(\alpha)$ by @thm-rank-nullity.

4. A subspace of the same finite dimension is the whole space (@cor-independent-set-extends-to-basis), so $\operatorname{im}\alpha'=(\ker\alpha)^0$.

:::

::: {#fig-dual-maps-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (V) at (0,1.4) {$V$};
\node[box] (W) at (3.2,1.4) {$W$};
\node[box] (Ws) at (3.2,0) {$W^*$};
\node[box] (Vs) at (0,0) {$V^*$};
\draw[->, emph] (V) -- (W) node[midway, above, lab] {$\alpha$};
\draw[->, emph, accent] (Ws) -- (Vs) node[midway, below, lab] {$\alpha'$};
\node[lab, note, anchor=west, align=left] at (4.0,1.4) {$\operatorname{im}\alpha\subseteq W$};
\node[lab, note, anchor=west, align=left] at (4.0,0) {$\ker\alpha'=\{\theta:\theta\circ\alpha=0\}=(\operatorname{im}\alpha)^0$};
\node[lab, note, anchor=west, align=left] at (4.0,-0.6) {$\operatorname{im}\alpha'=(\ker\alpha)^0\subseteq V^*$};
\end{tikzpicture}
\end{center}
```

A functional on $W$ is killed by $\alpha'$ exactly when it vanishes on everything $\alpha$ hits. Kernel and image swap roles between $\alpha$ and $\alpha'$, each turned into an annihilator.

:::

::: {#thm-dual-map-rank .theorem name="A map and its dual have the same rank" related="thm-row-rank-equals-column-rank"}

$r(\alpha')=r(\alpha)$. In matrix form, $r(A^{\mathsf T})=r(A)$: row rank equals column rank.

:::

::: {.proof}

1. Step 3 of the proof of @thm-dual-map-kernel-image showed $\dim\operatorname{im}\alpha'=r(\alpha)$.

2. Apply this to $\alpha=(\mathbf x\mapsto A\mathbf x)$ in the standard bases; by @thm-dual-map-matrix, $\alpha'$ has matrix $A^{\mathsf T}$.

:::

::: {#def-evaluation-map .definition name="The double dual and the evaluation map"}

The *double dual* of $V$ is $V^{**}=(V^*)^*$. The *evaluation map* is
$$\operatorname{ev}:V\to V^{**},\qquad \operatorname{ev}(v)(\theta)=\theta(v).$$

:::

::: {#fig-dual-maps-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (V) at (0,0) {$V$};
\node[box] (Vss) at (3.6,0) {$V^{**}$};
\draw[->, emph] (V) -- (Vss) node[midway, above, lab] {$\operatorname{ev}$};
\node[lab, note, anchor=west, align=left] at (4.4,0) {$\operatorname{ev}(v)$ is the functional on $V^*$\\$\theta\mapsto\theta(v)$: \emph{evaluate at $v$}};
\node[lab, note, align=center] at (1.8,-0.9) {no basis chosen; an isomorphism when $\dim V<\infty$};
\end{tikzpicture}
\end{center}
```

The evaluation map. A vector $v$ gives a functional on functionals by evaluating them at $v$. Since its definition uses no basis, $V\cong V^{**}$ is called canonical, unlike $V\cong V^*$.

:::

::: {#thm-double-dual-isomorphism .theorem name="The double dual is canonically V"}

$\operatorname{ev}$ is linear. If $V$ is finite-dimensional, it is an isomorphism $V\cong V^{**}$, defined without choosing a basis.

:::

::: {.proof}

1. Linear: $\operatorname{ev}(\lambda v+\mu w)(\theta)=\lambda\theta(v)+\mu\theta(w)$.

2. Injective: if $v\ne0$, extend $v=e_1$ to a basis; the dual functional $\varepsilon_1$ has $\operatorname{ev}(v)(\varepsilon_1)=1\ne0$, so $\operatorname{ev}(v)\ne0$.

3. If $\dim V=n$, then $\dim V^{**}=\dim V^*=n$ by @thm-dual-basis, so the injective map $\operatorname{ev}$ is an isomorphism by @cor-injective-iff-surjective.

:::

Under this identification, the dual basis of $\varepsilon_1,\dots,\varepsilon_n$ is $e_1,\dots,e_n$, and $\alpha''=\alpha$.

::: {#prp-annihilator-properties .proposition name="Annihilators of sums and intersections"}

Let $V$ be finite-dimensional and $U,U_1,U_2\le V$. Identifying $V^{**}$ with $V$ by $\operatorname{ev}$:

1. $U^{00}=U$;
2. $(U_1+U_2)^0=U_1^0\cap U_2^0$;
3. $(U_1\cap U_2)^0=U_1^0+U_2^0$.

:::

::: {.proof}

1. If $u\in U$ and $\theta\in U^0$, then $\operatorname{ev}(u)(\theta)=\theta(u)=0$, so $U\le U^{00}$. Both have dimension $\dim U$ by @thm-dimension-of-annihilator applied twice, so they are equal.

2. A functional kills $U_1+U_2$ exactly when it kills $U_1$ and $U_2$.

3. Apply item 2 to $U_1^0,U_2^0\le V^*$: $(U_1^0+U_2^0)^0=U_1^{00}\cap U_2^{00}=U_1\cap U_2$. Taking annihilators and using item 1 gives $U_1^0+U_2^0=(U_1\cap U_2)^0$.

:::

::: {#exm-dual-map .example name="The dual of differentiation"}

Let $D:F[t]_{\le2}\to F[t]_{\le2}$ be differentiation, with basis $1,t,t^2$ and dual basis $\varepsilon_0,\varepsilon_1,\varepsilon_2$ (coefficient functionals). The functional "evaluate at $1$" is $\theta=\varepsilon_0+\varepsilon_1+\varepsilon_2$, and $D'(\theta)=\theta\circ D$ sends $p\mapsto p'(1)$. Since $[D]$ has rows $(0,1,0),(0,0,2),(0,0,0)$, its transpose sends the coordinates $(1,1,1)$ of $\theta$ to $(0,1,2)$, that is, $D'(\theta)=\varepsilon_1+2\varepsilon_2$; indeed $(a+bt+ct^2)'(1)=b+2c$. The kernel of $D'$ is $(\operatorname{im}D)^0=\langle\varepsilon_2\rangle$: $\operatorname{im}D=F[t]_{\le1}$ when $2\ne0$ in $F$.

:::
