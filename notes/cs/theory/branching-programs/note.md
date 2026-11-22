---
title: "Branching Programs and Arithmetization"
sources: [mit18404j-23, mit18404j-24]
requires: [cs/theory/probabilistic-computation]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lectures 23 and 24, in our own wording; proofs written out in steps. -->

## Branching programs

::: {#def-branching-program .definition name="Branching program"}

A *branching program* (BP) is a directed acyclic graph with one *start* node and two *output* nodes labelled $0$ and $1$. Every other node is a *query* node labelled by a variable $x_i$ and has two outgoing edges labelled $0$ and $1$. On an assignment to $x_1,\dots,x_m$, follow the path from the start that takes, at each query node, the edge given by the value of its variable; the output node reached is the value. Two BPs are *equivalent* ($B_1\equiv B_2$) if they compute the same Boolean function. A BP is *read-once* (an ROBP) if no path queries a variable more than once.

:::

::: {#exm-robp .example name="A read-once branching program"}

The ROBP $B$ of the figure queries $x_1$, then $x_2$, then possibly $x_3$, and computes $x_1\wedge(x_2\vee x_3)$. On $x_1=1,x_2=0,x_3=1$ it follows $x_1\xrightarrow{1}x_2\xrightarrow{0}x_3\xrightarrow{1}$ output $1$.

:::

::: {#fig-branching-programs-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[state] (1) at (0,0) {$x_1$};
\node[state] (2) at (2.2,-1.1) {$x_2$};
\node[state] (3) at (3.0,-2.6) {$x_3$};
\node[box] (o0) at (0.6,-4.0) {$0$};
\node[box] (o1) at (5.4,-4.0) {$1$};
\draw[start] (1.west) -- ++(-0.6,0);
\draw[trans] (1) -- node[edge label] {1} (2);
\draw[trans] (1) -- node[edge label] {0} (o0);
\draw[trans] (2) -- node[edge label] {0} (3);
\draw[trans] (2) to[bend left=15] node[edge label] {1} (o1);
\draw[trans] (3) -- node[edge label] {1} (o1);
\draw[trans] (3) -- node[edge label] {0} (o0);
\end{tikzpicture}
\end{center}
```

The ROBP of @exm-robp, computing $x_1\wedge(x_2\vee x_3)$.

:::

Equivalence of general BPs, $EQ_{\mathsf{BP}}$, is coNP-complete (two BPs differ iff some assignment witnesses it, and a CNF formula can be turned into a BP). For read-once programs a randomized test works. Comparing the two programs on random Boolean inputs does not: they may differ on a single one of the $2^m$ assignments.

## Arithmetization

::: {#def-arithmetization-bp .definition name="Arithmetizing an ROBP"}

Fix a finite field $\mathbb F_q$. Let an assignment give each $x_i$ a value $a_i\in\mathbb F_q$, not necessarily $0$ or $1$. Give the start node the value $1$; an edge labelled $1$ out of a node querying $x_i$ carries (node value)$\cdot a_i$ and an edge labelled $0$ carries (node value)$\cdot(1-a_i)$; the value of every other node is the sum of the values on its incoming edges. The value $p_B(a_1,\dots,a_m)$ of $B$ is the value of the output node $1$.

:::

On Boolean inputs this is the ordinary computation: exactly one path carries the value $1$ and all other edges carry $0$. In general $p_B$ is a sum over paths to output $1$ of products of factors $a_i$ or $1-a_i$. One can rewrite $B$ to query every variable on every path (insert a query whose two edges go to the same node; this multiplies by $a_i+(1-a_i)=1$). Then every term is a product of exactly one factor $a_i$ or $1-a_i$ per variable, so $p_B$ is determined by the truth table of $B$:

$$
p_B(x_1,\dots,x_m)=\sum_{b\in\{0,1\}^m: B(b)=1}\ \prod_{i=1}^m \ell_{b_i}(x_i),\qquad \ell_1(x)=x,\ \ell_0(x)=1-x.
$$

::: {#prp-robp-polynomial .proposition name="Equivalent ROBPs have equal polynomials"}

For ROBPs $B_1,B_2$: $B_1\equiv B_2$ iff $p_{B_1}=p_{B_2}$ as polynomials. Each $p_{B}$ has degree at most $1$ in each variable.

:::

::: {.proof}

1. If $B_1\equiv B_2$ they have the same truth table, so the displayed formula gives the same polynomial.

2. If $p_{B_1}=p_{B_2}$, they agree in particular at all Boolean points, where they compute the outputs, so $B_1\equiv B_2$.

3. Read-once means each path has at most one factor for each variable, so each variable has degree at most 1.

:::

::: {#exm-arithmetize-robp .example name="Evaluating at a non-Boolean point"}

For the ROBP of @exm-robp, $p_B=x_1\big(x_2+(1-x_2)x_3\big)$. At $(a_1,a_2,a_3)=(2,3,4)$ over $\mathbb F_7$: the node $x_2$ gets $2$, the node $x_3$ gets $2\cdot(1-3)=-4\equiv3$, and output $1$ gets $2\cdot3+3\cdot4=18\equiv4$. Output $0$ gets $1\cdot(1-2)+3\cdot(1-4)=-10\equiv4$; the two outputs always sum to $1$. Another ROBP that queries $x_3$ before $x_2$ computes $x_1(x_3+(1-x_3)x_2)$, the same polynomial, so it also gives $4$.

:::

::: {#fig-branching-programs-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[state] (1) at (0,0) {$x_1$};
\node[state] (2) at (2.2,-1.1) {$x_2$};
\node[state] (3) at (3.0,-2.6) {$x_3$};
\node[box] (o0) at (0.6,-4.0) {$0$};
\node[hl box] (o1) at (5.4,-4.0) {$1$};
\draw[start] (1.west) -- ++(-0.6,0);
\draw[trans] (1) -- node[edge label] {$1\cdot2$} (2);
\draw[trans] (1) -- node[edge label] {$1\cdot(-1)$} (o0);
\draw[trans] (2) -- node[edge label] {$2\cdot(-2)$} (3);
\draw[trans] (2) to[bend left=15] node[edge label] {$2\cdot3$} (o1);
\draw[trans] (3) -- node[edge label] {$3\cdot4$} (o1);
\draw[trans] (3) -- node[edge label] {$3\cdot(-3)$} (o0);
\node[lab, note] at (0,0.55) {1};
\node[lab, note] at (2.2,-0.55) {2};
\node[lab, note] at (3.0,-3.15) {3};
\node[lab, note] at (5.4,-4.55) {$18\equiv4$};
\node[lab, note] at (0.6,-4.55) {$-10\equiv4$};
\end{tikzpicture}
\end{center}
```

The arithmetization of @exm-arithmetize-robp over $\mathbb F_7$ at $(2,3,4)$: node values next to the nodes, edge values as products (node value times $a_i$ or $1-a_i$).

:::

## The randomized equivalence test

::: {#lem-poly-roots .lemma name="Roots of a polynomial"}

A nonzero polynomial of degree at most $d$ in one variable over a field has at most $d$ roots. Hence, for $a$ chosen uniformly from $\mathbb F_q$, $\Pr[p(a)=0]\le d/q$.

:::

::: {.proof}

1. If $r$ is a root, then $p(x)=(x-r)p_1(x)$ with $\deg p_1=\deg p-1$, by division with remainder.

2. By induction on the degree, $p$ factors as a product of at most $d$ linear factors $x-r_i$ times a polynomial without roots, so its roots are among the $r_i$.

:::

::: {#thm-schwartz-zippel .theorem name="Schwartz–Zippel"}

Let $p(x_1,\dots,x_m)\ne0$ over $\mathbb F_q$ have degree at most $d$ in each variable. If $a_1,\dots,a_m$ are chosen independently and uniformly from $\mathbb F_q$, then

$$
\Pr[p(a_1,\dots,a_m)=0]\le\frac{md}{q}.
$$

:::

::: {.proof}

1. Induct on $m$; the case $m=1$ is @lem-poly-roots.

2. Write $p=\sum_{j=0}^{d}x_1^j\,p_j(x_2,\dots,x_m)$. As $p\ne0$, some $p_j\ne0$.

3. By induction, $\Pr[p_j(a_2,\dots,a_m)=0]\le(m-1)d/q$.

4. If $p_j(a_2,\dots,a_m)\ne0$, then $p(x_1,a_2,\dots,a_m)$ is a nonzero polynomial in $x_1$ of degree at most $d$, which vanishes at the random $a_1$ with probability at most $d/q$.

5. Adding the two failure probabilities gives at most $(m-1)d/q+d/q=md/q$.

:::

::: {#thm-eq-robp-bpp .theorem name="$EQ_{\mathsf{ROBP}}\in\mathrm{BPP}$"}

:::

::: {.proof}

1. On input $\langle B_1,B_2\rangle$ with $m$ variables, choose a prime $q\ge3m$, pick $a_1,\dots,a_m\in\mathbb F_q$ at random, and evaluate $p_{B_1}(a)$ and $p_{B_2}(a)$ by @def-arithmetization-bp, in polynomial time.

2. Accept iff the two values are equal.

3. If $B_1\equiv B_2$ then $p_{B_1}=p_{B_2}$ (@prp-robp-polynomial) and the test always accepts.

4. Otherwise $p=p_{B_1}-p_{B_2}$ is a nonzero polynomial of degree at most $1$ in each variable, and by @thm-schwartz-zippel the test accepts with probability at most $m/q\le\tfrac13$.

:::

```{=latex}
\begin{algorithm}
\caption{Randomized equivalence test for ROBPs}
\begin{algorithmic}
\INPUT read-once branching programs $B_1,B_2$ on $x_1,\dots,x_m$
\STATE choose a prime $q\ge3m$; pick $a_1,\dots,a_m\in\mathbb F_q$ uniformly at random
\FOR{$B\in\{B_1,B_2\}$}
    \STATE value of the start node $\gets1$
    \FOR{each node $v$ in topological order, $v$ querying $x_i$}
        \STATE send (value of $v$)$\cdot a_i$ along its $1$-edge and (value of $v$)$\cdot(1-a_i)$ along its $0$-edge
    \ENDFOR
    \STATE $p_B(a)\gets$ value of output node $1$
\ENDFOR
\RETURN accept iff $p_{B_1}(a)=p_{B_2}(a)$
\end{algorithmic}
\end{algorithm}
```
