<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camii-pms-7-q6" status="draft"}
1. *(i)* For $t\neq0$, $\int_a^be^{itx}dx=\frac{e^{itb}-e^{ita}}{it}$, of modulus at most $\frac2{|t|}\to0$.

2. *(ii)* By linearity (i) holds for step functions. Given $\varepsilon>0$, choose a step function $g$ with $\|f-g\|_1<\varepsilon$ (problem 4.5). Then $|\hat f(t)|\le|\hat f(t)-\hat g(t)|+|\hat g(t)|\le\|f-g\|_1+|\hat g(t)|$, so $\limsup_{|t|\to\infty}|\hat f(t)|\le\varepsilon$.

3. *(iii) Set-up.* By (ii) and @prp-fourier-bounded-continuous, $F:f\mapsto\hat f$ maps $L^1$ into the Banach space $C_0$ with the sup norm; it is linear, bounded ($\|\hat f\|_\infty\le\|f\|_1$) and injective (@cor-fourier-uniqueness). If it were onto, the open mapping theorem would make $F^{-1}$ bounded: $\|f\|_1\le K\|\hat f\|_\infty$ for some $K$.

4. *A family violating this.* For $n\ge1$ let $h_n(u)=\frac12\big(\mathbf 1_{[-n,n]}*\mathbf 1_{[-1,1]}\big)(u)$, a trapezoid with values in $[0,1]$, continuous and of compact support. Its transform is $\hat h_n(x)=\frac12\cdot\frac{2\sin nx}x\cdot\frac{2\sin x}x$ (@prp-convolution-properties), which is integrable ($O(x^{-2})$ at infinity, bounded near $0$). Put $f_n(x)=\frac1{2\pi}\hat h_n(x)=\frac{\sin nx\,\sin x}{\pi x^2}$, an even integrable function.

5. By the inversion formula (@thm-fourier-inversion) applied to $h_n$ and evenness, $\hat f_n=h_n$; hence $\|\hat f_n\|_\infty=1$.

6. On $(0,1]$, $\sin x\ge\frac{2x}\pi$, so $\|f_n\|_1\ge\frac2{\pi^2}\int_0^1\frac{|\sin nx|}xdx=\frac2{\pi^2}\int_0^n\frac{|\sin y|}y\,dy\to\infty$ (problem 3.6). This contradicts $\|f_n\|_1\le K$. So $F$ is not onto $C_0$.
:::

::: {.solution for="prob-camii-pms-7-q7" status="draft"}
1. *The tent function.* Let $Df=\mathbf 1_{(-1,0)}-\mathbf 1_{(0,1)}$. $f$ is $1$-Lipschitz and affine with slope $Df$ on each of $(-\infty,-1),(-1,0),(0,1),(1,\infty)$. So $q_h=\frac{\tau_hf-f}h-Df$ vanishes at $x$ unless $[x,x+h]$ (or $[x+h,x]$) contains one of $-1,0,1$, a set of measure at most $3|h|$, and $|q_h|\le2$ everywhere. Hence $\|q_h\|_2^2\le4\cdot3|h|\to0$: $f$ is $L^2$-differentiable with derivative $Df$.

2. *Transform of a difference quotient.* With $\hat f(u)=\int f(x)e^{iux}dx$, $\widehat{\tau_hf}(u)=e^{-iuh}\hat f(u)$. Let $g_h=(\tau_hf-f)/h\in L^1\cap L^2$; then $\hat g_h(u)=\frac{e^{-iuh}-1}h\hat f(u)$.

3. $g_h\to Df$ in $L^2$, so $(g_h)$ is Cauchy in $L^2$ as $h\to0$, and by Plancherel (@thm-plancherel) so is $(\hat g_h)$: it converges in $L^2$ to some $G$, and along a sequence $h_k\to0$, $\hat g_{h_k}\to G$ a.e. (@thm-lp-complete).

4. Pointwise $\frac{e^{-iuh}-1}h\to-iu$, so $G(u)=-iu\hat f(u)$ a.e. Hence $u\hat f(u)\in L^2$. Also $\hat f\in L^2$ by Plancherel, so $(1+|u|)\hat f\in L^2$.

5. *Sobolev inequality.* By Cauchy–Schwarz,
$$\|\hat f\|_1=\int\frac{(1+|u|)|\hat f(u)|}{1+|u|}du\le\|(1+|u|)\hat f\|_2\Big(\int\frac{du}{(1+|u|)^2}\Big)^{1/2}=\sqrt2\,\|(1+|u|)\hat f\|_2 .$$

6. So $\hat f\in L^1$, and by @thm-fourier-inversion $f$ agrees a.e. with the continuous function $x\mapsto\frac1{2\pi}\int\hat f(u)e^{-iux}du$, which is bounded by $\frac1{2\pi}\|\hat f\|_1$. Therefore $\|f\|_\infty\le C\|(1+|u|)\hat f\|_2$ with $C=\frac{\sqrt2}{2\pi}=\frac1{\sqrt2\,\pi}$.
:::
