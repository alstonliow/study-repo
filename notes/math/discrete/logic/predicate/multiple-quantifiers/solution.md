<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

<!-- Migrated from 1058note exercises/chapters (owner's solutions). -->

::: {.solution for="prob-predicate-03"}
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

::: {.solution for="prob-predicate-04"}
Write $d$ for $\mathrm{designedFirstComputerIn}$.

(a) $d(\mathrm{Pearcey},\mathrm{Australia})\wedge d(\mathrm{Beard},\mathrm{Australia})$.

(b) $\neg\exists X\ \exists Y\ \exists Z\ \bigl(Y\ne Z\wedge d(X,Y)\wedge d(X,Z)\bigr)$,
    or equivalently
    $\forall X\,\forall Y\,\forall Z\ \bigl((d(X,Y)\wedge d(X,Z))\to Y = Z\bigr)$.
:::

::: {.solution for="prob-predicate-05"}
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

::: {.solution for="prob-predicate-06"}
$$\forall A\ \forall B\ \bigl(A = B\ \leftrightarrow\ A\triangle B = \emptyset\bigr).$$
:::

::: {.solution for="prob-predicate-07"}
| | predicates | functions | variables (domain) | constants | proposition? |
|---|---|---|---|---|---|
| (a) | $\ge$ | squaring | $x\in\mathbb R$ (bound) | $0$ | yes, **true** |
| (b) | $<$ | squaring | $x\in\mathbb R$ (free) | $0$ | no: $x$ is free |
| (c) | $=$ | $2^x$, squaring | $x\in\mathbb N$ (bound) | $2$ | yes, **false**: $x = 0$ gives $1\ne0$ |
| (d) | $<$ | none | $x\in\mathbb R$ (free), $y\in\mathbb R$ (bound) | $0$ | no: $x$ is free |
| (e) | $<$ | none | $x,y,z\in\mathbb R$ (bound) | none | yes, **false**: take $x = z$ |
| (f) | none | none | $x,y$ Boolean (bound) | none | yes, **true**: $x = \mathrm T$, $y = \mathrm F$ |

Notes:

- (c) is false over $\mathbb N$ even though $2^x = x^2$ holds for $x = 2$ and
  $x = 4$; a universal statement needs every $x$.
- (d) is true for every value of $x$ once $x$ is fixed (if $x<0$, then
  $x<y$ for all positive $y$), but as written it has a free variable.
- (e) would be true if it required $x<z$ first, as in
  $\forall x\forall z\,(x<z\Rightarrow\exists y\,(x<y\wedge y<z))$: the
  reals are dense.
- In (f), $\neg(x\Rightarrow y)$ uses only connectives; $x,y$ are
  propositional variables.
:::

::: {.solution for="prob-predicate-08"}
- Predicates: $\subseteq$ (binary, used twice).
- Functions: the power set function $\mathcal P$.
- Variables: $A$ and $B$, ranging over sets; both are bound by $\forall$.
- Connective: $\Rightarrow$.

In words: *for all sets $A$ and $B$, if $A$ is a subset of $B$, then the power
set of $A$ is a subset of the power set of $B$* (Exercise 1.7).
:::

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

::: {.solution for="prob-predicate-12"}
$$\exists c\ \exists k\ \forall x\ \Bigl(t(P,x)\le c\cdot\mathrm{len}(x)^k\Bigr).$$
Here $c,k$ range over positive integers and $x$ over $A^*$. The order of the
quantifiers matters: $c$ and $k$ are chosen once, before $x$. This says that
$P$ runs in polynomial time.
:::

::: {.solution for="prob-predicate-13"}
$$\exists! x\ P(x) \;\equiv\; \exists x\ \Big(P(x)\wedge\big(\forall y\ (P(y)\Rightarrow x=y)\big)\Big)$$
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-1-q2" status="draft"}
(a) $(\exists x\in\mathbb R)\bigl(x^2=0\land(\forall y\in\mathbb R)(y^2=0\implies y=x)\bigr)$: a solution exists, and every solution equals it.

(b) $(\forall x,y\in\mathbb Q)\bigl(x\ne y\implies(\exists z\in\mathbb Q)((x<z\land z<y)\lor(y<z\land z<x))\bigr)$.

(c) $(\forall x\in\mathbb Z)\bigl(x^2>4\implies(x>2\lor x<-2)\bigr)$.

(d) Every real number is a complex number.

(e) There are no two integers whose squares differ by $10$. (This is true: $x^2-y^2=(x-y)(x+y)$, and $x-y$, $x+y$ have the same parity, so the product is odd or divisible by $4$, never $10$.)

(f) For every natural number $x>1$, $2x$ is the sum of two primes. (This is Goldbach's conjecture, still unproved.)
:::

::: {.solution for="prob-mit6042f10-1-q1" status="draft"}
(a) $\exists x\,\bigl(S(x)\land A(x)\bigr)$.

(b) $\forall x\,\bigl((T(x)\land S(x))\implies A(x)\bigr)$.

(c) $\lnot\exists x\,\bigl(T(x)\land\lnot A(x)\bigr)$, equivalently $\forall x\,(T(x)\implies A(x))$.

(d) $\exists x\,\exists y\,\exists z\,\bigl(\lnot E(x,y)\land\lnot E(y,z)\land\lnot E(x,z)\land Q(x)\land Q(y)\land Q(z)\bigr)$, where $Q(w)$ abbreviates $T(w)\land\lnot S(w)$. The three inequalities make the people distinct.
:::
