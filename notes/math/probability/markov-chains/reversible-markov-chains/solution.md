<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-4-q2" status="draft"}
The chain on $\{0,\dots,k-1\}$ is a birth–death chain, so it is reversible (its transition graph is a path, so @thm-kolmogorov-criterion holds trivially) and detailed balance $\pi(i)p=\pi(i+1)q$ gives $\pi(i)=\rho^i\pi(0)$. Normalising:
$$\pi(i)=\frac{1-\rho}{1-\rho^k}\,\rho^i\quad(\rho\ne1),\qquad\pi(i)=\frac1k\quad(\rho=1),\qquad i=0,\dots,k-1.$$
It is unique because the chain is irreducible.
:::
