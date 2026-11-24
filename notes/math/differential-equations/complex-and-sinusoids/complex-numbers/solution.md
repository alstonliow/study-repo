<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-6-q1" status="draft"}
**(a)**

| | rectangular | $\lvert z\rvert$ | $\operatorname{Arg} z$ |
|---|---|---|---|
| (i) | $1-i$ | $\sqrt2$ | $-\pi/4$ |
| (ii) | $\sqrt3+i$ | $2$ | $\pi/6$ |
| (iii) | $-\tfrac{\sqrt2}2-\tfrac{\sqrt2}2i$ | $1$ | $-3\pi/4$ |
| (iv) | $\tfrac12+\tfrac{\sqrt3}2i$ | $1$ | $\pi/3$ |
| (v) | $-\tfrac{\sqrt2}2+\tfrac{\sqrt2}2i$ | $1$ | $3\pi/4$ |

For (iii), the square roots of $i=e^{i\pi/2}$ are $\pm e^{i\pi/4}$; the one in the third quadrant is $e^{-3i\pi/4}$. For (iv), the sixth roots of $1$ are $e^{ik\pi/3}$ and only $k=1$ has $0<\theta<\pi/2$. For (v), $(1+i)/\sqrt2=e^{i\pi/4}$, so the number is $e^{-13i\pi/4}=e^{3i\pi/4}$ after adding $4\pi$. Each picture marks the point at distance $|z|$ from $0$ at angle $\operatorname{Arg}z$.

**(b)** $z^4=-4=4e^{i\pi}$ gives $z=\sqrt2\,e^{i(\pi/4+k\pi/2)}$, $k=0,1,2,3$: the four numbers $\pm1\pm i$. By the quadratic formula, $z^2+2z+2=0$ has roots $z=-1\pm i$.
:::

::: {.solution for="prob-mit1803ps-6-q2" status="draft"}
**(a)** (i) $\sqrt2\,e^{-i\pi/4}$; (ii) $2e^{i\pi/6}$; (iii) $e^{-3i\pi/4}$; (iv) $e^{i\pi/3}$; (v) $e^{3i\pi/4}$.

**(b)** $e^{a+bi}=e^a e^{ib}=2e^{i\pi}$ requires $e^a=2$ and $b=\pi+2\pi k$: $z=\ln2+(2k+1)\pi i$, $k\in\mathbb Z$.

**(c)** $\cos4t=\operatorname{Re}(\cos t+i\sin t)^4$. By the binomial theorem the real terms are those with even powers of $i\sin t$:
$$\cos4t=\cos^4t-6\cos^2t\sin^2t+\sin^4t .$$

**(d)**

(i) $w=2\pi i$ (or $-2\pi i$). The trajectory is the unit circle, traversed once per unit of time.

(ii) $w=-1$. The trajectory is the segment $(0,1]$ of the positive real axis (all of $(0,\infty)$ if negative $t$ are included), moving towards $0$.

(iii) $w=-1+2\pi i$. The trajectory is a spiral winding counterclockwise into $0$, its distance from $0$ shrinking by the factor $e^{-1}$ per turn.

(iv) $w=0$. The trajectory is the single point $1$.
:::
