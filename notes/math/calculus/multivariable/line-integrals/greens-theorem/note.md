---
title: "Green's Theorem"
sources: [mit1802-22, mit1802n-V4]
requires: [math/calculus/multivariable/line-integrals/gradient-fields-and-potentials, math/calculus/multivariable/multiple-integrals/mass-and-moments]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 22 and Supplementary Notes V4, in our own wording. Numbers checked in Python (sympy). -->

A closed curve $C$ bounding a region $R$ is **positively oriented** when $R$ lies on the left as one travels along $C$ (counterclockwise for the outer boundary).

::: {#thm-greens-theorem .theorem name="Green's theorem"}

Let $C$ be a positively oriented closed curve bounding the region $R$, and let $\mathbf{F}=M\,\mathbf{i}+N\,\mathbf{j}$ have continuous partial derivatives on all of $R$ (including $C$). Then
$$\oint_C\mathbf{F}\cdot d\mathbf{r}=\iint_R\operatorname{curl}\mathbf{F}\,dA,\qquad\text{i.e.}\qquad\oint_CM\,dx+N\,dy=\iint_R(N_x-M_y)\,dA .$$

:::

::: {.proof}

1. The theorem is the sum of two identities, $\oint_CM\,dx=-\iint_RM_y\,dA$ and $\oint_CN\,dy=\iint_RN_x\,dA$. We prove the first; the second is the same with the roles of $x$ and $y$ exchanged.

2. **Additivity.** If $R$ is cut into $R_1$ and $R_2$ with positively oriented boundaries $C_1,C_2$, then $\iint_R=\iint_{R_1}+\iint_{R_2}$, and also $\oint_C=\oint_{C_1}+\oint_{C_2}$, because the cut is traversed once in each direction and those two contributions cancel. So it is enough to prove the identity for pieces.

3. **Vertically simple regions.** Let $R$ be $a\le x\le b$, $f_0(x)\le y\le f_1(x)$. Its boundary consists of the lower curve $y=f_0(x)$ ($x$ from $a$ to $b$), the vertical side $x=b$, the upper curve $y=f_1(x)$ ($x$ from $b$ to $a$) and the vertical side $x=a$. On the vertical sides $dx=0$. So
$$\oint_CM\,dx=\int_a^bM(x,f_0(x))\,dx-\int_a^bM(x,f_1(x))\,dx .$$

4. On the other side,
$$-\iint_RM_y\,dA=-\int_a^b\int_{f_0(x)}^{f_1(x)}M_y\,dy\,dx=-\int_a^b\big[M(x,f_1(x))-M(x,f_0(x))\big]dx,$$
the same.

5. Any reasonable region can be cut into vertically simple pieces, so by step 2 the identity holds for $R$. (For the second identity, cut into horizontally simple pieces.)

:::

::: {#exm-green-disk .example name="A hard line integral made easy"}

$C$ the unit circle about $(2,0)$, counterclockwise. With $M=ye^{-x}$, $N=\frac12x^2-e^{-x}$:
$$\oint_Cye^{-x}\,dx+\big(\tfrac12x^2-e^{-x}\big)dy=\iint_R\big((x+e^{-x})-e^{-x}\big)dA=\iint_Rx\,dA=\bar x\cdot\text{area}=2\pi .$$

:::

::: {#cor-criterion-from-green .corollary name="Proof of the criterion"}

If $\mathbf{F}$ is continuously differentiable in the whole plane and $N_x=M_y$, then $\mathbf{F}$ is conservative, hence a gradient field (@thm-gradient-field-criterion).

:::

::: {.proof}

1. Let $C$ be a closed curve; we may assume it does not cross itself (otherwise split it into loops). It bounds a region $R$ in which $\mathbf{F}$ is defined.

2. By Green's theorem $\oint_C\mathbf{F}\cdot d\mathbf{r}=\pm\iint_R(N_x-M_y)\,dA=0$. So $\mathbf{F}$ is conservative, and by @thm-conservative-equivalences it is a gradient field.

:::

::: {#cor-area-by-line-integral .corollary name="Area as a line integral"}

$$\text{area}(R)=\oint_Cx\,dy=-\oint_Cy\,dx=\frac12\oint_Cx\,dy-y\,dx .$$

:::

::: {.proof}

1. Apply Green's theorem with $(M,N)=(0,x)$, $(-y,0)$ or $(-\frac y2,\frac x2)$; in each case $N_x-M_y=1$.

:::

A **planimeter** is a mechanical device that measures areas this way: tracing the boundary with its arm computes a line integral of this kind.

::: {#rmk-greens-theorem-1 .remark name="The field must be defined inside"}

The hypothesis that $\mathbf{F}$ is defined on all of $R$ matters. The field $\frac{-y\,\mathbf{i}+x\,\mathbf{j}}{x^2+y^2}$ has curl $0$ wherever it is defined, yet its work around the unit circle is $2\pi$: Green's theorem does not apply, because $R$ contains the origin. See @sec-math-calculus-multivariable-line-integrals-simply-connected-regions.

:::
