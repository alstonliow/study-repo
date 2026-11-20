<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-las-1-q4" status="draft"}
(i) $(\alpha+\beta)(\lambda u+\mu u')=\lambda\alpha u+\mu\alpha u'+\lambda\beta u+\mu\beta u'=\lambda(\alpha+\beta)u+\mu(\alpha+\beta)u'$.

Counter-examples: take $U=V=\mathbb R$, $\alpha=\iota$, $\beta=-\iota$, so $\alpha+\beta=0$.

(a) $\operatorname{im}(\alpha+\beta)=\{0\}$ but $\operatorname{im}\alpha+\operatorname{im}\beta=\mathbb R$.

(b) $\ker(\alpha+\beta)=\mathbb R$ but $\ker\alpha\cap\ker\beta=\{0\}$.

Valid inclusions: $\operatorname{im}(\alpha+\beta)\subseteq\operatorname{im}\alpha+\operatorname{im}\beta$, since $(\alpha+\beta)u=\alpha u+\beta u$; and $\ker\alpha\cap\ker\beta\subseteq\ker(\alpha+\beta)$, since $\alpha u=\beta u=0$ gives $(\alpha+\beta)u=0$.

(ii)

1. Every $v$ is $\alpha v+(v-\alpha v)$, with $\alpha v\in\operatorname{im}\alpha$ and $\alpha(v-\alpha v)=\alpha v-\alpha^2v=0$. So $V=\operatorname{im}\alpha+\ker\alpha$.

2. If $v\in\operatorname{im}\alpha\cap\ker\alpha$, write $v=\alpha w$; then $v=\alpha w=\alpha^2w=\alpha v=0$.

3. By @prp-direct-sum-criteria (the two-subspace case, whose proof does not use dimension), $V=\ker\alpha\oplus\operatorname{im}\alpha$.

The proof never used $\dim V<\infty$, so it works, and the result holds, for infinite-dimensional $V$ too.
:::

::: {.solution for="prob-camib-las-1-q6" status="draft"}
(i)

1. $\operatorname{im}\alpha^{k+1}=\alpha^k(\alpha V)\subseteq\alpha^k(V)=\operatorname{im}\alpha^k$, and if $\alpha^kv=0$ then $\alpha^{k+1}v=0$. So the images decrease and the kernels increase; in particular $r_k\ge r_{k+1}$.

2. Let $I_k=\operatorname{im}\alpha^k$. Then $\alpha$ maps $I_k$ onto $I_{k+1}$, and its kernel there is $\ker\alpha\cap I_k$. By @thm-rank-nullity for $\alpha|_{I_k}$,
$$r_k-r_{k+1}=\dim(\ker\alpha\cap I_k).$$

3. Since $I_{k+1}\subseteq I_k$, $\ker\alpha\cap I_{k+1}\subseteq\ker\alpha\cap I_k$, so $r_{k+1}-r_{k+2}\le r_k-r_{k+1}$.

4. If $r_k=r_{k+1}$, then by step 3 the later differences are $\le0$, and by step 1 they are $\ge0$; so all are $0$ and $r_{k+\ell}=r_k$.

(ii) Let $d_k=r_k-r_{k+1}$. Then $r_0=5$, $r_3=0$, so $d_0+d_1+d_2=5$; $d_0\ge d_1\ge d_2\ge0$ by (i); and $d_2=r_2\ge1$ since $\alpha^2\ne0$.

1. The non-increasing triples with sum $5$ and last entry $\ge1$ are $(3,1,1)$ and $(2,2,1)$.

2. They give $(r_1,r_2)=(2,1)$ and $(3,1)$.

3. Both occur. On a basis $e_1,\dots,e_5$: $\alpha:e_3\mapsto e_2\mapsto e_1\mapsto0$, $e_4,e_5\mapsto0$ has rank $2$ and $\alpha^2$ rank $1$; $\alpha:e_3\mapsto e_2\mapsto e_1\mapsto0$, $e_5\mapsto e_4\mapsto0$ has rank $3$ and $\alpha^2$ rank $1$. In both, $\alpha^3=0\ne\alpha^2$.

So $\operatorname{rk}(\alpha^2)=1$ and $\operatorname{rk}(\alpha)\in\{2,3\}$.
:::
