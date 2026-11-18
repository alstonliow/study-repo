<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801n-2c-q1" status="draft"}
With corner squares of side $x$ ($0\le x\le6$), the volume is $V=x(12-2x)^2$. $V'=(12-2x)^2-4x(12-2x)=(12-2x)(12-6x)$, which is $0$ at $x=2$ and $x=6$. $V(0)=V(6)=0$ and $V(2)=2\cdot8^2=128$, so the best corner square is $2$ inches (volume $128$ cubic inches).
:::

::: {.solution for="prob-mit1801n-2c-q2" status="draft"}
Let $x$ be each side perpendicular to the barn and $y$ the side parallel to it, with $xy=20000$. The fence has length $L=2x+y=2x+\frac{20000}x$ for $x>0$. $L'=2-\frac{20000}{x^2}=0$ at $x=100$, and $L\to\infty$ at both ends, so this is the minimum: $x=100$, $y=200$, $L=400$ feet.
:::

::: {.solution for="prob-mit1801n-2c-q5" status="draft"}
$A=\pi r^2+2\pi rh$, so $h=\frac{A-\pi r^2}{2\pi r}$ and $V=\pi r^2h=\frac12(Ar-\pi r^3)$ for $0<r\le\sqrt{A/\pi}$. $V'=\frac12(A-3\pi r^2)=0$ at $A=3\pi r^2$; then $2\pi rh=A-\pi r^2=2\pi r^2$, so $h=r$. $V=0$ at both ends of the range, so this is the maximum: height equal to radius (the same shape as in @exm-open-can, as expected).
:::

::: {.solution for="prob-mit1801n-2c-q11" status="draft"}
The rectangle is inscribed in the circle, so $x^2+y^2=D^2$ ($D$ the diameter). Maximize $xy^3$; differentiate implicitly in $y$, with $x\,x'=-y$: $\frac{d}{dy}(xy^3)=x'y^3+3xy^2=-\frac{y^4}x+3xy^2=\frac{y^2}{x}(3x^2-y^2)$. This is $0$ when $y^2=3x^2$; the strength is $0$ at both extremes ($x=0$ or $y=0$), so this is the maximum: $y/x=\sqrt3$.
:::

::: {.solution for="prob-mit1801n-2c-q13" status="draft"}
a) At fare $p$ the number of passengers is $100-\frac25(p-200)=180-\frac25p$, so the revenue is $R=p\big(180-\frac25p\big)$. $R'=180-\frac45p=0$ at $p=225$; $R$ is $0$ at $p=0$ and $p=450$, so the best fare is \$225 (90 passengers, revenue \$20,250).

b) Profit in cents: $P=xp-x\big(10-\frac x{10^5}\big)$ with $x=10^5\big(10-\frac p2\big)$. Then $p-10+\frac x{10^5}=\frac p2$, so $P=10^5\big(10-\frac p2\big)\frac p2$. $\frac{dP}{dp}=\frac{10^5}2(10-p)=0$ at $p=10$, where $x=5\times10^5$ is within the plant's range; $P$ is a downward parabola, so this is the maximum. Charge $10$ cents per kWh (profit $2.5\times10^6$ cents, i.e. \$25,000 per day).
:::
