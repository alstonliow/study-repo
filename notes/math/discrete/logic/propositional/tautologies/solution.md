<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-propositional-10" status="draft"}
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
