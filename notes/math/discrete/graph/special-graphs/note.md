---
title: "Some special graphs"
sources: [fit1058-cn-11.6, cs70-5.4.3]
requires: [math/discrete/graph/basic-definitions]
status: draft
---

<!-- Migrated from 1058note notes/chapters/10-graph-theory.tex: Some special graphs. -->

::: {#def-families .definition name="Standard families"}

- $K_n$ (*complete graph*): $n$ vertices, every pair adjacent.

- $\overline{K_n}$ (*null graph*): $n$ vertices, no edges.

- $C_n$ (*cycle*): $v_1\sim v_2\sim\cdots\sim v_n\sim v_1$, for $n\ge3$.

- $P_{n-1}$ (*path of length $n-1$*): vertices $v_1,\dots,v_n$ with $v_i\sim v_j$ iff $|i-j|=1$.

- $K_{m,n}$ (*complete bipartite*): $V=A\sqcup B$ with $|A|=m$, $|B|=n$, and $v\sim w$ iff one is in $A$ and the other in $B$.

- $Q_n$ (*hypercube*): $V=\{0,1\}^n$, with $v\sim w$ iff they differ in exactly one coordinate.

:::

::: {#prp-edge-counts .proposition}

$|E(K_n)| = \binom n2$,  $|E(\overline{K_n})| = 0$,  $|E(P_{n-1})| = n-1$,  $|E(Q_n)| = n\cdot2^{n-1}$.

:::

::: {.proof}

In $K_n$ the edges are exactly the unordered pairs of distinct vertices, so there are $\binom n2$. The null graph has no edges. The edges of $P_{n-1}$ are $\{v_i,v_{i+1}\}$ for $i=1,\dots,n-1$. In $Q_n$ every vertex has degree $n$ (flip any one of the $n$ coordinates), so by the handshaking lemma (@thm-handshake) $|E|=n\cdot2^n/2=n2^{n-1}$.

:::

::: {#fig-special-graphs-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[dotgraph]
\node (p0) at (0,0) {};
\node (p1) at (1.6,0) {};
\node (p2) at (1.6,1.6) {};
\node (p3) at (0,1.6) {};
\draw (p0)--(p1) (p1)--(p2) (p2)--(p3) (p3)--(p0) (p0)--(p2) (p1)--(p3);
\end{tikzpicture}
\qquad
\begin{tikzpicture}[dotgraph]
\node at (0,0) {};
\node at (1.6,0) {};
\node at (1.6,1.6) {};
\node at (0,1.6) {};
\end{tikzpicture}
\qquad
\begin{tikzpicture}[dotgraph]
\node (p0) at (0,0) {};
\node (p1) at (1.6,0) {};
\node (p2) at (1.6,1.6) {};
\node (p3) at (0,1.6) {};
\draw (p3)--(p0) (p0)--(p1) (p1)--(p2);
\end{tikzpicture}
\qquad
\begin{tikzpicture}[dotgraph]
\node (p0) at (0,0) {};
\node (p1) at (1.6,0) {};
\node (p2) at (1.6,1.6) {};
\node (p3) at (0,1.6) {};
\draw (p0)--(p1) (p1)--(p2) (p2)--(p3) (p3)--(p0);
\end{tikzpicture}
\end{center}
```

$K_4$,  $\overline{K_4}$,  $P_3$,  $C_4$ (left to right)

:::

::: {#fig-special-graphs-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[dotgraph]
\foreach \i in {0,...,4} {
  \node (v\i) at ({90+\i*72}:1.6) {};
}
\foreach \i in {0,...,4} {
  \foreach \j in {0,...,4} {
    \ifnum\i<\j
      \draw (v\i)--(v\j);
    \fi
  }
}
\end{tikzpicture}
\qquad
\begin{tikzpicture}[dotgraph]
\foreach \i in {0,...,5} {
  \node (c\i) at ({60*\i}:1.6) {};
}
\foreach \i in {0,...,5} {
  \pgfmathtruncatemacro{\j}{mod(\i+1,6)}
  \draw (c\i)--(c\j);
}
\end{tikzpicture}
\end{center}
```

$K_5$ (left) and $C_6$ (right)

:::

::: {#fig-special-graphs-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[dotgraph]
\node (a1) at (0,1) {};
\node (a2) at (0,-1) {};
\node (b1) at (2.5,1.5) {};
\node (b2) at (2.5,0.5) {};
\node (b3) at (2.5,-0.5) {};
\foreach \a in {a1,a2} {
  \foreach \b in {b1,b2,b3} {
    \draw (\a)--(\b);
  }
}
\end{tikzpicture}
\qquad
\begin{tikzpicture}[every node/.style={small vertex, tick}]
\node (000) at (0,0) {000};
\node (100) at (1.5,0) {100};
\node (010) at (0,1.5) {010};
\node (001) at (0.6,0.6) {001};
\node (110) at (1.5,1.5) {110};
\node (101) at (2.1,0.6) {101};
\node (011) at (0.6,2.1) {011};
\node (111) at (2.1,2.1) {111};
\draw (000)--(100) (000)--(010) (000)--(001);
\draw (100)--(110) (100)--(101);
\draw (010)--(110) (010)--(011);
\draw (001)--(101) (001)--(011);
\draw (110)--(111) (101)--(111) (011)--(111);
\end{tikzpicture}
\end{center}
```

$K_{2,3}$ (left) and $Q_3$ (right)

:::

## The hypercube

::: {#rmk-special-graphs-hypercube-recursive .remark name="The hypercube, built recursively"}

$Q_n$ consists of two copies of $Q_{n-1}$: the *$0$-subcube* of strings $0x$ and the *$1$-subcube* of strings $1x$, for $x\in\{0,1\}^{n-1}$, with an edge from each $0x$ to the matching $1x$. This gives a second proof of $|E(Q_n)|=n2^{n-1}$: if $E(n)=|E(Q_n)|$, then $E(1)=1$ and $E(n)=2E(n-1)+2^{n-1}$, and induction gives $E(n)=2(n-1)2^{n-2}+2^{n-1}=n2^{n-1}$.

:::

::: {#thm-hypercube-cut .theorem name="The hypercube is hard to cut"}

Let $S$ be a set of vertices of $Q_n$ with $|S|\le2^{n-1}$, and let $E_S$ be the set of edges with one end in $S$ and the other outside $S$. Then $|E_S|\ge|S|$.

:::

::: {.proof}

By induction on $n$.

1. For $n=1$, $Q_1$ is a single edge. If $|S|=0$ the claim is trivial; if $|S|=1$, the one edge leaves $S$.

2. Let $n\ge2$ and assume the claim for $Q_{n-1}$. Split $S=S_0\cup S_1$ into its parts in the $0$-subcube and the $1$-subcube; each subcube has $2^{n-1}$ vertices.

3. **Case $|S_0|,|S_1|\le2^{n-2}$.** Apply the hypothesis inside each subcube: at least $|S_0|$ edges of the $0$-subcube leave $S_0$, and at least $|S_1|$ edges of the $1$-subcube leave $S_1$. These edges all leave $S$, so $|E_S|\ge|S_0|+|S_1|=|S|$.

4. **Case $|S_0|>2^{n-2}$** (the case $|S_1|>2^{n-2}$ is symmetric). Then $|S_1|=|S|-|S_0|<2^{n-2}$, so the hypothesis gives at least $|S_1|$ edges leaving $S_1$ in the $1$-subcube. In the $0$-subcube the complement $V_0\setminus S_0$ has fewer than $2^{n-2}$ vertices, so the hypothesis applied to it gives at least $2^{n-1}-|S_0|$ edges between $S_0$ and $V_0\setminus S_0$.

5. Each vertex $0x\in S_0$ is joined to $1x$, and at most $|S_1|$ of these partners are in $S$, so at least $|S_0|-|S_1|$ edges between the subcubes leave $S$.

6. Adding the three disjoint groups, $|E_S|\ge|S_1|+(2^{n-1}-|S_0|)+(|S_0|-|S_1|)=2^{n-1}\ge|S|$.

:::

::: {#rmk-special-graphs-hypercube-network .remark name="Why networks use hypercubes"}

$K_n$ is very hard to cut but needs $\binom n2$ edges; a tree uses the fewest edges but falls apart when one edge is removed. $Q_n$ connects $2^n$ vertices with only $n$ edges per vertex, and by @thm-hypercube-cut cutting off any set of vertices costs at least as many edges as the set has vertices. A parallel computer with a million processors was built on $Q_{20}$ for this reason.

:::
