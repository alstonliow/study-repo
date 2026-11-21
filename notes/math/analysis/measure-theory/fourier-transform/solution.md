<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camii-pms-7-q1" status="draft"}
1. By definition it suffices to prove the two identities for real integrable $u$. The maps $x\mapsto x-y$ and $x\mapsto-x$ carry $\lambda^d$ to itself: the image measures give each box its volume (a box translated or reflected is a box of the same side lengths), so they equal $\lambda^d$ by uniqueness. The image-measure formula (problem 3.9), applied to $u^\pm$, gives $\int u(x-y)\,dx=\int u$ and $\int u(-x)\,dx=\int u$.

2. Let $z=\int f$. If $z=0$ there is nothing to show. Otherwise write $z=re^{i\theta}$ with $r=|z|$. Then $r=e^{-i\theta}z=\int e^{-i\theta}f$, by linearity of the complex integral.

3. $r$ is real, so $r=\operatorname{Re}\int e^{-i\theta}f=\int\operatorname{Re}(e^{-i\theta}f)\le\int|e^{-i\theta}f|=\int|f|$.
:::

::: {.solution for="prob-camii-pms-7-q2" status="draft"}
This is @prp-fourier-bounded-continuous.

1. $|\hat\mu(u)|=\big|\int e^{i\langle u,x\rangle}\mu(dx)\big|\le\int1\,d\mu=\mu(\mathbb R^d)$ by problem 7.1's inequality (which holds for any measure).

2. If $u_n\to u$, then $e^{i\langle u_n,x\rangle}\to e^{i\langle u,x\rangle}$ for each $x$, with modulus $1$, integrable for the finite $\mu$. Dominated convergence (on real and imaginary parts) gives $\hat\mu(u_n)\to\hat\mu(u)$.
:::

::: {.solution for="prob-camii-pms-7-q4" status="draft"}
1. For $0\le j\le k$, $|x|^j\le1+|x|^k$, which is $\mu$-integrable because $\mu$ is finite.

2. By induction on $j\le k$: $\hat\mu^{(j)}(u)=\int(ix)^je^{iux}\mu(dx)$. For $j=0$ it is the definition. If true for $j<k$, the $u$-derivative of $(ix)^je^{iux}$ is $(ix)^{j+1}e^{iux}$, of modulus $|x|^{j+1}$, integrable and independent of $u$. @thm-differentiation-under-integral (on real and imaginary parts) gives the formula for $j+1$.

3. $\hat\mu^{(k)}$ is continuous by dominated convergence: $u\mapsto(ix)^ke^{iux}$ is continuous with modulus $|x|^k$.

4. At $u=0$: $\hat\mu^{(k)}(0)=i^k\int x^k\,d\mu$.
:::

::: {.solution for="prob-camii-pms-7-q5" status="draft"}
1. *$\psi$ is $C^\infty$.* Let $g(t)=e^{-1/t}$ for $t>0$ and $g(t)=0$ for $t\le0$. By induction $g^{(k)}(t)=p_k(1/t)e^{-1/t}$ for $t>0$ with polynomials $p_k$, and $p_k(s)e^{-s}\to0$ as $s\to\infty$; so every derivative extends continuously by $0$ at $t=0$, and $g$ is $C^\infty$. Then $\psi(x)=Cg(1-x^2)$ is $C^\infty$, with support $[-1,1]$, and each $\psi^{(k)}$ is bounded.

2. *Smoothness of $f*\psi$.* $(f*\psi)(x)=\int f(y)\psi(x-y)\,dy$. The $x$-derivative of order $k$ of the integrand is $f(y)\psi^{(k)}(x-y)$, bounded by $\|\psi^{(k)}\|_\infty|f(y)|$, integrable and independent of $x$. By @thm-differentiation-under-integral and induction, $f*\psi$ is $k$ times differentiable with $(f*\psi)^{(k)}=f*\psi^{(k)}$, which is continuous by dominated convergence. So $f*\psi\in C^\infty$.

3. *Compact support.* If $f=0$ a.e. outside $[-R,R]$ and $|x|>R+1$, then $\psi(x-y)=0$ for all $|y|\le R$, so $(f*\psi)(x)=0$.
:::
