<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-7-q6" status="draft"}
Put $u=2x+5y-3$, $v=3x-7y+8$. Then $\dfrac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}2&5\\3&-7\end{vmatrix}=-29$, so $du\,dv=29\,dx\,dy$ (@thm-change-of-variables), and the ellipse becomes the unit disk $u^2+v^2<1$:
$$\text{area}=\iint dx\,dy=\frac1{29}\iint_{u^2+v^2<1}du\,dv=\frac\pi{29}.$$
:::

::: {.solution for="prob-mit1802n-3d-q7" status="draft"}
1. Jacobian: $\dfrac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}y&x\\-y/x^2&1/x\end{vmatrix}=\dfrac{2y}x=2v$, so $dx\,dy=\dfrac{du\,dv}{2v}$.

2. Integrand: $x^2=u/v$ and $y^2=uv$, so $x^2+y^2=\dfrac uv+uv$.

3. Region $1\le x\le2$, $0\le y\le1/x$: here $0\le u\le1$, and since $x^2=u/v$, the lines $x=1$ and $x=2$ become $v=u$ and $v=u/4$. For fixed $u$, $v$ runs from $u/4$ to $u$ (the other order would split into two pieces):
$$I_0=\int_0^1\!\!\int_{u/4}^u\Big(\frac uv+uv\Big)\frac{1}{2v}\,dv\,du\ \Big(=\frac{13}8\Big).$$
:::

::: {.solution for="prob-mit1802n-3d-q1" status="draft"}
The sides become $v=1$ and $v=4$; the lines $y=x/3$ and $y=(x-7)/3$ become $u=0$ and $u=7$. $\dfrac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}1&-3\\2&1\end{vmatrix}=7$, so $dx\,dy=\frac17du\,dv$ and
$$\iint_R\frac{x-3y}{2x+y}\,dx\,dy=\frac17\int_1^4\!\!\int_0^7\frac uv\,du\,dv=\frac17\cdot\frac{49}2\cdot\ln4=7\ln2 .$$
:::

::: {.solution for="prob-mit1802n-3d-q2" status="draft"}
Use $u=x-y$, $v=x+y$ (Example 2 of Notes CV): $\dfrac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}1&-1\\1&1\end{vmatrix}=2$, so $dx\,dy=\frac12du\,dv$. The sides $y=0$, $y=x$, $x+y=2$ become $u=v$, $u=0$, $v=2$: the triangle $0\le u\le v\le2$.
$$\frac12\int_0^2\!\!\int_0^v\cos\frac uv\,du\,dv=\frac12\int_0^2v\sin1\,dv=\sin1 .$$
:::

::: {.solution for="prob-mit1802n-3d-q3" status="draft"}
$dx\,dy=\frac12du\,dv$, and the region $x^2+4y^2\le16$ becomes the disc $u^2+v^2\le16$:
$$V=\frac12\iint_{u^2+v^2\le16}(16-u^2-v^2)\,du\,dv=\frac12\cdot2\pi\int_0^4(16-r^2)\,r\,dr=\pi(128-64)=64\pi .$$
:::

::: {.solution for="prob-mit1802n-3d-q4" status="draft"}
$\dfrac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}1&1\\2&-3\end{vmatrix}=-5$, so $dx\,dy=\frac15du\,dv$. The vertices $(0,0),(2,0),(0,-\frac43)$ go to $(0,0),(2,4),(-\frac43,4)$: the $x$-axis becomes $v=2u$, the $y$-axis $v=-3u$, the third side $v=4$. So for $0\le v\le4$, $-\frac v3\le u\le\frac v2$:
$$\frac15\int_0^4\!\!\int_{-v/3}^{v/2}u^2v^2\,du\,dv=\frac1{15}\Big(\frac18+\frac1{27}\Big)\int_0^4v^5\,dv=\frac1{15}\cdot\frac{35}{216}\cdot\frac{4096}6=\frac{1792}{243}\approx7.37 .$$
:::
