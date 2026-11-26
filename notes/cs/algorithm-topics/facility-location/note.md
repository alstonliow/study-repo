---
title: "Facility Location: Primal–Dual and Local Search"
sources: [mit6854-17]
requires: [cs/algorithm-topics/lp-rounding-and-primal-dual]
status: draft
---

<!-- Added 2026-11-26 from MIT 6.854J (Fall 2008, Goemans), Lecture 17, in our own wording; proofs written out in steps; the second inequality of the local search bound is stated without proof, as in the course. One note for the problem and its two algorithms (concept note, SPEC §8.6). -->

In the *uncapacitated facility location* problem we are given facilities $F$ with opening costs $f_i\ge0$, clients $D$, and connection costs $c_{ij}\ge0$ that are distances of a metric on $F\cup D$. We open a set $U\subseteq F$ and connect every client to its nearest open facility, paying
$$\sum_{i\in U}f_i+\sum_{j\in D}\min_{i\in U}c_{ij}.$$
The problem is NP-hard. Two simple $3$-approximations illustrate two design techniques; the best known ratio is about $1.5$, and $1.463$ cannot be beaten unless $\mathrm{NP}\subseteq\mathrm{DTIME}(n^{O(\log\log n)})$.

## The linear program

With $y_i$ = "facility $i$ is open" and $x_{ij}$ = "client $j$ uses facility $i$", the LP relaxation and its dual are
$$\min\Big\{\sum_if_iy_i+\sum_{i,j}c_{ij}x_{ij}:\sum_ix_{ij}=1\ \forall j,\ \ y_i-x_{ij}\ge0,\ \ x,y\ge0\Big\},$$
$$\max\Big\{\sum_jv_j:\sum_jw_{ij}\le f_i\ \forall i,\ \ v_j-w_{ij}\le c_{ij}\ \forall i,j,\ \ w\ge0\Big\}.$$
Read the dual as payments: client $j$ offers $v_j$; if $v_j>c_{ij}$ the surplus $w_{ij}=v_j-c_{ij}$ goes towards opening $i$, and $i$ can be paid for when the surpluses reach $f_i$.

## The primal–dual algorithm

