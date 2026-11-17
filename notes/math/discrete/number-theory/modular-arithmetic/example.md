<!-- Adapted (own wording) from UC Berkeley CS 70, Fall 2020, Note 6, §4-5 (source keys cs70-6.4, cs70-6.5, in note.md). -->

::: {#exm-no-inverse-twelve-mod-fifteen .example name="A number with no inverse" level="easy"}
The multiples of $12$ modulo $15$ are $12,9,6,3,0,12,9,\dots$: the value $1$ never appears, so $12$ has no inverse mod $15$, as @thm-inverse predicts since $\gcd(12,15)=3$. Notice also that $12\cdot5\equiv0$, although neither factor is $0$ modulo $15$.
:::

::: {#exm-solving-linear-congruence .example name="Dividing modulo m" level="easy"}
To solve $8x\equiv9\pmod{15}$, multiply both sides by $8^{-1}\equiv2$ (since $2\cdot8=16\equiv1$). This gives $x\equiv18\equiv3\pmod{15}$, and the solution is unique modulo $15$.
:::
