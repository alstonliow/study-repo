---
title: "Weighted Interval Scheduling"
sources: [mit6046-1, mit6046r-1]
requires: [cs/algorithm-patterns/greedy-algorithms]
aliases: [cs/algorithm-design/weighted-interval-scheduling]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 1 and Recitation 1, in our own wording; examples our own (checked by computation); proofs written out in steps. Split from cs/algorithm-design/interval-subproblems on 2026-11-25 (one problem per note, SPEC §8.6). -->

With weights on the requests, no greedy rule is optimal for interval scheduling (@def-interval-scheduling), but a dynamic program on suffixes is.

::: {#exm-weighted-interval-scheduling .example name="Weighted interval scheduling"}

Requests $[s(i),f(i))$ have weights $w(i)$; choose compatible requests of largest total weight (the unweighted version is @def-interval-scheduling). Sort the requests by starting time, $s(1)\le\dots\le s(n)$, and let $\mathrm{next}(i)$ be the first request $j>i$ with $s(j)\ge f(i)$, found by binary search.

1. *Subproblems:* $x(i)$, the best total weight using only requests $i,\dots,n$ (a suffix).
2. *Relation:* request $i$ is not used, or it is used and then the next usable request is $\mathrm{next}(i)$: $x(i)=\max\{x(i+1),\ w(i)+x(\mathrm{next}(i))\}$.
3. *Order:* decreasing $i$. 4. *Base:* $x(n+1)=0$. 5. *Original:* $x(1)$.
6. *Time:* sorting and the binary searches take $O(n\log n)$, and the $n$ subproblems $O(1)$ each.

:::

```{=latex}
\begin{algorithm}
\caption{Weighted interval scheduling}
\begin{algorithmic}
\INPUT Requests $[s(i),f(i))$ with weights $w(i)$, $i=1,\dots,n$
\OUTPUT The largest total weight of compatible requests
\STATE sort the requests so that $s(1)\le\dots\le s(n)$
\FOR{$i=1$ to $n$}
    \STATE $\mathrm{next}(i)\gets$ the least $j>i$ with $s(j)\ge f(i)$, or $n+1$ \COMMENT{binary search}
\ENDFOR
\STATE $x(n+1)\gets0$
\FOR{$i=n$ down to $1$}
    \STATE $x(i)\gets\max\{x(i+1),\ w(i)+x(\mathrm{next}(i))\}$
\ENDFOR
\RETURN $x(1)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-interval-subproblems-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[x=0.55cm,y=0.42cm]
\draw[hl box] (0,0) rectangle (6,-0.7);
\node[lab,tick] at (3.0,-0.35) {$5$};
\node[lab,tick] at (13.5,-0.35) {$1$};
\node[lab,tick] at (15,-0.35) {$7$};
\node[lab,tick] at (16.5,-0.35) {$8$};
\draw[box] (1,-1) rectangle (4,-1.7);
\node[lab,tick] at (2.5,-1.35) {$2$};
\node[lab,tick] at (13.5,-1.35) {$2$};
\node[lab,tick] at (15,-1.35) {$5$};
\node[lab,tick] at (16.5,-1.35) {$7$};
\draw[box] (3,-2) rectangle (5,-2.7);
\node[lab,tick] at (4.0,-2.35) {$3$};
\node[lab,tick] at (13.5,-2.35) {$3$};
\node[lab,tick] at (15,-2.35) {$6$};
\node[lab,tick] at (16.5,-2.35) {$7$};
\draw[box] (3,-3) rectangle (8,-3.7);
\node[lab,tick] at (5.5,-3.35) {$5$};
\node[lab,tick] at (13.5,-3.35) {$4$};
\node[lab,tick] at (15,-3.35) {$8$};
\node[lab,tick] at (16.5,-3.35) {$7$};
\draw[box] (4,-4) rectangle (7,-4.7);
\node[lab,tick] at (5.5,-4.35) {$3$};
\node[lab,tick] at (13.5,-4.35) {$5$};
\node[lab,tick] at (15,-4.35) {$8$};
\node[lab,tick] at (16.5,-4.35) {$5$};
\draw[box] (5,-5) rectangle (9,-5.7);
\node[lab,tick] at (7.0,-5.35) {$4$};
\node[lab,tick] at (13.5,-5.35) {$6$};
\node[lab,tick] at (15,-5.35) {$9$};
\node[lab,tick] at (16.5,-5.35) {$4$};
\draw[hl box] (6,-6) rectangle (10,-6.7);
\node[lab,tick] at (8.0,-6.35) {$3$};
\node[lab,tick] at (13.5,-6.35) {$7$};
\node[lab,tick] at (15,-6.35) {$9$};
\node[lab,tick] at (16.5,-6.35) {$3$};
\draw[box] (8,-7) rectangle (11,-7.7);
\node[lab,tick] at (9.5,-7.35) {$2$};
\node[lab,tick] at (13.5,-7.35) {$8$};
\node[lab,tick] at (15,-7.35) {$9$};
\node[lab,tick] at (16.5,-7.35) {$2$};
\node[lab,tick] at (13.5,1) {$i$};
\node[lab,tick] at (15,1) {$\mathrm{next}(i)$};
\node[lab,tick] at (16.5,1) {$x(i)$};
\draw[faint] (0,-8.3) -- (12,-8.3);
\foreach \t in {0,2,...,12} \node[lab,tick] at (\t,-8.8) {\t};
\end{scope}
\end{tikzpicture}
\end{center}
```

The eight requests of @fig-greedy-algorithms-1, sorted by start, now with weights (inside the bars). The table gives $\mathrm{next}(i)$ ($9$ means none) and $x(i)$, computed from the bottom up. The best total weight is $x(1)=8$, from the highlighted requests $[0,6), [6,10)$; the most requests, three, would weigh less.

:::
