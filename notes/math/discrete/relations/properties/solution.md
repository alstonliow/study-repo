<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-functions-17" status="draft"}
The inverse is the relation itself: $R^{-1} = R$.

$(x,y)\in R^{-1}$ means $(y,x)\in R$, and by symmetry this holds exactly when
$(x,y)\in R$. Conversely, $R^{-1} = R$ implies that $R$ is symmetric, so this
is another characterisation of symmetry.
:::

::: {.solution for="prob-functions-20" status="draft"}
An equivalence relation must be reflexive, symmetric and transitive.

| relation | equivalence? | reason |
|---|---|---|
| $\simeq_1$ same length | yes | "same value of a function" is always an equivalence |
| $\simeq_2$ same function | yes | same reason: the function computed |
| $\simeq_3$ same set of variable names | yes | same reason |
| $\simeq_4$ a common variable name | no | not transitive: $P$ uses `x`, $Q$ uses `x,y`, $R$ uses `y`; also not reflexive for a program with no variables |
| $\simeq_5$ no common variable name | no | not reflexive: a program shares its variables with itself |
| $\simeq_6$ same set of programmers | yes | same value of a function |
| $\simeq_7$ a common coauthor | no | not transitive, as for $\simeq_4$ |
| $\simeq_8$ completed before | no | not reflexive, not symmetric |
| $\simeq_9$ completed on the same day | yes | same value of a function |
| $\simeq_{10}$ completed after | no | not reflexive, not symmetric |

The general fact used: for any function $h$, "$h(P) = h(Q)$" is an
equivalence relation, since equality is reflexive, symmetric and transitive.
:::
