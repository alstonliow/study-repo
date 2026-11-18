<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801f06-1-q1" status="draft"}
Let $f(x)=\frac{x-1}{x+1}$, so $f(-x)=\frac{-x-1}{-x+1}=\frac{x+1}{x-1}$. By @thm-even-odd-decomposition the even and odd parts are
$$E(x)=\frac12\Big(\frac{x-1}{x+1}+\frac{x+1}{x-1}\Big)=\frac{(x-1)^2+(x+1)^2}{2(x^2-1)}=\frac{x^2+1}{x^2-1},$$
$$O(x)=\frac12\Big(\frac{x-1}{x+1}-\frac{x+1}{x-1}\Big)=\frac{(x-1)^2-(x+1)^2}{2(x^2-1)}=\frac{-2x}{x^2-1}.$$
Check: $E+O=\frac{x^2-2x+1}{x^2-1}=\frac{(x-1)^2}{(x-1)(x+1)}=\frac{x-1}{x+1}$. Both parts are defined for $x\neq\pm1$ (the decomposition needs a domain symmetric about $0$).
:::

::: {.solution for="prob-mit1801n-1a-q1" status="draft"}
$y=(x-1)^2-2$: the parabola $y=x^2$ moved $1$ to the right and $2$ down (@prp-graph-transformations), with vertex $(1,-2)$, crossing the $x$-axis at $1\pm\sqrt2$.
:::

::: {.solution for="prob-mit1801n-1a-q2" status="draft"}
The graph of $\lvert x\rvert$ (a V with corner at the origin) moved $2$ to the left and $1$ up: a V with corner at $(-2,1)$ and slopes $\pm1$.
:::

::: {.solution for="prob-mit1801n-1a-q3" status="draft"}
a) Replacing $x$ by $-x$ changes the sign of the numerator and leaves the denominator unchanged: **odd**.

b) $(\sin(-x))^2=(-\sin x)^2=\sin^2x$: **even**.

e) $J_0((-x)^2)=J_0(x^2)$, whatever $J_0$ is: **even**.
:::

::: {.solution for="prob-mit1801n-1a-q5" status="draft"}
$y=x^2+2x=(x+1)^2-1$ is not one-to-one on $\mathbb R$; restrict to $x\ge-1$, where it is increasing. Solving, $x=-1+\sqrt{y+1}$, so
$$g(x)=-1+\sqrt{x+1},\qquad x\ge-1 .$$
(On the other half, $x\le-1$, the inverse is $-1-\sqrt{x+1}$.) The graph of $g$ is the reflection of the right half of the parabola in $y=x$ (@prp-graph-of-inverse): it starts at $(-1,-1)$ and rises like a square root.

*Discrepancy:* the official solution restricts to $x\le-1$ but then gives $\sqrt{x+1}-1$, which is the inverse of the other half, $x\ge-1$.
:::

::: {.solution for="prob-mit1801n-1a-q6" status="draft"}
$A\sin(x+c)=A\cos c\sin x+A\sin c\cos x$, so $A\cos c=1$ and $A\sin c=\sqrt3$. Then $A=\sqrt{1+3}=2$ and $\tan c=\sqrt3$ with $\cos c>0$, so $c=\pi/3$:
$$\sin x+\sqrt3\cos x=2\sin\Big(x+\frac\pi3\Big).$$
:::

::: {.solution for="prob-mit1801n-1a-q7" status="draft"}
$3\sin(2x-\pi)=3\sin\big(2(x-\frac\pi2)\big)$: amplitude $3$, period $\frac{2\pi}2=\pi$, and the graph of $3\sin2x$ is shifted right by $\frac\pi2$ (the phase angle in the sense of the Notes). Since $\sin(\theta-\pi)=-\sin\theta$, this is also $-3\sin2x$: it starts at $0$, goes down to $-3$ at $x=\pi/4$, back to $0$ at $\pi/2$, up to $3$ at $3\pi/4$, and repeats with period $\pi$.
:::
