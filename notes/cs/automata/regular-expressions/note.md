---
title: "Regular Expressions"
sources: [mit18404j-2, mit18404j-3]
requires: [cs/automata/nondeterministic-finite-automata]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lectures 2 and 3, in our own wording; proofs written out in steps. -->

## Regular expressions

::: {#def-regular-expression .definition name="Regular expression"}

The *regular expressions* over $\Sigma$ and their languages are defined inductively:

1. *atomic:* $a$ for $a\in\Sigma$, with $L(a)=\{a\}$; $\varepsilon$, with $L(\varepsilon)=\{\varepsilon\}$; $\emptyset$, with $L(\emptyset)=\emptyset$;
2. *composite:* if $R_1,R_2$ are regular expressions, so are $R_1\cup R_2$, $R_1R_2$ and $R_1^*$, with

$$
L(R_1\cup R_2)=L(R_1)\cup L(R_2),\qquad L(R_1R_2)=L(R_1)L(R_2),\qquad L(R_1^*)=L(R_1)^*.
$$

:::

Star binds tightest, then concatenation, then union. $\Sigma$ abbreviates the union of all symbols.

::: {#exm-regex-examples .example name="Regular expressions over {0,1}"}

1. $(0\cup1)^*=\Sigma^*$, all strings.
2. $\Sigma^*1$, the strings ending in $1$.
3. $\Sigma^*11\Sigma^*$, the strings containing $11$.
4. $(\Sigma\Sigma)^*$, the strings of even length.
5. $0^*10^*$, the strings with exactly one $1$.
6. $1^*\emptyset=\emptyset$ and $\emptyset^*=\{\varepsilon\}$.

:::

## From expressions to automata

::: {#thm-regex-to-nfa .theorem name="Regular expressions give regular languages"}

For every regular expression $R$, the language $L(R)$ is regular.

:::

::: {.proof}

1. Induct on the structure of $R$.

2. *Atomic cases.* $L(a)$ is recognized by an NFA with two states and one $a$-move to the accept state; $L(\varepsilon)$ by a single accepting start state; $L(\emptyset)$ by a single non-accepting state.

3. *Composite cases.* If $L(R_1)$ and $L(R_2)$ are regular, then so are their union, concatenation and star, by @thm-regular-closed-union and @thm-regular-closed-concat-star.

:::

## From automata to expressions

::: {#def-gnfa .definition name="Generalized NFA"}

A *generalized NFA* (GNFA) is an NFA whose transitions are labelled by regular expressions; it may follow a transition labelled $R$ by reading any string of $L(R)$ at once. We assume that the start state has transitions to every other state and none coming in, that there is a single accept state, different from the start state, with transitions coming in from every other state and none going out, and that between any other two states (and from a state to itself) there is exactly one transition. A missing transition is labelled $\emptyset$.

:::

::: {#thm-nfa-to-regex .theorem name="Kleene's theorem"}

If $A$ is regular, then $A=L(R)$ for some regular expression $R$. Together with @thm-regex-to-nfa: a language is regular if and only if it is described by a regular expression.

:::

::: {.proof}

1. Take a DFA for $A$ and turn it into a GNFA: add a new start state with an $\varepsilon$-transition to the old one, and a new accept state with $\varepsilon$-transitions from the old accept states; merge parallel transitions $a,b$ into $a\cup b$ and fill in $\emptyset$ where nothing goes.

2. *Ripping a state.* If the GNFA has more than two states, choose a state $x$ other than the start and accept states and delete it. For each pair of remaining states $q_i$ (not the accept state) and $q_j$ (not the start state), replace the label $R_4$ of $q_i\to q_j$ by

$$
R_1R_2^*R_3\cup R_4,
$$

where $R_1$ labels $q_i\to x$, $R_2$ labels $x\to x$ and $R_3$ labels $x\to q_j$.

3. The new GNFA accepts the same strings. A path through the old GNFA that visits $x$ enters it from some $q_i$, loops at $x$ some number of times, and leaves to some $q_j$; the strings it reads on that stretch are exactly $L(R_1R_2^*R_3)$. Paths that avoid $x$ are unchanged, covered by $R_4$.

4. Repeat until only the start and accept states remain. The single remaining label $R$ is a regular expression with $L(R)=A$.

:::

```{=latex}
\begin{algorithm}
\caption{State ripping}
\begin{algorithmic}
\INPUT GNFA $G$ with start state $s$ and accept state $t$; $R(p,q)$ labels $p\to q$
\OUTPUT a regular expression for $L(G)$
\WHILE{$G$ has a state other than $s$ and $t$}
    \STATE choose such a state $x$
    \FOR{each $p\ne t$ and $q\ne s$, both different from $x$}
        \STATE $R(p,q)\gets R(p,x)\,R(x,x)^*\,R(x,q)\ \cup\ R(p,q)$
    \ENDFOR
    \STATE delete $x$
\ENDWHILE
\RETURN $R(s,t)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-regular-expressions-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[state] (i) at (0,0) {$q_i$};
\node[state] (x) at (2,1.2) {$x$};
\node[state] (j) at (4,0) {$q_j$};
\draw (i) edge[trans] node[edge label] {$R_1$} (x);
\draw (x) edge[trans, loop above] node[edge label] {$R_2$} (x);
\draw (x) edge[trans] node[edge label] {$R_3$} (j);
\draw (i) edge[trans] node[edge label] {$R_4$} (j);
\draw[map, emph] (4.9,0.5) -- (6.1,0.5);
\node[state] (i2) at (7,0) {$q_i$};
\node[state] (j2) at (11,0) {$q_j$};
\draw (i2) edge[trans] node[edge label] {$R_1R_2^*R_3\cup R_4$} (j2);
\end{tikzpicture}
\end{center}
```

Ripping state $x$ (@thm-nfa-to-regex): every path $q_i\to x\to\cdots\to x\to q_j$ is folded into the label of the direct transition.

:::

::: {#exm-rip-states .example name="Converting a two-state DFA"}

Let a DFA over $\{a,b\}$ have start state $1$ with $a$ looping at $1$ and $b$ leading to the accept state $2$, which loops on $a,b$. It accepts the strings containing a $b$. Add a start state $s$ and an accept state $t$:

1. ripping $1$ (with $R_1=\varepsilon$, $R_2=a$, $R_3=b$, $R_4=\emptyset$) labels $s\to2$ by $a^*b$;
2. ripping $2$ (with $R_1=a^*b$, $R_2=a\cup b$, $R_3=\varepsilon$, $R_4=\emptyset$) labels $s\to t$ by $a^*b(a\cup b)^*$.

So the language is $a^*b(a\cup b)^*$: some $a$'s, the first $b$, then anything.

:::

::: {#fig-regular-expressions-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.95cm]
\node[state] (s) at (0,0) {$s$};
\node[state] (1) at (1.8,0) {$1$};
\node[state] (2) at (3.6,0) {$2$};
\node[accept state] (t) at (5.4,0) {$t$};
\draw[start] (s.west) -- ++(-0.5,0);
\draw (s) edge[trans] node[edge label] {$\varepsilon$} (1);
\draw (1) edge[trans, loop above] node[edge label] {$a$} (1);
\draw (1) edge[trans] node[edge label] {$b$} (2);
\draw (2) edge[trans, loop above] node[edge label] {$a\cup b$} (2);
\draw (2) edge[trans] node[edge label] {$\varepsilon$} (t);
\begin{scope}[yshift=-1.9cm]
\node[state] (s) at (0,0) {$s$};
\node[state] (2) at (3.6,0) {$2$};
\node[accept state] (t) at (5.4,0) {$t$};
\draw[start] (s.west) -- ++(-0.5,0);
\draw (s) edge[trans] node[edge label] {$a^*b$} (2);
\draw (2) edge[trans, loop above] node[edge label] {$a\cup b$} (2);
\draw (2) edge[trans] node[edge label] {$\varepsilon$} (t);
\end{scope}
\begin{scope}[yshift=-3.4cm]
\node[state] (s) at (0,0) {$s$};
\node[accept state] (t) at (5.4,0) {$t$};
\draw[start] (s.west) -- ++(-0.5,0);
\draw (s) edge[trans] node[edge label] {$a^*b(a\cup b)^*$} (t);
\end{scope}
\node[lab, note, anchor=west] at (6.2,0) {GNFA};
\node[lab, note, anchor=west] at (6.2,-1.9) {rip $1$};
\node[lab, note, anchor=west] at (6.2,-3.4) {rip $2$};
\end{tikzpicture}
\end{center}
```

The steps of @exm-rip-states; transitions labelled $\emptyset$ are not drawn.

:::
