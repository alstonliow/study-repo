---
title: "Algorithms for Least Squares"
sources: [mit18335-8, mit18335-9]
requires: [math/numerical/qr-and-least-squares/gram-schmidt-in-floating-point]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lectures 8 and 9 (linear regression and the generalized SVD; solving the normal equations by QR), in our own wording; proofs written out in steps; the polynomial-fitting experiment was run in Python (numpy, double precision) against a 50-digit mpmath solution. -->

The full-rank least squares problem $\min_{\mathbf{x}}\lVert A\mathbf{x}-\mathbf{b}\rVert_2$, with $A$ of size $m\times n$, $m\ge n$, has the unique solution given by the normal equations $A^{\mathsf H}A\mathbf{x}=A^{\mathsf H}\mathbf{b}$ (@thm-least-squares-normal-equations). There are three standard ways to compute it, with different costs and very different accuracy.

::: {#def-least-squares-algorithms .definition name="Three least squares algorithms"}

1. *Normal equations.* Form $A^{\mathsf H}A$ and $A^{\mathsf H}\mathbf{b}$, compute the Cholesky factorization $A^{\mathsf H}A=R^{\mathsf H}R$ (@def-cholesky-factorization), and solve $R^{\mathsf H}\mathbf{w}=A^{\mathsf H}\mathbf{b}$, $R\mathbf{x}=\mathbf{w}$. Cost $\sim mn^2+\tfrac13n^3$ flops.

2. *QR.* Compute $A=\hat Q\hat R$ by Householder (@def-householder-qr), form $\mathbf{y}=\hat Q^{\mathsf H}\mathbf{b}$ by applying the reflectors, and solve $\hat R\mathbf{x}=\mathbf{y}$ by back substitution. Cost $\sim2mn^2-\tfrac23n^3$.

3. *SVD.* Compute $A=\hat U\hat\Sigma V^{\mathsf H}$, then $\mathbf{x}=V\hat\Sigma^{-1}\hat U^{\mathsf H}\mathbf{b}$. Cost $\sim2mn^2+11n^3$ for a standard dense SVD. It also handles rank-deficient $A$: dropping singular values below a tolerance gives the minimum-norm solution $A^{+}\mathbf{b}$.

:::

::: {#prp-least-squares-via-qr .proposition name="Why QR solves least squares"}

If $A=\hat Q\hat R$ with $\hat R$ invertible, the least squares solution is $\mathbf{x}=\hat R^{-1}\hat Q^{\mathsf H}\mathbf{b}$, and the residual norm is $\lVert(I-\hat Q\hat Q^{\mathsf H})\mathbf{b}\rVert$.

:::

::: {.proof}

1. Complete $\hat Q$ to a unitary $Q=[\hat Q\ \ Q_2]$. Since $Q^{\mathsf H}$ preserves norms, $\lVert A\mathbf{x}-\mathbf{b}\rVert^2=\lVert Q^{\mathsf H}(A\mathbf{x}-\mathbf{b})\rVert^2=\lVert\hat R\mathbf{x}-\hat Q^{\mathsf H}\mathbf{b}\rVert^2+\lVert Q_2^{\mathsf H}\mathbf{b}\rVert^2$.

2. The second term does not depend on $\mathbf{x}$, and the first is $0$ exactly when $\hat R\mathbf{x}=\hat Q^{\mathsf H}\mathbf{b}$.

3. The minimum is $\lVert Q_2^{\mathsf H}\mathbf{b}\rVert=\lVert Q_2Q_2^{\mathsf H}\mathbf{b}\rVert=\lVert(I-\hat Q\hat Q^{\mathsf H})\mathbf{b}\rVert$.

:::

::: {#thm-least-squares-conditioning .theorem name="Conditioning of least squares with respect to b"}

Let $A$ have full rank with $\kappa=\kappa(A)=\sigma_1/\sigma_n$, let $\mathbf{y}=A\mathbf{x}$ be the orthogonal projection of $\mathbf{b}\ne\mathbf{0}$ onto $\operatorname{range}(A)$, $\theta$ the angle between $\mathbf{b}$ and $\mathbf{y}$ (with $\theta<\pi/2$), and $\eta=\lVert A\rVert\lVert\mathbf{x}\rVert/\lVert A\mathbf{x}\rVert\in[1,\kappa]$. As a function of $\mathbf{b}$ (with $A$ fixed), the relative condition number of $\mathbf{x}$ is
$$\kappa_{\mathbf{b}\mapsto\mathbf{x}}=\frac{\kappa}{\eta\cos\theta}.$$

:::

::: {.proof}

1. $\mathbf{x}=A^{+}\mathbf{b}$ is linear in $\mathbf{b}$ with Jacobian $A^{+}$, and $\lVert A^{+}\rVert=1/\sigma_n$. By @def-relative-condition-number, $\kappa_{\mathbf{b}\mapsto\mathbf{x}}=\lVert A^{+}\rVert\lVert\mathbf{b}\rVert/\lVert\mathbf{x}\rVert$.

2. $\lVert\mathbf{y}\rVert=\lVert\mathbf{b}\rVert\cos\theta$, so $\lVert\mathbf{b}\rVert=\lVert A\mathbf{x}\rVert/\cos\theta$.

3. Substituting, $\kappa_{\mathbf{b}\mapsto\mathbf{x}}=\dfrac{\lVert A\mathbf{x}\rVert}{\sigma_n\lVert\mathbf{x}\rVert\cos\theta}=\dfrac{\sigma_1}{\sigma_n}\cdot\dfrac{\lVert A\mathbf{x}\rVert}{\lVert A\rVert\lVert\mathbf{x}\rVert}\cdot\dfrac1{\cos\theta}=\dfrac{\kappa}{\eta\cos\theta}$, using $\lVert A\rVert=\sigma_1$.

:::

::: {#fig-least-squares-algorithms-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.1]
\fill[tintA] (-0.6,-0.6) -- (4.6,-0.6) -- (5.6,1.4) -- (0.4,1.4) -- cycle;
\node[lab] at (5.2,0.2) {$\operatorname{range}(A)$};
\draw[emph, ->] (0.8,0.2) -- (3.8,2.9) node[lab, above] {$\mathbf{b}$};
\draw[hl, ->] (0.8,0.2) -- (3.8,0.8) node[lab, below right] {$\mathbf{y}=A\mathbf{x}$};
\draw[faint, dashed] (3.8,0.8) -- (3.8,2.9) node[lab, midway, right] {$\mathbf{r}=\mathbf{b}-A\mathbf{x}$};
\draw[faint] (3.6,0.76) -- (3.6,0.96) -- (3.8,1.0);
\draw[faint] (1.5,0.34) arc (11:42:0.7); \node[lab] at (1.75,0.6) {$\theta$};
\end{tikzpicture}
\end{center}
```

The least squares solution makes $A\mathbf{x}$ the orthogonal projection $\mathbf{y}$ of $\mathbf{b}$ onto $\operatorname{range}(A)$. When $\theta$ is near $\pi/2$ the projection is tiny compared with $\mathbf{b}$ and small changes in $\mathbf{b}$ change $\mathbf{x}$ a lot (@thm-least-squares-conditioning).

:::

::: {#rmk-least-squares-algorithms-1 .remark name="Sensitivity to A and the squared condition number"}

The condition number with respect to perturbations of $A$ is larger: up to a modest factor it is $\kappa+\kappa^2\tan\theta/\eta$. So when the fit is good ($\theta$ small) the problem behaves like a linear system with condition $\kappa$, but when the residual is large the problem is genuinely sensitive like $\kappa^2$. Householder QR and the SVD are backward stable for least squares, so their errors are $O(\varepsilon_{\text{mach}})$ times this condition number. The normal equations are not: forming $A^{\mathsf H}A$ squares the condition number, $\kappa(A^{\mathsf H}A)=\kappa(A)^2$, whatever $\theta$ is, so they lose about twice as many digits as necessary when the fit is good. They remain the fastest method and are fine when $A$ is well-conditioned.

:::

::: {#exm-polynomial-fit-algorithms .example name="Fitting a polynomial of degree 14"}

Fit $f(t)=e^{\sin4t}$ at $100$ equally spaced points in $[0,1]$ by a polynomial $x_1+x_2t+\dots+x_{15}t^{14}$, scaling $f$ so that the exact leading coefficient is $x_{15}=1$. The Vandermonde matrix has $\kappa(A)\approx2.3\times10^{10}$ and the fit is very good, so $\kappa_{\mathbf{b}\mapsto\mathbf{x}}$ is of order $\kappa$. Relative errors of the computed $x_{15}$ in double precision:

| method | error in $x_{15}$ |
|---|---|
| Householder QR | $1.3\times10^{-8}$ |
| SVD | $1.3\times10^{-8}$ |
| modified Gram–Schmidt, $\hat Q^{\mathsf T}\mathbf{b}$ formed explicitly | $2.7\times10^{-2}$ |
| modified Gram–Schmidt on $[A\ \ \mathbf{b}]$ | $1.5\times10^{-8}$ |
| normal equations | $0.97$ (Cholesky fails; Gaussian elimination used) |

Householder and the SVD lose the $\log_{10}\kappa\approx10$ digits the conditioning predicts and no more. MGS with an explicit $\hat Q^{\mathsf T}\mathbf{b}$ suffers from the loss of orthogonality of $\hat Q$; running MGS on the augmented matrix $[A\ \ \mathbf{b}]$ and reading $\hat Q^{\mathsf T}\mathbf{b}$ off the last column of $\hat R$ repairs this. The normal equations have $\kappa(A^{\mathsf T}A)\approx10^{20}>1/\varepsilon_{\text{mach}}$: $A^{\mathsf T}A$ is not even numerically positive definite, and no digit is correct.

:::

::: {#fig-least-squares-algorithms-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.3cm, y=0.35cm]
\draw[->, faint] (0,0) -- (0,9) node[lab, above] {$-\log_{10}(\text{error})$};
\draw[faint] (0,0) -- (5.6,0);
\foreach \y in {0,2,4,6,8} {\draw[faint] (-0.06,\y) -- (0.06,\y); \node[tick, left] at (-0.06,\y) {$\y$};}
\draw[faint, dashed] (0,5.6) -- (5.6,5.6) node[lab, right] {$\varepsilon_{\text{mach}}\kappa$};
\fill[bar] (0.3,0) rectangle (0.9,7.87); \node[tick, below] at (0.6,0) {Householder};
\fill[bar] (1.3,0) rectangle (1.9,7.87); \node[tick, below] at (1.6,0) {SVD};
\fill[accent] (2.3,0) rectangle (2.9,1.57); \node[tick, below] at (2.6,0) {MGS};
\fill[bar] (3.3,0) rectangle (3.9,7.82); \node[tick, below] at (3.6,-1.1) {MGS on $[A\ \mathbf{b}]$};
\fill[accent] (4.3,0) rectangle (4.9,0.05); \node[tick, below] at (4.6,0) {normal eq.};
\end{tikzpicture}
\end{center}
```

Correct digits of $x_{15}$ in @exm-polynomial-fit-algorithms. The dashed line marks $\varepsilon_{\text{mach}}\kappa(A)\approx2.5\times10^{-6}$; the backward stable methods do somewhat better than this worst-case estimate.

:::

::: {#rmk-least-squares-algorithms-2 .remark name="Regularised regression and the generalized SVD"}

In regression one often minimises $\lVert A\mathbf{x}-\mathbf{b}\rVert^2+\lambda\lVert B\mathbf{x}\rVert^2$, for example with $B=I$ (ridge regression) or $B$ a difference matrix (smoothness). It is the ordinary least squares problem for the stacked matrix $\bigl[\begin{smallmatrix}A\\\sqrt\lambda B\end{smallmatrix}\bigr]$, so QR applies. For $B=I$ the SVD of $A$ gives $\mathbf{x}_\lambda=\sum_i\dfrac{\sigma_i^2}{\sigma_i^2+\lambda}\,\dfrac{\mathbf{u}_i^{\mathsf H}\mathbf{b}}{\sigma_i}\mathbf{v}_i$: the regulariser damps the components with small $\sigma_i$, which are the ones amplified by ill-conditioning. For general $B$ the *generalized SVD* $A=U\,C\,X^{-1}$, $B=V\,S\,X^{-1}$ ($U,V$ unitary, $C,S$ diagonal, $C^{\mathsf H}C+S^{\mathsf H}S=I$) diagonalises both terms at once and gives the same kind of formula for every $\lambda$ from one factorization.

:::
