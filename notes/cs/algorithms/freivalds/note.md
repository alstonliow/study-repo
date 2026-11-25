---
title: "Freivalds' Check of a Matrix Product"
sources: [mit6046-6, mit6046r-4]
requires: [cs/algorithms/randomized-algorithms]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 6 and Recitation 4, in our own wording; proofs written out in steps. Split from cs/algorithms/randomized-algorithms on 2026-11-25 (one algorithm per note, SPEC §8.6). -->

A Monte Carlo algorithm (@sec-cs-algorithms-randomized-algorithms) that checks a matrix product faster than computing it.

::: {#thm-freivalds .theorem name="Freivalds' check"}

Given $n\times n$ matrices $A,B,C$ (over the integers, or any field), choose a vector $r\in\{0,1\}^n$ uniformly at random and answer "yes" if $A(Br)=Cr$. This takes $O(n^2)$ time. If $AB=C$ the answer is always "yes"; if $AB\ne C$ it is "yes" with probability at most $\frac12$.

:::

::: {.proof}

1. Computing $Br$, then $A(Br)$, then $Cr$ takes three matrix–vector products, $O(n^2)$.

2. If $AB=C$ then $A(Br)=(AB)r=Cr$.

3. Otherwise $D=AB-C\ne0$; pick an entry $d_{ij}\ne0$. The answer is "yes" only if $(Dr)_i=\sum_kd_{ik}r_k=0$, that is $r_j=-\frac1{d_{ij}}\sum_{k\ne j}d_{ik}r_k$.

4. Fix the other coordinates of $r$. At most one of the two values of $r_j$ satisfies this, so the probability of "yes" is at most $\frac12$.

:::

```{=latex}
\begin{algorithm}
\caption{Freivalds' check}
\begin{algorithmic}
\INPUT $n\times n$ matrices $A,B,C$; a number $k$ of trials
\OUTPUT "yes" if probably $AB=C$, "no" if certainly $AB\ne C$
\FOR{$j=1$ to $k$}
    \STATE choose $r\in\{0,1\}^n$ uniformly at random
    \IF{$A(Br)\ne Cr$}
        \RETURN "no"
    \ENDIF
\ENDFOR
\RETURN "yes"
\end{algorithmic}
\end{algorithm}
```

::: {#fig-randomized-algorithms-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$19$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$22$};
\draw[cell frame] (0.000,-0.550) rectangle (0.550,0.000);
\node[lab] at (0.275,-0.275) {$43$};
\draw[hl cell] (0.550,-0.550) rectangle (1.100,0.000);
\node[lab] at (0.825,-0.275) {$51$};
\node[lab,tick] at (0.55,0.85) {$C$ ($AB$ has $50$ here)};
\node[lab,tick] at (2.60,0.75) {$r$};
\node[lab,tick] at (3.90,0.75) {$A(Br)$};
\node[lab,tick] at (5.20,0.75) {$Cr$};
\node[lab,tick] at (6.50,0.75) {answer};
\draw[faint] (2.1,0.55) -- (7.1,0.55);
\node[lab,tick] at (2.60,0.30) {$(0,0)$};
\node[lab,tick] at (3.90,0.30) {$(0,0)$};
\node[lab,tick] at (5.20,0.30) {$(0,0)$};
\node[lab,tick] at (6.50,0.30) {yes};
\node[lab,tick] at (2.60,-0.12) {$(0,1)$};
\node[lab,tick] at (3.90,-0.12) {$(22,50)$};
\node[lab,tick] at (5.20,-0.12) {$(22,51)$};
\node[lab,tick] at (6.50,-0.12) {\textbf{no}};
\node[lab,tick] at (2.60,-0.54) {$(1,0)$};
\node[lab,tick] at (3.90,-0.54) {$(19,43)$};
\node[lab,tick] at (5.20,-0.54) {$(19,43)$};
\node[lab,tick] at (6.50,-0.54) {yes};
\node[lab,tick] at (2.60,-0.96) {$(1,1)$};
\node[lab,tick] at (3.90,-0.96) {$(41,93)$};
\node[lab,tick] at (5.20,-0.96) {$(41,94)$};
\node[lab,tick] at (6.50,-0.96) {\textbf{no}};
\end{tikzpicture}
\end{center}
```

Freivalds' check with the $A$ and $B$ of @fig-divide-and-conquer-3 and a wrong $C$ (one entry off by $1$). Of the four vectors $r\in\{0,1\}^2$, exactly the two with $r_2=1$ expose the error, so one trial answers ``no'' with probability $\frac12$, and $k$ trials miss the error with probability $2^{-k}$.

:::

Repeating with $k$ independent vectors makes the error probability at most $2^{-k}$, still in $O(kn^2)$ time, much faster than multiplying $A$ and $B$.
