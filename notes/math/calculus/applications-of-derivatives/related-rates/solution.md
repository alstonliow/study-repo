<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit1801f06-3-q6" status="draft"}
a) The lines are $y_1x+x_1y=x_1y_1$ and $y_2x+x_2y=x_2y_2$. Solving the $2\times2$ system (Cramer's rule),
$$x_3=\frac{x_1x_2(y_1-y_2)}{x_2y_1-x_1y_2},\qquad y_3=\frac{y_1y_2(x_2-x_1)}{x_2y_1-x_1y_2}.$$
Checks: (i) $y_2=0$ gives $x_3=\frac{x_1x_2y_1}{x_2y_1}=x_1$. (ii) Exchanging $x_i\leftrightarrow y_i$ turns the formula for $x_3$ into that for $y_3$ (the denominator only changes sign, as does $y_1-y_2$ versus $x_2-x_1$); the exchange is the reflection in the line $y=x$. (iii) The slopes are $-y_1/x_1$ and $-y_2/x_2$; they are equal exactly when $x_2y_1-x_1y_2=0$. (iv) Numerators have degree $3$, denominators degree $2$.

b) $x_2^2+y_2^2=1$. Since $x^2+y^2=1$ along the motion, $2x\,dx+2y\,dy=0$, so
$$\lim_{\Delta x\to0}\frac{\Delta y}{\Delta x}=\frac{dy}{dx}=-\frac{x_1}{y_1}.$$

c) Substituting, $x_2y_1-x_1y_2=y_1\Delta x-x_1\Delta y$ and $y_1-y_2=-\Delta y$, so
$$x_3=\frac{-x_1(x_1+\Delta x)\,\Delta y/\Delta x}{y_1-x_1\,\Delta y/\Delta x}\ \longrightarrow\ \frac{-x_1^2\,(-x_1/y_1)}{y_1+x_1^2/y_1}=\frac{x_1^3}{x_1^2+y_1^2}=x_1^3 .$$
So $X=x_1^3$, and by the symmetry $x\leftrightarrow y$ of (ii), $Y=y_1^3$.

d) $X^{2/3}+Y^{2/3}=x_1^2+y_1^2=1$.
:::
