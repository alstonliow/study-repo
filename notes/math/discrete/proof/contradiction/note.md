---
title: "Proof by contradiction"
sources: [fit1058-cn-3.9]
requires: []
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/03-proofs.tex: Proof by contradiction. -->

::: {.remark name="Pattern"}

Assume the *negation* of the claim; reason from it to a contradiction (some statement and its negation both derived as true); conclude the assumption was false, so the original claim holds.

:::

::: {#exm-infinitely-many-primes .example name="Infinitely many primes"}

There are infinitely many prime numbers.

:::

::: {.proof}

Suppose, for contradiction, that there are only finitely many primes $p_1,p_2,\dots,p_n$. Let
$$q = p_1 p_2 \cdots p_n + 1.$$
Since $q > p_i$ for every $i$, $q$ is not itself prime, so $q$ is composite and hence divisible by some prime. But for each $p_i$, dividing $q$ by $p_i$ leaves remainder $1$ (since $p_i$ divides $p_1\cdots p_n$ exactly), so $p_i \nmid q$. So $q$ is divisible by no prime at all – contradicting that $q$ is composite. Hence the assumption was false: there are infinitely many primes.

:::

::: {.remark name="A useful auxiliary fact used implicitly"}

The argument above (and many proofs by contradiction over $\mathbb{N}$ or $\mathbb{Z}^+$) relies on: any nonempty set of natural numbers has a smallest element (well-ordering). This lets you say things like “let $n$ be the smallest counterexample” and derive a contradiction from its minimality.

:::

::: {#exm-contradiction-1 .example}

$\sqrt{2}$ is irrational.

:::

::: {.proof}

Suppose, for contradiction, that $\sqrt2$ is rational: $\sqrt2 = a/b$ for integers $a,b$ with no common factor (in lowest terms). Squaring, $2 = a^2/b^2$, so $a^2 = 2b^2$ – hence $a^2$ is even, hence $a$ is even (an odd number squares to an odd number), say $a = 2c$. Substituting: $4c^2 = 2b^2$, so $b^2 = 2c^2$ – hence $b^2$ is even, hence $b$ is even. But then $a$ and $b$ are *both* even, contradicting that $a/b$ was in lowest terms. So the assumption was false: $\sqrt2$ is irrational.

:::

::: {.remark}

Alongside Euclid’s proof, this is the other canonical proof-by-contradiction example in mathematics – both hinge on deriving a property (divisibility, in each case) that eventually contradicts an assumption baked into the setup (finiteness of the prime list; lowest-terms form of the fraction).

:::

::: {.remark name="Open problems"}

Not every true mathematical statement has a known proof. An *open problem* is a precisely stated claim believed true (or at least undecided) but not yet proved or disproved.

:::

::: {#exm-the-collatz-conjecture .example name="The Collatz conjecture"}

Define, for $n\in\mathbb{Z}^+$:
$$\mathrm{Collatz}(n) = \begin{cases} n/2, & n \text{ even}, \\ 3n+1, & n \text{ odd}. \end{cases}$$
*Conjecture*: iterating $\mathrm{Collatz}$ from any starting $n\in\mathbb{Z}^+$ eventually reaches $1$.

:::

::: {.remark}

Verified by computer for enormous ranges of starting values, but no proof (or disproof) is known – an active open problem since 1937. Contrast with Euclid’s infinitude-of-primes proof (@sec-math-discrete-proof-contradiction above): that claim, once conjectured, was fully settled by a short contradiction argument; Collatz has resisted proof for nearly a century despite its simple statement.

:::
