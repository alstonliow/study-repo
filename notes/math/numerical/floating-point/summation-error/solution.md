<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit18335ps-1-q4" status="draft"}
**(a)** Let $n=2^m$. *Claim:* $\tilde f(x)=\sum_{i=1}^nx_i\prod_{k=1}^m(1+\epsilon_{i,k})$ with all $\lvert\epsilon_{i,k}\rvert\le\varepsilon_{\text{mach}}$.

1. For $m=0$ ($n=1$) the product is empty and $\tilde f=x_1$.

2. If the claim holds for $2^{m-1}$ numbers, apply it to each half. The final addition multiplies the sum of the two halves by one more factor $(1+\epsilon)$ (@def-floating-point-operations), which attaches the factor $(1+\epsilon_{i,m})=(1+\epsilon)$ to every term. So every $x_i$ carries exactly $m$ factors.

3. As in @thm-naive-summation-backward, $\prod_{k=1}^m(1+\epsilon_{i,k})=1+\delta_i$ with $\lvert\delta_i\rvert\le m\varepsilon_{\text{mach}}+O(\varepsilon_{\text{mach}}^2)$.

4. Hence $\lvert\tilde f-f\rvert=\bigl\lvert\sum_ix_i\delta_i\bigr\rvert\le\varepsilon_{\text{mach}}\log_2(n)\sum_i\lvert x_i\rvert+O(\varepsilon_{\text{mach}}^2)$.

**(b)** Stop the recursion early: when the block has fewer than $N$ elements (say $N=100$ to $200$), add it with the simple loop. There are then only about $2n/N$ function calls for $n-1$ additions, so the overhead is negligible and the inner loop runs at full speed. Each $x_i$ now passes through at most $N-1$ loop additions plus $\log_2(n/N)$ pairwise additions, so the bound becomes $\bigl(N+\log_2(n/N)\bigr)\varepsilon_{\text{mach}}\sum\lvert x_i\rvert$: still logarithmic in $n$, with a constant offset $N$ that does not grow.

**(c)** We ran the equivalent experiment in Python with numpy `float32` (recursion with a loop base case, exact reference by `math.fsum`): for uniform random $x_i\in[0,1)$ the mean relative error stays near $2.5\times10^{-8}$, a fraction of $\varepsilon_{\text{mach}}\approx6\times10^{-8}$, for all $n$ from $10$ to $10^5$, while recursive summation grows from $3\times10^{-8}$ to $6\times10^{-6}$ (@fig-summation-error-2). This is consistent with the bound: the worst case grows like $\log_2n$, and the typical (random-walk) error like $\sqrt{\log_2n}$, which over this range changes by less than a factor $2$.
:::
