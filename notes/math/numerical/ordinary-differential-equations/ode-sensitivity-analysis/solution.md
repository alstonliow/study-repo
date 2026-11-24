<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18s096-9-q1" status="draft"}
We use @thm-ode-adjoint-sensitivity: $G=\int_0^Tg\,dt$, $\dot\lambda=-f_u^{\mathsf T}\lambda-g_u^{\mathsf T}$ with $\lambda(T)=0$, and $\nabla G=\int_0^T(g_p^{\mathsf T}+f_p^{\mathsf T}\lambda)\,dt+(\partial u_0/\partial p)^{\mathsf T}\lambda(0)$.

1. Put $g(u,p,t)=\sum_{k=1}^K\delta(t-t_k)\,g_k(p,u)$. Since each $t_k$ lies inside $(0,T)$, $\int_0^Tg(u(p,t),p,t)\,dt=\sum_kg_k\bigl(p,u(p,t_k)\bigr)=G(p)$.

2. Now $g_u^{\mathsf T}=\sum_k\delta(t-t_k)\,(\partial g_k/\partial u)^{\mathsf T}$. Away from the $t_k$ the adjoint solves the homogeneous equation $\dot\lambda=-f_u^{\mathsf T}\lambda$. Integrating the adjoint equation over $(t_k-\varepsilon,t_k+\varepsilon)$ and letting $\varepsilon\to0$, the bounded term $f_u^{\mathsf T}\lambda$ contributes nothing and the delta contributes its weight:

   $$\lambda(t_k^-)=\lambda(t_k^+)+\Bigl(\frac{\partial g_k}{\partial u}\Bigr)^{\mathsf T}\Big|_{u(p,t_k)} .$$

   So, solving backwards from $\lambda(T)=0$, $\lambda$ stays $0$ until the last data time, and at each $t_k$ it jumps by $\partial g_k/\partial u$; in a solver this is a callback that stops at $t_k$ and adds the jump.

3. In $\int_0^Tg_p^{\mathsf T}\,dt$ the delta functions give $\sum_k(\partial g_k/\partial p)^{\mathsf T}$, the derivative of each term through its explicit $p$-dependence. If $g_k$ depends on $p$ only through $u$, then $g_p=0$ and this sum vanishes; the dependence through $u$ is carried entirely by the jumps of $\lambda$ and the term $\int f_p^{\mathsf T}\lambda\,dt$.

*Check.* For $u'=-pu$, $u(0)=1$, $p=1$, $T=2$ and $G=u(0.5)+u(1.5)$: $\lambda$ is $0$ on $(1.5,2)$, $e^{t-1.5}$ on $(0.5,1.5)$ and $e^{t-1.5}+e^{t-0.5}$ on $(0,0.5)$, and $\int_0^2(-u)\lambda\,dt=-0.63796$, equal to $\frac{d}{dp}\bigl(e^{-0.5p}+e^{-1.5p}\bigr)=-0.5e^{-0.5}-1.5e^{-1.5}$ (numerical quadrature in Python).
:::
