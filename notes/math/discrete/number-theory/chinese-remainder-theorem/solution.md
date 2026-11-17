<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-4-q3" status="draft"}
We need $x\equiv4\pmod7$, $x\equiv2\pmod4$, $x\equiv2\pmod5$. The moduli are pairwise coprime, so by @thm-crt there is exactly one solution modulo $140$.

1. The last two conditions say $4\mid x-2$ and $5\mid x-2$, i.e. $x\equiv2\pmod{20}$ (@prp-coprimedivides).

2. Try $x=2,22,42,62,82,102$: their remainders modulo $7$ are $2,1,0,6,5,4$. So $x\equiv102\pmod{140}$.

The smallest number of stitches is $102$ ($=7\cdot14+4=4\cdot25+2=5\cdot20+2$).
:::

::: {.solution for="prob-cs70hw-4-q4" status="draft"}
1. Take $2k$ distinct primes $p_1,q_1,\dots,p_k,q_k$, and let $m_i=p_iq_i$. The $m_i$ are pairwise coprime.

2. By @thm-crt there is a positive integer $x$ with $x\equiv-i\pmod{m_i}$ for $i=1,\dots,k$.

3. Then $x+i$ is divisible by the two distinct primes $p_i$ and $q_i$ for each $i$. A prime power $p^j$ has only one prime divisor, so none of $x+1,\dots,x+k$ is a prime power.
:::

::: {.solution for="prob-cs70hw-5-q3" status="draft"}
(a) $\gcd(n_1,n_2)=1$, so $n_2$ has an inverse $m$ modulo $n_1$ (@thm-inverse). Then $x_1=n_2m$ satisfies $x_1\equiv1\pmod{n_1}$ and $x_1\equiv0\pmod{n_2}$. Symmetrically, $x_2=n_1m'$ with $m'=n_1^{-1}\bmod n_2$.

(b) $x=a_1x_1+a_2x_2$ satisfies $x\equiv a_1\cdot1+a_2\cdot0=a_1\pmod{n_1}$ and $x\equiv a_2\pmod{n_2}$. If $x,x'$ are two solutions, then $n_1\mid x-x'$ and $n_2\mid x-x'$, so $n_1n_2\mid x-x'$ because $\gcd(n_1,n_2)=1$ (@prp-coprimedivides).

(c) Induction on $k$; $k=1$ is trivial and $k=2$ is (b). Suppose the claim holds for $k-1$ moduli. Equations (1)–$(k-1)$ are equivalent to a single congruence $x\equiv b\pmod{M}$ with $M=n_1\cdots n_{k-1}$. $M$ is coprime to $n_k$ (a prime dividing both would divide some $n_i$ and $n_k$). By (b), the system $x\equiv b\pmod M$, $x\equiv a_k\pmod{n_k}$ has a solution, unique modulo $Mn_k=n_1\cdots n_k$.

(d) By the division of polynomials (@thm-polynomial-division), $p(x)\equiv y_i\pmod{x-x_i}$ means that $p(x)-y_i$ has the root $x_i$, i.e. $p(x_i)=y_i$ (@thm-factor-theorem). For $x_i\ne x_j$ the polynomials $x-x_i$ and $x-x_j$ have no common factor of degree $1$, so they are co-prime and the polynomial CRT gives a solution, unique modulo $\prod_i(x-x_i)$. Taking the remainder modulo this product, there is exactly one solution of degree at most $k-1$: the polynomial through the points $(x_i,y_i)$. This is the interpolation theorem (@thm-interpolation), and the CRT construction is Lagrange's: the polynomial $\Delta_i$, which is $\equiv1\pmod{x-x_i}$ and $\equiv0\pmod{x-x_j}$ for $j\ne i$, plays the role of $x_1,x_2$ in (a), and $p=\sum_iy_i\Delta_i$ as in (b).
:::
