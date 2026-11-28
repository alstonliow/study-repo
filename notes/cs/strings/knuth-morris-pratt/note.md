---
title: "Knuth–Morris–Pratt Algorithm"
sources: [res-clrs-string-matching]
requires: [cs/strings/string-matching-automaton, cs/data-structures/amortized-analysis]
aliases: [cs/algorithm-topics/knuth-morris-pratt]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-23 from CLRS (3rd edition), Chapter 32, in our own wording; proofs written out in steps. The examples are our own. Split from cs/algorithm-topics/string-matching on 2026-11-25 (one algorithm per note, SPEC §8.6). -->

When a match of $P_q$ fails at the next character, the string-matching automaton (@def-suffix-function) falls back to a shorter prefix that is still a suffix of what was read. KMP computes these fall-backs on the fly from one table that depends only on $P$.

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
