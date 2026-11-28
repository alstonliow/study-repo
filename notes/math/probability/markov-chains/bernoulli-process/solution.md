<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6041f10-7-q1" status="draft"}
(a) The $i$th success comes before the $j$th failure exactly when the first $i+j-1$ trials contain at least $i$ successes (then they contain at most $j-1$ failures). So the probability is
$$\sum_{k=i}^{i+j-1}\binom{i+j-1}kp^k(1-p)^{i+j-1-k}.$$

(b) Call a failure an "arrival": arrivals form a Bernoulli process with parameter $1-p$. The time $T_j$ of the $j$th failure is Pascal of order $j$ with parameter $1-p$ (@thm-bernoulli-interarrivals), and the number of successes before it is $T_j-j$. Hence
$$E[T_j-j]=\frac j{1-p}-j=\frac{jp}{1-p},\qquad\mathrm{Var}(T_j-j)=\frac{jp}{(1-p)^2}.$$

(c) $L_{17}\ge42$ means the 17th success has not happened in the first $41$ trials, that is, those $41$ trials contain at most $16$ successes. So $a=16$ and $b=41$.
:::

::: {.solution for="prob-mit6041f10-7-q2" status="draft"}
A call gives a sample with probability $\frac34\cdot\frac23=\frac12$, independently, so samples form a Bernoulli process with $p=\frac12$; let $Y_k$ be the call of the $k$th sample.

(a) $\Pr(Y_1=3)=(\frac12)^2\cdot\frac12=\frac18$.

(b) By the fresh-start property (@thm-bernoulli-fresh-start) the calls after the eighth do not depend on the first eight. The fifth sample is on call 11 when calls 9 and 10 give none and call 11 gives one: $\frac18$.

(c) Pascal PMF: $\Pr(Y_2=5)=\binom41(\frac12)^2(\frac12)^3=\frac18$.

(d) $\Pr(Y_2=2)=\frac14$, so $\Pr(Y_2=5\mid Y_2\ne2)=\frac{1/8}{3/4}=\frac16$.

(e) He needs a new supply right after call $Y_2$, so we need $Y_2\ge5$:
$$1-\sum_{t=2}^4\binom{t-1}1\Bigl(\frac12\Bigr)^t=1-\Bigl(\frac14+\frac28+\frac3{16}\Bigr)=\frac5{16}.$$

(f) Look only at the calls to homes with a dog; there the door is answered with probability $\frac34$, independently. $D_m$ is the number of unanswered such calls before the $m$th answered one, a Pascal count minus $m$ as in part (b) of the previous problem with "success" probability $\frac14$:
$$E[D_m]=\frac{m\cdot\frac14}{\frac34}=\frac m3,\qquad\mathrm{Var}(D_m)=\frac{m\cdot\frac14}{(\frac34)^2}=\frac{4m}9.$$
:::
