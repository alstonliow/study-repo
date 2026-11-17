<!-- Adapted (own wording) from UC Berkeley CS 70, Fall 2020, Note 2, §7 (source key cs70-2.7). -->

::: {#exm-false-proof-assume-claim .example name="A false proof: assuming the claim"}
"Claim: $-2=2$. Assume $-2=2$; squaring gives $4=4$, which is true." This only shows that the claim implies something true, $P\implies\text{True}$, which holds for every $P$. Never start from the statement to be proved.
:::

::: {#exm-false-proof-divide-by-zero .example name="A false proof: dividing by zero"}
"Let $x=y$. Then $x^2-xy=x^2-y^2$, so $x(x-y)=(x+y)(x-y)$, so $x=x+y=2x$; with $x=1$, $1=2$." The step that cancels $x-y$ divides by $x-y=0$. Always check whether a quantity you divide by can be zero.
:::

::: {#exm-false-proof-squaring-inequality .example name="A false proof: squaring an inequality"}
"$-2\le1$, so squaring both sides gives $4\le1$." Squaring preserves $a\le b$ only when $0\le a$. In the same way, multiplying an inequality by a negative number reverses it: $-2<5$ gives $2>-5$.
:::
