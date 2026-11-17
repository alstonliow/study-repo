<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-sequences-02" status="draft"}
(a) $a_1 = 2$, $a_2 = 2\cdot2\cdot2 = 8$, $a_3 = 6\cdot8 = 48$,
    $a_4 = 8\cdot48 = 384$, $a_5 = 10\cdot384 = 3840$.

(b) Let $P(n)$ be the statement $a_n = 2^n n!$.

    1. *Base case.* $a_1 = 2 = 2^1\cdot1!$.

    2. *Inductive step.* Let $n\ge2$ and assume $P(n-1)$. Then
       $$a_n = 2n\,a_{n-1} = 2n\cdot2^{n-1}(n-1)! = 2^n\,n!.$$

    3. By induction, $P(n)$ holds for all $n\ge1$.
:::

::: {.solution for="prob-sequences-03" status="draft"}
(a) $b_1 = 3$, $b_2 = 9$, $b_3 = 81$, $b_4 = 6561$, $b_5 = 43{,}046{,}721$.
    Each term is $3$ raised to a power, and the exponent doubles each time:
    $3^1, 3^2, 3^4, 3^8, 3^{16}$.

(b) $b_n = 3^{2^{n-1}}$.

(c) 1. *Base case.* $b_1 = 3 = 3^{2^0}$.

    2. *Inductive step.* Let $n\ge2$ and assume $b_{n-1} = 3^{2^{n-2}}$. Then
       $$b_n = b_{n-1}^2 = \bigl(3^{2^{n-2}}\bigr)^2 = 3^{2\cdot2^{n-2}} = 3^{2^{n-1}}.$$

    3. By induction, the formula holds for all $n\ge1$.
:::

::: {.solution for="prob-sequences-04" status="draft"}
(a) $3, 5, 9, 17, 33, 65, 129$. The differences $2, 4, 8, 16, 32, 64$ double
    each time.

(b) $q_n = 2^n + 1$.

(c) 1. *Base cases.* $q_1 = 3 = 2^1 + 1$ and $q_2 = 5 = 2^2 + 1$.

    2. *Inductive step.* Let $n\ge3$ and assume the formula for $n-1$ and
       $n-2$. Then
       $$q_n = 3(2^{n-1}+1) - 2(2^{n-2}+1) = 3\cdot2^{n-1} - 2^{n-1} + 3 - 2 = 2^n + 1.$$

    3. By (strong) induction, the formula holds for all $n\ge1$.
:::

::: {.solution for="prob-sequences-05" status="draft"}
Let $P(n)$ be the statement $g_n\le n\log n - n + H_n$.

1. *Base case.* $g_1 = 0$, and the right-hand side is
   $1\cdot0 - 1 + 1 = 0$.

2. *Inductive step.* Let $n\ge2$ and assume $P(n-1)$:
   $$g_n = g_{n-1} + \log n\le (n-1)\log(n-1) - (n-1) + H_{n-1} + \log n.$$

3. By the hint, $\log(n-1) = \log n + \log\bigl(1 - \frac1n\bigr)\le\log n - \frac1n$.
   Since $n-1\ge0$,
   $$(n-1)\log(n-1)\le(n-1)\log n - \frac{n-1}n = (n-1)\log n - 1 + \frac1n.$$

4. Substituting into step 2:
   $$g_n\le (n-1)\log n - 1 + \frac1n - n + 1 + H_{n-1} + \log n = n\log n - n + \Bigl(H_{n-1} + \frac1n\Bigr) = n\log n - n + H_n.$$

5. This is $P(n)$. By induction, $P(n)$ holds for all $n\ge1$.
:::

::: {.solution for="prob-sequences-06" status="draft"}
**Explore.** $r_1, \dots, r_6 = 1, 2, 5, 14, 41, 122$. Each term is a bit less
than $3$ times the previous one.

**A simple bound.** $r_n\le3^{n-1}$. By induction: $r_1 = 1 = 3^0$, and if
$r_{n-1}\le3^{n-2}$, then $r_n = 3r_{n-1} - 1 < 3^{n-1}$.

