<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit1801f06-2a-q4" status="draft"}
a) Let $y=\cos^{-1}x$, so $\cos y=x$ with $0\le y\le\pi$. Differentiating, $-\sin y\cdot y'=1$. On $[0,\pi]$, $\sin y\ge0$, so $\sin y=+\sqrt{1-\cos^2y}=\sqrt{1-x^2}$ and
$$\frac{d}{dx}\cos^{-1}x=\frac{-1}{\sqrt{1-x^2}}\qquad(-1<x<1).$$

b) If $\theta=\sin^{-1}x\in[-\pi/2,\pi/2]$, then $\cos(\pi/2-\theta)=\sin\theta=x$ with $\pi/2-\theta\in[0,\pi]$, so $\cos^{-1}x=\pi/2-\sin^{-1}x$. The sum $\sin^{-1}x+\cos^{-1}x=\pi/2$ is constant, so its derivative is $0$. (Geometrically: the two acute angles of a right triangle add up to $\pi/2$.)
:::

::: {.solution for="prob-mit1801f06-3-q2" status="draft"}
Differentiating implicitly, $\frac23x^{-1/3}+\frac23y^{-1/3}y'=0$, so at a point $(x_0,y_0)$ of the curve with $x_0,y_0>0$ the slope is $m=-(y_0/x_0)^{1/3}$.

The tangent line $y=y_0+m(x-x_0)$ meets the $x$-axis at
$$X=x_0-\frac{y_0}{m}=x_0+y_0^{2/3}x_0^{1/3}=x_0^{1/3}\big(x_0^{2/3}+y_0^{2/3}\big)=x_0^{1/3},$$
and by the symmetric computation it meets the $y$-axis at $Y=y_0^{1/3}$. The part of the line in the first quadrant is the segment between $(X,0)$ and $(0,Y)$, of length $\sqrt{X^2+Y^2}=\sqrt{x_0^{2/3}+y_0^{2/3}}=1$.
:::
