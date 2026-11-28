---
title: "Direct Access Arrays and Hashing"
sources: [mit6006-4, mit6006r-4]
requires: [math/probability/limit-theorems/hashing-and-load-balancing, math/discrete/number-theory/modular-arithmetic]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 4 and Recitation 4, in our own wording; the universality proof is written out in steps (the lecture states the result without proof). Complements the probabilistic view in @sec-math-probability-limit-theorems-hashing-and-load-balancing. -->

## Direct access arrays

::: {#def-direct-access-array .definition name="Direct access array"}

If every key is an integer in $\{0,\dots,u-1\}$, a *direct access array* is a static array of length $u$ whose slot $k$ holds the item with key $k$ (or is empty). `find`, `insert` and `delete` take $O(1)$ time in the worst case, because the key is used directly as an address. Building it and the order operations take $\Theta(u)$ time, and it uses $\Theta(u)$ space.

:::

This beats the $\Omega(\log n)$ search bound (@thm-comparison-search-lower-bound) because reading slot $k$ is an operation with $u$ possible outcomes, not two. But the space is $\Theta(u)$, which is hopeless when the key space is much larger than the number $n$ of stored items (ten-letter names give $u=26^{10}$).

## Hash tables

::: {#def-hash-table .definition name="Hash function, hash table, chaining"}

A *hash function* is a function $h:\{0,\dots,u-1\}\to\{0,\dots,m-1\}$, usually with $m=\Theta(n)\ll u$. A *hash table* is a direct access array of length $m$ in which the item with key $k$ is stored at index $h(k)$, the *hash* of $k$. Two keys *collide* if they have the same hash. With *chaining*, slot $j$ holds a *chain*: a small sequence (for example a linked list) of all stored items whose keys hash to $j$. The ratio $\alpha=n/m$ is the *load factor*.

:::

```{=latex}
\begin{algorithm}
\caption{Hash table with chaining}
\begin{algorithmic}
\STATE \textbf{find}$(k)$:
\RETURN the item with key $k$ in the chain $T[h(k)]$, or none
\STATE \textbf{insert}$(x)$:
\IF{the chain $T[h(x.\mathrm{key})]$ has an item with key $x.\mathrm{key}$}
    \STATE replace it by $x$
\ELSE
    \STATE add $x$ to the chain $T[h(x.\mathrm{key})]$
\ENDIF
\STATE \textbf{delete}$(k)$:
\STATE remove the item with key $k$ from the chain $T[h(k)]$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-hashing-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0,0.0) rectangle (0.6,0.55);
\node[lab,tick] at (-0.25,0.27) {0};
\node[box] (c00) at (1.5,0.27) {$15$};
\draw[->] (0.6,0.27) -- (c00);
\draw[cell frame] (0,-0.65) rectangle (0.6,-0.10);
\node[lab,tick] at (-0.25,-0.38) {1};
\node[box] (c10) at (1.5,-0.38) {$26$};
\draw[->] (0.6,-0.38) -- (c10);
\draw[cell frame] (0,-1.3) rectangle (0.6,-0.75);
\node[lab,tick] at (-0.25,-1.03) {2};
\node[box] (c20) at (1.5,-1.03) {$12$};
\draw[->] (0.6,-1.03) -- (c20);
\node[box] (c21) at (3.1,-1.03) {$7$};
\draw[->] (2.08,-1.03) -- (c21);
\draw[cell frame] (0,-1.95) rectangle (0.6,-1.40);
\node[lab,tick] at (-0.25,-1.68) {3};
\draw[cell frame] (0,-2.6) rectangle (0.6,-2.05);
\node[lab,tick] at (-0.25,-2.33) {4};
\node[box] (c40) at (1.5,-2.33) {$19$};
\draw[->] (0.6,-2.33) -- (c40);
\node[box] (c41) at (3.1,-2.33) {$4$};
\draw[->] (2.08,-2.33) -- (c41);
\node[lab, anchor=west] at (5.6,-0.9) {$h(k)=k\bmod5$};
\end{tikzpicture}
\end{center}
```

A hash table of size $5$ with chaining, after inserting $12,7,19,4,26,15$ with $h(k)=k\bmod5$. Keys that collide share a chain; an operation scans only the chain at $h(k)$.

:::

When $m<u$, collisions are unavoidable by the pigeonhole principle (@thm-pigeonhole). An operation on key $k$ scans the chain at $h(k)$, so it costs $O(1)$ plus the length of that chain. For any *fixed* hash function and $u\ge nm$, some set of $n$ keys all hash to the same slot, giving chains of length $n$. The way out is to choose the hash function at random.

::: {#def-universal-hash-family .definition name="Universal hash family"}

A set $\mathcal H$ of hash functions $\{0,\dots,u-1\}\to\{0,\dots,m-1\}$ is *universal* if for all keys $k\ne l$,
$$\Pr_{h\in\mathcal H}\bigl(h(k)=h(l)\bigr)\le\frac1m,$$
where $h$ is chosen uniformly at random from $\mathcal H$.

:::

::: {#thm-universal-hash-family .theorem name="A universal family"}

Let $p\ge u$ be a prime. For $a\in\{1,\dots,p-1\}$ and $b\in\{0,\dots,p-1\}$ let
$$h_{ab}(k)=\bigl((ak+b)\bmod p\bigr)\bmod m.$$
Then $\mathcal H=\{h_{ab}\}$ is universal.

:::

::: {.proof}

1. Fix keys $k\ne l$ in $\{0,\dots,u-1\}$ and let $r=(ak+b)\bmod p$ and $s=(al+b)\bmod p$. Then $r-s\equiv a(k-l)\pmod p$. Since $p$ is prime and neither $a$ nor $k-l$ is divisible by $p$ (as $0<|k-l|<p$), $r\ne s$.

2. The map $(a,b)\mapsto(r,s)$ is a bijection from the $p(p-1)$ choices of $(a,b)$ to the $p(p-1)$ pairs $(r,s)$ with $r\ne s$: given $(r,s)$, the congruences force $a\equiv(r-s)(k-l)^{-1}$ and $b\equiv r-ak\pmod p$, where the inverse exists by @thm-inverse. So for random $(a,b)$, the pair $(r,s)$ is uniform over all pairs with $r\ne s$.

3. $h_{ab}(k)=h_{ab}(l)$ exactly when $r\equiv s\pmod m$. For fixed $r$, the values $s\in\{0,\dots,p-1\}$ with $s\equiv r\pmod m$ number at most $\lceil p/m\rceil$, one of which is $r$ itself. So at most $\lceil p/m\rceil-1\le\frac{p-1}m$ values of $s\ne r$ collide with $r$.

4. Given $r$, $s$ is uniform over the $p-1$ values $\ne r$, so the collision probability is at most $\frac{(p-1)/m}{p-1}=\frac1m$.

:::

::: {#thm-chain-length .theorem name="Expected chain length"}

Store $n$ keys in a hash table of size $m$ with a hash function drawn from a universal family. For each stored key $k_i$, the expected length of the chain containing it is at most $1+\frac{n-1}m$. With $m=\Omega(n)$ this is $O(1)$, so `find`, `insert` and `delete` take $O(1)$ expected time.

:::

::: {.proof}

1. Let $X_{ij}$ be the indicator variable (@def-indicator-variable) of the event $h(k_i)=h(k_j)$. The chain of $k_i$ has length $X_i=\sum_jX_{ij}$, where $X_{ii}=1$.

2. By linearity of expectation (@thm-linearity-of-expectation) and @prp-expectation-of-indicator,
   $$E[X_i]=1+\sum_{j\ne i}\Pr\bigl(h(k_i)=h(k_j)\bigr)\le1+\frac{n-1}m.$$

3. A search for a key that is not stored scans one chain, whose expected length is at most $\frac nm$ by the same computation without the term $X_{ii}$.

:::

::: {#rmk-hashing-resizing .remark name="Keeping the table the right size"}

As items are inserted and deleted, $n$ drifts away from $m$. When $n/m$ leaves a fixed range, build a new table of size $\Theta(n)$ with a freshly drawn hash function and reinsert everything in $O(n)$ expected time. The same argument as for dynamic arrays (@prp-dynamic-array-shrink) shows that the rebuilds cost $O(1)$ amortized per operation, so a hash table supports dictionary operations in *expected amortized* $O(1)$ time. The expectation is over the random choice of hash function only; no assumption about the input keys is needed.

:::

::: {#rmk-hashing-practice .remark name="Hashing in practice"}

The simple *division method* $h(k)=k\bmod m$ is a heuristic that works when keys are spread evenly; a prime $m$ far from powers of $2$ and $10$ avoids common patterns in keys. Python's `dict` and `set` are hash tables (using *open addressing*, which stores colliding items in other slots of the same array instead of in chains). A hash table gives no help with order operations such as `find_min` or `find_next`, which take $\Theta(n)$ time.

:::

| set data structure | `build` | `find` | `insert`, `delete` | `find_min`, `find_max` | `find_prev`, `find_next` |
|---|---|---|---|---|---|
| array | $n$ | $n$ | $n$ | $n$ | $n$ |
| sorted array | $n\log n$ | $\log n$ | $n$ | $1$ | $\log n$ |
| direct access array | $u$ | $1$ | $1$ | $u$ | $u$ |
| hash table | $n$ (e) | $1$ (e) | $1$ (a)(e) | $n$ | $n$ |

(e) expected, (a) amortized.
