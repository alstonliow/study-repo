---
title: "Rabin–Karp Algorithm"
sources: [res-clrs-string-matching]
requires: [cs/strings/string-matching, math/discrete/number-theory/modular-arithmetic]
aliases: [cs/algorithm-topics/rabin-karp]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-23 from CLRS (3rd edition), Chapter 32, in our own wording; proofs written out in steps. The examples are our own. Split from cs/algorithm-topics/string-matching on 2026-11-25 (one algorithm per note, SPEC §8.6). -->

The Rabin–Karp algorithm solves string matching (@def-string-matching) by hashing: it compares a fingerprint of each window of the text with the fingerprint of the pattern, and checks characters only where the fingerprints agree.

Take $\Sigma=\{0,1,\dots,d-1\}$, so a string of length $m$ is a number with $m$ digits in base $d$. Let $p$ be the value of $P$ and $t_s$ the value of the window $T[s+1..s+m]$. Then $s$ is valid exactly when $t_s=p$. These numbers are too large to compare in $O(1)$ time, so we compare them modulo a prime $q$ instead.

::: {#prp-rolling-hash .proposition name="Rolling hash"}

Let $h=d^{m-1}\bmod q$. Then
$$
t_{s+1}\equiv d\bigl(t_s-T[s+1]\,h\bigr)+T[s+m+1]\pmod q.
$$
So $p\bmod q$ and all of $t_0\bmod q,\dots,t_{n-m}\bmod q$ can be computed in $O(n+m)$ arithmetic operations on numbers below $dq$.

:::

::: {.proof}

1. $t_s=\sum_{j=1}^{m}T[s+j]\,d^{m-j}$. Removing the leading digit gives $t_s-T[s+1]d^{m-1}$; multiplying by $d$ shifts every digit up one place, and adding $T[s+m+1]$ appends the new last digit. The result is $t_{s+1}$.

2. Reduce everything modulo $q$ (@sec-math-discrete-number-theory-modular-arithmetic), using $d^{m-1}\equiv h$.

3. $p\bmod q$ and $t_0\bmod q$ take $O(m)$ steps by Horner's rule; each later window takes $O(1)$.

:::

A window with $t_s\equiv p\pmod q$ is a *hit*. A hit may be *spurious* ($t_s\ne p$), so every hit is checked character by character.

::: {#prp-rabin-karp .proposition name="Rabin–Karp running time"}

The Rabin–Karp algorithm finds all valid shifts. Its worst-case time is $\Theta((n-m+1)m)$. If $P$ has $v$ valid shifts and each invalid window is a hit with probability at most $c/q$ (as when the residues behave like random values modulo $q$), its expected time is
$$
O\bigl(n+m(v+1)+mn/q\bigr),
$$
which is $O(n+m)$ when $v=O(1)$ and $q\ge m$.

:::

::: {.proof}

1. *Correctness.* Every valid shift is a hit, and every hit is checked, so the algorithm reports exactly the valid shifts.

2. *Worst case.* If every window is a hit (for $T=a^n$, $P=a^m$, all of them are valid), each costs $m$ comparisons.

3. *Expected time.* Computing all residues takes $O(n+m)$ (@prp-rolling-hash). The checks cost $O(m)$ for each valid shift and $O(m)$ for each spurious hit. There are at most $n$ invalid windows, each spurious with probability at most $c/q$, so the expected number of spurious hits is $O(n/q)$.

4. With $q\ge m$, the term $mn/q$ is $O(n)$.

:::

::: {#fig-string-matching-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.6cm,y=0.6cm]
\foreach \c [count=\i] in {8,3,1,7,4,2,1,7} {
  \draw[cell frame] (\i-1,0) rectangle (\i,1); \node[lab] at (\i-0.5,0.5) {$\c$};
}
\draw[hl cell] (2,0) rectangle (5,1);
\node[lab] at (2.5,0.5) {$1$}; \node[lab] at (3.5,0.5) {$7$}; \node[lab] at (4.5,0.5) {$4$};
\draw[hl, dashed] (1,-0.08) rectangle (4,1.08);
\node[lab, anchor=east] at (-0.3,0.5) {$T$};
\foreach \v [count=\i] in {6,9,9,5,3,8} {
  \node[lab] at (\i-0.5,-0.9) {$\v$};
}
\node[lab, anchor=east] at (-0.3,-0.9) {$t_s\bmod 11$};
\node[lab, anchor=west] at (9.0,0.5) {$P=174$, $\;p\bmod11=9$};
\node[lab,tick] at (1.2,-1.75) {spurious};
\node[lab,tick] at (2.8,-1.75) {valid};
\draw[->, faint] (1.5,-1.5) -- (1.5,-1.15);
\draw[->, faint] (2.5,-1.5) -- (2.5,-1.15);
\end{tikzpicture}
\end{center}
```

Rabin–Karp with $d=10$, $q=11$ on the text $83174217$ and the pattern $174$. Each residue is written under the first digit of its window. Two windows hit: $317$ (dashed) is spurious, since $317\equiv9$ but $317\ne174$, and $174$ (highlighted) is valid. The roll from $831$ to $317$ is $10(6-8\cdot1)+7=-13\equiv9\pmod{11}$, with $h=100\bmod11=1$.

:::
