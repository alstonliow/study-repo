<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6854ps-4-q2" status="draft"}
Assume every row of $A$ has a positive entry (otherwise the primal is infeasible), and let $\mathrm{OPT}$ be the common optimal value (both programs are feasible, @thm-lp-strong-duality). Write $\sigma=\sum_js_j$, which grows at rate $1$, so $\sigma$ is the elapsed time.

*1.* Once $\alpha>0$: $\sum_ja_{ij}x_j=\sum_ja_{ij}s_j/\alpha\ge1$, so $x\ge0$ is primal feasible. $\sum_ia_{ij}y_i=d_j/D\le1$ and $y\ge0$, so $y$ is dual feasible, of value $\sum_it_i/D$. By weak duality every such value is at most $\mathrm{OPT}$, hence so is $LB$, the largest value seen so far.

*2.* Let $\Phi=\sum_it_i$ and $R=me^{-\sigma/LB}$. At time $0$, $\Phi=m=R$ (with $e^{-0/0}$ read as $1$). While $s_k$ grows at rate $1$, $dt_i/d\sigma=-a_{ik}t_i$, so $d\Phi/d\sigma=-d_k=-D$. Since $LB$ never decreases, $dR/d\sigma\ge-R/LB$. Whenever $\Phi=R$, the definition of $LB$ gives $LB\ge\Phi/D$, i.e. $D\ge\Phi/LB=R/LB$, so
$$\frac{d\Phi}{d\sigma}=-D\le-\frac R{LB}\le\frac{dR}{d\sigma}.$$
So $\Phi-R$, which starts at $0$, can never become positive: $\Phi\le R$ throughout.

*3.* $LB\le\mathrm{OPT}$, so $\Phi\le me^{-\sigma/\mathrm{OPT}}\to0$ as $\sigma\to\infty$.

*4.* $\max_it_i=e^{-\alpha}\le\Phi\le me^{-\sigma/LB}$, so $\alpha\ge\sigma/LB-\ln m$ and
$$\sum_jx_j=\frac\sigma\alpha\le\frac{\sigma}{\sigma/LB-\ln m}=\frac{LB}{1-LB\ln m/\sigma}\le\frac{LB}{1-\mathrm{OPT}\ln m/\sigma}$$
(for $\sigma>\mathrm{OPT}\ln m$). Since $LB\le\mathrm{OPT}\le\sum_jx_j$, letting $\sigma\to\infty$ squeezes both: $\sum_jx_j\to\mathrm{OPT}$ and $LB\to\mathrm{OPT}$. So $x$ tends to optimality, and so does the best dual solution $y$ found so far (whose value is $LB$).
:::

::: {.solution for="prob-mit6854ps-4-q3" status="draft"}
*1.* Fix the signs $\sigma_i=\operatorname{sign}(c_i)$ and $\varepsilon_k=\operatorname{sign}(y_k^Tc)$ ($\varepsilon_q=1$), and write $L_k(x)=\varepsilon_k\sum_iy_{ki}\sigma_ix_i$, so that $L_k(|c|)=|y_k^Tc|$. The system is
$$L_k(x)\ge0\ (k\le q),\qquad2L_{k+1}(x)\le L_k(x)\ (k<q),\qquad\sum_iy_{qi}\sigma_ix_i=1,\qquad x\ge0.$$
$x=|c|$ satisfies it. For a feasible $x'$ put $c'_i=\sigma_ix'_i$; then $y_k^Tc'=\varepsilon_kL_k(x')$, so $|y_k^Tc'|=L_k(x')$ and the hypotheses of the Lemma hold for $c'$.

*2.* The feasible set is a non-empty polyhedron inside $x\ge0$, so it has a vertex $x'$ (it contains no line). A vertex is the unique solution of $n$ linearly independent tight constraints (@thm-vertex-unique-solution). Their coefficients are integers of absolute value at most $3$ (entries of $L_k$ are $0,\pm1$, of $2L_{k+1}-L_k$ at most $3$), and the right sides are $0$ or $1$. By Cramer's rule $x'_i=d_i/d$ with $d$ and $d_i$ determinants of $n\times n$ integer matrices with entries at most $3$, hence at most $n!\,3^n=2^{O(n\log n)}$ in absolute value, and $d\ne0$. Then $c'=(\sigma_id_i/d)$ has the required form.

*3.* For $c'$ from 2: $|y_1^Tc'|\ge2^{q-1}|y_q^Tc'|=2^{q-1}$. On the other hand $|y_1^Tc'|\le\sum_i|c'_i|\le n\max_i|d_i|$ since $|d|\ge1$. So $2^{q-1}\le n\,2^{O(n\log n)}$ and $q=O(n\log n)$.

*4.* (Optional, not solved here.)
:::
