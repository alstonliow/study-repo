---
title: "Suffix Arrays and the LCP Array"
sources: [cs97si-10, vladu2005-sa]
requires: [cs/algorithm-topics/suffix-tries, cs/sorting/radix-sort]
status: draft
---

<!-- Added 2026-11-26 from Stanford CS 97SI (Winter 2011-12), Lecture 10, and the suffix-array article it links (Vladu and Negruşeri 2005), in our own wording; proofs written out in steps. Kasai's LCP algorithm, the example and the figure are our own additions; values checked by computation. -->

A suffix array lists the suffixes of a text in sorted order, by their starting positions. It takes $n$ integers, where a suffix trie can take $\Theta(n^2)$ nodes, and with its LCP array it answers most of the same questions.

::: {#def-suffix-array .definition name="Suffix array, LCP array"}

For a string $T$ of length $n$, the *suffix array* is the permutation $\mathrm{SA}$ of $0,\dots,n-1$ with $T[\mathrm{SA}[0]..]<T[\mathrm{SA}[1]..]<\dots$ in lexicographic order. The *LCP array* has $\mathrm{LCP}[k]$ = the length of the longest common prefix of the suffixes at $\mathrm{SA}[k-1]$ and $\mathrm{SA}[k]$, for $1\le k<n$.

:::

::: {#def-prefix-doubling .definition name="Prefix doubling"}

Let $r_k(i)$ be the rank of the length-$k$ prefix $T[i..i+k-1]$ among all such prefixes (a prefix running past the end is padded with a symbol smaller than every character, and equal prefixes get equal ranks). Start with $r_1(i)$ = rank of the character $T[i]$. Given $r_k$, sort the positions by the pair $\bigl(r_k(i),r_k(i+k)\bigr)$ (with $r_k(i+k)=0$ when $i+k\ge n$) and let $r_{2k}(i)$ be the rank of that pair. Stop when all ranks differ; the sorted order is $\mathrm{SA}$.

:::

```{=latex}
\begin{algorithm}
\caption{Suffix array by prefix doubling}
\begin{algorithmic}
\INPUT A string $T$ of length $n$
\OUTPUT Its suffix array $\mathrm{SA}$
\STATE $r(i)\gets$ rank of $T[i]$ among the characters of $T$ (from $1$), for all $i$; $k\gets1$
\REPEAT
    \STATE $\mathrm{SA}\gets$ positions sorted by $\bigl(r(i),\ r(i+k)\bigr)$ \COMMENT{$r(i+k)=0$ if $i+k\ge n$}
    \STATE $r'(\mathrm{SA}[0])\gets1$
    \FOR{$j=1$ \TO $n-1$}
        \STATE $r'(\mathrm{SA}[j])\gets r'(\mathrm{SA}[j-1])+[\text{pair of }\mathrm{SA}[j]\ne\text{pair of }\mathrm{SA}[j-1]]$
    \ENDFOR
    \STATE $r\gets r'$; $k\gets2k$
\UNTIL{$r(\mathrm{SA}[n-1])=n$}
\RETURN $\mathrm{SA}$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-prefix-doubling .theorem name="Prefix doubling"}

Prefix doubling returns the suffix array after at most $\lceil\log_2n\rceil+1$ rounds. With a comparison sort each round costs $O(n\log n)$, in total $O(n\log^2n)$; with a two-pass radix sort on the pairs (@sec-cs-sorting-radix-sort) each round costs $O(n)$, in total $O(n\log n)$.

:::

::: {.proof}

1. *Ranks stay correct.* The length-$2k$ prefix at $i$ is the length-$k$ prefix at $i$ followed by the length-$k$ prefix at $i+k$. Comparing two such strings lexicographically compares the first halves and, if equal, the second halves, which is exactly the order of the pairs $(r_k(i),r_k(i+k))$. Padding by the smallest symbol makes a shorter string precede its extensions, as rank $0$ does. So $r_{2k}$ ranks the length-$2k$ prefixes, by induction from $r_1$.

2. *Termination.* Once $k\ge n$, the length-$k$ prefix at $i$ is the whole suffix at $i$, padded; distinct suffixes have distinct lengths, so they are distinct strings and all ranks differ. The loop stops after at most $\lceil\log_2n\rceil+1$ rounds, possibly earlier.

3. *Order.* When all ranks differ, sorting by them sorts the suffixes, since two suffixes differ within their first $k$ characters (or one is a prefix of the other, which the padding orders first).

4. *Cost.* Each round is one sort of $n$ pairs and one pass; ranks are at most $n$, so radix sort applies.

:::

::: {#thm-kasai .theorem name="LCP array in linear time (Kasai et al.)"}

Let $\mathrm{rank}$ be the inverse of $\mathrm{SA}$. Process the positions $i=0,1,\dots,n-1$ in text order, keeping a counter $h$: if $\mathrm{rank}(i)>0$, let $j=\mathrm{SA}[\mathrm{rank}(i)-1]$, increase $h$ while $T[i+h]=T[j+h]$, set $\mathrm{LCP}[\mathrm{rank}(i)]=h$, and then decrease $h$ by one if $h>0$ (if $\mathrm{rank}(i)=0$, set $h=0$). This computes the LCP array in $O(n)$ time.

:::

::: {.proof}

1. *Key fact.* If the suffix at $i$ shares $h>0$ characters with its predecessor in sorted order (starting at $j$), then the suffix at $i+1$ shares at least $h-1$ characters with *its* predecessor. Indeed, deleting the first (common) character of both, the suffix at $j+1$ precedes the suffix at $i+1$ and agrees with it on $h-1$ characters; every suffix sorted between them agrees with the suffix at $i+1$ on at least those $h-1$ characters too, in particular its immediate predecessor.

2. *Correctness.* So starting the comparison at $h-1$ skips only characters known to match, and the loop extends $h$ to the exact common length.

3. *Time.* $h$ never exceeds $n$, it decreases at most $n$ times by one, and every successful comparison increases it, so there are at most $2n$ successful comparisons and $n$ failing ones.

:::

::: {#exm-suffix-arrays-1 .example name="banana"}

For $T=banana$ the character ranks are $a=1$, $b=2$, $n=3$, so $r_1=(2,1,3,1,3,1)$. Round $k=1$ sorts the pairs $(2,1),(1,3),(3,1),(1,3),(3,1),(1,0)$ and gives $r_2=(3,2,4,2,4,1)$; round $k=2$ sorts $(3,4),(2,2),(4,4),(2,1),(4,0),(1,0)$ and gives $r_4=(4,3,6,2,5,1)$, all distinct. Hence

$$
\mathrm{SA}=(5,3,1,0,4,2),\qquad \mathrm{LCP}=(\,\cdot\,,1,3,0,0,2),
$$

for the sorted suffixes $a$, $ana$, $anana$, $banana$, $na$, $nana$.

:::

::: {#fig-suffix-arrays-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=0.62cm]
\node[lab,tick] at (0,1) {$k$}; \node[lab,tick] at (1,1) {$\mathrm{SA}[k]$}; \node[lab,tick] at (2.2,1) {LCP};
\node[lab,tick,anchor=west] at (3,1) {suffix};
\node[lab,tick] at (0,-0) {$0$}; \node[lab] at (1,-0) {$5$};  \node[lab,anchor=west] at (3,-0) {\texttt{a}};
\node[lab,tick] at (0,-1) {$1$}; \node[lab] at (1,-1) {$3$}; \node[lab] at (2.2,-1) {$1$}; \node[lab,anchor=west] at (3,-1) {\texttt{\textcolor{accent}{\textbf{a}}na}};
\node[lab,tick] at (0,-2) {$2$}; \node[lab] at (1,-2) {$1$}; \node[lab] at (2.2,-2) {$3$}; \node[lab,anchor=west] at (3,-2) {\texttt{\textcolor{accent}{\textbf{ana}}na}};
\node[lab,tick] at (0,-3) {$3$}; \node[lab] at (1,-3) {$0$}; \node[lab] at (2.2,-3) {$0$}; \node[lab,anchor=west] at (3,-3) {\texttt{banana}};
\node[lab,tick] at (0,-4) {$4$}; \node[lab] at (1,-4) {$4$}; \node[lab] at (2.2,-4) {$0$}; \node[lab,anchor=west] at (3,-4) {\texttt{na}};
\node[lab,tick] at (0,-5) {$5$}; \node[lab] at (1,-5) {$2$}; \node[lab] at (2.2,-5) {$2$}; \node[lab,anchor=west] at (3,-5) {\texttt{\textcolor{accent}{\textbf{na}}na}};
\end{tikzpicture}
\end{center}
```

The suffix array of $banana$ (@exm-suffix-arrays-1). Each LCP value is the length of the common prefix with the row above (bold); for example $ana$ and $anana$ share $ana$.

:::

::: {#rmk-suffix-arrays-1 .remark name="Uses"}

All occurrences of a pattern $P$ form one block of $\mathrm{SA}$, found by two binary searches in $O(|P|\log n)$. The number of distinct substrings is $\binom{n+1}{2}-\sum_k\mathrm{LCP}[k]$ ($21-6=15$ for $banana$). The longest repeated substring is a maximum of LCP; for two strings, the longest common substring is found from the suffix array of $A\#B$ with a separator $\#$, as the largest LCP between neighbours that come from different strings. The LCP of any two suffixes is a range minimum of the LCP array.

:::
