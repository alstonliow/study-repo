<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camii-pms-1-q8" status="draft"}
We prove the second statement, which contains the first.

1. Lebesgue measure was built by Carathéodory's theorem (@thm-lebesgue-measure) from the ring $\mathcal A$ of finite disjoint unions of intervals $(a,b]$, and on Borel sets it equals the outer measure: $\lambda(B)=\lambda^*(B)=\inf\{\sum_k\lambda(I_k):\ I_k\in\mathcal A,\ B\subseteq\bigcup_kI_k\}$ (@thm-caratheodory-extension).

2. Let $\lambda(B)<\infty$ and $\varepsilon>0$. Choose $I_k\in\mathcal A$ covering $B$ with $\sum_k\lambda(I_k)\le\lambda(B)+\varepsilon/3$. The series converges, so pick $N$ with $\sum_{k>N}\lambda(I_k)\le\varepsilon/3$, and let $A=I_1\cup\dots\cup I_N\in\mathcal A$; it is a finite disjoint union of intervals $(a_i,b_i]$.

3. $B\setminus A\subseteq\bigcup_{k>N}I_k$, so $\lambda(B\setminus A)\le\varepsilon/3$.

4. $A\setminus B\subseteq\bigcup_kI_k\setminus B$, so $\lambda(A\setminus B)\le\sum_k\lambda(I_k)-\lambda(B)\le\varepsilon/3$.

5. Hence $\lambda(A\triangle B)\le2\varepsilon/3<\varepsilon$.
:::
