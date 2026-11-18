<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801f06-2b-q1" status="draft"}
a) The slicing plane is at distance $d\ge0$ above the centre, with $d^2+r^2=R^2$. The cap height is $h=R-d=R-\sqrt{R^2-r^2}$, so its area is
$$A=2\pi Rh=2\pi R\big(R-\sqrt{R^2-r^2}\big).$$

b) $A=2\pi R^2\Big(1-\sqrt{1-(r/R)^2}\Big)$, so $x=-(r/R)^2$. Using $(1+x)^{1/2}\approx1+\frac x2$: $1-\sqrt{1+x}\approx\frac{r^2}{2R^2}$ and
$$A\approx\pi r^2,$$
the area of the flat disk. Using $(1+x)^{1/2}\approx1+\frac x2-\frac{x^2}8$ (@prp-standard-quadratic-approximations): $1-\sqrt{1+x}\approx\frac{r^2}{2R^2}+\frac{r^4}{8R^4}$ and
$$A\approx\pi r^2+\frac{\pi r^4}{4R^2}.$$

c) Each dimple removes a cap of the ball (rim radius $r$) and adds a hemisphere of area $2\pi r^2$. So the area is $4\pi R^2+100\,(2\pi r^2-\text{cap})$:

i) flat cap (the linear approximation of (b)): $4\pi R^2+100\pi r^2$;

ii) quadratic approximation: $4\pi R^2+100\big(\pi r^2-\frac{\pi r^4}{4R^2}\big)$;

iii) exact: $4\pi R^2+100\big(2\pi r^2-2\pi R(R-\sqrt{R^2-r^2})\big)$.

With $\pi=3.14$, $r=0.15$, $R=1.5$: (i) $35.325$, (ii) $35.30734$, (iii) $35.30725$. Rounded to hundredths the exact answer is $35.31$; (ii) also gives $35.31$ (error about $9\times10^{-5}$), but (i) is off by about $0.018$ and rounds to $35.33$ (or $35.32$), which is wrong under the contest rules. So the flat-disk approximation is not adequate.

d) A dimple occupies a cap of rim radius $0.15$, area about $\pi(0.15)^2\approx0.0707$ cm², while the ball has area $4\pi(1.5)^2\approx28.3$ cm²; the ratio is $400$. Equal disks can cover at most about $\pi/\sqrt{12}\approx0.91$ of a surface (hexagonal packing), so roughly $0.91\times400\approx360$ dimples fit, a bit fewer on a curved surface: about $350$.

*Discrepancy:* with the numbers as printed, $100$ dimples do fit easily (about a quarter of the possible number), so the claim that they cannot be placed without overlap does not hold for these values; presumably it referred to the original, unchanged numbers.
:::

::: {.solution for="prob-mit1801f06-3-q3" status="draft"}
a) From $2L\,L'=2h$, $\frac{dL}{dh}=\frac hL$. At $h=25000$, $L=15000$ this is $\frac53$, matching the ratios $\approx1.6667$ of @prob-mit1801f06-1-q2; at $h=20001$ it is $\frac{20001}{200.0025}\approx100$, matching the ratios there as $\Delta h\to0$.

Why $\Delta L/\Delta h\le dL/dh$ at the left endpoint: $\frac{d}{dh}\frac hL=\frac{L-h\cdot h/L}{L^2}=\frac{L^2-h^2}{L^3}=-\frac{20000^2}{L^3}<0$, so $L'$ is decreasing ($L$ is concave down). By @thm-mean-value, $\frac{\Delta L}{\Delta h}=L'(c)$ for some $c\in(h_0,h_0+\Delta h)$, and $L'(c)\le L'(h_0)$.

$\lvert\Delta L\rvert\le2\lvert\Delta h\rvert$ holds (for small $\Delta h$, and exactly for all $\Delta h>0$ by the argument above) when $h/L\le2$, i.e. $h^2\le4(h^2-20000^2)$, i.e. $h\ge\frac{40000}{\sqrt3}\approx23{,}094$ km.

b) The horizontal distances are $L_1=\sqrt{21000^2-20000^2}=\sqrt{41\times10^6}\approx6403.12$ km and $L_2=\sqrt{52000^2-20000^2}=48000$ km. So you are at $x_1\pm6403.12$ and also at $x_2\pm48000$; since you know $x_1,x_2$, only one of the two candidate points from satellite 2 lies within about $6403$ km of $x_1$, and that decides the sign. If $x_1<x_2$, you are at $x=x_2-48000$ (to the left of $x_2$: the point $x_2+48000$ would be farther than $48000-6403$ from $x_1$, hence inconsistent); if $x_2<x_1$, you are at $x=x_2+48000$. (The hint names the same case twice; the second case is meant to be $x_2<x_1$.)

Accuracy: $\lvert\Delta L\rvert\approx\frac hL\lvert\Delta h\rvert$. For satellite 2, $\frac{52000}{48000}\approx1.08$, so $\lvert\Delta L_2\rvert\approx1.1\times10^{-2}$ km; for satellite 1, $\frac{21000}{6403}\approx3.28$, so $\lvert\Delta L_1\rvert\approx3.3\times10^{-2}$ km. Use satellite 2 for the position: $x=x_2\mp48000$, accurate to about $0.011$ km ($11$ m); the error $10^{-10}$ in $x_2$ is negligible.

c) If $\alpha$ is the angle between the line of sight and the horizontal, then $L=h\cos\alpha$, so $\frac{dL}{dh}=\frac hL=\frac1{\cos\alpha}=\sec\alpha$. The measurement is most sensitive (worst) when the satellite is nearly overhead ($\alpha\to\pi/2$).
:::

