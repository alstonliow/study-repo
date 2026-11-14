<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-predicate-14" status="draft"}
(a) 1. Assume $\exists X\,(P(X)\wedge Q(X))$, and let $a$ be such an $X$, so
       $P(a)$ and $Q(a)$ are both true.

    2. $P(a)$ shows $\exists X\,P(X)$, and $Q(a)$ shows $\exists X\,Q(X)$.

    3. So $(\exists X\,P(X))\wedge(\exists X\,Q(X))$.

    The converse fails: on the integers, "even" and "odd" each hold for some
    $X$, but never for the same $X$.

(b) (i) *Directly.* Assume $(\forall X\,P(X))\vee(\forall X\,Q(X))$, and let
    $a$ be arbitrary. If $\forall X\,P(X)$, then $P(a)$, so $P(a)\vee Q(a)$.
    If $\forall X\,Q(X)$, then $Q(a)$, so again $P(a)\vee Q(a)$. Since $a$ was
    arbitrary, $\forall X\,(P(X)\vee Q(X))$.

    (ii) *Using (a).* Apply (a) to the predicates $\neg P$ and $\neg Q$:
    $$\exists X\,(\neg P(X)\wedge\neg Q(X))\ \Rightarrow\ (\exists X\,\neg P(X))\wedge(\exists X\,\neg Q(X)).$$
    Take the contrapositive, and push the negations through with
    $\neg\exists = \forall\neg$ and De Morgan's laws:
    $$(\forall X\,P(X))\vee(\forall X\,Q(X))\ \Rightarrow\ \forall X\,(P(X)\vee Q(X)).$$
:::
