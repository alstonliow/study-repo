---
title: "Randomized Algorithms"
sources: [mit6046-6, mit6046r-4]
requires: [math/probability/random-variables/expectation-and-variance]
aliases: [cs/algorithm-design/randomized-algorithms]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 6 and Recitation 4, in our own wording; proofs written out in steps. On 2026-11-25 the algorithms moved to their own notes (one algorithm per note, SPEC §8.6); this note is their overview. -->

A *randomized algorithm* uses random numbers to make decisions, so on the same input different runs may behave differently. A *Monte Carlo* algorithm always runs fast and is *probably* correct; a *Las Vegas* algorithm is always correct and *probably* fast (its running time is a random variable whose expectation we bound). The probabilities are over the algorithm's own coins, for every input; no assumption about the inputs is made.

## The algorithms

Each algorithm has its own note: Freivalds' check of a matrix product (@sec-cs-algorithms-freivalds), randomized quicksort (@sec-cs-sorting-quicksort) and randomized selection (@sec-cs-sorting-randomized-selection).

| algorithm | kind | time | error |
|---|---|---|---|
| Freivalds' check (@thm-freivalds) | Monte Carlo | $O(n^2)$ per trial | at most $\frac12$ per trial |
| randomized quicksort (@thm-randomized-quicksort) | Las Vegas | $O(n\log n)$ expected | none |
| randomized selection (@thm-randomized-select) | Las Vegas | $O(n)$ expected | none |
