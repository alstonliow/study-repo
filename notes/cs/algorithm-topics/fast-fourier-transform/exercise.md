::: {.problem #prob-mit6046s15-2-q1 origin="external" source="mit6046s15-2-q1"}
**Pattern Matching**

Suppose you are given a source string $S[0..n-1]$ of length $n$, consisting of symbols $a$ and $b$. Suppose further that you are given a pattern string $P[0..m-1]$ of length $m\ll n$, consisting of symbols $a$, $b$, and $*$, representing a pattern to be found in string $S$. The symbol $*$ is a "wild card" symbol, which matches a single symbol, either $a$ or $b$. The other symbols must match exactly.

The problem is to output a sorted list $M$ of valid "match positions", which are positions $j$ in $S$ such that pattern $P$ matches the substring $S[j..j+|P|-1]$. For example, if $S=a\,b\,a\,b\,b\,a\,b$ and $P=a\,b\,*$, then the output $M$ should be $[0,2]$.

(a) Describe a straightforward, naïve algorithm to solve the problem. Your algorithm should run in time $O(nm)$.

(b) Give an algorithm to solve the problem by reducing it to the problem of polynomial multiplication. Specifically, describe how to convert strings $S$ and $P$ into polynomials such that the product of the polynomials allows you to determine the answer $M$. Give examples to illustrate your polynomial representation of the inputs and your way of determining outputs from the product, based on the example $S$ and $P$ strings given above.

(c) Suppose you combine your solution to Part (b) with an FFT algorithm for polynomial multiplication, as presented in Lecture 3. What is the time complexity of the resulting solution to the string matching problem?

(d) Now consider the same problem but with a larger symbol alphabet. Specifically, suppose you are given a representation of a DNA strand as a string $D[0..n-1]$ of length $n$, consisting of symbols $A$, $C$, $G$, and $T$; and you are given a pattern string $P[0..m-1]$ of length $m\ll n$, consisting of symbols $A$, $C$, $G$, $T$, and $*$.

The problem is, again, to output a sorted list $M$ of valid "match positions", which are positions $j$ in $D$ such that pattern $P$ matches the substring $D[j..j+|P|-1]$. For example, if $D=A\,C\,G\,A\,C\,C\,A\,T$ and $P=A\,C\,*\,A$, then the output $M$ should be $[0,3]$.

Based on your solutions to Parts (b) and (c), give an efficient algorithm for this setting. Illustrate your algorithm on the example above.
:::

::: {.problem #prob-mit18335-38-q1 origin="external" source="mit18335-38-q1"}
Prove that equation (2) really is the inverse of equation (1). Hint: subsitute (1) into (2), interchange the order of the two sums, and sum the geometric series.

*Note (these notes):* Equations (1) and (2) are the DFT and its inverse for $N$ complex numbers: (1) $y_k=\sum_{n=0}^{N-1}x_ne^{-\frac{2\pi i}{N}nk}$ and (2) $x_n=\frac1N\sum_{k=0}^{N-1}y_ke^{+\frac{2\pi i}{N}nk}$. This is @prp-inverse-dft with $\omega_N=e^{-2\pi i/N}$.
:::
