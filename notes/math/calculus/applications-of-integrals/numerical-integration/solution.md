<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit1801f06-6-q4" status="draft"}
Sketch: a parabola through $(-h,y_0)$, $(0,y_1)$, $(h,y_2)$, with the area under it over $[-h,h]$ shaded.

1. At $x=0$: $y_1=C$.

2. $\int_{-h}^h(Ax^2+Bx+C)\,dx=\frac23Ah^3+0+2Ch$, since $Bx$ is odd. So, knowing $C$, only $A$ is needed; write the area as $\frac h3\,(2Ah^2+6C)$.

3. Adding $y_0=Ah^2-Bh+C$ and $y_2=Ah^2+Bh+C$ eliminates $B$: $y_0+y_2=2Ah^2+2C$, so $2Ah^2=y_0+y_2-2y_1$.

4. Area $=\frac h3\big(y_0+y_2-2y_1+6y_1\big)=\frac h3(y_0+4y_1+y_2)$.

(This is @thm-simpson-parabola.)
:::

::: {.solution for="prob-mit1801f06-6-q5" status="draft"}
Let $a=\sqrt{\pi/2}\approx1.253314$. With eight intervals, $\Delta t=a/8\approx0.156664$ and the values $y_i=\cos(t_i^2)$, $t_i=i\,\Delta t$, are

| $i$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| $y_i$ | 1 | 0.999699 | 0.995185 | 0.975702 | 0.923880 | 0.817585 | 0.634393 | 0.359895 | 0 |

(The last value is $\cos(\pi/2)=0$.) Simpson's rule (@def-numerical-rules):

- four intervals ($\Delta t=a/4$, using $y_0,y_2,y_4,y_6,y_8$): $\frac{a/4}{3}(y_0+4y_2+2y_4+4y_6+y_8)\approx0.978219$;
- eight intervals: $\frac{a/8}3(y_0+4y_1+2y_2+4y_3+2y_4+4y_5+2y_6+4y_7+y_8)\approx0.977503$.

The true value is $\int_0^{\sqrt{\pi/2}}\cos(t^2)\,dt=0.977451$ (to six places), so the errors are about $7.7\times10^{-4}$ and $5.2\times10^{-5}$; halving the step divided the error by about $15$, close to the $16$ expected for Simpson's rule.

*Discrepancy:* the value $1.22505$ quoted in the problem cannot be right: $f(x)=\int_0^x\cos(t^2)dt$ has its largest value at $x=\sqrt{\pi/2}$ (see @prob-mit1801f06-5-q2), and that value is $0.97745$.
:::
