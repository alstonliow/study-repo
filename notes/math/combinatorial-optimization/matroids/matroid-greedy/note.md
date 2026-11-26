---
title: "The Greedy Algorithm on a Matroid"
sources: [mit18433-5]
requires: [math/combinatorial-optimization/matroids/matroids]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on matroid optimization (Section 5.2), in our own wording; example our own (checked by brute force); proofs written out in steps. The converse (greedy works only on matroids) is stated without proof, as in the course. -->

Given a matroid $M=(E,\mathcal I)$ and weights $c:E\to\mathbb R$, we want an independent set $S$ of largest weight $c(S)=\sum_{e\in S}c(e)$. Elements of negative weight never help, by (I1); with nonnegative weights the problem asks for a heaviest base. For the graphic matroid this is the maximum spanning tree problem.

::: {#def-matroid-greedy .definition name="Greedy algorithm for matroids"}

Sort $E$ as $e_1,\dots,e_m$ with $c(e_1)\ge c(e_2)\ge\dots\ge c(e_m)$. Start with $S_0=\varnothing$ and $k=0$. For $j=1,\dots,m$: if $S_k+e_j\in\mathcal I$, set $S_{k+1}=S_k+e_j$, call this element $s_{k+1}$, and increase $k$. Output $S_1,S_2,\dots$; for a maximum weight independent set, output the last $S_k$ obtained from the elements of nonnegative weight.

:::

```{=latex}
\begin{algorithm}
\caption{Greedy algorithm on a matroid}
\begin{algorithmic}
\INPUT matroid $M=(E,\mathcal I)$ with an independence test, weights $c$
\OUTPUT $S_k$ of maximum weight among independent sets of size $k$, for each $k$
\STATE sort $E$ so that $c(e_1)\ge\dots\ge c(e_m)$; $S_0\gets\varnothing$; $k\gets0$
\FOR{$j=1$ \TO $m$}
\IF{$S_k+e_j\in\mathcal I$} \STATE $S_{k+1}\gets S_k+e_j$; $k\gets k+1$ \ENDIF
\ENDFOR
\RETURN $S_1,\dots,S_k$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-matroid-greedy .theorem name="Greedy is optimal on matroids"}

For every matroid and every weight function, the set $S_k$ produced by the greedy algorithm has maximum weight among all independent sets of size $k$, for every $k$.

:::

::: {.proof}

1. Write $S_k=\{s_1,\dots,s_k\}$ in the order chosen, so $c(s_1)\ge\dots\ge c(s_k)$. Suppose some independent $T=\{t_1,\dots,t_k\}$ with $c(t_1)\ge\dots\ge c(t_k)$ has $c(T)>c(S_k)$. Then $c(t_p)>c(s_p)$ for some $p$; take the first such $p$.

2. Let $A=\{t_1,\dots,t_p\}$ and $B=\{s_1,\dots,s_{p-1}\}$. Both are independent and $|A|>|B|$, so by (I2) some $t_i\in A\setminus B$ has $B+t_i\in\mathcal I$.

3. Now $c(t_i)\ge c(t_p)>c(s_p)$, so the algorithm examined $t_i$ before $s_p$, at a moment when its current set $S$ was a subset of $B$. Since $B+t_i$ is independent, so is $S+t_i$ by (I1), and the algorithm would have taken $t_i$; then $t_i\in B$, contradicting $t_i\in A\setminus B$.

:::

As long as $c(s_k)\ge0$, adding $s_k$ does not decrease the weight, so the last set built from the nonnegative elements is a maximum weight independent set. For the graphic matroid, the greedy algorithm is Kruskal's algorithm (@def-kruskal), run with the heaviest edges first.

::: {#rmk-greedy-characterizes-matroids .remark name="Greedy characterises matroids"}

The converse also holds: an independence system on which the greedy algorithm finds a maximum weight set of each size, for every weight function, is a matroid. For example, on the matchings of the path $1$–$2$–$3$–$4$ with weights $c(23)=3$, $c(12)=c(34)=2$, greedy stops at $\{23\}$ of weight $3$, while $\{12,34\}$ weighs $4$.

:::

::: {#exm-matroid-greedy-small .example name="Greedy on a linear matroid"}

Take the columns $a_1=(1,0)$, $a_2=(0,1)$, $a_3=(1,1)$, $a_4=(2,0)$ of @exm-matroid-circuit-small with weights $c=(5,4,3,6)$. The order is $4,1,2,3$. Greedy takes $4$, rejects $1$ (parallel to $4$), takes $2$, and rejects $3$ (the rank is already $2$). It returns $\{2,4\}$ of weight $10$; the other bases weigh $9$, $8$, $7$ and $9$.

:::

::: {#fig-matroid-greedy-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.000,0.000) rectangle (0.900,0.900);
\node[lab] at (0.450,0.450) {$6$};
\draw[cell frame] (0.900,0.000) rectangle (1.800,0.900);
\node[lab] at (1.350,0.450) {$5$};
\draw[hl cell] (1.800,0.000) rectangle (2.700,0.900);
\node[lab] at (2.250,0.450) {$4$};
\draw[cell frame] (2.700,0.000) rectangle (3.600,0.900);
\node[lab] at (3.150,0.450) {$3$};
\node[lab] at (0.450,1.15) {$4$};
\node[lab, tick] at (0.450,-0.3) {take};
\node[lab] at (1.350,1.15) {$1$};
\node[lab, tick] at (1.350,-0.3) {skip};
\node[lab] at (2.250,1.15) {$2$};
\node[lab, tick] at (2.250,-0.3) {take};
\node[lab] at (3.150,1.15) {$3$};
\node[lab, tick] at (3.150,-0.3) {skip};
\node[lab, anchor=east] at (-0.15,0.45) {$c(e)$};
\node[lab, anchor=east] at (-0.15,1.15) {$e$};
\end{tikzpicture}
\end{center}
```

Greedy on the example, elements in order of decreasing weight: $4$ and $2$ are taken (highlighted), $1$ is skipped as parallel to $4$, and $3$ as the rank is already $2$. The result $\{2,4\}$ has weight $10$.

:::
