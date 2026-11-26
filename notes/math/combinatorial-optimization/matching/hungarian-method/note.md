---
title: "The Assignment Problem and the Hungarian Method"
sources: [mit18433-1]
requires: [math/combinatorial-optimization/matching/konig-theorem, math/combinatorial-optimization/polyhedra/lp-duality]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on bipartite matching (Section 1.2), in our own wording; example our own (checked by brute force over all permutations); proofs written out in steps. A second, algebraic proof of the integrality theorem is @thm-bipartite-incidence-tu with @thm-tu-integral-polyhedron. -->

::: {#def-assignment-problem .definition name="Assignment problem"}

Given a bipartite graph with sides $A$, $B$, $|A|=|B|=n/2$, and costs $c_{ij}$ for $i\in A$, $j\in B$, the *assignment problem* (or *minimum weight perfect matching problem*) asks for a perfect matching $M$ of least cost $c(M)=\sum_{ij\in M}c_{ij}$. Missing edges get cost $+\infty$, so the graph may be taken complete. Writing $x_{ij}=1$ for $ij\in M$ and $0$ otherwise, it is the integer program "minimise $\sum c_{ij}x_{ij}$ subject to (P), $x$ integral", where
$$(P)\qquad \sum_{j\in B}x_{ij}=1\ (i\in A),\qquad \sum_{i\in A}x_{ij}=1\ (j\in B),\qquad x\ge0 .$$
Dropping integrality gives the *linear programming relaxation*; its feasible set is the *bipartite perfect matching polytope*.

:::

For a minimisation problem the relaxation can only have a smaller optimum, $Z_{LP}\le Z_{IP}$, and an integral optimal solution of the relaxation solves the integer program. In general $Z_{LP}<Z_{IP}$ can happen, but not here.

::: {#prp-assignment-dual .proposition name="The dual bound"}

If numbers $u_i$ ($i\in A$) and $v_j$ ($j\in B$) satisfy $u_i+v_j\le c_{ij}$ for all $i,j$ (we write $w_{ij}=c_{ij}-u_i-v_j\ge0$ for the *reduced costs*), then every $x$ feasible for (P) has
$$\sum_{i,j}c_{ij}x_{ij}\ \ge\ \sum_{i\in A}u_i+\sum_{j\in B}v_j .$$
Equality holds exactly when $x_{ij}>0$ only on edges with $w_{ij}=0$.

:::

::: {.proof}

1. $\sum c_{ij}x_{ij}-\sum_{i,j}(u_i+v_j)x_{ij}=\sum w_{ij}x_{ij}\ge0$, since $w\ge0$ and $x\ge0$.

2. By the equality constraints of (P), $\sum_{i,j}(u_i+v_j)x_{ij}=\sum_iu_i\sum_jx_{ij}+\sum_jv_j\sum_ix_{ij}=\sum_iu_i+\sum_jv_j$.

3. Equality holds iff $\sum w_{ij}x_{ij}=0$, that is iff $w_{ij}x_{ij}=0$ for all $i,j$.

:::

So maximising $\sum u_i+\sum v_j$ subject to $u_i+v_j\le c_{ij}$ is the dual LP (D) of (P) (@def-lp-primal-dual), and the equality condition is complementary slackness (@thm-lp-complementary-slackness). A *primal–dual* algorithm keeps a feasible dual $(u,v)$ and looks for a perfect matching among the *tight* edges $E_=\{ij:w_{ij}=0\}$; such a matching is optimal by @prp-assignment-dual.

::: {#def-hungarian-method .definition name="Hungarian method"}

1. Start with $u_i=0$ and $v_j=\min_ic_{ij}$, a feasible dual.
2. Find a maximum matching $M$ in the bipartite graph $(A\cup B,E_=)$ with the augmenting path algorithm (@def-bipartite-augmenting-algorithm). If $M$ is perfect, stop and return it.
3. Otherwise let $L$ be the set of vertices reachable from exposed vertices of $A$, as in the proof of @thm-konig, and
$$\delta=\min\{w_{ij}: i\in A\cap L,\ j\in B\setminus L\}.$$
4. Set $u_i\gets u_i+\delta$ for $i\in A\cap L$ and $v_j\gets v_j-\delta$ for $j\in B\cap L$, and go to step 2 (keeping $M$).

:::

```{=latex}
\begin{algorithm}
\caption{Hungarian method}
\begin{algorithmic}
\INPUT costs $c_{ij}$, $i\in A$, $j\in B$, $|A|=|B|$
\OUTPUT a minimum cost perfect matching $M$ and an optimal dual $(u,v)$
\STATE $u_i\gets0$; $v_j\gets\min_ic_{ij}$; $M\gets\varnothing$
\LOOP
\STATE $E_=\gets\{ij:c_{ij}-u_i-v_j=0\}$; enlarge $M$ to a maximum matching of $E_=$
\IF{$M$ is perfect} \RETURN $M,(u,v)$ \ENDIF
\STATE $L\gets$ vertices reachable from exposed vertices of $A$ in the oriented graph
\STATE $\delta\gets\min\{c_{ij}-u_i-v_j:i\in A\cap L,\ j\in B\setminus L\}$
\STATE $u_i\gets u_i+\delta$ ($i\in A\cap L$); $v_j\gets v_j-\delta$ ($j\in B\cap L$)
\ENDLOOP
\end{algorithmic}
\end{algorithm}
```

::: {#thm-hungarian-method .theorem name="Correctness of the Hungarian method"}

If a perfect matching of finite cost exists, the Hungarian method stops after $O(n^2)$ dual updates and returns a minimum cost perfect matching $M$ together with a dual $(u,v)$ of the same value. It runs in $O(n^4)$ time, and in $O(n^3)$ with more careful bookkeeping.

:::

::: {.proof}

1. *The dual stays feasible.* By the proof of @thm-konig there is no tight edge from $A\cap L$ to $B\setminus L$, so $\delta>0$. The reduced cost $w_{ij}$ falls by $\delta$ only for $i\in A\cap L$, $j\in B\setminus L$, where it was at least $\delta$; it rises for $i\in A\setminus L$, $j\in B\cap L$, and is unchanged otherwise.

2. *The dual value rises.* It changes by $\delta(|A\cap L|-|B\cap L|)=\delta\big(\frac n2-|C|\big)$, where $C=(A\setminus L)\cup(B\cap L)$ is the vertex cover of size $|M|<\frac n2$ from the proof of @thm-konig.

3. *$M$ stays tight and $L$ grows.* No edge of $M$ joins $A\setminus L$ to $B\cap L$ (step 4 of that proof) or $A\cap L$ to $B\setminus L$ (the matched partner of a vertex of $A\cap L$ is in $L$), so all edges of $M$ keep $w=0$. Every arc used to reach $L$ goes from $A\cap L$ to $B\cap L$ or from $B\cap L$ to $A\cap L$, where $w$ is unchanged, so $L$ does not shrink; and the edge attaining $\delta$ becomes tight, adding a vertex of $B$ to $L$.

4. *Counting.* After at most $|B|=\frac n2$ updates without augmentation, an exposed vertex of $B$ is reached and $M$ grows. $M$ grows at most $\frac n2$ times, so there are $O(n^2)$ updates, each costing $O(n^2)$ time for $L$ and $\delta$. (With finite costs the minimum in step 3 is finite as long as a perfect matching of finite cost exists.)

5. *Optimality.* At the end $M$ is a perfect matching inside $E_=$, so by @prp-assignment-dual its cost equals the dual value, which is a lower bound for every feasible $x$. Hence $M$ is optimal for (P) and for the assignment problem.

:::

::: {#thm-bipartite-perfect-matching-polytope .theorem name="Integrality of the bipartite perfect matching polytope"}

Every vertex of (P) is a $0$–$1$ vector, the incidence vector of a perfect matching.

:::

::: {.proof}

1. Let $x^*$ be a vertex of (P). The face $\{x^*\}$ comes from a valid inequality $\alpha^{\mathsf T}x\le\beta$ (@def-polyhedron-face), so $x^*$ is the unique minimiser of $c^{\mathsf T}x$ over (P) for $c=-\alpha$.

2. For this $c$ the Hungarian method returns a perfect matching whose incidence vector is optimal for (P). By uniqueness it equals $x^*$.

:::

::: {#exm-hungarian-small .example name="A $3\times3$ instance"}

Let $A=\{1,2,3\}$, $B=\{1',2',3'\}$ and costs $c=\begin{pmatrix}4&1&3\\2&0&5\\3&2&2\end{pmatrix}$ (row $i$, column $j'$).

1. Start: $u=(0,0,0)$, $v=(2,0,2)$, reduced costs $w=\begin{pmatrix}2&1&1\\0&0&3\\1&2&0\end{pmatrix}$, tight edges $21',22',33'$.
2. A maximum tight matching is $\{21',33'\}$; row $1$ is exposed and has no tight edge, so $L=\{1\}$ and $\delta=\min(2,1,1)=1$.
3. Update: $u=(1,0,0)$. Row $1$ of $w$ becomes $(1,0,0)$, so $12'$ and $13'$ are tight, and $\{12',21',33'\}$ is a perfect tight matching.

Its cost $1+2+2=5$ equals the dual value $\sum u_i+\sum v_j=1+4=5$, so it is optimal; checking all $6$ permutations confirms that $5$ is the minimum.

:::

::: {#fig-hungarian-method-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$2$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$1$};
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$1$};
\node[lab, anchor=east] at (-0.100,0.275) {$u_1=0$};
\draw[cell frame] (3.600,0.000) rectangle (4.150,0.550);
\node[lab] at (3.875,0.275) {$1$};
\draw[hl cell] (4.150,0.000) rectangle (4.700,0.550);
\node[lab] at (4.425,0.275) {$0$};
\draw[cell frame] (4.700,0.000) rectangle (5.250,0.550);
\node[lab] at (4.975,0.275) {$0$};
\node[lab, anchor=east] at (3.500,0.275) {$u_1=1$};
\draw[hl cell] (0.000,-0.550) rectangle (0.550,0.000);
\node[lab] at (0.275,-0.275) {$0$};
\draw[hl cell] (0.550,-0.550) rectangle (1.100,0.000);
\node[lab] at (0.825,-0.275) {$0$};
\draw[cell frame] (1.100,-0.550) rectangle (1.650,0.000);
\node[lab] at (1.375,-0.275) {$3$};
\node[lab, anchor=east] at (-0.100,-0.275) {$u_2=0$};
\draw[hl cell] (3.600,-0.550) rectangle (4.150,0.000);
\node[lab] at (3.875,-0.275) {$0$};
\draw[cell frame] (4.150,-0.550) rectangle (4.700,0.000);
\node[lab] at (4.425,-0.275) {$0$};
\draw[cell frame] (4.700,-0.550) rectangle (5.250,0.000);
\node[lab] at (4.975,-0.275) {$3$};
\node[lab, anchor=east] at (3.500,-0.275) {$u_2=0$};
\draw[cell frame] (0.000,-1.100) rectangle (0.550,-0.550);
\node[lab] at (0.275,-0.825) {$1$};
\draw[cell frame] (0.550,-1.100) rectangle (1.100,-0.550);
\node[lab] at (0.825,-0.825) {$2$};
\draw[hl cell] (1.100,-1.100) rectangle (1.650,-0.550);
\node[lab] at (1.375,-0.825) {$0$};
\node[lab, anchor=east] at (-0.100,-0.825) {$u_3=0$};
\draw[cell frame] (3.600,-1.100) rectangle (4.150,-0.550);
\node[lab] at (3.875,-0.825) {$1$};
\draw[cell frame] (4.150,-1.100) rectangle (4.700,-0.550);
\node[lab] at (4.425,-0.825) {$2$};
\draw[hl cell] (4.700,-1.100) rectangle (5.250,-0.550);
\node[lab] at (4.975,-0.825) {$0$};
\node[lab, anchor=east] at (3.500,-0.825) {$u_3=0$};
\node[lab] at (0.83,0.85) {$w$ at the start};
\node[lab] at (4.43,0.85) {$w$ after $\delta=1$};
\node[lab] at (2.5,-1.55) {$v=(2,0,2)$};
\end{tikzpicture}
\end{center}
```

Reduced costs $w_{ij}=c_{ij}-u_i-v_j$ of the example. Left: the tight entries (highlighted) admit no perfect matching, since row $1$ has none. Right: after the dual update the highlighted perfect matching $\{12',21',33'\}$ is tight, hence optimal.

:::
