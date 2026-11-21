<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camii-pms-3-q1" status="draft"}
1. The sets $A_\varepsilon\cap B_\delta$ ($\varepsilon\in\{0,1\}^m$, $\delta\in\{0,1\}^n$) are measurable, pairwise disjoint and cover $E$: each $x$ lies in exactly the one with $\varepsilon_k=\mathbf 1_{A_k}(x)$, $\delta_j=\mathbf 1_{B_j}(x)$.

2. $A_k$ is the disjoint union of those $A_\varepsilon\cap B_\delta$ with $\varepsilon_k=1$. By additivity
$$a_k\mu(A_k)=\sum_{\varepsilon,\delta}\varepsilon_ka_k\,\mu(A_\varepsilon\cap B_\delta)$$
(the convention $0\cdot\infty=0$ makes this right also when $a_k=0$).

3. Sum over $k$ and exchange the finite sums: $\sum_ka_k\mu(A_k)=\sum_{\varepsilon,\delta}\big(\sum_k\varepsilon_ka_k\big)\mu(A_\varepsilon\cap B_\delta)$. Empty sets $A_\varepsilon\cap B_\delta$ contribute $0$ whatever the coefficient, so the coefficient may be replaced by $f_{\varepsilon,\delta}$. This is the first identity.

4. On a non-empty $A_\varepsilon\cap B_\delta$, take any point $x$: $f(x)=\sum_k\varepsilon_ka_k$ by the first representation and $f(x)=\sum_j\delta_jb_j$ by the second. So $f_{\varepsilon,\delta}$ equals $g_{\varepsilon,\delta}$, defined symmetrically from the $b_j$.

5. The same computation for the second representation gives $\sum_jb_j\mu(B_j)=\sum_{\varepsilon,\delta}g_{\varepsilon,\delta}\mu(A_\varepsilon\cap B_\delta)$, and by step 4 the right-hand sides agree.
:::

::: {.solution for="prob-camii-pms-3-q3" status="draft"}
This is @prp-integral-pi-system; the proof in steps:

1. Let $\mathcal D=\{A\in\mathcal E:\ \mu(f\mathbf 1_A)=0\}\supseteq\mathcal A$; in particular $E\in\mathcal D$.

2. If $A\subseteq B$ are in $\mathcal D$, then $\mu(f\mathbf 1_{B\setminus A})=\mu(f\mathbf 1_B)-\mu(f\mathbf 1_A)=0$.

3. If $A_n\uparrow A$ with $A_n\in\mathcal D$, then $\mu(f^\pm\mathbf 1_{A_n})\uparrow\mu(f^\pm\mathbf 1_A)$ by monotone convergence, both limits finite, so $\mu(f\mathbf 1_A)=\lim\mu(f\mathbf 1_{A_n})=0$.

4. So $\mathcal D$ is a d-system, and $\mathcal D=\mathcal E$ by Dynkin's lemma.

5. With $A=\{f>0\}$: $\mu(f^+)=\mu(f\mathbf 1_A)=0$, so $f^+=0$ a.e.; with $A=\{f<0\}$, $f^-=0$ a.e.
:::

::: {.solution for="prob-camii-pms-3-q5" status="draft"}
1. $f_\alpha\mathbf 1_{[1/n,1]}\uparrow f_\alpha\mathbf 1_{(0,1]}$, so by monotone convergence $\int_{(0,1]}f_\alpha\,d\lambda=\lim_n\int_{1/n}^1x^{-\alpha}dx$, where on the compact interval the Lebesgue integral of the continuous function equals the Riemann integral (@thm-riemann-is-lebesgue).

2. $\int_{1/n}^1x^{-\alpha}dx=\frac{1-n^{\alpha-1}}{1-\alpha}$ for $\alpha\neq1$ and $=\log n$ for $\alpha=1$. The limit is $\frac1{1-\alpha}<\infty$ if $\alpha<1$ and $\infty$ if $\alpha\ge1$.

3. Similarly $\int_{[1,\infty)}f_\alpha=\lim_n\int_1^nx^{-\alpha}dx$, with $\int_1^nx^{-\alpha}dx=\frac{n^{1-\alpha}-1}{1-\alpha}$ ($\alpha\ne1$) or $\log n$. The limit is $\frac1{\alpha-1}$ for $\alpha>1$ and $\infty$ for $\alpha\le1$.
:::

::: {.solution for="prob-camii-pms-3-q6" status="draft"}
1. On $[k\pi,(k+1)\pi]$ ($k\ge1$), $\frac{|\sin x|}x\ge\frac{|\sin x|}{(k+1)\pi}$ and $\int_{k\pi}^{(k+1)\pi}|\sin x|dx=2$. So $\int_{[1,\infty)}\frac{|\sin x|}x\,dx\ge\sum_{k\ge1}\frac2{(k+1)\pi}=\infty$: the function is not integrable.

2. Integrate by parts on $[1,N]$: $\int_1^N\frac{\sin x}x\,dx=\cos1-\frac{\cos N}N-\int_1^N\frac{\cos x}{x^2}\,dx$.

3. $\frac{\cos N}N\to0$, and $\big|\frac{\cos x}{x^2}\big|\le x^{-2}$ is integrable on $[1,\infty)$ (problem 3.5), so $\int_1^N\frac{\cos x}{x^2}dx\to\int_{[1,\infty)}\frac{\cos x}{x^2}dx$ by dominated convergence. Hence the limit exists.
:::

::: {.solution for="prob-camii-pms-3-q9" status="draft"}
1. For $g=\mathbf 1_A$, $A\in\mathcal G$: $g\circ f=\mathbf 1_{f^{-1}(A)}$, so $\mu(g\circ f)=\mu(f^{-1}(A))=\nu(A)=\nu(g)$.

2. For simple $g=\sum_ka_k\mathbf 1_{A_k}$, both sides are linear in $g$, so the identity holds.

3. For measurable $g\ge0$, choose simple $g_n\uparrow g$ (@prp-dyadic-approximation). Then $g_n\circ f\uparrow g\circ f$, and monotone convergence on both sides gives $\nu(g)=\lim\nu(g_n)=\lim\mu(g_n\circ f)=\mu(g\circ f)$.
:::
