<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-24-q1" status="draft"}
Use @def-generalized-derivative: the ordinary derivative plus a delta at each jump, weighted by the jump.

**(a)** $f=-t\,u(t)$ is continuous (a ramp going down), so $f'=-u(t)$: $0$ then $-1$.

**(b)** $f=(1-t)\,u(t)$ jumps by $+1$ at $0$, so $f'=-u(t)+\delta(t)$.

**(c)** $f=(2t-1)\bigl(u(t)-u(t-1)\bigr)$ jumps by $-1$ at $t=0$ (from $0$ to $-1$) and by $-1$ at $t=1$ (from $1$ to $0$), so
$$f'=2\bigl(u(t)-u(t-1)\bigr)-\delta(t)-\delta(t-1).$$

**(d)** A sawtooth rising with slope $1$ from $0$ to $1$ on each $[k,k+1)$: $f=t\,u(t)-\displaystyle\sum_{k\ge1}u(t-k)$. It is continuous at $0$ and drops by $1$ at each positive integer, so
$$f'=u(t)-\sum_{k\ge1}\delta(t-k).$$
:::
