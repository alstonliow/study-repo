<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-probability-2-10" status="draft"}
(a) **Uniform** on $\{1,\dots,13\}$: each value has $4$ of the $52$ cards.

(b) **Binomial** $\mathrm{Bin}(n,p)$, where $n$ is the number of days the
    train runs that week and $p$ is the daily probability of being late.

(c) **Poisson**: rare independent events arriving at a constant average rate.

(d) **Geometric**: the number of independent trials until the first success,
    where "success" is the train being on time.

(e) **Geometric**, with success probability $3/n$ if there are $n$
    equally likely coupons. (This is not the full coupon collector problem,
    which waits for all coupons.)

(f) **Binomial** $\mathrm{Bin}(7,q)$, where $q$ is the probability that a
    shell lands aperture-up. Shells are not coins, so $q$ need not be $\frac12$.

(g) $3/7 = 0.\overline{428571}$ has period $6$, and $1{,}002 = 167\cdot6$,
    so each of $1,2,4,5,7,8$ appears exactly $167$ times. **Uniform** on
    $\{1,2,4,5,7,8\}$.

(h) $5/11 = 0.\overline{45}$, so the digits $4$ and $5$ each appear $500$
    times. **Uniform** on $\{4,5\}$.

(i) **Uniform** on $\{0,\dots,9\}$ is the natural model. It is consistent
    with all digit counts of $\pi$ computed so far, but it has not been
    proved (it would follow if $\pi$ were *normal*).
:::