**An exact formula.** Comparing with powers of $3$: $2r_n - 1 = 1, 3, 9, 27, 81, \dots$.
So conjecture
$$r_n = \frac{3^{n-1}+1}2.$$

1. *Base case.* $r_1 = \frac{1+1}2 = 1$.

2. *Inductive step.* Let $n\ge2$ and assume $r_{n-1} = \frac{3^{n-2}+1}2$. Then
   $$r_n = 3\cdot\frac{3^{n-2}+1}2 - 1 = \frac{3^{n-1} + 3 - 2}2 = \frac{3^{n-1}+1}2.$$

3. By induction, the formula holds for all $n\ge1$.

(This also follows from rewriting the recurrence as
$r_n - \frac12 = 3\bigl(r_{n-1} - \frac12\bigr)$.)
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6042f10-8-q1" status="draft"}
Use the Akra–Bazzi formula (@sec-math-discrete-sequences-solving-recurrences): find $p$ with $\sum a_ib_i^p=1$, then $T(n)=\Theta\bigl(n^p(1+\int_1^n\frac{g(u)}{u^{p+1}}du)\bigr)$. The floors and the small additive terms are allowed perturbations.

(a) $8\cdot2^{-p}=1$ gives $p=3$; $\int_1^nu^{-3}du=\Theta(1)$, so $T(n)=\Theta(n^3)$.

(b) $2\cdot8^{-p}=1$ gives $p=\frac13$; $\int_1^nu^{-1/3}du=\Theta(n^{2/3})$, so $T(n)=\Theta(n)$.

(c) $p$ solves $7\cdot20^{-p}+2\cdot8^{-p}=1$; at $p=1$ the left side is $\frac7{20}+\frac28=0.6<1$, so $p<1$. Then $\int_1^nu^{-p}du=\Theta(n^{1-p})$ and $T(n)=\Theta(n)$.

(d) $2\cdot4^{-p}=1$ gives $p=\frac12$; $\int_1^n\frac{u^{1/2}}{u^{3/2}}du=\ln n$, so $T(n)=\Theta(\sqrt n\log n)$.

(e) $3\cdot9^{-p}=1$ gives $p=\frac12$; with $g=1$, $\int_1^nu^{-3/2}du=\Theta(1)$, so $T(n)=\Theta(\sqrt n)$. (The perturbation $n^{1/9}$ is $O(n/\log^2n)$.)
:::

::: {.solution for="prob-mit6042f10-8-q2" status="draft"}
(a) "$T(n)=O(n)$" is a statement about the whole function $T$, not about a single value $n$, so it cannot serve as the induction predicate $P(n)$: every single value is $O(1)$. Hidden in the step is a growing constant: if $T(n/2)\le c\frac n2$, the step only gives $T(n)\le(2c+1)n$, and the constant doubles at every level of the recursion.

(b) The step would read: $T(n)=4T(n/2)+n\le4c\frac n2+n=(2c+1)n$, using $P(n/2)$ (when $n/2\ge n_0$). To finish we would need $(2c+1)n\le cn$, which is false for $c>0$. So the step fails and no contradiction is reached; the attempt proves nothing. (Also the hypothesis is not available when $n/2<n_0$.)

(c) $4\cdot2^{-p}=1$ gives $p=2$, and $\int_1^nu^{-2}du=\Theta(1)$, so $T(n)=\Theta(n^2)$; in particular $T(n)\ne O(n)$.

(d) For $a\ge1$, $b>1$: $T(n)=O(n)$ if and only if $a<b$. By Akra–Bazzi, $p=\log_ba$; if $a<b$ then $p<1$ and $T(n)=\Theta(n)$; if $a=b$ then $T(n)=\Theta(n\log n)$; if $a>b$ then $T(n)=\Theta(n^{\log_ba})$.

