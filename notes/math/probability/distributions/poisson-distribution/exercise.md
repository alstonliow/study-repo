<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-probability-2-08 origin="external" source="fit1058-cn-10.12-q8"}
Meteors arrive randomly and independently. The Eta Aquariids meteor shower
has, at its peak and in idealised conditions, an average rate of $0.83$
visible meteors per minute.

(a) What is the distribution of the number of meteors seen in a given
    minute around the peak?

(b) What is the probability that no meteors are seen in a given minute?

(c) How long should an observer be prepared to wait to have
    probability $0.95$ of seeing a meteor?
:::

::: {.problem #prob-cs70hw-12-q6 origin="external" source="cs70hw-12-q6"}
**Sum of Poisson Variables.** Assume that you were given two independent Poisson random variables $X_1, X_2$. Assume that the first has mean $\lambda_1$ and the second has mean $\lambda_2$. Prove that $X_1 + X_2$ is a Poisson random variable with mean $\lambda_1 + \lambda_2$.

Hint: Recall the binomial theorem.
$$(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k}$$
:::

::: {.problem #prob-eecs126hw-7-q3 origin="external" source="eecs126hw-7-q3"}
**Balls and Bins: Poisson Convergence.** Consider throwing $m$ balls into $n$ bins uniformly at random. In this question, we will show that the number of empty bins converges to a Poisson limit, under the condition that $n\exp(-m/n)\to\lambda\in(0,\infty)$.

(a) Let $p_k(m,n)$ denote the probability that exactly $k$ bins are empty after throwing $m$ balls into $n$ bins uniformly at random. Show that
$$p_0(m,n)=\sum_{j=0}^{n}(-1)^j\binom nj\Bigl(1-\frac jn\Bigr)^m.$$
(Hint: Use the Inclusion-Exclusion Principle.)

(b) Show that
$$p_k(m,n)=\binom nk\Bigl(1-\frac kn\Bigr)^mp_0(m,n-k).\tag{1}$$

(c) Show that
$$\binom nk\Bigl(1-\frac kn\Bigr)^m\le\frac{\lambda^k}{k!}\tag{2}$$
as $m,n\to\infty$ (such that $n\exp(-m/n)\to\lambda$).

(d) Show that
$$\binom nk\Bigl(1-\frac kn\Bigr)^m\ge\frac{\lambda^k}{k!}\tag{3}$$
as $m,n\to\infty$ (such that $n\exp(-m/n)\to\lambda$). This is the hard part of the proof. To help you out, we have outlined a plan of attack:

i. Show that
$$\binom nk\Bigl(1-\frac kn\Bigr)^m\ge\Bigl(1-\frac kn\Bigr)^{k+m}\frac{n^k}{k!}.$$

ii. Show that
$$\ln\Bigl\{n^k\Bigl(1-\frac kn\Bigr)^m\Bigr\}\to k\ln\lambda$$
as $m,n\to\infty$ (such that $n\exp(-m/n)\to\lambda$). You may use the inequality $\ln(1-x)\ge-x-x^2$ for $0\le x\le1/2$.

iii. Show that
$$\Bigl(1-\frac kn\Bigr)^k\to1$$
as $m,n\to\infty$ (such that $n\exp(-m/n)\to\lambda$). Conclude that (3) holds.

(e) Now, show that
$$p_0(m,n)\to\exp(-\lambda).$$
(Try using the results you have already proven.) Conclude that
$$p_k(m,n)\to\frac{\lambda^k\exp(-\lambda)}{k!}.$$
:::

::: {.problem #prob-camib-sts-1-q10 origin="external" source="camib-sts-1-q10"}
(Law of small numbers) For each $n\in\mathbb N$, let $X_{n1},\dots,X_{nn}\overset{\text{iid}}{\sim}\mathrm{Bernoulli}(p_n)$ and let $S_n=\sum_{i=1}^nX_{ni}$. Prove that if $np_n\to\lambda\in(0,\infty)$ as $n\to\infty$, then for each $x\in\{0,1,2,\dots\}$,
$$P(S_n=x)\to P(Y=x)$$
as $n\to\infty$ where $Y\sim\mathrm{Poisson}(\lambda)$.
:::
