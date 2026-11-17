---
title: "Problems, Algorithms and Models of Computation"
sources: [mit6006-1, mit6006r-1]
requires: [math/discrete/sequences/big-o]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 1 and Recitation 1, in our own wording; proofs written out in steps. -->

## Problems and algorithms

::: {#def-computational-problem .definition name="Computational problem"}

A *computational problem* is a binary relation between *inputs* and *outputs*: it says, for each input, which outputs are correct. Usually the relation is given by a predicate that a correct output must satisfy, not by a list. We study problems whose inputs can be arbitrarily large, with the *input size* (often written $n$) as a parameter.

:::

::: {#def-algorithm .definition name="Algorithm"}

An *algorithm* is a deterministic procedure, given by a finite description, that maps each input to a single output. An algorithm *solves* a problem if it returns a correct output for every input of the problem.

:::

Because an algorithm has a fixed size but must handle inputs of every size, it has to loop or call itself, and its correctness is proved by induction (@sec-math-discrete-proof-induction).

::: {#exm-birthday-matching .example name="Birthday matching"}

*Problem:* given $n$ students with their birthdays (fine enough that $n$ may exceed the number of possible days), return a pair with the same birthday, or report that there is none.

*Algorithm:* keep a record, initially empty. For $k=1,\dots,n$, look up the birthday of student $k$ in the record; if it is there, return that pair; otherwise add student $k$ to the record. If the loop ends, return "none".

*Correctness*, by induction on $k$: claim that if the first $k$ students contain a matching pair, the algorithm returns a pair before it looks at student $k+1$.

1. For $k=0$ there is no pair, so the claim holds.

2. Assume the claim for $k$. If the first $k$ students contain a pair, a pair was already returned. Otherwise any pair among the first $k+1$ students contains student $k+1$, and the algorithm compares student $k+1$ with every recorded student, so it finds the pair.

3. A pair that is returned is correct, since it is only returned after a match is seen. With $k=n$, the algorithm returns a pair if and only if one exists.

*Running time:* if the record is a plain array that is searched from the start, step $k$ takes $\Theta(k)$ time and the total is $\sum_{k=1}^n\Theta(k)=\Theta(n^2)$. A better data structure for the record (a hash table, @sec-cs-data-structures-hashing) brings this down to $O(n)$ expected time.

:::

## Efficiency

We measure the running time of an algorithm by the number of fixed-time operations it performs, as a function of the input size, and compare functions with asymptotic notation (@def-big-o, @def-big-omega-big-theta-extra). An algorithm is *efficient* if its running time is bounded by a polynomial in the input size.

::: {#rmk-problems-and-algorithms-growth .remark name="How fast the classes grow"}

At about $10^9$ operations per second, an input of size $n=1000$ takes about a nanosecond for $\Theta(1)$, $10$ ns for $\Theta(\log n)$, a microsecond for $\Theta(n)$, $10$ microseconds for $\Theta(n\log n)$ and a millisecond for $\Theta(n^2)$. An exponential algorithm, $2^{\Theta(n)}$, needs about $2^{1000}\approx10^{301}$ operations, which is far beyond the age of the universe. Polynomial versus exponential is the line between feasible and infeasible.

:::

## The model of computation

To count "fixed-time operations" we must say which operations take constant time. That choice is a *model of computation*.

::: {#def-word-ram .definition name="Word-RAM"}

In the *word-RAM* model with word size $w$, memory is an array of $w$-bit *words*, each with an address. In $O(1)$ time the processor can

1. do integer arithmetic ($+,-,\times$, integer division, remainder), comparisons and bitwise operations on a constant number of words, and
2. read or write the word at a given address.

Addresses must fit in a word, so a machine that stores $n$ words needs $w\ge\log_2n$.

:::

::: {#rmk-problems-and-algorithms-word-size .remark name="Numbers fit in a word"}

Unless a problem says otherwise, we assume that each input number fits in a word, so that comparing or adding two of them costs $O(1)$. When numbers can be longer, their length becomes a parameter of the running time (for example, adding two $b$-bit numbers takes $O(\lceil b/w\rceil)$ time).

:::

## Data structures and how to solve a problem

A *data structure* stores a non-constant amount of data and supports a set of operations on it. The operations it promises form its *interface*; the data structure itself is one way to implement them (@sec-cs-data-structures-interfaces).

::: {#rmk-problems-and-algorithms-strategy .remark name="Two ways to solve a problem"}

1. *Reduce* it to a problem you already know how to solve: use a known data structure (arrays, hash tables, balanced trees, heaps), a sorting algorithm, or a graph algorithm (breadth-first search, shortest paths).
2. *Design* a new recursive algorithm: brute force, decrease and conquer, divide and conquer, dynamic programming, or a greedy method (@sec-cs-dynamic-programming-recursive-algorithms).

:::
