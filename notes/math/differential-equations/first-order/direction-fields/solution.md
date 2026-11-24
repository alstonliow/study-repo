<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-2-q1" status="draft"}
**(a)** The isocline of slope $m$ is $y^2 - x = m$, the parabola $x = y^2 - m$ opening to the right with vertex $(-m,0)$. Slopes are positive to the left of the nullcline $x=y^2$ and negative inside it. Solutions rise steeply when $|y|$ is large and to the left; inside the nullcline they fall.

**(b)** Numerically, the separatrix passes through $(0,\,0.729\ldots)$. To its right it runs just below the upper half $y=\sqrt x$ of the nullcline and is asymptotic to it; solutions starting above it blow up, solutions below it cross the nullcline and then decrease.

**(c)**

1. On the isocline $x = y^2+1$ the solution has slope $-1$.
2. Differentiating $x=y^2+1$ implicitly, the isocline has slope $dy/dx = 1/(2y)$.
3. Tangency means $1/(2b) = -1$, so $b = -\tfrac12$ and $a = b^2+1 = \tfrac54$.

**(d)** The solution is eventually trapped between the nullcline $y=-\sqrt x$ and the lower branch $y=-\sqrt{x-1}$ of the $m=-1$ isocline, and both are asymptotic to $-\sqrt x$ (their difference tends to $0$). So $y(x)\sim-\sqrt x$, and for large $x$ we have $y(x) > f(x)$ whatever $y(a)$ is.

(i) On the lower branch $y=-\sqrt{x-1}$ with $x>a$, the isocline has slope $-1/(2\sqrt{x-1}) > -1$, while a solution crossing it has slope $-1$, which is steeper downward. So a solution can only cross it from above to below, never from below to above; a solution below it at $x=a$ stays below.

(ii) On the nullcline $y=-\sqrt x$ the solution has slope $0$, while the nullcline has negative slope $-1/(2\sqrt x)$. A solution touching it from above would cross it moving upward relative to it, so it cannot pass below: once above, it stays above.

(iii) Suppose the solution stayed below $-\sqrt x$ for all $x>c$. Below the nullcline $y'=y^2-x>0$, so $y(x)\ge y(c)$ for all $x>c$; but $-\sqrt x\to-\infty$, so eventually $y(x)>-\sqrt x$, a contradiction. Hence it crosses.

**(e)** $y'(c) = d^2 - c = 0$: the point lies on the nullcline, $c = d^2$.

**(f)** Yes. Differentiating the equation, $y'' = 2yy' - 1$, so at a critical point $y''=-1<0$: every critical point is a strict local maximum.
:::
