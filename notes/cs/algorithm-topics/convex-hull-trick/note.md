---
title: "Convex Hull Trick"
sources: []
requires: [cs/algorithm-topics/convex-hull]
status: draft
---

<!-- Added 2026-11-26 for the CSES problems Monster Game I and II and Lines and Queries I, in our own wording. TODO: add a source. -->

Dynamic programs of the form $f(i)=\min_{j<i}\bigl(m_j\,x_i+b_j\bigr)$ ask for the minimum over many lines at one point. Keeping only the lines that can ever be minimal makes each query fast.

::: {#def-lower-envelope .definition name="Lower envelope"}

For lines $\ell_j(x)=m_jx+b_j$, the *lower envelope* is $E(x)=\min_j\ell_j(x)$. A line is *useful* if it attains $E(x)$ at some $x$. The envelope is a concave piecewise linear function.

:::

::: {#thm-convex-hull-trick .theorem name="Convex hull trick"}

Let the lines be added in order of decreasing slope $m_1>m_2>\dots$ and let $\ell_1,\dots,\ell_t$ be the useful ones so far, kept in a stack. A new line $\ell$ is added by popping the top line $\ell_t$ while it is not useful with respect to $\ell_{t-1}$ and $\ell$, that is while

$$
(b-b_{t-1})(m_{t-1}-m_t)\le(b_t-b_{t-1})(m_{t-1}-m).
$$

A query at $x$ is answered by binary search on the intersection points in $O(\log n)$ time, or by a pointer that only moves forward if the query points $x$ increase. With sorted slopes, $n$ lines and queries cost $O(n)$ in total with the pointer, $O(n\log n)$ with binary search.

:::

::: {.proof}

1. *Which lines are useless.* For slopes $m_{t-1}>m_t>m$ the line $\ell_{t-1}$ is lowest far to the left and the new line $\ell$ far to the right. The line $\ell_t$ is lowest exactly between its crossing with $\ell_{t-1}$ and its crossing with $\ell$, so it is useless iff $x(\ell_{t-1},\ell)\le x(\ell_{t-1},\ell_t)$, where $x(\ell_a,\ell_b)=(b_b-b_a)/(m_a-m_b)$. Clearing the positive denominators gives the displayed inequality.

2. *Stack invariant.* After the pops the crossing points of consecutive stack lines increase from left to right, which is exactly the statement that every line on the stack is minimal on its own interval.

3. *Amortised cost.* Each line is pushed once and popped at most once.

4. *Query.* The envelope is minimal on consecutive intervals, so the line for $x$ is found by binary search on the crossing points; if the queries increase, the optimum moves to the right, so a pointer into the stack suffices.

:::

::: {#exm-convex-hull-trick-1 .example name="Three lines"}

The lines $-x+4$, $-2x+7$, $-3x+9$ have decreasing slopes. The crossing of the first two is at $x=3$, that of the first and last at $x=2.5\le3$, so the middle line is useless: at $x=2.5$ the three values are $1.5$, $2$, $1.5$. The envelope is $-x+4$ for $x\le2.5$ and $-3x+9$ afterwards.

:::

::: {#fig-convex-hull-trick-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=0.5cm]
\draw[gridline] (0,0) -- (5,0);
\draw[faint] (0,4) -- (5,-1);
\draw[faint] (0,7) -- (5,-3);
\draw[faint] (0,9) -- (5,-6);
\draw[hl] (0,4) -- (2.5,1.5) -- (5,-6);
\end{tikzpicture}
\end{center}
```

@exm-convex-hull-trick-1: the three lines and the lower envelope (highlighted). The line with slope $-2$ lies above the envelope at the crossing of the other two.

:::

::: {#rmk-convex-hull-trick-1 .remark name="Arbitrary slopes and the Li Chao tree"}

If lines arrive in arbitrary order, one can store them in a segment tree over the query coordinates (the *Li Chao tree*): each node keeps one line, and when a new line is inserted, the line that is lower at the middle of the node's interval stays, and the other one is pushed to the one half where it can still be lower. Insertion and query take $O(\log n)$ time. For $f(i)=\min_j(f(j)+\text{cost}(j,i))$ with cost $b_jx_i$-type products, the transition is a query for the lines $m_j=b_j$, $b=f(j)$.

:::
