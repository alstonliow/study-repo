<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18650f16-7-q2" status="draft"}
1. Compare the recovery times of patients given a new treatment with those given the standard one, without assuming any parametric form: if the two distributions are equal, the treatment makes no difference at all, not just in the mean.

2. By the probability integral transform (@lem-probability-integral-transform) each $U_i$ and each $V_j$ is uniform on $[0,1]$.

3. a) Both $F_n$ and $G_m$ are right-continuous step functions that are constant between consecutive points of the pooled sample $Z_{(1)}<\dots<Z_{(n+m)}$ (distinct with probability $1$), and both vanish before $Z_{(1)}$ and equal $1$ from $Z_{(n+m)}$ on. So $|F_n-G_m|$ takes only the values it has at the pooled points:
   $$T_{n,m}=\max_{1\le k\le n+m}\bigl|F_n(Z_{(k)})-G_m(Z_{(k)})\bigr| .$$

   b) Under $H_0$, $G=F$, so $V_j=F(Y_j)$, and since $F$ is increasing, $X_i\le t\iff U_i\le F(t)$ and $Y_j\le t\iff V_j\le F(t)$. Hence $F_n(t)-G_m(t)=\frac1n\sum_i\mathbf 1_{U_i\le F(t)}-\frac1m\sum_j\mathbf 1_{V_j\le F(t)}$. As $t$ ranges over $\mathbb{R}$, $x=F(t)$ ranges over $(0,1)$; at $x=0$ and $x=1$ the difference is $0$ (with probability $1$), so the supremum can be taken over $[0,1]$.

   c) They are independent (functions of independent variables) and each is $U[0,1]$: the joint law is uniform on $[0,1]^{n+m}$.

   d) By (b), $T_{n,m}$ is a fixed function of $(U_1,\dots,U_n,V_1,\dots,V_m)$, whose law by (c) does not depend on $F$. So the null law of $T_{n,m}$ depends only on $n$ and $m$.

   e) As in @def-simulated-null-quantile: for $k=1,\dots,M$ (say $M=10^5$), draw $n+m$ independent uniforms, compute $T^{(k)}$ from the formula in (a) applied to them, and take $\hat q_\alpha$ to be the $\lceil(1-\alpha)M\rceil$-th smallest of $T^{(1)},\dots,T^{(M)}$. As $M\to\infty$, $\hat q_\alpha\to q_\alpha$.

   f) $\psi=\mathbf 1\{T_{n,m}>q_\alpha\}$. Under $H_0$, $\Pr(T_{n,m}>q_\alpha)\le\alpha$ for every $n,m$ by the definition of the quantile (with equality up to the discreteness of the null law), so $\psi$ has non-asymptotic level $\alpha$.
:::

::: {.solution for="prob-mit18650f16-7-q3" status="draft"}
Since the distribution is continuous, ties occur with probability $0$ and the ranks are well defined; we ignore that null event.

1. Are the hours of sleep and the reaction time of drivers independent? Ranks avoid assuming a linear or Gaussian relationship.

2. $(R_1,\dots,R_n)$ is always a permutation of $(1,\dots,n)$: the ranks must be distinct and $\sum_iR_i=n(n+1)/2$. Knowing $R_1=1$, for instance, forces $R_2\ne1$.

3. Let $\sigma$ be any permutation of $\{1,\dots,n\}$. The vector $(X_{\sigma(1)},\dots,X_{\sigma(n)})$ has the same law as $(X_1,\dots,X_n)$ (i.i.d. coordinates), and the event $\{R=\pi\}$ for a permutation $\pi$ corresponds, for the permuted sample, to $\{R=\pi\circ\sigma\}$. Hence all $n!$ rank vectors have the same probability, $1/n!$, whatever the common continuous distribution. The same argument applies to the $Q_i$.

4. Under $H_0$ the pairs are i.i.d. with $X_1\perp Y_1$, so the whole vector $(X_1,\dots,X_n)$ is independent of $(Y_1,\dots,Y_n)$ (the joint density factors). $R$ is a function of the first vector and $Q$ of the second, so they are independent.

5. By parts 3 and 4, under $H_0$ the pair $(R,Q)$ is uniform on the $(n!)^2$ pairs of permutations, whatever the original distribution.

6. a) $R$ is a permutation of $1,\dots,n$, so $\sum_iR_i=n(n+1)/2$ and $\bar R_n=(n+1)/2$; and
   $$\sum_i(R_i-\bar R_n)^2=\sum_ii^2-n\bar R_n^2=\frac{n(n+1)(2n+1)}6-\frac{n(n+1)^2}4=\frac{n(n+1)(n-1)}{12}.$$
   The same holds for $Q$.

   b) $\sum_i(R_i-\bar R_n)(Q_i-\bar Q_n)=\sum_iR_iQ_i-n\bar R_n\bar Q_n=\sum_iR_iQ_i-\frac{n(n+1)^2}4$. Divide by $\frac{n(n^2-1)}{12}$ (the square root of the product of the two equal sums of squares): $T_n=\frac{12}{n(n^2-1)}\sum_iR_iQ_i-\frac{3(n+1)^2}{n^2-1}$, and $\frac{(n+1)^2}{n^2-1}=\frac{n+1}{n-1}$.

7. By part 6b, $T_n$ is a fixed function of $(R,Q)$. Under $H_0$, $(R,Q)$ has the law of part 5. Two independent uniform samples also satisfy $H_0$ and have continuous distributions, so their rank vectors $(R',Q')$ have the same law, and $S_n$, the same function of $(R',Q')$, has the law of $T_n$.

8. Repeat $M$ times: draw two independent vectors of $n$ uniforms (or, equivalently, two independent random permutations), compute their ranks and $S_n^{(k)}$ by the formula of 6b. Estimate $q_\alpha$ by the $\lceil(1-\alpha)M\rceil$-th smallest $S_n^{(k)}$ (@def-simulated-null-quantile).

9. The null law of $S_n$ is symmetric about $0$ (replacing $Q'$ by $n+1-Q'$ preserves its law and changes $S_n$ to $-S_n$). The test $\mathbf 1\{|T_n|>q_{\alpha/2}\}$ rejects with probability at most $\alpha$ under $H_0$, for every $n$. Against the one-sided alternative of positive association, $\mathbf 1\{T_n>q_\alpha\}$ has level $\alpha$. ($T_n$ is *Spearman's rank correlation*.)
:::
