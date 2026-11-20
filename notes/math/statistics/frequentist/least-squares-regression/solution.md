<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1805s22-6-q2" status="draft"}
(a) $f(y_1\mid a,b)=\dfrac1{\sigma\sqrt{2\pi}}\exp\Bigl(-\dfrac{(y_1-ax_1-b)^2}{2\sigma^2}\Bigr)$, and the log-likelihood is $-\ln(\sigma\sqrt{2\pi})-\dfrac{(y_1-ax_1-b)^2}{2\sigma^2}$.

(b) For the three points the log-likelihood is a constant minus $\frac1{18}\sum_i(y_i-ax_i-b)^2$, so the MLE minimises the sum of squared residuals (@prp-least-squares-is-mle). Setting the partial derivatives to $0$ gives the normal equations
$$35a+9b=19,\qquad9a+3b=11 .$$
Solving, $a=-\frac74=-1.75$ and $b=\frac{107}{12}\approx8.92$. (Equivalently, $\bar x=3$, $\bar y=\frac{11}3$, $s_{xx}=8$, $s_{xy}=-14$, so $a=s_{xy}/s_{xx}$ and $b=\bar y-a\bar x$ by @prp-least-squares-slope.) $\sigma$ only scales the sum, so it does not affect the answer.

(c) The plot shows the three points and the line $y=-1.75x+8.92$, which passes through $(\bar x,\bar y)=(3,\frac{11}3)$; the residuals are $\frac5{6},-\frac53,\frac56$.
:::
