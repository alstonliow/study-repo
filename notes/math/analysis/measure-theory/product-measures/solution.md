<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camii-pms-3-q11" status="draft"}
1. Let $g(x)=f_1(x_1)\cdots f_n(x_n)$. By Tonelli (@thm-fubini), for a box $A=A_1\times\dots\times A_n$, $\int_Ag\,dx=\prod_k\int_{A_k}f_k=\prod_k\mu_{X_k}(A_k)$. So the measure with density $g$ agrees with $\mu_{X_1}\otimes\dots\otimes\mu_{X_n}$ on boxes, hence everywhere (@thm-uniqueness-of-extension): $g$ is a density of the product law.

2. By @prp-independence-product-law, the $X_k$ are independent iff $\mu_X=\mu_{X_1}\otimes\dots\otimes\mu_{X_n}$, i.e. iff $f$ and $g$ are densities of the same measure.

3. If $f=g$ a.e., the measures agree (@thm-integral-linear-monotone). Conversely, if $\int_Af=\int_Ag$ for all Borel $A$, then $f-g$ is integrable with $\int(f-g)\mathbf 1_A=0$ for all Borel $A$, so $f=g$ a.e. by @prp-integral-pi-system.
:::

::: {.solution for="prob-camii-pms-3-q12" status="draft"}
1. $(x,y)\mapsto|(x,y)|$ is continuous, hence Borel, and the composition with the Borel $f$ is measurable.

2. Define measures on $\mathcal B([0,\infty))$ by $\nu_1(A)=\lambda^2(\{z\in\mathbb R^2:\ |z|\in A\})$ (image measure of $\lambda^2$) and $\nu_2(A)=2\pi\int_Ar\,dr$ (density measure). The claimed identity is $\nu_1(f)=\nu_2(f)$, by the image-measure formula.

3. For $A=[0,s]$: by Tonelli, $\nu_1([0,s])=\int_{-s}^s2\sqrt{s^2-x^2}\,dx=\pi s^2$ (the substitution $x=s\sin t$ gives $2s^2\int_{-\pi/2}^{\pi/2}\cos^2t\,dt=\pi s^2$), and $\nu_2([0,s])=2\pi\cdot\frac{s^2}2=\pi s^2$. Differences give agreement on all $(a,b]$, and on $\{0\}$ both vanish.

4. Both measures are finite on each $[0,n]$, so by @cor-uniqueness-sigma-finite $\nu_1=\nu_2$. Then $\nu_1(f)=\nu_2(f)$ for every measurable $f\ge0$ (indicators, simple functions, monotone convergence).

5. With $f(r)=e^{-r^2/2}$: $\int_{\mathbb R^2}e^{-(x^2+y^2)/2}\,dx\,dy=2\pi\int_0^\infty re^{-r^2/2}dr=2\pi$. By Tonelli the left side is $\big(\int_{\mathbb R}e^{-x^2/2}dx\big)^2$. So $\int e^{-x^2/2}dx=\sqrt{2\pi}$, and $(2\pi)^{-1/2}e^{-x^2/2}$, being non-negative with integral $1$, is a probability density.
:::

::: {.solution for="prob-camii-pms-3-q13" status="draft"}
1. The pairs $(X_n,U_n)$ are independent (@cor-independence-grouping) and identically distributed, with joint law $\mu\otimes\lambda_{[0,1]}$ (@prp-independence-product-law).

2. For $A\in\mathcal E$, by Fubini,
$$\Pr(X_1\in A,\ RU_1\le f(X_1))=\int_A\lambda\big(\{u\in[0,1]:\ u\le f(x)/R\}\big)\mu(dx)=\int_A\frac{f(x)}R\,\mu(dx)=\frac{\nu(A)}R,$$
using $0\le f/R\le1$. With $A=E$, the acceptance probability is $p=\frac1R$ (so $R\ge1$).

3. The event $\{T=n,\ Y\in A\}$ is $\{RU_k>f(X_k)\text{ for }k<n\}\cap\{X_n\in A,\ RU_n\le f(X_n)\}$. By independence of the pairs,
$$\Pr(T=n,\ Y\in A)=(1-p)^{n-1}\frac{\nu(A)}R .$$

4. Summing over $n$: $\Pr(T<\infty,\ Y\in A)=\frac{\nu(A)}R\cdot\frac1p=\nu(A)$. In particular $\Pr(T<\infty)=\nu(E)=1$, so $Y$ is a.s. defined and $\Pr(Y\in A)=\nu(A)$.
:::
