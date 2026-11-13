---
title: "Sequences: Definitions and Basic Types"
sources: [fit1058-cn-6.1, fit1058-cn-6.2, fit1058-cn-6.3, fit1058-cn-6.4, fit1058-cn-6.5]
requires: [math/discrete/sequences/sums-and-series, math/discrete/sets/cartesian-product, math/discrete/sets/sets-and-elements]
status: draft
---

<!-- Migrated from 1058note notes/chapters/06-sequences-series.tex: Definitions and notation; Recursive definitions of sequences; Arithmetic sequences; Geometric sequences; Harmonic sequences. -->

## Definitions and notation

::: {#def-sequence .definition name="Sequence"}

A *sequence* is a function whose domain is $\mathbb{N}$ (an *infinite sequence*) or $\{1,\dots,n\}$ for some $n$ (a *finite sequence*, i.e. an ordered $n$-tuple, @sec-math-discrete-sets-cartesian-product).

:::

::: {#def-term-length .definition name="Term, length"}

For a sequence $f$, the value $f(n)$, also written $f_n$, is its *$n$-th term*. The *length* of a finite sequence is the number of its terms, i.e. the size of its domain.

:::

::: {.remark name="Indexing from $0$"}

Some books index sequences from $0$ instead of $1$, i.e. use domain $\{0,1,2,\dots\}$. This only shifts the subscripts; the sequence is the same.

:::

::: {.remark name="Ways to specify a sequence"}

- List all its terms (only practical if it is short).

- Give a formula for the $n$-th term, e.g. $(n^2 : n\in\mathbb{N})$ or $(n^2)_{n=1}^{\infty}$. This is like set-builder notation (@sec-math-discrete-sets-sets-and-elements), but with parentheses because order matters.

- Give a recurrence relation (@sec-math-discrete-sequences-basic-sequences), defining each term from earlier ones.

Listing a few terms and trusting the “pattern” does *not* define a sequence: infinitely many different sequences start the same way. For example, $1,2,4,8,16$ continues as $32$ if $f_n=2^{n-1}$, but as $31$ if $f_n$ is the number of regions formed by joining $n$ points on a circle.

:::

## Recursive definitions of sequences

::: {#def-recurrence-relation .definition name="Recurrence relation"}

A *recurrence relation* for $(a_n)$ expresses $a_n$ in terms of one or more earlier terms, together with enough *base cases* (initial terms given explicitly) to determine every term uniquely.

:::

::: {.remark name="Same shape as induction"}

A recursive definition has a **base case**, defining finitely many of the simplest terms directly, and a **recursive case**, defining a general term from earlier ones. This mirrors the base case and inductive step of a proof by induction, which is why induction is the natural way to prove things about recursively defined sequences.

:::

::: {#exm-basic-sequences-1 .example}

- $f_1=1$, $f_n=f_{n-1}+2$ gives $1,3,5,7,\dots$ (the odd numbers).

- $f_1=0$, $f_n=f_{n-1}+2$ gives $0,2,4,6,\dots$: the same rule with a different base case gives a different sequence.

- $f_1=1$, $f_n=nf_{n-1}$ gives $1,2,6,24,120,\dots$, i.e. $f_n=n!$.

:::

::: {.remark name="Multiple base cases"}

A rule such as $f_n=4f_{n-2}$, which looks *two* terms back, needs two base cases $f_1,f_2$; one base case alone fixes only every other term. For example, $f_1=2$, $f_2=0$, $f_n=4f_{n-2}$ gives $2,0,8,0,32,0,\dots$

:::

## Arithmetic sequences

::: {#def-arithmetic-sequence .definition name="Arithmetic sequence"}

An *arithmetic sequence* has a constant difference $d$ between consecutive terms: $f_1=a$, $f_n=f_{n-1}+d$. Its $n$-th term is $a+(n-1)d$.

:::

::: {#exm-basic-sequences-1-2 .example}

The positive integers ($a=1,d=1$), the odd numbers ($a=1,d=2$), and $10,7,4,1,-2,\dots$ ($a=10,d=-3$).

:::

## Geometric sequences

::: {#def-geometric-sequence .definition name="Geometric sequence"}

A *geometric sequence* has a constant ratio $r$ between consecutive terms: $f_1=a$, $f_n=f_{n-1}\cdot r$. Its $n$-th term is $ar^{n-1}$.

:::

::: {#exm-basic-sequences-1-3 .example}

The powers of $2$, $1,2,4,8,\dots$ ($a=1,r=2$), and $1,\frac12,\frac14,\frac18,\dots$ ($a=1,r=\frac12$).

:::

::: {.remark name="Arithmetic vs.\ geometric"}

Arithmetic sequences grow by *adding* the same amount each time; geometric sequences grow by *multiplying* by the same amount. For $r>1$, geometric growth eventually beats any arithmetic growth.

:::

## Harmonic sequences

::: {#def-harmonic-sequence .definition name="Harmonic sequence"}

$(a_n)$ is *harmonic* if $(1/a_n)$ is arithmetic.

:::

::: {#exm-basic-sequences-1-4 .example}

$(1/n : n\in\mathbb{N})$, i.e. $1,\frac12,\frac13,\dots$, is harmonic, since $1,2,3,\dots$ is arithmetic. Its partial sums are the harmonic numbers (@sec-math-discrete-sequences-sums-and-series).

:::
