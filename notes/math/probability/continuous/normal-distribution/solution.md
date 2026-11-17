<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-14-q7" status="draft"}
(a) For $t\ge0$, $\Pr(-\ln U_1\le t)=\Pr(U_1\ge e^{-t})=1-e^{-t}$, the CDF of $\mathrm{Exp}(1)$ (@prp-exponential-tail).

(b) By @thm-independent-joint-density, $(N_1,N_2)$ has density $\frac1{2\pi}e^{-(x^2+y^2)/2}$. For $s\ge0$, in polar coordinates,
$$\Pr(N_1^2+N_2^2\le s)=\int_0^{2\pi}\int_0^{\sqrt s}\frac1{2\pi}e^{-r^2/2}\,r\,dr\,d\theta=\Bigl[-e^{-r^2/2}\Bigr]_0^{\sqrt s}=1-e^{-s/2},$$
the CDF of $\mathrm{Exp}(\frac12)$.

(c) (Box–Muller.) Let $R=\sqrt{-2\ln U_1}$ and $\Theta=2\pi U_2$, and output $N=R\cos\Theta$.

1. By (a), $-2\ln U_1\sim\mathrm{Exp}(\frac12)$ (scaling an $\mathrm{Exp}(1)$ by $2$ halves the rate), so $R^2$ has the distribution of $N_1^2+N_2^2$ from (b). $\Theta$ is uniform on $[0,2\pi)$ and independent of $R$.

2. For $(N_1,N_2)$, the polar computation in (b) shows that the radius and the angle are independent, with the angle uniform: the density $\frac1{2\pi}e^{-r^2/2}r$ in $(r,\theta)$ is a product of a function of $r$ and the constant $\frac1{2\pi}$.

3. So $(R,\Theta)$ has the same joint distribution as the polar coordinates of $(N_1,N_2)$, and therefore $(R\cos\Theta,R\sin\Theta)$ has the distribution of $(N_1,N_2)$. In particular $N=R\cos\Theta\sim N(0,1)$.
:::
