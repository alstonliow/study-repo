---
title: "Open and Closed Sets in Metric Spaces"
sources: [camib-at-a4, camib-at-a5, camib-at-m1]
requires: [math/analysis/metric-spaces/metric-spaces]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Analysis II (Michaelmas 2015 lecture notes), Sections 4.2 and 5.2, and Metric and Topological Spaces (Easter 2015 lecture notes), Section 1.4, in our own wording; the sources' definitions are merged into one block each; examples ours; proofs written out in steps. -->

Open sets describe "all points near $x$" without fixing a distance scale. Many properties of a metric space depend only on its open sets; these are the topological properties studied in @sec-math-analysis-topology-topological-spaces.

::: {#def-open-ball .definition name="Open and closed balls"}

In a metric space $(X,d)$, the *open ball* and *closed ball* of radius $r>0$ about $x$ are
$$B_r(x)=\{y\in X:d(x,y)<r\},\qquad\overline B_r(x)=\{y\in X:d(x,y)\le r\}.$$

:::

::: {#fig-open-and-closed-sets-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) circle (1); \draw[faint, dashed] (0,0) circle (1);
\fill[tintB] (3,0) circle (1); \draw[emph] (3,0) circle (1);
\node[dot] at (0,0) {}; \draw[->, faint] (0,0) -- (0.71,0.71) node[lab, midway, above left] {$r$};
\node[dot] at (3,0) {}; \draw[->, faint] (3,0) -- (3.71,0.71) node[lab, midway, above left] {$r$};
\node[lab, below] at (0,-1.05) {$B_r(x)$: $d(x,y)<r$}; \node[lab, below] at (3,-1.05) {$\overline B_r(x)$: $d(x,y)\le r$};
\end{tikzpicture}
\end{center}
```

The open ball leaves out its boundary (dashed); the closed ball includes it. Drawn for the Euclidean metric; other metrics give other shapes (@exm-norms).

:::

The shape of a ball depends on the metric: in $\mathbb R^2$ the unit ball is a disc for $d_2$, a square for $d_\infty$, and a diamond for $d_1$. In a discrete space, $B_1(x)=\{x\}$.

::: {#def-open-set-metric .definition name="Open set, neighbourhood"}

$U\subseteq X$ is *open* if for every $x\in U$ there is $\delta>0$ with $B_\delta(x)\subseteq U$. An *open neighbourhood* of $x$ is an open set containing $x$.

:::

::: {#lem-open-ball-open .lemma name="Open balls are open"}

Every open ball $B_r(x)$ is an open set.

:::

::: {.proof}

1. Let $y\in B_r(x)$ and put $\delta=r-d(x,y)>0$.

2. If $z\in B_\delta(y)$, then $d(x,z)\le d(x,y)+d(y,z)<d(x,y)+\delta=r$, so $z\in B_r(x)$. Hence $B_\delta(y)\subseteq B_r(x)$.

:::

::: {#fig-open-and-closed-sets-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) circle (1.6); \draw[faint, dashed] (0,0) circle (1.6);
\node[dot] at (0,0) {}; \node[lab, below] at (0,0) {$x$};
\draw[regionB] (0.8,0.5) circle (0.6); \node[dot] at (0.8,0.5) {}; \node[lab, below] at (0.8,0.5) {$y$};
\draw[faint] (0,0) -- (0.8,0.5) node[lab, midway, above left] {$d(x,y)$};
\draw[->, emph] (0.8,0.5) -- (1.31,0.82) node[lab, right] {$r-d(x,y)$};
\end{tikzpicture}
\end{center}
```

Why an open ball is open: around any point $y$ of $B_r(x)$, the ball of radius $r-d(x,y)$ stays inside $B_r(x)$ by the triangle inequality.

:::

::: {#thm-open-sets-metric .theorem name="Properties of open sets"}

In a metric space $X$:

1. $\emptyset$ and $X$ are open;
2. any union of open sets is open;
3. the intersection of finitely many open sets is open.

:::

::: {.proof}

1. Both conditions are immediate ($\emptyset$ has no points to check).

2. If $x\in\bigcup_\alpha U_\alpha$, then $x\in U_\beta$ for some $\beta$, and a ball $B_\delta(x)\subseteq U_\beta\subseteq\bigcup_\alpha U_\alpha$.

3. If $x\in U_1\cap\dots\cap U_n$, take $\delta_i$ with $B_{\delta_i}(x)\subseteq U_i$ and $\delta=\min_i\delta_i>0$. Then $B_\delta(x)$ lies in every $U_i$.

:::

Finiteness in part 3 is needed: $\bigcap_{n\ge1}(-\frac1n,\frac1n)=\{0\}$ is not open in $\mathbb R$.

::: {#prp-convergence-open-sets .proposition name="Convergence through open sets"}

$x_n\to x$ in $X$ if and only if every open neighbourhood $U$ of $x$ contains $x_n$ for all sufficiently large $n$.

:::

::: {.proof}

1. If $x_n\to x$ and $U\ni x$ is open, take $B_\delta(x)\subseteq U$; eventually $d(x_n,x)<\delta$, so $x_n\in U$.

2. Conversely, apply the condition to the open sets $U=B_\varepsilon(x)$ (@lem-open-ball-open): eventually $d(x_n,x)<\varepsilon$.

:::

So convergence, and by @prp-sequential-continuity-metric continuity, depend only on which sets are open. Lipschitz equivalent metrics have the same open sets, and so do the metrics of @exm-metric-spaces-bounded-metric.

## Closed sets

::: {#def-limit-point-metric .definition name="Limit point, closed set"}

Let $E\subseteq X$. A point $x\in X$ is a *limit point* of $E$ if there is a sequence in $E\setminus\{x\}$ converging to $x$; equivalently, every ball $B_\delta(x)$ meets $E$ in a point other than $x$. A set $E$ is *closed* if it contains all its limit points.

:::

::: {#prp-closed-iff-complement-open .proposition name="Closed means complement open"}

$E\subseteq X$ is closed if and only if $X\setminus E$ is open. Equivalently, $E$ is closed if and only if the limit of every convergent sequence in $E$ lies in $E$.

:::

::: {.proof}

1. Suppose $E$ is closed and $x\notin E$. Then $x$ is not a limit point of $E$, so some ball $B_\delta(x)$ contains no point of $E$ other than $x$, and $x\notin E$; so $B_\delta(x)\subseteq X\setminus E$. Hence $X\setminus E$ is open.

2. Suppose $X\setminus E$ is open and $x$ is a limit point of $E$. If $x\notin E$, some ball $B_\delta(x)$ lies in $X\setminus E$, contradicting that every ball about $x$ meets $E$. So $x\in E$.

3. *Sequences.* If $x_n\in E$ and $x_n\to x$, either $x_n=x$ for some $n$, so $x\in E$, or $x$ is a limit point of $E$. So "closed" implies the sequence condition; conversely the sequence condition applied to sequences in $E\setminus\{x\}$ contains the definition.

:::

::: {#fig-open-and-closed-sets-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (1.590,0.000) -- (1.635,0.126) -- (1.651,0.257) -- (1.634,0.389) -- (1.582,0.516) -- (1.494,0.633) -- (1.375,0.732) -- (1.230,0.812) -- (1.068,0.870) -- (0.898,0.906) -- (0.728,0.924) -- (0.563,0.927) -- (0.408,0.922) -- (0.264,0.913) -- (0.130,0.905) -- (0.000,0.902) -- (-0.130,0.905) -- (-0.264,0.913) -- (-0.408,0.922) -- (-0.563,0.927) -- (-0.727,0.924) -- (-0.898,0.906) -- (-1.068,0.870) -- (-1.230,0.812) -- (-1.375,0.732) -- (-1.494,0.633) -- (-1.582,0.516) -- (-1.634,0.389) -- (-1.651,0.257) -- (-1.635,0.126) -- (-1.590,0.000) -- (-1.524,-0.117) -- (-1.444,-0.225) -- (-1.357,-0.323) -- (-1.269,-0.414) -- (-1.182,-0.500) -- (-1.098,-0.585) -- (-1.013,-0.669) -- (-0.927,-0.755) -- (-0.833,-0.840) -- (-0.728,-0.924) -- (-0.608,-1.002) -- (-0.474,-1.069) -- (-0.325,-1.121) -- (-0.165,-1.155) -- (-0.000,-1.166) -- (0.165,-1.155) -- (0.325,-1.121) -- (0.474,-1.069) -- (0.608,-1.002) -- (0.728,-0.924) -- (0.833,-0.840) -- (0.927,-0.755) -- (1.013,-0.669) -- (1.098,-0.585) -- (1.182,-0.500) -- (1.269,-0.414) -- (1.357,-0.323) -- (1.444,-0.225) -- (1.524,-0.117) -- cycle;
\draw[emph] (1.590,0.000) -- (1.635,0.126) -- (1.651,0.257) -- (1.634,0.389) -- (1.582,0.516) -- (1.494,0.633) -- (1.375,0.732) -- (1.230,0.812) -- (1.068,0.870) -- (0.898,0.906) -- (0.728,0.924) -- (0.563,0.927) -- (0.408,0.922) -- (0.264,0.913) -- (0.130,0.905) -- (0.000,0.902) -- (-0.130,0.905) -- (-0.264,0.913) -- (-0.408,0.922) -- (-0.563,0.927) -- (-0.727,0.924) -- (-0.898,0.906) -- (-1.068,0.870) -- (-1.230,0.812) -- (-1.375,0.732) -- (-1.494,0.633) -- (-1.582,0.516) -- (-1.634,0.389) -- (-1.651,0.257) -- (-1.635,0.126) -- (-1.590,0.000) -- (-1.524,-0.117) -- (-1.444,-0.225) -- (-1.357,-0.323) -- (-1.269,-0.414) -- (-1.182,-0.500) -- (-1.098,-0.585) -- (-1.013,-0.669) -- (-0.927,-0.755) -- (-0.833,-0.840) -- (-0.728,-0.924) -- (-0.608,-1.002) -- (-0.474,-1.069) -- (-0.325,-1.121) -- (-0.165,-1.155) -- (-0.000,-1.166) -- (0.165,-1.155) -- (0.325,-1.121) -- (0.474,-1.069) -- (0.608,-1.002) -- (0.728,-0.924) -- (0.833,-0.840) -- (0.927,-0.755) -- (1.013,-0.669) -- (1.098,-0.585) -- (1.182,-0.500) -- (1.269,-0.414) -- (1.357,-0.323) -- (1.444,-0.225) -- (1.524,-0.117) -- cycle;
\node[lab] at (-0.3,0) {$F$ closed};
\draw[regionB] (2.4,0.6) circle (0.55); \node[dot] at (2.4,0.6) {}; \node[lab, below] at (2.4,0.58) {$y\notin F$};
\node[hl dot] at (1.55,-0.05) {}; \node[lab, right] at (1.6,-0.2) {limit points stay in $F$};
\end{tikzpicture}
\end{center}
```

$F$ is closed when it contains all its limit points. Equivalently, every point outside $F$ has a ball around it missing $F$, so the complement is open.

:::

Taking complements in @thm-open-sets-metric: $\emptyset$ and $X$ are closed, finite unions of closed sets are closed, and arbitrary intersections of closed sets are closed.

::: {#exm-open-and-closed-sets-1 .example name="Open, closed, both and neither"}

1. A closed ball $\overline B_r(x)$ is closed: if $d(x,y)>r$, then $B_{d(x,y)-r}(y)$ misses it by the triangle inequality. Singletons are closed, since $\{x\}$ has no limit points.
2. In $\mathbb R$, $(0,1]$ is neither open (no ball about $1$ fits) nor closed ($0$ is a limit point not in it).
3. In a discrete space every set is open, since $\{x\}=B_1(x)$, hence every set is also closed.
4. In the subspace $Y=(0,2)$ of $\mathbb R$, the set $(0,1]$ is closed in $Y$: its only limit point in $\mathbb R$ outside it is $0\notin Y$. Openness and closedness depend on the ambient space.

:::
