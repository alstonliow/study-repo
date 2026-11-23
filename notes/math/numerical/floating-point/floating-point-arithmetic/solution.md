<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit18335ps-1-q2" status="draft"}
**(a)** The direct formula `(abs(x)^4 + abs(y)^4)^0.25` fails at both ends of the exponent range. For $x=10^{-100}$, $x^4=10^{-400}$ underflows to $0$ (below even the subnormal range, about $5\times10^{-324}$), so the result is $0$ instead of $10^{-100}$: a relative error of $100\%$. For $x=10^{100}$, $x^4=10^{400}$ overflows to $\infty$.

*Fix:* scale by $s=\max(|x|,|y|)$ before raising to the fourth power and multiply back afterwards:
$$L_4(x,y)=s\Bigl(\bigl(\tfrac{|x|}s\bigr)^4+\bigl(\tfrac{|y|}s\bigr)^4\Bigr)^{1/4},\qquad L_4(0,0)=0.$$
Now both ratios lie in $[0,1]$ and one of them is $1$, so the sum lies in $[1,2]$: no overflow, and an underflow of the smaller term only drops a contribution below $\varepsilon_{\text{mach}}$ relative to the result. Each operation (two divisions, powers, an addition, a fourth root, a multiplication) contributes a relative error $O(\varepsilon_{\text{mach}})$ by @def-floating-point-operations, and the fourth root reduces the relative error of its argument by a factor $4$ (its condition number is $\tfrac14$, cf. @exm-conditioning-elementary). So the result is within a few ulps. (If $s$ is replaced by the nearest power of $2$, the scaling itself is exact.) Checked in Python: the corrected function returns $10^{-100}$ and $10^{100}$, and $L_4(3,4)=4.284572294953817$, equal to a 80-digit computation rounded to double.

**(b)** The direct `cot(x) - cot(x+y)` for $x=1$, $y=10^{-20}$ returns $0$, because $1+10^{-20}$ rounds to $1$. Even when $x+y$ is representable, subtracting two nearly equal cotangents suffers cancellation (@prp-cancellation), with relative error about $\varepsilon_{\text{mach}}\lvert\cot x\rvert/\lvert\cot x-\cot(x+y)\rvert$.

*Fix:* use $\cot a-\cot b=\dfrac{\cos a\sin b-\sin a\cos b}{\sin a\sin b}=\dfrac{\sin(b-a)}{\sin a\,\sin b}$, so
$$\cot x-\cot(x+y)=\frac{\sin y}{\sin x\,\sin(x+y)}.$$
No subtraction of nearly equal quantities remains: $\sin y$ is computed accurately from $y$ itself, and $\sin(x+y)$ only needs $x+y$ to relative accuracy $\varepsilon_{\text{mach}}$. For $x=1$, $y=10^{-20}$ it gives $1.4122829274373917\times10^{-20}$, matching high precision to the last digit; for comparable arguments ($x=1$, $y=0.5$) it agrees with the exact $0.5711777716316783$. (Near zeros of $\sin x$ or $\sin(x+y)$ the problem itself is ill-conditioned, and the formula is as accurate as the problem allows.)
:::
