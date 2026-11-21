<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camii-pms-1-q9" status="draft"}
1. *σ-algebra.* $\emptyset=\emptyset\cup\emptyset$. If $N\subseteq B$ with $\mu(B)=0$, then $(A\cup N)^c=(A^c\cap B^c)\cup(A^c\cap B\cap N^c)$: the first set is in $\mathcal E$ and the second is contained in $B$. For countable unions, $\bigcup_n(A_n\cup N_n)=\bigcup_nA_n\cup\bigcup_nN_n$, and $\bigcup_nN_n\subseteq\bigcup_nB_n$, a null set.

2. *Well defined.* If $A\cup N=A'\cup N'$ with $N'\subseteq B'$ null, then $A\subseteq A'\cup B'$, so $\mu(A)\le\mu(A')$; by symmetry $\mu(A)=\mu(A')$.

3. *Countably additive.* If the sets $A_n\cup N_n$ are disjoint, so are the $A_n$, and $\mu\big(\bigcup(A_n\cup N_n)\big)=\mu\big(\bigcup A_n\big)=\sum\mu(A_n)$.

4. *The outer measure.* Here $\mu^*(C)=\inf\{\sum_n\mu(A_n):\ A_n\in\mathcal E,\ C\subseteq\bigcup A_n\}=\inf\{\mu(A):\ A\in\mathcal E,\ A\supseteq C\}$, since a countable cover can be replaced by its union. The infimum is attained: if $A^{(j)}\supseteq C$ with $\mu(A^{(j)})\le\mu^*(C)+\frac1j$, then $\bigcap_jA^{(j)}$ works. Let $\mathcal M$ be the $\mu^*$-measurable sets.

5. *$\mathcal E^\mu\subseteq\mathcal M$.* $\mathcal E\subseteq\mathcal M$ (step 3 of the proof of @thm-caratheodory-extension, $\mathcal E$ being a ring with countably additive $\mu$), every $N\in\mathcal N$ has $\mu^*(N)=0$ and so lies in $\mathcal M$ (since $\mu^*(B\cap N)+\mu^*(B\cap N^c)\le0+\mu^*(B)$), and $\mathcal M$ is a σ-algebra.

6. *$\mathcal M\subseteq\mathcal E^\mu$.* Write $E=\bigcup_kE_k$ with $E_k\in\mathcal E$, $\mu(E_k)<\infty$. Let $C\in\mathcal M$. By step 4 pick $A_k,D_k\in\mathcal E$ with $A_k\supseteq C\cap E_k$, $D_k\supseteq E_k\setminus C$ and $\mu(A_k)=\mu^*(C\cap E_k)$, $\mu(D_k)=\mu^*(E_k\setminus C)$; replacing them by $A_k\cap E_k$, $D_k\cap E_k$ keeps these properties.

7. Since $C$ is $\mu^*$-measurable and $\mu^*=\mu$ on $\mathcal E$: $\mu(E_k)=\mu^*(E_k\cap C)+\mu^*(E_k\setminus C)=\mu(A_k)+\mu(D_k)$.

8. $G_k=E_k\setminus D_k\in\mathcal E$ satisfies $G_k\subseteq C\cap E_k\subseteq A_k$ and $\mu(A_k\setminus G_k)=\mu(A_k)-\mu(E_k)+\mu(D_k)=0$. So $C\cap E_k=G_k\cup(C\cap E_k\setminus G_k)$ with the second set inside the null set $A_k\setminus G_k$: $C\cap E_k\in\mathcal E^\mu$.

9. $C=\bigcup_k(C\cap E_k)\in\mathcal E^\mu$ by step 1.
:::
