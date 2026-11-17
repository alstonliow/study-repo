---
title: "Shortest Paths, Parenthesization and Fingering by Dynamic Programming"
sources: [mit6006-17, mit6006r-17]
requires: [cs/dynamic-programming/subproblem-design, cs/graph-algorithms/all-pairs-shortest-paths]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 17 and Recitation 17, in our own wording; examples our own (checked by computation); proofs written out in steps. -->

## Shortest paths as dynamic programs

Shortest paths in a graph with cycles do not form an acyclic family of subproblems: $\delta(s,v)$ may depend on $\delta(s,u)$ and the other way round. *Expanding* the subproblems with the number of edges makes them acyclic.

::: {#exm-bellman-ford-dp .example name="Bellman–Ford as a dynamic program"}

1. *Subproblems:* $\delta_k(s,v)$, the least weight of a walk from $s$ to $v$ with at most $k$ edges (@def-k-edge-distance), for $v\in V$ and $0\le k\le|V|$.
2. *Relation:* guess the last edge: $\delta_k(s,v)=\min\bigl(\{\delta_{k-1}(s,u)+w(u,v):(u,v)\in E\}\cup\{\delta_{k-1}(s,v)\}\bigr)$.
3. *Order:* increasing $k$. 4. *Base:* $\delta_0(s,s)=0$, $\delta_0(s,v)=\infty$ for $v\ne s$.
5. *Original:* $\delta(s,v)=\delta_{|V|-1}(s,v)$ unless some witness shows $-\infty$ (@lem-witnesses).
6. *Time:* $\sum_{k=0}^{|V|}\sum_vO(1+\deg^-(v))=O(|V|(|V|+|E|))$.

This is exactly Bellman–Ford (@thm-bellman-ford), computed in a different order.

:::

For all pairs, the same idea costs $|V|$ times as much, $O(|V|^2|E|)$. A cleverer choice of subproblems has constant branching.

::: {#thm-floyd-warshall .theorem name="Floyd–Warshall"}

Let $G$ have vertices $1,\dots,|V|$ and no negative-weight cycle. Let $d(u,v,k)$ be the least weight of a path from $u$ to $v$ all of whose *intermediate* vertices (other than $u$ and $v$) lie in $\{1,\dots,k\}$. Then $d(u,u,0)=0$, $d(u,v,0)=w(u,v)$ if $(u,v)\in E$ and $\infty$ otherwise, and for $k\ge1$
$$d(u,v,k)=\min\bigl\{d(u,v,k-1),\ d(u,k,k-1)+d(k,v,k-1)\bigr\}.$$
Computing all $d(u,v,k)$ in order of increasing $k$ gives $\delta(u,v)=d(u,v,|V|)$ in $\Theta(|V|^3)$ time.

:::

::: {.proof}

1. Without negative-weight cycles, a lightest walk can be taken to be a path (as in @lem-simple-shortest-paths), so $\delta(u,v)=d(u,v,|V|)$, and minimising over walks or over paths with the same intermediate vertices gives the same value.

2. *Base:* with no intermediate vertex allowed, a path from $u$ to $v$ is empty ($u=v$) or a single edge.

3. *Relation.* Take a lightest path $\pi$ from $u$ to $v$ with intermediate vertices in $\{1,\dots,k\}$. If $k$ is not on $\pi$ as an intermediate vertex, its weight is $d(u,v,k-1)$. Otherwise $k$ appears once, and splits $\pi$ into a path from $u$ to $k$ and a path from $k$ to $v$, both with intermediate vertices in $\{1,\dots,k-1\}$, so its weight is at least $d(u,k,k-1)+d(k,v,k-1)$. Conversely, both options in the minimum are weights of walks with intermediate vertices in $\{1,\dots,k\}$, so they are at least $d(u,v,k)$ by step 1.

4. *Time:* $|V|^2(|V|+1)$ subproblems with $O(1)$ work each.

:::

This matches Johnson's algorithm (@thm-johnson) on dense graphs and is much simpler to implement. A negative entry $d(u,u,|V|)<0$ reveals a negative-weight cycle.

## Parenthesization

::: {#exm-arithmetic-parenthesization .example name="Arithmetic parenthesization"}

Given an expression $a_0\ast_1a_1\ast_2\cdots\ast_{n-1}a_{n-1}$ with integers $a_i$ (possibly negative) and operations $\ast_i\in\{+,\times\}$, place parentheses to make its value as large as possible. For $2\times(-3)+1\times(-4)$ the best is $\bigl(2\times(-3)+1\bigr)\times(-4)=20$.

Maximising each part is not enough: $(-3)\times(-3)>(-2)\times(-2)$, so a large product may need two very *negative* factors. So we expand the subproblems with both goals.

1. *Subproblems:* $x(i,j,\mathrm{opt})$, the minimum ($\mathrm{opt}=\min$) or maximum ($\mathrm{opt}=\max$) value of $a_i\ast_{i+1}\cdots\ast_{j-1}a_{j-1}$ over all parenthesizations, for $0\le i<j\le n$.
2. *Relation:* guess the operation $\ast_k$ evaluated last, and the extreme of each side:
   $$x(i,j,\mathrm{opt})=\mathrm{opt}\bigl\{x(i,k,\mathrm{opt}')\ast_kx(k,j,\mathrm{opt}''):i<k<j;\ \mathrm{opt}',\mathrm{opt}''\in\{\min,\max\}\bigr\}.$$
   This is right because the left side ranges over values in $[x(i,k,\min),x(i,k,\max)]$ and the right side over $[x(k,j,\min),x(k,j,\max)]$, and $l+r$ and $l\times r$ are linear in each argument separately, so their extremes over such a rectangle are reached at its corners.
3. *Order:* increasing $j-i$. 4. *Base:* $x(i,i+1,\mathrm{opt})=a_i$.
5. *Original:* $x(0,n,\max)$; parent pointers (two per subproblem) give the parenthesization as a binary tree.
6. *Time:* $O(n^2)$ subproblems with $O(n)$ work each: $O(n^3)$.

In the example, $x(0,4,\min)=-14$, from $2\times\bigl(-3+1\times(-4)\bigr)$.

:::

## Fingering

::: {#exm-piano-fingering .example name="Piano fingering"}

A pianist plays single notes $t_0,\dots,t_{n-1}$ with the right hand, using fingers $1,\dots,F$. A given function $d(t,f,t',f')$ measures the difficulty of moving from note $t$ played with finger $f$ to note $t'$ played with finger $f'$ (a sum of penalties for awkward crossings, weak fingers and so on). Assign fingers to minimise the total difficulty.

The suffix subproblem "best difficulty for $t_i,\dots,t_{n-1}$" is not enough: the cost of the next transition depends on which finger the rest starts with. So expand with that finger.

1. *Subproblems:* $x(i,f)$, the least total difficulty for $t_i,\dots,t_{n-1}$ when $t_i$ is played with finger $f$.
2. *Relation:* guess the finger for $t_{i+1}$: $x(i,f)=\min_{1\le f'\le F}\bigl\{d(t_i,f,t_{i+1},f')+x(i+1,f')\bigr\}$.
3. *Order:* decreasing $i$. 4. *Base:* $x(n-1,f)=0$. 5. *Original:* $\min_fx(0,f)$.
6. *Time:* $nF$ subproblems with $O(F)$ work: $O(nF^2)$, independent of how many different notes there are.

For a guitar, a "finger" becomes a pair (finger, string), replacing $F$ by $FS$ for $S$ strings. If several notes sound at once, each step chooses an assignment of fingers to at most $T$ notes, at most $F^T$ choices, so $O(nF^{2T})$ time, which is linear in $n$ for fixed small $F$ and $T$.

:::
