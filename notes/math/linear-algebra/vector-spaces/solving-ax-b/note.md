---
title: "Solving Ax = b"
sources: [mit1806-8]
requires: [math/linear-algebra/vector-spaces/nullspace]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 8, in our own wording; proofs written out in steps. Example numbers checked with sympy. -->

To solve $A\mathbf{x}=\mathbf{b}$, eliminate on the augmented matrix $[A\ \mathbf{b}]$. A zero row of $R$ turns into an equation $0=c$; the system is solvable exactly when every such $c$ is $0$.

::: {#thm-complete-solution .theorem name="Complete solution of Ax = b"}

If $A\mathbf{x}=\mathbf{b}$ has a solution $\mathbf{x}_p$, then its solutions are exactly
$$\mathbf{x}=\mathbf{x}_p+\mathbf{x}_n,\qquad \mathbf{x}_n\in N(A).$$
A *particular solution* is found by setting all free variables to $0$ and solving for the pivot variables.

:::

::: {.proof}

1. If $A\mathbf{x}_n=\mathbf{0}$ then $A(\mathbf{x}_p+\mathbf{x}_n)=\mathbf{b}+\mathbf{0}=\mathbf{b}$.

2. Conversely, if $A\mathbf{x}=\mathbf{b}$ then $A(\mathbf{x}-\mathbf{x}_p)=\mathbf{0}$, so $\mathbf{x}-\mathbf{x}_p\in N(A)$.

3. With the free variables at $0$, each nonzero row of the reduced system gives its pivot variable directly, so the particular solution exists whenever the zero rows are consistent.

:::

::: {#fig-solving-ax-b-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.1]
\draw[->] (-1.6,0) -- (3.4,0); \draw[->] (0,-0.9) -- (0,2.8);
\draw[emph, primary] (-1.5,-0.75) -- (3.2,1.6) node[lab, right] {$N(A)$};
\draw[emph, accent] (-1.4,1.25) -- (2.6,3.25) node[lab, right] {$\mathbf x_p+N(A)$};
\draw[->, emph] (0,0) -- (-0.4,1.6) node[lab, left] {$\mathbf x_p$};
\draw[->, emph, primary] (0,0) -- (1.6,0.8) node[lab, below right] {$\mathbf x_n$};
\draw[faint, dashed] (-0.4,1.6) -- (1.2,2.4) -- (1.6,0.8);
\draw[->, hl] (0,0) -- (1.2,2.4) node[lab, above left] {$\mathbf x$};
\end{tikzpicture}
\end{center}
```

The complete solution $\mathbf x=\mathbf x_p+\mathbf x_n$: the solutions of $A\mathbf x=\mathbf b$ are the nullspace shifted by one particular solution. For $\mathbf b\neq\mathbf 0$ the shifted copy misses $\mathbf 0$, so it is not a subspace.

:::

::: {#exm-complete-solution .example name="A complete solution"}

For $A$ of @exm-nullspace-three-by-four, row 3 of $A$ is row 1 plus row 2, so $A\mathbf{x}=\mathbf{b}$ is solvable only if $b_3=b_1+b_2$. For $\mathbf{b}=(1,4,5)$:
$$[A\ \mathbf{b}]\to\begin{bmatrix}1&2&0&1&1\\0&0&1&2&2\\0&0&0&0&0\end{bmatrix},\qquad \mathbf{x}_p=(1,0,2,0),$$
$$\mathbf{x}=(1,0,2,0)+c\,(-2,1,0,0)+d\,(-1,0,-2,1).$$

:::

::: {#fig-solving-ax-b-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,1.100) rectangle (0.550,1.650);
\node[lab] at (0.275,1.375) {$1$};
\draw[cell frame] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$2$};
\draw[cell frame] (1.100,1.100) rectangle (1.650,1.650);
\node[lab] at (1.375,1.375) {$0$};
\draw[cell frame] (1.650,1.100) rectangle (2.200,1.650);
\node[lab] at (1.925,1.375) {$1$};
\draw[cell frame] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$2$};
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$4$};
\draw[cell frame] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$1$};
\draw[cell frame] (1.650,0.550) rectangle (2.200,1.100);
\node[lab] at (1.925,0.825) {$4$};
\draw[cell frame] (0.000,-0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$3$};
\draw[cell frame] (0.550,-0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$6$};
\draw[cell frame] (1.100,-0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$1$};
\draw[cell frame] (1.650,-0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$5$};
\draw[cell frame] (2.25,1.10) rectangle (4.05,1.65); \node[lab] at (3.15,1.375) {$b_1$};
\draw[cell frame] (2.25,0.55) rectangle (4.05,1.10); \node[lab] at (3.15,0.82) {$b_2$};
\draw[cell frame] (2.25,-2.22e-16) rectangle (4.05,0.55); \node[lab] at (3.15,0.27) {$b_3$};
\draw[bold, ink] (2.22,1.7) -- (2.22,-0.05);
\draw[->] (4.25,0.825) -- (5.05,0.825);
\draw[cell frame] (5.250,1.100) rectangle (5.800,1.650);
\node[lab] at (5.525,1.375) {$1$};
\draw[cell frame] (5.800,1.100) rectangle (6.350,1.650);
\node[lab] at (6.075,1.375) {$2$};
\draw[cell frame] (6.350,1.100) rectangle (6.900,1.650);
\node[lab] at (6.625,1.375) {$0$};
\draw[cell frame] (6.900,1.100) rectangle (7.450,1.650);
\node[lab] at (7.175,1.375) {$1$};
\draw[cell frame] (5.250,0.550) rectangle (5.800,1.100);
\node[lab] at (5.525,0.825) {$0$};
\draw[cell frame] (5.800,0.550) rectangle (6.350,1.100);
\node[lab] at (6.075,0.825) {$0$};
\draw[cell frame] (6.350,0.550) rectangle (6.900,1.100);
\node[lab] at (6.625,0.825) {$1$};
\draw[cell frame] (6.900,0.550) rectangle (7.450,1.100);
\node[lab] at (7.175,0.825) {$2$};
\draw[hl cell] (5.250,-0.000) rectangle (5.800,0.550);
\node[lab] at (5.525,0.275) {$0$};
\draw[hl cell] (5.800,-0.000) rectangle (6.350,0.550);
\node[lab] at (6.075,0.275) {$0$};
\draw[hl cell] (6.350,-0.000) rectangle (6.900,0.550);
\node[lab] at (6.625,0.275) {$0$};
\draw[hl cell] (6.900,-0.000) rectangle (7.450,0.550);
\node[lab] at (7.175,0.275) {$0$};
\draw[cell frame] (7.5,1.10) rectangle (9.3,1.65); \node[lab] at (8.4,1.375) {$b_1$};
\draw[cell frame] (7.5,0.55) rectangle (9.3,1.10); \node[lab] at (8.4,0.82) {$b_2-2b_1$};
\draw[hl cell] (7.5,-2.22e-16) rectangle (9.3,0.55); \node[lab] at (8.4,0.27) {$b_3-b_2-b_1$};
\draw[bold, ink] (7.47,1.7) -- (7.47,-0.05);
\node[lab, note, anchor=west, align=left] at (9.5,0.6) {$0=b_3-b_2-b_1$:\\solvable only if\\$b_3=b_1+b_2$};
\end{tikzpicture}
\end{center}
```

Elimination on $[A\ \mathbf b]$ in @exm-complete-solution with a general right side. The zero row of $A$ turns into the condition $b_3-b_2-b_1=0$, the equation of the plane $C(A)$; $\mathbf b=(1,4,5)$ satisfies it.

:::

::: {#thm-rank-and-solutions .theorem name="Rank decides the number of solutions"}

Let $A$ be $m\times n$ with rank $r$ (so $r\le m$ and $r\le n$).

1. $r=m=n$ (square, invertible): exactly one solution for every $\mathbf{b}$.
2. $r=n<m$ (full column rank): no free variables, $N(A)=\{\mathbf{0}\}$; zero or one solution.
3. $r=m<n$ (full row rank): no zero rows in $R$; infinitely many solutions for every $\mathbf{b}$.
4. $r<m$ and $r<n$: zero or infinitely many solutions.

:::

::: {.proof}

1. Solvability for every $\mathbf{b}$ fails exactly when $R$ has a zero row ($r<m$): choose $\mathbf{b}$ so that that row of the eliminated right side is nonzero, which is possible because the elimination matrix is invertible.

2. When a solution exists, @thm-complete-solution says it is unique exactly when $N(A)=\{\mathbf{0}\}$, i.e. when there are no free variables ($r=n$), by @thm-special-solutions; otherwise there are infinitely many.

3. Combining the two answers gives the four cases.

:::

::: {#fig-solving-ax-b-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\draw[hl cell] (0,0) rectangle (1.4,-1.4); \node[lab] at (0.7,-0.7) {$I$};
\node[lab, note] at (0.7,-1.75) {$r=m=n$};
\node[lab, tick] at (0.7,-2.1) {exactly one solution};
\end{scope}
\begin{scope}[shift={(2.6,0)}]
\draw[hl cell] (0,0) rectangle (1.4,-0.9); \node[lab] at (0.7,-0.45) {$I$};
\draw[cell frame] (0,-0.9) rectangle (1.4,-1.4); \node[lab] at (0.7,-1.15) {$0$};
\node[lab, note] at (0.7,-1.75) {$r=n<m$};
\node[lab, tick] at (0.7,-2.1) {0 or 1 solution};
\end{scope}
\begin{scope}[shift={(5.2,0)}]
\draw[hl cell] (0,0) rectangle (0.8,-1.4); \node[lab] at (0.4,-0.7) {$I$};
\draw[cell frame] (0.8,0) rectangle (1.6,-1.4); \node[lab] at (1.20,-0.7) {$F$};
\node[lab, note] at (0.7,-1.75) {$r=m<n$};
\node[lab, tick] at (0.7,-2.1) {$\infty$ solutions};
\end{scope}
\begin{scope}[shift={(7.9,0)}]
\draw[hl cell] (0,0) rectangle (0.8,-0.9); \node[lab] at (0.4,-0.45) {$I$};
\draw[cell frame] (0.8,0) rectangle (1.6,-0.9); \node[lab] at (1.20,-0.45) {$F$};
\draw[cell frame] (0,-0.9) rectangle (1.6,-1.4); \node[lab] at (0.8,-1.15) {$0$};
\node[lab, note] at (0.7,-1.75) {$r<m$, $r<n$};
\node[lab, tick] at (0.7,-2.1) {0 or $\infty$};
\end{scope}
\end{tikzpicture}
\end{center}
```

The four shapes of $R$ (columns reordered so the pivot columns come first). Zero rows make some $\mathbf b$ unsolvable; free columns $F$ give a nullspace and so infinitely many solutions whenever there is one.

:::

::: {#rmk-solving-ax-b-1 .remark name="The shape of R in the four cases"}

The reduced forms are $R=I$; $R=\begin{bmatrix}I\\0\end{bmatrix}$; $R=\begin{bmatrix}I&F\end{bmatrix}$; $R=\begin{bmatrix}I&F\\0&0\end{bmatrix}$ (with the pivot columns moved to the front).

:::
