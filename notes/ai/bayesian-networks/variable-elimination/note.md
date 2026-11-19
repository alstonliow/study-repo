---
title: "Variable Elimination"
sources: [cs188-15]
requires: [ai/bayesian-networks/bayesian-networks]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 15 (inference by enumeration, factors, join and eliminate, variable elimination, evidence, ordering, complexity, polytrees), in our own wording; the traffic numbers are our own and were computed exactly in Python; proofs written out in steps. -->

Inference by enumeration (@def-probabilistic-inference) builds the whole joint distribution and then sums it, which takes time and space exponential in the number of variables. A Bayesian network (@def-bayesian-network) stores the joint as a product of small tables; variable elimination keeps it that way as long as possible, summing variables out of small products instead of the big one.

::: {#def-factor .definition name="Factor, join, eliminate"}

A *factor* $f(Y_1,\dots,Y_k)$ is a table of non-negative numbers, one for each combination of values of its variables (its *scope*); it is a tensor with one axis per variable. Conditional probability tables, joint distributions and their slices are factors; a factor need not sum to $1$.

- The *join* (pointwise product) of factors $f_1,\dots,f_m$ is the factor on the union of their scopes with $(f_1\cdots f_m)(y)=\prod_jf_j(y_{\text{scope}(f_j)})$.
- *Eliminating* (summing out) a variable $H$ from $f$ gives the factor on the scope without $H$, $\bigl(\sum_Hf\bigr)(y)=\sum_hf(y,h)$.
- *Selecting* evidence $E=e$ in $f$ keeps only the entries with $E=e$ and removes $E$ from the scope.

:::

The size of a factor is the product of its variables' domain sizes, so joining is what makes factors large and eliminating is what makes them small again.

::: {#def-variable-elimination .definition name="Variable elimination"}

To compute $P(Q\mid E=e)$ in a Bayesian network, *variable elimination* (VE) starts with one factor per variable, its conditional probability table with the evidence selected. Then, for each *hidden* variable $H$ (neither query nor evidence) in some order, it joins all factors whose scope contains $H$ and eliminates $H$ from the result. Finally it joins the remaining factors, which have scope $Q$, and normalises.

:::

```{=latex}
\begin{algorithm}
\caption{Variable elimination}
\begin{algorithmic}
\INPUT Bayesian network, query $Q$, evidence $E=e$, order of the hidden variables
\OUTPUT $P(Q\mid E=e)$
\STATE $\mathcal F\gets\{p(X_i\mid \text{Parents}(X_i))\text{ with } E=e \text{ selected} : i=1,\dots,n\}$
\FOR{each hidden variable $H$ in the order}
    \STATE $\mathcal F_H\gets$ the factors in $\mathcal F$ whose scope contains $H$
    \STATE $g\gets\sum_H\prod_{f\in\mathcal F_H}f$
    \STATE $\mathcal F\gets(\mathcal F\setminus\mathcal F_H)\cup\{g\}$
\ENDFOR
\STATE $f\gets\prod_{f'\in\mathcal F}f'$ \COMMENT{a factor on $Q$}
\RETURN $f/\sum_qf(q)$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-variable-elimination .theorem name="Variable elimination is exact"}

Whatever the order of the hidden variables, variable elimination returns $P(Q\mid E=e)$.

:::

::: {.proof}

1. Invariant: the product of the factors in $\mathcal F$, as a function of the variables not yet eliminated (other than $E$), equals $P(Q,E=e,\text{remaining hidden variables})$ summed over the hidden variables already eliminated.
2. Initially $\mathcal F$ holds the conditional tables with evidence selected, whose product is $P(Q,E=e,\text{all hidden})$ by the definition of the network: the invariant holds with nothing eliminated.
3. Eliminating $H$: the factors not containing $H$ do not depend on $h$, so by distributivity
$$
\sum_h\prod_{f\in\mathcal F}f=\Bigl(\prod_{f\notin\mathcal F_H}f\Bigr)\cdot\sum_h\prod_{f\in\mathcal F_H}f=\Bigl(\prod_{f\notin\mathcal F_H}f\Bigr)\cdot g,
$$
which is the product of the new set of factors. So the invariant is kept.
4. After all hidden variables are eliminated, the product is $P(Q,E=e)$ as a function of $Q$. Dividing by its sum $P(E=e)$ gives $P(Q\mid E=e)$.

:::

The only difference from enumeration is the moment of summing: enumeration joins everything first and sums at the end, VE sums out each variable as soon as all the factors containing it are together ("marginalising early").

::: {#exm-variable-elimination-traffic .example name="Rain, traffic, lateness"}

In the chain $R\to T\to L$ (rain, traffic, being late) let $P(+r)=0.2$, $P(+t\mid+r)=0.7$, $P(+t\mid-r)=0.2$, $P(+l\mid+t)=0.4$, $P(+l\mid-t)=0.1$. To find $P(L)$, eliminate $R$: join $P(R)$ and $P(T\mid R)$ and sum out $R$, giving $f_1(T)$ with $f_1(+t)=0.2\cdot0.7+0.8\cdot0.2=0.3$ and $f_1(-t)=0.7$. Eliminate $T$: $P(+l)=0.3\cdot0.4+0.7\cdot0.1=0.19$. No factor ever had more than two variables, while enumeration builds the eight-entry joint table.

With evidence $L=+l$ and query $R$, the factors are $P(R)$, $P(T\mid R)$ and the selected $P(+l\mid T)$. Eliminating $T$ gives $g(R)=\sum_tP(t\mid R)P(+l\mid t)$, so $g(+r)=0.31$ and $g(-r)=0.16$. Joining with $P(R)$ gives $(0.062,\ 0.128)$, and normalising, $P(+r\mid+l)=0.062/0.19=31/95\approx0.326$: being late raises the probability of rain from $0.2$.

:::

::: {#fig-variable-elimination-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\node[box] at (0,0) {$P(R)$};
\node[box] at (1.6,0) {$P(T\mid R)$};
\node[box] at (3.4,0) {$P(L\mid T)$};
\draw[->] (1.6,-0.45) -- (1.6,-0.95);
\node[lab, tick, anchor=west] at (1.7,-0.7) {join, sum out $R$};
\node[hl box] at (1.6,-1.4) {$f_1(T)=(0.3,0.7)$};
\node[box] at (4.3,-1.4) {$P(L\mid T)$};
\draw[->] (2.9,-1.85) -- (2.9,-2.35);
\node[lab, tick, anchor=west] at (3.0,-2.1) {join, sum out $T$};
\node[hl box] at (2.9,-2.8) {$P(L)=(0.19,0.81)$};
\end{tikzpicture}
\end{center}
```

Variable elimination for $P(L)$ in the chain $R\to T\to L$ of @exm-variable-elimination-traffic: each step joins the factors containing one variable and sums it out, so no factor ever has more than two variables.

:::

::: {#prp-variable-elimination-cost .proposition name="Cost of variable elimination"}

If every factor created by VE has at most $w$ variables, each with at most $d$ values, VE takes time and space $O(n\,d^{w})$ for a network with $n$ variables. The largest factor depends on the elimination order.

:::

::: {.proof}

1. Each hidden variable is eliminated once, and each elimination joins the factors in $\mathcal F_H$ into one table on at most $w$ variables (the scope of $g$ together with $H$), which has at most $d^{w}$ entries.
2. Every factor is joined exactly once: it is removed from $\mathcal F$ when it is joined. There are $n$ initial factors and at most $n$ created ones, so $O(n)$ factors in all.
3. Building a joined table entry by entry costs $O(d^{w})$ for each factor taking part, and summing out $H$ costs $O(d^{w})$ more. Adding over all eliminations gives $O(n\,d^{w})$ time; at most $O(n)$ tables of size $O(d^{w})$ are stored at once.

:::

In a star network with hub $Z$ and leaves $X_1,\dots,X_n$ and query $Z$, eliminating each leaf first creates only factors on $Z$; eliminating $Z$ first (were it hidden) joins all tables into one factor on $X_1,\dots,X_n$, of size $d^{n}$. Finding the best order is itself NP-hard, and for some networks every order produces large factors.

::: {#thm-bn-inference-np-hard .theorem name="Exact inference is NP-hard"}

Deciding whether $P(X=\text{true})>0$ for a variable $X$ of a Bayesian network with Boolean variables and tables given explicitly is NP-hard.

:::

::: {.proof}

1. Reduce 3-SAT. Given a formula with variables $u_1,\dots,u_m$ and clauses $c_1,\dots,c_k$, build a network with root nodes $U_1,\dots,U_m$, each true with probability $\tfrac12$.
2. For each clause add a node $C_j$ whose parents are its three variables and whose table makes $C_j$ deterministically true exactly when the clause is satisfied by their values; each table has $2^{3}$ rows.
3. Add nodes $A_1,\dots,A_k$ with $A_1=C_1$ and $A_j=A_{j-1}\wedge C_j$ deterministically (two parents each), and let $X=A_k$.
4. Then $P(X=\text{true})$ is $2^{-m}$ times the number of satisfying assignments, which is positive exactly when the formula is satisfiable. The network has size polynomial in the formula, so a polynomial-time inference algorithm would decide 3-SAT.

:::

The same construction shows that computing $P(X=\text{true})$ exactly counts satisfying assignments, a #P-hard problem. In practice networks are often sparse enough for VE, and approximate inference by sampling (@sec-ai-bayesian-networks-rejection-sampling) handles the rest.

::: {#rmk-polytrees .remark name="Polytrees"}

A *polytree* is a directed graph with no undirected cycles (its skeleton is a tree). For a polytree, eliminating variables from the leaves of the skeleton inwards towards the query keeps every factor within the scope of some conditional table, so VE runs in time linear in the total size of the tables. Cutset conditioning, as for CSPs (@def-cutset-conditioning), extends this to networks that are nearly polytrees.

:::
