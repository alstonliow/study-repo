---
title: "Suffix Tries"
sources: [cs97si-10]
requires: [cs/data-structures/tries, cs/algorithm-topics/string-matching]
status: draft
---

<!-- Added 2026-11-26 from Stanford CS 97SI (Winter 2011-12), Lecture 10 (suffix trie), in our own wording; proofs written out in steps. The example and figure are our own; counts checked by computation. -->

Every substring of a text $T$ is a prefix of a suffix of $T$. So the trie (@def-trie) of all suffixes of $T$ has one node per distinct substring, and many questions about substrings become walks in one tree.

::: {#def-suffix-trie .definition name="Suffix trie"}

The *suffix trie* of a string $T$ of length $n$ is the trie of its $n$ suffixes $T[i..n-1]$, $0\le i<n$. Each node $v$ spells a substring $s(v)$; a node is marked when $s(v)$ is a suffix. It is built by inserting the suffixes one by one (or, adding the characters $T[0],T[1],\dots$ in turn, by extending every current suffix by the new character).

:::

```{=latex}
\begin{algorithm}
\caption{Building a suffix trie}
\begin{algorithmic}
\INPUT A string $T$ of length $n$
\OUTPUT Its suffix trie
\STATE create the root
\FOR{$i=0$ \TO $n-1$}
    \STATE $v\gets$ root
    \FOR{$j=i$ \TO $n-1$}
        \IF{$v$ has no child labelled $T[j]$}
            \STATE create it
        \ENDIF
        \STATE $v\gets$ the child of $v$ labelled $T[j]$
    \ENDFOR
    \STATE mark $v$ \COMMENT{$s(v)=T[i..n-1]$ is a suffix}
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

::: {#prp-suffix-trie .proposition name="What a suffix trie answers"}

The non-root nodes of the suffix trie of $T$ are in bijection with the distinct non-empty substrings of $T$. The trie has $O(n^2)$ nodes, is built in $O(n^2)$ time, and then decides whether a pattern $P$ occurs in $T$ in $O(|P|)$ time.

:::

::: {.proof}

1. *Nodes are substrings.* A node spells a prefix of an inserted suffix, which is a substring. Every substring $T[i..j]$ is the prefix of length $j-i+1$ of the suffix starting at $i$, so the insertion of that suffix creates or passes a node spelling it. Two nodes of a trie spell different strings.

2. *Size and time.* A string of length $n$ has at most $n(n+1)/2$ non-empty substrings, and inserting the suffix of length $n-i$ costs $O(n-i)$ steps, $O(n^2)$ in all.

3. *Search.* $P$ occurs in $T$ exactly when it is a substring, that is, when the walk from the root along the characters of $P$ never falls off the trie; the walk takes $|P|$ steps.

:::

::: {#exm-suffix-tries-1 .example name="The suffix trie of abab"}

The suffixes are $abab$, $bab$, $ab$, $b$. Their trie has $8$ nodes: the root, $a$, $ab$, $aba$, $abab$, $b$, $ba$, $bab$, so $abab$ has $7$ distinct non-empty substrings. The marked nodes are $abab$, $bab$, $ab$ and $b$; searching $ba$ succeeds and $bb$ falls off after $b$.

:::

::: {#fig-suffix-tries-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[level distance=1cm, sibling distance=2cm, every node/.style={small vertex}, edge from parent/.style={draw}]
\node (r) {}
  child {node (a) {}
    child {node[fill=accentLight] (ab) {}
      child {node (aba) {}
        child {node[fill=accentLight] (abab) {} edge from parent node[edge label] {$b$}}
        edge from parent node[edge label] {$a$}}
      edge from parent node[edge label] {$b$}}
    edge from parent node[edge label] {$a$}}
  child {node[fill=accentLight] (b) {}
    child {node (ba) {}
      child {node[fill=accentLight] (bab) {} edge from parent node[edge label] {$b$}}
      edge from parent node[edge label] {$a$}}
    edge from parent node[edge label] {$b$}};
\draw[hl] (r) -- (b) -- (ba);
\end{tikzpicture}
\end{center}
```

The suffix trie of $abab$ (@exm-suffix-tries-1). Marked nodes, which end a suffix, are shaded; the highlighted walk finds the pattern $ba$.

:::

::: {#rmk-suffix-tries-1 .remark name="Suffix trees and suffix arrays"}

A text like $a^nb^n$ has $\Theta(n^2)$ distinct substrings, so a suffix trie can be quadratic. Compressing every chain of nodes with one child into one edge labelled by an interval of $T$ gives the *suffix tree*, with $O(n)$ nodes, which Ukkonen's algorithm builds in $O(n)$ time. In contests the simpler suffix array (@sec-cs-algorithm-topics-suffix-arrays) usually replaces both.

:::
