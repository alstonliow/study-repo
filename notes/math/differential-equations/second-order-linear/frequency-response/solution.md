<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-19-q1" status="draft"}
The applet uses unit mass, so driving through the spring gives $\ddot x+b\dot x+kx=ky$ (see the remark on driving through the spring in @sec-math-differential-equations-second-order-linear-frequency-response).

**(b)** Complexify with $y=e^{i\omega t}$: $z_p=\dfrac{k}{k-\omega^2+ib\omega}e^{i\omega t}$, so the complex gain is
$$H(\omega)=\frac{k}{k-\omega^2+ib\omega},\qquad g(\omega)=|H(\omega)|=\frac{k}{\sqrt{(k-\omega^2)^2+b^2\omega^2}},\qquad \tan\phi=\frac{b\omega}{k-\omega^2}.$$

**(a)** For $b=0.5$, $k=4$, $\omega=2$: $H=\dfrac{4}{i}=-4i$, so the gain is $4$ and the phase lag is $\pi/2$; the time lag is $\phi/\omega=\pi/4\approx0.785$.
:::

::: {.solution for="prob-mit1803ps-19-q2" status="draft"}
**(a)** $g(\omega)=4/\sqrt{h(\omega^2)}$ with $h(u)=(4-u)^2+\tfrac14u$. Then $h'(u)=-2(4-u)+\tfrac14=0$ at $u=3.875$, so $\omega_r=\sqrt{3.875}\approx1.969$, slightly below $2$ (as @thm-practical-resonance predicts for driving at the mass; the numerator $k$ is constant, so the same calculation applies). The maximal gain is $4/\sqrt{0.125^2+0.25\cdot3.875}=4/\sqrt{0.984375}\approx4.032$, barely more than $g(2)=4$.

**(b)** $\phi=45^\circ$ means $\tan\phi=1$: $0.5\,\omega=4-\omega^2$, so $\omega^2+0.5\omega-4=0$ and $\omega=\tfrac{-0.5+\sqrt{16.25}}2\approx1.766$.

**(c)** The Nyquist plot starts at $H(0)=1$ on the positive real axis, swings clockwise through the lower half plane (through $-4i$ at $\omega=2$) and returns to $0$ from the left as $\omega\to\infty$. At $\omega\approx1.766$ the point $H$ lies on the ray at angle $-\pi/4$, at distance $g\approx3.20$ from $0$.

**(d)** $H(\omega)=\dfrac{k}{k-\omega^2+ib\omega}$. A phase lag of $\pi/2$ means $H$ is a negative imaginary number, i.e. $k-\omega^2+ib\omega$ is purely imaginary: $k-\omega^2=0$, so $\omega=\sqrt k$, whatever $b$ is. That is why, at $\omega=2$, $k=4$, the strut stays on the negative imaginary axis while $b$ changes only its length $k/(b\omega)$.
:::

::: {.solution for="prob-mit1803ps-20-q1" status="draft"}
Complexify $V=\operatorname{Im}(V_0e^{i\omega t})$. Then $\dot V=\operatorname{Im}(i\omega V_0e^{i\omega t})$ and the exponential response formula gives
$$I_p=\operatorname{Im}\frac{i\omega V_0e^{i\omega t}}{-L\omega^2+iR\omega+1/C}=\operatorname{Im}\frac{V_0e^{i\omega t}}{Z},\qquad Z=R+i\left(\omega L-\frac1{\omega C}\right)$$
(@def-complex-impedance).

**(b)** $I$ is in phase with $V$ exactly when $Z$ is real: $\omega L=\dfrac1{\omega C}$, i.e. $\omega^2LC=1$. $R$ and $V_0$ do not matter.

**(a)** With $L=0.5$ H and $\omega=200$: $C=\dfrac1{\omega^2L}=\dfrac1{40000\cdot0.5}=5\times10^{-5}$ F $=50\ \mu$F, with any $R$ and $V_0$.

**(c)–(d)** The amplitude of $I$ is $V_0/|Z|$ with $|Z|^2=R^2+(\omega L-1/(\omega C))^2\ge R^2$, with equality exactly at $\omega=1/\sqrt{LC}$. There the amplitude is $V_0/R$ and the phase lag $\arg Z$ is $0$. For $R=100$, $L=1$, $C=10^{-4}$: $\omega=100$ rad/s, amplitude $500/100=5$ A, phase lag $0$.
:::

::: {.solution for="prob-mit1803ps-20-q2" status="draft"}
**(a)** $RE'=\operatorname{Re}(i\omega RE_0e^{i\omega t})$, and $p(i\omega)=-L\omega^2+iR\omega+1/C$. Dividing numerator and denominator by $i\omega$:
$$V_R=\operatorname{Re}\frac{RE_0e^{i\omega t}}{R+i(\omega L-\frac1{\omega C})}=A(\omega)\cos(\omega t-\phi),$$
$$A(\omega)=\frac{RE_0}{\sqrt{R^2+\left(\omega L-\frac1{\omega C}\right)^2}},\qquad \tan\phi=\frac{\omega L-1/(\omega C)}{R}.$$

**(b)** The amplitude response has one peak, at $\omega_0=1/\sqrt{LC}$, of height $E_0$ (gain $1$). Increasing $L$ or $C$ moves the peak to lower frequencies; increasing $R$ widens and flattens the peak without moving it.

**(c)** Put the peak at $\omega_1=1$: for example $L=1$, $C=1$ and small $R$, say $R=0.1$. The gain at $\omega_2=4$ is then $0.1/\sqrt{0.01+(4-\tfrac14)^2}\approx0.027$, so the $\omega_2$ component is almost removed. A smaller $R$ gives a narrower peak and a sharper filter; a larger $R$ lets more of $\omega_2$ through.

**(d)** With $L$ and $R$ fixed, changing $C$ moves the peak $\omega_0=1/\sqrt{LC}$ along the frequency axis while its height stays $1$ and other frequencies are damped. Turning a variable capacitor therefore selects which carrier frequency, i.e. which station, passes through: that is tuning.

**(e)** With $R=0$ and no input the equation is $LV''+V/C=0$, whose solutions oscillate at $\omega_0=1/\sqrt{LC}$. With $R>0$, the formula in (a) shows $A(\omega)\le RE_0/\sqrt{R^2}=E_0$, with equality exactly when $\omega L=1/(\omega C)$, i.e. $\omega=\omega_0$. So the maximum of $A$ is at $\omega_0$ for every $R>0$.
:::
