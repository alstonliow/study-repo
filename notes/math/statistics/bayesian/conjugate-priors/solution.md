<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1805s22-7-q6" status="draft"}
Use @thm-normal-normal-update with $a=1/\sigma^2_{\mathrm{prior}}$, $b=n/\sigma^2$.

(a) $a=\frac19$, $b=\frac14$: $\mu_{\mathrm{post}}=\frac{6/9+5/4}{1/9+1/4}=\frac{69}{13}\approx5.31$, $\sigma^2_{\mathrm{post}}=\frac{36}{13}\approx2.77$. So
$$f(\theta\mid x=5)=\frac1{\sqrt{2\pi\cdot36/13}}\exp\Bigl(-\frac{(\theta-69/13)^2}{2\cdot36/13}\Bigr).$$

(b) $a=\frac19$, $b=\frac84=2$: $\mu_{\mathrm{post}}=\frac{6/9+10}{1/9+2}=\frac{96}{19}\approx5.05$, $\sigma^2_{\mathrm{post}}=\frac9{19}\approx0.47$. The prior is a wide bump at $6$ (sd $3$); the posterior is a narrow bump at $5.05$ (sd $0.69$). Eight measurements are much more precise than the prior, so the belief moves almost all the way to $\bar x=5$ and becomes far more certain.

(c) $a=\frac1{225}$, $b=\frac1{100}$, so $\mu_{\mathrm{post}}=\frac{100\cdot4+9x}{13}$ (weights $\frac4{13}$ on the prior mean and $\frac9{13}$ on the score).
(i) $x=80$: $\mu_{\mathrm{post}}\approx86.2$. (ii) $x=150$: $\mu_{\mathrm{post}}\approx134.6$. Both estimates are pulled towards the population mean $100$ (regression to the mean).
:::
