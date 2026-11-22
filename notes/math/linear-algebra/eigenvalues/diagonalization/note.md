---
title: "Diagonalization and Powers of A"
sources: [mit1806-22]
requires: [math/linear-algebra/eigenvalues/eigenvalues-and-eigenvectors]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 22, in our own wording; proofs written out in steps. Example numbers checked with sympy. -->

::: {#thm-diagonalization .theorem name="Diagonalization"}

Suppose the $n\times n$ matrix $A$ has $n$ independent eigenvectors $\mathbf{x}_1,\dots,\mathbf{x}_n$ with eigenvalues $\lambda_1,\dots,\lambda_n$. Put them as the columns of the *eigenvector matrix* $S$ and let $\Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$. Then
$$AS=S\Lambda,\qquad A=S\Lambda S^{-1},\qquad A^k=S\Lambda^kS^{-1}.$$

:::

::: {.proof}

1. Column $j$ of $AS$ is $A\mathbf{x}_j=\lambda_j\mathbf{x}_j$, which is column $j$ of $S\Lambda$.

2. The columns of $S$ are independent, so $S$ is invertible (@prp-independence-and-nullspace); multiply on the right by $S^{-1}$.

3. $A^k=(S\Lambda S^{-1})(S\Lambda S^{-1})\cdots=S\Lambda^kS^{-1}$, since the inner factors $S^{-1}S$ cancel.

:::

::: {#fig-diagonalization-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (x) at (0,1.6) {$\mathbf x$}; \node[box] (Ax) at (6.4,1.6) {$A\mathbf x$};
\node[box] (c) at (0,0) {$\mathbf c=X^{-1}\mathbf x$}; \node[box] (Lc) at (6.4,0) {$\Lambda\mathbf c$};
\draw[->, emph] (x) -- node[above, lab] {$A$} (Ax);
\draw[->, emph, accent] (c) -- node[below, lab, note] {$\Lambda$: scale each coordinate by $\lambda_i$} (Lc);
\draw[->, emph] (x) -- node[left, lab] {$X^{-1}$} (c);
\draw[->, emph] (Lc) -- node[right, lab] {$X$} (Ax);
\node[lab, note, anchor=west, align=left] at (7.6,0.8) {standard coordinates on top,\\eigenvector coordinates below:\\$A=X\Lambda X^{-1}$};
\end{tikzpicture}
\end{center}
```

Diagonalization as a change of coordinates. Write $\mathbf x$ in the eigenvector basis ($X^{-1}$), multiply each coordinate by its eigenvalue ($\Lambda$), and go back ($X$). Going around the bottom equals going across the top.

:::

<!-- Merged 2026-11-20 (owner): the block thm-distinct-eigenvalues-independent was removed in favour of lem-eigenspaces-independent (Cambridge IB Linear Algebra), which states it for any field or inner product space with a full proof. -->

**Distinct eigenvalues give independent eigenvectors.** Eigenvectors belonging to different eigenvalues are linearly independent (@lem-eigenspaces-independent). In particular, if the $n$ eigenvalues of $A$ are distinct, $A$ is diagonalizable (@thm-diagonalizable-iff-eigenspaces).

::: {#rmk-diagonalization-1 .remark name="Repeated eigenvalues"}

With a repeated eigenvalue there may be too few eigenvectors. $A=\begin{bmatrix}2&1\\0&2\end{bmatrix}$ has $\lambda=2$ twice, but $N(A-2I)$ is only the line through $(1,0)$. Such a matrix cannot be diagonalized (@sec-math-linear-algebra-eigenvalues-similar-matrices-and-jordan-form). The *algebraic multiplicity* (as a root) can exceed the *geometric multiplicity* ($\dim N(A-\lambda I)$), never the other way round.

:::

::: {#cor-powers-and-difference-equations .corollary name="Difference equations"}

If $A$ is diagonalizable and $\mathbf{u}_{k+1}=A\mathbf{u}_k$, write $\mathbf{u}_0=c_1\mathbf{x}_1+\dots+c_n\mathbf{x}_n$ (that is, $\mathbf{c}=S^{-1}\mathbf{u}_0$). Then
$$\mathbf{u}_k=A^k\mathbf{u}_0=c_1\lambda_1^k\mathbf{x}_1+\dots+c_n\lambda_n^k\mathbf{x}_n.$$
Hence $A^k\to0$ as $k\to\infty$ exactly when every $\lvert\lambda_i\rvert<1$.

:::

::: {.proof}

1. $A^k\mathbf{x}_i=\lambda_i^k\mathbf{x}_i$, by applying $A\mathbf{x}_i=\lambda_i\mathbf{x}_i$ $k$ times; then use linearity.

2. $\lambda_i^k\to0$ for all $i$ iff every $\lvert\lambda_i\rvert<1$; since the $\mathbf{x}_i$ are independent, $A^k\mathbf{u}_0\to\mathbf{0}$ for every $\mathbf{u}_0$ iff this holds.

:::

::: {#fig-diagonalization-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, muted] (0,0) -- (5.2,0) node[right, lab, tick] {$k$}; \draw[->, muted] (0,-1.2) -- (0,1.3);
\draw[accent, emph] (0.00,0) -- (0.00,1.000); \fill[accent] (0.00,1.000) circle[pt];
\draw[accent, emph] (0.50,0) -- (0.50,-0.618); \fill[accent] (0.50,-0.618) circle[pt];
\draw[accent, emph] (1.00,0) -- (1.00,0.382); \fill[accent] (1.00,0.382) circle[pt];
\draw[accent, emph] (1.50,0) -- (1.50,-0.236); \fill[accent] (1.50,-0.236) circle[pt];
\draw[accent, emph] (2.00,0) -- (2.00,0.146); \fill[accent] (2.00,0.146) circle[pt];
\draw[accent, emph] (2.50,0) -- (2.50,-0.090); \fill[accent] (2.50,-0.090) circle[pt];
\draw[accent, emph] (3.00,0) -- (3.00,0.056); \fill[accent] (3.00,0.056) circle[pt];
\draw[accent, emph] (3.50,0) -- (3.50,-0.034); \fill[accent] (3.50,-0.034) circle[pt];
\draw[accent, emph] (4.00,0) -- (4.00,0.021); \fill[accent] (4.00,0.021) circle[pt];
\draw[accent, emph] (4.50,0) -- (4.50,-0.013); \fill[accent] (4.50,-0.013) circle[pt];
\node[lab, note, accent, anchor=west] at (5.3,0.6) {$\lambda_2^k=(-0.618)^k\to0$};
\end{tikzpicture}
\end{center}
```

In $\mathbf u_k=A^k\mathbf u_0=c_1\lambda_1^k\mathbf x_1+c_2\lambda_2^k\mathbf x_2$ each eigenvector component evolves on its own. An eigenvalue with $\lvert\lambda\rvert<1$, here $\lambda_2$ of the Fibonacci matrix, gives a component that shrinks (and alternates in sign when $\lambda<0$).

:::

::: {#exm-fibonacci-by-eigenvalues .example name="Fibonacci numbers"}

The rule $F_{k+2}=F_{k+1}+F_k$ becomes $\mathbf{u}_{k+1}=A\mathbf{u}_k$ with $\mathbf{u}_k=(F_{k+1},F_k)$ and $A=\begin{bmatrix}1&1\\1&0\end{bmatrix}$. The eigenvalues solve $\lambda^2-\lambda-1=0$:
$$\lambda_1=\frac{1+\sqrt5}2\approx1.618,\qquad\lambda_2=\frac{1-\sqrt5}2\approx-0.618,$$
with eigenvectors $(\lambda_i,1)$. From $\mathbf{u}_0=(1,0)=\frac{1}{\lambda_1-\lambda_2}\big((\lambda_1,1)-(\lambda_2,1)\big)$,
$$F_k=\frac{\lambda_1^k-\lambda_2^k}{\sqrt5}.$$
Since $\lvert\lambda_2\rvert<1$, $F_k$ is the integer nearest to $\lambda_1^k/\sqrt5$, and $F_{k+1}/F_k\to\lambda_1$. For example $F_{10}=55$ and $\lambda_1^{10}/\sqrt5\approx55.004$.

:::

::: {#fig-diagonalization-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[y={(0,1.3cm)}]
\draw[->, muted] (0,0) -- (6.6,0) node[right, lab, tick] {$k$}; \draw[->, muted] (0,0) -- (0,2.4);
\draw[faint, dashed, accent] (0,1.618) -- (6.3,1.618) node[right, lab, note] {$\lambda_1\approx1.618$};
\draw[faint] (0,1) -- (-0.1,1) node[left, lab, tick] {$1$}; \draw[faint] (0,2) -- (-0.1,2) node[left, lab, tick] {$2$};
\draw[emph, primary] (0.50,1.000) -- (1.00,2.000) -- (1.50,1.500) -- (2.00,1.667) -- (2.50,1.600) -- (3.00,1.625) -- (3.50,1.615) -- (4.00,1.619) -- (4.50,1.618) -- (5.00,1.618) -- (5.50,1.618) -- (6.00,1.618);
\fill[primary] (0.50,1.000) circle[pt];
\fill[primary] (1.00,2.000) circle[pt];
\fill[primary] (1.50,1.500) circle[pt];
\fill[primary] (2.00,1.667) circle[pt];
\fill[primary] (2.50,1.600) circle[pt];
\fill[primary] (3.00,1.625) circle[pt];
\fill[primary] (3.50,1.615) circle[pt];
\fill[primary] (4.00,1.619) circle[pt];
\fill[primary] (4.50,1.618) circle[pt];
\fill[primary] (5.00,1.618) circle[pt];
\fill[primary] (5.50,1.618) circle[pt];
\fill[primary] (6.00,1.618) circle[pt];
\end{tikzpicture}
\end{center}
```

The ratios $F_{k+1}/F_k$ of consecutive Fibonacci numbers ($1,2,1.5,1.67,1.6,\dots$) settle on $\lambda_1$, the larger eigenvalue. The other component is multiplied by $\lambda_2\approx-0.618$ each step, which makes the ratios alternate above and below the limit while it dies out.

:::

::: {#fig-diagonalization-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.38]
\draw[->] (-4.5,0) -- (14.5,0) node[lab, right] {$F_{k+1}$};
\draw[->] (0,-2) -- (0,9.5) node[lab, above] {$F_k$};
\draw[emph, primary] (-3.2,-2) -- (14,8.65) node[lab, right] {$(\lambda_1,1)$};
\draw[emph, muted, dashed] (1.24,-2) -- (-4.3,6.96) node[lab, above] {$(\lambda_2,1)$};
\draw[faint] (1,0) -- (1,1) -- (2,1) -- (3,2) -- (5,3) -- (8,5) -- (13,8);
\foreach \p/\k in {(1,0)/0,(1,1)/1,(2,1)/2,(3,2)/3,(5,3)/4,(8,5)/5,(13,8)/6} \node[hl dot] at \p {};
\node[lab, below] at (1,0) {$\mathbf u_0$};
\node[lab, below right] at (13,8) {$\mathbf u_6$};
\end{tikzpicture}
\end{center}
```

The vectors $\mathbf u_k=(F_{k+1},F_k)$ of @exm-fibonacci-by-eigenvalues. The component along $(\lambda_2,1)$ shrinks like $\lambda_2^k$, so the points line up along the eigenvector $(\lambda_1,1)$ and $F_{k+1}/F_k\to\lambda_1$.

:::
