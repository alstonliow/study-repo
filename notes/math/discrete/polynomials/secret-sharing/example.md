<!-- Adapted (own wording) from UC Berkeley CS 70, Fall 2020, Note 8 (source key cs70-8, in note.md). -->

::: {#exm-secret-sharing-gf7 .example name="Sharing a secret among five people" level="medium"}
Secret $s=1$, $n=5$ people, any $k=3$ should suffice. Work in $\mathrm{GF}(7)$ and take $P(x)=3x^2+5x+1$. The shares are $P(1)=2$, $P(2)=2$, $P(3)=1$, $P(4)=6$, $P(5)=3$.

People $3$, $4$, $5$ interpolate modulo $7$ (dividing means multiplying by an inverse):
$$\Delta_3=4(x-4)(x-5),\quad \Delta_4=6(x-3)(x-5),\quad \Delta_5=4(x-3)(x-4),$$
and $1\cdot\Delta_3+6\cdot\Delta_4+3\cdot\Delta_5=3x^2+5x+1$, so $s=P(0)=1$.

People $1$ and $5$ alone know $a_2+a_1+s=2$ and $4a_2+5a_1+s=3$: two equations in three unknowns. For every value of $s$ there is a solution, so they are no better off than guessing.
:::
