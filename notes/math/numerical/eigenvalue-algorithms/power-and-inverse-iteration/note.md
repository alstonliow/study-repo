---
title: "Power Iteration, Inverse Iteration and the Rayleigh Quotient"
sources: [mit18335-16, mit18335-17]
requires: [math/numerical/eigenvalue-algorithms/hessenberg-reduction]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lectures 16 and 17 (the power method; shifted QR and Rayleigh quotients) and the reading on real symmetric matrices, in our own wording; proofs written out in steps; the convergence data were computed with numpy for the 4 by 4 example below. -->

The simplest eigenvalue iterations work with one vector. Multiplying by $A$ amplifies the dominant eigenvector; multiplying by $(A-\mu I)^{-1}$ amplifies the eigenvector whose eigenvalue is closest to $\mu$; and the Rayleigh quotient turns an approximate eigenvector into an eigenvalue estimate of twice the accuracy. Together they explain how the QR algorithm works. Throughout, $A$ is real symmetric with eigenvalues $\lvert\lambda_1\rvert\ge\lvert\lambda_2\rvert\ge\dots\ge\lvert\lambda_m\rvert$ and orthonormal eigenvectors $\mathbf{q}_1,\dots,\mathbf{q}_m$.

::: {#def-rayleigh-quotient .definition name="Rayleigh quotient"}

For a nonzero $\mathbf{x}\in\mathbb{R}^m$ the *Rayleigh quotient* of $A$ is
$$r(\mathbf{x})=\frac{\mathbf{x}^{\mathsf T}A\mathbf{x}}{\mathbf{x}^{\mathsf T}\mathbf{x}}.$$
It is the scalar $\alpha$ that minimises $\lVert A\mathbf{x}-\alpha\mathbf{x}\rVert$, so it is the best eigenvalue estimate for a given approximate eigenvector.

:::

::: {#thm-rayleigh-quotient-quadratic .theorem name="The Rayleigh quotient is quadratically accurate"}

The gradient of $r$ is $\nabla r(\mathbf{x})=\dfrac{2}{\mathbf{x}^{\mathsf T}\mathbf{x}}\bigl(A\mathbf{x}-r(\mathbf{x})\mathbf{x}\bigr)$, which vanishes exactly at eigenvectors. Consequently, as $\mathbf{x}\to\mathbf{q}_J$,
$$r(\mathbf{x})-\lambda_J=O\bigl(\lVert\mathbf{x}-\mathbf{q}_J\rVert^2\bigr).$$

:::

::: {.proof}

1. Differentiate $r(\mathbf{x})\,\mathbf{x}^{\mathsf T}\mathbf{x}=\mathbf{x}^{\mathsf T}A\mathbf{x}$: $\nabla r\,(\mathbf{x}^{\mathsf T}\mathbf{x})+2r\mathbf{x}=2A\mathbf{x}$, using $A=A^{\mathsf T}$.

2. So $\nabla r=0$ iff $A\mathbf{x}=r(\mathbf{x})\mathbf{x}$, i.e. iff $\mathbf{x}$ is an eigenvector with eigenvalue $r(\mathbf{x})$.

3. *Quadratic accuracy, directly.* Write $\mathbf{x}=\sum_ja_j\mathbf{q}_j$ with $a_J$ close to $1$ and the other $a_j$ small. Then $r(\mathbf{x})=\sum_ja_j^2\lambda_j/\sum_ja_j^2$ and
$$r(\mathbf{x})-\lambda_J=\frac{\sum_{j\ne J}a_j^2(\lambda_j-\lambda_J)}{\sum_ja_j^2}.$$

4. The numerator is $O(\sum_{j\ne J}a_j^2)$, and $\sum_{j\ne J}a_j^2\le\lVert\mathbf{x}-\mathbf{q}_J\rVert^2$, which gives the claim.

:::

::: {#def-power-iteration .definition name="Power iteration"}

Start from a unit vector $\mathbf{v}^{(0)}$ and repeat
$$\mathbf{w}=A\mathbf{v}^{(k-1)},\qquad\mathbf{v}^{(k)}=\mathbf{w}/\lVert\mathbf{w}\rVert,\qquad\lambda^{(k)}=r(\mathbf{v}^{(k)}).$$

:::

```{=latex}
\begin{algorithm}
\caption{Power iteration}
\begin{algorithmic}
\INPUT symmetric $A$, unit vector $\mathbf{v}^{(0)}$
\FOR{$k=1,2,\dots$}
    \STATE $\mathbf{w}\gets A\mathbf{v}^{(k-1)}$
    \STATE $\mathbf{v}^{(k)}\gets\mathbf{w}/\lVert\mathbf{w}\rVert$
    \STATE $\lambda^{(k)}\gets(\mathbf{v}^{(k)})^{\mathsf T}A\mathbf{v}^{(k)}$
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

::: {#thm-power-iteration-convergence .theorem name="Convergence of power iteration"}

If $\lvert\lambda_1\rvert>\lvert\lambda_2\rvert$ and $\mathbf{q}_1^{\mathsf T}\mathbf{v}^{(0)}\ne0$, then
$$\lVert\mathbf{v}^{(k)}-(\pm\mathbf{q}_1)\rVert=O\Bigl(\Bigl\lvert\frac{\lambda_2}{\lambda_1}\Bigr\rvert^k\Bigr),\qquad\lvert\lambda^{(k)}-\lambda_1\rvert=O\Bigl(\Bigl\lvert\frac{\lambda_2}{\lambda_1}\Bigr\rvert^{2k}\Bigr),$$
with the sign $\pm$ fixed or alternating at each step.

:::

::: {.proof}

1. $\mathbf{v}^{(k)}$ is a multiple of $A^k\mathbf{v}^{(0)}$. Expanding $\mathbf{v}^{(0)}=\sum_ja_j\mathbf{q}_j$ with $a_1\ne0$,
$$A^k\mathbf{v}^{(0)}=\sum_ja_j\lambda_j^k\mathbf{q}_j=a_1\lambda_1^k\Bigl(\mathbf{q}_1+\sum_{j\ge2}\frac{a_j}{a_1}\Bigl(\frac{\lambda_j}{\lambda_1}\Bigr)^k\mathbf{q}_j\Bigr).$$

2. Each ratio $\lvert\lambda_j/\lambda_1\rvert^k\le\lvert\lambda_2/\lambda_1\rvert^k$, so after normalising, $\mathbf{v}^{(k)}=\pm\mathbf{q}_1+O(\lvert\lambda_2/\lambda_1\rvert^k)$.

3. The eigenvalue estimate follows from @thm-rayleigh-quotient-quadratic.

:::

::: {#fig-power-and-inverse-iteration-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=2.4]
\draw[faint, ->] (-0.1,0) -- (1.2,0); \draw[faint, ->] (0,-0.1) -- (0,1.15);
\draw[faint] (1,0) arc (0:90:1);
\draw[hl, ->] (0,0) -- (38.0:1.12) node[lab, below right] {$\mathbf{q}_1$};
\foreach \a/\k in {90.0/0,56.3/1,42.9/2} {\draw[emph, ->] (0,0) -- (\a:1); \node[lab] at (\a:1.14) {$\mathbf{v}^{(\k)}$};}
\draw[emph, ->] (0,0) -- (39.3:1);
\end{tikzpicture}
\end{center}
```

Power iteration for $A=\left[\begin{smallmatrix}2&1\\1&1.5\end{smallmatrix}\right]$ (eigenvalues $2.78$ and $0.72$) from $\mathbf{v}^{(0)}=\mathbf{e}_2$: the iterates turn towards the dominant eigenvector $\mathbf{q}_1$ at angle $38.0^\circ$, the angle error shrinking by about $\lambda_2/\lambda_1\approx0.26$ per step ($52^\circ$, $18^\circ$, $4.9^\circ$, $1.3^\circ$).

:::

::: {#def-inverse-iteration .definition name="Inverse iteration"}

Fix a *shift* $\mu$ that is not an eigenvalue and apply power iteration to $(A-\mu I)^{-1}$: solve $(A-\mu I)\mathbf{w}=\mathbf{v}^{(k-1)}$, normalise $\mathbf{v}^{(k)}=\mathbf{w}/\lVert\mathbf{w}\rVert$. The matrix $(A-\mu I)^{-1}$ has eigenvalues $1/(\lambda_j-\mu)$, largest for the $\lambda_J$ nearest to $\mu$, so if $\lambda_K$ is the next nearest,
$$\lVert\mathbf{v}^{(k)}-(\pm\mathbf{q}_J)\rVert=O\Bigl(\Bigl\lvert\frac{\mu-\lambda_J}{\mu-\lambda_K}\Bigr\rvert^k\Bigr).$$
Factor $A-\mu I$ once ($O(m^3)$, or $O(m)$ if $A$ is tridiagonal) and reuse the factors at every step.

:::

::: {#rmk-power-and-inverse-iteration-1 .remark name="Solving a nearly singular system is harmless here"}

When $\mu$ is very close to $\lambda_J$, $A-\mu I$ is nearly singular and the solve has a large error. But the error is almost entirely in the direction of $\mathbf{q}_J$, the direction we want, and it disappears in the normalisation. A backward stable solver returns the exact solution for a slightly perturbed matrix, whose dominant eigenvector is still close to $\mathbf{q}_J$.

:::

::: {#def-rayleigh-quotient-iteration .definition name="Rayleigh quotient iteration"}

Combine the two ideas, updating the shift at every step: start from a unit $\mathbf{v}^{(0)}$ and $\lambda^{(0)}=r(\mathbf{v}^{(0)})$, and repeat: solve $(A-\lambda^{(k-1)}I)\mathbf{w}=\mathbf{v}^{(k-1)}$, set $\mathbf{v}^{(k)}=\mathbf{w}/\lVert\mathbf{w}\rVert$ and $\lambda^{(k)}=r(\mathbf{v}^{(k)})$.

:::

```{=latex}
\begin{algorithm}
\caption{Rayleigh quotient iteration}
\begin{algorithmic}
\INPUT symmetric $A$, unit vector $\mathbf{v}^{(0)}$
\STATE $\lambda^{(0)}\gets(\mathbf{v}^{(0)})^{\mathsf T}A\mathbf{v}^{(0)}$
\FOR{$k=1,2,\dots$}
    \STATE solve $(A-\lambda^{(k-1)}I)\mathbf{w}=\mathbf{v}^{(k-1)}$
    \STATE $\mathbf{v}^{(k)}\gets\mathbf{w}/\lVert\mathbf{w}\rVert$
    \STATE $\lambda^{(k)}\gets(\mathbf{v}^{(k)})^{\mathsf T}A\mathbf{v}^{(k)}$
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

::: {#thm-rqi-cubic .theorem name="Rayleigh quotient iteration converges cubically"}

If Rayleigh quotient iteration converges to an eigenvector $\mathbf{q}_J$ of a symmetric matrix, then for $k$ large
$$\lVert\mathbf{v}^{(k+1)}-(\pm\mathbf{q}_J)\rVert=O\bigl(\lVert\mathbf{v}^{(k)}-(\pm\mathbf{q}_J)\rVert^3\bigr),\qquad\lvert\lambda^{(k+1)}-\lambda_J\rvert=O\bigl(\lvert\lambda^{(k)}-\lambda_J\rvert^3\bigr).$$

:::

::: {.proof}

1. Let $\epsilon=\lVert\mathbf{v}^{(k)}-\mathbf{q}_J\rVert$ (choosing the sign). By @thm-rayleigh-quotient-quadratic, $\lvert\lambda^{(k)}-\lambda_J\rvert=O(\epsilon^2)$.

2. One step of inverse iteration with shift $\mu=\lambda^{(k)}$ multiplies the error by $\lvert\mu-\lambda_J\rvert/\lvert\mu-\lambda_K\rvert$ to first order (@def-inverse-iteration), where $\lvert\mu-\lambda_K\rvert$ stays bounded away from zero once $\mu$ is close to $\lambda_J$, since $\lambda_J$ is a simple eigenvalue of the limit.

3. Hence $\lVert\mathbf{v}^{(k+1)}-\mathbf{q}_J\rVert=O(\epsilon^2)\cdot O(\epsilon)=O(\epsilon^3)$.

4. Applying step 1 at $k+1$: $\lvert\lambda^{(k+1)}-\lambda_J\rvert=O(\epsilon^6)=O(\lvert\lambda^{(k)}-\lambda_J\rvert^3)$.

:::

::: {#exm-eigen-iterations-compared .example name="The three iterations on one matrix"}

Let $A=\begin{bmatrix}4&1&0&0\\1&3&1&0\\0&1&2&1\\0&0&1&1\end{bmatrix}$, with eigenvalues $4.7453,\,3.1773,\,1.8227,\,0.2547$, and start from $\mathbf{v}^{(0)}=(1,1,1,1)/2$. Power iteration converges to $\mathbf{q}_1$ at the rate $\lambda_2/\lambda_1\approx0.67$, gaining one digit every $6$ steps. Inverse iteration with $\mu=4.5$ has rate $\lvert4.5-4.7453\rvert/\lvert4.5-3.1773\rvert\approx0.19$, a digit about every $1.4$ steps. Rayleigh quotient iteration has shifts $4.0,\ 4.43,\ 4.724,\ 4.74528$ and eigenvector errors $10^{-0.4},10^{-0.9},10^{-2.8},10^{-8.4}$: the number of correct digits triples at each step.

:::

::: {#fig-power-and-inverse-iteration-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.36cm, y=0.42cm]
\draw[->, faint] (0,0) -- (31.5,0) node[lab, right] {$k$};
\draw[->, faint] (0,0) -- (0,-9.8) node[lab, below] {$\log_{10}\lVert\mathbf{v}^{(k)}\mp\mathbf{q}_1\rVert$};
\foreach \x in {0,10,20,30} {\draw[faint] (\x,-0.15) -- (\x,0.15); \node[tick, above] at (\x,0.15) {$\x$};}
\foreach \y in {-2,-4,-6,-8} {\draw[faint] (-0.2,\y) -- (0.2,\y); \node[tick, left] at (-0.2,\y) {$\y$};}
\draw[emph] plot coordinates {(0,-0.23) (3,-0.82) (6,-1.35) (9,-1.87) (12,-2.39) (15,-2.91) (18,-3.44) (21,-3.96) (24,-4.48) (27,-5.0) (30,-5.53)};
\draw[emph, dashed] plot coordinates {(0,-0.23) (1,-1.0) (2,-1.76) (3,-2.49) (4,-3.23) (5,-3.96) (6,-4.69) (7,-5.42) (8,-6.16) (9,-6.89) (10,-7.62) (11,-8.35) (12,-9.08)};
\draw[hl] plot coordinates {(0,-0.23) (1,-0.36) (2,-0.94) (3,-2.81) (4,-8.44)};
\foreach \p in {(0,-0.23),(1,-0.36),(2,-0.94),(3,-2.81),(4,-8.44)} {\fill[accent] \p circle (2.4pt);}
\node[lab] at (25,-3.4) {power};
\node[lab] at (14.5,-8.2) {inverse, $\mu=4.5$};
\node[lab] at (7.5,-8.6) {RQI};
\end{tikzpicture}
\end{center}
```

Error of the eigenvector estimate in @exm-eigen-iterations-compared: linear convergence for power iteration (rate $0.67$) and inverse iteration (rate $0.19$), cubic for Rayleigh quotient iteration, which reaches $10^{-8}$ in four steps.

:::