Direct proof of sufficiency: let $a<b$ and $c=\max\bigl(\frac b{b-a},\ \max_{1\le n<b}\frac{T(n)}n\bigr)$. We show $T(n)\le cn$ by strong induction. For $n<b$ it holds by the choice of $c$. For $n\ge b$, $1\le\lfloor n/b\rfloor<n$, so
$$T(n)=aT(\lfloor n/b\rfloor)+n\le ac\frac nb+n=\Bigl(\frac{ac}b+1\Bigr)n\le cn,$$
because $c\ge\frac b{b-a}$ is equivalent to $\frac{ac}b+1\le c$.
:::

::: {.solution for="prob-mit6042f10-8-q4" status="draft"}
(a) The characteristic equation $r^3-4r^2+r+6=0$ has the root $r=-1$, and $r^3-4r^2+r+6=(r+1)(r-2)(r-3)$. So $x_n=a(-1)^n+b2^n+c3^n$ (@thm-distinct-roots). The initial values give $a+b+c=3$, $-a+2b+3c=4$, $a+4b+9c=14$, whose solution is $a=b=c=1$:
$$x_n=(-1)^n+2^n+3^n.$$

(b) The homogeneous part $r^2+r-2=(r+2)(r-1)$ has roots $-2$ and $1$. Since $1$ is a root, try a particular solution $An^2+Bn$: substituting gives $A=\frac16$, $B=\frac7{18}$. So $x_n=c_1(-2)^n+c_2+\frac{n^2}6+\frac{7n}{18}$, and $x_0=5$, $x_1=-\frac49$ give $c_1=2$, $c_2=3$:
$$x_n=2(-2)^n+3+\frac{n^2}6+\frac{7n}{18}.$$
(Check: $x_2=-x_1+2x_0+2=\frac{112}9$, and the formula gives $8+3+\frac46+\frac{14}{18}=\frac{112}9$.)
:::

::: {.solution for="prob-mit6006s20-2-q1" status="draft"}
(a) $T(n)=\Theta(n^2)$. *Tree:* level $i$ has $4^i$ nodes of size $n/2^i$, costing at most $c\,4^i\cdot n/2^i=c\,2^in$; over $\log_2n$ levels this is $O(n^2)$, and the $4^{\log_2n}=n^2$ leaves cost $\Theta(n^2)$. *Master theorem* (@thm-master-theorem): $p=\log_24=2$ and $f(n)=O(n)=O(n^{2-\varepsilon})$, case 1.

(b) $T(n)=O(n^4)$ and $T(n)=\Omega(n^{2\log_23})$ (note $2\log_23\approx3.17$); since the extra work is only bounded above, nothing tighter follows. *Master theorem:* $p=\log_{\sqrt2}3=2\log_23<4$. With $f(n)=\Theta(n^4)$ case 3 applies (regularity: $3(n/\sqrt2)^4=\frac34n^4$), giving the upper bound; with $f(n)=0$ case 1 gives the lower bound. *Tree:* level $i$ costs at most $3^i c(n/\sqrt2^{\,i})^4=cn^4(3/4)^i$, a decreasing geometric series summing to $O(n^4)$, and the $3^{\log_{\sqrt2}n}=n^{2\log_23}$ leaves give the lower bound.

(c) $T(n)=\Theta(n\log^2n)$. *Tree:* level $i$ has $2^i$ nodes of size $n/2^i$, costing $2^i\cdot5\frac n{2^i}\log\frac n{2^i}=5n(\log n-i)$; summing over $i<\log n$ gives $5n\sum_{j=1}^{\log n}j=\Theta(n\log^2n)$. *Master theorem:* $p=1$, $f(n)=\Theta(n\log n)$, case 2 with $k=1$.

(d) $T(n)=\Theta(n^2)$. *Upper bound:* guess $T(n)\le cn^2$ and suppose $T(n)\le T(n-2)+an$ for large $n$. Then $T(n)\le c(n-2)^2+an=cn^2-(4c-a)n+4c\le cn^2$ when $4c>a$ and $n\ge2$ (large constants handle the base cases). *Lower bound:* guess $T(n)\ge c'n^2$ with $T(n)\ge T(n-2)+bn$. Then $T(n)\ge c'(n-2)^2+bn=c'n^2+(b-4c')n+4c'\ge c'n^2$ when $c'\le b/4$.
:::
