::: {.problem #prob-mit6046s15-8-q2 origin="external" source="mit6046s15-8-q2"}
**NP-Completeness**

In this problem, you will prove NP-completeness of a few decision problems. To prove NP-hardness, you may reduce from any problem that has been shown, in class or in CLRS, to be NP-complete.

(a) Let TRIPLE-SAT denote the following decision problem: given a Boolean formula $\phi$, decide whether $\phi$ has at least three distinct satisfying assignments. Prove that TRIPLE-SAT is NP-complete.

(b) In Problem Set 1, we considered how one might locate donut shops at some of the vertices of a street network, modeled as an arbitrary undirected graph $G=(V,E)$. Each vertex $u$ has a nonnegative integer value $p(u)$, which describes the potential profit obtainable from a shop located at $u$. Two shops cannot be located at adjacent vertices. The problem was to design an algorithm that outputs a subset $U\subseteq V$ that maximizes the total profit $\sum_{u\in U}p(u)$. No doubt, you found an algorithm with time complexity that was exponential in the graph parameters. Now we will see why.

Define DONUT to be the following decision problem: given an undirected graph $G=(V,E)$, given a mapping $p$ from vertices $u\in V$ to nonnegative integer profits $p(u)$, and given a nonnegative integer $k$, decide whether there is a subset $U\subseteq V$ such that no two vertices in $U$ are neighbors in $G$, and such that $\sum_{u\in U}p(u)\ge k$. Prove that DONUT is NP-hard. (Hint: Try a reduction from 3SAT.)

Also, explain why this implies that, if there is a polynomial-time algorithm to solve the original problem, i.e., to output a subset $U$ that maximizes the total profit, then P = NP.

(c) Suppose we have one machine and a set of $n$ tasks $a_1,a_2,\dots,a_n$. Each task $a_j$ requires $t_j$ units of time on the machine, yields a profit of $p_j$, and has a deadline $d_j$. Here, the $t_j$, $p_j$, and $d_j$ values are nonnegative integers. The machine can process only one task at a time. Not all tasks have to be run, but if a task starts running, it must run without interruption and must complete by its deadline.

A schedule for a subset of the tasks describes when each of the tasks in the subset starts running. A schedule must observe the constraints given above. The profit for the schedule is the sum of all the $p_j$ values for the tasks $a_j$ in the schedule.

The problem is to produce a schedule for a subset of the tasks that returns the greatest possible amount of profit. State this problem as a decision problem and show that it is NP-complete. In showing this, you may reduce from any problem that has been shown, in class or in CLRS, to be NP-complete.
:::

::: {.problem #prob-mit6046r-8-q1 origin="external" source="mit6046r-8-q1"}
**Hamiltonian Cycle**: Given a directed graph $G=(V,E)$, is there a cycle that visits every vertex exactly once?

**Hamiltonian Path**: Given a directed graph $G=(V,E)$, is there a path that visits every vertex exactly once?

Given that Hamiltonian Cycle is NP-Complete, we prove that Hamiltonian Path is NP-Complete.
:::

::: {.problem #prob-mit6046r-8-q2 origin="external" source="mit6046r-8-q2"}
**3DM**: Given $3$ disjoint sets $X,Y,Z$, which each contain $n$ elements, and triples $T\subset X\times Y\times Z$, is there a a subset $S\subset T$ such that each element $a\in X\cup Y\cup Z$ is in exactly one $s\in S$.

**4-Partition**: Given $n$ integers $\{a_1,a_2,\dots,a_n\}$ is there a partition into $\frac n4$ subsets of $4$ elements each with the same sum $t=A/\frac n4$. Each integer $a_i\in(\frac t5,\frac t3)$ (which ensures that each subset has exactly $4$ elements).

Given that 3DM is NP-Complete, we prove that 4-Partition is NP-Complete.
:::

::: {.problem #prob-mit6046r-8-q5 origin="external" source="mit6046r-8-q5"}
**Prove Max2SAT is NP-Complete: Reducing from Clique**

Clique$(G,k)$: Given graph $G=(V,E)$ and integer $k$, is there a set of vertices $U\subseteq V$ with $|U|\ge k$ that form a complete graph ($k$-clique)?

Max2SAT$(C,X,k)$: Given a CNF formula consisting of clauses $C=\{c_1,c_2,\dots c_n\}$ and literals $X=\{x_1,x_2,\dots x_k\}$ such that each clause involves exactly two literals, does there exist an assignment of TRUE/FALSE to the literals such that at least $k$ clauses are satisfied?
:::

<!-- Sipser problems assigned in MIT 18.404J (Fall 2020) problem sets, which cite them by number only.
     Statements verbatim from the 3rd edition (owner decision 2026-11-23, meta/SPEC.md §10). -->

<!-- Sipser 7.28; 18.404J PS4 Q4 -->
<!-- The book's figure of the box and cards is not reproduced. -->
::: {.problem #prob-sipser3e-7-q28 origin="external" source="sipser3e-7-q28"}
You are given a box and a collection of cards as indicated in the following figure. Because of the pegs in the box and the notches in the cards, each card will fit in the box in either of two ways. Each card contains two columns of holes, some of which may not be punched out. The puzzle is solved by placing all the cards in the box so as to completely cover the bottom of the box (i.e., every hole position is blocked by at least one card that has no hole there). Let $\mathit{PUZZLE}=\{\langle c_1,\dots,c_k\rangle\mid \text{each } c_i \text{ represents a card and this collection of cards has a solution}\}$. Show that $\mathit{PUZZLE}$ is NP-complete.
:::

<!-- Sipser 7.37; 18.404J PS4 Q5 -->
::: {.problem #prob-sipser3e-7-q37 origin="external" source="sipser3e-7-q37"}
Let $U=\{\langle M,x,\#^t\rangle\mid \text{NTM } M \text{ accepts } x \text{ within } t \text{ steps on at least one branch}\}$. Note that $M$ isn't required to halt on all branches. Show that $U$ is NP-complete.
:::

<!-- Sipser 7.26; 18.404J PS5 Q1 -->
::: {.problem #prob-sipser3e-7-q26 origin="external" source="sipser3e-7-q26"}
Let $\phi$ be a 3cnf-formula. An *$\ne$-assignment* to the variables of $\phi$ is one where each clause contains two literals with unequal truth values. In other words, an $\ne$-assignment satisfies $\phi$ without assigning three true literals in any clause.

a. Show that the negation of any $\ne$-assignment to $\phi$ is also an $\ne$-assignment.

b. Let $\mathit{{\ne}SAT}$ be the collection of 3cnf-formulas that have an $\ne$-assignment. Show that we obtain a polynomial time reduction from $\mathit{3SAT}$ to $\mathit{{\ne}SAT}$ by replacing each clause $c_i$
$$(y_1\lor y_2\lor y_3)$$
with the two clauses
$$(y_1\lor y_2\lor z_i)\quad\text{and}\quad(\overline{z_i}\lor y_3\lor b),$$
where $z_i$ is a new variable for each clause $c_i$, and $b$ is a single additional new variable.

c. Conclude that $\mathit{{\ne}SAT}$ is NP-complete.
:::

<!-- Sipser 7.27; 18.404J PS5 Q2 -->
::: {.problem #prob-sipser3e-7-q27 origin="external" source="sipser3e-7-q27"}
A *cut* in an undirected graph is a separation of the vertices $V$ into two disjoint subsets $S$ and $T$. The size of a cut is the number of edges that have one endpoint in $S$ and the other in $T$. Let
$$\mathit{MAX\text-CUT}=\{\langle G,k\rangle\mid G \text{ has a cut of size } k \text{ or more}\}.$$
Show that $\mathit{MAX\text-CUT}$ is NP-complete. You may assume the result of Problem 7.26. (Hint: Show that $\mathit{{\ne}SAT}\le_{\mathrm p}\mathit{MAX\text-CUT}$. The variable gadget for variable $x$ is a collection of $3c$ nodes labeled with $x$ and another $3c$ nodes labeled with $\overline x$, where $c$ is the number of clauses. All nodes labeled $x$ are connected with all nodes labeled $\overline x$. The clause gadget is a triangle of three edges connecting three nodes labeled with the literals appearing in the clause. Do not use the same node in more than one clause gadget. Prove that this reduction works.)
:::

<!-- Sipser 7.36; 18.404J PS5 Q7 -->
::: {.problem #prob-sipser3e-7-q36 origin="external" source="sipser3e-7-q36"}
Show that the following problem is NP-complete. You are given a set of states $Q=\{q_0,q_1,\dots,q_l\}$ and a collection of pairs $\{(s_1,r_1),\dots,(s_k,r_k)\}$ where the $s_i$ are distinct strings over $\Sigma=\{0,1\}$, and the $r_i$ are (not necessarily distinct) members of $Q$. Determine whether a DFA $M=(Q,\Sigma,\delta,q_0,F)$ exists where $\delta(q_0,s_i)=r_i$ for each $i$. Here, $\delta(q,s)$ is the state that $M$ enters after reading $s$, starting at state $q$. (Note that $F$ is irrelevant here.)
:::
