<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

<!-- Migrated from 1058note exercises/chapters (owner's solutions). -->

::: {.solution for="prob-propositional-20"}
::: {.proof}

**Base case ($n=2$).** Consider $x_1\oplus x_2$:
$$\begin{array}{cc|c}
x_1 & x_2 & x_1\oplus x_2\\
\hline
0&0&0\\
0&1&1\\
1&0&1\\
1&1&0
\end{array}$$
Exactly $2$ of the $4$ assignments satisfy the expression, and $2^{2-1}=2$. So the base case holds. (The case with the extra $\oplus\,\text{True}$ simply flips every output, which does not change the *count* of satisfying assignments, by the same argument as below.)

**Inductive hypothesis.** Assume that for some $n$, any affine Boolean expression with $n$ variables has exactly $2^{n-1}$ satisfying truth assignments.

**Inductive step.** Suppose we have $n+1$ variables, and let
$$Q = x_1\oplus x_2\oplus\cdots\oplus x_n \quad(\text{or } x_1\oplus\cdots\oplus x_n\oplus\text{True}),$$
so that $Q$ is itself an affine expression on $n$ variables. The $(n+1)$-variable affine expression is then
$$Q\oplus x_{n+1}.$$

By definition of $\oplus$, $Q\oplus x_{n+1}$ is True exactly when $Q$ and $x_{n+1}$ differ:

$$\begin{array}{cc|c}
Q & x_{n+1} & Q\oplus x_{n+1}\\
\hline
0&0&0\\
0&1&1\\
1&0&1\\
1&1&0
\end{array}$$

So $Q\oplus x_{n+1}$ is satisfied exactly in the following two disjoint cases:

*Case 1: $Q=\text{False}$, $x_{n+1}=\text{True}$.* By the inductive hypothesis, $Q$ is True for $2^{n-1}$ of the $2^n$ assignments to $x_1,\dots,x_n$, so $Q$ is False for the remaining $2^n-2^{n-1}$ assignments. Combined with $x_{n+1}=\text{True}$ (1 way), this gives
$$2^n-2^{n-1}$$
satisfying assignments.

*Case 2: $Q=\text{True}$, $x_{n+1}=\text{False}$.* By the inductive hypothesis, $Q$ is True for $2^{n-1}$ assignments to $x_1,\dots,x_n$. Combined with $x_{n+1}=\text{False}$ (1 way), this gives
$$2^{n-1}$$
satisfying assignments.

Since these two cases are disjoint (they differ in the value of $x_{n+1}$), the total number of satisfying assignments for the $(n+1)$-variable expression is
$$(2^n - 2^{n-1}) + 2^{n-1} = 2^n = 2^{(n+1)-1}.$$

This matches the claimed formula for $n+1$ variables.

**Conclusion.** By induction, for all $n\in\mathbb{N}$, an affine Boolean expression with $n$ variables has exactly $2^{n-1}$ satisfying truth assignments. Since there are $2^n$ truth assignments in total, exactly half are satisfying and half are not.

:::
:::

::: {.solution for="prob-propositional-14" status="draft"}
$P$ is true exactly when at least two of $X,Y,Z$ are true (the *majority*
function).

(a) One conjunction for each row where $P$ is true:
    $$(\neg X\wedge Y\wedge Z)\vee(X\wedge\neg Y\wedge Z)\vee(X\wedge Y\wedge\neg Z)\vee(X\wedge Y\wedge Z).$$

(b) One conjunction for each row where $P$ is false:
    $$(\neg X\wedge\neg Y\wedge\neg Z)\vee(\neg X\wedge\neg Y\wedge Z)\vee(\neg X\wedge Y\wedge\neg Z)\vee(X\wedge\neg Y\wedge\neg Z).$$

(c) Negate (b) with De Morgan's laws:
    $$(X\vee Y\vee Z)\wedge(X\vee Y\vee\neg Z)\wedge(X\vee\neg Y\vee Z)\wedge(\neg X\vee Y\vee Z).$$
    That is $4$ clauses and $12$ literals.

(d) Distributing the DNF of (a), each clause picks one literal from each of
    the $4$ conjunctions. That gives $3^4 = 81$ clauses of $4$ literals each,
    so $324$ literal occurrences (many clauses are tautologies or repeats,
    but they are not simplified away).

    Route (c) is far shorter and easier: it produces one clause per false
    row, while route (d) multiplies out all the choices.
:::

::: {.solution for="prob-propositional-17" status="draft"}
1. Start from the DNF of the function, with one conjunction (minterm) per
   true row of its truth table. (If there are no true rows, the function is
   False, which is in ANF.)

2. Different minterms are never true together, because they disagree on some
   variable. For formulas $A,B$ that are never true together, $A\vee B = A\oplus B$, since by Exercise
   12(a) $A\vee B = A\oplus B\oplus(A\wedge B)$ and here $A\wedge B$ is False.
   So the $\vee$ between minterms can be replaced by $\oplus$.

3. Replace each negated variable by $\neg x = \mathrm{True}\oplus x$.

4. Each minterm is now a conjunction of factors of the form $x$ or
   $(\mathrm{True}\oplus x)$. Multiply out using the distributive law of
   $\wedge$ over $\oplus$ (Exercise 13). The result is an exclusive-or of
   conjunctions of unnegated variables, together with True terms.

5. Simplify using $A\oplus A = \mathrm{False}$ and $A\oplus\mathrm{False} = A$
   to remove repeated terms, and $x\wedge x = x$, $x\wedge\mathrm{True} = x$
   inside conjunctions. If everything cancels, the result is False.

The result is in algebraic normal form.
:::
