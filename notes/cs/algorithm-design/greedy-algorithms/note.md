---
title: "Greedy Algorithms: Interval Scheduling"
sources: [mit6046-1, mit6046r-6]
requires: [cs/algorithm-design/interval-subproblems]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 1 and Recitation 6, in our own wording; proofs written out in steps. -->

A *greedy* algorithm builds a solution one choice at a time, each time taking the choice that looks best now and never undoing it. It is fast and simple, but correct only for problems with the right structure, and the proof is the hard part. The usual proof shows that some optimal solution agrees with each greedy choice (an *exchange argument*), or that greedy *stays ahead* of every other solution.

## Interval scheduling

::: {#def-interval-scheduling .definition name="Interval scheduling"}

Requests $1,\dots,n$ each ask for a resource during $[s(i),f(i))$, with $s(i)<f(i)$. Two requests are *compatible* if their intervals do not overlap. Find a largest set of pairwise compatible requests.

:::

Natural greedy rules fail: choosing the shortest interval first, or the one with the fewest conflicts first, or the earliest start first, each has small counterexamples. The right rule is to finish as early as possible.

::: {#def-earliest-finish .definition name="Earliest-finish-time-first"}

Repeat: choose the request with the earliest finishing time, add it to the schedule, and delete every request incompatible with it; stop when no request is left. After sorting by finishing time this takes $O(n\log n)$ time.

:::

```{=latex}
\begin{algorithm}
\caption{Earliest-finish-time-first}
\begin{algorithmic}
\INPUT Requests $[s(i),f(i))$, $i=1,\dots,n$
\OUTPUT A largest set $R$ of compatible requests
\STATE sort the requests so that $f(1)\le\dots\le f(n)$
\STATE $R\gets\emptyset$; $t\gets-\infty$ \COMMENT{finishing time of the last chosen request}
\FOR{$i=1$ to $n$}
    \IF{$s(i)\ge t$}
        \STATE $R\gets R\cup\{i\}$; $t\gets f(i)$
    \ENDIF
\ENDFOR
\RETURN $R$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-earliest-finish .theorem name="Earliest finish is optimal"}

Earliest-finish-time-first returns a largest set of compatible requests.

:::

::: {.proof}

1. Let the greedy choices be $i_1,i_2,\dots,i_k$ in order and let $j_1,j_2,\dots,j_m$ be any compatible set, sorted by finishing time. We show by induction on $r$ that $f(i_r)\le f(j_r)$ for all $r\le\min(k,m)$ ("greedy stays ahead").

2. For $r=1$, greedy picks the request that finishes first of all, so $f(i_1)\le f(j_1)$.

3. Suppose $f(i_{r-1})\le f(j_{r-1})$. Then $s(j_r)\ge f(j_{r-1})\ge f(i_{r-1})$, so $j_r$ is compatible with $i_1,\dots,i_{r-1}$ and was still available when greedy chose $i_r$. Greedy chose the earliest-finishing available request, so $f(i_r)\le f(j_r)$.

4. If $m>k$, then $j_{k+1}$ starts after $f(j_k)\ge f(i_k)$, so it was still available after greedy's last choice, and greedy would not have stopped. Hence $m\le k$.

:::

::: {#fig-greedy-algorithms-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.55cm,y=0.42cm]
\foreach \s/\f/\y/\c in {0/6/0/box, 1/4/1/hl box, 3/5/2/box, 3/8/3/box, 4/7/4/hl box, 5/9/5/box, 6/10/6/box, 8/11/7/hl box} {
  \draw[\c] (\s,-\y) rectangle (\f,-\y-0.7);
}
\draw[faint] (0,-8.3) -- (12,-8.3);
\foreach \t in {0,2,...,12} \node[lab,tick] at (\t,-8.8) {\t};
\end{tikzpicture}
\end{center}
```

Eight requests drawn as intervals in time. Earliest finish first picks $[1,4)$, then the earliest-finishing request starting at or after $4$, namely $[4,7)$, then $[8,11)$ (highlighted): three requests, which is the maximum.

:::

## Weighted interval scheduling

If each request has a weight and we want the compatible set of largest total weight, no greedy rule works, but dynamic programming does: sort by finishing time and use @exm-weighted-interval-scheduling, in $O(n\log n)$ time.

## Scheduling to minimise total completion time

::: {#prp-shortest-processing-time .proposition name="Shortest processing time first"}

One machine must run $n$ jobs with processing times $t_1,\dots,t_n$, one after the other. If job $i$ completes at time $C_i$, the sum $\sum_iC_i$ (equivalently the average waiting time) is minimised by running the jobs in increasing order of $t_i$.

:::

::: {.proof}

1. If jobs run in the order $\pi(1),\dots,\pi(n)$, then $\sum_iC_i=\sum_{r=1}^n(n-r+1)\,t_{\pi(r)}$: the job in position $r$ delays itself and the $n-r$ jobs after it.

2. Suppose some order has a longer job immediately before a shorter one, $t_{\pi(r)}>t_{\pi(r+1)}$. Swapping them changes the sum by $(n-r+1)(t_{\pi(r+1)}-t_{\pi(r)})+(n-r)(t_{\pi(r)}-t_{\pi(r+1)})=t_{\pi(r+1)}-t_{\pi(r)}<0$ (an exchange argument).

3. So an optimal order has no such adjacent pair, that is, it is sorted by processing time.

:::

```{=latex}
\begin{algorithm}
\caption{Shortest processing time first}
\begin{algorithmic}
\INPUT Processing times $t_1,\dots,t_n$
\OUTPUT An order of the jobs minimising $\sum_iC_i$, and that sum
\STATE sort the jobs so that $t_{\pi(1)}\le\dots\le t_{\pi(n)}$
\STATE $T\gets0$; $\Sigma\gets0$
\FOR{$j=1$ to $n$}
    \STATE $T\gets T+t_{\pi(j)}$ \COMMENT{completion time of job $\pi(j)$}
    \STATE $\Sigma\gets\Sigma+T$
\ENDFOR
\RETURN $\pi$, $\Sigma$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-greedy-algorithms-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab,anchor=east] at (-0.20,0.25) {given order};
\draw[box] (0.00,0.00) rectangle (3.60,0.50);
\node[lab] at (1.80,0.25) {$J_1$};
\node[lab,tick] at (3.60,-0.20) {$4$};
\draw[box] (3.60,0.00) rectangle (4.50,0.50);
\node[lab] at (4.05,0.25) {$J_2$};
\node[lab,tick] at (4.50,-0.20) {$5$};
\draw[box] (4.50,0.00) rectangle (7.20,0.50);
\node[lab] at (5.85,0.25) {$J_3$};
\node[lab,tick] at (7.20,-0.20) {$8$};
\node[lab,anchor=west] at (7.50,0.25) {$\sum C_i=17$};
\node[lab,anchor=east] at (-0.20,-0.95) {shortest first};
\draw[box] (0.00,-1.20) rectangle (0.90,-0.70);
\node[lab] at (0.45,-0.95) {$J_2$};
\node[lab,tick] at (0.90,-1.40) {$1$};
\draw[box] (0.90,-1.20) rectangle (3.60,-0.70);
\node[lab] at (2.25,-0.95) {$J_3$};
\node[lab,tick] at (3.60,-1.40) {$4$};
\draw[box] (3.60,-1.20) rectangle (7.20,-0.70);
\node[lab] at (5.40,-0.95) {$J_1$};
\node[lab,tick] at (7.20,-1.40) {$8$};
\node[lab,anchor=west] at (7.50,-0.95) {$\sum C_i=13$};
\end{tikzpicture}
\end{center}
```

Three jobs $J_1,J_2,J_3$ with processing times $4,1,3$ (small numbers are completion times). In the given order the completion times are $4,5,8$, summing to $17$; shortest first gives $1,4,8$, summing to $13$, the minimum. Every job waits for all jobs before it, so short jobs should go first.

:::

::: {#rmk-greedy-algorithms-hard .remark name="When greedy is not enough"}

Small changes make interval problems hard: if each request may be served by only some of several non-identical machines, deciding whether all requests can be scheduled is NP-complete (@sec-cs-theory-np-complete-reductions). Then one looks for approximation algorithms (@sec-cs-algorithm-topics-approximation-algorithms) or algorithms fast for small parameters (@sec-cs-algorithm-topics-fixed-parameter-algorithms).

:::
