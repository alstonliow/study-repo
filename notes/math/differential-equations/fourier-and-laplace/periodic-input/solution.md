<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-23-q1" status="draft"}
From the previous problem, $g(t)=\dfrac4\pi\displaystyle\sum_{n\text{ odd}}\frac{(-1)^{(n-1)/2}}{n^2}\sin nt$.

**(a)** If $\omega_0$ is not an odd integer, @thm-periodic-input-response gives, term by term ($p(in)=\omega_0^2-n^2$ is real),
$$x_p(t)=\frac4\pi\sum_{n\text{ odd}}\frac{(-1)^{(n-1)/2}}{n^2(\omega_0^2-n^2)}\sin nt ,$$
which converges, with two derivatives, uniformly since its terms are $O(n^{-4})$.

**(b)** When $\omega_0$ is an odd integer $n$, the input contains $\sin nt$ with a nonzero coefficient and $p(in)=0$: pure resonance (@def-harmonic-resonance). The response to that harmonic contains $t\cos nt$, which is unbounded, and adding homogeneous solutions cannot cancel it; so there is no periodic solution. These are the values $\omega_0=1,3,5,\dots$.

**(c)** $\omega_r=1$. Near it the first term dominates: $x_p\approx\dfrac4\pi\cdot\dfrac{\sin t}{\omega_0^2-1}$. For $\omega_0$ just below $1$ this is a large multiple of $-\sin t$ (out of phase with the input's fundamental); just above $1$ a large multiple of $+\sin t$ (in phase).

**(d)** The homogeneous solutions $c_1\cos\omega_0t+c_2\sin\omega_0t$ have period $2\pi$ exactly when $\omega_0$ is an integer; when it is an even integer there is also no resonance, so $x_p$ plus any homogeneous solution is a $2\pi$-periodic solution: infinitely many. (For a non-integer rational $\omega_0$ these sums are periodic with a longer common period; with period $2\pi$ only $x_p$ works.)

**(e)** Yes: for $\omega_0$ an even integer every solution is $x_p+c_1\cos\omega_0t+c_2\sin\omega_0t$, a sum of $2\pi$-periodic functions.
:::
