<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-5-q5" status="draft"}
Work in $\mathrm{GF}(r)$ for a prime $r$ larger than $s$ and than the number of points handed out.

(a) Choose a random polynomial $P$ of degree $192$ with $P(0)=s$; any $193$ points determine it, and $192$ points reveal nothing about $s$ (@thm-secret-sharing). Give each country one point $P(i)$, $i=1,\dots,193$, and give the Secretary-General $138$ further points $P(194),\dots,P(331)$.

- All $193$ countries hold $193$ points: they recover $P$ and $s=P(0)$.
- The Secretary-General with $55$ countries holds $138+55=193$ points: they recover $s$.
- Any other group has at most $192$ points: $192$ countries alone, or the Secretary-General with at most $54$ countries ($138+54=192$). They learn nothing.

(b) Replace each country's point by a shared secret. If country $i$ received $t_i=P(i)$ in (a), choose a random polynomial $Q_i$ of degree $11$ with $Q_i(0)=t_i$ and give its $12$ representatives the points $Q_i(1),\dots,Q_i(12)$. All $12$ representatives together recover $t_i$; any $11$ learn nothing about it. The Secretary-General keeps the $138$ points of (a).
:::

::: {.solution for="prob-cs70hw-5-q6" status="draft"}
**Scheme.** Choose a random polynomial $P$ of degree $3$ over a large field $\mathrm{GF}(r)$ with $P(0)$ equal to the password, and give soldier $i$ the share $(i,P(i))$. Then $M=10$.

1. *The spies cannot open the safe.* Three points leave $P(0)$ undetermined: for every value of $P(0)$ there is a polynomial of degree $3$ through the three points and $(0,P(0))$ (@thm-secret-sharing).

2. *Any $10$ soldiers can open it.* Their shares are $10$ values of $P$, of which at most $3$ (the spies') are wrong. A polynomial of degree $3$ is a message of $n=4$ values, and $n+2k=4+2\cdot3=10$ values allow correcting $k=3$ errors with the Berlekamp–Welch algorithm (@thm-berlekamp-welch). So they recover $P$ and $P(0)$.

3. *Fewer than $10$ do not suffice for this kind of scheme.* The degree must be at least $3$, by step 1. Suppose $9$ soldiers meet: $3$ spies and $6$ honest soldiers, split into groups $H_1$ and $H_2$ of $3$. The spies take $P'=P+c\prod_{h\in H_1}(x-h)$ with $c\ne0$, a different polynomial of degree $3$ that agrees with $P$ on $H_1$, and report values of $P'$. Now the $9$ values fit $P$ except at the spies, and fit $P'$ except at $H_2$: both explanations have exactly $3$ liars. The group cannot tell them apart, and $P(0)\ne P'(0)$ because $c\prod_{h\in H_1}(0-h)\ne0$; with one try they may fail. With fewer than $9$ soldiers the same attack works with even smaller groups.

:::
