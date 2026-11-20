::: {.problem #prob-mit1801f06-8b-q1 origin="external" source="mit1801f06-8b-q1"}
a) Use L'Hospital's rule to evaluate
$$\lim_{x\to\infty}x^me^{-x}$$

b) Use part (a) and limit comparison to show that the improper integral $\int_0^\infty x^ne^{-x}\,dx$ converges for $n\ge0$. (Do not integrate by parts.)

c) Denote $A(n)=\int_0^\infty x^ne^{-x}\,dx$. Use integration by parts to find the constant $c_n$ for which
$$A(n+1)=c_nA(n)$$
(Explain what happens at the infinite limit using part (a).)

d) Find $A(0)$ and deduce from part (c) the formula for $A(n)$, $n=0,1,2,\ldots$.

e) (optional; extra credit) Show that the improper integral representing $A(-1/2)$ converges and evaluate it using a change of variables.
:::

::: {.problem #prob-mit1801n-6b-q1 origin="external" source="mit1801n-6b-q1"}
Test the following improper integrals for convergence by using comparison with a simpler integral.

6B-1. $\displaystyle\int_1^\infty\frac{dx}{\sqrt{x^3+5}}$
:::

::: {.problem #prob-mit1801n-6b-q2 origin="external" source="mit1801n-6b-q2"}
Test the following improper integrals for convergence by using comparison with a simpler integral.

6B-2. $\displaystyle\int_0^\infty\frac{x^2dx}{x^3+2}$
:::

::: {.problem #prob-mit1801n-6b-q7 origin="external" source="mit1801n-6b-q7"}
Decide whether the following integrals are convergent or divergent and evaluate if convergent.

a) $\displaystyle\int_0^\infty e^{-8x}dx$  f) $\displaystyle\int_e^\infty\frac{dx}{x(\ln x)^2}$  k) $\displaystyle\int_0^\infty e^{-2x}\cos x\,dx$  m) $\displaystyle\int_0^\infty\frac{dx}{(x+2)^3}$

*Note (these notes):* Parts (a), (f), (k) and (m) were assigned.
:::

::: {.problem #prob-mit1801n-6b-q8 origin="external" source="mit1801n-6b-q8"}
Find the following limits. (Use the fundamental theorem of calculus.)

c) $\displaystyle\lim_{x\to\infty}e^{x^2}\int_0^xe^{-t^2}dt$

*Note (these notes):* Only part (c) was assigned.
:::

::: {.problem #prob-cama1s-4-q5 origin="external" source="cama1s-4-q5"}
Do these improper integrals converge?
$$\text{(i)} \int_1^\infty \sin^2(1/x)\,dx, \qquad \text{(ii)} \int_0^\infty x^p\exp(-x^q)\,dx,$$
where $p, q > 0$. [You may assume familiar results about the continuity and differentiability properties of the exponential and logarithm.]
:::

::: {.problem #prob-cama1s-4-q6 origin="external" source="cama1s-4-q6"}
This question concerns tests for determining convergence of improper integrals over an unbounded domain. Let $f : [a,\infty) \to \mathbb{R}$ be integrable on $[a,R]$ for every $R \geq a$.

(a) (Dirichlet test) Suppose $f$ is continuous. Let $F(x) = \int_a^x f(t)\,dt$ for $x \in [a,\infty)$ and assume $F$ is bounded ($\sup_{x\geq a}|F(x)| < \infty$). Let $g : [a,\infty) \to \mathbb{R}$ be monotone, continuously differentiable, and satisfy $g(x) \to 0$ as $x \to \infty$. Show that the improper integral $\int_a^\infty fg$ converges. Deduce that $\int_1^\infty x^{-1/2}\sin x\,dx$ converges.

(b) (Root test) Suppose $L = \lim_{x\to\infty}|f(x)|^{1/x}$ exists. What can you say about the convergence of the improper integral $\int_a^\infty |f|$ for $L > 1$, $L < 1$ and $L = 1$? ($\star$) What about $\int_a^\infty f$? Justify your answers. [You may assume the familiar properties of the exponential function.]

(c) ($\star$) Does the $n$th term test hold for improper integrals: if $f \geq 0$ and the improper integral $\int_a^\infty f$ converges, must $f(x) \to 0$ as $x \to \infty$? What if $f$ is continuous?
:::
