<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-functions-18" status="draft"}
In §2.13, $\mathrm{Parent}(X,Y)$ holds when $Y$ is a parent of $X$. Its
transitive closure
$$\mathrm{Ancestor} = \mathrm{Parent}\cup\mathrm{Parent}^{(2)}\cup\mathrm{Parent}^{(3)}\cup\cdots$$
holds when $Y$ is a parent, grandparent, great-grandparent, … of $X$, so
"Ancestor" is a good name.

Two people are related when one is the other, one is an ancestor of the other,
or they have a common ancestor:
$$\mathrm{Related}(X,Y)\iff X = Y\ \vee\ \mathrm{Ancestor}(X,Y)\ \vee\ \mathrm{Ancestor}(Y,X)\ \vee\ \exists Z\,\bigl(\mathrm{Ancestor}(X,Z)\wedge\mathrm{Ancestor}(Y,Z)\bigr).$$
(The middle two cases are needed when the common ancestor would be $X$ or $Y$
themselves, for example when no earlier ancestor is recorded.)
:::

::: {.solution for="prob-functions-19" status="draft"}
Let $\mathrm{Collatz}^+$ be the transitive closure of the Collatz function
(as a binary relation on $\mathbb Z^+$):
$$\mathrm{Collatz}^+ = \bigcup_{i\ge1}\mathrm{Collatz}^{(i)}.$$
So $(n,m)\in\mathrm{Collatz}^+$ means that $m$ is reached from $n$ by applying
the function one or more times. The conjecture becomes
$$\forall n\in\mathbb Z^+:\ (n,1)\in\mathrm{Collatz}^+.$$
:::
