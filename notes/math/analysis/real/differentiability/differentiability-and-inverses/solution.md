<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cama1s-2-q3" status="draft"}
No. Let $f(x) = 0$ for all $x$, so $f(x) \to \ell = 0$ as $x \to a$ (any $a$). Let $g(y) = 0$ for $y \ne 0$ and $g(0) = 1$, so $g(y) \to k = 0$ as $y \to 0$ (the value at $0$ is ignored). But $g(f(x)) = g(0) = 1$ for all $x$, so $g(f(x)) \to 1 \ne k$.

The conclusion does hold if in addition $g$ is continuous at $\ell$ with $g(\ell) = k$, or if $f(x) \ne \ell$ for all $x \ne a$ near $a$: in both cases the $\delta$ for $f$ (with $\varepsilon$ replaced by the $\delta$ for $g$) works for $g \circ f$.
:::

::: {.solution for="prob-cama1s-2-q11" status="draft"}
1. For $x \ne 0$, $f$ is differentiable by the product and chain rules, with $f'(x) = 1 + 4x\sin(1/x) - 2\cos(1/x)$.

2. At $0$: $\dfrac{f(h) - f(0)}{h} = 1 + 2h\sin(1/h)$, and $|2h\sin(1/h)| \le 2|h| \to 0$. So $f'(0) = 1$.

3. Let $x_k = 1/(2k\pi)$. Then $f'(x_k) = 1 + 0 - 2 = -1 < 0$. Since $f'$ is continuous on $\mathbb{R}\setminus\{0\}$, $f' < 0$ on some interval around $x_k$, and by the mean value theorem $f$ is strictly decreasing on it.

4. Every interval around $0$ contains some $x_k$ together with a small interval around it, so $f$ is not increasing on any interval around $0$.
:::

::: {.solution for="prob-cama1s-3-q6" status="draft"}
Away from $0$ everything is smooth, so only the behaviour at $0$ matters. For $x \ne 0$,
$$f'_\alpha(x) = \alpha|x|^{\alpha-1}\operatorname{sgn}(x)\sin(1/x) - |x|^{\alpha-2}\cos(1/x).$$

1. Bounded iff $\alpha \ge 0$ (for $\alpha < 0$, take $x = 1/(2k\pi + \pi/2)$).

2. Continuous at $0$ iff $|x|^\alpha\sin(1/x) \to 0$, iff $\alpha > 0$. So $f_0$ is not continuous.

3. $f_\alpha(h)/h = \pm|h|^{\alpha-1}\sin(1/h) \to 0$ iff $\alpha > 1$; otherwise the quotient has no limit. So $f_1$ is not differentiable at $0$, and $f_\alpha$ is differentiable iff $\alpha > 1$, with $f'_\alpha(0) = 0$.

4. For $\alpha > 1$, $f'_\alpha$ is bounded iff the term $|x|^{\alpha-2}\cos(1/x)$ is bounded, iff $\alpha \ge 2$; it is continuous at $0$ iff that term tends to $0$, iff $\alpha > 2$. For $\alpha \le 1$, $f'_\alpha$ is not defined at $0$ (and is unbounded near $0$), so all three $f'$ rows get crosses.

5. For $\alpha > 2$, $f'_\alpha(h)/h$ behaves like $\mp|h|^{\alpha-3}\cos(1/h)$, which tends to $0$ iff $\alpha > 3$. So $f'_\alpha$ is differentiable iff $\alpha > 3$.

| | $-\frac12$ | $0$ | $\frac12$ | $1$ | $\frac32$ | $2$ | $\frac52$ | $3$ | $\frac72$ |
|---|---|---|---|---|---|---|---|---|---|
| $f_\alpha$ bounded | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| $f_\alpha$ continuous | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| $f_\alpha$ differentiable | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ |
| $f'_\alpha$ bounded | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ |
| $f'_\alpha$ continuous | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ |
| $f'_\alpha$ differentiable | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ |
:::
