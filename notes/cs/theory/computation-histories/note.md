---
title: "Computation Histories, Linearly Bounded Automata and PCP"
sources: [mit18404j-10]
requires: [cs/theory/reducibility]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lecture 10, in our own wording; proofs written out in steps. -->

A computation of a TM can be written down as a string. Questions of the form "does some string with a simple local property exist?" can then encode "does $M$ accept $w$?", which proves them undecidable.

::: {#def-computation-history .definition name="Computation history"}

An *accepting computation history* of a TM $M$ on $w$ is a sequence of configurations $C_1,C_2,\dots,C_l$ (@def-configuration) where $C_1$ is the start configuration on $w$, each $C_{i}$ yields $C_{i+1}$, and $C_l$ is accepting. We write it as the string $\#C_1\#C_2\#\cdots\#C_l\#$. $M$ accepts $w$ iff such a history exists.

:::

## Linearly bounded automata

::: {#def-lba .definition name="Linearly bounded automaton"}

A *linearly bounded automaton* (LBA) is a TM whose head never leaves the part of the tape that holds the input.

:::

::: {#prp-alba-decidable .proposition name="Acceptance for LBAs is decidable"}

$A_{\mathsf{LBA}}=\{\langle B,w\rangle: B \text{ is an LBA that accepts } w\}$ is decidable.

:::

::: {.proof}

1. An LBA with $q$ states and $g$ tape symbols has at most $q\,n\,g^n$ configurations on an input of length $n$ (state, head position, tape contents).

2. Simulate $B$ on $w$ for $q\,n\,g^n$ steps. If it has not halted by then, some configuration has repeated, so $B$ is in a loop and will never halt.

3. Accept if $B$ accepted, and reject if it rejected or did not halt in time.

:::

::: {#thm-elba-undecidable .theorem name="Emptiness for LBAs is undecidable"}

$E_{\mathsf{LBA}}=\{\langle B\rangle: B \text{ is an LBA and } L(B)=\emptyset\}$ is undecidable.

:::

::: {.proof}

1. We reduce $A_{\mathsf{TM}}$ to $\overline{E_{\mathsf{LBA}}}$. Given $\langle M,w\rangle$, build an LBA $B_{M,w}$ that accepts exactly the accepting computation histories of $M$ on $w$.

2. $B_{M,w}$ checks its input $\#C_1\#\cdots\#C_l\#$ within the input region: $C_1$ is the start configuration on $w$ (compare symbol by symbol with $w$, which is built into $B$); each $C_{i+1}$ follows from $C_i$ by the rules of $M$ (zigzag between the two, crossing off corresponding symbols; they agree except near the head); and $C_l$ contains $q_{\text{acc}}$.

3. So $L(B_{M,w})\ne\emptyset$ iff $M$ accepts $w$. A decider for $E_{\mathsf{LBA}}$ would therefore decide $A_{\mathsf{TM}}$.

:::

::: {#fig-computation-histories-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.42cm, y=0.5cm]
\foreach \s [count=\i from 0] in {\#,q_0,a,b,\#,x,q_3,b,\#,x,y,q_5,\#,\cdots,\#,x,y,q_{\text{a}},\#} {
  \draw[cell frame] (\i*1.35,0) rectangle (\i*1.35+1.35,1);
  \node[lab, note] at (\i*1.35+0.675,0.5) {$\s$};
}
\draw[decorate, decoration={brace, amplitude=4pt}] (1.35,1.15) -- node[lab, note, above=4pt] {$C_1$} (5.4,1.15);
\draw[decorate, decoration={brace, amplitude=4pt}] (6.75,1.15) -- node[lab, note, above=4pt] {$C_2$} (10.8,1.15);
\draw[decorate, decoration={brace, amplitude=4pt}] (12.15,1.15) -- node[lab, note, above=4pt] {$C_3$} (16.2,1.15);
\draw[decorate, decoration={brace, amplitude=4pt}] (20.25,1.15) -- node[lab, note, above=4pt] {$C_l$ accepts} (24.3,1.15);
\draw[->, faint] (2.0,-0.1) .. controls (4,-1.3) and (6,-1.3) .. (8.1,-0.1);
\draw[->, faint] (8.1,-0.1) .. controls (10,-1.3) and (12,-1.3) .. (13.5,-0.1);
\node[lab, note] at (8,-1.7) {consecutive configurations differ only near the head};
\end{tikzpicture}
\end{center}
```

An accepting computation history (@def-computation-history). An LBA can check it with local comparisons, zigzagging between consecutive configurations.

:::

::: {#thm-allcfg-undecidable .theorem name="Universality for grammars is undecidable"}

$ALL_{\mathsf{CFG}}=\{\langle G\rangle: G \text{ is a CFG and } L(G)=\Sigma^*\}$ is undecidable. Hence $EQ_{\mathsf{CFG}}$ is undecidable too.

:::

::: {.proof}

1. Reduce $A_{\mathsf{TM}}$ to $\overline{ALL_{\mathsf{CFG}}}$. Given $\langle M,w\rangle$, build a PDA $D$ that accepts every string that is *not* an accepting computation history of $M$ on $w$; write the history with every other configuration reversed, $\#C_1\#C_2^{\mathcal R}\#C_3\#C_4^{\mathcal R}\#\cdots$.

2. A string fails to be such a history if it does not start with $C_1$, or does not end with an accepting configuration, or some $C_{i+1}$ does not follow from $C_i$. $D$ guesses which: the first two are regular checks; for the third it guesses $i$, pushes $C_i$, and pops while reading $C_{i+1}^{\mathcal R}$ (or the reverse), finding a mismatch that is not explained by a move of $M$. The reversal makes the stack order match.

3. Convert $D$ to a CFG $G$ (@thm-pda-cfg-equivalence). Then $L(G)=\Sigma^*$ iff no accepting history exists, iff $M$ does not accept $w$.

4. For $EQ_{\mathsf{CFG}}$: $\langle G\rangle\in ALL_{\mathsf{CFG}}$ iff $\langle G,G_{\mathrm{all}}\rangle\in EQ_{\mathsf{CFG}}$, where $G_{\mathrm{all}}$ generates $\Sigma^*$.

:::

## The Post correspondence problem

::: {#def-pcp .definition name="Post correspondence problem"}

A *domino* $\big[\tfrac{t}{b}\big]$ has a string $t$ on top and $b$ at the bottom. Given a finite set $P$ of dominoes, a *match* is a nonempty sequence of dominoes from $P$ (repetitions allowed) whose top strings and bottom strings, concatenated, are equal.

$$
PCP=\{\langle P\rangle: P \text{ has a match}\}.
$$

:::

::: {#exm-pcp .example name="A match"}

For $P=\big\{\big[\tfrac{b}{ca}\big],\big[\tfrac{a}{ab}\big],\big[\tfrac{ca}{a}\big],\big[\tfrac{abc}{c}\big]\big\}$ the sequence $\big[\tfrac{a}{ab}\big]\big[\tfrac{b}{ca}\big]\big[\tfrac{ca}{a}\big]\big[\tfrac{a}{ab}\big]\big[\tfrac{abc}{c}\big]$ reads $abcaaabc$ on both rows. On the other hand $\big\{\big[\tfrac{abc}{ab}\big],\big[\tfrac{ca}{a}\big],\big[\tfrac{acc}{ba}\big]\big\}$ has no match: every top string is longer than its bottom string.

:::

::: {#fig-computation-histories-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.5cm, y=0.5cm]
\foreach \t/\b/\x/\w in {a/ab/0/2,b/ca/2/2,ca/a/4/2,a/ab/6/2,abc/c/8/3} {
  \draw[cell frame] (\x,0) rectangle (\x+\w,2);
  \draw[faint] (\x,1) -- (\x+\w,1);
  \node[lab] at (\x+\w/2,1.5) {$\t$};
  \node[lab] at (\x+\w/2,0.5) {$\b$};
}
\foreach \s [count=\i from 0] in {a,b,c,a,a,a,b,c} {
  \draw[hl cell] (\i*0.9+13,1.0) rectangle (\i*0.9+13.9,2.0); \node[lab] at (\i*0.9+13.45,1.5) {$\s$};
  \draw[hl cell] (\i*0.9+13,0) rectangle (\i*0.9+13.9,1.0); \node[lab] at (\i*0.9+13.45,0.5) {$\s$};
}
\node[lab, note] at (16.6,2.6) {top $=$ bottom};
\end{tikzpicture}
\end{center}
```

The match of @exm-pcp: the five dominoes, and the common string they spell on top and bottom.

:::

::: {#thm-pcp-undecidable .theorem name="PCP is undecidable"}

:::

::: {.proof}

1. Reduce $A_{\mathsf{TM}}$ to $PCP$; we may assume $M$ never moves its head left off the tape. First reduce to the *modified* problem $MPCP$, in which a match must start with a given domino; then remove that restriction.

2. Given $\langle M,w\rangle$, build dominoes whose only matches spell an accepting computation history of $M$ on $w$. The start domino is $\big[\tfrac{\#}{\#q_0w\#}\big]$: the bottom is one configuration ahead of the top.

3. For each move $\delta(q,a)=(r,b,\mathrm R)$ add $\big[\tfrac{qa}{br}\big]$; for each move $\delta(q,a)=(r,b,\mathrm L)$ and each tape symbol $c$ add $\big[\tfrac{cqa}{rcb}\big]$. Add $\big[\tfrac{a}{a}\big]$ for every tape symbol $a$, and $\big[\tfrac{\#}{\#}\big]$ and $\big[\tfrac{\#}{\sqcup\#}\big]$ (to extend the tape).

4. To catch up, the top must copy each configuration while the bottom writes the next one, so a partial match is always a computation history with the bottom one configuration ahead. Add $\big[\tfrac{aq_{\text{acc}}}{q_{\text{acc}}}\big]$ and $\big[\tfrac{q_{\text{acc}}a}{q_{\text{acc}}}\big]$, which let the accept state swallow the tape, and $\big[\tfrac{q_{\text{acc}}\#\#}{\#}\big]$ to finish. A match exists iff $M$ accepts $w$.

5. To force the start domino, put a new symbol $*$ before every symbol of each top string and after every symbol of each bottom string; the start domino also gets a $*$ at the front of its bottom string, so it is the only domino whose two rows begin with the same symbol and only it can begin a match, and a final domino $\big[\tfrac{*\diamond}{\diamond}\big]$ lets the rows end together.

:::
