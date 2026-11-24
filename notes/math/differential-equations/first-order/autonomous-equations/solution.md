<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-10-q1" status="draft"}
**(a)** The model is $\dot y=(1-y)y-a$ with $y$ in kilo-oryx (taking the natural growth rate as $1$ per year). Without hunting it is logistic with stable population $1$; hunting removes animals at a constant rate $a$ (kilo-oryx per year) whatever the population, which is the term $-a$.

**(b)** Critical points solve $y^2-y+a=0$: $y_\pm=\tfrac12\left(1\pm\sqrt{1-4a}\right)$ (@exm-logistic-harvesting).

- $a<\tfrac14$: two critical points; $f'(y)=1-2y$ is negative at $y_+$ (stable) and positive at $y_-$ (unstable).
- $a=\tfrac14$: one critical point $y=\tfrac12$, semistable ($f=-(y-\tfrac12)^2\le0$, so solutions above approach it and solutions below move away).
- $a>\tfrac14$: none; $\dot y<0$ everywhere.

**(c)** $a=0.1875=\tfrac3{16}$, so $\sqrt{1-4a}=\tfrac12$ and $y_\pm=\tfrac34,\tfrac14$. The stable population is 750 oryx; below 250 oryx the population crashes.

**(d)** The five behaviours, from top to bottom of the phase line:

1. $y>\tfrac34$: decreases to $\tfrac34$ as $t\to\infty$; going back in time it blows up to $+\infty$ in finite time.
2. $y=\tfrac34$: constant.
3. $\tfrac14<y<\tfrac34$: increases from $\tfrac14$ (as $t\to-\infty$) to $\tfrac34$ (as $t\to\infty$), an S-shaped curve.
4. $y=\tfrac14$: constant.
5. $y<\tfrac14$: decreases from $\tfrac14$ (as $t\to-\infty$) and reaches $0$ (extinction) in finite time, then $-\infty$ in finite time if continued.

**(e)** The equilibria satisfy $(1-y)y-a=0$, so the curve in the $(a,y)$-plane is the parabola $a=y-y^2$.
:::

::: {.solution for="prob-mit1803ps-11-q1" status="draft"}
**(a)** $y_0=\tfrac34$. With $y=u+\tfrac34$: $(1-y)y=(\tfrac14-u)(\tfrac34+u)=\tfrac3{16}-\tfrac12u-u^2$, so
$$\dot u=-\tfrac12u-u^2 .$$
The right side does not involve $t$, and it vanishes at $u=0$.

**(b)** Dropping $u^2$: $\dot u=-\tfrac12u$, with general solution $u=Ce^{-t/2}$. (The coefficient $-\tfrac12$ is $f'(y_0)=1-2y_0$.)

**(c)** Near equilibrium $y\approx\tfrac34+Ce^{-t/2}$. If $y(10)-y_0=b$, each unit of time multiplies the excess by $e^{-1/2}$: $y(11)\approx\tfrac34+e^{-1/2}b\approx\tfrac34+0.607\,b$ and $y(12)\approx\tfrac34+e^{-1}b\approx\tfrac34+0.368\,b$.

**(d)** The rate $\dot x=q(t)-p(t)x$ must be a function of $x$ alone, for every $x$. Taking $x=0$ shows $q$ is constant, and then $p$ is constant too.
:::
