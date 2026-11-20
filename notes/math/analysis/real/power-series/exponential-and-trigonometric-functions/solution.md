<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cama1s-4-q8" status="draft"}
(a)

1. If $a = 0$ there is nothing to prove. Otherwise, for $n > |a|$ we have $1 + a/n > 0$. The mean value theorem for $\log(1+x)$ on the interval between $0$ and $a/n$ gives $\xi_n$ between $0$ and $a/n$ with $\log(1 + a/n) = \frac an\cdot\frac{1}{1 + \xi_n}$.

2. So $n\log(1 + a/n) = a/(1 + \xi_n) \to a$, because $|\xi_n| \le |a|/n \to 0$.

3. $\exp$ is continuous, so $(1 + a/n)^n = \exp(n\log(1 + a/n)) \to e^a$.

(b) The limit is $\log a$. Write $a^{1/n} = e^{y_n}$ with $y_n = (\log a)/n$. By the mean value theorem for $\exp$, $e^{y_n} - 1 = y_ne^{\eta_n}$ with $\eta_n$ between $0$ and $y_n$. So $n(a^{1/n} - 1) = (\log a)e^{\eta_n} \to \log a$.
:::

::: {.solution for="prob-cama1s-4-q9" status="draft"}
(a) By the quotient rule, where $\cos x \ne 0$: $\tan' x = \dfrac{\cos^2x + \sin^2x}{\cos^2x} = \dfrac{1}{\cos^2x} = 1 + \tan^2x$.

(b)

1. On $(-\pi/2, \pi/2)$, $\cos > 0$, so $\tan$ is differentiable there with $\tan' > 0$; it is strictly increasing and continuous.

2. As $x \to \pi/2$ from below, $\sin x \to 1$ and $\cos x \to 0^+$, so $\tan x \to +\infty$; similarly $\tan x \to -\infty$ as $x \to -\pi/2$. By the intermediate value theorem $\tan$ maps $(-\pi/2, \pi/2)$ bijectively onto $\mathbb{R}$.

3. By the inverse function theorem, $\tan^{-1} : \mathbb{R} \to (-\pi/2, \pi/2)$ is differentiable with $(\tan^{-1})'(y) = \dfrac{1}{1 + \tan^2(\tan^{-1}y)} = \dfrac{1}{1 + y^2}$.

(c)

1. The series for $g$ has radius of convergence $1$, so it can be differentiated term by term on $(-1,1)$: $g'(x) = 1 - x^2 + x^4 - \cdots = \dfrac{1}{1 + x^2}$ (a geometric series with ratio $-x^2$).

2. So $h = g - \tan^{-1}$ has $h' = 0$ on $(-1,1)$, and by the mean value theorem $h$ is constant there.

3. $h(0) = 0 - 0 = 0$, so $\tan^{-1}x = g(x)$ for $|x| < 1$.
:::
