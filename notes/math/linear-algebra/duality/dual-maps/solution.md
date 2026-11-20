<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-las-2-q11" status="draft"}
The map $\Psi:\xi\mapsto(\xi(t^k))_{k\ge0}$ is linear. It is bijective: a linear form is determined by its values on the basis $1,t,t^2,\dots$, and any sequence $(a_k)$ arises, from $\xi\big(\sum_kc_kt^k\big)=\sum_kc_ka_k$ (a finite sum, so well defined and linear). Write $\xi\leftrightarrow(a_k)$ and $D^*\xi=\xi\circ D$ (the dual map, @def-dual-map).

(a) $(D^*\xi)(t^k)=\xi(kt^{k-1})=ka_{k-1}$: $(a_0,a_1,a_2,\dots)\mapsto(0,a_0,2a_1,3a_2,\dots)$.

(b) $(S^*\xi)(t^k)=\xi(t^{2k})=a_{2k}$: $(a_0,a_1,a_2,\dots)\mapsto(a_0,a_2,a_4,\dots)$.

(c) $DS(t^k)=2kt^{2k-1}$, so $((DS)^*\xi)(t^k)=2ka_{2k-1}$: $\mapsto(0,2a_1,4a_3,6a_5,\dots)$.

(d) $SD(t^k)=kt^{2k-2}$, so $((SD)^*\xi)(t^k)=ka_{2k-2}$: $\mapsto(0,a_0,2a_2,3a_4,\dots)$.

Check: $S^*D^*$ first gives $b_k=ka_{k-1}$, then $b_{2k}=2ka_{2k-1}$, which is (c). $D^*S^*$ first gives $c_k=a_{2k}$, then $kc_{k-1}=ka_{2k-2}$, which is (d).
:::

::: {.solution for="prob-camib-las-2-q12" status="draft"}
1. If $g=\sum\lambda_if_i$ and $f_i(v)=0$ for all $i$, then $g(v)=0$.

2. Conversely, let $F:V\to\mathbb F^n$, $F(v)=(f_1(v),\dots,f_n(v))$, so $\ker F=\bigcap_i\ker f_i\subseteq\ker g$.

3. Define $h$ on $\operatorname{im}F$ by $h(F(v))=g(v)$. It is well defined: if $F(v)=F(v')$ then $v-v'\in\ker F\subseteq\ker g$. It is linear because $F$ and $g$ are.

4. Extend $h$ to a linear functional on $\mathbb F^n$ (choose a complement of $\operatorname{im}F$, @prp-complements-exist, and set $h=0$ there). Every functional on $\mathbb F^n$ is $h(y)=\sum_i\lambda_iy_i$. Then $g(v)=h(F(v))=\sum_i\lambda_if_i(v)$, so $g=\sum\lambda_if_i$.

The proof never used $\dim V<\infty$ (only that there are finitely many $f_i$), so the statement holds for infinite-dimensional $V$ too. For infinitely many functionals it can fail: on the polynomials, the coefficient functionals $f_k(\sum c_jt^j)=c_k$ have $\bigcap_k\ker f_k=\{0\}$, yet $g(p)=p(1)=\sum_jc_j$ is not a finite combination of them.
:::
