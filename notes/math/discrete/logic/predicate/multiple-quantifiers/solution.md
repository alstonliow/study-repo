<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

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

::: {.solution for="prob-predicate-03" status="draft"}
Write $s$ for $\mathrm{supervised}$, and $\mathrm{Church}$, $\mathrm{Turing}$
for the two constants.

(a) $s(\mathrm{Church},\mathrm{Turing})$.

(b) $\forall X\ \neg s(X,X)$.

(c) $\neg\forall X\ \exists Y\ \bigl(Y\ne X\wedge s(X,Y)\bigr)$.

(d) There is someone who supervised a PhD but had no supervisor:
    $$\exists X\ \Bigl(\exists Y\ s(X,Y)\ \wedge\ \neg\exists Z\ s(Z,X)\Bigr).$$

(e) $\exists Y\ \exists X_1\ \exists X_2\ \bigl(X_1\ne X_2\wedge s(X_1,Y)\wedge s(X_2,Y)\bigr)$.

(f) $$\exists Y_1\ \exists Y_2\ \Bigl(Y_1\ne Y_2\wedge s(\mathrm{Turing},Y_1)\wedge s(\mathrm{Turing},Y_2)\wedge\forall Z\ \bigl(s(\mathrm{Turing},Z)\to(Z = Y_1\vee Z = Y_2)\bigr)\Bigr).$$
:::

::: {.solution for="prob-predicate-04" status="draft"}
Write $d$ for $\mathrm{designedFirstComputerIn}$.

(a) $d(\mathrm{Pearcey},\mathrm{Australia})\wedge d(\mathrm{Beard},\mathrm{Australia})$.

(b) $\neg\exists X\ \exists Y\ \exists Z\ \bigl(Y\ne Z\wedge d(X,Y)\wedge d(X,Z)\bigr)$,
    or equivalently
    $\forall X\,\forall Y\,\forall Z\ \bigl((d(X,Y)\wedge d(X,Z))\to Y = Z\bigr)$.
:::

::: {.solution for="prob-predicate-05" status="draft"}
We may only use $\mathrm{knows}$, so we cannot write $X = Y$. Instead, use
walks that are allowed to go back and forth. Assume, as in §2.14, that
$\mathrm{knows}$ is symmetric and that everyone knows someone. Write $k$ for
$\mathrm{knows}$:

$$\forall X\ \forall Y\ \exists Z_1\cdots\exists Z_5\ \Bigl(\bigl(k(X,Z_1)\wedge k(Z_1,Z_2)\wedge k(Z_2,Z_3)\wedge k(Z_3,Z_4)\wedge k(Z_4,Y)\bigr)\ \vee\ \bigl(k(X,Z_1)\wedge k(Z_1,Z_2)\wedge\cdots\wedge k(Z_4,Z_5)\wedge k(Z_5,Y)\bigr)\Bigr).$$

This says there is a walk of length $5$ or $6$ from $X$ to $Y$.

*Why this is the same as distance at most $6$.* If the distance is $d\le6$,
take a shortest path and pad it by going back and forth along one edge, which
adds $2$ each time. So there is a walk of length $5$ (if $d$ is odd) or $6$
(if $d$ is even, including $d = 0$). Conversely, a walk of length at most $6$
contains a path of length at most $6$.
:::

::: {.solution for="prob-predicate-06" status="draft"}
$$\forall A\ \forall B\ \bigl(A = B\ \leftrightarrow\ A\triangle B = \emptyset\bigr).$$
:::

::: {.solution for="prob-predicate-12" status="draft"}
$$\exists c\ \exists k\ \forall x\ \Bigl(t(P,x)\le c\cdot\mathrm{len}(x)^k\Bigr).$$
Here $c,k$ range over positive integers and $x$ over $A^*$. The order of the
quantifiers matters: $c$ and $k$ are chosen once, before $x$. This says that
$P$ runs in polynomial time.
:::
