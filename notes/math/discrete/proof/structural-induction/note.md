---
title: "Recursive Data Types and Structural Induction"
sources: [mcs-6.1, mcs-6.2, mcs-6.3, mcs-6.4]
requires: [math/discrete/proof/state-machines]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.042J, Mathematics for Computer Science (2015), Chapter 6, in our own wording; proofs written out in steps. -->

## Recursive definitions

::: {#def-recursive-data-type .definition name="Recursive definition of a set"}

A *recursive definition* of a set $R$ consists of

- *base cases*, which state that certain elements are in $R$, and
- *constructor cases*, which state how to build new elements of $R$ from elements already in $R$,

together with the *extremal clause*: $R$ contains nothing except what the base and constructor cases force into it.

:::

::: {#exm-recursive-strings .example name="Strings and matched brackets"}

1. The strings $A^*$ over an alphabet $A$: the empty string $\lambda$ is in $A^*$ (base case); if $s\in A^*$ and $a\in A$, then the string $as$ is in $A^*$ (constructor).

2. The set $M$ of *matched* bracket strings over $\{\texttt{[},\texttt{]}\}$: $\lambda\in M$; and if $s,t\in M$, then $\texttt{[}s\texttt{]}t\in M$.

3. Arithmetic expressions in one variable $x$: $x$ and every numeral are expressions; if $e,f$ are expressions, so are $(e+f)$, $(e*f)$ and $-(e)$.

:::

## Structural induction

::: {#thm-structural-induction .theorem name="Structural induction"}

Let $R$ be recursively defined, and $P$ a property of elements of $R$. If $P$ holds for every base-case element, and every constructor applied to elements with property $P$ produces an element with property $P$, then $P$ holds for every element of $R$.

:::

::: {.proof}

1. Every element of $R$ is obtained by finitely many applications of the base and constructor cases (extremal clause). Let the *depth* of an element be the least number of constructor applications needed to build it.

2. We show by strong induction on $d$ that every element of depth $d$ has property $P$. Elements of depth $0$ are base-case elements.

3. An element of depth $d>0$ is a constructor applied to elements of smaller depth, which have $P$ by the hypothesis; so it has $P$ by the constructor assumption.

:::

::: {#prp-matched-strings-balanced .proposition name="Matched strings are balanced"}

Every string in $M$ has as many left brackets as right brackets, and every prefix of it has at least as many left as right brackets.

:::

::: {.proof}

By structural induction on $M$, with $P(s)$ the stated property. For $u$ a string, let $\ell(u)$ and $r(u)$ count its left and right brackets.

1. *Base case:* $\lambda$ has no brackets.

2. *Constructor:* let $s,t\in M$ satisfy $P$, and $u=\texttt{[}s\texttt{]}t$. Then $\ell(u)=1+\ell(s)+\ell(t)=1+r(s)+r(t)=r(u)$.

3. A prefix of $u$ is either $\texttt{[}s'$ with $s'$ a prefix of $s$, which has $1+\ell(s')-r(s')\ge1$ more left brackets; or $\texttt{[}s\texttt{]}t'$ with $t'$ a prefix of $t$, which has $\ell(t')-r(t')\ge0$ more.

:::

The converse also holds: a bracket string with equal counts whose prefixes never have more right than left brackets is in $M$ (split it at the first point where the counts become equal).

## Recursive functions

::: {#def-recursive-function .definition name="Function defined by structural recursion"}

A function on a recursively defined set $R$ can be defined by giving its value on each base-case element, and its value on a constructed element in terms of the values on the parts. This is well defined when the definition is *unambiguous*: every element of $R$ is built in exactly one way.

:::

::: {#exm-recursive-functions .example name="Length, concatenation and depth"}

1. Length on $A^*$: $|\lambda|=0$ and $|as|=1+|s|$.

2. Concatenation: $\lambda\cdot t=t$ and $(as)\cdot t=a(s\cdot t)$. By structural induction on $s$, $|s\cdot t|=|s|+|t|$: for $s=\lambda$ both sides are $|t|$; and $|(as)\cdot t|=1+|s\cdot t|=1+|s|+|t|=|as|+|t|$.

3. On $M$, the nesting depth $d(\lambda)=0$, $d(\texttt{[}s\texttt{]}t)=\max(d(s)+1,d(t))$ is well defined, because each non-empty matched string splits as $\texttt{[}s\texttt{]}t$ in only one way ($\texttt{]}$ closes the first $\texttt{[}$ at the first point where the counts become equal).

:::

::: {#rmk-structural-induction-ambiguity .remark name="Ambiguous definitions"}

If the same element can be built in two ways, a "recursive function" may receive two different values. For example, defining matched strings also by "if $s,t\in M$ then $st\in M$" makes $\texttt{[]}\texttt{[]}\texttt{[]}$ buildable in two ways, and a function defined by $f(st)=f(s)+2f(t)$ would not be well defined. Before defining a function recursively, check that the recursive definition is unambiguous.

:::

::: {#exm-recursion-on-naturals .example name="Recursion on the natural numbers"}

$\mathbb N$ is recursively defined by: $0\in\mathbb N$; if $n\in\mathbb N$ then $n+1\in\mathbb N$. Structural induction on this definition is ordinary induction, and structural recursion gives definitions such as $0!=1$, $(n+1)!=(n+1)\cdot n!$. Not every recursive "definition" on $\mathbb N$ defines a total function: $f(n)=1+f(n+1)$ defines nothing, and whether $g(1)=1$, $g(n)=g(n/2)$ for even $n$, $g(n)=g(3n+1)$ for odd $n>1$ defines $g$ on all of $\mathbb Z^+$ is the open Collatz problem (@exm-iterated-collatz).

:::
