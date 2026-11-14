<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-predicate-02" status="draft"}
(a) $\forall X\ \neg\bigl(\mathrm{prolog}(X)\wedge\mathrm{elvish}(X)\bigr)$.

(b) Negate it and move the negation inwards:
    $$\neg\forall X\ \neg\bigl(\mathrm{prolog}(X)\wedge\mathrm{elvish}(X)\bigr)
      = \exists X\ \neg\neg\bigl(\mathrm{prolog}(X)\wedge\mathrm{elvish}(X)\bigr)
      = \exists X\ \bigl(\mathrm{prolog}(X)\wedge\mathrm{elvish}(X)\bigr).$$
    The first step uses $\neg\forall X\,\varphi = \exists X\,\neg\varphi$,
    and the second uses double negation.
:::
