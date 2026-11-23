---
title: "The Shifted QR Algorithm"
sources: [mit18335-17]
requires: [math/numerical/eigenvalue-algorithms/qr-algorithm]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 17 (shifted QR and Rayleigh quotients) and the reading on the QR algorithm II, in our own wording; proofs written out in steps; the iteration on the 4 by 4 example was run with numpy. -->

The unshifted QR algorithm converges linearly at rates $\lvert\lambda_{j+1}/\lambda_j\rvert$, which can be arbitrarily close to $1$. Shifting by an eigenvalue estimate turns the hidden inverse iteration in the last column into Rayleigh quotient iteration, and convergence becomes cubic. With deflation and a reduction to tridiagonal or Hessenberg form first, this is the practical algorithm in every numerical library.

::: {#def-shifted-qr-algorithm .definition name="The QR algorithm with shifts and deflation"}

Reduce $A$ to Hessenberg form (tridiagonal if $A$ is symmetric), $A^{(0)}=Q_0^{\mathsf H}AQ_0$ (@def-hessenberg-reduction). For $k=1,2,\dots$:

1. choose a shift $\mu^{(k)}$;

2. factor $A^{(k-1)}-\mu^{(k)}I=Q^{(k)}R^{(k)}$ and set $A^{(k)}=R^{(k)}Q^{(k)}+\mu^{(k)}I$;

3. if some subdiagonal entry is negligible, $\lvert a^{(k)}_{j+1,j}\rvert\le\varepsilon_{\text{mach}}\bigl(\lvert a^{(k)}_{jj}\rvert+\lvert a^{(k)}_{j+1,j+1}\rvert\bigr)$, set it to zero and continue separately on the two diagonal blocks (*deflation*). A $1\times1$ block is an eigenvalue.

:::

```{=latex}
\begin{algorithm}
\caption{Shifted QR algorithm for a symmetric tridiagonal matrix}
\begin{algorithmic}
\INPUT symmetric tridiagonal $T\in\mathbb{R}^{m\times m}$
\WHILE{$m>1$}
    \STATE $\mu\gets$ Wilkinson shift of the trailing $2\times2$ block of $T_{1:m,1:m}$
    \STATE $QR\gets T_{1:m,1:m}-\mu I$ \COMMENT{$m-1$ Givens rotations}
    \STATE $T_{1:m,1:m}\gets RQ+\mu I$
    \IF{$\lvert t_{m,m-1}\rvert$ is negligible}
        \STATE record the eigenvalue $t_{mm}$; set $t_{m,m-1}=t_{m-1,m}=0$; $m\gets m-1$
    \ENDIF
\ENDWHILE
\STATE record $t_{11}$
\end{algorithmic}
\end{algorithm}
```

::: {#prp-shifted-qr-similarity .proposition name="A shifted step is a similarity"}

$A^{(k)}=(Q^{(k)})^{\mathsf H}A^{(k-1)}Q^{(k)}$, and $\prod_{j\le k}\bigl(A-\mu^{(j)}I\bigr)=\underline Q^{(k)}\underline R^{(k)}$ with $\underline Q^{(k)}=Q_0Q^{(1)}\cdots Q^{(k)}$ (taking $A$ already Hessenberg, $Q_0=I$) and $\underline R^{(k)}=R^{(k)}\cdots R^{(1)}$.

:::

::: {.proof}

1. $R^{(k)}=(Q^{(k)})^{\mathsf H}(A^{(k-1)}-\mu^{(k)}I)$, so $A^{(k)}=(Q^{(k)})^{\mathsf H}(A^{(k-1)}-\mu^{(k)}I)Q^{(k)}+\mu^{(k)}I=(Q^{(k)})^{\mathsf H}A^{(k-1)}Q^{(k)}$.

2. The product formula follows by the induction of @thm-qr-algorithm-simultaneous-iteration, with $A$ replaced at step $j$ by $A-\mu^{(j)}I$; these factors commute, and $A\,\underline Q^{(k-1)}=\underline Q^{(k-1)}A^{(k-1)}$ as before.

:::

Inverting as in the last remark of @sec-math-numerical-eigenvalue-algorithms-qr-algorithm, the last column of $\underline Q^{(k)}$ is the result of inverse iteration with the shifts $\mu^{(1)},\dots,\mu^{(k)}$ applied to $\mathbf{e}_m$. The natural shift is therefore the Rayleigh quotient of that column, which is just an entry of the current matrix.

::: {#def-qr-shifts .definition name="Rayleigh quotient and Wilkinson shifts"}

1. The *Rayleigh quotient shift* is $\mu^{(k)}=a^{(k-1)}_{mm}$. Since $a^{(k-1)}_{mm}=(\underline{\mathbf{q}}_m^{(k-1)})^{\mathsf T}A\,\underline{\mathbf{q}}_m^{(k-1)}=r(\underline{\mathbf{q}}_m^{(k-1)})$, the last column then undergoes Rayleigh quotient iteration (@def-rayleigh-quotient-iteration).

2. The *Wilkinson shift* is the eigenvalue of the trailing $2\times2$ block $\begin{bmatrix}a&b\\b&c\end{bmatrix}$ that is closer to $c=a_{mm}$:
$$\mu=c-\frac{\operatorname{sign}(\delta)\,b^2}{\lvert\delta\rvert+\sqrt{\delta^2+b^2}},\qquad\delta=\frac{a-c}{2}$$
(with $\operatorname{sign}(0)=1$; the form avoids cancellation).

:::

::: {#thm-shifted-qr-convergence .theorem name="Convergence with shifts"}

For a real symmetric tridiagonal matrix:

1. with Rayleigh quotient shifts, whenever $a^{(k)}_{m,m-1}\to0$ it does so cubically, $\lvert a^{(k+1)}_{m,m-1}\rvert=O(\lvert a^{(k)}_{m,m-1}\rvert^3)$;

2. Rayleigh quotient shifts can fail to converge at all;

3. with Wilkinson shifts the iteration always converges, and in practice cubically, so that about two or three steps per eigenvalue suffice.

:::

::: {.proof}

1. By @prp-shifted-qr-similarity and the remark after it, the last column $\underline{\mathbf{q}}_m^{(k)}$ is produced by Rayleigh quotient iteration, so by @thm-rqi-cubic its distance $\epsilon_k$ to an eigenvector satisfies $\epsilon_{k+1}=O(\epsilon_k^3)$.

2. The last row of $A^{(k)}=(\underline Q^{(k)})^{\mathsf T}A\underline Q^{(k)}$ is $(\underline{\mathbf{q}}_m^{(k)})^{\mathsf T}A\underline Q^{(k)}$, and its off-diagonal part has norm $\lVert A\underline{\mathbf{q}}_m^{(k)}-r\,\underline{\mathbf{q}}_m^{(k)}\rVert=O(\epsilon_k)$, the residual of the approximate eigenvector. In the tridiagonal case that part is just $a^{(k)}_{m,m-1}$, so $\lvert a^{(k)}_{m,m-1}\rvert$ is proportional to $\epsilon_k$ and inherits the cubic rate.

3. *Failure.* For $A=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ the Rayleigh quotient shift is $a_{22}=0$; then $A=QR$ with $Q=A$, $R=I$, and $RQ=A$: the iteration stands still. The eigenvalues $\pm1$ are equally close to the shift, so inverse iteration cannot prefer either. The Wilkinson shift is $\pm1$, an exact eigenvalue, and one step deflates.

4. The global convergence of the Wilkinson-shift iteration for symmetric tridiagonal matrices is a theorem of Wilkinson (the off-diagonal entry $\lvert a_{m,m-1}\rvert$ decreases at least linearly, and once it is small the shift is close to the Rayleigh quotient, giving the asymptotic rate of part 1); we do not reproduce its proof.

:::

::: {#exm-shifted-qr-four-by-four .example name="Shifts on the 4 by 4 example"}

Apply the algorithm with Wilkinson shifts to the tridiagonal matrix of @exm-qr-algorithm-four-by-four. The trailing subdiagonal entry is $0.11$, $3.1\times10^{-5}$, $3.0\times10^{-16}$ after steps $1$–$3$, so $\lambda=0.2547$ deflates after three steps. On the remaining $3\times3$ block the new trailing entry is $9.0\times10^{-5}$ and then $1.9\times10^{-15}$, deflating $1.8227$; one more step on the $2\times2$ block finishes. Six QR steps give all four eigenvalues to full precision; the unshifted algorithm needs about $90$ steps to bring its first subdiagonal entry down to $10^{-16}$.

:::

::: {#fig-shifted-qr-algorithm-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.1cm, y=0.22cm]
\draw[->, faint] (0,0) -- (6.6,0) node[lab, right] {QR step};
\draw[->, faint] (0,0) -- (0,-19.5) node[lab, below] {$\log_{10}\lvert$trailing subdiagonal$\rvert$};
\foreach \x in {1,...,6} {\draw[faint] (\x,-0.3) -- (\x,0.3); \node[tick, above] at (\x,0.3) {$\x$};}
\foreach \y in {-5,-10,-15} {\draw[faint] (-0.05,\y) -- (0.05,\y); \node[tick, left] at (-0.05,\y) {$\y$};}
\draw[faint, dashed] (0,-15.65) -- (6.4,-15.65) node[lab, right] {$\varepsilon_{\text{mach}}$};
\draw[hl] plot coordinates {(1,-0.96) (2,-4.51) (3,-15.52)};
\draw[emph] plot coordinates {(4,-4.05) (5,-14.72)};
\foreach \p in {(1,-0.96),(2,-4.51),(3,-15.52)} {\fill[accent] \p circle (2.4pt);}
\foreach \p in {(4,-4.05),(5,-14.72),(6,-18.06)} {\fill \p circle (2.4pt);}
\node[note] at (2.2,-17.6) {deflate $0.2547$};
\node[note] at (4.6,-17.0) {deflate $1.8227$};
\end{tikzpicture}
\end{center}
```

The trailing subdiagonal entry of the active block in @exm-shifted-qr-four-by-four. Each drop is cubic (the exponent roughly triples), and whenever it falls below $\varepsilon_{\text{mach}}$ the last eigenvalue deflates and the iteration restarts on a smaller block. The last point is the $2\times2$ block, finished in one step.

:::

::: {#fig-shifted-qr-algorithm-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.04,0.05) -- (-0.10,0.05) -- (-0.10,-1.75) -- (-0.04,-1.75);
\draw[faint] (1.74,0.05) -- (1.80,0.05) -- (1.80,-1.75) -- (1.74,-1.75);
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
\fill[accentLight] (1.04,-1.68) rectangle (1.34,-1.38);
\node[tick] at (1.19,-1.53) {$\times$};
\node[tick] at (1.53,-1.53) {$\times$};
\node[note] at (0.85,-2.05) {$\lvert a_{54}\rvert<\varepsilon$};
\draw[map] (1.85,-0.85) -- (2.30,-0.85);
\draw[faint] (2.41,0.05) -- (2.35,0.05) -- (2.35,-1.75) -- (2.41,-1.75);
\draw[faint] (4.19,0.05) -- (4.25,0.05) -- (4.25,-1.75) -- (4.19,-1.75);
\node[tick] at (2.62,-0.17) {$\times$};
\node[tick] at (2.96,-0.17) {$\times$};
\node[tick] at (2.62,-0.51) {$\times$};
\node[tick] at (2.96,-0.51) {$\times$};
\node[tick] at (3.30,-0.51) {$\times$};
\node[tick] at (2.96,-0.85) {$\times$};
\node[tick] at (3.30,-0.85) {$\times$};
\node[tick] at (3.64,-0.85) {$\times$};
\node[tick] at (3.30,-1.19) {$\times$};
\node[tick] at (3.64,-1.19) {$\times$};
\node[tick, text=rule] at (3.98,-1.19) {$0$};
\node[tick, text=rule] at (3.64,-1.53) {$0$};
\fill[accentLight] (3.83,-1.68) rectangle (4.13,-1.38);
\node[tick] at (3.98,-1.53) {$\times$};
\node[note] at (3.30,-2.05) {deflated};
\end{tikzpicture}
\end{center}
```

Deflation: once $a_{m,m-1}$ is negligible the matrix splits, $a_{mm}$ is an eigenvalue, and the iteration continues on the leading block. An interior negligible entry splits the problem into two independent smaller problems.

:::

::: {#rmk-shifted-qr-algorithm-1 .remark name="Costs and the nonsymmetric case"}

For a symmetric matrix, the tridiagonal reduction costs $\tfrac43m^3$ flops, while each QR step on a tridiagonal block costs $O(m)$ (Givens rotations), so all eigenvalues cost $\tfrac43m^3+O(m^2)$; with eigenvectors, accumulating the rotations adds $O(m^3)$. For a nonsymmetric real matrix the eigenvalues may be complex, and the practical algorithm (Francis) applies two complex conjugate shifts at once in real arithmetic. It never forms $A-\mu I$: by the *implicit Q theorem* a Hessenberg similarity is determined by its first column, so one introduces a small "bulge" with the first column of $(A-\mu_1I)(A-\mu_2I)$ and chases it down the diagonal with reflectors. The total is about $10m^3$ flops for the real Schur form, and the method is backward stable.

:::
