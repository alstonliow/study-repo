---
title: "String-Matching Automaton"
sources: [res-clrs-string-matching]
requires: [cs/algorithm-topics/string-matching]
status: draft
---

<!-- Added 2026-11-23 from CLRS (3rd edition), Chapter 32, in our own wording; proofs written out in steps. The examples are our own. Split from cs/algorithm-topics/string-matching on 2026-11-25 (one algorithm per note, SPEC §8.6). -->

The naive matcher (@prp-naive-string-matching) forgets how much of the pattern it has already matched. A finite automaton built from the pattern remembers exactly that, and reads each character of the text once.

::: {#def-suffix-function .definition name="Suffix function, string-matching automaton"}

The *suffix function* of $P$ is $\sigma(x)=\max\{k:P_k\sqsupset x\}$, the length of the longest prefix of $P$ that is a suffix of $x$. The *string-matching automaton* of $P$ is the DFA (@def-dfa) with states $\{0,1,\dots,m\}$, start state $0$, accept state $m$, and transitions
$$
\delta(q,a)=\sigma(P_qa)\qquad(0\le q\le m,\ a\in\Sigma).
$$

:::

The state records how much of $P$ we are in the middle of matching. Run the DFA on $T$, and report the shift $i-m$ whenever it enters state $m$ after reading $T[i]$.

::: {#lem-suffix-function .lemma name="Suffix-function recursion"}

For every string $x$ and character $a$: if $q=\sigma(x)$, then $\sigma(xa)=\sigma(P_qa)$.

:::

::: {.proof}

1. Let $r=\sigma(xa)$. Since $P_q\sqsupset x$, also $P_qa\sqsupset xa$, so any prefix of $P$ that is a suffix of $P_qa$ is a suffix of $xa$. Hence $\sigma(P_qa)\le r$.

2. Conversely $r\le q+1$: if $r\ge1$, then $P_r\sqsupset xa$ means $P_{r-1}\sqsupset x$, so $r-1\le\sigma(x)=q$.

3. So $P_r$ and $P_qa$ are both suffixes of $xa$, and $|P_r|=r\le q+1=|P_qa|$. The shorter of two suffixes of one string is a suffix of the longer, so $P_r\sqsupset P_qa$, and $r\le\sigma(P_qa)$.

:::

::: {#thm-string-matching-automaton .theorem name="The automaton tracks the longest match"}

After reading $T_i$, the string-matching automaton is in state $\sigma(T_i)$. Hence it enters state $m$ exactly after reading $T[s+m]$ for each valid shift $s$, and it finds all valid shifts in $O(n)$ time once $\delta$ is built.

:::

::: {.proof}

1. By induction on $i$. For $i=0$ the state is $0=\sigma(\varepsilon)$.

2. If the state after $T_i$ is $q=\sigma(T_i)$, then after reading $a=T[i+1]$ it is $\delta(q,a)=\sigma(P_qa)=\sigma(T_ia)=\sigma(T_{i+1})$ by @lem-suffix-function.

3. The state is $m$ exactly when $P\sqsupset T_i$, that is, when $i-m$ is a valid shift.

4. Each character costs one table look-up: $O(n)$ time.

:::

Built directly from the definition, $\delta$ costs $O(m^3|\Sigma|)$ time; with the prefix function (@def-prefix-function) it can be built in $O(m|\Sigma|)$.

::: {#fig-string-matching-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.7cm]
\node[state] (q0) at (0,0) {$0$};
\node[state] (q1) at (1,0) {$1$};
\node[state] (q2) at (2,0) {$2$};
\node[state] (q3) at (3,0) {$3$};
\node[accept state] (q4) at (4,0) {$4$};
\draw[start] (q0.west) -- ++(-0.5,0);
\draw[trans] (q0) -- node[lab, above] {$a$} (q1);
\draw[trans] (q1) -- node[lab, above] {$b$} (q2);
\draw[trans] (q2) -- node[lab, above] {$a$} (q3);
\draw[trans] (q3) -- node[lab, above] {$b$} (q4);
\draw[trans] (q0) to[loop above] node[lab, above] {$b$} (q0);
\draw[trans] (q1) to[loop above] node[lab, above] {$a$} (q1);
\draw[trans] (q2) to[bend left=35] node[lab, below] {$b$} (q0);
\draw[trans] (q3) to[bend left=40] node[lab, below] {$a$} (q1);
\draw[trans] (q4) to[bend right=40] node[lab, above] {$a$} (q3);
\draw[trans] (q4) to[bend left=50] node[lab, below] {$b$} (q0);
\end{tikzpicture}
\end{center}
```

The string-matching automaton of $P=abab$ over $\{a,b\}$. Forward edges extend the match. The others fall back to the longest prefix of $P$ that is still a suffix of what was read: for example from state $4$ ($abab$ read), reading $a$ leaves $ababa$, whose longest such suffix is $aba$, state $3$.

:::
