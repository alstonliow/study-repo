<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-ats-4-q11" status="draft"}
(a) Let $g(x) = \|x\|^2 = x\cdot x$. Then $g(x + h) = g(x) + 2x\cdot h + \|h\|^2$, and $\|h\|^2/\|h\| \to 0$. So $g$ is differentiable with $Dg|_x(h) = 2x\cdot h$.

(b)

1. On $x \ne 0$, $\varphi(x) = \|x\|^{-1} = u(g(x))$ with $u(t) = t^{-1/2}$, differentiable for $t > 0$. By the chain rule, $D\varphi|_x(h) = -\frac12 g(x)^{-3/2}\cdot 2x\cdot h = -\dfrac{x\cdot h}{\|x\|^3}$.

2. $f(x) = \varphi(x)x$ is a product of a scalar function and the identity map, so by the product rule
$$Df|_x(h) = D\varphi|_x(h)\,x + \varphi(x)h = \frac{h}{\|x\|} - \frac{x(x\cdot h)}{\|x\|^3}.$$

3. At $0$, $f$ is not even continuous: for a unit vector $e$, $f(te) = e$ for $t > 0$ but $f(0) = 0$. So it is not differentiable there.

(c) $x\cdot Df|_x(h) = \dfrac{x\cdot h}{\|x\|} - \dfrac{\|x\|^2(x\cdot h)}{\|x\|^3} = 0$. Geometrically, $f$ maps $\mathbb{R}^n\setminus\{0\}$ into the unit sphere, so $\|f\|^2 \equiv 1$ and $2f(x)\cdot Df|_x(h) = 0$: the derivative is tangent to the sphere at $f(x) = x/\|x\|$, which is perpendicular to $x$. Also $f$ is constant along rays, so $Df|_x(x) = 0$: only the component of $h$ perpendicular to $x$ matters, scaled by $1/\|x\|$.
:::
