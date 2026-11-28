---
title: "Cryptographic Hash Functions"
sources: [mit6046-21, mit6046r-11]
requires: [cs/hashing/perfect-hashing, cs/theory/complexity-classes]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 21 and Recitation 11, in our own wording; proofs written out in steps. -->

The hash functions of hash tables (@sec-cs-data-structures-hashing) only need to spread keys evenly. A *cryptographic* hash function must also resist an adversary who is trying to make it fail.

::: {#def-crypto-hash .definition name="Cryptographic hash function"}

A *cryptographic hash function* is a fixed, public, deterministic function $h:\{0,1\}^*\to\{0,1\}^d$ that maps strings of any length to $d$-bit *digests* (for SHA-256, $d=256$), computable in time linear in the input. Its security is stated through what a polynomial-time adversary cannot do, except with negligible probability.

:::

::: {#def-random-oracle .definition name="Random oracle"}

A *random oracle* is an idealised hash function: a box that answers each new query $x$ with a uniformly random $d$-bit string, and repeats the same answer when $x$ is asked again. Real hash functions only approximate it, but properties are often stated and proved in this model.

:::

::: {#def-hash-properties .definition name="Desirable properties"}

1. *One-way (preimage resistant):* given $y$, it is infeasible to find any $x$ with $h(x)=y$.
2. *Collision resistant:* it is infeasible to find any $x\ne x'$ with $h(x)=h(x')$.
3. *Target collision resistant (second preimage resistant):* given $x$, it is infeasible to find $x'\ne x$ with $h(x')=h(x)$.
4. *Pseudorandom:* the outputs cannot be distinguished from those of a random oracle.
5. *Non-malleable:* from $h(x)$ it is infeasible to produce $h(x')$ for a related $x'$ (such as $x+1$).

:::

::: {#prp-cr-implies-tcr .proposition name="Collision resistance implies target collision resistance"}

If $h$ is collision resistant, it is target collision resistant.

:::

::: {.proof}

An algorithm that, given $x$, finds $x'\ne x$ with $h(x')=h(x)$ also finds a collision: run it on any $x$ and output the pair $(x,x')$. So if collisions are infeasible to find, so are second preimages.

:::

One-wayness does not follow from collision resistance in general, and neither implies the other in every construction; but a random oracle has all five properties.

::: {#prp-birthday-attack .proposition name="Birthday attack"}

For a random oracle with $d$-bit outputs, about $2^{d/2}$ queries suffice to find a collision with constant probability, while finding a preimage of a given $y$ takes about $2^d$ queries.

:::

::: {.proof}

1. With $q$ distinct queries, the probability that no two answers agree is $\prod_{i<q}(1-i/2^d)\le e^{-q(q-1)/2^{d+1}}$ (as in @prp-no-collision-exact), which is at most $e^{-1/2}$ once $q\ge2^{d/2}+1$.

2. Each query hits a given $y$ with probability $2^{-d}$, so about $2^d$ queries are needed to hit it with constant probability.

:::

So a $d$-bit hash offers only $d/2$ bits of security against collisions, which is why digests of $256$ bits are used.

## Applications

1. *Password storage:* store $h(\text{password})$, not the password; one-wayness keeps a stolen file from revealing passwords. Each user gets a random *salt* $s$, storing $(s,h(s\,\|\,\text{password}))$, so that precomputed tables are useless.
2. *File integrity:* publish $h(F)$; a corrupted or replaced file is detected. This needs target collision resistance.
3. *Commitments:* to commit to a bid $x$ without revealing it, publish $h(r\,\|\,x)$ for a random $r$; later reveal $r$ and $x$. Hiding needs one-wayness (and the random $r$), binding needs collision resistance.
4. *Digital signatures:* sign $h(M)$ instead of a long message $M$ (@sec-cs-cryptography-public-key-cryptography).
