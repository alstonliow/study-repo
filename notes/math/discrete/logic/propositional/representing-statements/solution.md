<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

<!-- Migrated from 1058note exercises/chapters (owner's solutions). -->

::: {.solution for="prob-propositional-21"}
**Truth table.**

$$\begin{array}{cc|c|c|ccc}
x_1 & x_0 & x & x+1 & y_2 & y_1 & y_0 \\
\hline
0 & 0 & 0 & 1 & 0 & 0 & 1 \\
0 & 1 & 1 & 2 & 0 & 1 & 0 \\
1 & 0 & 2 & 3 & 0 & 1 & 1 \\
1 & 1 & 3 & 4 & 1 & 0 & 0 \\
\end{array}$$

**Bit $y_2$.** This bit is $1$ only in the last row, where $x_1=x_0=1$:
$$y_2 \equiv x_1\wedge x_0$$

**Bit $y_1$.** This bit is $1$ exactly when $x_1,x_0$ differ:
$$y_1 \equiv (\neg x_1\wedge x_0)\vee(x_1\wedge\neg x_0) \equiv x_1\oplus x_0$$

**Bit $y_0$.** From the table:
$$y_0 \equiv (\neg x_1\wedge\neg x_0)\vee(x_1\wedge\neg x_0)$$

Factor out $\neg x_0$:
$$\equiv \neg x_0 \wedge(\neg x_1\vee x_1)$$

Since $\neg x_1\vee x_1\equiv\mathsf{True}$:
$$\equiv \neg x_0\wedge\mathsf{True} \equiv \neg x_0$$

This matches intuition: incrementing always flips the lowest bit.

**Summary.**
$$y_2 \equiv x_1\wedge x_0, \qquad y_1\equiv x_1\oplus x_0, \qquad y_0\equiv \neg x_0$$
:::

::: {.solution for="prob-propositional-15" status="draft"}
Write $J, M, K$ for Judith, Margaret, Katherine.

(a) $\neg J\vee\neg M$.

(b) $(J\vee M)\wedge(\neg J\vee\neg M)$.

(c) $J\vee M\vee K$.

(d) No two are both present:
    $(\neg J\vee\neg M)\wedge(\neg J\vee\neg K)\wedge(\neg M\vee\neg K)$.

(e) The conjunction of (c) and (d):
    $(J\vee M\vee K)\wedge(\neg J\vee\neg M)\wedge(\neg J\vee\neg K)\wedge(\neg M\vee\neg K)$.

(f) Of any two of them, at least one is present:
    $(J\vee M)\wedge(J\vee K)\wedge(M\vee K)$.

(g) Not all three: $\neg J\vee\neg M\vee\neg K$.

(h) The conjunction of (f) and (g):
    $(J\vee M)\wedge(J\vee K)\wedge(M\vee K)\wedge(\neg J\vee\neg M\vee\neg K)$.

(i) $J\wedge M\wedge K$ (three one-literal clauses).

(j) $\neg J\wedge\neg M\wedge\neg K$.
:::

::: {.solution for="prob-propositional-16" status="draft"}
Expand with the distributive law, choosing one literal from each clause, and
drop disjuncts that contain a variable and its negation or that are repeats.

1. The first clause gives $4$ choices: Harry, Ron, Hermione or Ginny.

2. $(\neg\mathrm{Hagrid}\vee\mathrm{Norberta})$ gives $2$ choices.

3. $(\neg\mathrm{Fred}\vee\mathrm{George})\wedge(\mathrm{Fred}\vee\neg\mathrm{George})$
   expands to $4$ conjunctions, two of which are contradictions. This leaves
   $\mathrm{Fred}\wedge\mathrm{George}$ or $\neg\mathrm{Fred}\wedge\neg\mathrm{George}$:
   $2$ choices.

4. The three clauses on Voldemort, Bellatrix and Dolores expand to $8$
   conjunctions. After simplification these are the $3$ conjunctions
   "at least two of the three are absent", e.g.
   $\neg\mathrm{Voldemort}\wedge\neg\mathrm{Bellatrix}$.

5. These four groups use disjoint variables, so the choices are independent.
   The DNF has
   $$4\times2\times2\times3 = 48$$
   disjuncts, each with $6$ literals. Without the simplifications in
   steps 3 and 4, the plain expansion has $4\cdot2^6 = 256$ disjuncts.

The CNF has $7$ clauses and $16$ literals, so the DNF is much larger.
:::
