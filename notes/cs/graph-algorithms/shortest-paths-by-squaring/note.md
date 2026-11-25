---
title: "All-Pairs Shortest Paths by Repeated Squaring"
sources: [mit6046-11]
requires: [cs/graph-algorithms/all-pairs-shortest-paths, cs/graph-algorithms/bellman-ford]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 11, in our own wording; proof written out in steps. Split from cs/graph-algorithms/all-pairs-shortest-paths on 2026-11-25 (one algorithm per note, SPEC §8.6). -->

Let $V=\{1,\dots,n\}$ and let $W$ be the $n\times n$ matrix with $W_{uu}=0$, $W_{uv}=w(u,v)$ for edges and $\infty$ otherwise. Let $D^{(m)}_{uv}$ be the least weight of a walk from $u$ to $v$ with at most $m$ edges, so $D^{(1)}=W$.

::: {#def-min-plus-product .definition name="Min-plus product"}

The *min-plus product* of $n\times n$ matrices $A$ and $B$ is $(A\otimes B)_{uv}=\min_k(A_{uk}+B_{kv})$: ordinary matrix multiplication with $+$ replaced by $\min$ and $\times$ by $+$.

:::

::: {#prp-shortest-paths-by-squaring .proposition name="Shortest paths by repeated squaring"}

$D^{(a+b)}=D^{(a)}\otimes D^{(b)}$. Hence, if $G$ has no negative-weight cycle, $\delta=D^{(n-1)}$ is computed by $\lceil\log_2(n-1)\rceil$ squarings $W,W^{\otimes2},W^{\otimes4},\dots$, in $O(n^3\log n)$ time.

:::

::: {.proof}

1. A walk from $u$ to $v$ with at most $a+b$ edges splits at some vertex $k$ into a walk with at most $a$ edges and one with at most $b$ (pad with the $0$-weight steps $W_{kk}=0$ if needed); conversely such pairs join into such a walk. Taking minima gives the product formula.

2. Without negative cycles, shortest walks can be taken with at most $n-1$ edges (@lem-simple-shortest-paths), so $D^{(m)}=\delta$ for every $m\ge n-1$; squaring overshoots harmlessly.

3. Each product takes $O(n^3)$ time, and there are $O(\log n)$ of them.

:::

```{=latex}
\begin{algorithm}
\caption{Shortest paths by repeated squaring}
\begin{algorithmic}
\INPUT Weight matrix $W$ of a digraph on $n$ vertices with no negative-weight cycle
\OUTPUT The matrix $\delta$ of shortest-path weights
\STATE $D\gets W$; $m\gets1$
\WHILE{$m<n-1$}
    \STATE $D\gets D\otimes D$ \COMMENT{$D_{uv}\gets\min_k(D_{uk}+D_{kv})$, $O(n^3)$}
    \STATE $m\gets2m$
\ENDWHILE
\RETURN $D$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-all-pairs-shortest-paths-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab] at (1.10,1.00) {$W=D^{(1)}$};
\node[lab,tick] at (-0.30,0.55) {$a$};
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$0$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$2$};
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$\infty$};
\draw[cell frame] (1.650,0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$4$};
\node[lab,tick] at (-0.30,0.00) {$b$};
\draw[cell frame] (0.000,-0.550) rectangle (0.550,0.000);
\node[lab] at (0.275,-0.275) {$\infty$};
\draw[cell frame] (0.550,-0.550) rectangle (1.100,0.000);
\node[lab] at (0.825,-0.275) {$0$};
\draw[cell frame] (1.100,-0.550) rectangle (1.650,0.000);
\node[lab] at (1.375,-0.275) {$-3$};
\draw[cell frame] (1.650,-0.550) rectangle (2.200,0.000);
\node[lab] at (1.925,-0.275) {$\infty$};
\node[lab,tick] at (-0.30,-0.55) {$c$};
\draw[cell frame] (0.000,-1.100) rectangle (0.550,-0.550);
\node[lab] at (0.275,-0.825) {$2$};
\draw[cell frame] (0.550,-1.100) rectangle (1.100,-0.550);
\node[lab] at (0.825,-0.825) {$\infty$};
\draw[cell frame] (1.100,-1.100) rectangle (1.650,-0.550);
\node[lab] at (1.375,-0.825) {$0$};
\draw[cell frame] (1.650,-1.100) rectangle (2.200,-0.550);
\node[lab] at (1.925,-0.825) {$\infty$};
\node[lab,tick] at (-0.30,-1.10) {$d$};
\draw[cell frame] (0.000,-1.650) rectangle (0.550,-1.100);
\node[lab] at (0.275,-1.375) {$\infty$};
\draw[cell frame] (0.550,-1.650) rectangle (1.100,-1.100);
\node[lab] at (0.825,-1.375) {$\infty$};
\draw[cell frame] (1.100,-1.650) rectangle (1.650,-1.100);
\node[lab] at (1.375,-1.375) {$1$};
\draw[cell frame] (1.650,-1.650) rectangle (2.200,-1.100);
\node[lab] at (1.925,-1.375) {$0$};
\node[lab,tick] at (0.28,0.72) {$a$};
\node[lab,tick] at (0.83,0.72) {$b$};
\node[lab,tick] at (1.38,0.72) {$c$};
\node[lab,tick] at (1.93,0.72) {$d$};
\node[lab] at (4.50,1.00) {$D^{(2)}$};
\node[lab,tick] at (3.10,0.55) {$a$};
\draw[cell frame] (3.400,0.000) rectangle (3.950,0.550);
\node[lab] at (3.675,0.275) {$0$};
\draw[cell frame] (3.950,0.000) rectangle (4.500,0.550);
\node[lab] at (4.225,0.275) {$2$};
\draw[hl cell] (4.500,0.000) rectangle (5.050,0.550);
\node[lab] at (4.775,0.275) {$-1$};
\draw[cell frame] (5.050,0.000) rectangle (5.600,0.550);
\node[lab] at (5.325,0.275) {$4$};
\node[lab,tick] at (3.10,0.00) {$b$};
\draw[hl cell] (3.400,-0.550) rectangle (3.950,0.000);
\node[lab] at (3.675,-0.275) {$-1$};
\draw[cell frame] (3.950,-0.550) rectangle (4.500,0.000);
\node[lab] at (4.225,-0.275) {$0$};
\draw[cell frame] (4.500,-0.550) rectangle (5.050,0.000);
\node[lab] at (4.775,-0.275) {$-3$};
\draw[cell frame] (5.050,-0.550) rectangle (5.600,0.000);
\node[lab] at (5.325,-0.275) {$\infty$};
\node[lab,tick] at (3.10,-0.55) {$c$};
\draw[cell frame] (3.400,-1.100) rectangle (3.950,-0.550);
\node[lab] at (3.675,-0.825) {$2$};
\draw[hl cell] (3.950,-1.100) rectangle (4.500,-0.550);
\node[lab] at (4.225,-0.825) {$4$};
\draw[cell frame] (4.500,-1.100) rectangle (5.050,-0.550);
\node[lab] at (4.775,-0.825) {$0$};
\draw[hl cell] (5.050,-1.100) rectangle (5.600,-0.550);
\node[lab] at (5.325,-0.825) {$6$};
\node[lab,tick] at (3.10,-1.10) {$d$};
\draw[hl cell] (3.400,-1.650) rectangle (3.950,-1.100);
\node[lab] at (3.675,-1.375) {$3$};
\draw[cell frame] (3.950,-1.650) rectangle (4.500,-1.100);
\node[lab] at (4.225,-1.375) {$\infty$};
\draw[cell frame] (4.500,-1.650) rectangle (5.050,-1.100);
\node[lab] at (4.775,-1.375) {$1$};
\draw[cell frame] (5.050,-1.650) rectangle (5.600,-1.100);
\node[lab] at (5.325,-1.375) {$0$};
\node[lab,tick] at (3.67,0.72) {$a$};
\node[lab,tick] at (4.22,0.72) {$b$};
\node[lab,tick] at (4.78,0.72) {$c$};
\node[lab,tick] at (5.33,0.72) {$d$};
\node[lab] at (7.90,1.00) {$D^{(4)}$};
\node[lab,tick] at (6.50,0.55) {$a$};
\draw[cell frame] (6.800,0.000) rectangle (7.350,0.550);
\node[lab] at (7.075,0.275) {$0$};
\draw[cell frame] (7.350,0.000) rectangle (7.900,0.550);
\node[lab] at (7.625,0.275) {$2$};
\draw[cell frame] (7.900,0.000) rectangle (8.450,0.550);
\node[lab] at (8.175,0.275) {$-1$};
\draw[cell frame] (8.450,0.000) rectangle (9.000,0.550);
\node[lab] at (8.725,0.275) {$4$};
\node[lab,tick] at (6.50,0.00) {$b$};
\draw[cell frame] (6.800,-0.550) rectangle (7.350,0.000);
\node[lab] at (7.075,-0.275) {$-1$};
\draw[cell frame] (7.350,-0.550) rectangle (7.900,0.000);
\node[lab] at (7.625,-0.275) {$0$};
\draw[cell frame] (7.900,-0.550) rectangle (8.450,0.000);
\node[lab] at (8.175,-0.275) {$-3$};
\draw[hl cell] (8.450,-0.550) rectangle (9.000,0.000);
\node[lab] at (8.725,-0.275) {$3$};
\node[lab,tick] at (6.50,-0.55) {$c$};
\draw[cell frame] (6.800,-1.100) rectangle (7.350,-0.550);
\node[lab] at (7.075,-0.825) {$2$};
\draw[cell frame] (7.350,-1.100) rectangle (7.900,-0.550);
\node[lab] at (7.625,-0.825) {$4$};
\draw[cell frame] (7.900,-1.100) rectangle (8.450,-0.550);
\node[lab] at (8.175,-0.825) {$0$};
\draw[cell frame] (8.450,-1.100) rectangle (9.000,-0.550);
\node[lab] at (8.725,-0.825) {$6$};
\node[lab,tick] at (6.50,-1.10) {$d$};
\draw[cell frame] (6.800,-1.650) rectangle (7.350,-1.100);
\node[lab] at (7.075,-1.375) {$3$};
\draw[hl cell] (7.350,-1.650) rectangle (7.900,-1.100);
\node[lab] at (7.625,-1.375) {$5$};
\draw[cell frame] (7.900,-1.650) rectangle (8.450,-1.100);
\node[lab] at (8.175,-1.375) {$1$};
\draw[cell frame] (8.450,-1.650) rectangle (9.000,-1.100);
\node[lab] at (8.725,-1.375) {$0$};
\node[lab,tick] at (7.08,0.72) {$a$};
\node[lab,tick] at (7.62,0.72) {$b$};
\node[lab,tick] at (8.18,0.72) {$c$};
\node[lab,tick] at (8.72,0.72) {$d$};
\end{tikzpicture}
\end{center}
```

Repeated squaring on the graph of @fig-all-pairs-shortest-paths-1 ($n=4$; row $u$, column $v$). Squaring $W$ gives the lightest walks with at most $2$ edges, and squaring again those with at most $4\ge n-1$ edges, which are the shortest-path weights. Highlighted entries changed in that squaring.

:::

The min-plus product has no subtraction, so Strassen's trick (@thm-strassen) does not apply directly. Floyd–Warshall (@thm-floyd-warshall) gets $O(n^3)$, and Johnson's algorithm $O(n^2\log n+n|E|)$; but the matrix view gives *transitive closure* (is there a path?) by Boolean matrix multiplication, which can use fast matrix multiplication, in $O(n^{\omega}\log n)$ time with $\omega<2.38$.
