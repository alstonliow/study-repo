<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-14-q1" status="draft"}
**(a)** Complexify: $\dot z+2z=e^{(3+4i)t}$. By the exponential response formula with $p(s)=s+2$, $z_p=\dfrac{e^{(3+4i)t}}{5+4i}=\dfrac{5-4i}{41}e^{3t}(\cos4t+i\sin4t)$. Its real part gives
$$x=\frac{e^{3t}}{41}\left(5\cos4t+4\sin4t\right)+Ce^{-2t}.$$

**(b)** $p(i)=-1+i+2=1+i$, so $x_p=\operatorname{Re}\dfrac{e^{it}}{1+i}=\operatorname{Re}\dfrac{(1-i)(\cos t+i\sin t)}2=\tfrac12\cos t+\tfrac12\sin t=\tfrac1{\sqrt2}\cos(t-\tfrac\pi4)$ (@exm-exponential-response). The characteristic roots are $-\tfrac12\pm\tfrac{\sqrt7}2i$, so
$$x=\tfrac12\cos t+\tfrac12\sin t+e^{-t/2}\left(c_1\cos\tfrac{\sqrt7}2t+c_2\sin\tfrac{\sqrt7}2t\right).$$

**(c)** The predicted pseudo-period is $2\pi/(\sqrt7/2)=4\pi/\sqrt7\approx4.75$.

**(d)** Amplitude $1/\sqrt2\approx0.707$, $x_p(0)=\tfrac12$, $\dot x_p(0)=\tfrac12$.

**(e)** $x_h$ must cancel $x_p$ at $t=0$: $x_h(0)=-\tfrac12$, $\dot x_h(0)=-\tfrac12$. With $\omega=\tfrac{\sqrt7}2$ and $x_h=e^{-t/2}(c_1\cos\omega t+c_2\sin\omega t)$: $c_1=-\tfrac12$ and $-\tfrac12c_1+\omega c_2=-\tfrac12$, so $c_2=-\tfrac3{4\omega}=-\tfrac{3}{2\sqrt7}$. Thus
$$x_h=-e^{-t/2}\left(\tfrac12\cos\tfrac{\sqrt7}2t+\tfrac3{2\sqrt7}\sin\tfrac{\sqrt7}2t\right).$$
:::
