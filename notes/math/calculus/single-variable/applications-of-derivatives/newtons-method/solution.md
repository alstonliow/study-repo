<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit1801f06-3-q5" status="draft"}
a) With $f(x)=x^3-9$, @def-newtons-method gives
$$x_{k+1}=x_k-\frac{x_k^3-9}{3x_k^2}=\frac13\Big(2x_k+\frac9{x_k^2}\Big).$$
In double precision (16 digits):

| $k$ | $x_k$ |
|---|---|
| 0 | 2 |
| 1 | 2.083333333333333 |
| 2 | 2.080088888888889 |
| 3 | 2.080083823064241 |
| 4 | 2.080083823051904 |
| 5 | 2.080083823051904 |

To 6 significant figures $9^{1/3}=2.08008$ (already from $k=2$). At $k=4$ the value no longer changes: the method has reached the full accuracy of the computer.

b) $x_0=2$ is smaller than $9^{1/3}$; every later $x_k$ ($k\ge1$) is larger than $9^{1/3}$. $x_1>x_0$, and from then on $x_k<x_{k-1}$ (decreasing towards the root). Reason: $f$ is increasing and concave up for $x>0$. A tangent line of a concave-up graph lies below the graph, so its zero is to the right of the true root whatever the starting point; hence $x_1,x_2,\ldots$ all lie to the right of the root. For $x_k$ to the right of the root, $f(x_k)>0$ and $f'(x_k)>0$, so the step $-f(x_k)/f'(x_k)$ is negative: the iterates decrease (but stay to the right).

c) $9^{1/3}=2(1+\frac18)^{1/3}$, and $(1+x)^{1/3}\approx1+\frac x3-\frac{x^2}9$, so
$$9^{1/3}\approx2\Big(1+\frac1{24}-\frac1{576}\Big)=2.079861.$$
The exact value is $2.080084$, so the difference is about $2.2\times10^{-4}$. A good estimate of it is the next term of the series, $2\cdot\frac{(1/3)(-2/3)(-5/3)}{6}\Big(\frac18\Big)^3=2\cdot\frac{5}{81}\cdot\frac1{512}\approx2.4\times10^{-4}$.
:::

::: {.solution for="prob-mit18335ps-1-q3" status="draft"}
**(a)** Replace $f$ near $x_n$ by its second-order Taylor polynomial and step to the root of the quadratic nearest $x_n$:
$$f_n+f_n'\delta+\tfrac12f_n''\delta^2=0,\qquad x_{n+1}=x_n+\delta,$$
where $f_n=f(x_n)$ etc. In the quadratic $a\delta^2+b\delta+c$ we have $a=\tfrac12f_n''$, $b=f_n'$, $c=f_n$. The root that tends to Newton's step $-f_n/f_n'$ as $f_n''\to0$ is the small one, and computed in the cancellation-free form it is
$$\delta=\frac{-2f_n}{f_n'+\operatorname{sign}(f_n')\sqrt{f_n'^2-2f_nf_n''}} .$$
The two terms in the denominator have the same sign, so nothing cancels. If the discriminant $f_n'^2-2f_nf_n''$ is negative (the quadratic model has no real root, which can happen far from the root), take an ordinary Newton step $\delta=-f_n/f_n'$ instead.

**(b)** Let $e_n=x_n-x$ and expand about $x_n$: $0=f(x)=f_n-f_n'e_n+\tfrac12f_n''e_n^2-\tfrac16f^{(3)}(\xi)e_n^3$. So the quadratic model $q(\delta)=f_n+f_n'\delta+\tfrac12f_n''\delta^2$ satisfies $q(-e_n)=\tfrac16f^{(3)}e_n^3+O(e_n^4)$, while $q(\delta)=0$ at the step. Since $q'\approx f'(x)\ne0$ near a simple root, $\delta-(-e_n)\approx-q(-e_n)/f'(x)$, and $e_{n+1}=e_n+\delta$ gives
$$e_{n+1}\approx-\frac{f^{(3)}(x)}{6f'(x)}\,e_n^3 .$$
With $e_n=x\delta_n$ this is
$$\delta_{n+1}\approx-\frac{x^2f^{(3)}(x)}{6f'(x)}\,\delta_n^3:$$
*cubic* convergence, the number of correct digits roughly tripling per step. For $f=x^3-1$ at $x=1$: $f^{(3)}=6$, $f'=3$, so $\delta_{n+1}\approx-\tfrac13\delta_n^3$.

**(c)** Implemented in Python with 200-digit `mpmath` arithmetic (instead of Julia `BigFloat`). From $x_1=2$ the first step has a negative discriminant ($144-2\cdot7\cdot12<0$) and falls back to Newton. The errors $x_n-1$ are
$$1,\ \ 0.417,\ \ -3.08\times10^{-2},\ \ 9.75\times10^{-6},\ \ -3.09\times10^{-16},\ \ 9.86\times10^{-48},\ \ -3.20\times10^{-142},$$
so the number of accurate digits goes $0.4,\ 1.5,\ 5.0,\ 15.5,\ 47.0,\ 141.5$, tripling each time, and the ratio $(x_{n+1}-1)/(x_n-1)^3$ is $-0.4259,\ -0.3336,\ -0.33333\ldots$, converging to the predicted $-\tfrac13$.
:::
