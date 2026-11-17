<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-4-q6" status="draft"}
1. $\gcd(a,N)=1$, so $p\nmid a$ and $q\nmid a$.

2. By Fermat's little theorem $a^{p-1}\equiv1\pmod p$, so $a^{(p-1)(q-1)+1}=\bigl(a^{p-1}\bigr)^{q-1}a\equiv a\pmod p$.

3. In the same way, $a^{(p-1)(q-1)+1}\equiv a\pmod q$.

4. So $p$ and $q$ both divide $a^{(p-1)(q-1)+1}-a$. They are distinct primes, hence coprime, so $N=pq$ divides it (@prp-coprimedivides).
:::

::: {.solution for="prob-cs70hw-5-q1" status="draft"}
(a) $ed\equiv1\pmod{p-1}$, so $ed=1+k(p-1)$ with $k\ge0$. If $x=0$, then $D(E(x))=0$. Otherwise $p\nmid x$, and by Fermat's little theorem $x^{ed}=x\cdot\bigl(x^{p-1}\bigr)^k\equiv x\pmod p$. Since $0\le x<p$, $D(E(x))=x$.

(b) Yes. $p$ is public, so Eve knows $p-1$ and $e$, and computes $d=e^{-1}\bmod(p-1)$ with the extended Euclidean algorithm (@sec-math-discrete-number-theory-extended-euclidean-algorithm). The numbers at least halve every two steps (@prp-ea-steps), so about $2\cdot1024$ iterations suffice.

(c) She computes $x=y^d\bmod p$ by repeated squaring (@sec-math-discrete-number-theory-modular-exponentiation): about $1024$ squarings and at most as many multiplications, since $d<p$ has at most $1024$ bits.

(d) Yes: a few thousand operations on $1024$-bit numbers take a fraction of a second. The security of RSA rests on keeping $(p-1)(q-1)$ secret, which requires knowing the factorisation of $N$; with $N$ prime there is nothing to factor.
:::

::: {.solution for="prob-cs70hw-5-q2" status="draft"}
(a)

1. Let $U$ be the set of numbers in $\{1,\dots,p^2-1\}$ coprime to $p$. The multiples of $p$ below $p^2$ are $p,2p,\dots,(p-1)p$, so $|U|=p^2-1-(p-1)=p(p-1)$.

2. Since $\gcd(a,p)=1$, multiplication by $a$ modulo $p^2$ maps $U$ to $U$ (a product of numbers coprime to $p$ is coprime to $p$), and it is injective: $au\equiv au'$ implies $u\equiv u'$, as $a$ is invertible modulo $p^2$.

3. So $\{au\bmod p^2:u\in U\}=U$, and multiplying all elements, $a^{p(p-1)}\prod_{u\in U}u\equiv\prod_{u\in U}u\pmod{p^2}$.

4. The product is coprime to $p$, hence invertible modulo $p^2$; cancelling it gives $a^{p(p-1)}\equiv1\pmod{p^2}$.

(b)

1. $ed=1+k\,p(p-1)q(q-1)$ for some $k\ge0$.

2. Modulo $p^2$: $x^{ed}=x\cdot\bigl(x^{p(p-1)}\bigr)^{kq(q-1)}\equiv x$ by (a), since $\gcd(x,p)=1$. In the same way $x^{ed}\equiv x\pmod{q^2}$.

3. $p^2$ and $q^2$ are coprime (for $p\ne q$), so $N=p^2q^2$ divides $x^{ed}-x$ (@prp-coprimedivides).
:::
