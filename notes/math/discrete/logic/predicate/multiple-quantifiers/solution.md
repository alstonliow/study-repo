<!-- Migrated from 1058note exercises/chapters (owner's solutions). -->

::: {.solution for="prob-predicate-09"}
Write $\text{WordContainsLetter}(W,L)$ as $W(W,L)$.

**(a)**
$$\forall W\,\exists L\ \Big(\big(L=a\vee L=e\vee L=i\vee L=o\vee L=u\big)\wedge W(W,L)\Big)\ \vee\ W(W,y)$$

**(b)** Writing $\text{Vowel}(L)$ as $V(L)$:
$$\forall W\,\exists L\ \Big(V(L)\wedge W(W,L)\Big)\ \vee\ W(W,y)$$
or, with the disjunction brought inside the scope of $\exists L$:
$$\forall W\ \Big(\exists L\ \big(V(L)\wedge W(W,L)\big)\ \vee\ W(W,y)\Big)$$
:::

::: {.solution for="prob-predicate-10"}
Write $\text{Even}(n)$ as $E(n)$ and $\text{Prime}(n)$ as $P(n)$. By
the domain assumption, any element that is not even is odd, so
“odd” is $\neg E(n)$, and “odd prime” is $P(n)\wedge\neg E(n)$.

**Infinitely many odd primes.** There is no largest
odd prime – for any bound $b$, some odd prime exceeds it:
$$R = \forall b\,\exists n\ \big(P(n)\wedge\neg E(n)\wedge b\leq n\big)$$

**Only finitely many even primes.** There is a
largest even prime $m$, and every even prime is at most $m$:
$$S = \exists m\ \Big(P(m)\wedge E(m)\ \wedge\ \forall n\big(P(n)\wedge E(n)\Rightarrow n\leq m\big)\Big)$$

**Final statement.**
$$R\wedge S$$
:::

::: {.solution for="prob-predicate-11"}
Write $\text{Date}(d,m,y)$ as $D(d,m,y)$. $(d_1,m_1,y_1)$ comes
chronologically before $(d_2,m_2,y_2)$ exactly when
$$y_1<y_2, \quad\text{or}\quad y_1=y_2 \wedge m_1<m_2, \quad\text{or}\quad y_1=y_2\wedge m_1=m_2\wedge d_1<d_2.$$

So the answer is
$$D(d_1,m_1,y_1)\wedge D(d_2,m_2,y_2)\wedge\Big((y_1<y_2)\vee\big((y_1=y_2)\wedge(m_1<m_2)\big)\vee\big((y_1=y_2)\wedge(m_1=m_2)\wedge(d_1<d_2)\big)\Big)$$
:::

::: {.solution for="prob-predicate-13"}
$$\exists! x\ P(x) \;\equiv\; \exists x\ \Big(P(x)\wedge\big(\forall y\ (P(y)\Rightarrow x=y)\big)\Big)$$
:::

::: {.solution for="prob-predicate-03"}
<!-- TODO: solution -->
:::

::: {.solution for="prob-predicate-04"}
<!-- TODO: solution -->
:::

::: {.solution for="prob-predicate-05"}
<!-- TODO: solution -->
:::

::: {.solution for="prob-predicate-06"}
<!-- TODO: solution -->
:::

::: {.solution for="prob-predicate-12"}
<!-- TODO: solution -->
:::
