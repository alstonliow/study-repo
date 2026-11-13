<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-propositional-14 origin="external" source="fit1058-cn-4.21-q14"}
Consider the truth table:

| $X$ | $Y$ | $Z$ | $P$ |
|:---:|:---:|:---:|:---:|
|  F  |  F  |  F  |  F  |
|  F  |  F  |  T  |  F  |
|  F  |  T  |  F  |  F  |
|  F  |  T  |  T  |  T  |
|  T  |  F  |  F  |  F  |
|  T  |  F  |  T  |  T  |
|  T  |  T  |  F  |  T  |
|  T  |  T  |  T  |  T  |

(a) Express $P$ in DNF.

(b) Express $\neg P$ in DNF.

(c) Using (b) as your starting point, express $P$ in CNF.

(d) Alternatively, start from the DNF in (a) and expand using the
    Distributive Laws (no further simplification). How many parts are
    in the large conjunction? How many literals? How does this compare
    with (c) in ease and efficiency?
:::

::: {.problem #prob-propositional-17 origin="external" source="fit1058-cn-4.21-q17"}
A Boolean function is in *algebraic normal form* if it is an
exclusive-or of some number of parts, each a conjunction of unnegated
variables or the constant True; the whole expression may also be just False
(otherwise False may not appear).

In ANF: $x\oplus y\oplus(x\wedge y)$, $\mathrm{True}\oplus y\oplus(x\wedge
    y\wedge z)$, $x$, $\mathrm{True}\oplus x$, $x\wedge z$, True, False.\
Not in ANF: $x\oplus y\oplus(\neg x\wedge y)$, $\mathrm{False}\oplus y\oplus
    (x\wedge y\wedge z)$, $\neg x$, $x\vee z$, $\mathrm{True}\oplus\mathrm{True}$.

Prove that every Boolean function can be written in algebraic normal form.
(Use Exercise 12(a) and what you know about DNF.)
:::

::: {.problem #prob-propositional-20 origin="external" source="fit1058-cn-4.21-q20"}
A Boolean expression is *affine* if it is of the form
$x_1\oplus x_2\oplus\cdots\oplus x_n$ or
$x_1\oplus\cdots\oplus x_n\oplus\mathrm{True}$. Prove, by induction on $n$,
that for all $n\in\mathbb{N}$, the number of satisfying truth assignments of an
affine Boolean expression with $n$ variables is $2^{n-1}$.
:::
