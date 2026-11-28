---
title: "The Baire Category Theorem"
sources: [camii-lan-2, camii-lans-2]
requires: [math/analysis/topology/closure-and-interior, math/analysis/banach-spaces/riesz-lemma]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Linear Analysis (lecture notes), Sections 2.1 and 2.2 (first applications), and Example Sheet 2 (questions 6, 8, 11, 13), in our own wording; proofs written out in steps. -->

A complete metric space cannot be built from countably many "thin" pieces. This is the one topological fact behind the uniform boundedness principle and the open mapping theorem.

::: {#def-nowhere-dense .definition name="Nowhere dense, meagre"}

A subset $E$ of a topological space $X$ is *nowhere dense* if $\overline E$ has empty interior. $E$ is *meagre* (of the first category) if it is a countable union of nowhere dense sets; otherwise it is of the *second category*. A set is *residual* if its complement is meagre.

:::

::: {#thm-baire .theorem name="Baire category theorem"}

Let $X$ be a non-empty complete metric space. If $U_1,U_2,\dots$ are dense open subsets of $X$, then $\bigcap_nU_n$ is dense in $X$. Equivalently, $X$ is not a countable union of nowhere dense sets; every non-empty open subset of $X$ is non-meagre.

:::

::: {.proof}

1. Let $W\subseteq X$ be a non-empty open set; we find a point of $W\cap\bigcap_nU_n$.

2. Since $U_1$ is dense, $W\cap U_1$ is open and non-empty. Choose $x_1$ and $0<r_1<1$ with $\overline B(x_1,r_1)\subseteq W\cap U_1$.

3. Inductively, $B(x_n,r_n)\cap U_{n+1}$ is non-empty and open (density), so choose $x_{n+1}$ and $0<r_{n+1}<1/(n+1)$ with $\overline B(x_{n+1},r_{n+1})\subseteq B(x_n,r_n)\cap U_{n+1}$.

4. For $m\ge n$ we have $x_m\in B(x_n,r_n)$, so $d(x_m,x_n)<r_n<1/n$ and $(x_n)$ is Cauchy. By completeness $x_n\to x$.

5. For each $n$, $x\in\overline B(x_n,r_n)\subseteq U_n$ (the closed balls are nested), and $x\in\overline B(x_1,r_1)\subseteq W$.

6. For the equivalent form: if $X=\bigcup E_n$ with $E_n$ nowhere dense, the sets $U_n=X\setminus\overline{E_n}$ are dense and open with empty intersection, contradicting the first part.

:::

::: {#fig-baire-category-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,0) circle (2.0);
\draw[faint] (0.5,0.2) circle (1.1);
\draw[faint] (0.8,0.3) circle (0.55);
\draw[emph] (0.95,0.35) circle (0.25);
\node[hl dot] at (0.98,0.38) {}; \node[lab, right] at (1.1,0.4) {$x$};
\node[lab] at (-1.2,1.3) {$U_1$}; \node[lab] at (-0.1,0.5) {$U_2$};
\end{tikzpicture}
\end{center}
```

Nested closed balls, each inside $U_n$, shrink to a point of $\bigcap U_n$.

:::

::: {#cor-baire-consequences .corollary name="First consequences"}

(i) $\mathbb R$ is uncountable, and more generally a non-empty countable complete metric space has an isolated point. (ii) $\mathbb Q$ is not a countable intersection of open sets, i.e. $\mathbb Q$ is not a $G_\delta$ in $\mathbb R$. (iii) An infinite-dimensional Banach space has no countable Hamel basis.

:::

::: {.proof}

1. (i) If $X=\{x_1,x_2,\dots\}$ has no isolated point, each $\{x_n\}$ is nowhere dense (closed with empty interior) and $X=\bigcup\{x_n\}$ is meagre, contradicting @thm-baire. For $X=\mathbb R$ use that $\mathbb R$ has no isolated points.

2. (ii) If $\mathbb Q=\bigcap G_n$ with $G_n$ open, each $G_n$ is dense, and so is $\mathbb R\setminus\{q_k\}$ for each rational $q_k$. Then $\bigcap_nG_n\cap\bigcap_k(\mathbb R\setminus\{q_k\})=\emptyset$ is an intersection of countably many dense open sets, contradicting @thm-baire.

3. (iii) If $X$ had a countable Hamel basis $(v_k)$, then $X=\bigcup_n\operatorname{span}(v_1,\dots,v_n)$. Each finite-dimensional subspace is closed (@prp-finite-dim-complete-closed) and proper, hence has empty interior (a subspace containing a ball is everything). So $X$ is meagre, contradicting @thm-baire.

:::

::: {#prp-continuous-nowhere-differentiable .proposition name="Nowhere differentiable continuous functions are generic"}

The set of $f\in C[0,1]$ that are differentiable at no point of $[0,1]$ is residual in $(C[0,1],\|\cdot\|_\infty)$; in particular such functions exist.

:::

::: {.proof}

1. For $n\ge1$ let $E_n$ be the set of $f\in C[0,1]$ for which there is $x\in[0,1]$ with $|f(x+h)-f(x)|\le n|h|$ whenever $x+h\in[0,1]$. A function differentiable at some point lies in some $E_n$.

2. *$E_n$ is closed.* Let $f_k\to f$ uniformly with $f_k\in E_n$ with witnesses $x_k$. Pass to a subsequence $x_k\to x$. Then for fixed $h$, $|f(x+h)-f(x)|=\lim|f_k(x_k+h)-f_k(x_k)|\le n|h|$, using uniform convergence and continuity of $f$.

3. *$E_n$ has empty interior.* Given $f\in C[0,1]$ and $\varepsilon>0$, choose a piecewise linear $g$ with $\|f-g\|_\infty<\varepsilon/2$ and all slopes of absolute value at most $M$. Add a zigzag $s$ with $\|s\|_\infty<\varepsilon/2$ whose slopes are $\pm(M+n+1)$. On each linear piece of $g+s$ the slope has absolute value at least $n+1$, so at every point $x$ (also at kinks) the inequality $|(g+s)(x+h)-(g+s)(x)|\le n|h|$ fails for small $h$ of suitable sign. Hence $g+s\notin E_n$ and $\|f-(g+s)\|_\infty<\varepsilon$.

4. So each $E_n$ is closed and nowhere dense; $\bigcup E_n$ is meagre and its complement is residual, in particular non-empty by @thm-baire.

:::

::: {#prp-meagre-subspace .proposition name="Proper subspaces and meagre sets"}

A proper subspace $Y$ of a normed space $X$ has empty interior. Hence if $Y$ is a closed proper subspace it is nowhere dense, and $\ell^p$ is a meagre subset of $\ell^q$ for $1\le p<q$.

:::

::: {.proof}

1. If $Y$ contains a ball $B(y,r)$ then $B(0,r)=B(y,r)-y\subseteq Y$, and by scaling $Y=X$.

2. $\ell^p=\bigcup_nF_n$ with $F_n=\{x\in\ell^q:\|x\|_p\le n\}$. Each $F_n$ is closed in $\ell^q$: if $x^k\to x$ in $\ell^q$ then coordinates converge, so every partial sum $\sum_{i\le M}|x_i|^p=\lim_k\sum_{i\le M}|x^k_i|^p\le n^p$. Each $F_n$ lies in the proper subspace $\ell^p$, which has empty interior by step 1. So $\ell^p$ is meagre in the complete space $\ell^q$.

:::

::: {#exm-baire-limits .example name="Pointwise limits and 'eventually zero' conditions"}

(i) If $f:\mathbb R\to\mathbb R$ is continuous and $f(nx)\to0$ as $n\to\infty$ for every $x>0$, then $f(x)\to0$ as $x\to\infty$. Fix $\varepsilon>0$. The sets $A_N=\{x\in[1,2]:|f(nx)|\le\varepsilon\ \forall n\ge N\}$ are closed and cover the complete space $[1,2]$, so by @thm-baire some $A_N$ contains an interval $(a,b)$. For $n\ge N$ the interval $(na,nb)$ lies in $\{|f|\le\varepsilon\}$. These intervals overlap once $nb>(n+1)a$, i.e. $n>a/(b-a)$, and so cover all $t$ beyond $\max(N,a/(b-a)+1)\,a$.

(ii) A pointwise limit of continuous functions $[0,1]\to\mathbb R$ has a point of continuity, in fact the points of continuity form a dense $G_\delta$.

:::
