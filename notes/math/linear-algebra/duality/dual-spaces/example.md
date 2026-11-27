<!-- Added 2026-11-27: the examples of Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 3.1, restated in our own words with our own checks. -->

::: {#exm-linear-functionals .example name="Linear functionals"}

1. On $\mathbb R^3$, $x\mapsto x_1-x_3$.
2. On $F^X$, evaluation at a fixed point, $f\mapsto f(x)$.
3. On $C([0,1],\mathbb R)$, $f\mapsto\int_0^1f(t)\,dt$.
4. On $\operatorname{Mat}_n(F)$, the trace $A\mapsto\sum_iA_{ii}$.

Each is linear with values in the field, so each lies in the dual space.

:::

::: {#exm-annihilator-dual-basis .example name="An annihilator in the dual basis"}

In $\mathbb R^3$ with dual basis $\varepsilon_1,\varepsilon_2,\varepsilon_3$, let $U=\langle e_1+2e_2+e_3\rangle$ and $W=\langle\varepsilon_1-\varepsilon_3,\ 2\varepsilon_1-\varepsilon_2\rangle$.

1. $(\varepsilon_1-\varepsilon_3)(e_1+2e_2+e_3)=1-1=0$ and $(2\varepsilon_1-\varepsilon_2)(e_1+2e_2+e_3)=2-2=0$, so $W\subseteq U^0$.

2. $\dim U^0=3-1=2=\dim W$, the two spanning functionals being independent; so $U^0=W$.

3. Likewise $U\subseteq W^0$ and $\dim W^0=3-2=1$, so $W^0=U$ (identifying $V$ with $V^{**}$).

:::
