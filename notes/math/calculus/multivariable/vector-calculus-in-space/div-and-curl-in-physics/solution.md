<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802n-6h-q1" status="draft"}
@thm-div-curl-zero: $\nabla\cdot\langle R_y-Q_z,P_z-R_x,Q_x-P_y\rangle=R_{yx}-Q_{zx}+P_{zy}-R_{xy}+Q_{xz}-P_{yz}=0$, since the mixed partials are equal. Hypothesis: $P,Q,R$ have continuous second partial derivatives (so that @thm-mixed-partials applies).
:::

::: {.solution for="prob-mit1802n-6h-q2" status="draft"}
a) If $S$ bounds the solid $D$ (and $\mathbf{F}$ has continuous second partials in $D$), the divergence theorem gives $\iiint_D\nabla\cdot(\nabla\times\mathbf{F})\,dV=0$ by 6H-1.

b) Draw a closed curve $C$ on $S$ cutting it into two pieces $S_1,S_2$. With the outward normal, the boundary orientations induced by $S_1$ and $S_2$ on $C$ are opposite. By Stokes, $\iint_{S_1}=\oint_C\mathbf{F}\cdot d\mathbf{r}$ and $\iint_{S_2}=-\oint_C\mathbf{F}\cdot d\mathbf{r}$; the sum is $0$.
:::
