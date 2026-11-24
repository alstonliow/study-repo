<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-30-q1" status="draft"}
By @prp-transfer-weight, $w=\mathcal L^{-1}(1/p(s))$ (times $u(t)$).

**(a)** $\dfrac1{3s^2+6s+6}=\dfrac13\cdot\dfrac1{(s+1)^2+1}$, so $w=\tfrac13u(t)e^{-t}\sin t$.

**(b)** $\dfrac1{s^4-1}=\dfrac12\left(\dfrac1{s^2-1}-\dfrac1{s^2+1}\right)=\dfrac14\left(\dfrac1{s-1}-\dfrac1{s+1}\right)-\dfrac12\cdot\dfrac1{s^2+1}$, so
$$w=u(t)\left(\tfrac14e^t-\tfrac14e^{-t}-\tfrac12\sin t\right).$$
:::

::: {.solution for="prob-mit1803ps-31-q1" status="draft"}
**(a)** By @thm-poles-long-term, each pole $r$ contributes terms $t^je^{rt}$ (higher powers of $t$ only for repeated poles).

(1) $f=c_1e^t+(\text{polynomials})\cdot\cos t,\sin t$ terms: it grows like $e^t$ (since the pole $1$ is present), with an oscillation of period $2\pi$ superimposed. Examples: $f=e^t+\cos t$, $F=\dfrac1{s-1}+\dfrac s{s^2+1}$; $f=e^t-\sin t$, $F=\dfrac1{s-1}-\dfrac1{s^2+1}$.

(2) $f=e^{-t}(c_1\cos4t+c_2\sin4t)$ (times polynomials for repeated poles): a decaying oscillation with pseudo-period $\pi/2$, tending to $0$. Examples: $e^{-t}\cos4t$, $F=\dfrac{s+1}{(s+1)^2+16}$; $e^{-t}\sin4t$, $F=\dfrac4{(s+1)^2+16}$.

(3) $f=q(t)e^{-t}$ with $q$ a polynomial: no oscillation, decays to $0$. Examples: $e^{-t}$, $F=\dfrac1{s+1}$; $te^{-t}$, $F=\dfrac1{(s+1)^2}$.

(4) $F$ has no poles, so it is not a proper rational function unless $F=0$; among the transforms we use, $f$ is then a combination of delta functions (zero except at isolated instants). Examples: $f=\delta(t)$, $F=1$; $f=\delta(t-1)$, $F=e^{-s}$.

**(b)**

(i) By the s-shift, $W(s)=\mathcal L(w)=\dfrac{3/2}{(s+\frac12)^2+\frac94}=\dfrac{3/2}{s^2+s+\frac52}$. So $W=1/p$ with characteristic polynomial $p(s)=\tfrac23s^2+\tfrac23s+\tfrac53$ (that is $m=\tfrac23$, $b/m=1$, $k/m=\tfrac52$).

(ii) The poles are $-\tfrac12\pm\tfrac32i$, in the left half-plane.

(iii) By @thm-practical-resonance, $\omega_r=\sqrt{k/m-b^2/(2m^2)}=\sqrt{\tfrac52-\tfrac12}=\sqrt2\approx1.41$: avoid circular frequencies near $\sqrt2$.

(iv) With $b=1$, $k=2.5$ the amplitude response $|W(i\omega)|$ peaks at $\omega=\sqrt2$. The 3D window shows the surface $|W(s)|$ over the $s$-plane: it rises to infinite spikes above the two poles, and its slice along the imaginary axis $s=i\omega$ is the amplitude response curve. The colour coding of the individual features cannot be checked now that the applet no longer runs.
:::
