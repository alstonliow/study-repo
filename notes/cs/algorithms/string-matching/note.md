---
title: "String Matching"
sources: [res-clrs-string-matching]
requires: [math/discrete/number-theory/modular-arithmetic]
status: draft
---

<!-- Added 2026-11-23 from CLRS (3rd edition), Chapter 32, in our own wording; proofs written out in steps. The examples are our own. -->

Searching for a word in a document, a motif in a DNA sequence or a signature in network traffic are all the same problem: find every place where a short string occurs in a long one. The obvious algorithm can take $\Theta(nm)$ time. Three ideas do better: hashing the windows (Rabin–Karp), compiling the pattern into a finite automaton, and the Knuth–Morris–Pratt algorithm, which gets the automaton's linear running time from a table of size $m$.

## The problem

::: {#def-string-matching .definition name="String matching"}

Let $\Sigma$ be a finite alphabet, $T=T[1..n]$ a *text* and $P=P[1..m]$ a *pattern* in $\Sigma^*$, with $m\le n$. A *shift* $s$, $0\le s\le n-m$, is *valid* if $T[s+1..s+m]=P$, that is, if $P$ occurs in $T$ starting at position $s+1$. The *string-matching problem* is to find all valid shifts.

:::

We write $P_q=P[1..q]$ for the prefix of length $q$ (so $P_0=\varepsilon$ and $P_m=P$), and similarly $T_i=T[1..i]$. Write $w\sqsubset x$ if $w$ is a prefix of $x$, and $w\sqsupset x$ if $w$ is a suffix of $x$. So $s$ is valid exactly when $P\sqsupset T_{s+m}$.

::: {#prp-naive-string-matching .proposition name="Naive matching"}

Checking each shift $s=0,1,\dots,n-m$ by comparing $P$ with $T[s+1..s+m]$ character by character finds all valid shifts in $O((n-m+1)m)$ time, and this is $\Theta(nm)$ in the worst case.

:::

::: {.proof}

1. There are $n-m+1$ shifts and each check makes at most $m$ comparisons.

2. For $T=a^n$ and $P=a^m$ with $m=\lfloor n/2\rfloor$, every one of the $n-m+1$ checks makes all $m$ comparisons, which is $\Theta(nm)$.

:::

The naive method wastes what it learns: after matching $P_q$ at shift $s$ and failing at the next character, it forgets that it has already seen $T[s+1..s+q]=P_q$. The faster algorithms below use this knowledge.

::: {#fig-string-matching-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.55cm,y=0.55cm]
\foreach \c [count=\i] in {a,b,a,a,b,a,b,a,a,b} {
  \draw[cell frame] (\i-1,0) rectangle (\i,1); \node[lab] at (\i-0.5,0.5) {$\c$};
  \node[lab,tick] at (\i-0.5,1.45) {\i};
}
\node[lab, anchor=east] at (-0.3,0.5) {$T$};
\foreach \c [count=\i] in {a,a,b} {
  \draw[cell frame] (\i+1,-1.6) rectangle (\i+2,-0.6); \node[lab] at (\i+1.5,-1.1) {$\c$};
  \draw[hl cell] (\i+6,-1.6) rectangle (\i+7,-0.6); \node[lab] at (\i+6.5,-1.1) {$\c$};
}
\node[lab, anchor=east] at (1.7,-1.1) {$P$ at $s=2$};
\node[lab, anchor=west] at (10.2,-1.1) {$s=7$};
\draw[hl cell] (2,0) rectangle (5,1);
\node[lab] at (2.5,0.5) {$a$}; \node[lab] at (3.5,0.5) {$a$}; \node[lab] at (4.5,0.5) {$b$};
\draw[hl cell] (7,0) rectangle (10,1);
\node[lab] at (7.5,0.5) {$a$}; \node[lab] at (8.5,0.5) {$a$}; \node[lab] at (9.5,0.5) {$b$};
\end{tikzpicture}
\end{center}
```

The text $T=abaababaab$ and the pattern $P=aab$. The valid shifts are $2$ and $7$: $P$ occurs at positions $3$ and $8$ (highlighted).

:::

## Rabin–Karp: hashing the windows

Take $\Sigma=\{0,1,\dots,d-1\}$, so a string of length $m$ is a number with $m$ digits in base $d$. Let $p$ be the value of $P$ and $t_s$ the value of the window $T[s+1..s+m]$. Then $s$ is valid exactly when $t_s=p$. These numbers are too large to compare in $O(1)$ time, so we compare them modulo a prime $q$ instead.

::: {#prp-rolling-hash .proposition name="Rolling hash"}

Let $h=d^{m-1}\bmod q$. Then
$$
t_{s+1}\equiv d\bigl(t_s-T[s+1]\,h\bigr)+T[s+m+1]\pmod q.
$$
So $p\bmod q$ and all of $t_0\bmod q,\dots,t_{n-m}\bmod q$ can be computed in $O(n+m)$ arithmetic operations on numbers below $dq$.

:::

::: {.proof}

1. $t_s=\sum_{j=1}^{m}T[s+j]\,d^{m-j}$. Removing the leading digit gives $t_s-T[s+1]d^{m-1}$; multiplying by $d$ shifts every digit up one place, and adding $T[s+m+1]$ appends the new last digit. The result is $t_{s+1}$.

2. Reduce everything modulo $q$ (@sec-math-discrete-number-theory-modular-arithmetic), using $d^{m-1}\equiv h$.

3. $p\bmod q$ and $t_0\bmod q$ take $O(m)$ steps by Horner's rule; each later window takes $O(1)$.

:::

A window with $t_s\equiv p\pmod q$ is a *hit*. A hit may be *spurious* ($t_s\ne p$), so every hit is checked character by character.

::: {#prp-rabin-karp .proposition name="Rabin–Karp running time"}

The Rabin–Karp algorithm finds all valid shifts. Its worst-case time is $\Theta((n-m+1)m)$. If $P$ has $v$ valid shifts and each invalid window is a hit with probability at most $c/q$ (as when the residues behave like random values modulo $q$), its expected time is
$$
O\bigl(n+m(v+1)+mn/q\bigr),
$$
which is $O(n+m)$ when $v=O(1)$ and $q\ge m$.

:::

::: {.proof}

1. *Correctness.* Every valid shift is a hit, and every hit is checked, so the algorithm reports exactly the valid shifts.

2. *Worst case.* If every window is a hit (for $T=a^n$, $P=a^m$, all of them are valid), each costs $m$ comparisons.

3. *Expected time.* Computing all residues takes $O(n+m)$ (@prp-rolling-hash). The checks cost $O(m)$ for each valid shift and $O(m)$ for each spurious hit. There are at most $n$ invalid windows, each spurious with probability at most $c/q$, so the expected number of spurious hits is $O(n/q)$.

4. With $q\ge m$, the term $mn/q$ is $O(n)$.

:::

::: {#fig-string-matching-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.6cm,y=0.6cm]
\foreach \c [count=\i] in {8,3,1,7,4,2,1,7} {
  \draw[cell frame] (\i-1,0) rectangle (\i,1); \node[lab] at (\i-0.5,0.5) {$\c$};
}
\draw[hl cell] (2,0) rectangle (5,1);
\node[lab] at (2.5,0.5) {$1$}; \node[lab] at (3.5,0.5) {$7$}; \node[lab] at (4.5,0.5) {$4$};
\draw[hl, dashed] (1,-0.08) rectangle (4,1.08);
\node[lab, anchor=east] at (-0.3,0.5) {$T$};
\foreach \v [count=\i] in {6,9,9,5,3,8} {
  \node[lab] at (\i-0.5,-0.9) {$\v$};
}
\node[lab, anchor=east] at (-0.3,-0.9) {$t_s\bmod 11$};
\node[lab, anchor=west] at (9.0,0.5) {$P=174$, $\;p\bmod11=9$};
\node[lab,tick] at (1.2,-1.75) {spurious};
\node[lab,tick] at (2.8,-1.75) {valid};
\draw[->, faint] (1.5,-1.5) -- (1.5,-1.15);
\draw[->, faint] (2.5,-1.5) -- (2.5,-1.15);
\end{tikzpicture}
\end{center}
```

Rabin–Karp with $d=10$, $q=11$ on the text $83174217$ and the pattern $174$. Each residue is written under the first digit of its window. Two windows hit: $317$ (dashed) is spurious, since $317\equiv9$ but $317\ne174$, and $174$ (highlighted) is valid. The roll from $831$ to $317$ is $10(6-8\cdot1)+7=-13\equiv9\pmod{11}$, with $h=100\bmod11=1$.

:::

## Matching with a finite automaton

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

Built directly from the definition, $\delta$ costs $O(m^3|\Sigma|)$ time; with the prefix function below it can be built in $O(m|\Sigma|)$.

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

## The Knuth–Morris–Pratt algorithm

When a match of $P_q$ fails at the next character, the automaton falls back to a shorter prefix that is still a suffix of what was read. KMP computes these fall-backs on the fly from one table that depends only on $P$.

::: {#def-prefix-function .definition name="Prefix function"}

The *prefix function* of $P$ is $\pi:\{1,\dots,m\}\to\{0,\dots,m-1\}$,
$$
\pi(q)=\max\{k<q:P_k\sqsupset P_q\},
$$
the length of the longest proper prefix of $P_q$ that is also a suffix of $P_q$ (its longest *border*).

:::

::: {#lem-prefix-function-iteration .lemma name="All borders by iteration"}

For $1\le q\le m$, the lengths $k<q$ with $P_k\sqsupset P_q$ are exactly $\pi(q),\pi(\pi(q)),\pi^{(3)}(q),\dots$, down to $0$.

:::

::: {.proof}

1. *Each iterate is a border.* $P_{\pi(q)}\sqsupset P_q$ by definition, and "is a suffix of" is transitive, so by induction every $P_{\pi^{(i)}(q)}$ is a suffix of $P_q$.

2. *No border is skipped.* Suppose some $k$ with $P_k\sqsupset P_q$ is not an iterate, and take the largest such $k$. Let $j$ be the smallest iterate greater than $k$ (it exists, since $q$ itself is one, counting $\pi^{(0)}(q)=q$).

3. $P_k$ and $P_j$ are both suffixes of $P_q$ and $k<j$, so $P_k\sqsupset P_j$. Hence $k\le\pi(j)$. But $\pi(j)$ is the next iterate after $j$, so $\pi(j)\le k$ by the choice of $j$. So $k=\pi(j)$ is an iterate, a contradiction.

:::

```{=latex}
\begin{algorithm}
\caption{KMP matcher}
\begin{algorithmic}
\INPUT text $T[1..n]$, pattern $P[1..m]$, prefix function $\pi$
\STATE $q\gets0$ \COMMENT{number of characters matched}
\FOR{$i=1$ \TO $n$}
    \WHILE{$q>0$ and $P[q+1]\ne T[i]$}
        \STATE $q\gets\pi(q)$ \COMMENT{fall back to the next shorter border}
    \ENDWHILE
    \IF{$P[q+1]=T[i]$}
        \STATE $q\gets q+1$
    \ENDIF
    \IF{$q=m$}
        \STATE report the valid shift $i-m$; $q\gets\pi(m)$
    \ENDIF
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

The prefix function is computed by the same loop, matching $P$ against itself: for $q=2,\dots,m$, start from $k=\pi(q-1)$, fall back with $k\gets\pi(k)$ while $k>0$ and $P[k+1]\ne P[q]$, then set $\pi(q)=k+1$ if $P[k+1]=P[q]$ and $\pi(q)=k$ otherwise (with $\pi(1)=0$).

::: {#thm-kmp .theorem name="Knuth–Morris–Pratt"}

The KMP matcher finds all valid shifts in $O(n)$ time, and the prefix function is computed in $O(m)$ time. So string matching takes $O(n+m)$ time in total, independent of $|\Sigma|$.

:::

::: {.proof}

1. *Correctness.* By induction on $i$, after processing $T[i]$ the value $q$ equals $\sigma(T_i)$, as in the automaton. Suppose $q=\sigma(T_{i-1})$ before the step. By @lem-suffix-function, $\sigma(T_i)=\sigma(P_qa)$ with $a=T[i]$; this is $k+1$ for the largest border length $k$ of $P_q$ (including $k=q$) with $P[k+1]=a$, or $0$ if there is none. By @lem-prefix-function-iteration the `while` loop tries exactly these $k$ in decreasing order, so it stops at the right one. After a full match, $q\gets\pi(m)$ is the largest border, which is what the next step needs. (The same argument shows the $\pi$ computation is correct.)

2. *Time.* Use $q$ as a potential (@def-potential-method). Each iteration of the `for` loop raises $q$ by at most $1$, and each step of the `while` loop lowers it by at least $1$, since $\pi(q)<q$. As $q\ge0$, the total number of `while` steps is at most the total increase, which is at most $n$. So the matcher takes $O(n)$ time, and the same argument with $k$ gives $O(m)$ for $\pi$.

:::

::: {#fig-string-matching-4}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.55cm,y=0.55cm]
\node[lab, anchor=east] at (-0.3,0.5) {$P[q]$};
\node[lab, anchor=east] at (-0.3,-0.5) {$\pi(q)$};
\node[lab, anchor=east] at (-0.3,1.45) {$q$};
\foreach \c/\v [count=\i] in {a/0,b/0,a/1,a/1,b/2,a/3,b/2} {
  \draw[cell frame] (\i-1,0) rectangle (\i,1); \node[lab] at (\i-0.5,0.5) {$\c$};
  \draw[cell frame] (\i-1,-1) rectangle (\i,0); \node[lab] at (\i-0.5,-0.5) {$\v$};
  \node[lab,tick] at (\i-0.5,1.45) {\i};
}
\begin{scope}[xshift=6.5cm]
\foreach \c [count=\i] in {a,b,a,a,b,a,a,b,a,b} {
  \draw[cell frame] (\i-1,0) rectangle (\i,1); \node[lab] at (\i-0.5,0.5) {$\c$};
}
\node[lab, anchor=east] at (-0.2,0.5) {$T$};
\foreach \c [count=\i] in {a,b,a,a,b,a} {
  \draw[cell frame] (\i-1,-1.3) rectangle (\i,-0.3); \node[lab] at (\i-0.5,-0.8) {$\c$};
}
\draw[hl cell] (6,-1.3) rectangle (7,-0.3); \node[lab] at (6.5,-0.8) {$b$};
\foreach \c [count=\i] in {a,b,a,a,b,a,b} {
  \draw[cell frame] (\i+2,-2.6) rectangle (\i+3,-1.6); \node[lab] at (\i+2.5,-2.1) {$\c$};
}
\draw[hl cell] (3,-2.6) rectangle (6,-1.6);
\node[lab] at (3.5,-2.1) {$a$}; \node[lab] at (4.5,-2.1) {$b$}; \node[lab] at (5.5,-2.1) {$a$};
\node[lab,tick, anchor=west] at (7.2,-0.8) {mismatch after $q=6$};
\node[lab,tick, anchor=west] at (10.2,-2.1) {$q\gets\pi(6)=3$};
\end{scope}
\end{tikzpicture}
\end{center}
```

Left: the prefix function of $P=abaabab$. For example $\pi(6)=3$, because $aba$ is both a prefix and a suffix of $abaaba$, and no longer proper prefix is. Right: matching against $T=abaabaabab$, the first $6$ characters match but $T[7]=a\ne P[7]=b$. KMP slides $P$ so that its border $aba$ (highlighted) lies under the last three text characters read, and continues with $q=3$, without moving back in $T$. From there it matches $abab$ and reports the valid shift $3$.

:::

::: {#rmk-string-matching-1 .remark name="Beyond one pattern"}

KMP reads each text character once and never moves back, which suits streams. For many patterns at once, the Aho–Corasick automaton generalises the KMP fall-back links to a trie of patterns. For many searches in one fixed text, it pays to preprocess the text instead, with suffix trees or suffix arrays.

:::
