::: {.problem #prob-mit1805s22-4-q6 origin="external" source="mit1805s22-4-q6"}
Fat tails
This problem will explore the tails of two distributions. The tails are important when we want to think about probabilities of extreme events.

(a) As an example, in the general population IQ has mean 100 and standard deviation of 15. IQ is normally distributed. Use the R function pnorm to give the probability that a randomly chosen person has IQ greater than 160, i.e. more than 4 standard deviations above the mean.

(b) Now, in order to be able to use R or Wolfram Alpha without a lot of distracting algebraic manipulation, we'll modify the definition of IQ. Suppose that Modified_IQ has mean 0 and standard deviation $\sqrt{3}$.

Assuming Modified_IQ is normally distributed, find the probability that a randomly chosen person has Modified_IQ more than 4 standard deviations above the mean.

(c) Now assume that Modified_IQ follows a t-distribution with 3 degrees of freedom. Later in the class we will work extensively with t-distributions. Here, it will be enough for us to know the following about this distribution.

- Range: $(-\infty, \infty)$
- PDF: $f(x) = \dfrac{2}{\sqrt{3}\,\pi}\left(1 + \dfrac{x^2}{3}\right)^{-2}$
- Mean: $\mu = 0$
- Standard deviation: $\sigma = \sqrt{3}$

(So this has the same mean and standard deviation as in part (b).)

For this problem, you can work with this pdf directly or you can look up how to use the R functions dt and pt.

Assuming it follows this t-distribution, find the probability that a randomly chosen person has Modified_IQ more than 4 standard deviations above the mean.

You can use R or another calculation package to do the calculation, but you must explicitly show the integral in terms of the probability density.

Compare this value with the probability in part (b)

(d) For this problem, compute probabilities using both the normal distribution in part (b) and the t-distribution in part (c). Do this for the following probabilities.

(i) $P(\text{Modified\_IQ} > 20)$, (ii) $P(\text{Modified\_IQ} > 40)$, (iii) $P(\text{Modified\_IQ} > 200)$.

Why do we say that the t-distribution has a 'fat tail'?

Hence the moral of this problem: Knowing the mean and standard deviation of a quantity is often not enough for predicting the frequency of extreme events (high IQ, 100-year floods, etc.); you need to know the underlying distribution itself (which often requires finding out the underlying geophysics, geochemistry, and biology). In the solutions we will show you graphs of these distributions zoomed in around $4\sigma$ above the mean. If you do that yourself, you will see that they look very different.

*Note (these notes):* The PDF and standard deviation in (c) were garbled in the text extraction and are restored here from the $t_3$ density (the constant $\frac{2}{\sqrt3\,\pi}$ makes it integrate to $1$).
:::

::: {.problem #prob-camib-sts-2-q9 origin="external" source="camib-sts-2-q9"}
If $X\sim N(0,1)$ and $Y\sim\chi^2_n$ are independent, we say that $T=X/\sqrt{Y/n}$ has a $t$-distribution with $n$ degrees of freedom and write $T\sim t_n$. Show that the probability density function of $T$ is
$$f_T(t)=\frac{\Gamma\bigl(\frac{n+1}{2}\bigr)}{\Gamma\bigl(\frac n2\bigr)}\,\frac1{(n\pi)^{1/2}}\,\frac1{(1+t^2/n)^{(n+1)/2}},\qquad t\in\mathbb R.$$
:::

::: {.problem #prob-camib-sts-2-q10 origin="external" source="camib-sts-2-q10"}
Let $X_1,\dots,X_n\overset{\text{iid}}{\sim}N(\mu,\sigma^2)$, where $\sigma^2$ is unknown, and suppose we are interested in testing $H_0:\mu=\mu_0$ against $H_1:\mu\ne\mu_0$. Letting $\bar X=n^{-1}\sum_{i=1}^nX_i$ and $S_{XX}=\sum_{i=1}^n(X_i-\bar X)^2$, show that the likelihood ratio can be expressed as
$$L_X(H_0,H_1)=\Bigl(1+\frac{T^2}{n-1}\Bigr)^{n/2},$$
where $T=\dfrac{n^{1/2}(\bar X-\mu_0)}{\{S_{XX}/(n-1)\}^{1/2}}$. Determine the distribution of $T$ under $H_0$, and hence determine the size $\alpha$ likelihood ratio test.
:::
