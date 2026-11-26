---
title: "XOR Basis"
sources: []
requires: []
status: draft
---

<!-- Added 2026-11-26 for the CSES bitwise problems, in our own wording. TODO: add a source. -->

Numbers below $2^b$ are vectors over the field with two elements, and XOR is vector addition. Subset-XOR questions become linear algebra over $\mathbb F_2$, and a small set of numbers, a *basis*, represents all subsets.

::: {#def-xor-basis .definition name="XOR basis"}

For a multiset $S$ of non-negative integers below $2^b$, a *basis* $B\subseteq \operatorname{span}(S)$ is a set of numbers with distinct highest set bits such that every XOR of a subset of $S$ is an XOR of a subset of $B$ (and conversely). The *rank* $r=|B|$.

:::

::: {#thm-xor-basis .theorem name="Building and using a XOR basis"}

Keep an array $\operatorname{bas}[0..b-1]$, initially $0$. To insert $x$: for bit $j$ from $b-1$ down to $0$ with bit $j$ of $x$ set, if $\operatorname{bas}[j]=0$ then set $\operatorname{bas}[j]\gets x$ and stop, otherwise $x\gets x\oplus\operatorname{bas}[j]$. This takes $O(b)$ time per number and ends with a basis, and:

1. the number of distinct subset-XOR values is $2^r$ (all with equal multiplicity $2^{|S|-r}$);
2. the maximum subset XOR is found by starting with $m=0$ and for $j$ from $b-1$ down to $0$ replacing $m$ by $m\oplus\operatorname{bas}[j]$ whenever that increases $m$;
3. after reducing the basis (clearing each leading bit from the other elements), the $k$-th smallest subset XOR ($k$ counted from $0$) is the XOR of the basis elements selected by the binary digits of $k$, the lowest digit selecting the element with the lowest leading bit.

:::

::: {.proof}

1. *Invariant.* Every inserted number is an XOR of stored basis elements and the other way round: reducing $x$ by $\operatorname{bas}[j]$ keeps the span, and a stored element is an XOR of inserted numbers. Distinct leading bits are kept by construction.

2. *Independence and count.* A nonempty XOR of basis elements has the highest bit of its element with the highest leading bit, so it is non-zero. Hence the $2^r$ XORs of subsets of $B$ are distinct. The map from subsets of $S$ to their XORs is linear, with image of size $2^r$ and so with fibres of equal size $2^{|S|-r}$.

3. *Maximum.* Going from the high bit down, a value in the span with top bit set at $j$ can be reached only using $\operatorname{bas}[j]$ and elements below, so greedily making each bit $1$ if possible is optimal (a larger bit outweighs all lower ones).

4. *Order statistics.* In a reduced basis, the leading bit of $\operatorname{bas}[j]$ appears in no other element, so the subset XOR with chosen set $T$ has the leading bits of $T$ set exactly. Comparing two XORs, the largest differing leading bit decides, which is the order of the binary numbers $k$ formed by the chosen elements.

:::

::: {#exm-xor-basis-1 .example name="Numbers 5, 3, 6"}

Insert $5=101_2$: $\operatorname{bas}[2]=5$. Insert $3=011_2$: bit $1$ is set and $\operatorname{bas}[1]=0$, so $\operatorname{bas}[1]=3$. Insert $6=110_2$: bit $2$ set, so $x=6\oplus5=3$; bit $1$ set, so $x=3\oplus3=0$, which adds nothing. The rank is $2$, the subset XORs are $\{0,3,5,6\}$, and the maximum is $5\oplus 3=6$.

:::

::: {#fig-xor-basis-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \r/\row/\n in {0/{1,0,1}/5,1/{0,1,1}/3,2/{1,1,0}/6} {
  \foreach \v [count=\c from 0] in \row {
    \ifnum\v=1 \draw[hl cell] (0.6*\c,-0.7*\r) rectangle +(0.6,0.6);
    \else \draw[cell frame] (0.6*\c,-0.7*\r) rectangle +(0.6,0.6);\fi
    \node[lab] at (0.6*\c+0.3,-0.7*\r+0.3) {$\v$};
  }
  \node[lab,anchor=west] at (2,-0.7*\r+0.3) {$\n$};
}
\node[lab,tick,anchor=west] at (3,0.3) {$\operatorname{bas}[2]$};
\node[lab,tick,anchor=west] at (3,-0.4) {$\operatorname{bas}[1]$};
\node[lab,tick,anchor=west] at (3,-1.1) {$6=5\oplus3$, dependent};
\end{tikzpicture}
\end{center}
```

@exm-xor-basis-1: the inserted numbers as bit vectors; $5$ and $3$ become basis elements, $6=5\oplus3$ reduces to $0$.

:::
