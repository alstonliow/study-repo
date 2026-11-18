<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit1801f06-4-q6" status="draft"}
a) The line $y=y_0+m_0(x-x_0)$ (with $m_0<0$, so that it cuts off a segment in the first quadrant) meets the axes at $\big(x_0-\frac{y_0}{m_0},0\big)$ and $(0,y_0-m_0x_0)$. So
$$L^2=\Big(x_0-\frac{y_0}{m_0}\Big)^2+(y_0-m_0x_0)^2 .$$

b) Apply (a) at every point $(x,y)$ of the graph with $m_0=y'$:
$$L^2=\Big(x-\frac{y}{y'}\Big)^2+(y-xy')^2 .$$

c) Write $x-\frac y{y'}=\frac{xy'-y}{y'}$ and $y-xy'=-(xy'-y)$, and note $(xy'-y)'=xy''$. Differentiating, with $L$ constant,
$$0=2\,\frac{xy'-y}{y'}\cdot\frac{xy''\,y'-(xy'-y)\,y''}{y'^2}+2(xy'-y)\cdot xy''=2(xy'-y)\,y''\Big(\frac{y}{y'^3}+x\Big).$$
So $\Big(x+\dfrac{y}{y'^3}\Big)(xy'-y)\,y''=0$.

d) On $x^{2/3}+y^{2/3}=L^{2/3}$, implicit differentiation gives $y'=-(y/x)^{1/3}$, so $y'^3=-y/x$ and $x+\frac y{y'^3}=x-x=0$: the equation holds. It also satisfies $f(0)=L$, $f(L)=0$, and (b) holds by the computation of @prob-mit1801f06-3-q2 scaled by $L$.

$y''=0$ means a straight line; but then each "tangent line" is the line itself, and $f(0)=L$, $f(L)=0$ force $y=L-x$, whose first-quadrant part has length $L\sqrt2\ne L$. So (b) fails: differentiating (b) introduced solutions of (c) that are not solutions of (b). $xy'-y=0$ means $y=cx$, a line through the origin, which cannot have $f(0)=L>0$ (and its first-quadrant part is unbounded). So the hypocycloid (astroid) is the only solution.
:::
