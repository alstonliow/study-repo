---
title: "Clustering and the k-Means Algorithm"
sources: [cs229-10]
requires: [ai/machine-learning/supervised-learning]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS229 lecture notes (version of 23 August 2026), Chapter 10 (clustering, the k-means algorithm, distortion, convergence, local optima), in our own wording. The convergence proof is written out in steps; the example is our own and was run in Python. -->

In *unsupervised learning* the training set is $\mathbf{x}^{(1)},\dots,\mathbf{x}^{(N)}$ with no labels, and the task is to find structure in it. The simplest structure is a grouping of the points into clusters.

::: {#def-k-means .definition name="k-means"}

Given points $\mathbf{x}^{(1)},\dots,\mathbf{x}^{(N)}\in\mathbb{R}^d$ and a number of clusters $k$, the *$k$-means algorithm* chooses initial *centroids* $\boldsymbol\mu_1,\dots,\boldsymbol\mu_k$ (for example $k$ distinct training points at random) and repeats until the assignments stop changing:

1. *Assignment step*: for each $i$, set $c^{(i)}=\operatorname{arg\,min}_j\lVert\mathbf{x}^{(i)}-\boldsymbol\mu_j\rVert^2$, breaking ties in favour of the current cluster.
2. *Update step*: for each $j$ with at least one assigned point, set $\boldsymbol\mu_j$ to the mean of the points with $c^{(i)}=j$.

:::

```{=latex}
\begin{algorithm}
\caption{$k$-means}
\begin{algorithmic}
\INPUT Points $\mathbf{x}^{(1)},\dots,\mathbf{x}^{(N)}$, number of clusters $k$
\STATE choose initial centroids $\boldsymbol\mu_1,\dots,\boldsymbol\mu_k$
\REPEAT
    \FOR{$i=1,\dots,N$}
        \STATE $c^{(i)}\gets\operatorname{arg\,min}_j\lVert\mathbf{x}^{(i)}-\boldsymbol\mu_j\rVert^2$
    \ENDFOR
    \FOR{$j=1,\dots,k$}
        \STATE $\boldsymbol\mu_j\gets$ mean of $\{\mathbf{x}^{(i)}:c^{(i)}=j\}$
    \ENDFOR
\UNTIL{no $c^{(i)}$ changes}
\RETURN $c$, $\boldsymbol\mu$
\end{algorithmic}
\end{algorithm}
```

::: {#def-distortion .definition name="Distortion"}

The *distortion* of assignments $c$ and centroids $\boldsymbol\mu$ is

$$
J(c,\boldsymbol\mu)=\sum_{i=1}^N\bigl\lVert\mathbf{x}^{(i)}-\boldsymbol\mu_{c^{(i)}}\bigr\rVert^2,
$$

the total squared distance from each point to its centroid.

:::

::: {#thm-k-means-converges .theorem name="k-means converges"}

Each step of $k$-means does not increase the distortion, and the algorithm stops after finitely many iterations, at assignments and centroids that neither step can improve.

:::

::: {.proof}

1. *Assignment step.* With $\boldsymbol\mu$ fixed, $J$ is a sum of separate terms, one per point, and each point moves to a centroid at least as close as its current one. So $J$ does not increase.

2. *Update step.* With $c$ fixed, the terms of cluster $j$ are $\sum_{i:c^{(i)}=j}\lVert\mathbf{x}^{(i)}-\boldsymbol\mu_j\rVert^2$. Its gradient in $\boldsymbol\mu_j$ is $-2\sum_{i:c^{(i)}=j}(\mathbf{x}^{(i)}-\boldsymbol\mu_j)$, zero exactly at the mean, and the function is a strictly convex quadratic, so the mean minimizes it. So $J$ does not increase.

3. There are at most $k^N$ assignments. The centroids after an update step are determined by the assignment, so the pair after each full iteration is determined by the assignment alone.

4. If an iteration changes the assignment, the tie-breaking rule means some point moved to a strictly closer centroid, so $J$ strictly decreased. Since $J$ never increases, no assignment can occur twice, and after at most $k^N$ iterations the assignment stops changing.

5. At that point the assignment step changes nothing and the update step reproduces the same centroids, so neither step can lower $J$.

:::

::: {#exm-k-means-line .example name="Six points on a line"}

Cluster $1,2,3,10,11,12$ into $k=2$ clusters, starting with the bad centroids $\mu_1=1$, $\mu_2=2$.

| iteration | centroids | clusters | distortion |
|---|---|---|---|
| 1 | $1,\ 2$ | $\{1\},\ \{2,3,10,11,12\}$ | $246$ |
| 2 | $1,\ 7.6$ | $\{1,2,3\},\ \{10,11,12\}$ | $41.68$ |
| 3 | $2,\ 11$ | $\{1,2,3\},\ \{10,11,12\}$ | $4$ |

The assignments do not change in iteration 3, so the algorithm stops with centroids $2$ and $11$.

:::

::: {#fig-k-means-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.7cm,y=0.9cm]
\draw[faint] (0.5,2.0) -- (12.5,2.0);
\node[lab,anchor=east] at (0.3,2.0) {start: $\mu=1,\,2$};
\node[hl dot] at (1,2.0) {};
\node[dot] at (2,2.0) {};
\node[dot] at (3,2.0) {};
\node[dot] at (10,2.0) {};
\node[dot] at (11,2.0) {};
\node[dot] at (12,2.0) {};
\node[lab] at (1,2.38) {$\times$};
\node[lab] at (2,2.38) {$\times$};
\draw[faint] (0.5,1.0) -- (12.5,1.0);
\node[lab,anchor=east] at (0.3,1.0) {update: $\mu=1,\,7.6$};
\node[hl dot] at (1,1.0) {};
\node[hl dot] at (2,1.0) {};
\node[hl dot] at (3,1.0) {};
\node[dot] at (10,1.0) {};
\node[dot] at (11,1.0) {};
\node[dot] at (12,1.0) {};
\node[lab] at (1,1.38) {$\times$};
\node[lab] at (7.6,1.38) {$\times$};
\draw[faint] (0.5,0.0) -- (12.5,0.0);
\node[lab,anchor=east] at (0.3,0.0) {converged: $\mu=2,\,11$};
\node[hl dot] at (1,0.0) {};
\node[hl dot] at (2,0.0) {};
\node[hl dot] at (3,0.0) {};
\node[dot] at (10,0.0) {};
\node[dot] at (11,0.0) {};
\node[dot] at (12,0.0) {};
\node[lab] at (2,0.38) {$\times$};
\node[lab] at (11,0.38) {$\times$};
\end{tikzpicture}
\end{center}
```

$k$-means on the six points of @exm-k-means-line: centroids ($\times$) and clusters (filled: cluster 1) at each iteration.

:::

::: {#rmk-k-means-1 .remark name="Local optima and the choice of k"}

$k$-means is coordinate descent on $J$ (@thm-k-means-converges), and $J$ is not convex in $(c,\boldsymbol\mu)$, so the result depends on the starting centroids. The usual remedy is to run it from several random starts and keep the run of smallest distortion; spreading the initial centroids apart (as in *k-means++*) also helps. The number of clusters $k$ is a modelling choice: the distortion always falls as $k$ grows, so it cannot choose $k$ by itself. A probabilistic version with soft assignments is the Gaussian mixture model of @sec-ai-unsupervised-learning-gaussian-mixtures.

:::
