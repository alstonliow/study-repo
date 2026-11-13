---
title: "Some special graphs"
sources: [fit1058-cn-11.6]
requires: [math/discrete/graph/degree]
level: core
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

```{=latex}
\begin{center}
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
\node (p0) at (0,0) {};
\node (p1) at (1.6,0) {};
\node (p2) at (1.6,1.6) {};
\node (p3) at (0,1.6) {};
\draw (p0)--(p1) (p1)--(p2) (p2)--(p3) (p3)--(p0) (p0)--(p2) (p1)--(p3);
\end{tikzpicture}
\qquad
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
\node at (0,0) {};
\node at (1.6,0) {};
\node at (1.6,1.6) {};
\node at (0,1.6) {};
\end{tikzpicture}
\qquad
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
\node (p0) at (0,0) {};
\node (p1) at (1.6,0) {};
\node (p2) at (1.6,1.6) {};
\node (p3) at (0,1.6) {};
\draw (p3)--(p0) (p0)--(p1) (p1)--(p2);
\end{tikzpicture}
\qquad
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
\node (p0) at (0,0) {};
\node (p1) at (1.6,0) {};
\node (p2) at (1.6,1.6) {};
\node (p3) at (0,1.6) {};
\draw (p0)--(p1) (p1)--(p2) (p2)--(p3) (p3)--(p0);
\end{tikzpicture}
\end{center}
```

$K_4$,  $\overline{K_4}$,  $P_3$,  $C_4$ (left to right)

```{=latex}
\begin{center}
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
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
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
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

```{=latex}
\begin{center}
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
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
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1pt,minimum size=5mm,font=\tiny}]
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
