---
title: "Non-Context-Free Languages"
sources: [mit18404j-5]
requires: [cs/automata/pushdown-automata]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lecture 5, in our own wording; proofs written out in steps. -->

## The pumping lemma for context-free languages

::: {#thm-pumping-lemma-cfl .theorem name="Pumping lemma for context-free languages"}

If $A$ is context-free, there is a number $p$ such that every $s\in A$ with $|s|\ge p$ can be written $s=uvxyz$ with

$$
uv^ixy^iz\in A \text{ for all } i\ge0,\qquad |vy|>0,\qquad |vxy|\le p.
$$

:::

::: {.proof}

1. Let $G$ be a CFG for $A$ with variable set $V$, and let $b\ge2$ bound the length of the right side of every rule. A parse tree of height $h$ (edges on the longest root-to-leaf path) has at most $b^h$ leaves. Put $p=b^{|V|+1}$.

2. Let $s\in A$ with $|s|\ge p$ and take a parse tree $\tau$ of $s$ with the fewest nodes. Since $s$ has at least $b^{|V|+1}$ symbols, $\tau$ has height at least $|V|+1$.

3. A longest root-to-leaf path has at least $|V|+2$ nodes, of which only the leaf is a terminal. Among its lowest $|V|+1$ variables some variable $R$ repeats, by the pigeonhole principle.

4. Let the upper $R$ derive $vxy$ and the lower $R$ derive $x$, so that $s=uvxyz$ (see the figure). Replacing the lower subtree by a copy of the upper one, $i-1$ times, gives parse trees of $uv^ixy^iz$ for $i\ge2$; replacing the upper subtree by the lower gives $uxz$. So $uv^ixy^iz\in A$ for all $i\ge0$.

5. If $v$ and $y$ were both empty, replacing the upper subtree by the lower would give a parse tree of $s$ with fewer nodes, contradicting the choice of $\tau$. So $|vy|>0$.

6. The upper $R$ lies among the lowest $|V|+1$ variables of a longest path, so its subtree has height at most $|V|+1$ and yields $|vxy|\le b^{|V|+1}=p$.

:::

::: {#fig-non-context-free-languages-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (0,3.4) -- (-3.2,0) -- (3.2,0) -- cycle;
\draw[regionB] (0.2,2.2) -- (-1.6,0) -- (2.0,0) -- cycle;
\draw[regionC] (0.3,1.1) -- (-0.5,0) -- (1.1,0) -- cycle;
\node[lab, fill=white] at (0,3.55) {$S$};
\node[lab] at (0.2,2.2) {$R$};
\node[lab] at (0.3,1.1) {$R$};
\draw[gridline] (-3.2,0) -- (3.2,0);
\foreach \x in {-3.2,-1.6,-0.5,1.1,2.0,3.2} \draw (\x,0.08) -- (\x,-0.08);
\node[lab] at (-2.4,-0.3) {$u$};
\node[lab] at (-1.05,-0.3) {$v$};
\node[lab] at (0.3,-0.3) {$x$};
\node[lab] at (1.55,-0.3) {$y$};
\node[lab] at (2.6,-0.3) {$z$};
\begin{scope}[xshift=8cm]
\draw[regionA] (0,4.4) -- (-4,0) -- (4,0) -- cycle;
\draw[regionB] (0.2,3.2) -- (-2.6,0) -- (3,0) -- cycle;
\draw[regionB] (0.1,2.0) -- (-1.5,0) -- (2.0,0) -- cycle;
\draw[regionC] (0.25,0.9) -- (-0.4,0) -- (0.9,0) -- cycle;
\node[lab] at (0.2,3.2) {$R$};
\node[lab] at (0.1,2.0) {$R$};
\node[lab] at (0.25,0.9) {$R$};
\foreach \x in {-4,-2.6,-1.5,-0.4,0.9,2.0,3,4} \draw (\x,0.08) -- (\x,-0.08);
\node[lab] at (-3.3,-0.3) {$u$};
\node[lab] at (-2.05,-0.3) {$v$};
\node[lab] at (-0.95,-0.3) {$v$};
\node[lab] at (0.25,-0.3) {$x$};
\node[lab] at (1.45,-0.3) {$y$};
\node[lab] at (2.5,-0.3) {$y$};
\node[lab] at (3.5,-0.3) {$z$};
\end{scope}
\end{tikzpicture}
\end{center}
```

Proof of @thm-pumping-lemma-cfl. Left: a variable $R$ repeats on a long path, so $s=uvxyz$ with the upper $R$ yielding $vxy$ and the lower $R$ yielding $x$. Right: putting the upper subtree in place of the lower one yields $uv^2xy^2z$.

:::

## Examples

::: {#exm-anbncn-not-cf .example name="$a^kb^kc^k$ is not context-free"}

Let $B=\{a^kb^kc^k: k\ge0\}$, suppose it is context-free with pumping length $p$, and take $s=a^pb^pc^p$. Since $|vxy|\le p$, the string $vxy$ meets at most two of the three blocks, so $v$ and $y$ together contain no $a$ or no $c$. Pumping up to $uv^2xy^2z$ increases the number of some symbols (as $|vy|>0$) but not of all three, or puts symbols out of order if $v$ or $y$ straddles two blocks. Either way $uv^2xy^2z\notin B$.

:::

::: {#exm-ww-not-cf .example name="Doubled strings are not context-free"}

Let $F=\{ww: w\in\{0,1\}^*\}$, suppose it is context-free with pumping length $p$, and take $s=0^p1^p0^p1^p$. (The string $0^p10^p1$, which worked in @exm-ww-nonregular, can be pumped here, with $v$ the last $0$ of the first block, $x=1$, and $y$ the first $0$ of the second block: $uv^ixy^iz=0^{p-1+i}1\,0^{p-1+i}1\in F$.) Let $t=uxz$ be pumped down, $k=|vy|$ with $1\le k\le p$. If $k$ is odd, $|t|$ is odd and $t\notin F$; so let $k$ be even, and let $h=2p-k/2$ be half the length of $t$, so $\tfrac32p\le h<2p$. Since $|vxy|\le p$, the string $vxy$ lies in the first half of $s$, in the second half, or in the middle block $1^p0^p$.

1. *First half.* Then $t=0^a1^b0^p1^p$ with $a+b=2p-k<h$, so position $h$ of $t$ lies in the block $0^p$ and the first half of $t$ ends in $0$, while the second half ends in $1$.
2. *Second half.* Then $t=0^p1^p0^a1^b$, so position $h+1\le 2p$ lies in the first block $1^p$: the second half of $t$ starts with $1$, the first half with $0$.
3. *Middle.* Then $t=0^p1^a0^b1^p$. If $t=ww$, then $w$ starts with $p$ zeros (as $h\ge p$) and ends with $p$ ones, so $h=|w|\ge 2p$, a contradiction.

In every case $t\notin F$, so $F$ is not context-free. (Its complement, by contrast, is context-free.)

:::

## Closure properties

::: {#prp-cfl-closure .proposition name="Closure properties of CFLs"}

The context-free languages are closed under union, concatenation and star, and under intersection with a regular language. They are not closed under intersection or complement.

:::

::: {.proof}

1. If $G_1,G_2$ have start variables $S_1,S_2$ (with disjoint variable sets), new start rules $S\to S_1\mid S_2$, $S\to S_1S_2$ and $S\to SS_1\mid\varepsilon$ give union, concatenation and star.

2. For a PDA $P$ and a DFA $M$, a PDA whose states are pairs runs both at once, moving $M$ whenever $P$ reads a symbol, and accepts when both accept (the product construction of @thm-regular-closed-union with a stack).

3. $\{a^kb^kc^l\}$ and $\{a^lb^kc^k\}$ are context-free, but their intersection is $\{a^kb^kc^k\}$, which is not (@exm-anbncn-not-cf).

4. Since $A_1\cap A_2=\overline{\overline{A_1}\cup\overline{A_2}}$, closure under complement and union would give closure under intersection. So CFLs are not closed under complement.

:::
