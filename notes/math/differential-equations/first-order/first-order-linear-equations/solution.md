<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-4-q1" status="draft"}
**(a)** Let $B(t)$ be the balance in dollars after $t$ years. In a short time $\Delta t$ interest adds about $IB\,\Delta t$ and payments remove $q\,\Delta t$, so $\Delta B\approx(IB-q)\Delta t$; letting $\Delta t\to0$,
$$B' = IB - q,\qquad\text{i.e.}\quad B' - IB = -q .$$

**(b)** The constant $q/I$ is a particular solution and $e^{It}$ solves the homogeneous equation, so $B = \dfrac qI + Ce^{It}$ (@prp-first-order-linear-structure).

**(c)** A constant balance means $C=0$, so $B=q/I$. With $q=12\,000$ dollars per year and $I=0.05$: $B = \$240\,000$.

**(d)** With $B(0)=B_0$, $C = B_0 - q/I$. Setting $B(20)=0$: $\dfrac qI + \left(B_0-\dfrac qI\right)e^{20I}=0$, so
$$B_0 = \frac qI\left(1-e^{-20I}\right) = 240\,000\,(1-e^{-1}) \approx \$151\,708.93 .$$
:::

::: {.solution for="prob-mit1803ps-4-q2" status="draft"}
**(a)** $x$ decays from $1$ to $0$; $y$ rises from $0$, peaks and decays to $0$; $z$ increases from $0$ to $1$. Limits: $x,y\to0$, $z\to1$.

**(b)** $e^{-\sigma t_S}=\tfrac12$ gives $\sigma=\ln2/t_S$, and likewise $\mu=\ln2/t_M$ (so $\sigma=\mu$ here). Half of the decaying St becomes Mi and half En:
$$\dot x=-\sigma x,\qquad \dot y=\tfrac{\sigma}{2}x-\mu y,\qquad \dot z=\tfrac\sigma2x+\mu y .$$
The three right sides add to $0$.

**(c)**

1. $x=e^{-\sigma t}$.
2. $\dot y+\mu y=\tfrac\sigma2e^{-\sigma t}$, $y(0)=0$. With the integrating factor $e^{\mu t}$: if $\sigma\neq\mu$, $y=\dfrac{\sigma}{2(\mu-\sigma)}\left(e^{-\sigma t}-e^{-\mu t}\right)$; if $\sigma=\mu$ (our case), $(e^{\sigma t}y)'=\tfrac\sigma2$, so $y=\tfrac\sigma2\,te^{-\sigma t}$.
3. $z=1-x-y$, since the sum stays $1$: for $\sigma=\mu$, $z=1-e^{-\sigma t}-\tfrac\sigma2te^{-\sigma t}$.

**(d)** For $\sigma\neq\mu$, $\dot y=0$ when $\sigma e^{-\sigma t}=\mu e^{-\mu t}$, i.e. $t=\dfrac{\ln(\mu/\sigma)}{\mu-\sigma}$. For $\sigma=\mu$, $\dot y=\tfrac\sigma2e^{-\sigma t}(1-\sigma t)=0$ at $t=1/\sigma=t_S/\ln2$ (the limit of the general formula).

**(e)** The equations are linear and homogeneous with $y(0)=z(0)=0$, so all three functions are doubled.

**(f)** $q=te^t+2e^t=(t+2)e^t$. In standard form $\dot x+\tfrac2tx=(1+\tfrac2t)e^t$ with integrating factor $t^2$: $(t^2x)'=(t^2+2t)e^t=(t^2e^t)'$, so $x=e^t+Ct^{-2}$ on $t>0$ or $t<0$.
:::
