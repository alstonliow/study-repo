<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-propositional-10"}
1. The implication can only be false if its premise $P\wedge(P\Rightarrow Q)$
   is true and its conclusion $Q$ is false.

2. If the premise is true, then $P$ is true and $P\Rightarrow Q$ is true, so
   $Q$ is true.

3. So the case in step 1 cannot occur, and the formula is true under every
   assignment: it is a tautology. (A truth table with $4$ rows confirms
   this.)

This tautology is the rule *modus ponens*: from $P$ and $P\Rightarrow Q$ we may
deduce $Q$. Because it is a tautology, the deduction is valid whatever $P$ and
$Q$ stand for. This is what justifies each step of a proof that applies a
known implication to a known fact.
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-1-q3" status="draft"}
Rows are $(P,Q)=(T,T),(T,F),(F,T),(F,F)$.

| | $TT$ | $TF$ | $FT$ | $FF$ | verdict |
|---|---|---|---|---|---|
| (a) | T | T | T | T | tautology |
| (b) | T | T | T | T | tautology |
| (c) | F | F | F | F | contradiction |
| (d) | T | T | T | T | tautology |
| (e) | F | F | F | F | contradiction |
| (f) | F | T | T | F | neither |

Reasons, which the table confirms row by row:

(a) The implication binds weakest, and $(Q\land P)\lor(\lnot Q\land P)\equiv P$, so the statement is $P\implies P$.

(b) $P\lor Q\lor P\lor\lnot Q$ contains $Q\lor\lnot Q$.

(c) $P$ and $P\implies\lnot Q$ give $\lnot Q$, which contradicts $Q$.

(d) $\lnot P\implies Q\equiv P\lor Q$ and $\lnot Q\implies P\equiv Q\lor P$, so it is $A\implies A$.

(e) With $Q$ true, $\lnot P\implies\lnot Q$ forces $P$ true, and $P\implies\lnot Q$ forces $P$ false.

(f) It is true exactly when one of $P,Q$ is true: exclusive or.
:::
