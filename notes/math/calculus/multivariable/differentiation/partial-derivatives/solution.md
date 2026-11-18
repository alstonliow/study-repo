<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-3-q2" status="draft"}
a) $w_x=yx^{y-1}$ and $w_y=x^y\ln x$, so $\Delta w\approx yx^{y-1}\Delta x+x^y\ln x\,\Delta y$. At $(2,2)$: $w_x=4$, $w_y=4\ln2\approx2.773$. With $\Delta x=-0.02$, $\Delta y=0.01$: $\Delta w\approx-0.08+0.0277=-0.0523$, so $1.98^{2.01}\approx3.948$. The exact value is $3.9473\ldots$, an error of about $0.0005$.

b) More sensitive to $x$: $w_x=4>w_y=4\ln2\approx2.77$, so a change in $x$ changes $w$ about $1.44$ times as much as the same change in $y$.
:::

::: {.solution for="prob-mit1802f07-3-q3" status="draft"}
$f_x=3x^2-y^2-8x+3+2xy$ and $f_y=x^2-2xy=x(x-2y)$.

a), b) At $(1,1.5)$: $f_x=-1.25<0$ and $f_y=-2<0$. At $(1.2,0.6)$: $f_x=-1.2<0$ and $f_y=0$ (there $x=2y$). On the contour plot: at $(1,1.5)$ moving right or up crosses levels towards lower values; at $(1.2,0.6)$ the level curve through the point is horizontal.

d) $f_y=0$ when $x=0$ or $x=2y$. With $x=0$, $f_x=3-y^2=0$ gives $(0,\sqrt3)\approx(0,1.73)$. With $x=2y$, $f_x=15y^2-16y+3=0$ gives $y=\frac{8\pm\sqrt{19}}{15}$: the points $(0.49,0.24)$ and $(1.65,0.82)$. (Second derivatives: $f_{xx}=6x-8+2y$, $f_{xy}=2x-2y$, $f_{yy}=-2x$.)

- $(1.65,0.82)$, $f\approx-0.32$: $AC-B^2<0$, a saddle. Two branches of the level curve $f\approx-0.32$ cross there. Going East or West $f$ goes up ($f_{xx}\approx3.5>0$), going North or South it goes down ($f_{yy}\approx-3.3<0$).
- $(0.49,0.24)$, $f\approx0.66$: $AC-B^2>0$, $f_{xx}<0$, a local maximum. The level curves near it are small closed curves shrinking to the point; $f$ goes down in every direction.
- $(0,1.73)$ on the edge $x=0$: $f(0,y)=0$ for all $y$, so the line $x=0$ is part of the level curve $f=0$, and a second branch of that level curve crosses it at this point (a saddle). Going North or South $f$ stays exactly the same ($0$); going East (into the square) it goes down.
:::

::: {.solution for="prob-mit1802n-2a-q2" status="draft"}
a) $w_x=3x^2y-3y^2$, $w_y=x^3-6xy+4y$.

b) $z_x=\dfrac1y$, $z_y=-\dfrac x{y^2}$.

c) $3\cos(3x+2y)$ and $2\cos(3x+2y)$.

d) $2xy\,e^{x^2y}$ and $x^2e^{x^2y}$.

e) $z_x=\ln(2x+y)+\dfrac{2x}{2x+y}$, $z_y=\dfrac x{2x+y}$.
:::

::: {.solution for="prob-mit1802n-2a-q3" status="draft"}
a) $f_x=mx^{m-1}y^n$, $f_{xy}=mnx^{m-1}y^{n-1}$; $f_y=nx^my^{n-1}$, $f_{yx}=mnx^{m-1}y^{n-1}$.

b) $f_x=\dfrac y{(x+y)^2}$, $f_{xy}=\dfrac{(x+y)-2y}{(x+y)^3}=\dfrac{x-y}{(x+y)^3}$; $f_y=-\dfrac x{(x+y)^2}$, $f_{yx}=-\dfrac{(x+y)-2x}{(x+y)^3}=\dfrac{x-y}{(x+y)^3}$.

c) $f_x=-2x\sin(x^2+y)$, $f_{xy}=-2x\cos(x^2+y)$; $f_y=-\sin(x^2+y)$, $f_{yx}=-2x\cos(x^2+y)$.
:::

::: {.solution for="prob-mit1802n-2a-q5" status="draft"}
a) $w_{xx}=a^2e^{ax}\sin ay$ and $w_{yy}=-a^2e^{ax}\sin ay$; the sum is $0$.

b) $w_x=\dfrac{2x}{x^2+y^2}$, $w_{xx}=\dfrac{2(y^2-x^2)}{(x^2+y^2)^2}$; by symmetry $w_{yy}=\dfrac{2(x^2-y^2)}{(x^2+y^2)^2}$; the sum is $0$ (for $(x,y)\ne(0,0)$).
:::

::: {.solution for="prob-mit1802n-2b-q1" status="draft"}
a) $z_x=y^2=1$, $z_y=2xy=2$: $z=1+(x-1)+2(y-1)$, i.e. $z=x+2y-2$.

b) $w_x=-y^2/x^2=-4$, $w_y=2y/x=4$: $w=4-4(x-1)+4(y-2)$, i.e. $w=-4x+4y$.
:::

::: {.solution for="prob-mit1802n-2b-q3" status="draft"}
$h=\sqrt{x^2+y^2}$, $h_x=x/h$, $h_y=y/h$. At $(3,4)$, $h=5$: $\Delta h\approx\frac35(0.01)+\frac45(0.01)=0.014$.
:::

::: {.solution for="prob-mit1802n-2b-q6" status="draft"}
$V=\pi r^2h$, $\Delta V\approx2\pi rh\,\Delta r+\pi r^2\Delta h=12\pi\,\Delta r+4\pi\,\Delta h$. If both are measured to within $\varepsilon$, $|\Delta V|\lesssim16\pi\varepsilon$, which is at most $0.1$ when $\varepsilon\le\frac{0.1}{16\pi}\approx0.002$. (The volume is three times as sensitive to the radius as to the height: one could instead allow $|\Delta r|\le0.0013$ and $|\Delta h|\le0.004$, splitting the error equally.)
:::

::: {.solution for="prob-mit1802n-2b-q9" status="draft"}
a) $w_x=2x(y+1)=2$ and $w_y=x^2=1$ at $(1,0)$: $w$ is twice as sensitive to $x$.

b) $\Delta w\approx2\Delta x+\Delta y=0$ when $\Delta y/\Delta x=-2$.
:::
