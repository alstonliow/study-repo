<!-- Adapted (own wording) from UC Berkeley CS 70, Fall 2020, Note 8 (source key cs70-8, in note.md). -->

::: {#exm-polynomial-long-division .example name="Dividing by x - 1" level="easy"}
Divide $p(x)=x^3+x^2-1$ by $x-1$. Remove the leading term three times:
$$x^3+x^2-1=x^2(x-1)+(2x^2-1),\quad 2x^2-1=2x(x-1)+(2x-1),\quad 2x-1=2(x-1)+1.$$
So $p(x)=(x^2+2x+2)(x-1)+1$: quotient $x^2+2x+2$, remainder $1=p(1)$.
:::
