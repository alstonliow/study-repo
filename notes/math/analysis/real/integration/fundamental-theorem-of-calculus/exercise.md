::: {.problem #prob-cama1s-4-q2 origin="external" source="cama1s-4-q2"}
Let $f : [0,1] \to \mathbb{R}$ be continuous. Let
$$G(x,t) = \begin{cases} t(x-1), & t \leq x \\ x(t-1), & t \geq x \end{cases}$$
Let $g(x) = \int_0^1 f(t)G(x,t)\,dt$. Show that $g''(x)$ exists for $x \in (0,1)$ and equals $f(x)$.
:::

::: {.problem #prob-cama1s-4-q3 origin="external" source="cama1s-4-q3"}
This question takes you through the construction of bump functions and partitions of unity.

(a) Starting from the function $h : \mathbb{R} \to \mathbb{R}$ defined by $h(x) = \exp(-1/x^2)$ for $x \neq 0$ and $h(0) = 0$ studied before in sheet 3, construct a function $g : \mathbb{R} \to \mathbb{R}$ that is infinitely-differentiable, positive on a given interval $(a,b)$ and zero elsewhere.

(b) ($\star$) Assuming standard results concerning integration, including the fundamental theorem of calculus, construct a function from $\mathbb{R}$ to $\mathbb{R}$ that is infinitely-differentiable, identically 1 on $[-1,1]$ and identically 0 outside $(-2,2)$.

(c) ($\star$) Construct an infinitely-differentiable, non-negative, function $\psi : \mathbb{R} \to \mathbb{R}$ that is identically 0 outside $(-2,2)$, and satisfies
$$\sum_{n=-\infty}^\infty \psi(x - n) = 1, \qquad \text{for all } x \in \mathbb{R}.$$
:::

::: {.problem #prob-cama1s-4-q13 origin="external" source="cama1s-4-q13"}
Let $I_n(\theta) = \int_{-1}^1(1 - x^2)^n\cos(\theta x)\,dx$. Prove that
$$\theta^2I_n = 2n(2n-1)I_{n-1} - 4n(n-1)I_{n-2}$$
for $n \geq 2$, and hence that
$$\theta^{2n+1}I_n(\theta) = n!\big(P_n(\theta)\sin\theta + Q_n(\theta)\cos\theta\big),$$
where $P_n$ and $Q_n$ are polynomials of degree at most $2n$ with integer coefficients. Deduce that $\pi$ is irrational.
:::
