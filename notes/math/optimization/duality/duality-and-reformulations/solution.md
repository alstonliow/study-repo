<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-ee364ahw-4-q3" status="draft"}
Write $a_i$ for the $i$th column of $A$.

(a) With multipliers $\mu\succeq0$ for $Ax\preceq b$ and $\nu$ for the equalities, written as $x_i^2-x_i=0$,
$$L(x,\mu,\nu)=c^Tx+\mu^T(Ax-b)+\sum_i\nu_i(x_i^2-x_i)=\sum_i\big(\nu_ix_i^2+(c_i+a_i^T\mu-\nu_i)x_i\big)-b^T\mu.$$
It separates over $i$. The term in $x_i$ is bounded below iff $\nu_i>0$, or $\nu_i=0$ and $c_i+a_i^T\mu=0$; for $\nu_i>0$ its minimum is $-\frac{(c_i+a_i^T\mu-\nu_i)^2}{4\nu_i}$. So the dual problem is
$$\text{maximize }-b^T\mu-\frac14\sum_i\frac{(c_i+a_i^T\mu-\nu_i)^2}{\nu_i}\quad\text{s.t. }\mu\succeq0,\ \nu\succeq0,$$
reading $s^2/0$ as $0$ if $s=0$ and $\infty$ otherwise. Maximize over each $\nu_i\ge0$ by hand: with $s=c_i+a_i^T\mu$, the function $-\frac{(s-\nu)^2}{4\nu}=-\frac{s^2}{4\nu}+\frac s2-\frac\nu4$ has supremum $\frac s2-\frac{\lvert s\rvert}{2}=\min\{0,s\}$ (at $\nu=\lvert s\rvert$, or as $\nu\to0$ when $s=0$). The dual simplifies to
$$\text{maximize }-b^T\mu+\sum_{i=1}^n\min\{0,\ c_i+a_i^T\mu\}\quad\text{s.t. }\mu\succeq0.$$

(b) For (1), use $u\succeq0$ for $Ax\preceq b$, $v\succeq0$ for $-x\preceq0$ and $w\succeq0$ for $x\preceq\mathbf 1$. The Lagrangian $(c+A^Tu-v+w)^Tx-b^Tu-\mathbf 1^Tw$ is affine in $x$, so the dual is
$$\text{maximize }-b^Tu-\mathbf 1^Tw\quad\text{s.t. }c+A^Tu-v+w=0,\ u,v,w\succeq0.$$
For fixed $u$, the constraint asks $w_i-v_i=-(c_i+a_i^Tu)$ with $v_i,w_i\ge0$; the smallest $w_i$ is $\max\{0,-(c_i+a_i^Tu)\}$, so $-\mathbf 1^Tw$ is at most $\sum_i\min\{0,c_i+a_i^Tu\}$, with equality for that choice. Hence the LP dual is exactly the dual found in (a), with $u=\mu$. The LP relaxation is feasible-or-not with strong duality (an LP), so both lower bounds equal the optimal value of this common dual problem (when the LP relaxation is feasible; if it is infeasible, both bounds are $+\infty$ or the dual is unbounded).
:::
