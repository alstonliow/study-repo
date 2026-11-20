::: {.problem #prob-mit1801f06-4-q1 origin="external" source="mit1801f06-4-q1"}
a) Use the mean value property to show that if $f(0)=0$ and $f'(x)\ge0$, then $f(x)\ge0$ for all $x\ge0$.

b) Deduce from part (a) that $\ln(1+x)\le x$ for $x\ge0$. Hint: Use $f(x)=x-\ln(1+x)$.

c) Use the same method as in (b) to show $\ln(1+x)\ge x-x^2/2$ and $\ln(1+x)\le x-x^2/2+x^3/3$ for $x\ge0$.

d) Find the pattern in (b) and (c) and make a general conjecture.

e) Show that $\ln(1+x)\le x$ for $-1<x\le0$. (Use the change of variable $u=-x$.)
:::

::: {.problem #prob-mit1801n-2g-q1 origin="external" source="mit1801n-2g-q1"}
For each of these functions, on the indicated interval, find explicitly the point $c$ whose existence is predicted by the Mean-value Theorem; if there is more than one such $c$, find all of them. Use the form (1).

(b) $\ln x$ on $[1,2]$

*Note (these notes):* Only part (b) was assigned. Form (1) is $\frac{f(b)-f(a)}{b-a}=f'(c)$, as in @thm-mean-value.
:::

::: {.problem #prob-mit1801n-2g-q2 origin="external" source="mit1801n-2g-q2"}
Using the form (2), show that

(b) $\sqrt{1+x}<1+x/2$ if $x>0$.

*Note (these notes):* Only part (b) was assigned. Form (2) is $f(b)=f(a)+f'(c)(b-a)$ for some $c$ between $a$ and $b$.
:::

::: {.problem #prob-mit1801n-2g-q5 origin="external" source="mit1801n-2g-q5"}
a) Suppose $f''(x)$ exists on an interval $I$ and $f(x)$ has a zero at three distinct points $a<b<c$ on $I$. Show there is a point $p$ on $[a,c]$ where $f''(p)=0$.

b) Illustrate part (a) on the cubic $f(x)=(x-a)(x-b)(x-c)$.
:::

::: {.problem #prob-mit1801n-2g-q6 origin="external" source="mit1801n-2g-q6"}
Using the form (2) of the Mean-value Theorem, prove that on an interval $[a,b]$,

a) $f'(x)>0\ \Rightarrow\ f(x)$ increasing;  (b) $f'(x)=0\ \Rightarrow\ f(x)$ constant.

*Note (these notes):* Form (2) is $f(x_2)=f(x_1)+f'(c)(x_2-x_1)$ for some $c$ between $x_1$ and $x_2$.
:::

::: {.problem #prob-cama1s-2-q10 origin="external" source="cama1s-2-q10"}
Let $f : [a,b] \to \mathbb{R}$ be continuous on $[a,b]$ and differentiable on $(a,b)$. Which of the following must be true?

(a) If $f$ is increasing then $f'(x) \geqslant 0$ for all $x \in (a,b)$.

(b) If $f'(x) \geqslant 0$ for all $x \in (a,b)$ then $f$ is increasing.

(c) If $f$ is strictly increasing then $f'(x) > 0$ for all $x \in (a,b)$.

(d) If $f'(x) > 0$ for all $x \in (a,b)$ then $f$ is strictly increasing.
:::

::: {.problem #prob-cama1s-2-q12 origin="external" source="cama1s-2-q12"}
Let $f : \mathbb{R} \to \mathbb{R}$ be differentiable for all $x$. Prove that
$$\lim_{x\to\infty} f'(x) = \ell \implies \lim_{x\to\infty}\frac{f(x)}{x} = \ell.$$
If $f(x)/x \to \ell$ as $x \to \infty$, must $f'(x)$ tend to a limit?
:::

::: {.problem #prob-cama1s-2-q13 origin="external" source="cama1s-2-q13"}
Prove that $2x^5 + 3x^4 + 2x + 16 = 0$ has no real solutions outside $[-2,-1]$ and exactly one inside.
:::

::: {.problem #prob-cama1s-3-q2 origin="external" source="cama1s-3-q2"}
Suppose that $f : \mathbb{R} \to \mathbb{R}$ satisfies $|f(x) - f(y)| \leqslant |x - y|^2$ for all $x, y \in \mathbb{R}$. Show that $f$ is constant.
:::

::: {.problem #prob-cama1s-3-q3 origin="external" source="cama1s-3-q3"}
"Let $f'$ exist on $(a,b)$ and let $c \in (a,b)$. If $c + h \in (a,b)$ then $(f(c+h) - f(c))/h = f'(c + \theta h)$. Let $h \to 0$; then $f'(c + \theta h) \to f'(c)$. Thus $f'$ is continuous at $c$." Explain why this argument is false; at what point does it fail?
:::

::: {.problem #prob-cama1s-3-q5 origin="external" source="cama1s-3-q5"}
Prove Darboux's theorem: if $f : \mathbb{R} \to \mathbb{R}$ is differentiable then $f'$ has the intermediate value property, i.e. $f'$ maps intervals to intervals. (That is to say, if $a < b$ and $f'(a) < z < f'(b)$ then there exists $c$, $a < c < b$, with $f'(c) = z$.)
:::
