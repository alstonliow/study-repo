---
title: "Nondeterministic Finite Automata"
sources: [mit18404j-2]
requires: [cs/automata/finite-automata]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lecture 2, in our own wording; proofs written out in steps. -->

## Nondeterminism

::: {#def-nfa .definition name="Nondeterministic finite automaton"}

A *nondeterministic finite automaton* (NFA) is a 5-tuple $N=(Q,\Sigma,\delta,q_0,F)$ as in @def-dfa, except that the transition function is

$$
\delta:Q\times\Sigma_\varepsilon\to\mathcal P(Q),\qquad \Sigma_\varepsilon=\Sigma\cup\{\varepsilon\}.
$$

From a state, a symbol may lead to several states, to none, and an *$\varepsilon$-move* changes state without reading input. $N$ *accepts* $w$ if $w$ can be written as $y_1y_2\cdots y_m$ with each $y_i\in\Sigma_\varepsilon$ and there are states $r_0=q_0,r_1,\dots,r_m$ with $r_i\in\delta(r_{i-1},y_i)$ and $r_m\in F$.

:::

Think of $N$ as following all choices at once: it accepts if *some* branch of the computation ends in an accept state after the whole input is read. A branch with no available move dies. Equivalently, $N$ guesses the right choices, and acceptance means a good guess exists.

::: {#exm-nfa-third-from-end .example name="A 1 three places from the end"}

Let $C=\{w\in\{0,1\}^*: \text{the third symbol from the end of } w \text{ is } 1\}$. An NFA with four states recognizes $C$: in $q_1$ it reads anything, and on a $1$ it may *guess* that this is the third symbol from the end and move to $q_2$; then it reads any two symbols to $q_3$ and $q_4$, and accepts in $q_4$. A DFA must remember the last three symbols; the subset construction below gives a DFA with exactly $2^3=8$ reachable states, and no DFA with fewer states recognizes $C$ (two different strings of length 3 differ in some position $i$, and appending $i-1$ symbols separates them).

:::

::: {#fig-nondeterministic-finite-automata-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[state] (1) at (0,0) {$q_1$};
\node[state] (2) at (2.3,0) {$q_2$};
\node[state] (3) at (4.6,0) {$q_3$};
\node[accept state] (4) at (6.9,0) {$q_4$};
\draw[start] (1.west) -- ++(-0.7,0);
\draw (1) edge[trans, loop above] node[edge label] {0,1} (1);
\draw (1) edge[trans] node[edge label] {1} (2);
\draw (2) edge[trans] node[edge label] {0,1} (3);
\draw (3) edge[trans] node[edge label] {0,1} (4);
\node[lab, note] at (2.3,-0.85) {guess: this 1 is third from the end};
\end{tikzpicture}
\end{center}
```

The NFA of @exm-nfa-third-from-end. On a $1$, state $q_1$ has two moves (stay, or go to $q_2$); state $q_4$ has no moves, so a branch that guessed too early dies.

:::

## Equivalence with DFAs

::: {#thm-nfa-dfa-equivalence .theorem name="Subset construction"}

Every NFA has an equivalent DFA. So a language is regular if and only if some NFA recognizes it.

:::

::: {.proof}

1. Let $N=(Q,\Sigma,\delta,q_0,F)$. For $R\subseteq Q$ let $E(R)$ be the set of states reachable from $R$ by zero or more $\varepsilon$-moves.

2. Build the DFA $M=(\mathcal P(Q),\Sigma,\delta',q_0',F')$: a state of $M$ is a *set* of states of $N$, namely all states that some branch of $N$ can be in. Put

$$
q_0'=E(\{q_0\}),\qquad \delta'(R,a)=E\Big(\bigcup_{r\in R}\delta(r,a)\Big),\qquad F'=\{R: R\cap F\ne\emptyset\}.
$$

3. By induction on the length of a prefix $u$ of the input, the state of $M$ after reading $u$ is exactly the set of states that $N$ can be in after reading $u$: true for $u=\varepsilon$ by the choice of $q_0'$, and the step is the definition of $\delta'$.

4. $M$ accepts $w$ iff that set meets $F$ at the end, iff some branch of $N$ accepts $w$. So $L(M)=L(N)$.

5. A DFA is a special NFA, which gives the converse.

:::

```{=latex}
\begin{algorithm}
\caption{Subset construction}
\begin{algorithmic}
\INPUT NFA $N=(Q,\Sigma,\delta,q_0,F)$
\OUTPUT DFA $M$ with $L(M)=L(N)$, built on the reachable subsets only
\STATE $S_0\gets E(\{q_0\})$; mark $S_0$ unprocessed
\WHILE{some subset $R$ is unprocessed}
    \STATE mark $R$ processed
    \FOR{$a\in\Sigma$}
        \STATE $R'\gets E\big(\bigcup_{r\in R}\delta(r,a)\big)$; set $\delta'(R,a)\gets R'$
        \IF{$R'$ is new}
            \STATE mark $R'$ unprocessed
        \ENDIF
    \ENDFOR
\ENDWHILE
\STATE accept states: the subsets $R$ with $R\cap F\ne\emptyset$
\end{algorithmic}
\end{algorithm}
```

If $N$ has $k$ states then $M$ has $2^k$ states; @exm-nfa-third-from-end shows that this blow-up can be needed (there $k+1$ NFA states need $2^k$ DFA states).

::: {#fig-nondeterministic-finite-automata-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.15cm]
\foreach \i/\t in {0/{$\{1\}$},1/{$\{1,2\}$},2/{$\{1,3\}$},3/{$\{1,2,3\}$},4/{$\{1,4\}$},5/{$\{1,2,4\}$},6/{$\{1,3,4\}$},7/{$\{1,2,3,4\}$}}
  {\ifnum\i>3 \node[hl box, note] (s\i) at (\i*1.5,0) {\t};\else \node[box, note] (s\i) at (\i*1.5,0) {\t};\fi}
\node[lab, note] at (0,-0.75) {$000$};
\node[lab, note] at (1.5,-0.75) {$001$};
\node[lab, note] at (3,-0.75) {$010$};
\node[lab, note] at (4.5,-0.75) {$011$};
\node[lab, note] at (6,-0.75) {$100$};
\node[lab, note] at (7.5,-0.75) {$101$};
\node[lab, note] at (9,-0.75) {$110$};
\node[lab, note] at (10.5,-0.75) {$111$};
\node[lab, note, anchor=east] at (-0.7,-0.75) {last three bits:};
\end{tikzpicture}
\end{center}
```

The eight reachable states of the subset DFA for @exm-nfa-third-from-end (state $q_i$ written $i$). Each set records which of the last three bits were $1$; the four sets containing $q_4$ are accepting (shaded).

:::

## Closure under concatenation and star

::: {#thm-regular-closed-concat-star .theorem name="Closure under concatenation and star"}

If $A_1$ and $A_2$ are regular, so are $A_1A_2$ and $A_1^*$.

:::

::: {.proof}

1. Let NFAs $N_1$ and $N_2$ recognize $A_1$ and $A_2$ (@thm-nfa-dfa-equivalence).

2. *Concatenation.* Put $N_1$ and $N_2$ side by side. The start state is that of $N_1$, the accept states are those of $N_2$, and from every accept state of $N_1$ add an $\varepsilon$-move to the start state of $N_2$. A branch accepts $w$ exactly when it reads some $x\in A_1$ in $N_1$, jumps, and reads the rest $y\in A_2$ in $N_2$; the NFA guesses where $x$ ends.

3. *Star.* Add a new start state $s$, which is also an accept state (so that $\varepsilon$ is accepted), with an $\varepsilon$-move to the old start state of $N_1$, and add $\varepsilon$-moves from every accept state of $N_1$ back to the old start state. A branch accepts iff it reads $x_1,x_2,\dots,x_k\in A_1$ one after another, guessing each boundary.

4. In both cases the new NFA recognizes the required language, so the language is regular by @thm-nfa-dfa-equivalence.

:::

Adding $s$ matters: making the old start state accepting instead could accept strings that are not in $A_1^*$, if $N_1$ can return to its start state in the middle of a word.

::: {#fig-nondeterministic-finite-automata-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (-0.4,-0.9) rectangle (2.6,0.9);
\node[lab, note] at (1.1,1.15) {$N_1$};
\node[state] (a) at (0,0) {};
\node[accept state] (f1) at (2.1,0.45) {};
\node[accept state] (f2) at (2.1,-0.45) {};
\draw[regionB] (3.8,-0.9) rectangle (6.8,0.9);
\node[lab, note] at (5.3,1.15) {$N_2$};
\node[state] (b) at (4.3,0) {};
\node[accept state] (g) at (6.3,0) {};
\draw[start] (a.west) -- ++(-0.6,0);
\draw[trans] (f1) -- node[edge label] {$\varepsilon$} (b);
\draw[trans] (f2) -- node[edge label] {$\varepsilon$} (b);
\node[lab, note] at (3.2,-1.4) {$A_1A_2$: accept states of $N_1$ become ordinary};
\begin{scope}[xshift=9cm]
\draw[regionA] (-0.4,-0.9) rectangle (2.6,0.9);
\node[lab, note] at (1.1,1.15) {$N_1$};
\node[state] (c) at (0,0) {};
\node[accept state] (h1) at (2.1,0.45) {};
\node[accept state] (h2) at (2.1,-0.45) {};
\node[accept state] (s) at (-1.6,0) {$s$};
\draw[start] (s.west) -- ++(-0.6,0);
\draw[trans] (s) -- node[edge label] {$\varepsilon$} (c);
\draw (h1) edge[trans, bend right=50] node[edge label] {$\varepsilon$} (c);
\draw (h2) edge[trans, bend left=50] node[edge label] {$\varepsilon$} (c);
\node[lab, note] at (0.6,-1.4) {$A_1^*$: new start state $s$ accepts $\varepsilon$};
\end{scope}
\end{tikzpicture}
\end{center}
```

The constructions in the proof of @thm-regular-closed-concat-star.

:::
