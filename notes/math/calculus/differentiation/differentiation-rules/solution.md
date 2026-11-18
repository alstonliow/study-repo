<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit1801f06-1-q7" status="draft"}
a) Apply @thm-derivative-product-rule to $(uv)\cdot w$: $D(uvw)=D(uv)\,w+uv\,Dw=u'vw+uv'w+uvw'$.

b) Claim: $D(u_1\cdots u_n)=\sum_{i=1}^n u_1\cdots u_{i-1}\,u_i'\,u_{i+1}\cdots u_n$ (differentiate one factor at a time and add).

1. Base case $n=1$: $Du_1=u_1'$.

2. Inductive step: assume the formula for $n$ factors and let $P=u_1\cdots u_n$. By the product rule, $D(Pu_{n+1})=P'u_{n+1}+P\,u_{n+1}'$.

3. By the hypothesis, $P'u_{n+1}=\sum_{i=1}^n u_1\cdots u_i'\cdots u_n\,u_{n+1}$, which gives the terms $i=1,\dots,n$ of the formula for $n+1$ factors; $P\,u_{n+1}'$ is the term $i=n+1$.
:::
