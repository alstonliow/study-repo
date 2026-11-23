---
title: "Conditioning of a Problem"
sources: [mit18335-5, mit18335-7]
requires: [math/linear-algebra/matrix-methods/matrix-norms]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lectures 5 and 7 (condition numbers; the SVD and condition numbers), in our own wording; proofs written out in steps, numbers checked with numpy. -->

Conditioning is a property of a *problem*, not of an algorithm: it measures how much the exact answer can change when the data change slightly. Since the data on a computer are already rounded, no algorithm can be expected to do better than the condition number allows.

::: {#def-relative-condition-number .definition name="Condition number of a problem" generalizes="def-condition-number"}

View a problem as a function $f:X\to Y$ between normed spaces, and fix data $x$ with $x\ne0$ and $f(x)\ne0$. The *relative condition number* of $f$ at $x$ is
$$\kappa(x)=\lim_{\delta\to0}\ \sup_{\lVert\delta x\rVert\le\delta}\ \frac{\lVert f(x+\delta x)-f(x)\rVert/\lVert f(x)\rVert}{\lVert\delta x\rVert/\lVert x\rVert}.$$
If $f$ is differentiable with Jacobian $J(x)$ this equals
$$\kappa(x)=\frac{\lVert J(x)\rVert\,\lVert x\rVert}{\lVert f(x)\rVert},$$
with $\lVert J\rVert$ the induced norm (@def-induced-matrix-norm). The problem is *well-conditioned* at $x$ if $\kappa$ is small (say $1$, $10$ or $100$) and *ill-conditioned* if it is large (say $10^6$ or more).

:::

Roughly, a relative change $10^{-k}$ in the data can change the answer by $\kappa\cdot10^{-k}$: about $\log_{10}\kappa$ digits are lost however the answer is computed.

::: {#exm-conditioning-elementary .example name="Square root, multiplication and subtraction"}

1. $f(x)=\sqrt x$ for $x>0$: $\kappa=\lvert f'(x)\rvert\,\lvert x\rvert/\lvert f(x)\rvert=\frac{1}{2\sqrt x}\cdot\frac{x}{\sqrt x}=\tfrac12$. Well-conditioned everywhere.

2. $f(x_1,x_2)=x_1x_2$ with the $\infty$-norm: $J=[x_2\ \ x_1]$, $\lVert J\rVert_\infty=\lvert x_1\rvert+\lvert x_2\rvert$, so $\kappa=(\lvert x_1\rvert+\lvert x_2\rvert)\max(\lvert x_1\rvert,\lvert x_2\rvert)/\lvert x_1x_2\rvert$, which is $2$ when $\lvert x_1\rvert=\lvert x_2\rvert$.

3. $f(x_1,x_2)=x_1-x_2$ with the $\infty$-norm: $J=[1\ \ {-1}]$, $\lVert J\rVert_\infty=2$, so
$$\kappa=\frac{2\max(\lvert x_1\rvert,\lvert x_2\rvert)}{\lvert x_1-x_2\rvert},$$
arbitrarily large when $x_1\approx x_2$. This is the cancellation of @prp-cancellation seen as a property of the problem.

:::

::: {#fig-conditioning-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.9]
\draw[faint, ->] (-0.3,0) -- (3.3,0); \draw[faint, ->] (0,-0.3) -- (0,3.2);
\draw[regionA] (1.4,1.6) circle (0.32);
\fill (1.4,1.6) circle (1.5pt) node[lab, below=7pt] {$x$};
\node[lab] at (1.6,2.6) {data};
\draw[map] (3.6,1.6) -- (5.2,1.6) node[midway, lab, above] {$f$};
\begin{scope}[xshift=6.2cm]
\draw[faint, ->] (-0.3,0) -- (3.3,0); \draw[faint, ->] (0,-0.3) -- (0,3.2);
\draw[regionB, rotate around={35:(1.6,1.6)}] (1.6,1.6) ellipse (1.3 and 0.12);
\fill (1.6,1.6) circle (1.5pt) node[lab, above left=4pt] {$f(x)$};
\node[lab] at (1.6,2.9) {answers};
\end{scope}
\end{tikzpicture}
\end{center}
```

A small ball of perturbed data around $x$ is mapped by an ill-conditioned problem to a long thin set of answers: some directions of perturbation are amplified enormously. The condition number is the worst amplification of relative size.

:::

::: {#thm-condition-matrix-vector .theorem name="Conditioning of matrix–vector multiplication"}

Let $A$ be a fixed $m\times n$ matrix and $f(\mathbf{x})=A\mathbf{x}$ with $A\mathbf{x}\ne\mathbf{0}$. Then
$$\kappa(\mathbf{x})=\frac{\lVert A\rVert\,\lVert\mathbf{x}\rVert}{\lVert A\mathbf{x}\rVert}.$$
If $A$ is square and invertible, $\kappa(\mathbf{x})\le\lVert A\rVert\,\lVert A^{-1}\rVert$ for every $\mathbf{x}$, and the same bound holds for the problem $\mathbf{b}\mapsto A^{-1}\mathbf{b}$ of solving $A\mathbf{x}=\mathbf{b}$ for $\mathbf{x}$ with $A$ fixed.

:::

::: {.proof}

1. $f$ is linear, so its Jacobian is $A$ and @def-relative-condition-number gives $\kappa=\lVert A\rVert\lVert\mathbf{x}\rVert/\lVert A\mathbf{x}\rVert$.

2. If $A$ is invertible, $\lVert\mathbf{x}\rVert=\lVert A^{-1}A\mathbf{x}\rVert\le\lVert A^{-1}\rVert\,\lVert A\mathbf{x}\rVert$, so $\lVert\mathbf{x}\rVert/\lVert A\mathbf{x}\rVert\le\lVert A^{-1}\rVert$.

3. Solving $A\mathbf{x}=\mathbf{b}$ for fixed $A$ is multiplication by $A^{-1}$; apply steps 1–2 with $A$ and $A^{-1}$ exchanged.

:::

::: {#def-matrix-condition-number-general .definition name="Condition number of a matrix in any norm" generalizes="def-condition-number"}

For a square invertible matrix and an induced norm, $\kappa(A)=\lVert A\rVert\,\lVert A^{-1}\rVert$. In the $2$-norm $\kappa(A)=\sigma_1/\sigma_m$. For a full-rank $m\times n$ matrix with $m\ge n$ one sets $\kappa(A)=\lVert A\rVert_2\lVert A^{+}\rVert_2=\sigma_1/\sigma_n$, with $A^{+}$ the pseudoinverse. $A$ is called ill-conditioned when $\kappa(A)$ is large.

:::

::: {#thm-condition-linear-system .theorem name="Perturbing the matrix of a linear system" generalizes="thm-condition-number-error"}

Let $A$ be invertible and $A\mathbf{x}=\mathbf{b}$ with $\mathbf{b}$ fixed. If $(A+\delta A)(\mathbf{x}+\delta\mathbf{x})=\mathbf{b}$, then to first order in $\delta A$
$$\frac{\lVert\delta\mathbf{x}\rVert}{\lVert\mathbf{x}\rVert}\le\kappa(A)\,\frac{\lVert\delta A\rVert}{\lVert A\rVert},$$
and the bound is attained for some $\delta A$. So the condition number of $A\mapsto A^{-1}\mathbf{b}$ is exactly $\kappa(A)$.

:::

::: {.proof}

1. Expand: $A\,\delta\mathbf{x}+\delta A\,\mathbf{x}+\delta A\,\delta\mathbf{x}=\mathbf{0}$. Dropping the second-order term, $\delta\mathbf{x}=-A^{-1}\,\delta A\,\mathbf{x}$.

2. Hence $\lVert\delta\mathbf{x}\rVert\le\lVert A^{-1}\rVert\,\lVert\delta A\rVert\,\lVert\mathbf{x}\rVert$; dividing by $\lVert\mathbf{x}\rVert$ and writing $\lVert\delta A\rVert=\lVert A\rVert\cdot\lVert\delta A\rVert/\lVert A\rVert$ gives the bound.

3. *Equality* (2-norm). Choose a unit vector $\mathbf{y}$ with $\lVert A^{-1}\mathbf{y}\rVert=\lVert A^{-1}\rVert$ and put $\delta A=\varepsilon\,\mathbf{y}\mathbf{x}^{\mathsf H}/\lVert\mathbf{x}\rVert$. Then $\lVert\delta A\rVert=\varepsilon$ and $\delta A\,\mathbf{x}=\varepsilon\lVert\mathbf{x}\rVert\mathbf{y}$, so $\lVert A^{-1}\delta A\,\mathbf{x}\rVert=\varepsilon\lVert\mathbf{x}\rVert\lVert A^{-1}\rVert$.

:::

::: {#exm-nearly-parallel-lines .example name="Two nearly parallel lines"}

$A=\begin{bmatrix}1&1\\1&1.1\end{bmatrix}$ has $\kappa_2(A)\approx42$. With $\mathbf{b}=(2,\,2.1)$ the solution is $\mathbf{x}=(1,1)$. Changing $b_2$ to $2.2$, a relative change of about $3.4\%$ in $\mathbf{b}$, moves the solution to $(0,2)$, a relative change of $100\%$. Geometrically the two equations are nearly parallel lines, and a small shift of one of them slides the intersection far along the other.

:::

::: {#fig-conditioning-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.4]
\draw[faint, ->] (-0.6,0) -- (3,0) node[lab, right] {$x_1$};
\draw[faint, ->] (0,-0.3) -- (0,2.6) node[lab, above] {$x_2$};
\draw[emph] (-0.5,2.5) -- (2.5,-0.5);
\draw[hl] (-0.5,2.3636) -- (2.5,-0.3636);
\draw[hl, dashed] (-0.5,2.4545) -- (2.5,-0.2727);
\fill (1,1) circle (1.3pt) node[lab, above right] {$(1,1)$};
\fill (0,2) circle (1.3pt) node[lab, left] {$(0,2)$};
\node[lab] at (3.0,-0.65) {$x_1+x_2=2$};
\end{tikzpicture}
\end{center}
```

The lines $x_1+x_2=2$ and $x_1+1.1x_2=2.1$ meet at $(1,1)$. Raising the right side of the second equation to $2.2$ (dashed) shifts that line only slightly, yet the intersection slides along the first line to $(0,2)$.

:::

::: {#rmk-conditioning-1 .remark name="Condition number and distance to singularity"}

In the 2-norm $1/\kappa(A)=\sigma_m/\sigma_1$ is the relative distance from $A$ to the nearest singular matrix: by the SVD, subtracting $\sigma_m\mathbf{u}_m\mathbf{v}_m^{\mathsf H}$ makes $A$ singular, and no smaller perturbation does (@thm-eckart-young-spectral). An ill-conditioned matrix is thus a matrix close to a singular one, and in floating point with $\kappa(A)\gtrsim1/\varepsilon_{\text{mach}}$ it is numerically indistinguishable from singular.

:::
