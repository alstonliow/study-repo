<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-13-q1" status="draft"}
**(a)** $p(s)=\tfrac12s^2+\tfrac32s+\tfrac58$. Multiplying by $8$: $4s^2+12s+5=(2s+1)(2s+5)$, so the roots are $-\tfrac12$ and $-\tfrac52$ (overdamped).

**(b)** $x=c_1e^{-t/2}+c_2e^{-5t/2}$ with $c_1+c_2=x_0$ and $-\tfrac12c_1-\tfrac52c_2=\dot x_0$. Solving:
$$x(t)=\frac{5x_0+2\dot x_0}{4}\,e^{-t/2}-\frac{x_0+2\dot x_0}{4}\,e^{-5t/2}.$$

**(c)** Exactly when one coefficient vanishes: $\dot x_0=-\tfrac52x_0$ (only the fast mode) or $\dot x_0=-\tfrac12x_0$ (only the slow mode). These are the two lines through the origin in the initial-condition box.

**(d)** Let $x_0>0$ and write $c_1,c_2$ for the coefficients in (b). Then $x(t)=0$ means $e^{2t}=-c_2/c_1$, which has a solution $t>0$ exactly when $-c_2/c_1>1$.

1. If $c_1>0$ this needs $x_0+2\dot x_0>5x_0+2\dot x_0$, which is impossible.
2. If $c_1<0$, i.e. $\dot x_0<-\tfrac52x_0$, then $x_0+2\dot x_0<5x_0+2\dot x_0<0$, so the ratio is greater than $1$.
3. ($c_1=0$ gives a pure exponential, which never vanishes.)

So the door swings through exactly when $\dot x_0<-\tfrac52x_0$; for $x_0=0.25$ this is $\dot x_0<-0.625$.
:::

::: {.solution for="prob-mit1803ps-13-q2" status="draft"}
**(a)** The roots are equal when $b^2=4mk=4\cdot\tfrac12\cdot\tfrac58=\tfrac54$, i.e. $b=\tfrac{\sqrt5}2\approx1.118$. The double root is $-b/(2m)=-\tfrac{\sqrt5}2$, and the general solution is $x=(c_1+c_2t)e^{-\sqrt5\,t/2}$.

**(b)** $p(s)=\tfrac12s^2+\tfrac14s+\tfrac58$, i.e. $s^2+\tfrac12s+\tfrac54=0$, with roots $-\tfrac14\pm\tfrac{\sqrt{19}}4i\approx-0.25\pm1.09i$. The general solution is
$$x=e^{-t/4}\left(c_1\cos\tfrac{\sqrt{19}}4t+c_2\sin\tfrac{\sqrt{19}}4t\right).$$

**(c)** Every solution is $Ae^{-t/4}\cos(\omega_dt-\phi)$ with $\omega_d=\tfrac{\sqrt{19}}4$ (@prp-damped-solutions), so its zeros are where $\cos(\omega_dt-\phi)=0$: equally spaced, $\pi/\omega_d=\tfrac{4\pi}{\sqrt{19}}\approx2.88$ apart. The door oscillates at the same rate as it comes to rest (only the amplitude shrinks). The pseudo-period is $2\pi/\omega_d=\tfrac{8\pi}{\sqrt{19}}\approx5.77$. Different initial conditions change $A$ and $\phi$ but not the spacing $\approx2.88$ between successive zeros.
:::
