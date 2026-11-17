<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-5-q4" status="draft"}
(a) Strong induction on $n$. $P_0(7)=19$ and $P_1(7)=49-35+5=19$. For $n\ge2$, $P_n(7)=7P_{n-2}(7)-P_{n-1}(7)$, and both terms are divisible by $19$ by the hypothesis.

(b)

1. *$\deg P_n\le n$ for $n\ge2$.* $\deg P_2=1$ and $\deg P_3=3$. For $n\ge4$, $\deg P_n\le\max(\deg P_{n-2}+1,\deg P_{n-1})\le\max(n-1,n-1)$ by the hypothesis. So $\deg P_{2017}\le2017$.

2. Reducing the coefficients modulo $q$ gives a polynomial over $\mathrm{GF}(q)$ of degree at most $2017$, which is not the zero polynomial by assumption.

3. A non-zero polynomial of degree at most $d$ over a field has at most $d$ roots (@prp-polynomials-mod-p). So $P_{2017}$ has at most $2017$ roots modulo $q$.
:::
