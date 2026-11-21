<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camii-pms-4-q2" status="draft"}
1. By Markov's inequality (@thm-markov-inequality-measure), $\Pr(|X|\ge\lambda)\le\lambda^{-p}E|X|^p$.

2. For every outcome, $|X|^p=\int_0^{|X|}p\lambda^{p-1}d\lambda=\int_0^\infty p\lambda^{p-1}\mathbf 1_{\{|X|\ge\lambda\}}\,d\lambda$. The integrand is a non-negative measurable function of $(\omega,\lambda)$ ($\{(\omega,\lambda):|X(\omega)|\ge\lambda\}$ is product-measurable, being $\{F\ge0\}$ for the measurable $F(\omega,\lambda)=|X(\omega)|-\lambda$).

3. Take expectations and exchange by Tonelli (@thm-fubini): $E|X|^p=\int_0^\infty p\lambda^{p-1}\Pr(|X|\ge\lambda)\,d\lambda$.

4. If $\Pr(|X|\ge\lambda)\le C\lambda^{-q}$ for $\lambda\ge\lambda_0$, then
$$E|X|^p\le\int_0^{\lambda_0}p\lambda^{p-1}d\lambda+\int_{\lambda_0}^\infty pC\lambda^{p-1-q}d\lambda=\lambda_0^p+\frac{pC}{q-p}\lambda_0^{p-q}<\infty,$$
since $p-1-q<-1$.
:::

::: {.solution for="prob-camii-pms-4-q3" status="draft"}
1. If $\|f\|_2=0$ then $f=0$ a.e., so $fg=0$ a.e. and both sides are $0$; similarly for $g$. If one norm is infinite and the other positive, the right side is $\infty$.

2. Otherwise both norms are finite and positive. For $a,b\in\mathbb R$, $0\le(|a|-|b|)^2$ gives $|ab|\le\frac12(a^2+b^2)$.

3. Apply this with $a=f/\|f\|_2$ and $b=g/\|g\|_2$ and integrate: $\frac{\|fg\|_1}{\|f\|_2\|g\|_2}\le\frac12(1+1)=1$.
:::
