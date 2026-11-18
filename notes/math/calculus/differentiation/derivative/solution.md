<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

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
