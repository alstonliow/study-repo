---
title: "Finite Automata and Regular Languages"
sources: [mit18404j-1]
requires: [math/discrete/proof/state-machines]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lecture 1, in our own wording; proofs written out in steps. -->

## Strings and languages

::: {#def-string-language .definition name="Alphabet, string, language"}

An *alphabet* $\Sigma$ is a finite nonempty set of *symbols*. A *string* over $\Sigma$ is a finite sequence $w=w_1w_2\cdots w_n$ of symbols, of *length* $|w|=n$; the string of length $0$ is the *empty string* $\varepsilon$. The set of all strings is $\Sigma^*$. A *language* is a set $A\subseteq\Sigma^*$. Writing two strings side by side, $xy$, concatenates them, and $x^k$ is $x$ repeated $k$ times.

:::

## Deterministic finite automata

::: {#def-dfa .definition name="Deterministic finite automaton"}

A *deterministic finite automaton* (DFA) is a 5-tuple

$$
M=(Q,\Sigma,\delta,q_0,F),
$$

where $Q$ is a finite set of *states*, $\Sigma$ an alphabet, $\delta:Q\times\Sigma\to Q$ the *transition function*, $q_0\in Q$ the *start state* and $F\subseteq Q$ the set of *accept states*. On input $w=w_1\cdots w_n$, $M$ passes through the states $r_0=q_0$, $r_i=\delta(r_{i-1},w_i)$ for $i=1,\dots,n$, and *accepts* $w$ if $r_n\in F$. The language of $M$ is

$$
L(M)=\{w\in\Sigma^*: M \text{ accepts } w\},
$$

and we say that $M$ *recognizes* $L(M)$.

:::

A DFA reads its input once, left to right, and remembers only its current state: a finite amount of memory, fixed in advance and independent of the input length.

::: {#exm-dfa-divisible-by-three .example name="Binary numbers divisible by 3"}

Over $\Sigma=\{0,1\}$, read $w$ as a binary number. Appending a bit $b$ turns the value $v$ into $2v+b$, so the remainder modulo $3$ changes from $r$ to $(2r+b)\bmod 3$. The DFA with states $r_0,r_1,r_2$, start and only accept state $r_0$, and $\delta(r_i,b)=r_{(2i+b)\bmod 3}$ recognizes the binary strings whose value is divisible by $3$ (the empty string counts as $0$). On $1001$ (nine) it visits $r_0,r_1,r_2,r_1,r_0$ and accepts.

:::

::: {#fig-finite-automata-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[accept state] (a) at (0,0) {$r_0$};
\node[state] (b) at (2.6,0) {$r_1$};
\node[state] (c) at (5.2,0) {$r_2$};
\draw[start] (a.west) -- ++(-0.7,0);
\draw (a) edge[trans, loop above] node[edge label] {0} (a);
\draw (a) edge[trans, bend left=25] node[edge label] {1} (b);
\draw (b) edge[trans, bend left=25] node[edge label] {1} (a);
\draw (b) edge[trans, bend left=25] node[edge label] {0} (c);
\draw (c) edge[trans, bend left=25] node[edge label] {0} (b);
\draw (c) edge[trans, loop above] node[edge label] {1} (c);
\end{tikzpicture}
\end{center}
```

The DFA of @exm-dfa-divisible-by-three. The arrow from nowhere marks the start state and the double circle the accept state; state $r_i$ means "the bits read so far have value $\equiv i \pmod 3$".

:::

::: {#def-regular-language .definition name="Regular language"}

A language is *regular* if some DFA recognizes it.

:::

## Regular operations and closure

::: {#def-regular-operations .definition name="Regular operations"}

For languages $A,B\subseteq\Sigma^*$:

$$
A\cup B,\qquad A\circ B=AB=\{xy: x\in A,\ y\in B\},\qquad A^*=\{x_1x_2\cdots x_k: k\ge 0,\ x_i\in A\}.
$$

These are *union*, *concatenation* and *star*. Note $\varepsilon\in A^*$ for every $A$ (take $k=0$).

:::

For example, with $A=\{\text{good},\text{bad}\}$ and $B=\{\text{boy},\text{girl}\}$, $AB$ has the four strings goodboy, goodgirl, badboy, badgirl, and $A^*$ is infinite.

::: {#thm-regular-closed-union .theorem name="Closure under union"}

If $A_1$ and $A_2$ are regular, so is $A_1\cup A_2$.

:::

::: {.proof}

1. Let $M_i=(Q_i,\Sigma,\delta_i,q_i,F_i)$ recognize $A_i$ for $i=1,2$. The idea is to run both machines at once, in parallel, keeping one state of each.

2. Define $M=(Q_1\times Q_2,\Sigma,\delta,(q_1,q_2),F)$ with

$$
\delta\big((r_1,r_2),a\big)=\big(\delta_1(r_1,a),\delta_2(r_2,a)\big),\qquad F=(F_1\times Q_2)\cup(Q_1\times F_2).
$$

3. By induction on the number of symbols read, after reading a prefix $u$ of the input $M$ is in state $(r_1,r_2)$ where $r_i$ is the state $M_i$ reaches on $u$.

4. So $M$ ends in $F$ exactly when $M_1$ ends in $F_1$ or $M_2$ ends in $F_2$, that is, $L(M)=A_1\cup A_2$.

:::

::: {#fig-finite-automata-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[accept state] (ae) at (0,2.8) {$a_0e$};
\node[state] (ao) at (4.6,2.8) {$a_0o$};
\node[accept state] (be) at (0,0) {$a_1e$};
\node[accept state] (bo) at (4.6,0) {$a_1o$};
\draw[start] (ae.west) -- ++(-0.7,0);
\draw (ae) edge[trans, bend left=18] node[edge label] {0} (ao);
\draw (ao) edge[trans, bend left=18] node[edge label] {0} (ae);
\draw (be) edge[trans, bend left=18] node[edge label] {1} (bo);
\draw (bo) edge[trans, bend left=18] node[edge label] {1} (be);
\draw (ae) edge[trans, bend left=10] node[edge label, pos=0.18] {1} (bo);
\draw (bo) edge[trans, bend left=10] node[edge label, pos=0.18] {0} (ae);
\draw (ao) edge[trans, bend left=10] node[edge label, pos=0.18] {1} (be);
\draw (be) edge[trans, bend left=10] node[edge label, pos=0.18] {0} (ao);
\node[lab, note, anchor=west] at (5.5,2.8) {last bit not 1};
\node[lab, note, anchor=west] at (5.5,0) {last bit 1};
\node[lab, note] at (0,3.7) {even length};
\node[lab, note] at (4.6,3.7) {odd length};
\end{tikzpicture}
\end{center}
```

The product construction of @thm-regular-closed-union for $A_1$ = strings ending in $1$ (states $a_0,a_1$) and $A_2$ = strings of even length (states $e,o$). A state remembers one state of each machine; it accepts when either component accepts, so only $a_0o$ rejects.

:::

::: {#prp-regular-complement-intersection .proposition name="Complement and intersection"}

If $A$, $A_1$, $A_2$ are regular, so are $\overline A=\Sigma^*-A$ and $A_1\cap A_2$.

:::

::: {.proof}

1. For the complement, keep the DFA of $A$ and swap accept and non-accept states: $F$ becomes $Q-F$. Since the run on each input is unchanged, exactly the rejected strings are now accepted.

2. For the intersection, use the product construction of @thm-regular-closed-union with $F=F_1\times F_2$.

:::

::: {#rmk-finite-automata-1}

Closure under concatenation is harder: a DFA for $A_1A_2$ would have to guess where the first part of the input ends. Nondeterminism (@sec-cs-automata-nondeterministic-finite-automata) makes this guess easy, and closure under concatenation and star follows there.

:::
