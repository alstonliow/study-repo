<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camii-pms-1-q1" status="draft"}
1. $\mathcal E^*=\bigcap_{\mathcal E\in\mathcal S}\mathcal E$. Every $\mathcal E\in\mathcal S$ contains $\emptyset$, so $\emptyset\in\mathcal E^*$ (if $\mathcal S=\emptyset$, $\mathcal E^*$ is the power set, also a σ-algebra).

2. If $A\in\mathcal E^*$, then $A\in\mathcal E$ for every $\mathcal E\in\mathcal S$, so $A^c\in\mathcal E$ for every such $\mathcal E$, i.e. $A^c\in\mathcal E^*$.

3. If $A_1,A_2,\dots\in\mathcal E^*$, then for each $\mathcal E\in\mathcal S$ all $A_n$ lie in $\mathcal E$, hence so does $\bigcup_nA_n$; thus $\bigcup_nA_n\in\mathcal E^*$.

4. Example: $E=\{1,2,3\}$, $\mathcal E_1=\{\emptyset,\{1\},\{2,3\},E\}$, $\mathcal E_2=\{\emptyset,\{2\},\{1,3\},E\}$. Both are σ-algebras. Their union contains $\{1\}$ and $\{2\}$ but not $\{1\}\cup\{2\}=\{1,2\}$, so it is not closed under unions.
:::

::: {.solution for="prob-camii-pms-1-q2" status="draft"}
Write $\sigma_a,\sigma_b,\sigma_c$ for the generated σ-algebras. It is enough to show that each generating set lies in the next σ-algebra, cyclically, since $\mathcal A\subseteq\sigma(\mathcal B)$ implies $\sigma(\mathcal A)\subseteq\sigma(\mathcal B)$.

1. $(a,b)=\bigcup_{n>1/(b-a)}(a,b-\tfrac1n]\in\sigma_b$. So $\sigma_a\subseteq\sigma_b$.

2. $(a,b]=(-\infty,b]\setminus(-\infty,a]\in\sigma_c$. So $\sigma_b\subseteq\sigma_c$.

3. $(-\infty,b]=\bigcap_{n\ge1}(-\infty,b+\tfrac1n)$ and $(-\infty,b+\tfrac1n)=\bigcup_{m\ge1}(-m,b+\tfrac1n)$ (with $-m<b$), so $(-\infty,b]\in\sigma_a$. So $\sigma_c\subseteq\sigma_a$.

Hence $\sigma_a=\sigma_b=\sigma_c$ (all equal to $\mathcal B$, since open sets are countable unions of open intervals).
:::

::: {.solution for="prob-camii-pms-1-q4" status="draft"}
This is @prp-pi-and-d-is-sigma. In brief: let $\mathcal A$ be both.

1. $\emptyset\in\mathcal A$, and for $A\in\mathcal A$, $A^c=E\setminus A\in\mathcal A$ since $A\subseteq E\in\mathcal A$.

2. $A\cup B=(A^c\cap B^c)^c\in\mathcal A$, so $\mathcal A$ is closed under finite unions.

3. For any sequence, $B_n=A_1\cup\dots\cup A_n\in\mathcal A$ increase to $\bigcup_nA_n$, which is therefore in $\mathcal A$.
:::
