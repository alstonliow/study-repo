---
title: "NP-Completeness and the Cook–Levin Theorem"
sources: [mit18404j-15, mit18404j-16]
requires: [cs/theory/complexity-classes, math/discrete/logic/propositional/normal-forms]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lectures 15 and 16, in our own wording; proofs written out in steps. The informal definition for programs is @def-polynomial-reduction; further reductions are in @sec-cs-theory-np-complete-reductions. -->

## Polynomial-time reductions

::: {#def-np-complete-tm .definition name="Polynomial-time reducibility, NP-completeness" related="def-polynomial-reduction"}

$A$ is *polynomial-time reducible* to $B$, written $A\le_{\mathrm p}B$, if $A\le_{\mathrm m}B$ (@def-mapping-reducibility) by a reduction $f$ computable in polynomial time. $B$ is *NP-complete* if $B\in\mathrm{NP}$ and $A\le_{\mathrm p}B$ for every $A\in\mathrm{NP}$.

:::

::: {#prp-poly-reduction-properties .proposition name="Using polynomial-time reductions"}

If $A\le_{\mathrm p}B$ and $B\in\mathrm P$, then $A\in\mathrm P$. If $B$ is NP-complete, then $B\in\mathrm P$ iff $\mathrm P=\mathrm{NP}$. If $B$ is NP-complete, $C\in\mathrm{NP}$ and $B\le_{\mathrm p}C$, then $C$ is NP-complete.

:::

::: {.proof}

1. To decide $A$, compute $f(w)$ in time $|w|^a$ and run the decider of $B$, in time $|f(w)|^b\le|w|^{ab}$ (the output is no longer than the running time). This is polynomial.

2. If $B\in\mathrm P$ is NP-complete, every $A\in\mathrm{NP}$ reduces to $B$ and is in $\mathrm P$ by step 1.

3. Composing two polynomial-time reductions gives one, so every $A\in\mathrm{NP}$ satisfies $A\le_{\mathrm p}B\le_{\mathrm p}C$.

:::

The plan: prove one problem NP-complete directly (SAT), then reduce it to others.

## Reductions from 3SAT

Write $\mathit{SAT}=\{\langle\phi\rangle: \phi \text{ is a satisfiable Boolean formula}\}$ and $\mathit{3SAT}$ for the satisfiable formulas in conjunctive normal form with three literals per clause (@def-3sat). A *$k$-clique* in an undirected graph is a set of $k$ nodes, every two joined by an edge, and $\mathit{CLIQUE}=\{\langle G,k\rangle: G \text{ has a } k\text{-clique}\}$.

::: {#thm-3sat-clique .theorem name="3SAT reduces to CLIQUE" related="cor-vertex-cover-clique"}

$\mathit{3SAT}\le_{\mathrm p}\mathit{CLIQUE}$.

:::

::: {.proof}

1. Let $\phi$ have clauses $C_1,\dots,C_k$. Build $G$ with one node for each literal occurrence, grouped in $k$ triples, one per clause.

2. Join two nodes by an edge unless they lie in the same triple or are *contradictory* ($x$ and $\bar x$). Output $\langle G,k\rangle$; this takes polynomial time.

3. If $\phi$ has a satisfying assignment, pick in each clause one true literal. These $k$ nodes lie in different triples and are never contradictory (all are true), so they form a $k$-clique.

4. Conversely, a $k$-clique has exactly one node per triple (nodes in a triple are not adjacent) and contains no contradictory pair. Setting all its literals true is consistent and makes every clause true.

:::

::: {#fig-cook-levin-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[hl state] (n00) at (0.82,2.85) {$x$};
\node[state] (n01) at (0.00,3.25) {$y$};
\node[state] (n02) at (-0.82,2.85) {$z$};
\node[state] (n10) at (-3.56,-0.99) {$\bar x$};
\node[hl state] (n11) at (-3.52,-1.90) {$\bar y$};
\node[state] (n12) at (-2.78,-2.43) {$z$};
\node[hl state] (n20) at (2.78,-2.43) {$x$};
\node[state] (n21) at (3.52,-1.90) {$\bar y$};
\node[state] (n22) at (3.56,-0.99) {$\bar z$};
\begin{scope}[on background layer]
\draw[faint] (n00) -- (n12);
\draw[faint] (n00) -- (n21);
\draw[faint] (n00) -- (n22);
\draw[faint] (n01) -- (n10);
\draw[faint] (n01) -- (n12);
\draw[faint] (n01) -- (n20);
\draw[faint] (n01) -- (n22);
\draw[faint] (n02) -- (n10);
\draw[faint] (n02) -- (n11);
\draw[faint] (n02) -- (n12);
\draw[faint] (n02) -- (n20);
\draw[faint] (n02) -- (n21);
\draw[faint] (n10) -- (n21);
\draw[faint] (n10) -- (n22);
\draw[faint] (n11) -- (n21);
\draw[faint] (n11) -- (n22);
\draw[faint] (n12) -- (n20);
\draw[faint] (n12) -- (n21);
\draw[hl] (n00) -- (n11);
\draw[hl] (n00) -- (n20);
\draw[hl] (n11) -- (n20);
\end{scope}
\end{tikzpicture}
\end{center}
```

The graph of @thm-3sat-clique for $(x\vee y\vee z)\wedge(\bar x\vee\bar y\vee z)\wedge(x\vee\bar y\vee\bar z)$, one triple per clause. The shaded 3-clique $x,\bar y,x$ gives the satisfying assignment $x=1$, $y=0$ ($z$ arbitrary).

:::

::: {#cor-clique-np-complete .corollary name="CLIQUE is NP-complete"}

If $\mathit{3SAT}$ is NP-complete (@thm-3sat-np-complete), so is $\mathit{CLIQUE}$: it is in $\mathrm{NP}$ (the certificate is the clique) and @prp-poly-reduction-properties applies.

:::

::: {#thm-3sat-hampath .theorem name="HAMPATH is NP-complete"}

$\mathit{3SAT}\le_{\mathrm p}\mathit{HAMPATH}$, so $\mathit{HAMPATH}$ is NP-complete.

:::

::: {.proof}

1. Let $\phi$ have variables $x_1,\dots,x_m$ and clauses $c_1,\dots,c_k$. For each variable build a *diamond*: a top and a bottom node joined through a horizontal row of $3k+1$ nodes linked by edges in both directions. Stack the diamonds, the bottom of each being the top of the next; $s$ is the top of the first and $t$ the bottom of the last.

2. A Hamiltonian path must cross each row either left to right (read: $x_i$ true) or right to left ($x_i$ false).

3. For each clause $c_j$ add a node $c_j$. If $x_i$ occurs in $c_j$, add edges from the $(3j-1)$-th node of row $i$ to $c_j$ and from $c_j$ to the $3j$-th node, so a left-to-right crossing can detour through $c_j$; if $\bar x_i$ occurs, add the edges in the opposite direction. The separators between the pairs keep detours apart.

4. A satisfying assignment gives a Hamiltonian path: cross each row in the direction of its value, and visit each clause node once by a detour from the row of one true literal.

5. Conversely, in a Hamiltonian path every detour to $c_j$ must return to the neighbouring node of the same row (otherwise some node could not be visited later), so the path crosses each row in one direction. Read off the assignment; each $c_j$ is visited by a detour that agrees with its direction, so it has a true literal.

6. $\mathit{HAMPATH}\in\mathrm{NP}$ (@exm-hampath-composites), and the graph has polynomial size.

:::

::: {#fig-cook-levin-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.75cm, y=0.75cm]
\node[small vertex] (top) at (3.5,2.2) {$s$};
\node[small vertex] (bot) at (3.5,-2.2) {};
\foreach \i in {0,...,7} \node[small vertex] (r\i) at (\i,0) {};
\foreach \i [evaluate=\i as \j using int(\i+1)] in {0,...,6} {\draw (r\i) edge[trans, bend left=18] (r\j); \draw (r\j) edge[trans, bend left=18] (r\i);}
\draw[trans] (top) -- (r0); \draw[trans] (top) -- (r7);
\draw[trans] (r0) -- (bot); \draw[trans] (r7) -- (bot);
\node[hl state] (c) at (3.5,1.25) {$c_1$};
\draw[trans, hl] (r1) -- (c); \draw[trans, hl] (c) -- (r2);
\node[lab, note, anchor=west] at (8.3,0.5) {left to right: $x_i=1$};
\node[lab, note, anchor=west] at (8.3,-0.2) {right to left: $x_i=0$};
\node[lab, note, anchor=west] at (8.3,1.25) {detour if $x_i\in c_1$};
\end{tikzpicture}
\end{center}
```

One variable gadget of @thm-3sat-hampath (row shortened). A left-to-right crossing can visit $c_1$ between two neighbouring row nodes.

:::

## The Cook–Levin theorem

::: {#thm-cook-levin .theorem name="Cook–Levin"}

$\mathit{SAT}$ is NP-complete.

:::

::: {.proof}

1. $\mathit{SAT}\in\mathrm{NP}$: the certificate is a satisfying assignment.

2. Let $A\in\mathrm{NP}$ be decided by an NTM $N$ in time $n^k$. Given $w$ of length $n$, we construct in polynomial time a formula $\phi_{N,w}$ that is satisfiable iff $N$ accepts $w$.

3. A *tableau* is an $n^k\times n^k$ table whose rows are the configurations of one branch of $N$ on $w$, each padded with blanks and written between end markers $\#$; it is *accepting* if some row is accepting. $N$ accepts $w$ iff an accepting tableau exists.

4. Let $C=Q\cup\Gamma\cup\{\#\}$. For each cell $(i,j)$ and each $s\in C$ take a Boolean variable $x_{i,j,s}$, meaning "cell $(i,j)$ contains $s$". Let $\phi_{N,w}=\phi_{\text{cell}}\wedge\phi_{\text{start}}\wedge\phi_{\text{accept}}\wedge\phi_{\text{move}}$:
    a. $\phi_{\text{cell}}$: every cell contains exactly one symbol, $\bigwedge_{i,j}\big[\bigvee_s x_{i,j,s}\wedge\bigwedge_{s\ne t}(\overline{x_{i,j,s}}\vee\overline{x_{i,j,t}})\big]$;
    b. $\phi_{\text{start}}$: row 1 is $\#q_0w_1\cdots w_n\sqcup\cdots\sqcup\#$, one variable per cell;
    c. $\phi_{\text{accept}}$: $\bigvee_{i,j}x_{i,j,q_{\text{acc}}}$;
    d. $\phi_{\text{move}}$: every $2\times3$ *window* of cells is *legal*, that is, consistent with the transition function of $N$; for each window, an OR over the finitely many legal windows of the AND of their six cell variables.

5. A row follows legally from the row above iff all windows between them are legal: a step of $N$ changes the tape only next to the head, and each window sees enough to check that. So the satisfying assignments of $\phi_{N,w}$ correspond to accepting tableaux.

6. The table has $n^{2k}$ cells and $|C|$ is a constant, so $\phi_{N,w}$ has $O(n^{2k})$ size and is written in polynomial time.

:::

::: {#fig-cook-levin-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.5cm, y=0.5cm]
\foreach \r/\row in {0/{\#,q_0,w_1,w_2,w_3,\sqcup,\sqcup,\#},1/{\#,a,q_2,w_2,w_3,\sqcup,\sqcup,\#},2/{\#,a,b,q_7,w_3,\sqcup,\sqcup,\#}} {
  \foreach \s [count=\i from 0] in \row {
    \draw[cell frame] (\i*1.2,-\r) rectangle (\i*1.2+1.2,-\r+1);
    \node[lab, note] at (\i*1.2+0.6,-\r+0.5) {$\s$};
  }
}
\foreach \i in {0,...,7} \node[lab, note] at (\i*1.2+0.6,-3.4) {$\vdots$};
\draw[hl] (1.2,-1) rectangle (4.8,1);
\node[lab, note, anchor=west] at (10,0.5) {start configuration};
\node[lab, note, anchor=west] at (10,-1.5) {each row follows};
\node[lab, note, anchor=west] at (10,-2.1) {from the one above};
\draw[decorate, decoration={brace, amplitude=4pt}] (0,1.2) -- node[lab, note, above=4pt] {$n^k$ columns} (9.6,1.2);
\end{tikzpicture}
\end{center}
```

The tableau in the proof of @thm-cook-levin. The highlighted $2\times3$ window shows a legal move ($q_0$ reads $w_1$, writes $a$, moves right into $q_2$); the formula checks every window.

:::

::: {#thm-3sat-np-complete .theorem name="3SAT is NP-complete"}

:::

::: {.proof}

1. Modify the construction in the proof of @thm-cook-levin so that $\phi_{N,w}$ is in conjunctive normal form (@def-cnf). $\phi_{\text{cell}}$, $\phi_{\text{start}}$ and $\phi_{\text{accept}}$ already are.

2. $\phi_{\text{move}}$ is an AND, over windows, of formulas of constant size (6 cells, a fixed set of legal windows). Each such formula can be converted to an equivalent CNF formula of constant size, by the distributive law.

3. Split clauses to three literals. A clause $(a_1\vee\cdots\vee a_l)$ with $l>3$ becomes

$$
(a_1\vee a_2\vee z_1)\wedge(\overline{z_1}\vee a_3\vee z_2)\wedge\cdots\wedge(\overline{z_{l-3}}\vee a_{l-1}\vee a_l)
$$

with new variables $z_i$; this is satisfiable together with the rest exactly when some $a_i$ is true (set the $z$'s to pass the truth along). Short clauses repeat a literal, as in $(a\vee a\vee b)$.

4. The result is a 3CNF formula of polynomial size, satisfiable iff $N$ accepts $w$. As $\mathit{3SAT}\in\mathrm{NP}$, it is NP-complete.

:::
