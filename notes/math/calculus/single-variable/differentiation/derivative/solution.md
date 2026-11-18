<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801f06-1-q2" status="draft"}
By Pythagoras $L=\sqrt{h^2-20000^2}$ (in km).

a) $L_0=\sqrt{25000^2-20000^2}=15000$. Computing $\Delta L/\Delta h$ for $h=25000\pm\Delta h$:

| $\Delta h$ | $h_0+\Delta h$ | $h_0-\Delta h$ |
|---|---|---|
| $1$ | $1.6666$ | $1.6667$ |
| $10^{-1}$ | $1.6667$ | $1.6667$ |
| $10^{-2}$ | $1.6667$ | $1.6667$ |

All ratios are about $5/3$, so $C=2$ works: $|\Delta L|\le2|\Delta h|$.

b) $L_0=\sqrt{20001^2-20000^2}=\sqrt{40001}\approx200.0025$. The ratios are now

| $\Delta h$ | $h_0+\Delta h$ | $h_0-\Delta h$ |
|---|---|---|
| $1$ | $82.85$ | $200.00$ |
| $10^{-1}$ | $97.62$ | $102.64$ |
| $10^{-2}$ | $99.76$ | $100.26$ |

The largest is $200.0025$, so a round $C$ that works in all three cases is $C=250$ (any $C\ge200.0025$ will do; $C=200$ just fails for $\Delta h=1$). The estimate $|\Delta L|\le250|\Delta h|$ is about a hundred times worse than in (a): $L$ is determined much **less** accurately when the point is nearly below the satellite. (The ratio tends to $dL/dh=h/L$, which is $5/3$ in (a) and about $100$ in (b).)
:::

::: {.solution for="prob-mit1801f06-1-q3" status="draft"}
The top of the tower is at $(0,1100)$. By symmetry let the ant be at $(a,1000-a^2)$ with $a>0$. The ant first sees the tower top when the line of sight from the ant to $(0,1100)$ just grazes the mound, i.e. when it is the tangent line at the ant's position (before that, the mound is in the way, since it is concave down).

The tangent at $x=a$ has slope $-2a$: $y=1000-a^2-2a(x-a)$. At $x=0$ it reaches $y=1000+a^2$. Setting $1000+a^2=1100$ gives $a=10$, so the ant is at height
$$y=1000-10^2=900\text{ feet}.$$
:::

::: {.solution for="prob-mit1801f06-1-q5" status="draft"}
Let $V(t)=(10-t)^2/5$.

a) $V(0)=20$ and $V(5)=5$, so the average rate of change is $\frac{5-20}{5}=-3$: water drains at an average of $3$ liters per minute.

b) $V'(t)=-\frac{2(10-t)}5$, so $V'(5)=-2$: water flows out at $2$ liters per minute.
:::

::: {.solution for="prob-mit1801f06-2a-q1" status="draft"}
From @prob-mit1801f06-1-q1, $E(x)=\frac{x^2+1}{x^2-1}$ and $O(x)=\frac{-2x}{x^2-1}$, both with vertical asymptotes at $x=\pm1$.

**$E$ (even).** $E(0)=-1$; on $(-1,1)$ it is negative, tends to $-\infty$ at $x\to\pm1$ from inside, and has its top at $(0,-1)$. For $\lvert x\rvert>1$ it is above $1$, tends to $+\infty$ next to the asymptotes and decreases towards the horizontal asymptote $y=1$ as $\lvert x\rvert\to\infty$.
*Slope:* on $(-1,1)$ the slope goes from $+\infty$ near $-1$ down through $0$ at $x=0$ to $-\infty$ near $1$; for $x>1$ the slope is negative and rises to $0$; for $x<-1$ it is positive and falls to $0$. So $E'$ is odd, with $E'(0)=0$, vertical asymptotes at $\pm1$, and $E'\to0$ at $\pm\infty$ (check: $E'=-4x/(x^2-1)^2$).

**$O$ (odd).** $O(0)=0$, $O\to0$ as $\lvert x\rvert\to\infty$; on $(-1,1)$ it rises from $-\infty$ to $+\infty$ through the origin; for $x>1$ it rises from $-\infty$ towards $0$; for $x<-1$ it rises from $0$ to $+\infty$. It is increasing on every interval.
*Slope:* always positive; smallest (equal to $2$) at the origin within $(-1,1)$, large near the asymptotes, tending to $0$ at $\pm\infty$. So $O'$ is even and positive with vertical asymptotes at $\pm1$ (check: $O'=2(x^2+1)/(x^2-1)^2$).

Note that the derivative of an even function is odd and the derivative of an odd function is even.
:::

::: {.solution for="prob-mit1801n-1b-q2" status="draft"}
a) $\frac{s(t+h)-s(t)}h=b-32t-16h\to b-32t$, so $v=b-32t$.

b) The top is where $v=0$: $t=b/32$.

c) $s(b/32)=\frac{b^2}{32}-\frac{b^2}{64}=\frac{b^2}{64}$.

d) $v$ is a line falling from $b$ at $t=0$ through $0$ at $t=b/32$ to $-b$ at $t=b/16$; below it, $s$ is a parabola from $(0,0)$ up to $(b/32,b^2/64)$ and back to $0$ at the landing time $b/16$.

