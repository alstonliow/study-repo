---
title: "Cholesky Factorization"
sources: [mit18335-14]
requires: [math/numerical/direct-solvers/lu-stability]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 14 (Cholesky factorization and other specialized solvers), in our own wording; proofs written out in steps. -->

When $A$ is Hermitian positive definite, symmetric elimination needs no pivoting, half the work and half the storage. The resulting Cholesky factorization is the standard solver for the positive definite systems that arise from energy minimisation, normal equations and covariance matrices.

::: {#thm-cholesky-existence .theorem name="Existence and uniqueness of the Cholesky factorization" related="prp-symmetric-ldlt"}

Every Hermitian positive definite matrix $A\in\mathbb{C}^{m\times m}$ has a unique factorization
$$A=R^{\mathsf H}R$$
with $R$ upper triangular and $r_{jj}>0$ for all $j$.

:::

::: {.proof}

1. *Induction on $m$.* For $m=1$, $A=(a_{11})$ with $a_{11}>0$ and $R=(\sqrt{a_{11}})$ is the only choice.

2. Write $A=\begin{bmatrix}a_{11}&\mathbf{w}^{\mathsf H}\\\mathbf{w}&K\end{bmatrix}$. Here $a_{11}=\mathbf{e}_1^{\mathsf H}A\mathbf{e}_1>0$; put $\alpha=\sqrt{a_{11}}$. Then
$$A=\begin{bmatrix}\alpha&0\\\mathbf{w}/\alpha&I\end{bmatrix}\begin{bmatrix}1&0\\0&K-\mathbf{w}\mathbf{w}^{\mathsf H}/a_{11}\end{bmatrix}\begin{bmatrix}\alpha&\mathbf{w}^{\mathsf H}/\alpha\\0&I\end{bmatrix}=R_1^{\mathsf H}A_1R_1 .$$

3. The middle matrix is congruent to $A$ via the invertible $R_1$, so it is positive definite (for $\mathbf{y}\ne\mathbf{0}$, $\mathbf{y}^{\mathsf H}A_1\mathbf{y}=\mathbf{z}^{\mathsf H}A\mathbf{z}>0$ with $\mathbf{z}=R_1^{-1}\mathbf{y}$). Its lower block $S=K-\mathbf{w}\mathbf{w}^{\mathsf H}/a_{11}$ is therefore Hermitian positive definite of size $m-1$.

4. By induction $S=\hat R^{\mathsf H}\hat R$, and then $A=R^{\mathsf H}R$ with $R=\begin{bmatrix}\alpha&\mathbf{w}^{\mathsf H}/\alpha\\0&\hat R\end{bmatrix}$.

5. *Uniqueness.* In any such factorization the first row of $R$ is forced: $r_{11}^2=a_{11}$ with $r_{11}>0$, and $r_{11}r_{1j}=a_{1j}$. Then $\hat R^{\mathsf H}\hat R=S$ is forced too, and by induction $\hat R$ is unique.

:::

::: {#def-cholesky-factorization .definition name="Cholesky algorithm"}

The proof is an algorithm: for $k=1,\dots,m$, set $r_{kk}=\sqrt{a_{kk}}$, divide the rest of row $k$ by it, and subtract the outer product of that row from the trailing block (only its upper triangle need be stored and updated). Equivalently, row by row,
$$r_{kk}=\Bigl(a_{kk}-\sum_{i<k}\lvert r_{ik}\rvert^2\Bigr)^{1/2},\qquad r_{kj}=\frac{a_{kj}-\sum_{i<k}\overline{r_{ik}}\,r_{ij}}{r_{kk}}\quad(j>k).$$
It costs $\sim\tfrac13m^3$ flops, half of LU.

:::

```{=latex}
\begin{algorithm}
\caption{Cholesky factorization (outer-product form)}
\begin{algorithmic}
\INPUT Hermitian positive definite $A$; $R\gets$ upper triangle of $A$
\FOR{$k=1,\dots,m$}
    \FOR{$j=k+1,\dots,m$}
        \STATE $R_{j,\,j:m}\gets R_{j,\,j:m}-\bigl(\overline{r_{kj}}/r_{kk}\bigr)R_{k,\,j:m}$
    \ENDFOR
    \STATE $R_{k,\,k:m}\gets R_{k,\,k:m}/\sqrt{r_{kk}}$
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

::: {#exm-cholesky-three-by-three .example name="A 3 by 3 factorization"}

$$\begin{bmatrix}4&2&2\\2&5&3\\2&3&6\end{bmatrix}=\begin{bmatrix}2&0&0\\1&2&0\\1&1&2\end{bmatrix}\begin{bmatrix}2&1&1\\0&2&1\\0&0&2\end{bmatrix}.$$
Step 1: $r_{11}=\sqrt4=2$ and the first row is $(2,1,1)$; the trailing block becomes $\begin{bmatrix}5&3\\3&6\end{bmatrix}-\begin{bmatrix}1\\1\end{bmatrix}\begin{bmatrix}1&1\end{bmatrix}=\begin{bmatrix}4&2\\2&5\end{bmatrix}$. Step 2: $r_{22}=2$, $r_{23}=1$, leaving $5-1=4$. Step 3: $r_{33}=2$. Every pivot is positive, as the theorem guarantees.

:::

::: {#fig-cholesky-factorization-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.5cm, y=0.5cm]
\node[lab] at (1.5,0.6) {$A$};
\foreach \r/\a/\b/\c in {1/4/2/2,2/2/5/3,3/2/3/6} {\node[tick] at (0.5,-\r+0.5) {$\a$}; \node[tick] at (1.5,-\r+0.5) {$\b$}; \node[tick] at (2.5,-\r+0.5) {$\c$};}
\draw[hl cell] (0,-1) rectangle (3,0); \draw[hl cell] (0,-3) rectangle (1,-1);
\foreach \r/\a/\b/\c in {1/4/2/2,2/2/5/3,3/2/3/6} {\node[tick] at (0.5,-\r+0.5) {$\a$}; \node[tick] at (1.5,-\r+0.5) {$\b$}; \node[tick] at (2.5,-\r+0.5) {$\c$};}
\draw[faint] (0,0) rectangle (3,-3);
\draw[map] (3.4,-1.5) -- (5.0,-1.5) node[midway, note, below=2pt] {step 1};
\begin{scope}[xshift=2.8cm]
\node[lab] at (1.5,0.6) {row $1$ of $R$, block $S$};
\draw[hl cell] (0,-1) rectangle (3,0);
\node[tick] at (0.5,-0.5) {$2$}; \node[tick] at (1.5,-0.5) {$1$}; \node[tick] at (2.5,-0.5) {$1$};
\draw[cell frame] (1,-3) rectangle (3,-1);
\node[tick] at (1.5,-1.5) {$4$}; \node[tick] at (2.5,-1.5) {$2$}; \node[tick] at (1.5,-2.5) {$2$}; \node[tick] at (2.5,-2.5) {$5$};
\end{scope}
\draw[map] (9.0,-1.5) -- (10.6,-1.5) node[midway, note, below=2pt] {steps 2,3};
\begin{scope}[xshift=5.6cm]
\node[lab] at (1.5,0.6) {$R$};
\foreach \r/\a/\b/\c in {1/2/1/1} {\node[tick] at (0.5,-0.5) {$2$}; \node[tick] at (1.5,-0.5) {$1$}; \node[tick] at (2.5,-0.5) {$1$};}
\node[tick] at (1.5,-1.5) {$2$}; \node[tick] at (2.5,-1.5) {$1$}; \node[tick] at (2.5,-2.5) {$2$};
\node[tick, text=rule] at (0.5,-1.5) {$0$}; \node[tick, text=rule] at (0.5,-2.5) {$0$}; \node[tick, text=rule] at (1.5,-2.5) {$0$};
\draw[faint] (0,0) rectangle (3,-3);
\end{scope}
\end{tikzpicture}
\end{center}
```

The Cholesky algorithm on @exm-cholesky-three-by-three. Step 1 uses the first row and column of $A$ (shaded) to produce the first row of $R$ and the Schur complement $S$ of positive definite size $2$; the same step applied to $S$ and then to the remaining $1\times1$ block finishes $R$.

:::

::: {#thm-cholesky-stable .theorem name="Cholesky is backward stable without pivoting"}

For Hermitian positive definite $A$, every entry of the Cholesky factor satisfies $\lvert r_{ij}\rvert\le\sqrt{a_{jj}}\le\lVert A\rVert_2^{1/2}$, so $\lVert R\rVert_2^2=\lVert A\rVert_2$: there is no growth. Consequently the computed factor satisfies $\tilde R^{\mathsf H}\tilde R=A+\delta A$ with $\lVert\delta A\rVert/\lVert A\rVert=O(\varepsilon_{\text{mach}})$ (provided the algorithm runs to completion, which it does when $\kappa(A)\varepsilon_{\text{mach}}$ is small).

:::

::: {.proof}

1. Column $j$ of $A=R^{\mathsf H}R$ on the diagonal gives $a_{jj}=\sum_{i\le j}\lvert r_{ij}\rvert^2$, so each $\lvert r_{ij}\rvert\le\sqrt{a_{jj}}$.

2. $a_{jj}=\mathbf{e}_j^{\mathsf H}A\mathbf{e}_j\le\lVert A\rVert_2$.

3. $\lVert R\rVert_2^2=\lVert R^{\mathsf H}R\rVert_2=\lVert A\rVert_2$, since $\lVert R\rVert_2^2$ is the largest eigenvalue of $R^{\mathsf H}R$.

4. The rounding analysis of @thm-lu-backward-error applies with $L=R^{\mathsf H}$ and gives $\lvert\delta A\rvert\le c_m\varepsilon_{\text{mach}}\lvert R^{\mathsf H}\rvert\lvert R\rvert$ entrywise. By Cauchy–Schwarz, $(\lvert R^{\mathsf H}\rvert\lvert R\rvert)_{ij}\le\sqrt{a_{ii}a_{jj}}\le\lVert A\rVert_2$, so $\lVert\delta A\rVert=O(\varepsilon_{\text{mach}})\lVert A\rVert$.

:::

::: {#rmk-cholesky-factorization-1 .remark name="Other specialised solvers"}

Structure beyond symmetry saves more. A *banded* matrix with bandwidth $p$ (zero when $\lvert i-j\rvert>p$) has LU and Cholesky factors with the same band, computed in $O(mp^2)$ flops; for a tridiagonal matrix this is $O(m)$ (the "Thomas algorithm"). Symmetric *indefinite* matrices use $A=PLDL^{\mathsf H}P^{\mathsf T}$ with $1\times1$ and $2\times2$ diagonal blocks and symmetric pivoting (Bunch–Kaufman), at the Cholesky cost. Testing whether a Hermitian matrix is positive definite is best done by attempting Cholesky: it fails exactly when a pivot $a_{kk}-\sum\lvert r_{ik}\rvert^2$ is not positive.

:::

::: {#fig-cholesky-factorization-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.04,0.05) -- (-0.10,0.05) -- (-0.10,-2.09) -- (-0.04,-2.09);
\draw[faint] (2.08,0.05) -- (2.14,0.05) -- (2.14,-2.09) -- (2.08,-2.09);
\node[tick] at (0.17,-0.17) {$\times$};
\node[tick] at (0.51,-0.17) {$\times$};
\node[tick] at (0.17,-0.51) {$\times$};
\node[tick] at (0.51,-0.51) {$\times$};
\node[tick] at (0.85,-0.51) {$\times$};
\node[tick] at (0.51,-0.85) {$\times$};
\node[tick] at (0.85,-0.85) {$\times$};
\node[tick] at (1.19,-0.85) {$\times$};
\node[tick] at (0.85,-1.19) {$\times$};
\node[tick] at (1.19,-1.19) {$\times$};
\node[tick] at (1.53,-1.19) {$\times$};
\node[tick] at (1.19,-1.53) {$\times$};
\node[tick] at (1.53,-1.53) {$\times$};
\node[tick] at (1.87,-1.53) {$\times$};
\node[tick] at (1.53,-1.87) {$\times$};
\node[tick] at (1.87,-1.87) {$\times$};
\node[note] at (1.02,-2.39) {$A$ (tridiagonal)};
\draw[map] (2.19,-1.02) -- (2.64,-1.02);
\draw[faint] (2.75,0.05) -- (2.69,0.05) -- (2.69,-2.09) -- (2.75,-2.09);
\draw[faint] (4.87,0.05) -- (4.93,0.05) -- (4.93,-2.09) -- (4.87,-2.09);
\fill[accentLight] (2.81,-0.32) rectangle (3.11,-0.02);
\node[tick] at (2.96,-0.17) {$\times$};
\fill[accentLight] (3.15,-0.32) rectangle (3.45,-0.02);
\node[tick] at (3.30,-0.17) {$\times$};
\fill[accentLight] (3.15,-0.66) rectangle (3.45,-0.36);
\node[tick] at (3.30,-0.51) {$\times$};
\fill[accentLight] (3.49,-0.66) rectangle (3.79,-0.36);
\node[tick] at (3.64,-0.51) {$\times$};
\fill[accentLight] (3.49,-1.00) rectangle (3.79,-0.70);
\node[tick] at (3.64,-0.85) {$\times$};
\fill[accentLight] (3.83,-1.00) rectangle (4.13,-0.70);
\node[tick] at (3.98,-0.85) {$\times$};
\fill[accentLight] (3.83,-1.34) rectangle (4.13,-1.04);
\node[tick] at (3.98,-1.19) {$\times$};
\fill[accentLight] (4.17,-1.34) rectangle (4.47,-1.04);
\node[tick] at (4.32,-1.19) {$\times$};
\fill[accentLight] (4.17,-1.68) rectangle (4.47,-1.38);
\node[tick] at (4.32,-1.53) {$\times$};
\fill[accentLight] (4.51,-1.68) rectangle (4.81,-1.38);
\node[tick] at (4.66,-1.53) {$\times$};
\fill[accentLight] (4.51,-2.02) rectangle (4.81,-1.72);
\node[tick] at (4.66,-1.87) {$\times$};
\node[note] at (3.81,-2.39) {$R$ (bidiagonal)};
\end{tikzpicture}
\end{center}
```

A tridiagonal positive definite matrix and its Cholesky factor: $R$ is upper bidiagonal, with no fill outside the band, so the factorization costs $O(m)$ flops and storage.

:::
