<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit1801f06-8b-q1" status="draft"}
a) The limit is $0$ for every real $m$. For $m\le0$ both factors are bounded and $e^{-x}\to0$. For $m>0$ write it as $\frac{x^m}{e^x}$ ($\infty/\infty$) and apply @thm-lhopital $\lceil m\rceil$ times: each time the power drops by one while $e^x$ stays, until the numerator is $m(m-1)\cdots x^{m-\lceil m\rceil}$, which is bounded for $x\ge1$.

b) The integrand is continuous on $[0,\infty)$, so only the infinite end matters. By (a) with $m=n+2$, $\frac{x^ne^{-x}}{x^{-2}}=x^{n+2}e^{-x}\to0$, so $x^ne^{-x}\le x^{-2}$ for $x\ge b$, some $b\ge1$. Since $\int_b^\infty x^{-2}dx$ converges (@thm-p-integrals), so does $\int_b^\infty x^ne^{-x}dx$ by @thm-comparison-integrals. (A limit of $0$ rather than a positive number is enough for convergence, by this direct comparison.)

c) With $u=x^{n+1}$, $v=-e^{-x}$ (@thm-integration-by-parts):
$$\int_0^Nx^{n+1}e^{-x}dx=\Big[-x^{n+1}e^{-x}\Big]_0^N+(n+1)\int_0^Nx^ne^{-x}dx .$$
The boundary term is $-N^{n+1}e^{-N}\to0$ by (a) (and it is $0$ at $x=0$). Letting $N\to\infty$, $A(n+1)=(n+1)A(n)$, so $c_n=n+1$.

d) $A(0)=\int_0^\infty e^{-x}dx=1$. By induction $A(n)=n\,A(n-1)=\dots=n!$.

e) $A(-\tfrac12)=\int_0^\infty x^{-1/2}e^{-x}dx$. On $(0,1]$, $x^{-1/2}e^{-x}\le x^{-1/2}$, whose integral converges ($p=\frac12<1$); on $[1,\infty)$, $x^{-1/2}e^{-x}\le e^{-x}$. So it converges. Substituting $x=u^2$, $dx=2u\,du$:
$$A(-\tfrac12)=\int_0^\infty\frac{e^{-u^2}}{u}\,2u\,du=2\int_0^\infty e^{-u^2}du=\sqrt\pi,$$
using the Gaussian integral (@prp-gaussian-integral).
:::
