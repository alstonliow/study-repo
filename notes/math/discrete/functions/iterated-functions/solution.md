<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-functions-13" status="draft"}
All of them. If $f$ has inverse $f^{-1}$, then $f^{(k)}$ has inverse
$(f^{-1})^{(k)}$:

1. $f^{(k)}\circ(f^{-1})^{(k)} = f\circ\cdots\circ f\circ f^{-1}\circ\cdots\circ f^{-1}$.

2. The innermost $f\circ f^{-1}$ in the middle is the identity, so it can be
   removed. Repeating this $k$ times leaves the identity.

3. The same argument shows $(f^{-1})^{(k)}\circ f^{(k)}$ is the identity.
   (For $k=0$, $f^{(0)}$ is the identity, which is its own inverse.)
:::

::: {.solution for="prob-functions-14" status="draft"}
Write $f$ as the string $f(1)f(2)f(3)$. Exactly $9$ functions are eventually
constant:
$$111,\ 222,\ 333,\qquad 112,\ 131,\ 221,\ 233,\ 313,\ 322.$$
The first three are already constant. For the other six, $f^{(2)}$ is
constant: for example, $f = 112$ sends $3\mapsto2\mapsto1$ and fixes $1$.

**Challenge.** Draw $f$ as an arrow diagram, with an arrow $x\to f(x)$ for each
$x$. Then $f^{(k)}$ is eventually constant, with value $c$, if and only if:

1. $c$ is the only fixed point of $f$, and

2. every $x$ reaches $c$ by following arrows; equivalently, $f$ has no cycles
   other than the loop at $c$.

*Why.* If $f^{(k)}$ is constant with value $c$ for all large $k$, then
$f(c) = f(f^{(k)}(c)) = f^{(k+1)}(c) = c$. Any other fixed point $x$ would
have $f^{(k)}(x) = x\ne c$. A cycle of length at least $2$ would never reach
$c$. Conversely, if the conditions hold, every $x$ reaches $c$ within $n-1$
steps and stays there, so $f^{(n-1)}$ is constant.

These diagrams are rooted trees with all edges pointing toward the root $c$,
plus a loop at $c$. There are $n^{n-1}$ such functions; for $n = 3$ this
gives the $9$ above.
:::
