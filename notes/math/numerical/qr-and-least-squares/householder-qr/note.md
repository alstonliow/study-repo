---
title: "Householder QR and Givens Rotations"
sources: [mit18335-10]
requires: [math/numerical/floating-point/stability-and-backward-error]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 10 (modified Gram–Schmidt and Householder QR; slides on Householder reflectors and Givens rotations), in our own wording; proofs written out in steps, numbers checked with numpy. -->

Gram–Schmidt makes the columns of $A$ orthonormal by multiplying by triangular matrices on the right: *triangular orthogonalization*. Householder's method does the opposite, *orthogonal triangularization*: it multiplies $A$ on the left by orthogonal matrices until it is upper triangular. Because orthogonal matrices preserve norms, every step is perfectly conditioned, and the result is backward stable.

::: {#thm-full-qr-existence .theorem name="Existence and uniqueness of the QR factorization" generalizes="thm-qr-factorization"}

Every $m\times n$ matrix $A$ with $m\ge n$ (real or complex) has a *full QR factorization* $A=QR$ with $Q$ an $m\times m$ unitary matrix and $R$ an $m\times n$ upper triangular matrix (zero below the diagonal). Keeping the first $n$ columns of $Q$ and the first $n$ rows of $R$ gives the *reduced QR factorization* $A=\hat Q\hat R$ with $\hat Q$ of size $m\times n$ with orthonormal columns and $\hat R$ square upper triangular. If $A$ has full rank $n$, the reduced factorization with all $r_{jj}>0$ is unique.

:::

::: {.proof}

1. *Existence.* The Householder algorithm below produces unitary $Q_1,\dots,Q_n$ with $Q_n\cdots Q_1A=R$ upper triangular, for any $A$; it never divides by zero, because a column that is already zero below the diagonal is left alone. Set $Q=Q_1^{\mathsf H}\cdots Q_n^{\mathsf H}$.

2. *Reduced form.* Rows $n+1,\dots,m$ of $R$ are zero, so they multiply only the last $m-n$ columns of $Q$, which can be dropped.

3. *Uniqueness.* If $A=\hat Q\hat R$ has full rank, $\hat R$ is invertible and $A^{\mathsf H}A=\hat R^{\mathsf H}\hat R$. This is a Cholesky factorization of the positive definite matrix $A^{\mathsf H}A$, which is unique once the diagonal is positive (@thm-cholesky-existence); then $\hat Q=A\hat R^{-1}$ is determined too.

:::

::: {#def-householder-reflector .definition name="Householder reflector"}

For a nonzero $\mathbf{v}\in\mathbb{C}^m$ the *Householder reflector* is
$$F=I-2\,\frac{\mathbf{v}\mathbf{v}^{\mathsf H}}{\mathbf{v}^{\mathsf H}\mathbf{v}}.$$
It is Hermitian, unitary and its own inverse, and it reflects $\mathbb{C}^m$ across the hyperplane $\mathbf{v}^{\perp}$: $F\mathbf{v}=-\mathbf{v}$ and $F\mathbf{w}=\mathbf{w}$ for $\mathbf{w}\perp\mathbf{v}$. To map a given $\mathbf{x}$ to a multiple of $\mathbf{e}_1$ one takes
$$\mathbf{v}=\mathbf{x}+\operatorname{sign}(x_1)\lVert\mathbf{x}\rVert\,\mathbf{e}_1,\qquad F\mathbf{x}=-\operatorname{sign}(x_1)\lVert\mathbf{x}\rVert\,\mathbf{e}_1,$$
with $\operatorname{sign}(x_1)=x_1/\lvert x_1\rvert$ (and $1$ if $x_1=0$).

:::

::: {#prp-householder-maps-x .proposition name="The reflector maps x onto the axis"}

With $\mathbf{v}$ as in @def-householder-reflector, $F\mathbf{x}=-\operatorname{sign}(x_1)\lVert\mathbf{x}\rVert\mathbf{e}_1$, and $\lVert\mathbf{v}\rVert\ge\lVert\mathbf{x}\rVert$.

:::

::: {.proof}

1. Write $s=\operatorname{sign}(x_1)$ and $\alpha=\lVert\mathbf{x}\rVert$, so $\mathbf{v}=\mathbf{x}+s\alpha\mathbf{e}_1$ and $\mathbf{x}-(-s\alpha\mathbf{e}_1)=\mathbf{v}$.

2. $\mathbf{x}$ and $-s\alpha\mathbf{e}_1$ have the same length, so their difference $\mathbf{v}$ is perpendicular to their sum $\mathbf{x}-s\alpha\mathbf{e}_1$ (expand the inner product; the cross terms are real because $\bar s x_1=\lvert x_1\rvert$).

3. Hence $\mathbf{x}=\tfrac12\mathbf{v}+\tfrac12(\mathbf{x}-s\alpha\mathbf{e}_1)$ splits into a part along $\mathbf{v}$ and a part orthogonal to it, and $F\mathbf{x}=-\tfrac12\mathbf{v}+\tfrac12(\mathbf{x}-s\alpha\mathbf{e}_1)=-s\alpha\mathbf{e}_1$.

4. $\lvert v_1\rvert=\lvert x_1\rvert+\alpha\ge\alpha$, so $\lVert\mathbf{v}\rVert\ge\alpha$. This is the reason for the sign: the other choice $\mathbf{x}-s\alpha\mathbf{e}_1$ has first entry $s(\lvert x_1\rvert-\alpha)$, which suffers cancellation when $\mathbf{x}$ is nearly parallel to $\mathbf{e}_1$.

:::

::: {#fig-householder-qr-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.8]
\draw[->, faint] (-6,0) -- (5.6,0) node[lab, right] {$\mathbf{e}_1$};
\draw[->, faint] (0,-1.2) -- (0,4.6);
\draw[emph, ->] (0,0) -- (3,4) node[lab, above right] {$\mathbf{x}=(3,4)$};
\draw[hl, ->] (0,0) -- (-5,0) node[lab, below] {$F\mathbf{x}=(-5,0)$};
\draw[faint, ->] (0,0) -- (5,0) node[lab, below] {$(5,0)$};
\draw[->, emph] (0,0) -- (1.6,0.8) node[lab, below right] {$\mathbf{v}=(8,4)/5$};
\draw[faint, dashed] (-1.1,2.2) -- (1.1,-2.2) node[lab, below] {$\mathbf{v}^{\perp}$};
\draw[faint, dotted] (3,4) -- (-5,0);
\end{tikzpicture}
\end{center}
```

The reflector for $\mathbf{x}=(3,4)$: $\mathbf{v}=\mathbf{x}+5\mathbf{e}_1=(8,4)$ (drawn shortened), and $F$ reflects across the line $\mathbf{v}^{\perp}$ (dashed through the origin), sending $\mathbf{x}$ to $(-5,0)$. The segment from $\mathbf{x}$ to $F\mathbf{x}$ (dotted) is parallel to $\mathbf{v}$. Reflecting to $(+5,0)$ instead would use $\mathbf{v}=(-2,4)$, shorter and prone to cancellation.

:::

::: {#def-householder-qr .definition name="Householder QR factorization"}

For $k=1,\dots,n$: let $\mathbf{x}$ be the part of column $k$ of the current matrix from row $k$ down, form $\mathbf{v}_k$ from $\mathbf{x}$ as in @def-householder-reflector and normalise it, and apply the reflector $I-2\mathbf{v}_k\mathbf{v}_k^{\mathsf H}$ to rows $k,\dots,m$ of columns $k,\dots,n$. Step $k$ is multiplication by $Q_k=\begin{bmatrix}I_{k-1}&0\\0&F_k\end{bmatrix}$, which zeros column $k$ below the diagonal without disturbing the zeros already made. The result is $R=Q_n\cdots Q_1A$. The matrix $Q$ is not formed: the vectors $\mathbf{v}_k$ are stored (they fit below the diagonal of $R$), and $Q^{\mathsf H}\mathbf{b}$ or $Q\mathbf{x}$ is computed by applying the reflectors in turn.

:::

```{=latex}
\begin{algorithm}
\caption{Householder QR}
\begin{algorithmic}
\INPUT $A\in\mathbb{C}^{m\times n}$, $m\ge n$; overwritten by $R$
\FOR{$k=1,\dots,n$}
    \STATE $\mathbf{x}\gets A_{k:m,\,k}$
    \STATE $\mathbf{v}_k\gets\mathbf{x}+\operatorname{sign}(x_1)\lVert\mathbf{x}\rVert\mathbf{e}_1$; \quad $\mathbf{v}_k\gets\mathbf{v}_k/\lVert\mathbf{v}_k\rVert$
    \STATE $A_{k:m,\,k:n}\gets A_{k:m,\,k:n}-2\mathbf{v}_k\bigl(\mathbf{v}_k^{\mathsf H}A_{k:m,\,k:n}\bigr)$
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

::: {#fig-householder-qr-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.04,0.05) -- (-0.10,0.05) -- (-0.10,-1.75) -- (-0.04,-1.75);
\draw[faint] (1.06,0.05) -- (1.12,0.05) -- (1.12,-1.75) -- (1.06,-1.75);
\node[tick] at (0.17,-0.17) {$\times$};
\node[tick] at (0.51,-0.17) {$\times$};
\node[tick] at (0.85,-0.17) {$\times$};
\node[tick] at (0.17,-0.51) {$\times$};
\node[tick] at (0.51,-0.51) {$\times$};
\node[tick] at (0.85,-0.51) {$\times$};
\node[tick] at (0.17,-0.85) {$\times$};
\node[tick] at (0.51,-0.85) {$\times$};
\node[tick] at (0.85,-0.85) {$\times$};
\node[tick] at (0.17,-1.19) {$\times$};
\node[tick] at (0.51,-1.19) {$\times$};
\node[tick] at (0.85,-1.19) {$\times$};
\node[tick] at (0.17,-1.53) {$\times$};
\node[tick] at (0.51,-1.53) {$\times$};
\node[tick] at (0.85,-1.53) {$\times$};
\node[note] at (0.51,-2.05) {$A$};
\draw[map] (1.17,-0.85) -- (1.62,-0.85);
\draw[faint] (1.73,0.05) -- (1.67,0.05) -- (1.67,-1.75) -- (1.73,-1.75);
\draw[faint] (2.83,0.05) -- (2.89,0.05) -- (2.89,-1.75) -- (2.83,-1.75);
\fill[accentLight] (1.79,-0.32) rectangle (2.09,-0.02);
\node[tick] at (1.94,-0.17) {$\times$};
\fill[accentLight] (2.13,-0.32) rectangle (2.43,-0.02);
\node[tick] at (2.28,-0.17) {$\times$};
\fill[accentLight] (2.47,-0.32) rectangle (2.77,-0.02);
\node[tick] at (2.62,-0.17) {$\times$};
\node[tick, text=rule] at (1.94,-0.51) {$0$};
\fill[accentLight] (2.13,-0.66) rectangle (2.43,-0.36);
\node[tick] at (2.28,-0.51) {$\times$};
\fill[accentLight] (2.47,-0.66) rectangle (2.77,-0.36);
\node[tick] at (2.62,-0.51) {$\times$};
\node[tick, text=rule] at (1.94,-0.85) {$0$};
\fill[accentLight] (2.13,-1.00) rectangle (2.43,-0.70);
\node[tick] at (2.28,-0.85) {$\times$};
\fill[accentLight] (2.47,-1.00) rectangle (2.77,-0.70);
\node[tick] at (2.62,-0.85) {$\times$};
\node[tick, text=rule] at (1.94,-1.19) {$0$};
\fill[accentLight] (2.13,-1.34) rectangle (2.43,-1.04);
\node[tick] at (2.28,-1.19) {$\times$};
\fill[accentLight] (2.47,-1.34) rectangle (2.77,-1.04);
\node[tick] at (2.62,-1.19) {$\times$};
\node[tick, text=rule] at (1.94,-1.53) {$0$};
\fill[accentLight] (2.13,-1.68) rectangle (2.43,-1.38);
\node[tick] at (2.28,-1.53) {$\times$};
\fill[accentLight] (2.47,-1.68) rectangle (2.77,-1.38);
\node[tick] at (2.62,-1.53) {$\times$};
\node[note] at (2.28,-2.05) {$Q_1A$};
\draw[map] (2.94,-0.85) -- (3.39,-0.85);
\draw[faint] (3.50,0.05) -- (3.44,0.05) -- (3.44,-1.75) -- (3.50,-1.75);
\draw[faint] (4.60,0.05) -- (4.66,0.05) -- (4.66,-1.75) -- (4.60,-1.75);
\node[tick] at (3.71,-0.17) {$\times$};
\node[tick] at (4.05,-0.17) {$\times$};
\node[tick] at (4.39,-0.17) {$\times$};
\node[tick, text=rule] at (3.71,-0.51) {$0$};
\fill[accentLight] (3.90,-0.66) rectangle (4.20,-0.36);
\node[tick] at (4.05,-0.51) {$\times$};
\fill[accentLight] (4.24,-0.66) rectangle (4.54,-0.36);
\node[tick] at (4.39,-0.51) {$\times$};
\node[tick, text=rule] at (3.71,-0.85) {$0$};
\node[tick, text=rule] at (4.05,-0.85) {$0$};
\fill[accentLight] (4.24,-1.00) rectangle (4.54,-0.70);
\node[tick] at (4.39,-0.85) {$\times$};
\node[tick, text=rule] at (3.71,-1.19) {$0$};
\node[tick, text=rule] at (4.05,-1.19) {$0$};
\fill[accentLight] (4.24,-1.34) rectangle (4.54,-1.04);
\node[tick] at (4.39,-1.19) {$\times$};
\node[tick, text=rule] at (3.71,-1.53) {$0$};
\node[tick, text=rule] at (4.05,-1.53) {$0$};
\fill[accentLight] (4.24,-1.68) rectangle (4.54,-1.38);
\node[tick] at (4.39,-1.53) {$\times$};
\node[note] at (4.05,-2.05) {$Q_2Q_1A$};
\draw[map] (4.71,-0.85) -- (5.16,-0.85);
\draw[faint] (5.27,0.05) -- (5.21,0.05) -- (5.21,-1.75) -- (5.27,-1.75);
\draw[faint] (6.37,0.05) -- (6.43,0.05) -- (6.43,-1.75) -- (6.37,-1.75);
\node[tick] at (5.48,-0.17) {$\times$};
\node[tick] at (5.82,-0.17) {$\times$};
\node[tick] at (6.16,-0.17) {$\times$};
\node[tick, text=rule] at (5.48,-0.51) {$0$};
\node[tick] at (5.82,-0.51) {$\times$};
\node[tick] at (6.16,-0.51) {$\times$};
\node[tick, text=rule] at (5.48,-0.85) {$0$};
\node[tick, text=rule] at (5.82,-0.85) {$0$};
\fill[accentLight] (6.01,-1.00) rectangle (6.31,-0.70);
\node[tick] at (6.16,-0.85) {$\times$};
\node[tick, text=rule] at (5.48,-1.19) {$0$};
\node[tick, text=rule] at (5.82,-1.19) {$0$};
\node[tick, text=rule] at (6.16,-1.19) {$0$};
\node[tick, text=rule] at (5.48,-1.53) {$0$};
\node[tick, text=rule] at (5.82,-1.53) {$0$};
\node[tick, text=rule] at (6.16,-1.53) {$0$};
\node[note] at (5.82,-2.05) {$R$};
\end{tikzpicture}
\end{center}
```

Householder QR on a $5\times3$ matrix. Each $Q_k$ acts on rows $k,\dots,5$ only; the entries it changes are shaded. After three reflections the matrix is $R$.

:::

::: {#thm-householder-qr-cost .theorem name="Work for Householder QR"}

Householder QR of an $m\times n$ matrix takes $\sim2mn^2-\tfrac23n^3$ flops. Applying $Q^{\mathsf H}$ or $Q$ to a vector takes $\sim4mn-2n^2$ flops, and forming $\hat Q$ explicitly costs another $\sim2mn^2-\tfrac23n^3$.

:::

::: {.proof}

1. At step $k$ the active block has $\ell=m-k+1$ rows and $n-k+1$ columns. The update $\mathbf{v}^{\mathsf H}B$ and then $B-2\mathbf{v}(\mathbf{v}^{\mathsf H}B)$ costs about $2\ell$ flops plus $2\ell$ flops per column, $4\ell(n-k+1)$ in all; forming $\mathbf{v}$ costs only $O(\ell)$.

2. Summing, $\sum_{k=1}^n4(m-k)(n-k)\approx4\int_0^n(m-t)(n-t)\,dt=4\bigl(mn^2-\tfrac12(m+n)n^2+\tfrac13n^3\bigr)=2mn^2-\tfrac23n^3$.

3. Applying the $n$ reflectors to a vector costs $\sum_k4(m-k+1)\approx4mn-2n^2$ flops. Forming $\hat Q$ means applying them to the $n$ columns of $\bigl[\begin{smallmatrix}I\\0\end{smallmatrix}\bigr]$, exploiting the zeros, at the cost stated.

:::

::: {#thm-householder-qr-backward-stable .theorem name="Householder QR is backward stable"}

The computed $\tilde R$ and the exactly unitary $\tilde Q$ defined by the computed vectors $\tilde{\mathbf{v}}_k$ satisfy
$$\tilde Q\tilde R=A+\delta A,\qquad \frac{\lVert\delta A\rVert}{\lVert A\rVert}=O(\varepsilon_{\text{mach}}).$$

:::

::: {.proof}

1. *One reflection.* Applying a reflector computed in floating point to a vector $\mathbf{y}$ gives $F(\mathbf{y}+\delta\mathbf{y})$ for the exact reflector $F$ of the computed $\tilde{\mathbf{v}}$, with $\lVert\delta\mathbf{y}\rVert=O(\varepsilon_{\text{mach}})\lVert\mathbf{y}\rVert$: the inner product $\tilde{\mathbf{v}}^{\mathsf H}\mathbf{y}$ and the update are backward stable (@prp-arithmetic-backward-stable), and $\lVert\tilde{\mathbf{v}}\rVert\approx1$.

2. *Errors do not grow.* After step $k$ the computed matrix is $Q_k(A_{k-1}+E_k)$ with $\lVert E_k\rVert=O(\varepsilon_{\text{mach}})\lVert A_{k-1}\rVert$. Unitary $Q_k$ preserve norms, so $\lVert A_k\rVert=\lVert A\rVert(1+O(\varepsilon_{\text{mach}}))$ for every $k$.

3. *Push all errors back.* Unwinding, $\tilde R=Q_n\cdots Q_1(A+E_1+Q_1^{\mathsf H}E_2+\dots)$, and each term $Q_1^{\mathsf H}\cdots Q_{k-1}^{\mathsf H}E_k$ has norm $O(\varepsilon_{\text{mach}})\lVert A\rVert$. Setting $\delta A$ to their sum (there are $n$ of them, a dimension-dependent constant) gives $\tilde Q\tilde R=A+\delta A$.

4. The entries of $\tilde R$ below the diagonal are set to zero rather than computed, which is a further perturbation of size $O(\varepsilon_{\text{mach}})\lVert A\rVert$ absorbed in $\delta A$.

:::

::: {#exm-householder-two-by-two .example name="A 2 by 2 example"}

For $A=\begin{bmatrix}3&1\\4&2\end{bmatrix}$ the first column is $\mathbf{x}=(3,4)$ with $\lVert\mathbf{x}\rVert=5$, so $\mathbf{v}=(8,4)$ and
$$F=I-\frac{2}{80}\begin{bmatrix}64&32\\32&16\end{bmatrix}=\begin{bmatrix}-0.6&-0.8\\-0.8&0.6\end{bmatrix},\qquad FA=\begin{bmatrix}-5&-2.2\\0&0.4\end{bmatrix}.$$
So $A=QR$ with $Q=F$ and $R=FA$. Gram–Schmidt would give the same factorization with the signs of the first row of $R$ and the first column of $Q$ flipped (positive diagonal); by uniqueness these are the only two choices of sign for the first column.

:::

::: {#def-givens-rotation .definition name="Givens rotation"}

A *Givens rotation* $G(i,j,\theta)$ is the identity except in rows and columns $i,j$, where it is the plane rotation $\begin{bmatrix}c&s\\-s&c\end{bmatrix}$ with $c=\cos\theta$, $s=\sin\theta$. Given $a=x_i$, $b=x_j$ (real), the choice $c=a/r$, $s=b/r$, $r=\sqrt{a^2+b^2}$ makes $(G\mathbf{x})_i=r$ and $(G\mathbf{x})_j=0$, changing no other entry. QR by Givens rotations zeros the subdiagonal one entry at a time; for a dense matrix this costs about $3mn^2-n^3$ flops, $50\%$ more than Householder, but it is the method of choice when only a few entries need zeroing, as for Hessenberg and banded matrices (@sec-math-numerical-eigenvalue-algorithms-shifted-qr-algorithm) and for updating a factorization after a row is added.

:::

::: {#fig-householder-qr-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.04,0.05) -- (-0.10,0.05) -- (-0.10,-1.41) -- (-0.04,-1.41);
\draw[faint] (1.06,0.05) -- (1.12,0.05) -- (1.12,-1.41) -- (1.06,-1.41);
\node[tick] at (0.17,-0.17) {$\times$};
\node[tick] at (0.51,-0.17) {$\times$};
\node[tick] at (0.85,-0.17) {$\times$};
\node[tick] at (0.17,-0.51) {$\times$};
\node[tick] at (0.51,-0.51) {$\times$};
\node[tick] at (0.85,-0.51) {$\times$};
\node[tick] at (0.51,-0.85) {$\times$};
\node[tick] at (0.85,-0.85) {$\times$};
\node[tick] at (0.85,-1.19) {$\times$};
\node[note] at (0.51,-1.71) {$A$};
\draw[map] (1.17,-0.68) -- (1.62,-0.68);
\draw[faint] (1.73,0.05) -- (1.67,0.05) -- (1.67,-1.41) -- (1.73,-1.41);
\draw[faint] (2.83,0.05) -- (2.89,0.05) -- (2.89,-1.41) -- (2.83,-1.41);
\fill[accentLight] (1.79,-0.32) rectangle (2.09,-0.02);
\node[tick] at (1.94,-0.17) {$\times$};
\fill[accentLight] (2.13,-0.32) rectangle (2.43,-0.02);
\node[tick] at (2.28,-0.17) {$\times$};
\fill[accentLight] (2.47,-0.32) rectangle (2.77,-0.02);
\node[tick] at (2.62,-0.17) {$\times$};
\node[tick, text=rule] at (1.94,-0.51) {$0$};
\fill[accentLight] (2.13,-0.66) rectangle (2.43,-0.36);
\node[tick] at (2.28,-0.51) {$\times$};
\fill[accentLight] (2.47,-0.66) rectangle (2.77,-0.36);
\node[tick] at (2.62,-0.51) {$\times$};
\node[tick] at (2.28,-0.85) {$\times$};
\node[tick] at (2.62,-0.85) {$\times$};
\node[tick] at (2.62,-1.19) {$\times$};
\node[note] at (2.28,-1.71) {$G_1A$};
\draw[map] (2.94,-0.68) -- (3.39,-0.68);
\draw[faint] (3.50,0.05) -- (3.44,0.05) -- (3.44,-1.41) -- (3.50,-1.41);
\draw[faint] (4.60,0.05) -- (4.66,0.05) -- (4.66,-1.41) -- (4.60,-1.41);
\node[tick] at (3.71,-0.17) {$\times$};
\node[tick] at (4.05,-0.17) {$\times$};
\node[tick] at (4.39,-0.17) {$\times$};
\node[tick, text=rule] at (3.71,-0.51) {$0$};
\fill[accentLight] (3.90,-0.66) rectangle (4.20,-0.36);
\node[tick] at (4.05,-0.51) {$\times$};
\fill[accentLight] (4.24,-0.66) rectangle (4.54,-0.36);
\node[tick] at (4.39,-0.51) {$\times$};
\node[tick, text=rule] at (4.05,-0.85) {$0$};
\fill[accentLight] (4.24,-1.00) rectangle (4.54,-0.70);
\node[tick] at (4.39,-0.85) {$\times$};
\node[tick] at (4.39,-1.19) {$\times$};
\node[note] at (4.05,-1.71) {$G_2G_1A$};
\draw[map] (4.71,-0.68) -- (5.16,-0.68);
\draw[faint] (5.27,0.05) -- (5.21,0.05) -- (5.21,-1.41) -- (5.27,-1.41);
\draw[faint] (6.37,0.05) -- (6.43,0.05) -- (6.43,-1.41) -- (6.37,-1.41);
\node[tick] at (5.48,-0.17) {$\times$};
\node[tick] at (5.82,-0.17) {$\times$};
\node[tick] at (6.16,-0.17) {$\times$};
\node[tick, text=rule] at (5.48,-0.51) {$0$};
\node[tick] at (5.82,-0.51) {$\times$};
\node[tick] at (6.16,-0.51) {$\times$};
\node[tick, text=rule] at (5.82,-0.85) {$0$};
\fill[accentLight] (6.01,-1.00) rectangle (6.31,-0.70);
\node[tick] at (6.16,-0.85) {$\times$};
\node[tick, text=rule] at (6.16,-1.19) {$0$};
\node[note] at (5.82,-1.71) {$R$};
\end{tikzpicture}
\end{center}
```

Givens QR of a $4\times3$ upper Hessenberg-like matrix: each rotation acts on two adjacent rows (shaded) and zeros one subdiagonal entry, so three rotations suffice instead of full reflections.

:::
