---
title: "The Hahn–Banach Theorem"
sources: [camii-lan-1, camii-lans-2]
requires: [math/analysis/banach-spaces/bounded-linear-maps, math/linear-algebra/duality/dual-spaces]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Linear Analysis (lecture notes), Section 1.7, in our own wording; proofs written out in steps. Zorn's lemma is taken as given (it is equivalent to the axiom of choice). The complex case is derived from the real case by the standard trick, written out here. -->

A normed space has few obvious functionals. The Hahn–Banach theorem says that functionals defined on a subspace extend without increasing the norm, so $X^*$ is always large enough to separate points of $X$.

::: {#lem-zorn .lemma name="Zorn's lemma"}

Let $(S,\le)$ be a non-empty partially ordered set in which every totally ordered subset has an upper bound in $S$. Then $S$ has a maximal element.

:::

::: {#lem-extension-one-step .lemma name="One-dimensional extension"}

Let $X$ be a real vector space, $p:X\to\mathbb R$ sublinear ($p(x+y)\le p(x)+p(y)$, $p(\lambda x)=\lambda p(x)$ for $\lambda\ge0$), $Y\subsetneq X$ a subspace, and $f:Y\to\mathbb R$ linear with $f\le p$ on $Y$. For $z\notin Y$ there is a linear extension $\tilde f$ to $Y+\mathbb Rz$ with $\tilde f\le p$.

:::

::: {.proof}

1. An extension is determined by $c=\tilde f(z)$, with $\tilde f(y+tz)=f(y)+tc$. We need $f(y)+tc\le p(y+tz)$ for all $y\in Y$, $t\in\mathbb R$.

2. For $t>0$ dividing by $t$, this says $c\le p(y+z)-f(y)$ for all $y\in Y$. For $t<0$, replacing $y$ by $-y$ and dividing by $-t$, it says $c\ge f(y)-p(y-z)$ for all $y\in Y$. For $t=0$ it is the hypothesis.

3. So we need $\sup_y\big(f(y)-p(y-z)\big)\le c\le\inf_y\big(p(y'+z)-f(y')\big)$. This interval is non-empty because for all $y,y'\in Y$,
$$f(y)+f(y')=f(y+y')\le p(y+y')\le p(y-z)+p(y'+z).$$

:::

::: {#thm-hahn-banach .theorem name="Hahn–Banach theorem (real case, sublinear form)"}

Let $X$ be a real vector space, $p$ a sublinear functional on $X$, $Y$ a subspace and $f:Y\to\mathbb R$ linear with $f\le p$ on $Y$. Then there is a linear $F:X\to\mathbb R$ with $F|_Y=f$ and $F\le p$ on $X$.

:::

::: {.proof}

1. Let $S$ be the set of pairs $(Z,g)$ with $Y\subseteq Z\subseteq X$ a subspace and $g:Z\to\mathbb R$ linear, $g|_Y=f$, $g\le p$ on $Z$, ordered by extension.

2. $S\ne\emptyset$ since $(Y,f)\in S$. A chain $\{(Z_i,g_i)\}$ has the upper bound $(\bigcup Z_i,g)$ with $g=g_i$ on $Z_i$ (well defined because the chain is ordered by extension).

3. By @lem-zorn there is a maximal $(Z,F)$. If $Z\ne X$, @lem-extension-one-step extends $F$ to a larger subspace, contradicting maximality. So $Z=X$.

:::

::: {#fig-hahn-banach-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-3,0) -- (3,0);
\draw[emph] (-1.2,0) -- (1.4,0); \node[lab, below] at (-1.2,-0.1) {$\sup_y f(y)-p(y-z)$}; \node[lab, above] at (1.4,0.1) {$\inf_y p(y+z)-f(y)$};
\node[hl dot] at (0.2,0) {}; \node[lab, below] at (0.2,-0.1) {$c$};
\end{tikzpicture}
\end{center}
```

The value $c=\tilde f(z)$ of a one-step extension may be any number in this interval.

:::

::: {#cor-hahn-banach-normed .corollary name="Hahn–Banach for normed spaces"}

Let $X$ be a real or complex normed space, $Y$ a subspace and $f\in Y^*$. Then there is $F\in X^*$ with $F|_Y=f$ and $\|F\|=\|f\|$.

:::

::: {.proof}

1. *Real case.* Take $p(x)=\|f\|\|x\|$, which is sublinear. @thm-hahn-banach gives $F\le p$; applying it to $-x$ gives $|F(x)|\le\|f\|\|x\|$. So $\|F\|\le\|f\|$, and $\ge$ is clear.

2. *Complex case.* Regard $X$ as a real space and let $u=\operatorname{Re}f$, a real functional with $|u|\le\|f\|\|\cdot\|$ and $f(y)=u(y)-iu(iy)$. Extend $u$ to a real functional $U$ on $X$ with $|U|\le\|f\|\|\cdot\|$ by step 1, and set $F(x)=U(x)-iU(ix)$. This is complex linear and extends $f$.

3. For $x\in X$ choose $\lambda$ with $|\lambda|=1$ and $\lambda F(x)=|F(x)|$. Then $|F(x)|=F(\lambda x)=U(\lambda x)\le\|f\|\|x\|$. So $\|F\|=\|f\|$.

:::

::: {#cor-hahn-banach-separates .corollary name="Functionals separate points and compute the norm"}

Let $X$ be a normed space. (i) For $x\in X$, $x\ne0$ there is $F\in X^*$ with $\|F\|=1$ and $F(x)=\|x\|$. (ii) $\|x\|=\max\{|F(x)|:\|F\|\le1\}$. (iii) If $F(x)=F(y)$ for all $F\in X^*$ then $x=y$. In particular $X^*\ne\{0\}$ if $X\ne\{0\}$.

:::

::: {.proof}

1. On $Y=\mathbb Fx$ define $f(\lambda x)=\lambda\|x\|$, so $\|f\|=1$. Extend by @cor-hahn-banach-normed to get (i).

2. (ii): $|F(x)|\le\|F\|\|x\|\le\|x\|$ and (i) shows the bound is attained.

3. (iii) apply (ii) to $x-y$.

:::

::: {#prp-annihilator-closure .proposition name="Closed subspaces and functionals"}

If $Y$ is a closed subspace of a normed space $X$ and $x\notin Y$, there is $F\in X^*$ with $F|_Y=0$ and $F(x)=\operatorname{dist}(x,Y)\ne0$ and $\|F\|=1$. Consequently $Y$ is dense in $X$ if and only if every $F\in X^*$ vanishing on $Y$ is zero.

:::

::: {.proof}

1. On $Y+\mathbb Fx$ put $f(y+\lambda x)=\lambda d$, $d=\operatorname{dist}(x,Y)>0$. Then $|f(y+\lambda x)|=|\lambda|d\le\|\lambda x+y\|$ since $d\le\|x+y/\lambda\|$ for $\lambda\ne0$. So $\|f\|\le1$; testing on $y$ with $\|x-y\|$ close to $d$ gives $\|f\|=1$. Extend by @cor-hahn-banach-normed.

2. If $Y$ is dense the only functional vanishing on $Y$ is $0$, by continuity. If $Y$ is not dense, apply the first part to $x\notin\overline Y$ and the closed subspace $\overline Y$.

:::
