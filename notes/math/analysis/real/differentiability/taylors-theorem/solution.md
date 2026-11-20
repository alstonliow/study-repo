<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cama1s-3-q7" status="draft"}
(a)

1. On $[-1,1]\setminus\{0\}$, $\varphi$ is a quotient of continuous functions, and differentiable on $(-1,1)\setminus\{0\}$ with $\varphi'(x) = \dfrac{xf'(x) - f(x) + f(0)}{x^2}$.

2. At $0$, $\varphi(x) \to f'(0) = \varphi(0)$ by the definition of $f'(0)$, so $\varphi$ is continuous.

3. $\dfrac{\varphi(h) - \varphi(0)}{h} = \dfrac{f(h) - f(0) - hf'(0)}{h^2}$. Numerator and denominator vanish at $h = 0$, and the quotient of their derivatives is $\dfrac{f'(h) - f'(0)}{2h} \to \dfrac{f''(0)}{2}$. By l'Hôpital's rule, $\varphi'(0) = f''(0)/2$.

(b)

1. Fix $x \ne 0$. Taylor's theorem with Lagrange remainder, expanding $f$ about $x$ and evaluating at $0$, gives $\xi$ strictly between $0$ and $x$ with $f(0) = f(x) - xf'(x) + \frac{x^2}{2}f''(\xi)$.

2. So $xf'(x) - f(x) + f(0) = \frac{x^2}{2}f''(\xi)$ and $\varphi'(x) = \frac12 f''(\xi)$; write $\xi = \theta x$ with $\theta \in (0,1)$. For $x = 0$ any $\theta$ works by (a).

3. $\varphi(1) = f(1) - f(0)$ and $\varphi(-1) = f(0) - f(-1)$. By the mean value theorem for $\varphi$ on $[-1,1]$ there is $\eta \in (-1,1)$ with $\varphi(1) - \varphi(-1) = 2\varphi'(\eta)$, that is, $f(1) + f(-1) - 2f(0) = f''(\theta\eta)$. Take $c = \theta\eta \in (-1,1)$.
:::

::: {.solution for="prob-cama1s-3-q8" status="draft"}
1. *Growth fact.* For every integer $k \ge 0$, $t^k e^{-t^2} \to 0$ as $|t| \to \infty$, since $e^{t^2} \ge t^{2m}/m!$ for every $m$.

2. *Claim.* For $x \ne 0$, $f^{(n)}(x) = p_n(1/x)e^{-1/x^2}$ for a polynomial $p_n$. This holds for $n = 0$ with $p_0 = 1$, and differentiating gives $p_{n+1}(t) = -t^2p_n'(t) + 2t^3p_n(t)$.

3. *Claim.* $f^{(n)}(0) = 0$ and $f^{(n)}$ is continuous at $0$ for all $n$. Continuity: $f^{(n)}(x) = p_n(1/x)e^{-1/x^2} \to 0$ by step 1 with $t = 1/x$. Derivative at $0$: if $f^{(n)}(0) = 0$, then $\dfrac{f^{(n)}(h) - 0}{h} = \frac1h p_n(1/h)e^{-1/h^2} \to 0$ by step 1, so $f^{(n+1)}(0) = 0$. Induction on $n$ proves both.

4. So $f$ is infinitely differentiable on $\mathbb{R}$ and all its derivatives vanish at $0$.

5. Comment: the Taylor series of $f$ at $0$ is identically $0$. It converges everywhere, but to $f(x)$ only at $x = 0$, since $f(x) > 0$ for $x \ne 0$. An infinitely differentiable function need not equal the sum of its Taylor series: the remainder in Taylor's theorem does not tend to $0$ here.
:::
