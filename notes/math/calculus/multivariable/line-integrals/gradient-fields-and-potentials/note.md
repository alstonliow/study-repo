---
title: "The Criterion for Gradient Fields, Potentials and Curl"
sources: [mit1802-21, mit1802n-V2]
requires: [math/calculus/multivariable/line-integrals/conservative-fields]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 21 and Supplementary Notes V2, in our own wording. Numbers checked in Python (sympy). -->

::: {#thm-gradient-field-criterion .theorem name="Criterion for gradient fields"}

Let $\mathbf{F}=M\,\mathbf{i}+N\,\mathbf{j}$ have continuous partial derivatives.

1. If $\mathbf{F}$ is a gradient field, then $N_x=M_y$.
2. Conversely, if $\mathbf{F}$ is defined and continuously differentiable in the whole plane (or in a simply connected region) and $N_x=M_y$, then $\mathbf{F}$ is a gradient field.

:::

::: {.proof}

1. If $\mathbf{F}=\nabla f$ then $M=f_x$ and $N=f_y$, so $N_x=f_{yx}=f_{xy}=M_y$ by @thm-symmetry-mixed-partials.

2. The converse follows from Green's theorem: see @cor-criterion-from-green; for simply connected regions, @sec-math-calculus-multivariable-line-integrals-simply-connected-regions.

:::

::: {#exm-gradient-criterion .example name="Testing fields"}

- $\mathbf{F}=-y\,\mathbf{i}+x\,\mathbf{j}$: $N_x=1\ne-1=M_y$. Not a gradient field.
- $\mathbf{F}=(4x^2+axy)\,\mathbf{i}+(3y^2+4x^2)\,\mathbf{j}$: $N_x=8x$ and $M_y=ax$, so it is a gradient field exactly when $a=8$.

:::

::: {#prp-finding-potential .proposition name="Two ways to find a potential"}

Let $\mathbf{F}=\langle M,N\rangle$ be a gradient field on the whole plane.

1. **By a line integral.** $f(x_1,y_1)=\int_C\mathbf{F}\cdot d\mathbf{r}+c$ for any curve $C$ from $(0,0)$ to $(x_1,y_1)$; the easiest is usually along the $x$-axis to $(x_1,0)$ and then vertically to $(x_1,y_1)$:
$$f(x_1,y_1)=\int_0^{x_1}M(x,0)\,dx+\int_0^{y_1}N(x_1,y)\,dy+c .$$
2. **By antiderivatives.** Integrate $f_x=M$ with respect to $x$, holding $y$ fixed: $f=\int M\,dx+g(y)$. Differentiate with respect to $y$ and compare with $f_y=N$ to find $g'(y)$, then $g$.

:::

::: {.proof}

1. Method 1 is @thm-ftc-line-integrals read backwards: $f(x_1,y_1)-f(0,0)=\int_C\nabla f\cdot d\mathbf{r}$, and $f(0,0)$ is the arbitrary constant $c$.

2. In method 2, $f_y-\frac{\partial}{\partial y}\int M\,dx$ does not depend on $x$, because its $x$-derivative is $N_x-M_y=0$; so a function $g(y)$ can be found.

:::

::: {#fig-gradient-fields-and-potentials-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.2]
\draw[->] (-0.4,0) -- (3.4,0) node[lab, right] {$x$};
\draw[->] (0,-0.4) -- (0,2.5) node[lab, above] {$y$};
\draw[hl, ->] (0,0) -- (1.4,0);
\draw[hl] (1.3,0) -- (2.6,0);
\draw[hl, ->] (2.6,0) -- (2.6,1.1);
\draw[hl] (2.6,1.0) -- (2.6,1.9);
\fill[ink] (0,0) circle[pt] node[lab, below left] {$(0,0)$};
\fill[ink] (2.6,0) circle[pt] node[lab, below] {$(x_1,0)$};
\fill[ink] (2.6,1.9) circle[pt] node[lab, above right] {$(x_1,y_1)$};
\node[lab] at (1.3,-0.35) {$\int M(x,0)\,dx$};
\node[lab, right] at (2.7,0.95) {$\int N(x_1,y)\,dy$};
\draw[faint, dashed] (0,0) .. controls (0.6,1.6) and (1.6,0.8) .. (2.6,1.9);
\end{tikzpicture}
\end{center}
```

Finding a potential by a line integral (@prp-finding-potential). Any path from the origin gives the same value; the highlighted one, along the $x$-axis and then vertically, splits the integral into two single-variable integrals. The dashed path would give the same answer.

:::

::: {#exm-finding-potential .example name="Both methods on one field"}

$\mathbf{F}=(4x^2+8xy)\,\mathbf{i}+(3y^2+4x^2)\,\mathbf{j}$.

- Method 1: along the $x$-axis $\int_0^{x_1}4x^2\,dx=\frac43x_1^3$; then up, $\int_0^{y_1}(3y^2+4x_1^2)\,dy=y_1^3+4x_1^2y_1$. So $f=\frac43x^3+4x^2y+y^3+c$.
- Method 2: $f=\int(4x^2+8xy)\,dx=\frac43x^3+4x^2y+g(y)$; then $f_y=4x^2+g'(y)=3y^2+4x^2$ gives $g=y^3+c$. Same answer.

:::

::: {#def-curl-plane .definition name="Curl in the plane"}

The **curl** of $\mathbf{F}=M\,\mathbf{i}+N\,\mathbf{j}$ is the function
$$\operatorname{curl}\mathbf{F}=N_x-M_y .$$
So the criterion says: on the whole plane, $\mathbf{F}$ is a gradient field exactly when its curl is $0$.

:::

::: {#rmk-gradient-fields-and-potentials-1 .remark name="What curl measures"}

For a velocity field, the curl is twice the angular velocity of the rotating part of the motion: a uniform translation $\langle a,b\rangle$ and the expansion $\langle x,y\rangle$ have curl $0$, while the rotation $\langle-y,x\rangle$ with angular velocity $1$ has curl $2$. For a force field, the curl measures the torque the field exerts on a small test body, i.e. how much it tends to make it turn.

:::
