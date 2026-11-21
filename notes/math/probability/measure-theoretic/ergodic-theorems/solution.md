<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camii-pms-9-q1" status="draft"}
1. $\tau^{-1}(\emptyset)=\emptyset$; $\tau^{-1}(A^c)=\tau^{-1}(A)^c=A^c$ for invariant $A$; $\tau^{-1}\big(\bigcup_nA_n\big)=\bigcup_n\tau^{-1}(A_n)=\bigcup_nA_n$. So $\mathcal E_\tau$ is a σ-algebra.

2. If $f\circ\tau=f$, then $\tau^{-1}(\{f\le a\})=\{f\circ\tau\le a\}=\{f\le a\}$, so every $\{f\le a\}$ is invariant and $f$ is $\mathcal E_\tau$-measurable (@lem-measurable-generator).

3. Conversely, if $f$ is $\mathcal E_\tau$-measurable, then $\{f\circ\tau\le a\}=\tau^{-1}(\{f\le a\})=\{f\le a\}$ for every $a$. If $f(\tau x)\neq f(x)$ for some $x$, say $f(\tau x)<a<f(x)$ for a rational $a$, then $x$ lies in $\{f\circ\tau\le a\}$ but not in $\{f\le a\}$, a contradiction; similarly in the other order. So $f\circ\tau=f$. (Measure preservation is not needed.)
:::

::: {.solution for="prob-camii-pms-9-q2" status="draft"}
1. For each $a$, $\{f\le a\}$ is invariant (problem 9.1), so it has measure $0$ or its complement $\{f>a\}$ has measure $0$.

2. If $\mu(E)=0$ every constant works; assume $\mu(E)>0$. Let $c=\inf\{a\in\mathbb Q:\ \mu(\{f>a\})=0\}$. If the set is empty, $\mu(\{f\le a\})=0$ for every rational $a$ and $\mu(E)=\lim_a\mu(\{f\le a\})=0$; if $c=-\infty$, $\mu(\{f>a\})=0$ for all rational $a$ and again $\mu(E)=0$. So $c\in\mathbb R$.

3. For rational $a>c$, $\mu(\{f>a\})=0$ (the condition is monotone in $a$); taking a countable union, $\mu(\{f>c\})=0$.

4. For rational $a<c$, $\mu(\{f>a\})>0$, so by step 1 $\mu(\{f\le a\})=0$; taking a countable union, $\mu(\{f<c\})=0$. Hence $f=c$ a.e.
:::

::: {.solution for="prob-camii-pms-9-q3" status="draft"}
1. *Measure-preserving.* $\tau^{-1}([s,t))=[\frac s2,\frac t2)\cup[\frac{s+1}2,\frac{t+1}2)$ has length $t-s$. The intervals $[s,t)$ with $\emptyset$ form a π-system generating $\mathcal B([0,1))$, and $\lambda\circ\tau^{-1}$, $\lambda$ are probability measures agreeing on it, so they are equal (@thm-uniqueness-of-extension).

2. *Coding by binary digits.* Let $R_k(x)$ be the $k$th binary digit (expansions not ending in all ones). Then $R_k(\tau x)=R_{k+1}(x)$, and under $\lambda$ the $R_k$ are i.i.d. fair bits (@thm-iid-sequence-exists). Let $\mathcal G_n=\sigma(R_{n+1},R_{n+2},\dots)$.

3. *Ergodic.* If $A$ is invariant then $A=\tau^{-n}(A)$. Every Borel set is in $\sigma(R_1,R_2,\dots)$ (dyadic intervals generate $\mathcal B$), and $\tau^{-n}(B)\in\mathcal G_n$ for $B\in\sigma(R_1,R_2,\dots)$ since $R_k\circ\tau^n=R_{k+n}$. So $A\in\bigcap_n\mathcal G_n$, a tail event of the independent $R_k$, and $\lambda(A)\in\{0,1\}$ by @thm-kolmogorov-zero-one.

4. *Limit.* By Birkhoff (@thm-birkhoff-ergodic) $\frac1n\sum_{k<n}f\circ\tau^k\to\overline f$ a.e., $\overline f$ is a.e. constant, and by von Neumann (@thm-von-neumann-ergodic, $p=1$) the convergence is in $L^1$, so the constant is $\lim E\big[\frac1n\sum_{k<n}f\circ\tau^k\big]=\int_0^1f\,dx$. So $\overline f=\int_0^1f(x)\,dx$ a.e.
:::

