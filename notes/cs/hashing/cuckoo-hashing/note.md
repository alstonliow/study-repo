---
title: "Cuckoo Hashing"
sources: [mit6851-10]
requires: [cs/hashing/independent-hash-families]
aliases: [cs/data-structures/cuckoo-hashing]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-27 from MIT 6.851 (Spring 2012), Lecture 10, in our own wording; proofs written out in steps. Only the simplest case of the analysis is proved here; the cycle cases are summarised. -->

Cuckoo hashing (Pagh and Rodler) keeps every key in one of two possible slots, so a search looks at exactly two places, and an insertion kicks out ("bumps") an occupant to its other slot, like a cuckoo laying eggs in other birds' nests.

::: {#def-cuckoo-hashing .definition name="Cuckoo hashing"}

Use two hash functions $f,g$ into a table with two arrays $T_1,T_2$ of $m$ slots each (the lecture takes $m=4n$). The invariant is that a key $x$ lies in $T_1[f(x)]$ or in $T_2[g(x)]$.

* $\operatorname{search}(x)$: look at $T_1[f(x)]$ and $T_2[g(x)]$;
* $\operatorname{delete}(x)$: search, then clear the slot;
* $\operatorname{insert}(x)$: put $x$ in $T_1[f(x)]$, bumping any occupant $y$; put $y$ into its slot in the *other* array, bumping again, and so on. If after $6\log n$ bumps the process has not ended, choose new $f,g$ and rebuild the whole table.

The *cuckoo graph* has the slots as vertices and an edge $\{f(x),g(x)\}$ for each stored key $x$; an insertion is a walk in it.

:::

::: {#fig-cuckoo-hashing-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.00,1.2) rectangle +(0.55,0.55); 
\draw[cell frame] (0.55,1.2) rectangle +(0.55,0.55); 
\draw[cell frame] (1.10,1.2) rectangle +(0.55,0.55); \node[lab] at (1.375,1.475) {$y$};
\draw[cell frame] (1.65,1.2) rectangle +(0.55,0.55); 
\draw[cell frame] (2.20,1.2) rectangle +(0.55,0.55); 
\draw[cell frame] (0.00,0) rectangle +(0.55,0.55); \node[lab] at (0.275,0.275) {$z$};
\draw[cell frame] (0.55,0) rectangle +(0.55,0.55); 
\draw[cell frame] (1.10,0) rectangle +(0.55,0.55); 
\draw[cell frame] (1.65,0) rectangle +(0.55,0.55); 
\draw[cell frame] (2.20,0) rectangle +(0.55,0.55); \node[lab] at (2.475,0.275) {$w$};
\node[lab, anchor=east] at (-0.1,1.475) {$T_1$};\node[lab, anchor=east] at (-0.1,0.275) {$T_2$};
\draw[->,hl] (1.375,1.2) -- node[edge label,midway,right] {$y\to g(y)$} (1.1,0.55);
\end{tikzpicture}
\end{center}
```

Inserting a key $x$ with $f(x)=3$ into $T_1$ (slots counted from $1$) bumps the occupant $y$, which moves to its slot $g(y)=3$ in $T_2$; if that were occupied the bump would continue.

:::

::: {#thm-cuckoo-hashing .theorem name="Cuckoo hashing"}

For $f,g$ totally random (or $O(\log n)$-independent), a search and a delete take $2$ probes in the worst case, an insert takes $O(1)$ time in expectation, and the table uses $O(n)$ space; the probability that the key set forces a full rebuild is $O(1/n)$.

:::

::: {.proof}

We prove the expected number of bumps for the walk that never revisits a key (the simplest of three cases).

1. When $x$ is inserted, the slot $T_1[f(x)]$ is occupied only if some stored $y$ has $f(y)=f(x)$ or $g(y)=f(x)$. There are fewer than $n$ keys, so by a union bound over $y$ the probability is at most $2n/m\le\tfrac12$ for $m=4n$.

2. The same bound holds for the next bumped key, with fresh values of the hash functions (the keys on the walk are distinct, and a walk of $O(\log n)$ steps involves $O(\log n)$ independent-looking values). So the probability that at least $t$ keys are bumped is at most $2^{-t}$.

3. The expected number of bumps is $\sum_{t\ge1}t\,2^{-t}=O(1)$, and the chance that $6\log n$ bumps occur is $2^{-6\log n}=O(n^{-6})$.

4. *The other cases.* The walk may enter a cycle of the cuckoo graph: after bumping $x_1,\dots,x_k$ it may bump an earlier key $x_i$, going back along the path and then continuing with new keys. The length is then at most three times that of the corresponding simple walks, so the expectation is again $O(1)$, and the probability of a rebuild is $O(n^{-2})$. Finally the case in which the second walk also hits the path (two cycles) occurs with probability $O(n^{-2})$ by a counting argument over the possible configurations of $t$ keys in the cuckoo graph.

5. A rebuild costs $O(n)$ insertions and occurs with probability $O(n^{-2})$, so it adds $O(1/n)$ expected cost per insertion.

:::

::: {#rmk-cuckoo-hashing-1 .remark name="Space and independence"}

The deletion and search bounds are worst case, and deletion does not need tombstones, which is the practical attraction. With more careful analysis a load factor close to $\tfrac12$ per table is possible, that is $(2+\varepsilon)n$ slots in all. $6$-wise independent families are not sufficient (Cohen–Kane), and simple tabulation hashing leads to a failure probability of $\Theta(n^{-1/3})$.

:::