e) A bounce with initial speed $b_2$ reaches $b_2^2/64$; half the first height means $b_2^2=b^2/2$, so $b_2=b/\sqrt2$. The second bounce lasts $b_2/16=\frac{b}{16\sqrt2}$, from $t=b/16$ to $t=\frac b{16}\big(1+\frac1{\sqrt2}\big)$, with a smaller parabola for $s$ (top $b^2/128$) and $v$ jumping from $-b$ to $+b/\sqrt2$ at the bounce, then falling with slope $-32$ to $-b/\sqrt2$.

f) The bounce times form a geometric series with ratio $1/\sqrt2$:
$$\frac b{16}\Big(1+\frac1{\sqrt2}+\frac12+\cdots\Big)=\frac{b/16}{1-1/\sqrt2}=\frac{(2+\sqrt2)\,b}{16}\approx3.4\cdot\frac b{16}.$$
:::

::: {.solution for="prob-mit1801n-1c-q1" status="draft"}
$\dfrac{\pi(r+h)^2-\pi r^2}{h}=\dfrac{\pi(2rh+h^2)}h=\pi(2r+h)\to2\pi r$ as $h\to0$.
:::

::: {.solution for="prob-mit1801n-1c-q2" status="draft"}
$f(a)=0$, so $\dfrac{f(x)-f(a)}{x-a}=\dfrac{(x-a)g(x)}{x-a}=g(x)$ for $x\ne a$, and $g(x)\to g(a)$ as $x\to a$ because $g$ is continuous. So $f'(a)=g(a)$. (The product rule cannot be used, since $g$ need not be differentiable.)
:::

::: {.solution for="prob-mit1801n-1c-q3" status="draft"}
a) $\dfrac1h\Big[\dfrac1{2(x+h)+1}-\dfrac1{2x+1}\Big]=\dfrac{-2}{(2x+2h+1)(2x+1)}\to\dfrac{-2}{(2x+1)^2}$.

b) $\dfrac{2(x+h)^2+5(x+h)+4-(2x^2+5x+4)}h=4x+5+2h\to4x+5$.

e) In (a) the slope is always negative, so never $+1$ or $0$; it is $-1$ when $(2x+1)^2=2$, i.e. $x=\frac{-1\pm\sqrt2}2$ (points $(x,\pm\frac1{\sqrt2})$). In (b): slope $1$ at $x=-1$ (point $(-1,1)$), slope $-1$ at $x=-\frac32$ (point $(-\frac32,1)$), slope $0$ at $x=-\frac54$ (point $(-\frac54,\frac78)$).
:::

::: {.solution for="prob-mit1801n-1c-q4" status="draft"}
Using @prob-mit1801n-1c-q3:

a) $f(1)=\frac13$, $f'(1)=-\frac29$: $y=\frac13-\frac29(x-1)=\frac{5-2x}9$.

b) $y=2a^2+5a+4+(4a+5)(x-a)=(4a+5)x-2a^2+4$.
:::

::: {.solution for="prob-mit1801n-1c-q5" status="draft"}
The tangent at $x=a$ is $y=1+(a-1)^2+2(a-1)(x-a)$. It passes through $(0,0)$ when $0=1+(a-1)^2-2a(a-1)=2-a^2$, so $a=\pm\sqrt2$. The slopes are $2(a-1)$, giving the two lines
$$y=2(\sqrt2-1)\,x\qquad\text{and}\qquad y=-2(\sqrt2+1)\,x .$$
:::

::: {.solution for="prob-mit1801n-1c-q6" status="draft"}
a) The slope of the semicircle goes from $+\infty$ at the left end, through $0$ at the top, to $-\infty$ at the right end: the derivative is an odd, decreasing curve with vertical asymptotes at the two ends.

b) The derivative of a downward parabola is a straight line with negative slope through the origin (odd).

c) The derivative is even: positive near $0$ (the graph rises through the origin), negative beyond the turning points, tending to $0$ at both ends.

d) The derivative is odd: positive on the outer side of each left-hand rise, zero at the two tops and at $0$, with signs mirrored on the right.

e) For a zigzag the derivative is a step function equal to the slope of each segment. Reading the figure, the segments rise with slope $1$ and fall with slope $-2$, so the derivative alternates between $1$ and $-2$, and the period is $6$.
:::

::: {.solution for="prob-mit1801n-1d-q6" status="draft"}
Differentiable implies continuous (@thm-differentiable-continuous), so the two pieces must agree at $0$: $b=1$. The slopes must agree too: the right piece has slope $2x+4=4$ at $0$, so $a=4$. With $a=4$, $b=1$ the difference quotients from both sides tend to $4$, so $f$ is differentiable.
:::

::: {.solution for="prob-mit1801n-1d-q8" status="draft"}
Continuity at $0$: $\lim_{x\to0^+}(ax+b)=b$ must equal $\sin0=0$, so $b=0$. The left slope at $0$ is $2\cos0=2$ and the right slope is $a$, so $f$ fails to be differentiable exactly when $a\ne2$. Answer: $b=0$ and any $a\ne2$.
:::
