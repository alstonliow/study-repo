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

::: {.solution for="prob-eecs126hw-3-q4" status="draft"}
(a) The density of $Z=X_1+X_2$ is
$$f_Z(z)=\int_{-\infty}^{\infty}\frac{1}{2\pi}e^{-\frac{x^2+(z-x)^2}{2}}\,dx.$$
Complete the square: $x^2+(z-x)^2=2(x-\tfrac z2)^2+\tfrac{z^2}{2}$. Hence
$$f_Z(z)=\frac1{2\pi}e^{-z^2/4}\int e^{-(x-z/2)^2}\,dx=\frac{\sqrt\pi}{2\pi}e^{-z^2/4}=\frac{1}{\sqrt{2\pi\cdot2}}e^{-z^2/(2\cdot2)},$$
the $N(0,2)$ density.

(b) For odd $n$, $x^n\phi(x)$ is odd and integrable, so $E[X^n]=0$. For $n\ge2$, integrating by parts with $\phi'(x)=-x\phi(x)$,
$$E[X^n]=\int x^{n-1}\cdot x\phi(x)\,dx=\bigl[-x^{n-1}\phi(x)\bigr]_{-\infty}^{\infty}+(n-1)\int x^{n-2}\phi(x)\,dx=(n-1)E[X^{n-2}].$$
With $E[X^0]=1$, for even $n=2k$: $E[X^{2k}]=(2k-1)(2k-3)\cdots1=\frac{(2k)!}{2^kk!}$ (e.g. $1,3,15$ for $n=2,4,6$).
:::

::: {.solution for="prob-eecs126hw-6-q5" status="draft"}
(a) $\hat I_{ij}=\frac1d\sum_{k=1}^{d}S_{ki}S_{kj}$, a sum of $d$ independent terms.

- $i=j$: $E[S_{ki}^2]=1$ and $\operatorname{Var}(S_{ki}^2)=3-1=2$, so $E[\hat I_{ii}]=1$ and $\operatorname{Var}(\hat I_{ii})=\frac{2d}{d^2}=\frac2d$.
- $i\ne j$: $E[S_{ki}S_{kj}]=0$ and $E[S_{ki}^2S_{kj}^2]=1$, so $E[\hat I_{ij}]=0$ and $\operatorname{Var}(\hat I_{ij})=\frac1d$.

(b) $\hat I_{ij}=\sum_kS_{ki}S_{kj}$.

- $i=j$: column $i$ has exactly one entry $\pm1$, so $\hat I_{ii}=1$ always: mean $1$, variance $0$.
- $i\ne j$: the product is non-zero only if columns $i$ and $j$ chose the same row (probability $\frac1d$), and then it is $\pm1$ with equal probability, independently. So $E[\hat I_{ij}]=0$ and $\operatorname{Var}(\hat I_{ij})=E[\hat I_{ij}^2]=\frac1d$.
:::
