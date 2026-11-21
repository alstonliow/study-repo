<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camii-pms-2-q1" status="draft"}
1. *Sums and products.* $\{f_1+f_2<a\}=\bigcup_{q\in\mathbb Q}\{f_1<q\}\cap\{f_2<a-q\}$, a countable union of measurable sets (if $f_1(x)+f_2(x)<a$, pick a rational $q$ with $f_1(x)<q<a-f_2(x)$). The sets $\{g<a\}$ generate as well as $\{g\le a\}$, since $\{g\le a\}=\bigcap_n\{g<a+\frac1n\}$. For the product, $f_1f_2=\frac14\big((f_1+f_2)^2-(f_1-f_2)^2\big)$; $-f_2$ is measurable, and $h^2$ is measurable for measurable $h$ because $\{h^2\le a\}=\{-\sqrt a\le h\le\sqrt a\}$ for $a\ge0$ (empty for $a<0$).

2. *Sup and inf.* $\{\sup_nf_n\le a\}=\bigcap_n\{f_n\le a\}$ and $\{\inf_nf_n<a\}=\bigcup_n\{f_n<a\}$.

3. *limsup and liminf.* $\limsup_nf_n=\inf_m\sup_{n\ge m}f_n$ and $\liminf_nf_n=\sup_m\inf_{n\ge m}f_n$; apply step 2 twice.

4. *Convergence set.* $f_n(x)$ converges in $[-\infty,\infty]$ iff $\liminf_nf_n(x)=\limsup_nf_n(x)$. If $\liminf<\limsup$ at $x$, there is a rational $q$ strictly between them. So the complement of the convergence set is $\bigcup_{q\in\mathbb Q}\big(\{\liminf_nf_n<q\}\cap\{\limsup_nf_n>q\}\big)$, which is measurable by step 3.
:::

::: {.solution for="prob-camii-pms-2-q2" status="draft"}
1. $\nu$ is well defined on $\mathcal G$ because $f^{-1}(A)\in\mathcal E$ for $A\in\mathcal G$, and $\nu(A)\in[0,\infty]$.

2. $\nu(\emptyset)=\mu(f^{-1}(\emptyset))=\mu(\emptyset)=0$.

3. If $A_1,A_2,\dots\in\mathcal G$ are disjoint, the preimages $f^{-1}(A_n)$ are disjoint (a point mapped into two of them would have $f(x)$ in both), and $f^{-1}\big(\bigcup_nA_n\big)=\bigcup_nf^{-1}(A_n)$. So $\nu\big(\bigcup A_n\big)=\sum_n\mu(f^{-1}(A_n))=\sum_n\nu(A_n)$.
:::
