---
title: "Binary Search on the Answer and Ternary Search"
sources: [cs97si-9]
requires: [cs/sorting/binary-search]
status: draft
---

<!-- Added 2026-11-26 from Stanford CS 97SI (Winter 2011-12), Lecture 9 (notes on binary and ternary search), in our own wording; proofs written out in steps. The example is our own. -->

Binary search (@prp-binary-search) works on any monotone yes/no question, not only on sorted arrays; ternary search finds the minimum of a function that decreases and then increases.

::: {#prp-binary-search-predicate .proposition name="Binary search on a monotone predicate"}

Let $P$ be a predicate on the integers $l,\dots,h$ with $P(l)$ false, $P(h)$ true and $P$ monotone ($P(x)$ implies $P(x+1)$). Repeating "$m\gets\lfloor(l+h)/2\rfloor$; if $P(m)$ then $h\gets m$ else $l\gets m$" until $h=l+1$ ends with $h$ the smallest $x$ such that $P(x)$ holds, after $\lceil\log_2(h-l)\rceil$ evaluations of $P$.

:::

::: {.proof}

1. *Invariant:* $P(l)$ is false and $P(h)$ is true. It holds at the start, and each step replaces $h$ by an $m$ with $P(m)$ true or $l$ by an $m$ with $P(m)$ false.

2. While $h\ge l+2$, the midpoint satisfies $l<m<h$, so $h-l$ drops to at most $\lceil(h-l)/2\rceil$ and the loop stops after $\lceil\log_2(h-l)\rceil$ steps.

3. At the end $h=l+1$ with $P(l)$ false and $P(h)$ true; by monotonicity every $x\le l$ is false, so $h$ is the smallest true point.

:::

Many optimisation problems are solved this way: "can it be done with cost at most $x$?" is monotone in $x$, so binary search on $x$ turns a decision procedure into an optimiser ("binary search on the answer"). On real numbers, run a fixed number of halvings instead of testing $h=l+1$.

::: {#def-ternary-search .definition name="Ternary search"}

A function $f:[l,h]\to\mathbb{R}$ is *unimodal* if for some $x^*$ it is strictly decreasing on $[l,x^*]$ and strictly increasing on $[x^*,h]$. *Ternary search* repeats: let $m_1=l+(h-l)/3$ and $m_2=h-(h-l)/3$; if $f(m_1)<f(m_2)$ set $h\gets m_2$, otherwise set $l\gets m_1$.

:::

```{=latex}
\begin{algorithm}
\caption{Ternary search for the minimum of a unimodal $f$}
\begin{algorithmic}
\INPUT Unimodal $f$ on $[l,h]$, number of rounds $R$
\OUTPUT An approximation of $x^*$
\FOR{$t=1$ \TO $R$}
    \STATE $m_1\gets l+(h-l)/3$; $m_2\gets h-(h-l)/3$
    \IF{$f(m_1)<f(m_2)$}
        \STATE $h\gets m_2$ \COMMENT{$x^*\notin(m_2,h]$}
    \ELSE
        \STATE $l\gets m_1$ \COMMENT{$x^*\notin[l,m_1)$}
    \ENDIF
\ENDFOR
\RETURN $(l+h)/2$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-ternary-search .theorem name="Ternary search"}

Each round keeps $x^*\in[l,h]$ and multiplies the length $h-l$ by $2/3$. After $R$ rounds the returned point is within $\tfrac12(2/3)^R(h_0-l_0)$ of $x^*$, using $2R$ evaluations of $f$.

:::

::: {.proof}

1. *Case $f(m_1)<f(m_2)$.* If $x^*>m_2$, both $m_1<m_2$ would lie on the decreasing part, giving $f(m_1)>f(m_2)$, a contradiction. So $x^*\le m_2$ and $[l,m_2]$ still contains $x^*$.

2. *Case $f(m_1)\ge f(m_2)$.* If $x^*<m_1$, both points would lie on the increasing part, giving $f(m_1)<f(m_2)$, a contradiction. So $x^*\ge m_1$.

3. Either way the new interval has length $\tfrac23(h-l)$. After $R$ rounds it has length $(2/3)^R(h_0-l_0)$ and contains $x^*$, so its midpoint is within half of that.

:::

::: {#exm-ternary-search-1 .example name="A parabola"}

For $f(x)=(x-2)^2+1$ on $[0,5]$: round 1 compares $f(5/3)\approx1.11$ with $f(10/3)\approx2.78$ and keeps $[0,3.33]$; round 2 compares $f(1.11)\approx1.79$ with $f(2.22)\approx1.05$ and keeps $[1.11,3.33]$; round 3 compares $f(1.85)\approx1.02$ with $f(2.59)\approx1.35$ and keeps $[1.11,2.59]$, which contains $x^*=2$.

:::

::: {#fig-ternary-search-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.3cm,y=0.45cm]
\draw[->] (-0.2,0) -- (5.3,0) node[lab,right] {$x$};
\draw[->] (0,-0.2) -- (0,10.5) node[lab,above] {$f$};
\draw[emph, domain=0:5, samples=60, smooth] plot (\x,{(\x-2)^2+1});
\foreach \m/\c in {1.667/faint,3.333/faint} \draw[\c,dashed] (\m,0) -- (\m,{(\m-2)^2+1});
\node[dot] at (1.667,1.111) {}; \node[dot] at (3.333,2.778) {};
\node[lab,tick,below] at (1.667,0) {$m_1$}; \node[lab,tick,below] at (3.333,0) {$m_2$};
\draw[hl] (0,-0.9) -- (3.333,-0.9);
\draw[faint] (3.333,-0.9) -- (5,-0.9);
\node[lab,tick,anchor=west] at (5.05,-0.9) {kept: $[0,m_2]$};
\node[hl dot] at (2,1) {}; \node[lab,tick,above] at (2,1.3) {$x^*$};
\end{tikzpicture}
\end{center}
```

The first round of @exm-ternary-search-1: $f(m_1)<f(m_2)$, so the minimum cannot lie right of $m_2$ and the last third is discarded.

:::

::: {#rmk-ternary-search-1 .remark name="Plateaus and integers"}

If $f$ may be constant on a stretch, equal values no longer say which side to drop and ternary search can fail; then binary search on the sign of $f(x+1)-f(x)$ (for integers) or of the derivative is safer. On integers, stop when $h-l\le2$ and check the remaining points directly.

:::
