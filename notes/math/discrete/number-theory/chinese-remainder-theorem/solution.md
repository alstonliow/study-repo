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
