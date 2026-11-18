<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-4-q1" status="draft"}
a) The equations of @thm-least-squares-line-calculus are $\big(\sum x_i^2\big)a+\big(\sum x_i\big)b=\sum x_iy_i$ and $\big(\sum x_i\big)a+nb=\sum y_i$, so
$$A=\begin{pmatrix}x*x'&x*u'\\x*u'&u*u'\end{pmatrix},\qquad r=\begin{pmatrix}x*y'\\u*y'\end{pmatrix}$$
(in Matlab: `A = [x*x', x*u'; x*u', u*u']`, `r = [x*y'; u*y']`, `z = A\r`).

c) Here $A=\begin{pmatrix}55&15\\15&5\end{pmatrix}$, $r=\begin{pmatrix}198.27\\42.269\end{pmatrix}$, giving $a\approx7.146$, $b\approx-12.985$. The errors $y_i-(ax_i+b)$ are about $5.96,\ -0.84,\ -7.00,\ -7.34,\ 9.21$; the worst is $9.21$ (in 2005).

d) Fitting a line to $(x_i,\ln y_i)$: $a_1\approx1.3955$, $b_1\approx-3.5636$. The errors $y_i-e^{b_1}e^{a_1x_i}$ are about $0.011,\ 0.008,\ -0.413,\ 0.738,\ 1.581$; the worst is $1.58$ (in 2005), much better than the linear fit.

f) $x=6$: $e^{b_1+6a_1}\approx123$ million iPods in 2006. $x=15$: $e^{b_1+15a_1}\approx3.5\times10^7$ million, i.e. $3.5\times10^{13}$ iPods, more than 5000 per person on Earth. Exponential growth cannot go on for long; the actual 2006 figure, 46.4 million, is already far below the prediction.
:::

::: {.solution for="prob-mit1802n-2g-q1" status="draft"}
Minimise $D(a,b)=\sum(y_i-ax_i-b)^2$: $D_a=-2\sum x_i(y_i-ax_i-b)=0$, $D_b=-2\sum(y_i-ax_i-b)=0$ (@thm-least-squares-line-calculus).

a) $D=(0-b)^2+(2-b)^2+(3-a-b)^2$. $D_a=-2(3-a-b)=0$, $D_b=-2b-2(2-b)-2(3-a-b)=0$: $a+b=3$ and $a+3b=5$, so $b=1$, $a=2$: $y=2x+1$. (The line passes through $(1,3)$ and through $(0,1)$, the average of the two points with $x=0$.)

b) $D=b^2+(2-a-b)^2+(1-2a-b)^2$. $D_a=0$: $5a+3b=4$; $D_b=0$: $3a+3b=3$. So $a=b=\frac12$: $y=\frac12(x+1)$.
:::

::: {.solution for="prob-mit1802n-2g-q4" status="draft"}
Minimise $D=\sum_i(z_i-a-bx_i-cy_i)^2$. Setting $D_a=D_b=D_c=0$:
$$\begin{aligned}na+\Big(\sum x_i\Big)b+\Big(\sum y_i\Big)c&=\sum z_i,\\\Big(\sum x_i\Big)a+\Big(\sum x_i^2\Big)b+\Big(\sum x_iy_i\Big)c&=\sum x_iz_i,\\\Big(\sum y_i\Big)a+\Big(\sum x_iy_i\Big)b+\Big(\sum y_i^2\Big)c&=\sum y_iz_i .\end{aligned}$$
:::
