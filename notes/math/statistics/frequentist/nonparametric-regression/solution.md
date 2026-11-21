<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18650f16-9-q1" status="draft"}
1. $I_i=\{\max(0,i-k),\dots,\min(n,i+k)\}$, so $|I_i|=\min(i,k)+\min(n-i,k)+1\le2k+1$. For the lower bound: if $i\ge k$ the first term is $k$; if $i<k$, then $\min(n-i,k)\ge k-i$ because $n\ge k$, so the two terms add to at least $i+(k-i)=k$. Hence $|I_i|\ge k+1$.

2. a) The $Y_j$ are independent with variance $\sigma^2$, so $\operatorname{Var}(\hat f_i)=\sigma^2/|I_i|\le\sigma^2/(k+1)\le\sigma^2/k$.

   b) $E[\hat f_i]=\frac1{|I_i|}\sum_{j\in I_i}f(x_j)$, so $b_i=\frac1{|I_i|}\sum_{j\in I_i}\bigl(f(x_j)-f(x_i)\bigr)$ and the bound is the triangle inequality.

   c) By the mean value theorem $|f(x_j)-f(x_i)|\le L|x_j-x_i|=L|j-i|/n\le Lk/n$ for $j\in I_i$. So $|b_i|\le Lk/n$.

   d) Quadratic risk $=b_i^2+\operatorname{Var}(\hat f_i)$ (@prp-mse-bias-variance); combine (a) and (c). This is @prp-local-average-bias-variance with window $h=k/n$.

   e) Minimise $\varphi(k)=\frac{L^2k^2}{n^2}+\frac{\sigma^2}k$ over $k>0$: $\varphi'(k)=\frac{2L^2k}{n^2}-\frac{\sigma^2}{k^2}=0$ gives
   $$k^*=\Bigl(\frac{\sigma^2n^2}{2L^2}\Bigr)^{1/3},$$
   to be rounded to an integer in $[1,n]$ ($\varphi$ is convex, so the nearer of the two neighbouring integers is optimal).

   f) Substituting, $\varphi(k^*)=\frac3{2^{2/3}}\,L^{2/3}\sigma^{4/3}\,n^{-2/3}$: the risk tends to $0$ at rate $n^{-2/3}$ (slower than the parametric $1/n$).

   g) Take $k=\lceil n^{2/3}\rceil$, so $n^{2/3}\le k\le2n^{2/3}$ and $k\le n$. Then $\frac{L^2k^2}{n^2}\le4L^2n^{-2/3}$ and $\frac{\sigma^2}k\le\sigma^2n^{-2/3}$, so the risk is at most $(4L^2+\sigma^2)n^{-2/3}$; only the constant is worse.

3. Let $x\in[x_i,x_{i+1}]$ and $x=(1-t)x_i+tx_{i+1}$, $t\in[0,1]$. Then
   $$\hat f(x)-f(x)=(1-t)\bigl(\hat f_i-f(x_i)\bigr)+t\bigl(\hat f_{i+1}-f(x_{i+1})\bigr)+\bigl[(1-t)f(x_i)+tf(x_{i+1})-f(x)\bigr].$$
   The bracket is at most $L/n$ in absolute value, since $|f(x_i)-f(x)|$ and $|f(x_{i+1})-f(x)|$ are at most $L/n$. Using $(a+b+c)^2\le3(a^2+b^2+c^2)$ and part 2(d),
   $$E\bigl[(\hat f(x)-f(x))^2\bigr]\le3\Bigl(\frac{L^2k^2}{n^2}+\frac{\sigma^2}k+\frac{L^2}{n^2}\Bigr)\le\frac{6L^2k^2}{n^2}+\frac{3\sigma^2}k$$
   for every $x$ (using $k\ge1$). Integrating over $[0,1]$ and exchanging $E$ and $\int$ (Tonelli; the integrand is non-negative) gives the bound with $c_1=6L^2$, $c_2=3\sigma^2$. With $k=\lceil n^{2/3}\rceil$, as in 2(g), $R(\hat f,f)\le(24L^2+3\sigma^2)n^{-2/3}$.
:::

::: {.solution for="prob-mit18650f16-9-q2" status="draft"}
Let $p_h=\Pr(|X_1-x|\le h)=F(x+h)-F(x-h)$; since $[x-h,x+h]\subseteq[0,1]$, $p_h=\int_{x-h}^{x+h}f$.

1. Each indicator is $\operatorname{Ber}(p_h)$, and they are independent.

2. $E[(\hat f(x)-f(x))^2]=b(x)^2+\sigma^2(x)$ (@prp-mse-bias-variance).

3. $E[\hat f(x)]=\frac{np_h}{2nh}=\frac{p_h}{2h}$, so $b(x)=\frac{F(x+h)-F(x-h)}{2h}-f(x)$, which is the stated formula.

4. $F'=f$ and $F''=f'$ exist, so Taylor's formula with Lagrange remainder gives $F(x\pm h)=F(x)\pm hf(x)+\frac{h^2}2f'(\xi_\pm)$ for some $\xi_\pm$ between $x$ and $x\pm h$. Hence $F(x+h)-F(x-h)-2hf(x)=\frac{h^2}2\bigl(f'(\xi_+)-f'(\xi_-)\bigr)$, of absolute value at most $h^2L$, and $|b(x)|\le\frac{h^2L}{2h}=\frac{Lh}2$.

5. $\sigma^2(x)=\frac{np_h(1-p_h)}{4n^2h^2}\le\frac{p_h}{4nh^2}$, and $p_h=\int_{x-h}^{x+h}f\le2hL$. So $\sigma^2(x)\le\frac{2hL}{4nh^2}=\frac L{2nh}$.

6. $E[(\hat f(x)-f(x))^2]\le\dfrac{L^2h^2}4+\dfrac L{2nh}$.

7. The bound is minimised at $h=(nL)^{-1/3}$, which needs $L$. Without $L$, take $h=n^{-1/3}$ (for $n$ large enough that $x\in(h,1-h)$): the bound becomes $\frac{L^2}4n^{-2/3}+\frac L2n^{-2/3}=Cn^{-2/3}$ with $C=\frac{L^2}4+\frac L2$.
:::
