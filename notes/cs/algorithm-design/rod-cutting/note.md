---
title: "Rod Cutting"
sources: [mit6006-18, mit6006r-18]
requires: [cs/algorithm-design/pseudopolynomial-time]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 18 and Recitation 18, in our own wording; examples our own (checked by computation); proofs written out in steps. Split from cs/algorithm-design/pseudopolynomial-time on 2026-11-25 (one problem per note, SPEC §8.6). -->

Integer subproblems: one for each length up to the given one.

::: {#exm-rod-cutting .example name="Rod cutting"}

A rod of integer length $L$ is to be cut into pieces of integer lengths; a piece of length $\ell$ sells for $v(\ell)$. Maximise the total value. For $L=5$ and values $v(1),\dots,v(5)=1,2,3,9,11$, the best is to sell the rod whole for $11$. Taking the piece with the best value per unit length first (length $4$, then $1$) gives only $10$, so the greedy idea fails.

1. *Subproblems:* $x(\ell)$, the most a rod of length $\ell$ yields, for $0\le\ell\le L$.
2. *Relation:* guess the length $p$ of the first piece: $x(\ell)=\max\{v(p)+x(\ell-p):1\le p\le\ell\}$.
3. *Order:* increasing $\ell$. 4. *Base:* $x(0)=0$.
5. *Original:* $x(L)$; storing the best $p$ for each $\ell$ recovers the cuts.
6. *Time:* $L+1$ subproblems with $O(L)$ work: $O(L^2)$.

:::

```{=latex}
\begin{algorithm}
\caption{Rod cutting}
\begin{algorithmic}
\INPUT Length $L$ and values $v(1),\dots,v(L)$
\OUTPUT The best total value $x(L)$
\STATE $x(0)\gets0$
\FOR{$\ell=1$ to $L$}
    \STATE $x(\ell)\gets\max\{v(p)+x(\ell-p):1\le p\le\ell\}$ \COMMENT{record the best $p$}
\ENDFOR
\RETURN $x(L)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-pseudopolynomial-time-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.550,0.900) rectangle (1.250,1.600);
\node[lab] at (0.900,1.250) {$1$};
\draw[cell frame] (1.250,0.900) rectangle (1.950,1.600);
\node[lab] at (1.600,1.250) {$2$};
\draw[cell frame] (1.950,0.900) rectangle (2.650,1.600);
\node[lab] at (2.300,1.250) {$3$};
\draw[cell frame] (2.650,0.900) rectangle (3.350,1.600);
\node[lab] at (3.000,1.250) {$9$};
\draw[cell frame] (3.350,0.900) rectangle (4.050,1.600);
\node[lab] at (3.700,1.250) {$11$};
\node[lab, anchor=east] at (0.450,1.250) {$v(\ell)$};
\draw[cell frame] (0.000,0.000) rectangle (0.700,0.700);
\node[lab] at (0.350,0.350) {$0$};
\draw[cell frame] (0.700,0.000) rectangle (1.400,0.700);
\node[lab] at (1.050,0.350) {$1$};
\draw[cell frame] (1.400,0.000) rectangle (2.100,0.700);
\node[lab] at (1.750,0.350) {$2$};
\draw[cell frame] (2.100,0.000) rectangle (2.800,0.700);
\node[lab] at (2.450,0.350) {$3$};
\draw[cell frame] (2.800,0.000) rectangle (3.500,0.700);
\node[lab] at (3.150,0.350) {$9$};
\draw[hl cell] (3.500,0.000) rectangle (4.200,0.700);
\node[lab] at (3.850,0.350) {$11$};
\node[lab, anchor=east] at (-0.100,0.350) {$x(\ell)$};
\draw[cell frame] (0.000,-0.900) rectangle (0.700,-0.200);
\draw[cell frame] (0.700,-0.900) rectangle (1.400,-0.200);
\node[lab] at (1.050,-0.550) {$1$};
\draw[cell frame] (1.400,-0.900) rectangle (2.100,-0.200);
\node[lab] at (1.750,-0.550) {$2$};
\draw[cell frame] (2.100,-0.900) rectangle (2.800,-0.200);
\node[lab] at (2.450,-0.550) {$3$};
\draw[cell frame] (2.800,-0.900) rectangle (3.500,-0.200);
\node[lab] at (3.150,-0.550) {$4$};
\draw[cell frame] (3.500,-0.900) rectangle (4.200,-0.200);
\node[lab] at (3.850,-0.550) {$5$};
\node[lab, anchor=east] at (-0.100,-0.550) {best $p$};
\node[lab,tick] at (0.35,1.85) {$0$};
\node[lab,tick] at (1.05,1.85) {$1$};
\node[lab,tick] at (1.75,1.85) {$2$};
\node[lab,tick] at (2.45,1.85) {$3$};
\node[lab,tick] at (3.15,1.85) {$4$};
\node[lab,tick] at (3.85,1.85) {$5$};
\node[lab,tick,anchor=east] at (-0.10,1.85) {$\ell$};
\end{tikzpicture}
\end{center}
```

Rod cutting for $L=5$ with values $1,2,3,9,11$, filled by increasing $\ell$. For example $x(4)=\max\{1+x(3),\,2+x(2),\,3+x(1),\,9+x(0)\}=9$. The answer is $x(5)=11$ with best first piece $p=5$: the rod is sold whole.

:::

The input consists of $L+1$ numbers ($L$ and the $L$ values), so $O(L^2)$ is a polynomial in the input size: rod cutting is solved in polynomial time.
