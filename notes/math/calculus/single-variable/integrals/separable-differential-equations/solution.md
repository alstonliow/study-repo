<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

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

::: {.solution for="prob-mit1801n-3f-q1" status="draft"}
c) $\sqrt y\,dy=3\,dx$, so $\frac23y^{3/2}=3x+c$ and $y=\big(\frac92x+c'\big)^{2/3}$.

d) For $y\ne0$: $\frac{dy}{y^2}=x\,dx$, so $-\frac1y=\frac{x^2}2+c$ and $y=\frac{-2}{x^2+C}$. Also $y\equiv0$ is a solution (the one lost by dividing, @def-separable-equation).
:::

::: {.solution for="prob-mit1801n-3f-q2" status="draft"}
a) $\frac{dy}y=4x\,dx$: $\ln y=2x^2+c$, $y=Ae^{2x^2}$. From $y(1)=3$, $A=3e^{-2}$, so $y=3e^{2x^2-2}$ and $y(3)=3e^{16}\approx2.67\times10^7$.

e) $e^{-y}dy=dx$: $-e^{-y}=x+c$. From $y(3)=0$: $-1=3+c$, $c=-4$, so $e^{-y}=4-x$ and $y=-\ln(4-x)$. Then $y(0)=-\ln4$. The solution is defined for $x<4$ (it tends to $+\infty$ as $x\to4^-$).
:::

::: {.solution for="prob-mit1801n-3f-q4" status="draft"}
b) Let $D=T-T_e$. Then $D'=-kD$, so $D=D_0e^{-kt}$ (@exm-exponential-growth) and
$$T=T_e+(T_0-T_e)e^{-kt}.$$

c) $k>0$, so $e^{-kt}\to0$ and $T\to T_e$.

d) $D$ goes from $640$ to $160$ in $8$ hours: $e^{-8k}=\frac14$. Cooling to $50^\circ$ means $D=10=\frac{640}{64}=640\big(\frac14\big)^3$, which takes $3\cdot8=24$ hours.
:::

::: {.solution for="prob-mit1801n-3f-q5" status="draft"}
a) $p=e^{-0.13h}$ (in $\mathrm{kg/cm^2}$); at $h=10$: $p=e^{-1.3}\approx0.273$.

b) $h=0.1$ km: $1-e^{-0.013}\approx0.012916\ \mathrm{kg/cm^2}$. With $e^x\approx1+x$, $e^{-0.013}\approx1-0.013$: a drop of about $1.3\%$.

c) $p'(0)=-0.13\,p(0)=-0.13$, so $\Delta p\approx-0.13\times0.1=-0.013$, the same as in (b), found without solving the equation. For Everest, $\Delta h=10$ gives $\Delta p\approx-1.3$, i.e. a pressure of $-0.3$: impossible. The linear approximation is only good for small $\Delta h$.
:::

::: {.solution for="prob-mit1801n-3f-q8" status="draft"}
At $P=(x,y)$ the tangent meets the axes at $\big(x-\frac y{y'},0\big)$ and $(0,y-xy')$. $P$ is the midpoint exactly when $x-\frac y{y'}=2x$ (and then also $y-xy'=2y$), i.e. $y'=-\frac yx$. Separating, $\frac{dy}y=-\frac{dx}x$, so $\ln y=-\ln x+c$ and
$$xy=C\qquad(C>0):$$
the hyperbolas with the axes as asymptotes.
:::