::: {#def-facility-location-primal-dual .definition name="Primal–dual facility location (Jain–Vazirani)"}

1. *Dual ascent.* Raise all $v_j$ together at rate $1$ (time $t=v_j$). When $v_j$ reaches $c_{ij}$ for a facility $i$ not yet paid for, start raising $w_{ij}$ with $v_j$. When $\sum_jw_{ij}=f_i$, facility $i$ is *paid for* at time $t_i$: stop raising all $w_{ij}$ and freeze every $v_j$ with $w_{ij}>0$. When $v_j$ reaches $c_{ij}$ for an $i$ already paid for, freeze $v_j$. Stop when all $v_j$ are frozen; for each $j$, let the facility that froze it be its *witness*.
2. *Pruning.* Join $i$ and $j$ when $w_{ij}>0$. Go through the paid-for facilities in order of $t_i$ and open $i$ unless it shares a client neighbour with an already opened facility.
3. Connect each client to its nearest open facility.

:::

The values stay dual feasible throughout, so $\sum_jv_j\le\mathrm{LP}\le\mathrm{OPT}$.

::: {#thm-facility-location-primal-dual .theorem name="The primal–dual algorithm is a 3-approximation"}

With $U$ the opened facilities and $\sigma(j)$ the facility of client $j$,
$$3\sum_{i\in U}f_i+\sum_jc_{\sigma(j)j}\le3\sum_jv_j\le3\,\mathrm{OPT}.$$

:::

::: {.proof}

1. Opened facilities share no client neighbour, so each client $j$ has at most one opened neighbour (an $i\in U$ with $w_{ij}>0$).

2. *Client with an opened neighbour $i$.* Then $w_{ij}>0$, so $v_j=c_{ij}+w_{ij}$, and $c_{\sigma(j)j}\le c_{ij}$. Hence $c_{\sigma(j)j}+3w_{ij}\le3v_j$. Summing over these clients, and using $\sum_jw_{ij}=f_i$ for each $i\in U$ (all its contributors are such clients), pays for all opening costs.

3. *Client without an opened neighbour.* It contributes nothing to opening costs; it suffices to find an open facility within distance $3v_j$. Let $i$ be its witness: $c_{ij}\le v_j$ and $t_i\le v_j$. If $i\in U$ we are done.

4. Otherwise $i$ was skipped because of an opened $i'$ with $t_{i'}\le t_i$ sharing a client neighbour $j'$. A positive $w_{ij'}$ means $c_{ij'}<v_{j'}\le t_i$, and likewise $c_{i'j'}\le t_{i'}$. By the triangle inequality
$$c_{i'j}\le c_{i'j'}+c_{ij'}+c_{ij}\le t_{i'}+t_i+v_j\le3v_j.$$

5. Adding the two kinds of clients gives the inequality; the last step is weak duality.

:::

::: {#exm-facility-location .example name="Two facilities, three clients"}

Facilities $1,2$ with $f_1=f_2=2$; clients $a,b,c$ with $c_{1a}=1$, $c_{1b}=1$, $c_{2b}=1$, $c_{2c}=1$, and the other distances $3$ (a metric: the points lie on a line $a,1,b,2,c$ at unit spacing). All $v_j$ rise together; at $t=1$ every client reaches its near facilities and the surpluses start. Facility $1$ collects from $a$ and $b$, facility $2$ from $b$ and $c$, each at rate $2$, so both are paid for at $t=2$, with all $v_j=2$ and dual value $6$. They share the client $b$, so only facility $1$ is opened (ties broken by index); $c$ then connects to $1$ at cost $3=\tfrac32v_c$. The solution costs $2+1+1+3=7\le3\cdot6$; the optimum is $7$ as well (opening both costs $4+3=7$).

:::

::: {#fig-facility-location-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.4,0)--(4.4,0);
\node[small vertex] (Da) at (0.0,0) {$a$};
\node[lab, tick] at (0.0,-0.55) {$v_a=2$};
\node[hl box] (F1) at (1.3,0) {$1$};
\node[small vertex] (Db) at (2.6,0) {$b$};
\node[lab, tick] at (2.6,-0.55) {$v_b=2$};
\node[box] (F2) at (3.90,0) {$2$};
\node[small vertex] (Dc) at (5.2,0) {$c$};
\node[lab, tick] at (5.2,-0.55) {$v_c=2$};
\draw[hl] (Da) to[bend left=35] (F1);
\draw[hl] (Db) to[bend right=35] (F1);
\draw[hl] (Dc) to[bend right=30] (F1);
\end{tikzpicture}
\end{center}
```

The example on a line: both facilities are paid for at time $2$ with all $v_j=2$; they share client $b$, so only facility $1$ opens, and every client connects to it (total cost $7\le3\cdot6$).

:::

## Local search

::: {#def-facility-location-local-search .definition name="Local search for facility location"}

Start from any non-empty set $U$ of open facilities. While some $U'$ obtained by *adding* one facility, *dropping* one, or *swapping* one open for one closed facility costs less, move to it. A locally optimal $U$ is returned.

:::

::: {#rmk-facility-location-1 .remark editor="No figure: a local search step is one add, drop or swap; the example above already shows the instances the moves act on."}

On @exm-facility-location, starting from $U=\{2\}$ (cost $7$), no move improves, and $\{2\}$ is also optimal.

:::

::: {#thm-facility-location-local-search .theorem name="Locally optimal solutions are 3-approximate"}

Let $U$ be locally optimal with opening cost $O$ and connection cost $A$, and let an optimal solution $U^*$ have costs $O^*$ and $A^*$. Then $A\le A^*+O^*$ and $O\le O^*+2A^*$, so $O+A\le3\,\mathrm{OPT}$.

:::

::: {.proof}

1. *First inequality.* For $i\in U^*\setminus U$, adding $i$ and moving to it exactly the clients that $U^*$ connects to $i$ does not help, so $f_i+\sum_{j:\sigma^*(j)=i}\big(c_{ij}-c_{\sigma(j)j}\big)\ge0$. For $i\in U^*\cap U$ the same sum without $f_i$ is $\ge0$ since $\sigma(j)$ is the nearest open facility.

2. Adding over $i\in U^*$ gives $O^*+A^*-A\ge0$.

3. The second inequality uses the drop and swap moves and is stated without proof.

:::

Each improving step is easy to find ($O(|F|^2)$ neighbours), but the number of steps can be exponential; this local search problem is PLS-complete. Accepting only moves that improve the cost by a factor $1-\varepsilon/\mathrm{poly}(n)$ bounds the number of steps polynomially and gives a $(3+\varepsilon)$-approximation.
