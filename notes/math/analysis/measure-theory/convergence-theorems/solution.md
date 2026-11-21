<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camii-pms-3-q2" status="draft"}
1. $f$ is Borel (continuous) and $|f|\le M$, so $\mu(|f|)\le M\mu(\mathbb R)<\infty$; likewise for $\nu$.

2. Taking $f=1$ gives $\mu(\mathbb R)=\nu(\mathbb R)<\infty$.

3. For $a<b$ let $h_k$ be continuous, equal to $1$ on $[a+\frac1k,b]$, $0$ outside $(a,b+\frac1k)$, linear in between ($k$ large). Then $0\le h_k\le1$ and $h_k\to\mathbf 1_{(a,b]}$ pointwise. By dominated convergence with the constant $1$ (integrable for finite measures), $\mu((a,b])=\lim\mu(h_k)=\lim\nu(h_k)=\nu((a,b])$.

4. The intervals $(a,b]$ with $\emptyset$ form a π-system generating $\mathcal B$, so $\mu=\nu$ by @thm-uniqueness-of-extension.
:::

::: {.solution for="prob-camii-pms-3-q7" status="draft"}
1. *First integral.* For $n\ge1$, $\big|\frac{\sin(e^x)}{1+nx^2}\big|\le\frac1{1+x^2}$, which is integrable on $[0,\infty)$ (its integral is $\frac\pi2$). For each $x>0$ the integrand tends to $0$. Dominated convergence gives the limit $0$.

2. *Second integral.* For $x\in(0,1]$, the AM–GM inequality gives $1+n^2x^{3/2}\ge2nx^{3/4}$, so $0\le\frac{n\cos x}{1+n^2x^{3/2}}\le\frac{1}{2x^{3/4}}$, integrable on $(0,1]$ by problem 3.5 since $\frac34<1$.

3. For fixed $x>0$, $\frac{n\cos x}{1+n^2x^{3/2}}\le\frac{1}{nx^{3/2}}\to0$. Dominated convergence gives the limit $0$.
:::

::: {.solution for="prob-camii-pms-3-q8" status="draft"}
1. $(uv)'=u'v+uv'$ is continuous, so by the fundamental theorem of calculus (and @thm-riemann-is-lebesgue on $[-N,N]$)
$$\int_{[-N,N]}(u'v+uv')\,dx=u(N)v(N)-u(-N)v(-N)\to0 .$$

2. The functions $(u'v+uv')\mathbf 1_{[-N,N]}$ tend to $u'v+uv'$ pointwise and are dominated by $|u'v|+|uv'|$, integrable. By dominated convergence the left side tends to $\int_{\mathbb R}(u'v+uv')$.

3. Hence $\int u'v+\int uv'=0$, both integrals being finite.
:::

::: {.solution for="prob-camii-pms-3-q10" status="draft"}
1. Let $\varphi$ be finite on $(-\delta,\delta)$ and fix $0<\eta<\delta'<\delta$. Since $e^{\delta'|x|}\le e^{\delta'x}+e^{-\delta'x}$, $E[e^{\delta'|X|}]\le\varphi(\delta')+\varphi(-\delta')<\infty$.

2. For each $k$, $c_k=\sup_x|x|^ke^{-(\delta'-\eta)|x|}<\infty$, so for $|\theta|<\eta$: $|X|^ke^{\theta X}\le|X|^ke^{\eta|X|}\le c_ke^{\delta'|X|}$, integrable. In particular $E|X|^k\le c_kE[e^{\delta'|X|}]<\infty$.

3. By induction on $k$: $\varphi^{(k)}(\theta)=E[X^ke^{\theta X}]$ for $|\theta|<\eta$. The case $k=0$ is the definition. If it holds for $k$, the $\theta$-derivative of $X^ke^{\theta X}$ is $X^{k+1}e^{\theta X}$, bounded on $|\theta|<\eta$ by the integrable $c_{k+1}e^{\delta'|X|}$, so @thm-differentiation-under-integral gives the formula for $k+1$.

4. At $\theta=0$: $\varphi^{(n)}(0)=E[X^n]$.
:::

::: {.solution for="prob-camii-pms-4-q1" status="draft"}
1. Let $g_n=|f_n|+|f|-|f_n-f|$. By the triangle inequality $g_n\ge0$, and $g_n\to2|f|$ a.e.

2. Fatou's lemma (@thm-fatou-lemma), after changing the functions on a null set:
$$2\|f\|_1\le\liminf_n\mu(g_n)=\liminf_n\big(\|f_n\|_1+\|f\|_1-\|f_n-f\|_1\big)=2\|f\|_1-\limsup_n\|f_n-f\|_1 .$$

3. $\|f\|_1<\infty$, so $\limsup_n\|f_n-f\|_1\le0$.
:::
