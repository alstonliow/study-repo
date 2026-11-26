<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6854ps-6-q1" status="draft"}
1. *Backward analysis.* Condition on the set $Q_i=\{p_1,\dots,p_i\}$; then $P_i=\operatorname{conv}Q_i$ is fixed and $p_i$ is a uniformly random element of $Q_i$. The facets created at step $i$ are exactly the facets of $P_i$ that contain $p_i$ (@prp-hull-update).

2. In general position each facet has exactly $d$ vertices, so it contains $p_i$ with probability $d/i$. Hence $\mathbb E[N_i\mid Q_i]=\frac di\,F(P_i)\le\frac di\,C\,i^{\lfloor d/2\rfloor}$, where $F$ counts facets and $C$ is the constant of the upper bound. The same bound holds unconditionally.

3. With $a=\lfloor d/2\rfloor\ge1$ (for $d\ge2$), $\sum_{i=d+2}^n\frac di\,C\,i^a=Cd\sum_{i\le n}i^{a-1}\le Cd\,n\cdot n^{a-1}=O(n^{\lfloor d/2\rfloor})$ for fixed $d$.
:::
