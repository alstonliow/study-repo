---
title: "The Open Mapping, Inverse Mapping and Closed Graph Theorems"
sources: [camii-lan-2, camii-lans-2]
requires: [math/analysis/banach-spaces/baire-category]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Linear Analysis (lecture notes), Section 2.2, and Example Sheet 2 (questions 9, 10, 12, 14), in our own wording; proofs written out in steps. -->

A bounded surjection between Banach spaces is automatically open. Two corollaries are routinely used: a bounded bijection has bounded inverse, and a closed-graph operator is bounded.

::: {#lem-open-mapping .lemma name="Open mapping lemma"}

Let $X$ be a Banach space, $Y$ a normed space and $T\in B(X,Y)$. If $\overline{T(B_X(1))}\supseteq B_Y(\delta)$ for some $\delta>0$, then $T(B_X(1))\supseteq B_Y(\delta/2)$. In particular $T$ is onto.

:::

::: {.proof}

1. Scaling the hypothesis, $\overline{T(B_X(2^{-n}))}\supseteq B_Y(\delta2^{-n})$ for every $n\ge0$.

2. Let $y\in B_Y(\delta/2)$. By step 1 with $n=1$ there is $x_1\in B_X(\frac12)$ with $\|y-Tx_1\|<\delta/4$. Then $y-Tx_1\in B_Y(\delta/4)$, so there is $x_2\in B_X(\frac14)$ with $\|y-Tx_1-Tx_2\|<\delta/8$, and so on: $x_n\in B_X(2^{-n})$ with $\|y-T(x_1+\dots+x_n)\|<\delta2^{-n-1}$.

3. $\sum\|x_n\|<\sum2^{-n}=1$, so $\sum x_n$ converges to some $x$ with $\|x\|<1$ (completeness of $X$), and by continuity $Tx=y$.

:::

::: {#thm-open-mapping .theorem name="Open mapping theorem"}

Let $X,Y$ be Banach spaces and $T\in B(X,Y)$ surjective. Then $T$ is an open map: it sends open sets to open sets.

:::

::: {.proof}

1. $Y=\bigcup_nT(B_X(n))=\bigcup_n\overline{T(B_X(n))}$. By @thm-baire some $\overline{T(B_X(n))}$ has non-empty interior, containing a ball $B_Y(y_0,r)$.

2. Then the set $\overline{T(B_X(n))}-\overline{T(B_X(n))}\supseteq B_Y(y_0,r)-B_Y(y_0,r)\supseteq B_Y(r)$, and the left side is contained in $\overline{T(B_X(2n))}$ since $B_X(n)-B_X(n)\subseteq B_X(2n)$.

3. By scaling $\overline{T(B_X(1))}\supseteq B_Y(r/2n)$, and @lem-open-mapping gives $T(B_X(1))\supseteq B_Y(r/4n)$.

4. If $U\subseteq X$ is open and $x\in U$ with $B_X(x,\varepsilon)\subseteq U$, then $T(U)\supseteq Tx+\varepsilon T(B_X(1))\supseteq B_Y(Tx,\varepsilon r/4n)$. So $T(U)$ is open.

:::

::: {#fig-open-mapping-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[emph] (0,0) circle (1.0); \node[lab] at (0,0) {$B_X(1)$};
\draw[faint] (5,0) ellipse (1.9 and 1.2);
\draw[hl] (5,0) circle (0.7); \node[lab] at (5,0) {$B_Y(\delta)$};
\node[lab, above] at (5,1.2) {$T(B_X(1))$};
\draw[map] (1.2,0) -- (2.9,0); \node[lab, above] at (2.05,0) {$T$};
\end{tikzpicture}
\end{center}
```

The open mapping theorem: the image of the unit ball contains a ball about $0$.

:::

::: {#cor-inverse-mapping .corollary name="Inverse mapping theorem"}

A bijective $T\in B(X,Y)$ between Banach spaces has $T^{-1}\in B(Y,X)$, i.e. $T$ is an isomorphism.

:::

::: {.proof}

$T$ is open, so $T^{-1}$ is continuous.

:::

::: {#cor-equivalent-complete-norms .corollary name="Comparable complete norms are equivalent"}

If $\|\cdot\|_1\le C\|\cdot\|_2$ on $X$ and $X$ is complete in both norms, then the two norms are equivalent.

:::

::: {.proof}

The identity $(X,\|\cdot\|_2)\to(X,\|\cdot\|_1)$ is a bounded bijection between Banach spaces; apply @cor-inverse-mapping.

:::

::: {#thm-closed-graph .theorem name="Closed graph theorem"}

Let $X,Y$ be Banach spaces and $T:X\to Y$ linear. If the graph $\Gamma(T)=\{(x,Tx)\}\subseteq X\times Y$ is closed, then $T$ is bounded.

:::

::: {.proof}

1. Give $X\times Y$ the norm $\|(x,y)\|=\|x\|+\|y\|$, which makes it a Banach space. The graph $\Gamma$ is a closed subspace, hence Banach.

2. The projection $\pi_1:\Gamma\to X$, $(x,Tx)\mapsto x$, is a bounded linear bijection, so by @cor-inverse-mapping its inverse $x\mapsto(x,Tx)$ is bounded.

3. Therefore $\|x\|+\|Tx\|\le C\|x\|$ and $T$ is bounded.

:::

::: {#exm-closed-graph-uses .example name="Using the closed graph theorem"}

(i) Let $X$ be a closed subspace of $C[0,1]$ (sup norm) all of whose elements are continuously differentiable. Then $D:X\to C[0,1]$, $f\mapsto f'$, has closed graph (if $f_n\to f$ and $f_n'\to g$ uniformly, then $f'=g$), so $D$ is bounded: $\|f'\|_\infty\le C\|f\|_\infty$. By Arzelà–Ascoli (@sec-math-analysis-function-spaces-arzela-ascoli) the unit ball of $X$ is then compact (it is bounded and equicontinuous and closed), hence $X$ is finite-dimensional by @thm-unit-ball-compact.

(ii) Completeness of the domain is needed: $D:(C^1[0,1],\|\cdot\|_\infty)\to C[0,1]$ has closed graph (if $f_n\to f$ and $f_n'\to g$ uniformly then $f\in C^1$ and $f'=g$) but is unbounded, because $C^1[0,1]$ is not complete in the sup norm.

:::
