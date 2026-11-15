---
title: "Counting functions"
sources: [fit1058-cn-2.12]
requires: [math/discrete/functions/injections-surjections-bijections]
status: draft
---

<!-- Migrated from 1058note notes/chapters/02-functions.tex: Counting functions. -->

::: {#thm-counting-all-functions .theorem name="Counting all functions"}

If $|A|=m$, $|B|=n$, the number of functions $f: A \to B$ is $n^m$.

:::

::: {.proof}

Each of the $m$ elements of $A$ independently has $n$ possible images in $B$; by the product rule, $\underbrace{n \times n \times \cdots \times n}_{m} = n^m$.

:::

::: {#thm-counting-injections .theorem name="Counting injections"}

If $|A|=m$, $|B|=n$, the number of injections $f: A \to B$ is
$$n(n-1)(n-2)\cdots(n-m+1) = \frac{n!}{(n-m)!} \quad (\text{also written } P(n,m)).$$

:::

::: {#fig-functions-counting-1}

```{=latex}
\begin{tikzpicture}[x=0.9cm, y=0.9cm]
  \foreach \r/\a in {0/a,1/b,2/c} {
    \foreach \c/\b in {0/a,1/b,2/c} {
      \ifnum\r=\c
        \filldraw[fill=black!8, draw=white, line width=1.5pt] (\c,-\r) rectangle (\c+1,-\r-1);
      \else
        \filldraw[fill=defc!30, draw=white, line width=1.5pt] (\c,-\r) rectangle (\c+1,-\r-1);
      \fi
      \node[font=\small] at (\c+0.5,-\r-0.5) {$\a\b$};
    }
    \node[left, font=\small] at (0,-\r-0.5) {$\a$};
    \node[above, font=\small] at (\r+0.5,0) {$\a$};
  }
  \node[left, font=\small] at (-0.4,-1.5) {$f(1)$};
  \node[above, font=\small] at (1.5,0.4) {$f(2)$};
\end{tikzpicture}
```

The $3^2=9$ functions $f:\{1,2\}\to\{a,b,c\}$, written $f(1)f(2)$. The $3\cdot2=6$ off the diagonal (blue) are injective

:::

::: {.proof}

Enumerate $A = \{a_1,\dots,a_m\}$. $a_1$ has $n$ choices in $B$; $a_2$ must avoid $f(a_1)$, so $n-1$ choices; …; $a_m$ must avoid the $m-1$ already-used values, so $n-m+1$ choices. These choices are made in sequence, so by the product rule the total is $n(n-1)\cdots(n-m+1)$.

:::

::: {.remark}

If $m > n$, the product includes a factor of $0$, correctly giving $0$ injections – consistent with the pigeonhole principle.

:::

::: {#thm-counting-bijections-permutations .theorem name="Counting bijections / permutations"}

If $|A|=|B|=n$, the number of bijections $f: A \to B$ is $n!$.

:::

::: {.proof}

By @sec-math-discrete-functions-injections-surjections-bijections, for finite sets of equal size, bijective $\iff$ injective. So this is the injection count with $m=n$: $n(n-1)\cdots(n-n+1) = n!$.

:::

::: {.remark}

In particular, the number of permutations of an $n$-element set (bijections $A \to A$) is $n!$.

:::
