<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camii-pms-1-q3" status="draft"}
Let $\mu$ be countably additive on the ring $\mathcal A$ (so $\mu(\emptyset)=0$).

1. *Additive.* For disjoint $A,B\in\mathcal A$, apply countable additivity to $A,B,\emptyset,\emptyset,\dots$, whose union $A\cup B$ is in $\mathcal A$.

2. *Increasing.* If $A\subseteq B$ in $\mathcal A$, then $B\setminus A\in\mathcal A$ and $\mu(B)=\mu(A)+\mu(B\setminus A)\ge\mu(A)$.

3. *Countably subadditive.* Let $A_n\in\mathcal A$ with $A=\bigcup_nA_n\in\mathcal A$. Put $B_n=A\cap A_n\setminus(A_1\cup\dots\cup A_{n-1})$; rings are closed under finite unions, differences and intersections, so $B_n\in\mathcal A$. The $B_n$ are disjoint with union $A$, so $\mu(A)=\sum_n\mu(B_n)\le\sum_n\mu(A_n)$ by step 2, as $B_n\subseteq A_n$.
:::

::: {.solution for="prob-camii-pms-1-q5" status="draft"}
1. *(⇒)* Let $A_n\downarrow\emptyset$ in $\mathcal A$. The sets $A_k\setminus A_{k+1}$ ($k\ge n$) lie in $\mathcal A$, are disjoint and have union $A_n$ (a point of $A_n$ leaves the sequence at some last index, since $\bigcap A_k=\emptyset$). By countable additivity $\mu(A_n)=\sum_{k\ge n}\mu(A_k\setminus A_{k+1})$.

2. Taking $n=1$ shows the series $\sum_k\mu(A_k\setminus A_{k+1})$ converges (to the finite $\mu(A_1)$). So its tails $\mu(A_n)$ tend to $0$.

3. *(⇐)* Let $B_1,B_2,\dots\in\mathcal A$ be disjoint with $B=\bigcup_kB_k\in\mathcal A$. Then $C_n=B\setminus(B_1\cup\dots\cup B_n)\in\mathcal A$ decreases to $\emptyset$.

4. By additivity $\mu(B)=\sum_{k\le n}\mu(B_k)+\mu(C_n)$, and $\mu(C_n)\to0$ by hypothesis. So $\mu(B)=\sum_k\mu(B_k)$.
:::

::: {.solution for="prob-camii-pms-1-q6" status="draft"}
1. Let $B_m=\bigcap_{n\ge m}A_n$. Then $B_m\uparrow\liminf_nA_n$ and $\mu(B_m)\le\mu(A_n)$ for all $n\ge m$, i.e. $\mu(B_m)\le\inf_{n\ge m}\mu(A_n)$. By continuity from below (no finiteness needed, @prp-measure-continuity), $\mu(\liminf A_n)=\lim_m\mu(B_m)\le\lim_m\inf_{n\ge m}\mu(A_n)=\liminf_n\mu(A_n)$.

2. The middle inequality is trivial.

3. Let $C_m=\bigcup_{n\ge m}A_n\downarrow\limsup_nA_n$, with $\mu(C_m)\ge\sup_{n\ge m}\mu(A_n)$. Since $\mu(C_1)\le\mu(E)<\infty$, continuity from above gives $\mu(\limsup A_n)=\lim_m\mu(C_m)\ge\limsup_n\mu(A_n)$.

4. Without finiteness: Lebesgue measure on $\mathbb R$ and $A_n=[n,n+1]$. Each point lies in at most two $A_n$, so $\limsup A_n=\emptyset$, while $\limsup\mu(A_n)=1>0$.
:::
