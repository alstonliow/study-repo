<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-21-q1" status="draft"}
The target $f$ is even, so only cosines are needed. It is also "odd about $\pi/2$": $f(\pi-t)=-f(t)$. Since $\cos n(\pi-t)=(-1)^n\cos nt$, only odd $n$ survive.

**(b)** By @prp-even-odd-fourier, $b_n=0$ and
$$a_n=\frac2\pi\left(\frac\pi4\int_0^{\pi/2}\cos nt\,dt-\frac\pi4\int_{\pi/2}^{\pi}\cos nt\,dt\right)=\frac12\left(\frac{\sin(n\pi/2)}n+\frac{\sin(n\pi/2)}n\right)=\frac{\sin(n\pi/2)}{n},$$
using $\sin n\pi=0$. Also $a_0=0$. So $a_1=1$, $a_3=-\tfrac13$, $a_5=\tfrac15$, $a_7=-\tfrac17,\dots$, and the even ones vanish:
$$f(t)=\cos t-\frac{\cos3t}3+\frac{\cos5t}5-\cdots$$

**(a), (c)** Eyeballed values should be close to these; minimizing the RMS distance one slider at a time lands exactly on them, whatever the order, because the cosines are orthogonal (@thm-fourier-coefficients): the distance is a sum of separate squares, one per coefficient.
:::

::: {.solution for="prob-mit1803ps-22-q1" status="draft"}
Recall $\operatorname{sq}(t)=\dfrac4\pi\displaystyle\sum_{n\text{ odd}}\frac{\sin nt}{n}$.

**(a)** It is already a finite Fourier series: $2\sin(t-\tfrac\pi3)=2\sin t\cos\tfrac\pi3-2\cos t\sin\tfrac\pi3=\sin t-\sqrt3\cos t$.

**(b)** With $L=2\pi$ the frequencies are $n/2$. Since $\operatorname{sq}$ is odd, $a_n=0$ and $b_n=\dfrac1\pi\displaystyle\int_0^{2\pi}\operatorname{sq}(t)\sin\tfrac{nt}2\,dt=\dfrac1\pi\left(\int_0^\pi\sin\tfrac{nt}2\,dt-\int_\pi^{2\pi}\sin\tfrac{nt}2\,dt\right)=\dfrac{2}{n\pi}\left(1-2\cos\tfrac{n\pi}2+\cos n\pi\right)$. This is $0$ for odd $n$ and for $n\equiv0\pmod4$, and $\dfrac{8}{n\pi}$ for $n\equiv2\pmod4$. Writing $n=2m$ with $m$ odd gives $\dfrac{4}{m\pi}\sin mt$: the same series as before. A function has only one Fourier series, and the $4\pi$-periodic view just allows extra frequencies whose coefficients turn out to be zero.

**(c)** $\operatorname{sq}(t-\tfrac\pi4)=\dfrac4\pi\displaystyle\sum_{n\text{ odd}}\frac{\sin(nt-n\pi/4)}{n}=\dfrac4\pi\sum_{n\text{ odd}}\frac{\cos\frac{n\pi}4\sin nt-\sin\frac{n\pi}4\cos nt}{n}$. Minimal period $2\pi$; a square wave switching at $t=\pi/4+k\pi$.

**(d)** $1+2\operatorname{sq}(2\pi t)=1+\dfrac8\pi\displaystyle\sum_{n\text{ odd}}\frac{\sin2\pi nt}{n}$: a wave alternating between $3$ (on $0<t<\tfrac12$) and $-1$. Minimal period $1$.

**(e)** $f(t)=\tfrac\pi4\operatorname{sq}(t+\tfrac\pi2)$. Since $\sin(nt+n\pi/2)=\sin\frac{n\pi}2\cos nt$ for odd $n$,
$f(t)=\displaystyle\sum_{n\text{ odd}}\frac{\sin(n\pi/2)}{n}\cos nt=\cos t-\frac{\cos3t}3+\frac{\cos5t}5-\cdots$, as in the previous problem. Minimal period $2\pi$.

**(f)** $g$ is continuous with slope $+1$ on $(-\tfrac\pi2,\tfrac\pi2)$ and $-1$ on $(\tfrac\pi2,\tfrac{3\pi}2)$, so $g'(t)=\operatorname{sq}(t+\tfrac\pi2)=\dfrac4\pi\displaystyle\sum_{n\text{ odd}}\frac{\sin(n\pi/2)}{n}\cos nt$. Integrating term by term (allowed, @prp-fourier-operations, read backwards) and using that $g$ is odd, so has no constant term:
$$g(t)=\frac4\pi\sum_{n\text{ odd}}\frac{\sin(n\pi/2)}{n^2}\sin nt=\frac4\pi\left(\sin t-\frac{\sin3t}9+\frac{\sin5t}{25}-\cdots\right).$$
A triangle wave between $-\tfrac\pi2$ and $\tfrac\pi2$, minimal period $2\pi$.
:::
