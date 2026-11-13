<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-predicate-03 origin="external" source="fit1058-cn-5.16-q3"}
$\mathrm{supervised}(X,Y)$ means person $X$ supervised the PhD of person $Y$.
Express each in predicate logic.

(a) Alonzo Church was the PhD supervisor of Alan Turing.

(b) No person supervised their own PhD.

(c) Not everyone has supervised someone else’s PhD.

(d) Not every PhD supervisor had a PhD supervisor. (Write this as an
    existential statement.)

(e) Someone had at least two PhD supervisors.

(f) Alan Turing supervised the PhDs of exactly two people.
:::

::: {.problem #prob-predicate-04 origin="external" source="fit1058-cn-5.16-q4"}
$\mathrm{designedFirstComputerIn}(X,Y)$ means person $X$ was one of the
designers of the first computer in country $Y$. Express in predicate logic:

(a) Trevor Pearcey and Maston Beard designed the first computer in
    Australia.

(b) No-one designed the first computer in two different countries.
:::

::: {.problem #prob-predicate-05 origin="external" source="fit1058-cn-5.16-q5"}
(Six degrees of separation) Consider the binary predicate
$\mathrm{knows}$ (p.68, §2.14) on the set of all people. It has been claimed
that the distance between any two people in the social network is at most 6.
Write this claim in predicate logic, using just $\mathrm{knows}$.
:::

::: {.problem #prob-predicate-06 origin="external" source="fit1058-cn-5.16-q6"}
Suppose you have the equality predicate for sets, the symmetric difference
function for sets, and set variables $A$ and $B$. Write the statement of
Theorem 4 (*For any two sets $A$ and $B$, they are identical if and
only if their symmetric difference is empty*) in predicate logic.
:::

::: {.problem #prob-predicate-09 origin="external" source="fit1058-cn-5.16-q9"}
Let $W$ range over English words, $L$ over English letters, and
$\mathrm{WordContainsLetter}(W,L)$ be True when word $W$ contains letter $L$
(e.g. $\mathrm{WordContainsLetter}(\mathtt{quizzical},\mathtt z)$ is True).

(a) Write the statement of Theorem 15 (*Every English word has a
    vowel or a ‘y’*) in predicate logic.

(b) Now also use a unary predicate $\mathrm{Vowel}$ on letters. Write
    Theorem 15 again, more compactly.
:::

::: {.problem #prob-predicate-10 origin="external" source="fit1058-cn-5.16-q10"}
Using the properties $\mathrm{Even}$, $\mathrm{Prime}$ and the binary
predicate $\le$ on $\mathbb{N}$, write a predicate logic expression for:
*There are infinitely many odd prime numbers but only finitely many even
prime numbers.*
:::

::: {.problem #prob-predicate-11 origin="external" source="fit1058-cn-5.16-q11"}
The ternary predicate $\mathrm{Date}(d,m,y)$ on $\mathbb{N}^3$ is True iff
$(d,m,y)$ is a valid Gregorian date in day-month-year format. Using
$\mathrm{Date}$ and $<$, write an expression which is True iff
$(d_1,m_1,y_1)$ and $(d_2,m_2,y_2)$ are both valid dates and the first comes
chronologically before the second.
:::

::: {.problem #prob-predicate-12 origin="external" source="fit1058-cn-5.16-q12"}
Suppose you have: the predicate $\le$; the function
$t:\{\text{programs}\}\times A^*\to\mathbb{N}$, $t(P,x)$ = time taken by program $P$
on input $x$; the function $\mathrm{len}:A^*\to\mathbb{N}_0$; multiplication and
exponentiation on positive integers; a string variable $x\in A^*$; positive
integer variables $c,k$. Write in predicate logic:
*There exist integers $c$ and $k$ such that, for every input string $x$,
the time taken by program $P$ on input $x$ is at most the product of $c$ and
the $k$-th power of the length of $x$.*
:::

::: {.problem #prob-predicate-13 origin="external" source="fit1058-cn-5.16-q13"}
$\exists!x\,P(x)$ means “there exists a unique $x$ such that $P(x)$
holds”. How would you write this statement using only the tools of
predicate logic (without “!”)?
:::
