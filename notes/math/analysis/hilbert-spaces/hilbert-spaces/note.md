---
title: "Hilbert Spaces and Orthogonal Projection"
sources: [camii-lan-4, camii-lans-3]
requires: [math/linear-algebra/inner-product-spaces/inner-products, math/analysis/banach-spaces/bounded-linear-maps]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Linear Analysis (lecture notes), Sections 4.1 and 4.2 (orthogonal complements), and Example Sheet 3 (questions 6-10), in our own wording; proofs written out in steps. The projection theorem in L2 (math/analysis/measure-theory/lp-spaces) is the case of the Hilbert space L2. -->

An inner product space is the setting in which geometry (angles, perpendiculars, projections) works. Completeness makes projections onto closed subspaces exist, which is why Hilbert spaces are the best-behaved infinite-dimensional spaces.

::: {#def-hilbert-space .definition name="Hilbert space"}

An inner product space $(H,\langle\cdot,\cdot\rangle)$ (@def-inner-product-space), with norm $\|x\|=\sqrt{\langle x,x\rangle}$, is a *Hilbert space* if it is complete. Vectors $x,y$ are *orthogonal*, $x\perp y$, if $\langle x,y\rangle=0$. For $S\subseteq H$, $S^\perp=\{x:\langle x,s\rangle=0\ \forall s\in S\}$.

:::

::: {#exm-hilbert-spaces .example name="Examples"}

$\mathbb F^n$ with the Euclidean inner product; $\ell^2$ with $\langle x,y\rangle=\sum x_n\overline{y_n}$; $L^2$ of a measure space (@def-lp-space). The space $C[0,1]$ with $\langle f,g\rangle=\int_0^1f\bar g$ is an inner product space that is **not** complete, and its completion is $L^2[0,1]$.

:::

::: {#prp-parallelogram .proposition name="Parallelogram law, polarisation and Pythagoras"}

In an inner product space, $\|x+y\|^2+\|x-y\|^2=2\|x\|^2+2\|y\|^2$, and if $x\perp y$ then $\|x+y\|^2=\|x\|^2+\|y\|^2$. Conversely, a norm satisfying the parallelogram law comes from a (unique) inner product, given in the real case by $\langle x,y\rangle=\frac14(\|x+y\|^2-\|x-y\|^2)$ and in the complex case by $\langle x,y\rangle=\frac14\sum_{k=0}^3i^k\|x+i^ky\|^2$.

:::

::: {.proof}

1. Expand $\|x\pm y\|^2=\|x\|^2\pm2\operatorname{Re}\langle x,y\rangle+\|y\|^2$ and add or use $\langle x,y\rangle=0$.

2. *Converse (real case).* Define $B(x,y)=\frac14(\|x+y\|^2-\|x-y\|^2)$. Then $B$ is symmetric, $B(x,x)=\|x\|^2$, $B(0,y)=0$. From the parallelogram law, $B(x+x',y)+B(x-x',y)=2B(x,y)$, and with $x=x'$ this gives $B(2x,y)=2B(x,y)$ and then additivity $B(x+x',y)=B(x,y)+B(x',y)$. Additivity gives $B(\lambda x,y)=\lambda B(x,y)$ for rational $\lambda$, and by continuity of the norm for real $\lambda$.

3. *Complex case:* define the real part $B$ as above and set $\langle x,y\rangle=B(x,y)+iB(x,iy)$; one checks sesquilinearity from the real case.

:::

::: {#prp-completion-inner-product .proposition name="Completion of an inner product space"}

The completion of an inner product space $E$ is a Hilbert space, the inner product extending by continuity.

:::

::: {.proof}

1. The inner product is continuous: $|\langle x,y\rangle-\langle x',y'\rangle|\le\|x-x'\|\|y\|+\|x'\|\|y-y'\|$.

2. Hence it extends uniquely to the completion $\bar E$ (a limit of pairs of Cauchy sequences), still sesquilinear and positive definite, with norm the completed norm.

:::

::: {#thm-projection .theorem name="Closest point and orthogonal projection"}

Let $H$ be an inner product space and $F\subseteq H$ a complete subspace (e.g. any closed subspace of a Hilbert space). For every $x\in H$ there is a unique $y\in F$ with $\|x-y\|=\operatorname{dist}(x,F)$, and $x-y\in F^\perp$. Consequently $H=F\oplus F^\perp$ and $y=P_Fx$, the orthogonal projection, has $\|P_F\|\le1$.

:::

::: {.proof}

1. Let $d=\operatorname{dist}(x,F)$ and pick $y_n\in F$ with $\|x-y_n\|\to d$.

2. By the parallelogram law applied to $x-y_n$ and $x-y_m$,
$$\|y_n-y_m\|^2=2\|x-y_n\|^2+2\|x-y_m\|^2-4\Big\|x-\tfrac{y_n+y_m}2\Big\|^2\le2\|x-y_n\|^2+2\|x-y_m\|^2-4d^2\to0.$$
So $(y_n)$ is Cauchy and converges to some $y\in F$ (completeness of $F$), with $\|x-y\|=d$.

3. *Orthogonality.* For $z\in F$ and $t\in\mathbb F$, $d^2\le\|x-y-tz\|^2=d^2-2\operatorname{Re}\big(\bar t\langle x-y,z\rangle\big)+|t|^2\|z\|^2$. Choosing $t=\varepsilon\langle x-y,z\rangle$ with small $\varepsilon>0$ shows $\langle x-y,z\rangle=0$.

4. *Uniqueness.* If $y,y'$ both have $x-y,x-y'\perp F$ then $y-y'\in F\cap F^\perp=\{0\}$.

5. $x=y+(x-y)\in F+F^\perp$, and $F\cap F^\perp=0$. By Pythagoras $\|P_Fx\|\le\|x\|$.

:::

::: {#fig-hilbert-spaces-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[emph] (-0.5,-0.3) -- (5,1.5) node[lab, right] {$F$};
\node[hl dot] at (3.0,3.0) {}; \node[lab, above] at (3.0,3.0) {$x$};
\node[dot] at (3.0,1.0) {}; \node[lab, below right] at (3.0,1.0) {$P_Fx$};
\draw[hl] (3.0,3.0) -- (3.0,1.0); \draw[faint, dashed] (0,0) -- (3.0,3.0);
\end{tikzpicture}
\end{center}
```

The nearest point $P_Fx$ of a closed subspace $F$; $x-P_Fx\perp F$.

:::

::: {#cor-double-perp .corollary name="Double orthogonal complement"}

For a closed subspace $F$ of a Hilbert space $H$, $F^{\perp\perp}=F$. For any subspace $S$, $S^\perp$ is closed and $S^{\perp\perp}=\overline{\operatorname{span}}\,S$. In particular a subspace $S$ is dense iff $S^\perp=\{0\}$.

:::

::: {.proof}

1. $S^\perp=\bigcap_{s}\{x:\langle x,s\rangle=0\}$ is an intersection of kernels of continuous functionals, so closed.

2. $F\subseteq F^{\perp\perp}$ is clear. If $x\in F^{\perp\perp}$ write $x=y+z$ with $y\in F$, $z\in F^\perp$ by @thm-projection. Then $z=x-y\in F^{\perp\perp}\cap F^\perp=\{0\}$, so $x\in F$.

3. For general $S$ apply the above to $F=\overline{\operatorname{span}}S$, noting $S^\perp=F^\perp$.

:::

::: {#exm-nonclosed-perp .example name="Completeness is needed"}

Let $E=c_{00}$ be the inner product space of finitely supported sequences with the $\ell^2$ inner product (not complete), and $Y=\{x\in E:\sum_nx_n/n=0\}$. $Y$ is a proper closed subspace of $E$ (a kernel of a continuous functional). Within $\ell^2$ the only vectors orthogonal to $Y$ are the multiples of $(1/n)_n$, which is not finitely supported, so $Y^\perp=\{0\}$ in $E$. Thus @thm-projection and @cor-double-perp fail without completeness.

:::

::: {#prp-polarisation-isometry .proposition name="Isometries and inner products"}

For a linear map $T$ on an inner product space, $\langle Tx,Ty\rangle=\langle x,y\rangle$ for all $x,y$ iff $\|Tx\|=\|x\|$ for all $x$. On a complex space, $\langle Tx,x\rangle=0$ for all $x$ implies $T=0$; on a real space this fails (rotation by $90^\circ$ in $\mathbb R^2$).

:::

::: {.proof}

1. If $T$ preserves inner products it preserves norms. Conversely the polarisation identities of @prp-parallelogram express $\langle x,y\rangle$ through norms of $x\pm y$ (and $x\pm iy$), which $T$ preserves.

2. Complex case: $0=\langle T(x+\lambda y),x+\lambda y\rangle=\bar\lambda\langle Tx,y\rangle+\lambda\langle Ty,x\rangle$ for all $\lambda$. Taking $\lambda=1$ and $\lambda=i$ gives $\langle Tx,y\rangle+\langle Ty,x\rangle=0$ and $\langle Tx,y\rangle-\langle Ty,x\rangle=0$, so $\langle Tx,y\rangle=0$ for all $y$, and $Tx=0$.

3. The rotation $T(a,b)=(-b,a)$ has $\langle Tx,x\rangle=0$ for all real $x$ but $T\ne0$.

:::
