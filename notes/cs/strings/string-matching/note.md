---
title: "String Matching"
sources: [res-clrs-string-matching]
requires: []
aliases: [cs/algorithms/string-matching, cs/algorithm-topics/string-matching]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-23 from CLRS (3rd edition), Chapter 32, in our own wording; proofs written out in steps. The examples are our own. On 2026-11-25 Rabin–Karp, the string-matching automaton and KMP moved to their own notes (one algorithm per note, SPEC §8.6); this note is their overview, with the problem and the naive matcher. -->

Searching for a word in a document, a motif in a DNA sequence or a signature in network traffic are all the same problem: find every place where a short string occurs in a long one. The obvious algorithm can take $\Theta(nm)$ time. Three ideas do better: hashing the windows (Rabin–Karp), compiling the pattern into a finite automaton, and the Knuth–Morris–Pratt algorithm, which gets the automaton's linear running time from a table of size $m$.

## The problem

::: {#def-string-matching .definition name="String matching"}

Let $\Sigma$ be a finite alphabet, $T=T[1..n]$ a *text* and $P=P[1..m]$ a *pattern* in $\Sigma^*$, with $m\le n$. A *shift* $s$, $0\le s\le n-m$, is *valid* if $T[s+1..s+m]=P$, that is, if $P$ occurs in $T$ starting at position $s+1$. The *string-matching problem* is to find all valid shifts.

:::

We write $P_q=P[1..q]$ for the prefix of length $q$ (so $P_0=\varepsilon$ and $P_m=P$), and similarly $T_i=T[1..i]$. Write $w\sqsubset x$ if $w$ is a prefix of $x$, and $w\sqsupset x$ if $w$ is a suffix of $x$. So $s$ is valid exactly when $P\sqsupset T_{s+m}$.

::: {#prp-naive-string-matching .proposition name="Naive matching"}

Checking each shift $s=0,1,\dots,n-m$ by comparing $P$ with $T[s+1..s+m]$ character by character finds all valid shifts in $O((n-m+1)m)$ time, and this is $\Theta(nm)$ in the worst case.

:::

::: {.proof}

1. There are $n-m+1$ shifts and each check makes at most $m$ comparisons.

2. For $T=a^n$ and $P=a^m$ with $m=\lfloor n/2\rfloor$, every one of the $n-m+1$ checks makes all $m$ comparisons, which is $\Theta(nm)$.

:::

The naive method wastes what it learns: after matching $P_q$ at shift $s$ and failing at the next character, it forgets that it has already seen $T[s+1..s+q]=P_q$. The faster algorithms use this knowledge.

::: {#fig-string-matching-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.55cm,y=0.55cm]
\foreach \c [count=\i] in {a,b,a,a,b,a,b,a,a,b} {
  \draw[cell frame] (\i-1,0) rectangle (\i,1); \node[lab] at (\i-0.5,0.5) {$\c$};
  \node[lab,tick] at (\i-0.5,1.45) {\i};
}
\node[lab, anchor=east] at (-0.3,0.5) {$T$};
\foreach \c [count=\i] in {a,a,b} {
  \draw[cell frame] (\i+1,-1.6) rectangle (\i+2,-0.6); \node[lab] at (\i+1.5,-1.1) {$\c$};
  \draw[hl cell] (\i+6,-1.6) rectangle (\i+7,-0.6); \node[lab] at (\i+6.5,-1.1) {$\c$};
}
\node[lab, anchor=east] at (1.7,-1.1) {$P$ at $s=2$};
\node[lab, anchor=west] at (10.2,-1.1) {$s=7$};
\draw[hl cell] (2,0) rectangle (5,1);
\node[lab] at (2.5,0.5) {$a$}; \node[lab] at (3.5,0.5) {$a$}; \node[lab] at (4.5,0.5) {$b$};
\draw[hl cell] (7,0) rectangle (10,1);
\node[lab] at (7.5,0.5) {$a$}; \node[lab] at (8.5,0.5) {$a$}; \node[lab] at (9.5,0.5) {$b$};
\end{tikzpicture}
\end{center}
```

The text $T=abaababaab$ and the pattern $P=aab$. The valid shifts are $2$ and $7$: $P$ occurs at positions $3$ and $8$ (highlighted).

:::

## The algorithms

Rabin–Karp (@sec-cs-strings-rabin-karp), the string-matching automaton (@sec-cs-strings-string-matching-automaton) and the Knuth–Morris–Pratt algorithm (@sec-cs-strings-knuth-morris-pratt) have their own notes.

| algorithm | idea | preprocessing | matching time |
|---|---|---|---|
| naive (@prp-naive-string-matching) | check every shift | none | $O((n-m+1)m)$ |
| Rabin–Karp (@prp-rabin-karp) | rolling hash modulo $q$ | $\Theta(m)$ | $O((n-m+1)m)$ worst, $O(n+m)$ expected |
| automaton (@thm-string-matching-automaton) | DFA on prefixes of $P$ | $O(m\lvert\Sigma\rvert)$ | $\Theta(n)$ |
| KMP (@thm-kmp) | prefix function $\pi$ | $\Theta(m)$ | $\Theta(n)$ |

::: {#rmk-string-matching-1 .remark name="Beyond one pattern"}

KMP reads each text character once and never moves back, which suits streams. For many patterns at once, the Aho–Corasick automaton generalises the KMP fall-back links to a trie of patterns. For many searches in one fixed text, it pays to preprocess the text instead, with suffix trees or suffix arrays.

:::
