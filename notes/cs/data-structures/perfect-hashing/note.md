---
title: "Universal and Perfect Hashing"
sources: [mit6046-8]
requires: [cs/data-structures/hashing]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 8, in our own wording; proofs written out in steps. Universal families and chaining are in @sec-cs-data-structures-hashing. -->

## A dot-product universal family

::: {#thm-dot-product-hash .theorem name="Dot-product hashing is universal"}

Let $m$ be prime and $u=m^r$. Write each key $k$ in base $m$ as a vector $(k_0,\dots,k_{r-1})$ of digits, and for a vector $a=(a_0,\dots,a_{r-1})$ of digits let
$$h_a(k)=\Bigl(\sum_{i=0}^{r-1}a_ik_i\Bigr)\bmod m.$$
Then $\{h_a\}$, with $a$ chosen uniformly from all $m^r$ vectors, is a universal family (@def-universal-hash-family).

:::

::: {.proof}

1. Let $k\ne l$; they differ in some digit, say $k_d\ne l_d$.

2. $h_a(k)=h_a(l)$ exactly when $a_d(k_d-l_d)\equiv-\sum_{i\ne d}a_i(k_i-l_i)\pmod m$.

3. Fix the other digits $a_i$, $i\ne d$. Since $m$ is prime and $k_d-l_d\not\equiv0$, this congruence has exactly one solution $a_d$ modulo $m$ (@thm-inverse).

4. So for each choice of the other $r-1$ digits, exactly one of the $m$ values of $a_d$ causes a collision: the probability is $\frac1m$.

:::

## Perfect hashing

For a *static* set of $n$ keys (built once, then only searched), we can get $O(1)$ worst-case search time with $O(n)$ space.

::: {#def-perfect-hashing .definition name="Two-level (FKS) perfect hashing"}

1. *Level 1:* hash the $n$ keys into $m=n$ slots with a function $h_1$ from a universal family; let $n_j$ be the number of keys in slot $j$. If $\sum_jn_j^2>cn$ for a fixed constant $c$ (for example $c=4$), choose a new $h_1$ and repeat.
2. *Level 2:* for each slot $j$, hash its $n_j$ keys into a table of size $m_j=n_j^2$ with a function $h_{2,j}$ from a universal family; if two of them collide, choose a new $h_{2,j}$ and repeat.

A search computes $j=h_1(x)$, then looks in slot $h_{2,j}(x)$ of table $j$: two hash evaluations, $O(1)$ in the worst case.

:::

::: {#fig-perfect-hashing-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0,0.00) rectangle (0.5,0.50);
\node[lab,tick] at (-0.25,0.25) {0};
\draw[->] (0.5,0.25) -- (1.0,0.25);
\draw[hl cell] (1.050,0.000) rectangle (1.550,0.500);
\node[lab] at (1.300,0.250) {$72$};
\draw[cell frame] (0,-0.55) rectangle (0.5,-0.05);
\node[lab,tick] at (-0.25,-0.30) {1};
\draw[->] (0.5,-0.30) -- (1.0,-0.30);
\draw[cell frame] (1.050,-0.550) rectangle (1.550,-0.050);
\draw[hl cell] (1.550,-0.550) rectangle (2.050,-0.050);
\node[lab] at (1.800,-0.300) {$37$};
\draw[hl cell] (2.050,-0.550) rectangle (2.550,-0.050);
\node[lab] at (2.300,-0.300) {$10$};
\draw[cell frame] (2.550,-0.550) rectangle (3.050,-0.050);
\draw[cell frame] (0,-1.10) rectangle (0.5,-0.60);
\node[lab,tick] at (-0.25,-0.85) {2};
\draw[cell frame] (0,-1.65) rectangle (0.5,-1.15);
\node[lab,tick] at (-0.25,-1.40) {3};
\draw[->] (0.5,-1.40) -- (1.0,-1.40);
\draw[hl cell] (1.050,-1.650) rectangle (1.550,-1.150);
\node[lab] at (1.300,-1.400) {$75$};
\draw[cell frame] (0,-2.20) rectangle (0.5,-1.70);
\node[lab,tick] at (-0.25,-1.95) {4};
\draw[->] (0.5,-1.95) -- (1.0,-1.95);
\draw[hl cell] (1.050,-2.200) rectangle (1.550,-1.700);
\node[lab] at (1.300,-1.950) {$40$};
\draw[cell frame] (1.550,-2.200) rectangle (2.050,-1.700);
\draw[hl cell] (2.050,-2.200) rectangle (2.550,-1.700);
\node[lab] at (2.300,-1.950) {$22$};
\draw[cell frame] (2.550,-2.200) rectangle (3.050,-1.700);
\draw[cell frame] (0,-2.75) rectangle (0.5,-2.25);
\node[lab,tick] at (-0.25,-2.50) {5};
\draw[cell frame] (0,-3.30) rectangle (0.5,-2.80);
\node[lab,tick] at (-0.25,-3.05) {6};
\draw[->] (0.5,-3.05) -- (1.0,-3.05);
\draw[hl cell] (1.050,-3.300) rectangle (1.550,-2.800);
\node[lab] at (1.300,-3.050) {$60$};
\draw[cell frame] (0,-3.85) rectangle (0.5,-3.35);
\node[lab,tick] at (-0.25,-3.60) {7};
\draw[->] (0.5,-3.60) -- (1.0,-3.60);
\draw[hl cell] (1.050,-3.850) rectangle (1.550,-3.350);
\node[lab] at (1.300,-3.600) {$52$};
\draw[cell frame] (1.550,-3.850) rectangle (2.050,-3.350);
\draw[hl cell] (2.050,-3.850) rectangle (2.550,-3.350);
\node[lab] at (2.300,-3.600) {$70$};
\draw[cell frame] (2.550,-3.850) rectangle (3.050,-3.350);
\draw[cell frame] (0,-4.40) rectangle (0.5,-3.90);
\node[lab,tick] at (-0.25,-4.15) {8};
\end{tikzpicture}
\end{center}
```

Two-level perfect hashing of nine keys. Level $1$ uses $h_1(k)=k\bmod9$; a slot with $n_j$ keys gets its own collision-free table of size $n_j^2$ (here $h_2(k)=k\bmod n_j^2$). Here the level-2 tables have $\sum_jn_j^2=15$ slots in all, linear in $n$.

:::

::: {#lem-birthday-perfect .lemma name="Quadratic tables avoid collisions"}

If $n_j$ keys are hashed into $n_j^2$ slots with a universal family, then with probability at least $\frac12$ there is no collision.

:::

::: {.proof}

There are $\binom{n_j}2$ pairs, each colliding with probability at most $\frac1{n_j^2}$. By the union bound the probability of some collision is at most $\binom{n_j}2\frac1{n_j^2}<\frac12$.

:::

::: {#lem-sum-squares .lemma name="Total size of the level-2 tables"}

With $h_1$ universal into $n$ slots, $E\bigl[\sum_jn_j^2\bigr]<2n$. So $\sum_jn_j^2\le4n$ with probability at least $\frac12$, by Markov's inequality.

:::

::: {.proof}

1. $\sum_jn_j^2$ counts ordered pairs of keys (including a key with itself) that land in the same slot: $\sum_jn_j^2=n+2\cdot\#\{\text{colliding unordered pairs}\}$.

2. By linearity, the expected number of colliding pairs is at most $\binom n2\frac1n<\frac n2$, so $E[\sum_jn_j^2]<n+n=2n$.

3. By @thm-markov-inequality, $\Pr(\sum_jn_j^2>4n)<\frac{2n}{4n}=\frac12$.

:::

::: {#thm-perfect-hashing .theorem name="Perfect hashing"}

The two-level scheme stores $n$ keys in $O(n)$ space, answers searches in $O(1)$ worst-case time, and is built in $O(n)$ expected time.

:::

::: {.proof}

1. *Space:* level 1 has $n$ slots and level 2 has $\sum_jn_j^2\le cn$ slots, plus $O(1)$ words per hash function.

2. *Build time:* each attempt at level 1 costs $O(n)$ and succeeds with probability at least $\frac12$, so the expected number of attempts is at most $2$ (a geometric random variable, @def-geometric-distribution). Each level-2 table $j$ costs $O(n_j^2)$ per attempt and also needs at most $2$ attempts in expectation, so level 2 costs $O(\sum_jn_j^2)=O(n)$ expected.

:::

::: {#rmk-perfect-hashing-why .remark name="Why two levels"}

Hashing all $n$ keys into $n^2$ slots directly would also avoid collisions with probability $\frac12$, but would use $\Theta(n^2)$ space. Spreading the keys first, and paying quadratic space only inside each small slot, keeps the total linear.

:::
