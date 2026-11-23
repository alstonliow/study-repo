<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-6-q11" status="draft"}
Problem 6.10 defines $\phi_{\mathrm{eq}}$ as the sentence saying that $R_1$ is reflexive, symmetric and transitive, that is, an equivalence relation.

1. *The model.* Take the universe $\mathbb N$, let $R_1$ be equality and $R_2$ be "less than": $R_1(x,y)\iff x=y$ and $R_2(x,y)\iff x<y$.

2. *Check each conjunct.*
   - Equality is an equivalence relation, so $\phi_{\mathrm{eq}}$ holds.
   - If $x=y$ then not $x<y$.
   - If $x\ne y$ then exactly one of $x<y$ and $y<x$ holds.
   - $<$ is transitive.
   - Every $x$ has $y=x+1$ with $x<y$.

3. So $(\mathbb N,=,<)$ is a model of $\phi_{\mathrm{lt}}$.

4. *Remark.* $\phi_{\mathrm{lt}}$ has no finite model. In a finite model, $R_2$ would be a strict order on the $R_1$-classes in which every element has a strictly larger one, which is impossible.
:::
