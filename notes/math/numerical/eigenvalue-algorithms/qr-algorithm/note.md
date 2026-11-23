---
title: "The QR Algorithm"
sources: [mit18335-16]
requires: [math/numerical/eigenvalue-algorithms/power-and-inverse-iteration]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 16 (the power method and the QR algorithm) and its two readings (QR algorithm I and II), in our own wording; proofs written out in steps; iterates computed with numpy for the 4 by 4 example. -->

The QR algorithm is the standard method for computing all eigenvalues of a dense matrix. Its basic form is strikingly simple: factor $A=QR$, multiply the factors in the reverse order, and repeat. The iterates are unitarily similar to $A$ and converge to Schur form. The reason is that the algorithm secretly runs power iteration on a whole basis of vectors at once.

::: {#def-qr-algorithm .definition name="The QR algorithm (unshifted)"}

Set $A^{(0)}=A$. For $k=1,2,\dots$, compute a QR factorization $A^{(k-1)}=Q^{(k)}R^{(k)}$ and set
$$A^{(k)}=R^{(k)}Q^{(k)}.$$

:::

```{=latex}
\begin{algorithm}
\caption{Unshifted QR algorithm}
\begin{algorithmic}
\INPUT $A\in\mathbb{C}^{m\times m}$ (in practice already in Hessenberg form)
\STATE $A^{(0)}\gets A$
\FOR{$k=1,2,\dots$}
    \STATE $Q^{(k)}R^{(k)}\gets A^{(k-1)}$ \COMMENT{QR factorization}
    \STATE $A^{(k)}\gets R^{(k)}Q^{(k)}$
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

::: {#prp-qr-step-similarity .proposition name="A QR step is a unitary similarity and keeps Hessenberg form"}

$A^{(k)}=(Q^{(k)})^{\mathsf H}A^{(k-1)}Q^{(k)}$, so all iterates have the eigenvalues of $A$, and $A^{(k)}$ is Hermitian if $A$ is. If $A^{(k-1)}$ is upper Hessenberg and invertible, so is $A^{(k)}$.

:::

::: {.proof}

1. From $A^{(k-1)}=Q^{(k)}R^{(k)}$, $R^{(k)}=(Q^{(k)})^{\mathsf H}A^{(k-1)}$, so $A^{(k)}=R^{(k)}Q^{(k)}=(Q^{(k)})^{\mathsf H}A^{(k-1)}Q^{(k)}$.

2. A unitary similarity preserves the eigenvalues (@thm-similar-same-eigenvalues) and Hermitian symmetry.

3. *Hessenberg.* If $A^{(k-1)}=H$ is Hessenberg and invertible, $R^{(k)}$ is invertible and $Q^{(k)}=H(R^{(k)})^{-1}$. A Hessenberg matrix times an upper triangular one is Hessenberg (entry $(i,j)$ is $\sum_\ell h_{i\ell}t_{\ell j}$, and $h_{i\ell}=0$ for $\ell<i-1$, $t_{\ell j}=0$ for $\ell>j$, so it vanishes for $i>j+1$). Then $A^{(k)}=R^{(k)}Q^{(k)}$ is again upper triangular times Hessenberg, which is Hessenberg by the same argument.

:::

::: {#def-simultaneous-iteration .definition name="Simultaneous iteration"}

Apply power iteration to $n$ vectors at once, keeping them orthonormal: start from $\underline Q^{(0)}$ with orthonormal columns and for $k=1,2,\dots$ compute the reduced QR factorization
$$A\underline Q^{(k-1)}=\underline Q^{(k)}\underline{\hat R}^{(k)}.$$
Column $1$ of $\underline Q^{(k)}$ performs power iteration; the first $j$ columns span $A^k\operatorname{span}\{$first $j$ columns of $\underline Q^{(0)}\}$, since QR factorization does not change the spans of leading columns.

:::

::: {#thm-qr-algorithm-simultaneous-iteration .theorem name="The QR algorithm is simultaneous iteration"}

Run simultaneous iteration with $\underline Q^{(0)}=I$ and set $\underline R^{(k)}=\underline{\hat R}^{(k)}\cdots\underline{\hat R}^{(1)}$ and $\underline A^{(k)}=(\underline Q^{(k)})^{\mathsf H}A\underline Q^{(k)}$. Run the QR algorithm and set $\underline Q^{(k)}{}'=Q^{(1)}\cdots Q^{(k)}$, $\underline R^{(k)}{}'=R^{(k)}\cdots R^{(1)}$. If the QR factorizations are normalised the same way (say with positive diagonal in $R$, $A$ invertible), then $\underline Q^{(k)}=\underline Q^{(k)}{}'$, $\underline R^{(k)}=\underline R^{(k)}{}'$, $\underline A^{(k)}=A^{(k)}$, and both processes produce the QR factorization of the matrix power:
$$A^k=\underline Q^{(k)}\underline R^{(k)}.$$

:::

::: {.proof}

1. *Simultaneous iteration.* By induction, $A^k=A\cdot A^{k-1}=A\underline Q^{(k-1)}\underline R^{(k-1)}=\underline Q^{(k)}\underline{\hat R}^{(k)}\underline R^{(k-1)}=\underline Q^{(k)}\underline R^{(k)}$; the base case is $A^0=I=\underline Q^{(0)}$.

2. *QR algorithm.* By @prp-qr-step-similarity applied repeatedly, $A^{(k)}=(\underline Q^{(k)}{}')^{\mathsf H}A\,\underline Q^{(k)}{}'$, i.e. $A\,\underline Q^{(k-1)}{}'=\underline Q^{(k-1)}{}'A^{(k-1)}$.

3. Then $A^k=A\cdot A^{k-1}=A\,\underline Q^{(k-1)}{}'\underline R^{(k-1)}{}'$ (induction hypothesis) $=\underline Q^{(k-1)}{}'A^{(k-1)}\underline R^{(k-1)}{}'=\underline Q^{(k-1)}{}'Q^{(k)}R^{(k)}\underline R^{(k-1)}{}'=\underline Q^{(k)}{}'\underline R^{(k)}{}'$.

4. Both are QR factorizations of the invertible matrix $A^k$ with the same normalisation, which is unique (@thm-full-qr-existence). Hence the $Q$'s and $R$'s agree, and so do $\underline A^{(k)}$ and $A^{(k)}$ by step 2.

:::

::: {#fig-qr-algorithm-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\node[box] (a0) at (0,0) {$A^{(k-1)}$};
\node[box] (qr) at (3.6,0) {$Q^{(k)}R^{(k)}$};
\node[hl box] (a1) at (7.6,0) {$A^{(k)}=R^{(k)}Q^{(k)}$};
\draw[map] (a0) -- (qr) node[midway, note, above] {factor};
\draw[map] (qr) -- (a1) node[midway, note, above] {reverse};
\draw[map] (a1.south) to[bend left=25] node[note, below] {repeat} (a0.south);
\node[box] (s0) at (0,-2.4) {$\underline Q^{(k-1)}$};
\node[box] (s1) at (3.6,-2.4) {$A\underline Q^{(k-1)}$};
\node[hl box] (s2) at (7.6,-2.4) {$\underline Q^{(k)}\underline{\hat R}^{(k)}$};
\draw[map] (s0) -- (s1) node[midway, note, above] {multiply};
\draw[map] (s1) -- (s2) node[midway, note, above] {orthonormalize};
\node[note, anchor=west] at (7.8,-1.2) {$A^{(k)}=(\underline Q^{(k)})^{\mathsf H}A\underline Q^{(k)}$};
\draw[faint, <->] (7.6,-0.45) -- (7.6,-1.95);
\end{tikzpicture}
\end{center}
```

Two views of one iteration. Top: the QR algorithm factors and multiplies in reverse order. Bottom: simultaneous iteration multiplies a basis by $A$ and re-orthonormalizes. They produce the same matrices (@thm-qr-algorithm-simultaneous-iteration); the QR algorithm works on the "rotated" matrix $A^{(k)}$, simultaneous iteration on the basis $\underline Q^{(k)}$.

:::

::: {#thm-qr-algorithm-convergence .theorem name="Convergence of the unshifted QR algorithm"}

Let $A$ be real symmetric with eigenvalues $\lvert\lambda_1\rvert>\lvert\lambda_2\rvert>\dots>\lvert\lambda_m\rvert>0$ and orthonormal eigenvectors forming $Q=[\mathbf{q}_1\cdots\mathbf{q}_m]$, and suppose all leading principal submatrices of $Q^{\mathsf T}$ are nonsingular. Then the QR algorithm gives $A^{(k)}\to\operatorname{diag}(\lambda_1,\dots,\lambda_m)$, the columns of $\underline Q^{(k)}$ converge to $\pm\mathbf{q}_j$, and for $j<\ell$
$$\lvert a^{(k)}_{\ell j}\rvert=O(c^k),\qquad c=\max_{1\le i<m}\frac{\lvert\lambda_{i+1}\rvert}{\lvert\lambda_i\rvert}<1 .$$
More precisely, the subdiagonal entry $a^{(k)}_{j+1,j}$ decays like $\lvert\lambda_{j+1}/\lambda_j\rvert^k$.

:::

::: {.proof}

1. By @thm-qr-algorithm-simultaneous-iteration the first $j$ columns of $\underline Q^{(k)}$ span $A^k\operatorname{span}\{\mathbf{e}_1,\dots,\mathbf{e}_j\}$.

2. Write $\mathbf{e}_i=\sum_\ell(Q^{\mathsf T})_{\ell i}\mathbf{q}_\ell$. The assumption that the leading $j\times j$ block of $Q^{\mathsf T}$ is nonsingular says that $\mathbf{e}_1,\dots,\mathbf{e}_j$ have independent components along $\mathbf{q}_1,\dots,\mathbf{q}_j$. Applying $A^k$ multiplies the component along $\mathbf{q}_\ell$ by $\lambda_\ell^k$; after taking suitable combinations, $A^k\operatorname{span}\{\mathbf{e}_1,\dots,\mathbf{e}_j\}$ is spanned by vectors $\mathbf{q}_i+O(\lvert\lambda_{j+1}/\lambda_j\rvert^k)$, $i=1,\dots,j$, exactly as in the proof of @thm-power-iteration-convergence with $\lambda_1$ replaced by the smallest of $\lambda_1,\dots,\lambda_j$ in modulus.

3. So the span of the first $j$ columns of $\underline Q^{(k)}$ converges to $\operatorname{span}\{\mathbf{q}_1,\dots,\mathbf{q}_j\}$ at the rate $\lvert\lambda_{j+1}/\lambda_j\rvert^k$. Taking this for $j$ and $j-1$, column $j$ converges to $\pm\mathbf{q}_j$ at rate $c^k$.

4. Finally $a^{(k)}_{\ell j}=(\underline{\mathbf{q}}_\ell^{(k)})^{\mathsf T}A\,\underline{\mathbf{q}}_j^{(k)}$. With $\underline{\mathbf{q}}^{(k)}_j=\pm\mathbf{q}_j+O(c^k)$ this equals $\lambda_j\delta_{\ell j}+O(c^k)$, and the subdiagonal entry $(j+1,j)$ measures how far column $j+1$'s leading span is from being invariant, which decays like $\lvert\lambda_{j+1}/\lambda_j\rvert^k$.

:::

::: {#exm-qr-algorithm-four-by-four .example name="Watching the QR algorithm converge"}

For the tridiagonal matrix of @exm-eigen-iterations-compared, the QR algorithm stays tridiagonal and symmetric (@prp-qr-step-similarity). After one step the subdiagonal is $(0.691,\,0.642,\,-0.178)$; after five steps $(0.149,\,0.0826,\,-1.0\times10^{-4})$, with diagonal $(4.7310,\,3.1865,\,1.8278,\,0.2547)$; after twenty steps the matrix is diagonal to four decimals, $\operatorname{diag}(4.7453,\,3.1773,\,1.8227,\,0.2547)$. The three subdiagonal entries decay at the rates $\lambda_2/\lambda_1\approx0.67$, $\lambda_3/\lambda_2\approx0.57$ and $\lambda_4/\lambda_3\approx0.14$. The last one is fastest because $\lambda_4$ is small: this is inverse iteration at work (see the last remark of this note).

:::

::: {#fig-qr-algorithm-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.26cm, y=0.13cm]
\draw[->, faint] (0,0) -- (42,0) node[lab, right] {$k$};
\draw[->, faint] (0,0) -- (0,-36) node[lab, below] {$\log_{10}\lvert a^{(k)}_{j+1,j}\rvert$};
\foreach \x in {0,10,20,30,40} {\draw[faint] (\x,-0.4) -- (\x,0.4); \node[tick, above] at (\x,0.4) {$\x$};}
\foreach \y in {-10,-20,-30} {\draw[faint] (-0.3,\y) -- (0.3,\y); \node[tick, left] at (-0.3,\y) {$\y$};}
\draw[emph] plot coordinates {(0,0) (4,-0.66) (8,-1.35) (12,-2.04) (16,-2.74) (20,-3.44) (24,-4.13) (28,-4.83) (32,-5.53) (36,-6.22) (40,-6.92)};
\draw[emph, dashed] plot coordinates {(0,0) (4,-0.84) (8,-1.81) (12,-2.77) (16,-3.74) (20,-4.7) (24,-5.67) (28,-6.63) (32,-7.6) (36,-8.56) (40,-9.53)};
\draw[hl] plot coordinates {(0,0) (4,-3.37) (8,-6.79) (12,-10.21) (16,-13.63) (20,-17.05) (24,-20.46) (28,-23.88) (32,-27.3) (36,-30.72) (40,-34.14)};
\node[lab] at (34,-4.2) {$j=1$};
\node[lab] at (34,-11.2) {$j=2$};
\node[lab] at (27,-28) {$j=3$};
\end{tikzpicture}
\end{center}
```

Subdiagonal entries of $A^{(k)}$ in @exm-qr-algorithm-four-by-four on a log scale, computed in double precision (tiny entries are representable; they are simply negligible). Each decays linearly with slope $\log_{10}\lvert\lambda_{j+1}/\lambda_j\rvert$: $-0.17$, $-0.24$ and $-0.85$ per step.

:::

::: {#rmk-qr-algorithm-1 .remark name="Inverse iteration is hidden in the last column"}

Inverting $A^k=\underline Q^{(k)}\underline R^{(k)}$ and using $A^{\mathsf T}=A$ gives $A^{-k}=\underline Q^{(k)}(\underline R^{(k)})^{-\mathsf T}$, a QR-type factorization with a *lower* triangular factor. Reading it from the last column backwards, the QR algorithm is also simultaneous inverse iteration started from the reversed identity: the last column of $\underline Q^{(k)}$ undergoes inverse iteration with shift $0$ and converges to the eigenvector of the smallest eigenvalue. Replacing the shift $0$ by a good eigenvalue estimate is the idea of the shifted QR algorithm (@sec-math-numerical-eigenvalue-algorithms-shifted-qr-algorithm).

:::
