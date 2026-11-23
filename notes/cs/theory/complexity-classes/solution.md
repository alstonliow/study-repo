<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-7-q18" status="draft"}
1. Assume $\mathrm P=\mathrm{NP}$. Let $A\in\mathrm P$ with $A\ne\emptyset$ and $A\ne\Sigma^*$, and fix strings $w_{\text{in}}\in A$ and $w_{\text{out}}\notin A$.

2. *Every NP language reduces to $A$.* Let $B\in\mathrm{NP}=\mathrm P$, decided in polynomial time by $M_B$. Define $f(x)=w_{\text{in}}$ if $M_B$ accepts $x$, and $f(x)=w_{\text{out}}$ otherwise. Then $f$ is computable in polynomial time, and $x\in B$ iff $f(x)\in A$. So $B\le_{\mathrm p}A$.

3. $A\in\mathrm P=\mathrm{NP}$ and every NP language reduces to $A$, so $A$ is NP-complete.

4. The exceptions are needed: no language other than $\emptyset$ reduces to $\emptyset$, and no language other than $\Sigma^*$ reduces to $\Sigma^*$.
:::

::: {.solution for="prob-sipser3e-7-q39" status="draft"}
1. *A decision problem.* Let $F=\{\langle N,k\rangle\mid N \text{ has a divisor } d \text{ with } 1<d\le k\}$, numbers in binary. $F\in\mathrm{NP}$: the certificate is $d$, and division checks it in polynomial time. So if $\mathrm P=\mathrm{NP}$, then $F\in\mathrm P$.

2. *Find the smallest prime factor.* $N>1$ is prime iff $\langle N,N-1\rangle\notin F$. Otherwise, binary search on $k\in[2,N-1]$ for the least $k$ with $\langle N,k\rangle\in F$; that $k$ is the smallest divisor larger than $1$, and it is prime. This takes $O(\log N)$ queries.

3. *Repeat.* Divide $N$ by the factor found and continue. $N$ has at most $\log_2N$ prime factors, counted with multiplicity.

4. In total there are $O(\log^2N)$ calls to the polynomial-time decider for $F$, plus arithmetic on numbers of at most $\log_2N$ bits, so the whole factorization takes polynomial time.
:::
