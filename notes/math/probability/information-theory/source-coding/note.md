---
title: "Source Coding and Huffman Codes"
sources: [eecs126-7, eecs126d-10]
requires: [math/probability/information-theory/entropy, math/probability/discrete/concentration-inequalities]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley EECS126 (Fall 2021), note "Information Theory Introduction", Section 2, and Discussion 10, in our own wording; proofs written out in steps. -->

A source emits i.i.d. symbols $X_1,X_2,\dots$ with PMF $p$. How many bits per symbol are needed to store them? The answer is the entropy $H(X)$ (@def-entropy).

::: {#def-typical-set .definition name="Typical set"}

For $\varepsilon>0$ and $n\ge1$, the *typical set* $A_\varepsilon^{(n)}$ is the set of sequences $(x_1,\dots,x_n)$ with
$$2^{-n(H(X)+\varepsilon)}\le p(x_1)\cdots p(x_n)\le2^{-n(H(X)-\varepsilon)}.$$

:::

::: {#fig-source-coding-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0,0) rectangle (6,2.4);
\node[tick, anchor=north west] at (0,2.4) {all $2^n$ sequences};
\draw[regionA] (3.6,0.4) rectangle (5.4,1.6);
\node[tick, align=center] at (4.5,1.0) {typical set\\$\approx2^{nH}$ sequences\\probability $\approx1$};
\end{tikzpicture}
\end{center}
```

For a biased binary source ($H<1$) the typical set is a vanishing fraction of all sequences, yet it carries almost all the probability; indexing only it needs about $nH$ bits

:::

::: {#thm-aep .theorem name="Asymptotic equipartition property"}

1. $\Pr\bigl((X_1,\dots,X_n)\in A_\varepsilon^{(n)}\bigr)\to1$ as $n\to\infty$.
2. $|A_\varepsilon^{(n)}|\le2^{n(H(X)+\varepsilon)}$.

:::

::: {.proof}

1. Membership means $\bigl|\frac1n\sum_i\log_2\frac1{p(X_i)}-H(X)\bigr|\le\varepsilon$. The terms $\log_2\frac{1}{p(X_i)}$ are i.i.d. with mean $H(X)$, so the weak law of large numbers (@thm-law-of-large-numbers) gives probability tending to $1$.

2. Each typical sequence has probability at least $2^{-n(H(X)+\varepsilon)}$ and the probabilities sum to at most $1$.

:::

::: {#thm-source-coding .theorem name="Source coding theorem"}

For every $\varepsilon>0$ and large $n$, $n$ symbols can be encoded into $n(H(X)+\varepsilon)$ bits and decoded correctly with probability tending to $1$. Conversely, no scheme using $n(H(X)-\varepsilon)$ bits has error probability tending to $0$.

:::

::: {.proof}

1. *Achievability.* Index the typical sequences with $\lceil n(H(X)+\varepsilon)\rceil$ bits (possible by @thm-aep part 2) and send the index; an atypical sequence is a decoding error, whose probability tends to $0$ by part 1.

2. *Converse (sketch).* $n(H(X)-\varepsilon)$ bits can describe at most $2^{n(H(X)-\varepsilon)}$ sequences. Typical sequences each have probability at most $2^{-n(H(X)-\varepsilon/2)}$ (use $\varepsilon/2$ in the typical set), so the described typical sequences carry probability at most $2^{-n\varepsilon/2}\to0$, and atypical ones carry vanishing probability too.

:::

For a single symbol at a time, *prefix codes* (no codeword is a prefix of another, so a stream decodes unambiguously) satisfy $L\ge H(X)$ for the mean codeword length $L$, and Huffman's algorithm finds the best one.

::: {#def-huffman-code .definition name="Huffman code"}

Given a PMF $p$ on a finite alphabet, Huffman's algorithm builds a binary tree: repeatedly merge the two nodes of smallest probability into a new node whose probability is their sum, until one node remains. The codeword of a symbol is the sequence of left/right ($0/1$) choices on the path from the root to its leaf.

:::

```{=latex}
\begin{algorithm}
\caption{Huffman code}
\begin{algorithmic}
\INPUT Symbols $x$ with probabilities $p(x)$
\OUTPUT A binary prefix code
\STATE Make a leaf for every symbol; put all leaves in a min-priority queue keyed by probability
\WHILE{the queue holds more than one node}
    \STATE $a\gets$ extract-min; $b\gets$ extract-min
    \STATE make a node $c$ with children $a$ (bit $0$) and $b$ (bit $1$), $p(c)=p(a)+p(b)$; insert $c$
\ENDWHILE
\STATE Read each codeword from the root down to the leaf
\end{algorithmic}
\end{algorithm}
```

::: {#thm-huffman-optimal .theorem name="Huffman codes are optimal"}

A Huffman code has the smallest mean codeword length among all binary prefix codes for $p$, and that length satisfies
$$H(X)\le L<H(X)+1.$$

:::

::: {.proof}

1. *Bounds.* Lengths $\ell(x)=\lceil\log_2\frac1{p(x)}\rceil$ satisfy Kraft's inequality $\sum_x2^{-\ell(x)}\le1$, so a prefix code with these lengths exists, and its mean length is below $H(X)+1$. Conversely for any prefix code, with $q(x)=2^{-\ell(x)}/\sum_y2^{-\ell(y)}$, Gibbs' inequality (@thm-gibbs-inequality) gives $L-H(X)=D(p\,\|\,q)-\log_2\sum_y2^{-\ell(y)}\ge0$.

2. *Exchange.* Some optimal code has the two least likely symbols $a,b$ as sibling leaves at maximal depth: in an optimal tree every internal node has two children, the deepest level has two siblings, and swapping $a,b$ into them does not increase $L$.

3. *Induction.* Merging $a$ and $b$ into one symbol of probability $p(a)+p(b)$ lowers the mean length of such a code by exactly $p(a)+p(b)$, for every code with $a,b$ siblings. So an optimal code for the merged alphabet (by induction, the Huffman code) expands to an optimal code for the original one, and that expansion is what Huffman's algorithm builds.

:::

::: {#exm-huffman-five .example name="Five symbols"}

For probabilities $0.4,0.2,0.2,0.1,0.1$, Huffman merges $0.1+0.1=0.2$, then two of the three $0.2$'s into $0.4$, then $0.2+0.4=0.6$, then $0.4+0.6$. One resulting set of lengths is $2,2,2,3,3$, with mean $2.2$ bits, against $H(X)\approx2.122$ bits.

:::

::: {#fig-source-coding-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (b) at (0.000,-1.900) {$b$};
\node[small vertex] (n1) at (0.750,-0.950) {$0.4$};
\node[small vertex] (c) at (1.500,-1.900) {$c$};
\node[small vertex] (n3) at (2.250,0.000) {$1.0$};
\node[small vertex] (d) at (3.000,-2.850) {$d$};
\node[small vertex] (n0) at (3.750,-1.900) {$0.2$};
\node[small vertex] (e) at (4.500,-2.850) {$e$};
\node[small vertex] (n2) at (5.250,-0.950) {$0.6$};
\node[small vertex] (a) at (6.000,-1.900) {$a$};
\draw (n0)--(d);
\draw (n0)--(e);
\draw (n1)--(b);
\draw (n1)--(c);
\draw (n2)--(n0);
\draw (n2)--(a);
\draw (n3)--(n1);
\draw (n3)--(n2);
\node[lab,tick] at (3.225,-2.325) {0};
\node[lab,tick] at (4.275,-2.325) {1};
\node[lab,tick] at (0.225,-1.375) {0};
\node[lab,tick] at (1.275,-1.375) {1};
\node[lab,tick] at (4.350,-1.375) {0};
\node[lab,tick] at (5.775,-1.375) {1};
\node[lab,tick] at (1.350,-0.425) {0};
\node[lab,tick] at (3.900,-0.425) {1};
\node[lab,tick,anchor=north] at (6.000,-2.150) {$0.4$, \texttt{11}};
\node[lab,tick,anchor=north] at (0.000,-2.150) {$0.2$, \texttt{00}};
\node[lab,tick,anchor=north] at (1.500,-2.150) {$0.2$, \texttt{01}};
\node[lab,tick,anchor=north] at (3.000,-3.100) {$0.1$, \texttt{100}};
\node[lab,tick,anchor=north] at (4.500,-3.100) {$0.1$, \texttt{101}};
\end{tikzpicture}
\end{center}
```

The Huffman tree for probabilities $0.4,0.2,0.2,0.1,0.1$ (symbols $a$–$e$). Internal nodes show merged probabilities; each leaf shows its probability and codeword. The two $0.1$ symbols are merged first and end deepest, with $3$-bit codewords.

:::
