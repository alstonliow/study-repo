---
title: "Fundamental Matrices and Variation of Parameters"
sources: [mit1803-35]
requires: [math/differential-equations/linear-systems/eigenvalue-method]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.03SC Differential Equations (Fall 2011), Session 35 (general linear systems, existence and uniqueness, the Wronskian, fundamental and normalized fundamental matrices, the exponential matrix, variation of parameters), in our own wording; examples are ours, checked in Python; proofs written out in steps. The existence and uniqueness theorem is stated without proof, as in the course; the matrix exponential is @def-matrix-exponential. -->

A system of $n$ equations has $n$ independent solutions. Putting them side by side as columns gives one matrix that solves every initial value problem and, by variation of parameters, every inhomogeneous one.

::: {#thm-existence-uniqueness-linear-systems .theorem name="Existence and uniqueness for linear systems"}
If $A(t)$ and $\mathbf F(t)$ are continuous on an interval $I$, then for every $t_0\in I$ and $\mathbf x_0\in\mathbb R^n$ the system $\mathbf x'=A(t)\mathbf x+\mathbf F(t)$ has exactly one solution on all of $I$ with $\mathbf x(t_0)=\mathbf x_0$.
:::

::: {#def-wronskian-system .definition name="Wronskian"}
The *Wronskian* of $n$ solutions $\mathbf x_1,\dots,\mathbf x_n$ of $\mathbf x'=A(t)\mathbf x$ is
$$
W(t)=\det\bigl(\mathbf x_1(t)\ \cdots\ \mathbf x_n(t)\bigr).
$$
:::

::: {#thm-wronskian-dichotomy .theorem name="The Wronskian vanishes everywhere or nowhere"}
For solutions of $\mathbf x'=A(t)\mathbf x$ on $I$, either $W(t)=0$ for all $t\in I$ (the solutions are dependent) or $W(t)\neq0$ for all $t\in I$ (they are independent, and every solution is a combination of them).
:::

::: {.proof}
1. Suppose $W(t_0)=0$. Then some nontrivial combination $\mathbf y=\sum c_k\mathbf x_k$ has $\mathbf y(t_0)=\mathbf0$.

2. $\mathbf y$ solves the system, and so does the zero function, with the same value at $t_0$; by @thm-existence-uniqueness-linear-systems, $\mathbf y=\mathbf0$ on all of $I$.

3. So the columns are dependent at every $t$, and $W\equiv0$.

4. If instead $W\neq0$ everywhere, then for any solution $\mathbf x$ we can solve $\sum c_k\mathbf x_k(t_0)=\mathbf x(t_0)$, and uniqueness gives $\mathbf x=\sum c_k\mathbf x_k$.
:::

::: {#def-fundamental-matrix .definition name="Fundamental matrix"}
A *fundamental matrix* of $\mathbf x'=A(t)\mathbf x$ is a matrix $X(t)$ whose columns are $n$ independent solutions. It satisfies $X'=AX$, $\det X(t)\neq0$, and the general solution is $\mathbf x=X(t)\,\mathbf c$. The *normalized* fundamental matrix at $t_0$ is $\Phi(t)=X(t)X(t_0)^{-1}$, with $\Phi(t_0)=I$; the solution with $\mathbf x(t_0)=\mathbf x_0$ is $\Phi(t)\mathbf x_0$.
:::

::: {#prp-exponential-fundamental-matrix .proposition name="The exponential matrix is the normalized fundamental matrix" related="def-matrix-exponential"}
For constant $A$, the normalized fundamental matrix at $0$ is $e^{At}$. Hence $e^{At}=X(t)X(0)^{-1}$ for any fundamental matrix $X$.
:::

::: {.proof}
1. Differentiating the series term by term, $\frac{d}{dt}e^{At}=Ae^{At}$, and $e^{A\cdot0}=I$.

2. So each column of $e^{At}$ solves the system, and the columns are independent at $t=0$.

3. $X(t)X(0)^{-1}$ also solves $Y'=AY$ with $Y(0)=I$; by uniqueness, column by column, it equals $e^{At}$.
:::

::: {#exm-exponential-rotation .example name="A rotation"}
For $A=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, the solutions $(\cos t,-\sin t)$ and $(\sin t,\cos t)$ form a fundamental matrix that is already $I$ at $t=0$, so
$$
e^{At}=\begin{pmatrix}\cos t&\sin t\\-\sin t&\cos t\end{pmatrix},
$$
a clockwise rotation by angle $t$.
:::

::: {#fig-fundamental-matrices-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.1]
\draw[->] (-1.8,0) -- (1.9,0) node[lab, right] {$x$};
\draw[->] (0,-1.6) -- (0,1.9) node[lab, above] {$y$};
\draw[faint] (0,0) circle (1.3);
\draw[->, emph, primary] (0,0) -- (1.3,0) node[below right, lab] {$\mathbf x_0$};
\draw[->, emph, accent] (0,0) -- (0.808,-1.018) node[below right, lab] {$e^{At}\mathbf x_0$};
\draw[->, accent] (0.55,0) arc (0:-51.566:0.55); \node[lab, note, accent] at (0.75,-0.3) {$t$};
\end{tikzpicture}
\end{center}
```

For $A=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ the matrix $e^{At}$ rotates every initial vector clockwise by the angle $t$.

:::

::: {#thm-variation-of-parameters-systems .theorem name="Variation of parameters"}
If $X(t)$ is a fundamental matrix of $\mathbf x'=A(t)\mathbf x$, the solutions of $\mathbf x'=A(t)\mathbf x+\mathbf F(t)$ are
$$
\mathbf x(t)=X(t)\left(\int X(t)^{-1}\mathbf F(t)\,dt+\mathbf c\right).
$$
For constant $A$ and $\mathbf x(0)=\mathbf x_0$ this reads $\mathbf x(t)=e^{At}\mathbf x_0+\int_0^te^{A(t-\tau)}\mathbf F(\tau)\,d\tau$.
:::

::: {.proof}
1. Try $\mathbf x=X(t)\mathbf u(t)$. Then $\mathbf x'=X'\mathbf u+X\mathbf u'=AX\mathbf u+X\mathbf u'$.

2. So $\mathbf x'=A\mathbf x+\mathbf F$ holds exactly when $X\mathbf u'=\mathbf F$, that is $\mathbf u'=X^{-1}\mathbf F$ ($X$ is invertible).

3. Integrating gives $\mathbf u=\int X^{-1}\mathbf F\,dt+\mathbf c$; every solution arises, since $\mathbf u=X^{-1}\mathbf x$ for any solution $\mathbf x$.

4. For constant $A$ take $X=e^{At}$, with $X^{-1}=e^{-At}$, and integrate from $0$.
:::

::: {#fig-fundamental-matrices-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (h) at (0,1.2) {$X'=AX$\\ fundamental matrix $X$};
\node[box] (n) at (5,1.2) {$\Phi=X(t)X(t_0)^{-1}$\\ $\Phi(t_0)=I$};
\node[hl box] (v) at (2.5,-0.3) {$\mathbf x=X\left(\int X^{-1}\mathbf F\,dt+\mathbf c\right)$};
\draw[map] (h) -- (n) node[midway, above, lab, note] {normalize}; \draw[map] (h) -- (v) node[midway, left, lab, note] {vary $\mathbf c$};
\end{tikzpicture}
\end{center}
```

One fundamental matrix gives the solution of every initial value problem (normalized) and of every inhomogeneous system (variation of parameters).

:::
