---
title: "Stability of Gaussian Elimination"
sources: [mit18335-13]
requires: [math/numerical/direct-solvers/triangular-systems]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 13 (LU factorization and partial pivoting), in our own wording; proofs written out in steps; growth factors measured with scipy.linalg.lu on random Gaussian matrices. -->

Gaussian elimination computes $PA=LU$ (@thm-pa-equals-lu) in $\sim\tfrac23m^3$ flops. In exact arithmetic any nonzero pivot will do; in floating point the choice of pivot decides whether the method is stable. The analysis rests on one number, the growth factor.

::: {#exm-elimination-without-pivoting .example name="A tiny pivot destroys the answer"}

Let $A=\begin{bmatrix}10^{-20}&1\\1&1\end{bmatrix}$ and $\mathbf{b}=(1,2)$, so $\mathbf{x}\approx(1,1)$; $A$ is well-conditioned ($\kappa\approx2.6$). Elimination without row exchange uses the multiplier $\ell_{21}=10^{20}$ and $u_{22}=1-10^{20}$, which rounds to $-10^{20}$. The computed factors multiply to
$$\tilde L\tilde U=\begin{bmatrix}1&0\\10^{20}&1\end{bmatrix}\begin{bmatrix}10^{-20}&1\\0&-10^{20}\end{bmatrix}=\begin{bmatrix}10^{-20}&1\\1&0\end{bmatrix},$$
which has lost the entry $a_{22}=1$ entirely, and solving with them gives $\tilde{\mathbf{x}}=(0,1)$. Each rounding was tiny; the damage came from the huge entries of $\tilde L$ and $\tilde U$. Exchanging the rows first gives the multiplier $10^{-20}$ and the correct answer.

:::

::: {#def-partial-pivoting .definition name="Gaussian elimination with partial pivoting"}

At step $k=1,\dots,m-1$, choose the row $i\ge k$ whose entry in column $k$ has the largest absolute value, swap rows $i$ and $k$ (of the working matrix and of the part of $L$ already computed), then eliminate below the pivot with multipliers $\ell_{jk}=u_{jk}/u_{kk}$ for $j>k$. The result is $PA=LU$ with $P$ the product of the swaps, and every multiplier satisfies $\lvert\ell_{jk}\rvert\le1$.

:::

```{=latex}
\begin{algorithm}
\caption{LU with partial pivoting}
\begin{algorithmic}
\INPUT $A\in\mathbb{C}^{m\times m}$; set $U\gets A$, $L\gets I$, $P\gets I$
\FOR{$k=1,\dots,m-1$}
    \STATE choose $i\ge k$ maximising $\lvert u_{ik}\rvert$
    \STATE swap rows $k$ and $i$ in $U_{\cdot,\,k:m}$, in $L_{\cdot,\,1:k-1}$ and in $P$
    \FOR{$j=k+1,\dots,m$}
        \STATE $\ell_{jk}\gets u_{jk}/u_{kk}$
        \STATE $U_{j,\,k:m}\gets U_{j,\,k:m}-\ell_{jk}U_{k,\,k:m}$
    \ENDFOR
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

::: {#fig-lu-stability-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.04,0.05) -- (-0.10,0.05) -- (-0.10,-1.41) -- (-0.04,-1.41);
\draw[faint] (1.40,0.05) -- (1.46,0.05) -- (1.46,-1.41) -- (1.40,-1.41);
\node[tick] at (0.17,-0.17) {$\times$};
\node[tick] at (0.51,-0.17) {$\times$};
\node[tick] at (0.85,-0.17) {$\times$};
\node[tick] at (1.19,-0.17) {$\times$};
\node[tick] at (0.17,-0.51) {$\times$};
\node[tick] at (0.51,-0.51) {$\times$};
\node[tick] at (0.85,-0.51) {$\times$};
\node[tick] at (1.19,-0.51) {$\times$};
\fill[accentLight] (0.02,-1.00) rectangle (0.32,-0.70);
\node[tick] at (0.17,-0.85) {$\bullet$};
\node[tick] at (0.51,-0.85) {$\times$};
\node[tick] at (0.85,-0.85) {$\times$};
\node[tick] at (1.19,-0.85) {$\times$};
\node[tick] at (0.17,-1.19) {$\times$};
\node[tick] at (0.51,-1.19) {$\times$};
\node[tick] at (0.85,-1.19) {$\times$};
\node[tick] at (1.19,-1.19) {$\times$};
\node[note] at (0.68,-1.71) {$A$};
\draw[map] (1.51,-0.68) -- (1.96,-0.68);
\draw[faint] (2.07,0.05) -- (2.01,0.05) -- (2.01,-1.41) -- (2.07,-1.41);
\draw[faint] (3.51,0.05) -- (3.57,0.05) -- (3.57,-1.41) -- (3.51,-1.41);
\fill[accentLight] (2.13,-0.32) rectangle (2.43,-0.02);
\node[tick] at (2.28,-0.17) {$\bullet$};
\node[tick] at (2.62,-0.17) {$\times$};
\node[tick] at (2.96,-0.17) {$\times$};
\node[tick] at (3.30,-0.17) {$\times$};
\node[tick] at (2.28,-0.51) {$\times$};
\node[tick] at (2.62,-0.51) {$\times$};
\node[tick] at (2.96,-0.51) {$\times$};
\node[tick] at (3.30,-0.51) {$\times$};
\node[tick] at (2.28,-0.85) {$\times$};
\node[tick] at (2.62,-0.85) {$\times$};
\node[tick] at (2.96,-0.85) {$\times$};
\node[tick] at (3.30,-0.85) {$\times$};
\node[tick] at (2.28,-1.19) {$\times$};
\node[tick] at (2.62,-1.19) {$\times$};
\node[tick] at (2.96,-1.19) {$\times$};
\node[tick] at (3.30,-1.19) {$\times$};
\node[note] at (2.79,-1.71) {swap rows $1,3$};
\draw[map] (3.62,-0.68) -- (4.07,-0.68);
\draw[faint] (4.18,0.05) -- (4.12,0.05) -- (4.12,-1.41) -- (4.18,-1.41);
\draw[faint] (5.62,0.05) -- (5.68,0.05) -- (5.68,-1.41) -- (5.62,-1.41);
\node[tick] at (4.39,-0.17) {$\times$};
\node[tick] at (4.73,-0.17) {$\times$};
\node[tick] at (5.07,-0.17) {$\times$};
\node[tick] at (5.41,-0.17) {$\times$};
\node[tick, text=rule] at (4.39,-0.51) {$0$};
\fill[accentLight] (4.58,-0.66) rectangle (4.88,-0.36);
\node[tick] at (4.73,-0.51) {$\times$};
\fill[accentLight] (4.92,-0.66) rectangle (5.22,-0.36);
\node[tick] at (5.07,-0.51) {$\times$};
\fill[accentLight] (5.26,-0.66) rectangle (5.56,-0.36);
\node[tick] at (5.41,-0.51) {$\times$};
\node[tick, text=rule] at (4.39,-0.85) {$0$};
\fill[accentLight] (4.58,-1.00) rectangle (4.88,-0.70);
\node[tick] at (4.73,-0.85) {$\times$};
\fill[accentLight] (4.92,-1.00) rectangle (5.22,-0.70);
\node[tick] at (5.07,-0.85) {$\times$};
\fill[accentLight] (5.26,-1.00) rectangle (5.56,-0.70);
\node[tick] at (5.41,-0.85) {$\times$};
\node[tick, text=rule] at (4.39,-1.19) {$0$};
\fill[accentLight] (4.58,-1.34) rectangle (4.88,-1.04);
\node[tick] at (4.73,-1.19) {$\times$};
\fill[accentLight] (4.92,-1.34) rectangle (5.22,-1.04);
\node[tick] at (5.07,-1.19) {$\times$};
\fill[accentLight] (5.26,-1.34) rectangle (5.56,-1.04);
\node[tick] at (5.41,-1.19) {$\times$};
\node[note] at (4.90,-1.71) {eliminate};
\end{tikzpicture}
\end{center}
```

One step of partial pivoting on a $4\times4$ matrix: the largest entry in the pivot column (marked $\bullet$) is swapped to the diagonal, then elimination zeros the rest of the column and updates the shaded block. The next step repeats this on the trailing $3\times3$ block.

:::

::: {#def-growth-factor .definition name="Growth factor"}

The *growth factor* of an elimination $PA=LU$ is
$$\rho=\frac{\max_{i,j}\lvert u_{ij}\rvert}{\max_{i,j}\lvert a_{ij}\rvert}.$$

:::

::: {#thm-lu-backward-error .theorem name="Backward error of Gaussian elimination"}

Let $\tilde L,\tilde U$ and $P$ be computed by Gaussian elimination with partial pivoting. Then $\tilde L\tilde U=PA+\delta A$ with
$$\frac{\lVert\delta A\rVert}{\lVert A\rVert}=O(\rho\,\varepsilon_{\text{mach}}),$$
and solving $A\mathbf{x}=\mathbf{b}$ with the computed factors by forward and back substitution gives $(A+\Delta A)\tilde{\mathbf{x}}=\mathbf{b}$ with $\lVert\Delta A\rVert/\lVert A\rVert=O(\rho\,\varepsilon_{\text{mach}})$.

:::

::: {.proof}

1. Entry $(i,j)$ of $U$ (for $i\le j$) or of $L$ (for $i>j$) is obtained from $a_{ij}$ by subtracting the products $\ell_{ik}u_{kj}$, $k<\min(i,j)$, one at a time, followed for $L$ by a division. By the same count as in @thm-back-substitution-backward-stable,
$$\Bigl\lvert a_{ij}-\sum_k\tilde\ell_{ik}\tilde u_{kj}\Bigr\rvert\le m\,\varepsilon_{\text{mach}}\sum_k\lvert\tilde\ell_{ik}\rvert\lvert\tilde u_{kj}\rvert+O(\varepsilon_{\text{mach}}^2),$$
with $A$ replaced by $PA$. In matrix form $\lvert\delta A\rvert\le m\varepsilon_{\text{mach}}\lvert\tilde L\rvert\lvert\tilde U\rvert$ entrywise.

2. With partial pivoting $\lvert\tilde\ell_{ik}\rvert\le1$, and $\lvert\tilde u_{kj}\rvert\le\rho\max\lvert a_{ij}\rvert$ by the definition of $\rho$. So each entry of $\lvert\tilde L\rvert\lvert\tilde U\rvert$ is at most $m\rho\max\lvert a_{ij}\rvert$, and $\lVert\delta A\rVert=O(\rho\,\varepsilon_{\text{mach}})\lVert A\rVert$ with constants depending only on $m$.

3. The two triangular solves add backward errors $\delta L,\delta U$ with $\lvert\delta L\rvert\le m\varepsilon_{\text{mach}}\lvert\tilde L\rvert$ and $\lvert\delta U\rvert\le m\varepsilon_{\text{mach}}\lvert\tilde U\rvert$ (@thm-back-substitution-backward-stable). Then $(\tilde L+\delta L)(\tilde U+\delta U)=PA+\delta A+\delta L\,\tilde U+\tilde L\,\delta U+\delta L\,\delta U$, and the extra terms are bounded by the same $O(m\rho\,\varepsilon_{\text{mach}})\max\lvert a_{ij}\rvert$ as in step 2.

:::

So Gaussian elimination is backward stable exactly when $\rho$ is bounded independently of the matrix. Without pivoting $\rho$ can be arbitrarily large (in @exm-elimination-without-pivoting it is $10^{20}$). With partial pivoting it is bounded, but only by a constant that grows exponentially in $m$.

::: {#prp-growth-factor-bound .proposition name="Growth with partial pivoting"}

With partial pivoting, $\rho\le2^{m-1}$, and this is attained: the matrix with $1$ on the diagonal and in the last column and $-1$ everywhere below the diagonal has $\rho=2^{m-1}$.

:::

::: {.proof}

1. Since $\lvert\ell_{jk}\rvert\le1$, an update $u_{ji}\gets u_{ji}-\ell_{jk}u_{ki}$ gives $\lvert u_{ji}\rvert\le2\max\lvert\cdot\rvert$ of the previous working matrix. So the largest entry at most doubles at each of the $m-1$ steps.

2. For the given matrix every pivot candidate in column $k$ has absolute value $1$, so no rows are swapped. Elimination in column $1$ adds row $1$ to each row below; this leaves the other entries left of the last column unchanged and doubles the last column below row $1$.

3. Inductively, after step $k$ the last column holds $1,2,4,\dots,2^{k-1},2^k,\dots,2^k$, and finally $u_{mm}=2^{m-1}$ while $\max\lvert a_{ij}\rvert=1$. For $m=5$ the last column of $U$ is $(1,2,4,8,16)$.

:::

::: {#rmk-lu-stability-1 .remark name="Why partial pivoting works in practice"}

Matrices with large growth are extraordinarily rare in practice. For random matrices with independent Gaussian entries the growth factor grows only like a small power of $m$ (about $m^{1/2}$ or less), and the set of matrices with growth $\rho>m^{\alpha}$ seems to shrink exponentially as $\alpha$ grows; a precise explanation of this behaviour is still incomplete. Partial pivoting is therefore the standard method, "backward stable in practice" though not in the worst case. *Complete pivoting* (choosing the largest entry of the whole trailing block) has a much smaller worst-case growth but costs $O(m^3)$ comparisons; QR is unconditionally backward stable but costs twice as much.

:::

::: {#fig-lu-stability-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.85cm, y=0.85cm]
\draw[->, faint] (2.6,0) -- (9.6,0) node[lab, right] {$\log_2m$};
\draw[->, faint] (2.6,0) -- (2.6,3.5) node[lab, above] {$\log_{10}\rho$};
\foreach \x in {3,...,9} {\draw[faint] (\x,-0.06) -- (\x,0.06); \node[tick, below] at (\x,-0.06) {$\x$};}
\foreach \y in {1,2,3} {\draw[faint] (2.54,\y) -- (2.66,\y); \node[tick, left] at (2.54,\y) {$\y$};}
\draw[emph] plot coordinates {(3,0.08) (4,0.28) (5,0.41) (6,0.59) (7,0.76) (8,0.90) (9,1.09)};
\foreach \p in {(3,0.08),(4,0.28),(5,0.41),(6,0.59),(7,0.76),(8,0.90),(9,1.09)} {\fill \p circle (2pt);}
\draw[faint, dashed] (3,0.45) -- (9,1.35) node[lab, right] {$\sqrt m$};
\draw[hl] plot coordinates {(3,2.11) (3.17,2.41) (3.32,2.71) (3.46,3.01)};
\node[lab] at (5.6,2.6) {worst case $2^{m-1}$};
\end{tikzpicture}
\end{center}
```

Mean growth factor of partial pivoting on random Gaussian $m\times m$ matrices (ten samples each, $m=8,\dots,512$), compared with $\sqrt m$ (dashed) and the worst-case bound $2^{m-1}$, which already exceeds $10^3$ at $m=11$.

:::
