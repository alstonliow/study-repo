<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camii-pms-1-q7" status="draft"}
1. *(⇐)* Choosing $A_n\in\sigma(A_n)$ in the definition of independent σ-algebras gives independence of the events.

2. *(⇒)* The collection $\mathcal P_n=\{\emptyset,A_n,\Omega\}$ is a π-system containing $\Omega$ and generating $\sigma(A_n)$.

3. For a finite set $J$ of indices and $B_j\in\mathcal P_j$: if some $B_j=\emptyset$ both sides of the product formula are $0$; the factors with $B_j=\Omega$ equal $1$ and can be dropped; what remains is the product formula for some of the $A_j$, true by independence.

4. By @thm-independence-pi-systems the σ-algebras $\sigma(\mathcal P_n)=\sigma(A_n)$ are independent.
:::

::: {.solution for="prob-camii-pms-2-q4" status="draft"}
1. $E[X_n]=n^2\Pr(A_n)-1=0$, so $E[\bar X_n]=0$ by linearity.

2. $\sum_n\Pr(A_n)=\sum_nn^{-2}<\infty$, so by the first Borel–Cantelli lemma (@lem-borel-cantelli) almost surely only finitely many $A_n$ occur. No independence is needed.

3. Fix such an outcome and $N$ with $\omega\notin A_n$ for $n>N$. Then $X_n(\omega)=-1$ for $n>N$, and
$$\bar X_n(\omega)=\frac{X_1(\omega)+\dots+X_N(\omega)}n-\frac{n-N}n\to-1 .$$
:::

::: {.solution for="prob-camii-pms-2-q5" status="draft"}
1. For any $m\ge1$, $\Pr(m\mid X)=\sum_k\frac{(mk)^{-s}}{\zeta(s)}=m^{-s}$.

2. For distinct primes $p_1,\dots,p_r$, $p_1,\dots,p_r$ all divide $X$ iff their product does, so $\Pr(A_{p_1}\cap\dots\cap A_{p_r})=(p_1\cdots p_r)^{-s}=\prod_i\Pr(A_{p_i})$. So the $A_p$ are independent, and so are their complements (@thm-independence-pi-systems with the π-systems $\{\emptyset,A_p,\Omega\}$).

3. $X=1$ iff no prime divides $X$. Let $p_1<p_2<\cdots$ be the primes; the events $\bigcap_{i\le r}A_{p_i}^c$ decrease to $\{X=1\}$, so by continuity from above
$$\frac1{\zeta(s)}=\Pr(X=1)=\lim_r\prod_{i\le r}(1-p_i^{-s})=\prod_p(1-p^{-s}).$$

4. Square-free: let $B_p=\{p^2\mid X\}$. As in step 2, $\Pr(B_{p_1}\cap\dots\cap B_{p_r})=(p_1\cdots p_r)^{-2s}$, so the $B_p$ are independent, and as in step 3 $\Pr(X\text{ square-free})=\prod_p(1-p^{-2s})$, which is $1/\zeta(2s)$ by Euler's formula at $2s>1$.

5. Highest common factor. Given $n\mid X$, $X/n$ has the law of $X$: $\Pr(X=nk\mid n\mid X)=\frac{(nk)^{-s}/\zeta(s)}{n^{-s}}=\frac{k^{-s}}{\zeta(s)}$. The same holds for $Y$, and independence of $X,Y$ is preserved under this conditioning (the joint conditional law is the product). Now $H=n$ iff $n\mid X$, $n\mid Y$ and $\gcd(X/n,Y/n)=1$. Hence
$$\Pr(H=n)=\Pr(n\mid X)\Pr(n\mid Y)\Pr(H=1)=n^{-2s}\Pr(H=1).$$

6. Summing over $n\ge1$: $1=\Pr(H=1)\,\zeta(2s)$, so $\Pr(H=n)=n^{-2s}/\zeta(2s)$.
:::

::: {.solution for="prob-camii-pms-2-q6" status="draft"}
1. *Gaussian tails.* For $x>0$ and $Z\sim N(0,1)$,
$$\frac{x}{1+x^2}\,\frac{e^{-x^2/2}}{\sqrt{2\pi}}\le\Pr(Z>x)\le\frac1x\,\frac{e^{-x^2/2}}{\sqrt{2\pi}} .$$
Upper: $\int_x^\infty e^{-t^2/2}dt\le\int_x^\infty\frac tx e^{-t^2/2}dt=\frac{e^{-x^2/2}}x$. Lower: $\frac{d}{dt}\big(-\frac{e^{-t^2/2}}t\big)=(1+t^{-2})e^{-t^2/2}$, so $\frac{e^{-x^2/2}}x=\int_x^\infty(1+t^{-2})e^{-t^2/2}dt\le(1+x^{-2})\int_x^\infty e^{-t^2/2}dt$.

2. *Upper bound.* Fix $\varepsilon>0$ and $x_n=(1+\varepsilon)\sqrt{2\log n}$. Then $\Pr(X_n>x_n)\le e^{-x_n^2/2}=n^{-(1+\varepsilon)^2}$ for $n\ge3$ (where $x_n\sqrt{2\pi}\ge1$), which is summable. By the first Borel–Cantelli lemma, a.s. $X_n\le x_n$ eventually, so $\limsup_nX_n/\sqrt{2\log n}\le1+\varepsilon$. Let $\varepsilon\downarrow0$ along a sequence.

3. *Lower bound.* Let $y_n=\sqrt{2\log n}$. For $n\ge3$, $\frac{y_n}{1+y_n^2}\ge\frac1{2y_n}$, so $\Pr(X_n>y_n)\ge\frac{1}{2\sqrt{2\pi}}\frac{1}{n\sqrt{2\log n}}$, whose sum diverges (compare with $\int\frac{dx}{x\sqrt{\log x}}=2\sqrt{\log x}$). The events are independent, so by the second Borel–Cantelli lemma $X_n>y_n$ infinitely often, a.s. Hence $\limsup_nX_n/y_n\ge1$.
:::
