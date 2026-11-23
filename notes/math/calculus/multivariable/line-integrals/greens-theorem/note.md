---
title: "Green's Theorem"
sources: [mit1802-22, mit1802n-V4]
requires: [math/calculus/multivariable/line-integrals/gradient-fields-and-potentials, math/calculus/multivariable/multiple-integrals/mass-and-moments]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 22 and Supplementary Notes V4, in our own wording. Numbers checked in Python (sympy). -->

A closed curve $C$ bounding a region $R$ is **positively oriented** when $R$ lies on the left as one travels along $C$ (counterclockwise for the outer boundary).

::: {#fig-greens-theorem-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] plot[smooth cycle] coordinates {(0,0) (2,-0.4) (3.4,0.6) (2.8,2) (1,1.8)};
\draw[emph] plot[smooth cycle] coordinates {(0,0) (2,-0.4) (3.4,0.6) (2.8,2) (1,1.8)};
\draw[->, emph] (1.4,-0.3) -- (1.6,-0.36); \draw[->, emph] (2,1.98) -- (1.8,1.96);
\node[lab] at (1.7,0.8) {$R$}; \node[lab] at (3.6,1.6) {$C$};
\end{tikzpicture}
\end{center}
```

Green's theorem: $C$ is the boundary of $R$, traversed counterclockwise, so $R$ is on the left.

:::

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

::: {#fig-greens-theorem-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) -- (1.5,0) -- (1.5,1.5) -- (0,1.5) -- cycle;
\fill[tintC] (1.5,0) -- (3,0) -- (3,1.5) -- (1.5,1.5) -- cycle;
\draw[emph, ->] (0,0) -- (1.4,0);
\draw[emph, ->] (1.4,0.1) -- (1.4,1.4);
\draw[emph, ->] (1.5,1.5) -- (0,1.5);
\draw[emph, ->] (0,1.5) -- (0,0.05);
\draw[emph, ->] (1.6,0) -- (3,0);
\draw[emph, ->] (3,0) -- (3,1.5);
\draw[emph, ->] (3,1.5) -- (1.6,1.5);
\draw[emph, ->] (1.6,1.4) -- (1.6,0.1);
\node[lab] at (0.75,0.75) {$R_1$};
\node[lab] at (2.25,0.75) {$R_2$};
\node[lab, below] at (1.5,-0.35) {cancel};
\end{tikzpicture}
\end{center}
```

Why Green's theorem can be proved piece by piece: cut $R$ into $R_1$ and $R_2$. The shared edge is traversed once upward and once downward, so its line integrals cancel, and the sum of the two boundary integrals is the integral around the outer boundary.

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

::: {#fig-greens-theorem-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-2.3,0) -- (2.5,0) node[lab, right] {$x$};
\draw[->, faint] (0,-1.5) -- (0,1.6) node[lab, above] {$y$};
\fill[tintA] (2,0) -- (1.99,0.1) -- (1.97,0.19) -- (1.93,0.28) -- (1.88,0.38) -- (1.81,0.46) -- (1.73,0.55) -- (1.64,0.63) -- (1.53,0.71) -- (1.41,0.78) -- (1.29,0.84) -- (1.15,0.9) -- (1,0.95) -- (0.85,1) -- (0.68,1.03) -- (0.52,1.06) -- (0.35,1.08) -- (0.17,1.1) -- (0,1.1) -- (-0.17,1.1) -- (-0.35,1.08) -- (-0.52,1.06) -- (-0.68,1.03) -- (-0.85,1) -- (-1,0.95) -- (-1.15,0.9) -- (-1.29,0.84) -- (-1.41,0.78) -- (-1.53,0.71) -- (-1.64,0.63) -- (-1.73,0.55) -- (-1.81,0.46) -- (-1.88,0.38) -- (-1.93,0.28) -- (-1.97,0.19) -- (-1.99,0.1) -- (-2,0) -- (-1.99,-0.1) -- (-1.97,-0.19) -- (-1.93,-0.28) -- (-1.88,-0.38) -- (-1.81,-0.46) -- (-1.73,-0.55) -- (-1.64,-0.63) -- (-1.53,-0.71) -- (-1.41,-0.78) -- (-1.29,-0.84) -- (-1.15,-0.9) -- (-1,-0.95) -- (-0.85,-1) -- (-0.68,-1.03) -- (-0.52,-1.06) -- (-0.35,-1.08) -- (-0.17,-1.1) -- (0,-1.1) -- (0.17,-1.1) -- (0.35,-1.08) -- (0.52,-1.06) -- (0.68,-1.03) -- (0.85,-1) -- (1,-0.95) -- (1.15,-0.9) -- (1.29,-0.84) -- (1.41,-0.78) -- (1.53,-0.71) -- (1.64,-0.63) -- (1.73,-0.55) -- (1.81,-0.46) -- (1.88,-0.38) -- (1.93,-0.28) -- (1.97,-0.19) -- (1.99,-0.1) -- cycle;
\draw[emph, ->] (2,0) arc[start angle=0, end angle=350, x radius=2, y radius=1.1];
\node[lab] at (0,0.25) {$A=\tfrac12\oint_C x\,dy-y\,dx$};
\node[lab, right] at (2,0.9) {$C$};
\end{tikzpicture}
\end{center}
```

The area inside an ellipse by a line integral around its boundary: with $x=a\cos t$, $y=b\sin t$, $\tfrac12\oint x\,dy-y\,dx=\tfrac12\int_0^{2\pi}ab\,dt=\pi ab$.

:::

A **planimeter** is a mechanical device that measures areas this way: tracing the boundary with its arm computes a line integral of this kind.

::: {#rmk-greens-theorem-1 .remark name="The field must be defined inside"}

The hypothesis that $\mathbf{F}$ is defined on all of $R$ matters. The field $\frac{-y\,\mathbf{i}+x\,\mathbf{j}}{x^2+y^2}$ has curl $0$ wherever it is defined, yet its work around the unit circle is $2\pi$: Green's theorem does not apply, because $R$ contains the origin. See @sec-math-calculus-multivariable-line-integrals-simply-connected-regions.

:::
