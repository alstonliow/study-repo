<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-proofs-10 origin="external" source="fit1058-cn-3.15-q10"}
Consider the following algorithm:

> for each $i=1,2,\dots,n$:\
> for each $j=1,2,\dots,i$:\
> for each $k=1,2,\dots,j$:\
> \[some action\]

(a) For each pair $i,j$, how many times is the action performed?

(b) For each $i$, how many times is the action performed? Write this
    both as a sum and (using a theorem in this chapter) as a simple
    algebraic expression in $i$.

(c) Write a sum, in terms of $n$, for the total number of times the
    action is performed.

(d) Work out this expression for $n=1,2,3,4,5$ (and more).

(e) Explore how these numbers behave.

(f) Conjecture a simple algebraic expression in $n$ for the total.

(g) Prove, by induction on $n$, that your expression is correct.
:::

::: {.problem #prob-proofs-11 origin="external" source="fit1058-cn-3.15-q11"}
The $n$-th harmonic number is $H_n = 1+\frac12+\frac13+\cdots+\frac1n$. We
prove by induction that $H_n\ge\log_e(n+1)$.

(i) Inductive basis: prove that $H_1\ge\log_e(1+1)$.

(ii) Let $n\ge1$ and assume $H_n\ge\log_e(n+1)$. Write $H_{n+1}$
     recursively using $H_n$, use the inductive hypothesis, then use
     $\log_e(1+x)\le x$ and an elementary property of logarithms to show
     $H_{n+1}\ge\log_e(n+2)$.

(iii) What can you now conclude, and why?

Afterthoughts: try to prove $H_n\ge\log_e n$ directly by induction — where
is the snag? Would the proof work for other bases? Can you prove
$H_n\le(\log_e n)+1$?
:::
