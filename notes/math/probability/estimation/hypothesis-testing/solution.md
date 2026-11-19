<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-9-q4" status="draft"}
Let $S_0=0$ and $G_i=S_i-S_{i-1}$.

1. Under $X=0$ the gaps are i.i.d. $\text{Exp}(1)$: $f(s\mid0)=\prod_ie^{-g_i}=e^{-s_n}$ for $0<s_1<\dots<s_n$.
2. Under $X=1$ every other customer is lost, so each gap is the sum of two $\text{Exp}(1)$ times, with Erlang density $ge^{-g}$ (@thm-poisson-process-counts): $f(s\mid1)=\bigl(\prod_ig_i\bigr)e^{-s_n}$.
3. The priors are equal, so MAP is ML (@thm-map-minimises-error): decide that the rumor is true iff
$$\prod_{i=1}^{n}(S_i-S_{i-1})>1,\quad\text{i.e.}\quad\sum_{i=1}^{n}\ln(S_i-S_{i-1})>0.$$
Regular gaps near $1$ or larger favour the rumor; many short gaps favour the plain Poisson process.
:::

::: {.solution for="prob-eecs126hw-9-q5" status="draft"}
$f(y\mid0)=e^{-y}$ and $f(y\mid1)=4e^{-4y}$ for $y\ge0$.

(a) Decide $1$ iff $p\cdot4e^{-4y}>(1-p)e^{-y}$, i.e. iff
$$Y<\frac13\ln\frac{4p}{1-p}.$$
(If $4p\le1-p$, the threshold is $\le0$ and MAP always decides $0$.)

(b) With $p=\frac12$: decide $1$ iff $Y<\frac{\ln4}{3}\approx0.462$.
:::

::: {.solution for="prob-eecs126hw-12-q1" status="draft"}
Let $Y\in\{1,2,\dots\}$ be the number of flips, with $P(Y=y\mid\theta)=(1-\theta)^{y-1}\theta$ for bias (probability of heads) $\theta$.

1. The likelihood ratio $L(y)=\frac qp\bigl(\frac{1-q}{1-p}\bigr)^{y-1}$ is decreasing in $y$ because $q>p$. So the Neyman–Pearson test (@thm-neyman-pearson) decides $1$ for small $Y$: $\hat X=1$ if $Y<k$, $\hat X=1$ with probability $\gamma$ if $Y=k$, and $\hat X=0$ if $Y>k$.
2. Under $X=0$, $P(Y<k)=1-(1-p)^{k-1}$. Take $k$ the integer with $1-(1-p)^{k-1}\le\beta<1-(1-p)^{k}$ (for $\beta=1$ always decide $1$).
3. The false alarm probability must equal $\beta$:
$$\gamma=\frac{\beta-\bigl(1-(1-p)^{k-1}\bigr)}{p(1-p)^{k-1}}\in[0,1).$$
:::

::: {.solution for="prob-eecs126hw-12-q2" status="draft"}
The likelihood ratio is $L(y)=\exp\bigl(\frac{(\mu_1-\mu_0)}{\sigma^2}\bigl(y-\frac{\mu_0+\mu_1}2\bigr)\bigr)$, monotone in $y$; no randomisation is needed since $Y$ is continuous. Let $z_\alpha=\Phi^{-1}(1-\alpha)$.

- If $\mu_1>\mu_0$: $\hat X=1$ iff $Y>\mu_0+\sigma z_\alpha$.
- If $\mu_1<\mu_0$: $\hat X=1$ iff $Y<\mu_0-\sigma z_\alpha$.
- If $\mu_1=\mu_0$ the observation is useless: decide $1$ with probability $\alpha$ regardless of $Y$.

In each case $P(\hat X=1\mid X=0)=\alpha$ exactly. (@exm-neyman-pearson-gaussian is the case $\mu_0=0,\mu_1=1,\sigma=1$.)
:::

::: {.solution for="prob-eecs126hw-12-q3" status="draft"}
Let $Z=\#\{i:x_i\ne y_i\}$, the number of flipped bits; given the inputs, $Z\sim\text{Bin}(n,\epsilon)$ and the likelihood depends on the data only through $Z$.

1. For a fixed $\epsilon_0>0.1$,
$$L(z)=\Bigl(\frac{\epsilon_0}{0.1}\Bigr)^z\Bigl(\frac{1-\epsilon_0}{0.9}\Bigr)^{n-z}=\Bigl(\frac{1-\epsilon_0}{0.9}\Bigr)^n\Bigl(\frac{\epsilon_0/(1-\epsilon_0)}{0.1/0.9}\Bigr)^{z},$$
which is increasing in $z$ because $\frac{\epsilon_0}{1-\epsilon_0}>\frac19$. So the Neyman–Pearson test decides $\epsilon>0.1$ iff $Z>t$ (@thm-neyman-pearson).
2. The threshold is set by the null alone: under $\epsilon=0.1$, $Z\approx N(0.1n,0.09n)$ by the CLT, and $P(Z>t)=0.05$ gives
$$t=0.1n+1.645\cdot0.3\sqrt n\approx0.1n+0.49\sqrt n.$$
3. Neither the form of the test nor $t$ depends on $\epsilon_0$, so this one test is the most powerful for every $\epsilon_0>0.1$ simultaneously.
:::

::: {.solution for="prob-eecs126d-11-q2" status="draft"}
1. The likelihood ratio $L(y)=\frac{f(y\mid1)}{f(y\mid0)}$ is $0$ on $[-1,0)$, $1$ on $[0,1]$ and $+\infty$ on $(1,2]$.
2. By @thm-neyman-pearson the optimal rule decides $1$ where $L=\infty$ (this costs no false alarms), decides $0$ where $L=0$, and randomises where $L=1$, with the threshold at $\lambda=1$:
$$r(y)=\begin{cases}1,&1<y\le2,\\1\text{ with probability }\gamma,&0\le y\le1,\\0,&-1\le y<0.\end{cases}$$
3. The false alarm probability is $\gamma P(0\le Y\le1\mid X=0)=\frac\gamma2$, so $\gamma=\min(2\beta,1)$.
4. The miss probability is $(1-\gamma)P(0\le Y\le1\mid X=1)=\frac{1-\gamma}2=\max(\frac12-\beta,0)$. For $\beta\ge\frac12$ there are no misses; deciding $1$ also on $[-1,0)$ would only add false alarms.
:::
