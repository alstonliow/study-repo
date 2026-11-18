<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-10-q10" status="draft"}
1. $x^3-cx$ is odd, so its integrals against the even functions $1$ and $x^2-\frac13$ vanish automatically.

2. Against $x$: $\int_{-1}^1(x^4-cx^2)\,dx=\frac25-\frac{2c}3$, which is $0$ for $c=\frac35$.

3. So the fourth Legendre polynomial (up to scaling) is $x^3-\frac35x$.
:::

::: {.solution for="prob-mit1806s10-10-q11" status="draft"}
1. $\int_0^\pi\cos x\,dx-\int_\pi^{2\pi}\cos x\,dx=0-0=0$.

2. $\int_0^\pi\sin x\,dx-\int_\pi^{2\pi}\sin x\,dx=2-(-2)=4$.

3. $\int_0^\pi\sin2x\,dx-\int_\pi^{2\pi}\sin2x\,dx=0-0=0$.

4. Dividing by $\pi$ (@thm-fourier-coefficients), these give $a_1=0$, $b_1=\frac4\pi$, $b_2=0$.
:::

::: {.solution for="prob-mit1806s10-10-q13" status="draft"}
1. Over a period $[-\pi,\pi]$ (equivalent to $[0,2\pi]$ by periodicity), $a_0=\frac1{2\pi}\int F=\frac1{2\pi}\cdot h\cdot\frac1h=\frac1{2\pi}$.

2. $a_k=\frac1\pi\int_{-h/2}^{h/2}\frac1h\cos kx\,dx=\frac2{\pi hk}\sin\frac{kh}2$.

3. $b_k=\frac1\pi\int_{-h/2}^{h/2}\frac1h\sin kx\,dx=0$, since $F$ is even and $\sin kx$ is odd.

4. As $h\to0$, $\frac{\sin(kh/2)}{kh/2}\to1$, so $a_k\to\frac1\pi$ for every $k\ge1$, $a_0=\frac1{2\pi}$, and $b_k=0$: the delta function has all cosine coefficients equal.
:::
