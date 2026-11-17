<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-4-q6" status="draft"}
1. $\gcd(a,N)=1$, so $p\nmid a$ and $q\nmid a$.

2. By Fermat's little theorem $a^{p-1}\equiv1\pmod p$, so $a^{(p-1)(q-1)+1}=\bigl(a^{p-1}\bigr)^{q-1}a\equiv a\pmod p$.

3. In the same way, $a^{(p-1)(q-1)+1}\equiv a\pmod q$.

4. So $p$ and $q$ both divide $a^{(p-1)(q-1)+1}-a$. They are distinct primes, hence coprime, so $N=pq$ divides it (@prp-coprimedivides).
:::
