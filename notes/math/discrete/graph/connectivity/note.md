---
title: "Connectivity"
sources: [fit1058-cn-11.9]
requires: [math/discrete/graph/basic-definitions, math/discrete/relations/equivalence-relations]
status: draft
---

<!-- Migrated from 1058note notes/chapters/10-graph-theory.tex: Connectivity. -->

::: {#def-connected-graph-component .definition name="Connected graph, component"}

Vertices $v,w$ are *connected* if there is a path (equivalently, a walk) between them. $G$ is *connected* if every pair of vertices is connected. A *component* of $G$ is a maximal connected subgraph.

:::

::: {#prp-connectivity-1 .proposition}

Being connected is an equivalence relation on $V$, and its equivalence classes are exactly the vertex sets of the components of $G$.

:::

::: {.proof}

**Reflexive**: the walk of length $0$.  **Symmetric**: reverse the walk.  **Transitive**: join a walk from $u$ to $v$ with a walk from $v$ to $w$. So it is an equivalence relation, and its classes partition $V$ (@sec-math-discrete-relations-equivalence-relations); each class is a maximal set of mutually connected vertices, i.e. the vertex set of a component.

:::

```{=latex}
\begin{center}
\begin{tikzpicture}[every node/.style={circle,draw,fill=white,inner sep=1.5pt,minimum size=6mm}]
\node (a) at (0,1.5) {$a$};
\node (b) at (0,0) {$b$};
\node (c) at (1.3,0.75) {$c$};
\node (d) at (2.6,0.75) {$d$};
\node (e) at (4.5,0.75) {$e$};
\node (f) at (6,1.5) {$f$};
\node (g) at (6,0) {$g$};
\draw (a)--(b) (a)--(c) (b)--(c) (c)--(d) (f)--(g);
\begin{scope}[on background layer]
\filldraw[fill=blue!10,draw=blue,rounded corners] (-0.6,-0.6) rectangle (3.2,2.1);
\filldraw[fill=red!10,draw=red,rounded corners] (4.1,0.35) rectangle (4.9,1.15);
\filldraw[fill=green!10,draw=green!50!black,rounded corners] (5.5,-0.6) rectangle (6.5,2.1);
\end{scope}
\end{tikzpicture}
\end{center}
```

The three components of the graph of @sec-math-discrete-graph-basic-definitions; each shaded region is one equivalence class
