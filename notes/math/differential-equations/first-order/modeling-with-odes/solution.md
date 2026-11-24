<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-1-q1" status="draft"}
**(a)** $a$ is added to $t$, so it is a time: years. The rate $k(t)$ has units $1/\text{year}$ and $(a+t)^2$ has units $\text{year}^2$, so $k_0$ has units of years.

**(b)** $\dfrac{dx}{dt} = \dfrac{k_0}{(a+t)^2}\,x$.

**(c)**

1. $x=0$ is a solution (the one lost when dividing by $x$).
2. Where $x\neq0$, separate: $\dfrac{dx}{x} = \dfrac{k_0\,dt}{(a+t)^2}$, so $\ln|x| = -\dfrac{k_0}{a+t} + c$.
3. Hence $|x| = e^c e^{-k_0/(a+t)}$, and since a solution cannot change sign (it would have to pass through the solution $x=0$), $x = C e^{-k_0/(a+t)}$ with $C\neq0$.
4. Together with $x=0$: the general solution is $x = Ce^{-k_0/(a+t)}$, $C\in\mathbb R$, on each of the intervals $t>-a$ and $t<-a$.

**(d)** $x(0)=x_0$ gives $C = x_0e^{k_0/a}$, so $x(t) = x_0\exp\!\left(\dfrac{k_0}{a}-\dfrac{k_0}{a+t}\right)$. As $t\to\infty$ the exponent tends to $k_0/a$: the population stabilizes at $x_0e^{k_0/a}$.
:::
