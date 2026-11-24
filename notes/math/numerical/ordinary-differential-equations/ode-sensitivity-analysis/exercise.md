::: {.problem #prob-mit18s096-9-q1 origin="external" source="mit18s096-9-q1"}
Suppose that $G(p)$ takes the form of a sum of $K$ terms:
$$
G(p)=\sum_{k=1}^K g_k(p,u(p,t_k))
$$
for times $t_k\in(0,T)$ and functions $g_k(p,u)$. For example, this could arise in least-square fitting of experimental data $u^*(t_k)$ at $K$ discrete times, with $g_k(u(p,t_k))=\|u^*(t_k)-u(p,t_k)\|^2$ measuring the squared difference between $u(p,t_k)$ and the measured data at time $t_k$.

1. Show that such a $G(p)$ can be expressed as a special case of our formulation in this chapter, by defining our function $g(u,t)$ using a sum of Dirac delta functions $\delta(t-t_k)$.
2. Explain how this affects the adjoint solution $v(t)$: in particular, how the introduction of delta-function terms on the right-hand side of $dv/dt$ causes $v(t)$ to have a sequence of discontinuous jumps. (In several popular numerical ODE solvers, such discontinuities can be incorporated via discrete-time "callbacks".)
3. Explain how these delta functions may also introduce a summation into the computation of $\nabla_p G$, but only if $g_k$ depends explicitly on $p$ (not just via $u$).

*Note (these notes):* The adjoint solution $v(t)$ of the course notes is $\lambda(t)$ in @thm-ode-adjoint-sensitivity, with the same sign convention.
:::
