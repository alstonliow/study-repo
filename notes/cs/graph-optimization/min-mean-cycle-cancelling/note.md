---
title: "Minimum Mean Cycle Cancelling and Cancel-and-Tighten"
sources: [mit6854-4, mit6854-5, mit6854-7]
requires: [cs/graph-optimization/min-cost-circulation]
status: draft
---

<!-- Added 2026-11-26 from MIT 6.854J (Fall 2008, Goemans), Lecture 4 (Sections 2.1-2.4), Lecture 5 (Sections 1-2) and Lecture 7 (Section 2), in our own wording; proofs written out in steps. Notation of @def-min-cost-circulation: capacities c, costs a. -->

Klein's algorithm (@def-cycle-cancelling) is only pseudo-polynomial for a careless choice of cycles. Goldberg and Tarjan (1986) showed that cancelling a cycle of *minimum mean cost* makes it strongly polynomial: the number of iterations depends on $n$ and $m$ only, even for irrational costs. Throughout, $n=|V|$, $m=|E|$.

## Measuring progress

::: {#def-epsilon-optimal .definition name="Minimum mean cost, $\varepsilon$-optimality"}

For a circulation $f$ let
$$\mu(f)=\min_{\Gamma\text{ cycle of }G_f}\frac{a(\Gamma)}{|\Gamma|},$$
$|\Gamma|$ being the number of edges. $f$ is *$\varepsilon$-optimal* if some potential $p$ has $a_p(v,w)\ge-\varepsilon$ for all $(v,w)\in E_f$, and $\varepsilon(f)$ is the least $\varepsilon$ for which $f$ is $\varepsilon$-optimal.

:::

$G_f$ has a negative cycle exactly when $\mu(f)<0$, and by @thm-circulation-optimality $f$ is optimal exactly when $\varepsilon(f)\le0$.

::: {#thm-epsilon-equals-mean .theorem name="$\varepsilon(f)=-\mu(f)$"}

For every circulation $f$, $\varepsilon(f)=-\mu(f)$. Moreover there is a potential $p$ with $a_p\ge\mu(f)$ on $E_f$, and for it every edge of a minimum mean cycle has $a_p(v,w)=\mu(f)$.

:::

::: {.proof}

1. *$\mu\ge-\varepsilon$.* Take $p$ with $a_p\ge-\varepsilon(f)$ on $E_f$. For a cycle $\Gamma$ of $G_f$, $a(\Gamma)=a_p(\Gamma)\ge-|\Gamma|\varepsilon(f)$ (@prp-reduced-cost).

2. *$\varepsilon\le-\mu$.* Lower every cost in $G_f$ by $\mu(f)$. Then every cycle has mean cost, hence cost, at least $0$. Let $p(v)$ be the least cost of a path to $v$ from an added vertex joined to all vertices by edges of cost $0$. Then $p(w)\le p(v)+a(v,w)-\mu(f)$, that is $a_p(v,w)\ge\mu(f)$ on $E_f$.

3. With this $p$, the reduced costs on a minimum mean cycle are all at least $\mu(f)$ and average to $\mu(f)$, so they all equal $\mu(f)$.

:::

So the minimum mean cycle is a cycle whose edges all have the most negative reduced cost allowed. The mean $\mu(f)$ can be computed in $O(nm)$ time with a variant of Bellman–Ford (Karp's algorithm), or by binary search on a shift $\lambda$ of all costs with one negative-cycle test per step.

## The algorithm

::: {#def-goldberg-tarjan .definition name="Minimum mean cycle cancelling (Goldberg–Tarjan)"}

Start with $f=0$. While $\mu(f)<0$, push $\min_{e\in\Gamma}c_f(e)$ units around a cycle $\Gamma$ of $G_f$ of mean cost $\mu(f)$.

:::

::: {#fig-min-mean-cycle-cancelling-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (m1) at (0,0) {$1$};
\node[small vertex] (m2) at (-1.8,0) {$2$};
\node[small vertex] (m3) at (1.5,1) {$3$};
\node[small vertex] (m4) at (1.5,-1) {$4$};
\draw[->, hl] (m1) to[bend left=25] node[edge label] {$-2$} (m2);
\draw[->, hl] (m2) to[bend left=25] node[edge label] {$-1$} (m1);
\draw[->, emph] (m1) -- node[edge label] {$-5$} (m3);
\draw[->, emph] (m3) -- node[edge label] {$1$} (m4);
\draw[->, emph] (m4) -- node[edge label] {$0$} (m1);
\node[lab] at (-0.9,-1.2) {mean $-1.5$};
\node[lab] at (2.6,0) {mean $-\tfrac43$};
\end{tikzpicture}
\end{center}
```

Two negative cycles: $1\,3\,4\,1$ has the smaller total cost ($-4$), but $1\,2\,1$ has the smaller mean ($-1.5$), so Goldberg–Tarjan cancels it.

:::

::: {#lem-goldberg-tarjan-progress .lemma name="Progress"}

$\varepsilon(f)$ never increases. After any $m$ consecutive iterations starting from $f$, the circulation $f'$ satisfies $\varepsilon(f')\le(1-1/n)\,\varepsilon(f)$.

:::

::: {.proof}

1. Fix the potential $p$ of @thm-epsilon-equals-mean for $f$, so $a_p\ge-\varepsilon(f)$ on $E_f$ and $a_p=-\varepsilon(f)$ on the cancelled cycle. Pushing around the cycle may delete residual edges and creates only reverses of cycle edges, whose reduced cost is $+\varepsilon(f)\ge0$. So $a_p\ge-\varepsilon(f)$ still holds: $\varepsilon$ does not increase.

2. Keep the same $p$ for the next $m$ iterations and let $A$ be the set of residual edges with $a_p<0$. While every cancelled cycle lies inside $A$, each cancellation removes at least one edge of $A$ (a saturated one) and adds none (new edges have $a_p>0$). So within $m$ iterations some cancelled cycle $\Gamma$ contains an edge with $a_p\ge0$, or $\mu$ reaches $0$ and we are done.

3. The other $|\Gamma|-1$ edges have $a_p\ge-\varepsilon(f)$, so at the moment $\Gamma$ is cancelled
$$\varepsilon=-\mu=-\frac{a_p(\Gamma)}{|\Gamma|}\le\frac{|\Gamma|-1}{|\Gamma|}\varepsilon(f)\le\Big(1-\frac1n\Big)\varepsilon(f),$$
using $|\Gamma|\le n$; by step 1 it stays below this bound.

:::

::: {#thm-goldberg-tarjan-integer .theorem name="Iterations with integer costs"}

If the costs are integers of absolute value at most $C$, the algorithm stops after at most $mn\lceil\ln(nC)\rceil$ iterations.

:::

::: {.proof}

1. At the start $p=0$ shows $\varepsilon(0)\le C$.

2. If $\varepsilon(f)<1/n$, every cycle of $G_f$ has $a(\Gamma)=a_p(\Gamma)>-|\Gamma|/n\ge-1$, hence $a(\Gamma)\ge0$ as it is an integer; $f$ is optimal.

3. By @lem-goldberg-tarjan-progress, after $mn\lceil\ln(nC)\rceil$ iterations $\varepsilon\le(1-1/n)^{n\ln(nC)}C<e^{-\ln(nC)}C=1/n$.

:::

For arbitrary real costs the argument uses edges whose flow can no longer change.

::: {#def-fixed-edge .definition name="Fixed edge"}

An edge $e$ is *$\varepsilon$-fixed* if $f(e)$ has the same value for every $\varepsilon$-optimal circulation $f$.

:::

::: {#lem-fixed-edge .lemma name="Large reduced costs fix edges"}

Let $\varepsilon=\varepsilon(f)>0$ and let $p$ show that $f$ is $\varepsilon$-optimal. If $|a_p(v,w)|\ge2n\varepsilon$, then $(v,w)$ is $\varepsilon$-fixed.

:::

::: {.proof}

1. By skew symmetry we may assume $a_p(v,w)\le-2n\varepsilon$. Then $(v,w)$ is not residual for $f$ (its reduced cost is below $-\varepsilon$), so $f(v,w)=c(v,w)$. Suppose some $\varepsilon$-optimal $f'$ has $f'(v,w)\ne f(v,w)$; then $f'(v,w)<f(v,w)$.

2. The circulation $f-f'$ is positive on $(v,w)$. Decomposing it into cycles (@thm-flow-decomposition), some cycle $\Gamma$ through $(v,w)$ has $f'(x,y)<f(x,y)$ on all its edges $(x,y)$.

3. Each edge of $\Gamma$ is residual for $f'$, since $f'(x,y)<f(x,y)\le c(x,y)$. Each reverse edge $(y,x)$ is residual for $f$, since $f(y,x)=-f(x,y)<-f'(x,y)=f'(y,x)\le c(y,x)$; so $a_p(y,x)\ge-\varepsilon$, that is $a_p(x,y)\le\varepsilon$.

4. Hence $a(\Gamma)=a_p(\Gamma)\le-2n\varepsilon+(|\Gamma|-1)\varepsilon<-n\varepsilon\le-|\Gamma|\varepsilon$. So $\Gamma$ is a cycle of $G_{f'}$ of mean cost below $-\varepsilon$, and by @thm-epsilon-equals-mean $\varepsilon(f')=-\mu(f')>\varepsilon$: $f'$ is not $\varepsilon$-optimal, a contradiction.

:::

::: {#thm-goldberg-tarjan-strong .theorem name="Strongly polynomial bound"}

Minimum mean cycle cancelling stops after $O(m^2n\log n)$ iterations, for any real costs.

:::

::: {.proof}

1. Let $f$ be the current circulation, not optimal, and $\Gamma$ the cycle cancelled next, so $a(\Gamma)/|\Gamma|=\mu(f)=-\varepsilon(f)$. Run $k=mn\lceil\ln(2n)\rceil$ further iterations to reach $f'$; by @lem-goldberg-tarjan-progress, $\varepsilon(f')<\varepsilon(f)/(2n)$.

2. Let $p'$ show that $f'$ is $\varepsilon(f')$-optimal. Then $a_{p'}(\Gamma)=a(\Gamma)=-|\Gamma|\varepsilon(f)<-2n|\Gamma|\varepsilon(f')$, so some edge $e$ of $\Gamma$ has $a_{p'}(e)<-2n\varepsilon(f')$. By @lem-fixed-edge, $e$ is $\varepsilon(f')$-fixed.

3. $e$ was not $\varepsilon(f)$-fixed: $f$ and the circulation right after cancelling $\Gamma$ are both $\varepsilon(f)$-optimal (by step 1 of @lem-goldberg-tarjan-progress) and differ on $e$.

4. Since $\varepsilon$ never increases, an edge once fixed stays fixed. So every block of $k$ iterations fixes a new edge, and there are $m$ edges.

:::

Each iteration costs $O(nm)$ (finding the cycle), so the total is $O(m^3n^2\log n)$, or $O(m^2n^2\log(nC))$ with integer costs.

## Cancel-and-tighten

Finding an exact minimum mean cycle is the expensive part. It suffices to cancel cycles that are negative for one fixed potential and then repair the potential.

::: {#def-cancel-and-tighten .definition name="Cancel-and-tighten"}

Call $(v,w)\in E_f$ *admissible* for $p$ if $a_p(v,w)<0$, and a cycle admissible if all its edges are. Start with $f=0$, $p=0$, $\varepsilon=\max|a|$. While $f$ is not optimal:

1. *Cancel:* while $G_f$ has an admissible cycle, push the most flow possible around it.
2. *Tighten:* the admissible edges now form an acyclic graph. Number the vertices in a topological order $\ell:V\to\{1,\dots,n\}$ of it (@thm-dfs-topological-sort) and set $p(v)\gets p(v)-\ell(v)\varepsilon/n$ and $\varepsilon\gets(1-1/n)\varepsilon$.

:::

```{=latex}
\begin{algorithm}
\caption{Cancel-and-tighten}
\begin{algorithmic}
\INPUT graph with capacities $c$, costs $a$
\OUTPUT a minimum-cost circulation $f$
\STATE $f\gets0$; $p\gets0$; $\varepsilon\gets\max_e|a(e)|$
\WHILE{$G_f$ has a negative cycle}
\WHILE{$G_f$ has a cycle $\Gamma$ with $a_p(e)<0$ for all $e\in\Gamma$}
\STATE push $\min_{e\in\Gamma}c_f(e)$ around $\Gamma$
\ENDWHILE
\STATE $\ell\gets$ topological order of the admissible edges
\STATE $p(v)\gets p(v)-\ell(v)\varepsilon/n$ for all $v$; $\varepsilon\gets(1-1/n)\varepsilon$
\ENDWHILE
\RETURN $f$
\end{algorithmic}
\end{algorithm}
```

::: {#lem-cancel-and-tighten .lemma name="One round of cancel-and-tighten"}

If $a_p\ge-\varepsilon$ on $E_f$ before a round, then the cancel step cancels at most $m$ cycles, and after the tighten step $a_p\ge-(1-1/n)\varepsilon$ on $E_f$.

:::

::: {.proof}

1. Cancelling an admissible cycle saturates at least one admissible edge, and the new residual edges are reverses of admissible ones, with $a_p>0$. So the number of admissible edges drops by one each time: at most $m$ cancellations, and $a_p\ge-\varepsilon$ still holds.

2. After tightening, $a_{p'}(v,w)=a_p(v,w)+\big(\ell(w)-\ell(v)\big)\varepsilon/n$ for every residual edge.

3. If $(v,w)$ is admissible, $\ell(w)\ge\ell(v)+1$, so $a_{p'}(v,w)\ge-\varepsilon+\varepsilon/n$.

4. Otherwise $a_p(v,w)\ge0$ and $\ell(w)-\ell(v)\ge-(n-1)$, so $a_{p'}(v,w)\ge-(n-1)\varepsilon/n$.

:::

::: {#fig-min-mean-cycle-cancelling-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (qu) at (0,0) {$u$};
\node[small vertex] (qv) at (1.6,0.8) {$v$};
\node[small vertex] (qw) at (1.6,-0.8) {$w$};
\node[small vertex] (qz) at (3.2,0) {$z$};
\node[lab, tick] at (0,0.45) {$\ell=1$};
\node[lab, tick] at (1.6,1.25) {$\ell=2$};
\node[lab, tick] at (1.6,-0.35) {$\ell=3$};
\node[lab, tick] at (3.2,0.45) {$\ell=4$};
\draw[->, hl] (qu)--(qv);
\draw[->, hl] (qu)--(qw);
\draw[->, hl] (qv)--(qw);
\draw[->, hl] (qw)--(qz);
\draw[->, faint] (qz) to[bend right=40] (qv);
\end{tikzpicture}
\end{center}
```

Tightening: after the cancel step the admissible edges (thick) form an acyclic graph; with a topological numbering $\ell$, lowering $p(v)$ by $\ell(v)\varepsilon/n$ raises every admissible reduced cost by at least $\varepsilon/n$, and lowers the others (thin) by at most $(n-1)\varepsilon/n$.

:::

The proofs of @thm-goldberg-tarjan-integer and @thm-goldberg-tarjan-strong carry over with rounds in place of blocks of $m$ iterations, giving $O\big(\min(n\log(nC),\,mn\log n)\big)$ rounds. A depth-first search that deletes dead-end edges as it backtracks finds all cycles of one cancel step in $O(nm)$ time; with link-cut trees (@thm-link-cut-trees) each cycle costs $O(\log n)$ amortized and a cancel step $O(m\log n)$.

::: {#rmk-min-mean-cycle-cancelling-1 .remark name="Running times"}

With the plain search, cancel-and-tighten runs in $O\big(\min(mn^2\log(nC),\,m^2n^2\log n)\big)$; with dynamic trees, in $O\big(\min(mn\log n\log(nC),\,m^2n\log^2n)\big)$. Minimum-cost circulation was the first large class of linear programs shown to be solvable in strongly polynomial time (Tardos, 1985); whether general linear programming is, is open.

:::
