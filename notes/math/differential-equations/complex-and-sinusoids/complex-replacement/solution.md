<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-8-q1" status="draft"}
**(a)** $\dfrac1{\sqrt3+i}=\dfrac{\sqrt3-i}{4}$, so the real part of $\dfrac{\sqrt3-i}4(\cos3t+i\sin3t)$ is $\dfrac{\sqrt3}4\cos3t+\dfrac14\sin3t$. Its amplitude is $\sqrt{3/16+1/16}=\tfrac12$ and its phase lag is $\arg(\sqrt3+i)=\pi/6$, so it equals $\tfrac12\cos(3t-\pi/6)$.

By the second method, $\sqrt3+i=2e^{i\pi/6}$, so $\dfrac{e^{3it}}{2e^{i\pi/6}}=\tfrac12e^{i(3t-\pi/6)}$: $B=\tfrac12$, $\phi=\pi/6$, and the real part is $\tfrac12\cos(3t-\pi/6)$ again.

**(b)** Substituting $z=we^{2it}$: $(2i+3)we^{2it}=e^{2it}$, so $w=\dfrac1{3+2i}=\dfrac{3-2i}{13}$. The general solution is $z=\dfrac{3-2i}{13}e^{2it}+Ce^{-3t}$ (complex $C$).

**(c)** The equation is the real part of (b) (@def-complex-replacement), so $x_p=\operatorname{Re}\dfrac{(3-2i)(\cos2t+i\sin2t)}{13}=\dfrac{3\cos2t+2\sin2t}{13}$. The general solution is $x=\dfrac{3\cos2t+2\sin2t}{13}+Ce^{-3t}$ (real $C$).
:::
