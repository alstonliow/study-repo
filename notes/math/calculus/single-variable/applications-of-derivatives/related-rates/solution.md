<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

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

::: {.solution for="prob-mit1801n-2e-q2" status="draft"}
Let $x$ be the distance along the shore from the point nearest the beacon to the spot, and $\theta$ the angle between the beam and the perpendicular to the shore, so $x=4\tan\theta$ and $\frac{d\theta}{dt}=3\cdot2\pi=6\pi$ rad/min. Then $\frac{dx}{dt}=4\sec^2\theta\cdot6\pi$. The beam makes $60^\circ$ with the shore when $\theta=30^\circ$, where $\sec^2\theta=\frac43$. So the spot moves at $4\cdot\frac43\cdot6\pi=32\pi\approx100.5$ miles per minute.
:::

::: {.solution for="prob-mit1801n-2e-q3" status="draft"}
When the second boat is $x=10$ miles east of the crossing, it has spent $\frac13$ hour since crossing, so the first boat, $10$ minutes ahead, is $y=30\cdot\big(\frac13+\frac16\big)=15$ miles north. With $D^2=x^2+y^2$ and $x'=y'=30$: $D'=\frac{xx'+yy'}D=\frac{10\cdot30+15\cdot30}{\sqrt{325}}=\frac{150}{\sqrt{13}}\approx41.6$ miles per hour.
:::

::: {.solution for="prob-mit1801n-2e-q5" status="draft"}
Let $x$ be the horizontal distance from the point under the pulley and $z$ the length of rope from the pulley to the hand: $z^2=x^2+10^2$. The weight rises as fast as $z$ grows: $z'=4$. Then $xx'=zz'$; at $x=20$, $z=\sqrt{500}=10\sqrt5$, so $x'=\frac{10\sqrt5\cdot4}{20}=2\sqrt5\approx4.47$ feet per second.
:::

::: {.solution for="prob-mit1801n-2e-q7" status="draft"}
At depth $h$ each slanted side moves out by $h$, so the water surface has width $\frac12+2h$ and the cross-section has area $h\cdot\frac{\frac12+(\frac12+2h)}2=h^2+\frac h2$. The volume is $V=4\big(h^2+\frac h2\big)$, so $V'=(8h+2)h'$. With $V'=1$ and $h=\frac12$: $6h'=1$, $h'=\frac16$ meter per second.
:::