::: {.solution for="prob-camii-pms-9-q4" status="draft"}
1. *Measure-preserving.* $\tau^{-1}([s,t))$ is $[s,t)$ shifted by $-a$ modulo $1$: one or two intervals of total length $t-s$. Conclude as in problem 9.3.

2. *Rational $a$: not ergodic.* Let $a=p/q$ in lowest terms ($a=0$: $q=1$). If $q\ge2$, the set $A=\bigcup_{j=0}^{q-1}[\frac jq,\frac jq+\frac1{2q})$ is invariant ($\tau$ permutes the intervals $[\frac jq,\frac{j+1}q)$ by translation) with $\lambda(A)=\frac12$. If $a=0$, $\tau$ is the identity and every set is invariant. Not ergodic.

3. *Irrational $a$: ergodic.* Let $A$ be invariant and $f=\mathbf 1_A$, so $f\circ\tau=f$. Its Fourier coefficients $c_k=\int_0^1f(x)e^{-2\pi ikx}dx$ satisfy, by measure preservation (the image-measure formula for $g(x)=f(x)e^{-2\pi ikx}$, using $e^{-2\pi ik\tau(x)}=e^{-2\pi ika}e^{-2\pi ikx}$),
$$c_k=\int f(\tau x)e^{-2\pi ik\tau(x)}dx=e^{-2\pi ika}c_k .$$
For $k\neq0$, $ka\notin\mathbb Z$, so $e^{-2\pi ika}\neq1$ and $c_k=0$. Then $f-c_0$ has all Fourier coefficients $0$, so $f=c_0$ a.e.; as $f$ takes values in $\{0,1\}$, $\lambda(A)=c_0\in\{0,1\}$.

4. *Invariant function, irrational $a$:* as in problem 9.3, $\overline f=\int_0^1f\,dx$ a.e.

5. *Rational $a=p/q$:* $\tau^q$ is the identity, so for $n=mq+r$ ($0\le r<q$), $S_n(f)=m\sum_{j<q}f\circ\tau^j+S_r(f)$. Since $S_r(f)/n\to0$ pointwise, $\frac{S_n(f)}n\to\frac1q\sum_{j=0}^{q-1}f(x+ja\bmod1)=\frac1q\sum_{j=0}^{q-1}f\big(x+\tfrac jq\bmod1\big)$ (as $j$ runs over $0,\dots,q-1$, $jp\bmod q$ does too). This is $\overline f$; for $a=0$ it is $f$ itself.
:::

::: {.solution for="prob-camii-pms-9-q5" status="draft"}
1. Let $\Pi:\Omega\to\mathbb R^{\mathbb N}$, $\Pi(\omega)=(X_n(\omega))_n$, measurable for the product σ-algebra, and $\nu=\Pr\circ\Pi^{-1}$ the law of the sequence. Let $\Theta$ be the shift on $\mathbb R^{\mathbb N}$.

2. *$\Theta$ preserves $\nu$.* For a cylinder $C=A_1\times\dots\times A_n\times\mathbb R\times\cdots$, $\nu(\Theta^{-1}C)=\Pr(X_2\in A_1,\dots,X_{n+1}\in A_n)=\Pr(X_1\in A_1,\dots,X_n\in A_n)=\nu(C)$ by stationarity with $k=1$. Cylinders form a generating π-system, so $\nu\circ\Theta^{-1}=\nu$.

3. Let $f(x)=x_1$; $\int|f|^pd\nu=E|X_1|^p<\infty$. With $S_n(f)(x)=x_1+\dots+x_n$, Birkhoff and von Neumann (@thm-birkhoff-ergodic, @thm-von-neumann-ergodic) give an invariant $\bar f$ with $S_n(f)/n\to\bar f$ $\nu$-a.e. and in $L^p(\nu)$, and $\bar f\in L^p(\nu)$.

4. Put $X=\bar f\circ\Pi$. Then $\frac1n\sum_{i\le n}X_i=\frac{S_n(f)}n\circ\Pi$, so the convergence set has $\Pr$-probability equal to its $\nu$-measure, $1$; and $E\big|\frac1n\sum_{i\le n}X_i-X\big|^p=\int|S_n(f)/n-\bar f|^pd\nu\to0$ by the image-measure formula. Also $X\in L^p$.

5. $L^p$ convergence implies $L^1$ convergence on a probability space, so $E[X]=\lim_nE\big[\frac1n\sum_{i\le n}X_i\big]=E[X_1]$, using $E[X_i]=E[X_1]$ by stationarity.
:::
