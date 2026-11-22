---
title: "Nondeterministic Time and NP"
sources: [mit18404j-14]
requires: [cs/theory/time-complexity]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lecture 14, in our own wording; proofs written out in steps. The verifier definition of NP for programs is @def-np. -->

## Nondeterministic time

::: {#def-ntime .definition name="NTIME and NP"}

A nondeterministic TM (@def-ntm) *runs in time* $t(n)$ if on every input of length $n$ all branches halt within $t(n)$ steps. Then

$$
\mathrm{NTIME}(t(n))=\{A: \text{some 1-tape NTM decides } A \text{ in time } O(t(n))\},\qquad \mathrm{NP}=\bigcup_k\mathrm{NTIME}(n^k).
$$

:::

Like $\mathrm P$, the class $\mathrm{NP}$ is the same for all reasonable nondeterministic models. Simulating nondeterminism deterministically (@thm-ntm-equivalent) visits up to $b^{t(n)}$ nodes, so $\mathrm{NTIME}(t(n))\subseteq\bigcup_c\mathrm{TIME}(c^{t(n)})$; whether exponential time is really needed is the $\mathrm P$ versus $\mathrm{NP}$ question.

::: {#thm-np-verifier .theorem name="NP means polynomial-time verifiable" related="def-np"}

$A\in\mathrm{NP}$ iff there are a polynomial-time deterministic TM $V$ (a *verifier*) and a $k$ such that

$$
A=\{w: V \text{ accepts } \langle w,c\rangle \text{ for some string } c \text{ with } |c|\le |w|^k\}.
$$

The string $c$ is a *certificate* for $w$.

:::

::: {.proof}

1. Let $V$ be such a verifier. An NTM, on input $w$, nondeterministically writes a string $c$ of length at most $|w|^k$ and runs $V$ on $\langle w,c\rangle$. Some branch accepts iff some certificate exists, and every branch takes polynomial time.

2. Conversely, let an NTM $N$ decide $A$ in time $n^k$. Let $V$, on $\langle w,c\rangle$, simulate $N$ on $w$, using the symbols of $c$ to choose the moves at each step, and accept iff this branch accepts. A certificate is the list of choices on an accepting branch, of length at most $n^k$ symbols.

:::

::: {#exm-hampath-composites .example name="Problems in NP"}

1. $\mathit{HAMPATH}=\{\langle G,s,t\rangle: G \text{ has a path from } s \text{ to } t \text{ through every node exactly once}\}$ is in $\mathrm{NP}$: the certificate is the path, which is checked in polynomial time (@def-hamiltonian). No polynomial-time algorithm is known.
2. $\mathit{COMPOSITES}=\{\langle x\rangle: x>1 \text{ is not prime, written in binary}\}$ is in $\mathrm{NP}$: the certificate is a factor $1<y<x$ with $y\mid x$. In fact it is in $\mathrm P$: primality testing was shown to be in $\mathrm P$ in 2002.
3. The complement $\overline{\mathit{HAMPATH}}$ is not known to be in $\mathrm{NP}$: there is no obvious short proof that a graph has *no* Hamiltonian path. The class of complements of $\mathrm{NP}$ languages is $\mathrm{coNP}$.

:::

::: {#fig-nondeterministic-time-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionB] (0,0) ellipse (3.6 and 1.6);
\draw[regionA] (-1.1,-0.1) ellipse (1.6 and 0.9);
\node[lab] at (-1.1,-0.1) {$\mathrm P$};
\node[lab] at (1.9,0.6) {$\mathrm{NP}$};
\node[lab, note] at (1.6,-0.4) {$\mathit{HAMPATH}$};
\node[lab, note] at (-1.1,-0.55) {$\mathit{PATH}$, $\mathit{COMPOSITES}$};
\node[lab, note] at (0,-2.0) {$\mathrm P=\mathrm{NP}$? (open)};
\end{tikzpicture}
\end{center}
```

$\mathrm P\subseteq\mathrm{NP}$: a deterministic machine is a nondeterministic one. Finding a path can be fast while finding a Hamiltonian path seems to need search; checking either is fast.

:::

## Dynamic programming: grammars in P

::: {#thm-acfg-in-p .theorem name="Every context-free language is in P"}

For a fixed CFG $G$ in Chomsky normal form, membership in $L(G)$ is decidable in time $O(n^3)$.

:::

::: {.proof}

1. The decider of @thm-acfg-decidable tries exponentially many derivations. Instead, solve subproblems: for $1\le i\le j\le n$ let $T[i,j]$ be the set of variables that derive the substring $w_i\cdots w_j$.

2. *Length 1:* $A\in T[i,i]$ iff $A\to w_i$ is a rule.

3. *Longer substrings,* in order of length: $A\in T[i,j]$ iff some rule $A\to BC$ and some split $i\le k<j$ have $B\in T[i,k]$ and $C\in T[k+1,j]$.

4. Accept iff $S\in T[1,n]$ (for $w=\varepsilon$, check the rule $S\to\varepsilon$).

5. There are $O(n^2)$ entries, each computed from $O(n)$ splits and a constant number of rules, so the time is $O(n^3)$. By @thm-chomsky-normal-form every CFL has such a grammar.

:::

```{=latex}
\begin{algorithm}
\caption{Dynamic programming for $A_{\mathsf{CFG}}$}
\begin{algorithmic}
\INPUT grammar $G$ in Chomsky normal form, string $w=w_1\cdots w_n$ with $n\ge1$
\FOR{$i=1$ \TO $n$}
    \STATE $T[i,i]\gets\{A: A\to w_i \text{ is a rule}\}$
\ENDFOR
\FOR{$\ell=2$ \TO $n$}
    \FOR{$i=1$ \TO $n-\ell+1$}
        \STATE $j\gets i+\ell-1$; $T[i,j]\gets\emptyset$
        \FOR{$k=i$ \TO $j-1$}
            \FOR{each rule $A\to BC$}
                \IF{$B\in T[i,k]$ and $C\in T[k+1,j]$}
                    \STATE add $A$ to $T[i,j]$
                \ENDIF
            \ENDFOR
        \ENDFOR
    \ENDFOR
\ENDFOR
\RETURN accept iff $S\in T[1,n]$
\end{algorithmic}
\end{algorithm}
```

::: {#exm-cyk .example name="Filling the table"}

The grammar $S\to AT\mid AB$, $T\to SB$, $A\to0$, $B\to1$ generates $\{0^k1^k: k\ge1\}$. On $w=0011$: the diagonal is $A,A,B,B$; among the substrings of length 2 only $01$ gets $S$; of length 3 only $011$ gets $T$ (from $S\,B$); and the whole string gets $S$ (from $A\,T$), so $w$ is accepted.

:::

::: {#fig-nondeterministic-time-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm, y=0.7cm]
\foreach \i/\c in {1/0,2/0,3/1,4/1} \node[lab] at (\i-0.5,0.5) {$\c$};
\foreach \l/\row in {1/{A,A,B,B},2/{,S,},3/{,T},4/{S}} {
  \foreach \v [count=\i] in \row {
    \draw[cell frame] (\i-1+\l/2-0.5,-\l) rectangle (\i+\l/2-0.5,-\l+0.9);
    \node[lab] at (\i-1+\l/2,-\l+0.45) {$\v$};
  }
  \node[lab, note, anchor=east] at (-0.4,-\l+0.45) {length \l};
}
\draw[hl cell] (1.5,-4) rectangle (2.5,-3.1); \node[lab] at (2,-3.55) {$S$};
\end{tikzpicture}
\end{center}
```

The table of @exm-cyk: row $\ell$ holds $T[i,i+\ell-1]$ for each start $i$, centred under its substring. $S$ in the bottom cell means $0011\in L(G)$.

:::