::: {.solution for="prob-mit1801f06-3-q4" status="draft"}
a) The ray from the origin to $(a,b)$ makes angle $\theta$ with the positive $x$-axis, so $\tan\theta=\frac ba=a-\frac1{4a}$. Differentiating with respect to $a$: $\sec^2\theta\,\frac{d\theta}{da}=1+\frac1{4a^2}$, so
$$\frac{d\theta}{da}=\cos^2\theta\Big(1+\frac1{4a^2}\Big).$$
This simplifies: the distance from the focus to $(a,b)$ is $\rho=\sqrt{a^2+b^2}=a^2+\frac14$ (check: $a^2+(a^2-\frac14)^2=(a^2+\frac14)^2$), and $a=\rho\cos\theta$. Then $1+\frac1{4a^2}=\frac{\rho}{a^2}$ and $\frac{d\theta}{da}=\frac{\rho\cos^2\theta}{a^2}=\frac{\cos\theta}{a}$.

b) At $\theta=-\pi/6$: $a-\frac1{4a}=-\frac1{\sqrt3}$, i.e. $4a^2+\frac4{\sqrt3}a-1=0$, with roots $a=\frac1{2\sqrt3}$ and $a=-\frac{\sqrt3}2$. The second gives the point $(-\frac{\sqrt3}2,\frac12)$, in the direction $5\pi/6$, so $a=\frac1{2\sqrt3}\approx0.2887$ (with $b=-\frac16$). There $\frac{d\theta}{da}=\frac{\cos(-\pi/6)}{a}=\frac{\sqrt3/2}{1/(2\sqrt3)}=3$, so $\lvert\Delta a\rvert\approx\frac{\lvert\Delta\theta\rvert}3\approx3.3\times10^{-4}$:
$$a\approx0.2887\pm0.0003.$$

c) $4a^2-4a\tan\theta-1=0$ gives (positive root, for $\cos\theta>0$) $a=\frac{\tan\theta+\sec\theta}2=\frac{1+\sin\theta}{2\cos\theta}$. At $\theta=-\pi/6$ this is $\frac{1/2}{\sqrt3}=\frac1{2\sqrt3}$. Also $\frac{da}{d\theta}=\frac{2\cos^2\theta+2\sin\theta(1+\sin\theta)}{4\cos^2\theta}=\frac{1+\sin\theta}{2\cos^2\theta}=\frac1{2(1-\sin\theta)}$, which is $\frac13$ at $\theta=-\pi/6$, agreeing with (a) and (b).
:::

::: {.solution for="prob-mit1801n-2a-q2" status="draft"}
By (2): $f(0)=\frac1a$ and $f'(x)=-\frac{b}{(a+bx)^2}$, so $f'(0)=-\frac b{a^2}$ and $\frac1{a+bx}\approx\frac1a-\frac b{a^2}x$.

By the basic formulas: $\frac1{a+bx}=\frac1a\cdot\frac1{1+(b/a)x}\approx\frac1a\Big(1-\frac bax\Big)$, using $(1+u)^{-1}\approx1-u$ (@prp-standard-linear-approximations). Same answer.
:::

::: {.solution for="prob-mit1801n-2a-q3" status="draft"}
Basic formulas: $(1+x)^{3/2}\approx1+\frac32x$ and $(1+2x)^{-1}\approx1-2x$, so the product is $\approx1+\frac32x-2x=1-\frac x2$ (dropping $x^2$).

By (2): $f(0)=1$ and $f'(x)=\frac{\frac32(1+x)^{1/2}(1+2x)-2(1+x)^{3/2}}{(1+2x)^2}$, so $f'(0)=\frac32-2=-\frac12$. Again $f(x)\approx1-\frac x2$.
:::

::: {.solution for="prob-mit1801n-2a-q7" status="draft"}
$\sec x=\frac1{\cos x}\approx\frac1{1-x^2/2}\approx1+\frac{x^2}2$ and $(1-x^2)^{-1/2}\approx1+\frac{x^2}2$. Multiplying and dropping terms of degree above $2$: $\dfrac{\sec x}{\sqrt{1-x^2}}\approx1+x^2$.
:::

::: {.solution for="prob-mit1801n-2a-q11" status="draft"}
$p=C(v_0+\Delta v)^{-k}=Cv_0^{-k}\Big(1+\frac{\Delta v}{v_0}\Big)^{-k}$. With $(1+u)^r\approx1+ru+\frac{r(r-1)}2u^2$ and $r=-k$:
$$p\approx Cv_0^{-k}\Big(1-k\frac{\Delta v}{v_0}+\frac{k(k+1)}2\Big(\frac{\Delta v}{v_0}\Big)^2\Big)=p_0\Big(1-k\frac{\Delta v}{v_0}+\frac{k(k+1)}2\frac{(\Delta v)^2}{v_0^2}\Big),$$
where $p_0=Cv_0^{-k}$ is the original pressure.
:::

::: {.solution for="prob-mit1801n-2a-q12" status="draft"}
a) $\big(1+x+\frac{x^2}2\big)\big(1+x+x^2\big)\approx1+2x+\big(1+1+\frac12\big)x^2=1+2x+\frac52x^2$.

d) $\cos x\approx1-\frac{x^2}2$ and $\ln(1+u)\approx u$, so $\ln\cos x\approx-\frac{x^2}2$ (the next term of $\ln(1+u)$ is of degree $4$ in $x$).

e) With $x=1+h$: $(1+h)\ln(1+h)\approx(1+h)\big(h-\frac{h^2}2\big)\approx h+\frac{h^2}2$, i.e. $x\ln x\approx(x-1)+\frac12(x-1)^2$.
:::
