---
title: "Multiplicities of Eigenvalues and Jordan Normal Form"
sources: [camib-la-6, mit1806-28]
requires: [math/linear-algebra/endomorphisms/cayley-hamilton]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 6.4, in our own wording; examples ours (checked with sympy); proofs written out in steps. MIT 18.06 states the Jordan form without proof (thm-jordan-form, def-jordan-block); here the statement is the same, uniqueness is proved below and existence in math/linear-algebra/endomorphisms/generalized-eigenspaces. Merge proposed to the owner. -->

<!-- Merged 2026-11-20 (owner): thm-jordan-form (18.06 L28, stated without proof) merged into thm-jordan-normal-form, which gained its sentence on block counts and diagonalisability. -->

Not every endomorphism is diagonalisable. The Jordan normal form is the best substitute over $\mathbb C$: a block diagonal matrix with one eigenvalue per block and $1$s just above the diagonal. Throughout, $\alpha\in\operatorname{End}(V)$, $\dim V=n$, and $\lambda$ is an eigenvalue of $\alpha$.

::: {#def-algebraic-geometric-multiplicity .definition name="Algebraic and geometric multiplicity"}

1. The *algebraic multiplicity* $a_\lambda$ is the multiplicity of $\lambda$ as a root of $\chi_\alpha$.
2. The *geometric multiplicity* $g_\lambda=\dim E(\lambda)=n(\alpha-\lambda\iota)$.
3. $c_\lambda$ is the multiplicity of $\lambda$ as a root of $m_\alpha$.

:::

::: {#prp-multiplicity-bounds .proposition name="Bounds on the multiplicities"}

$1\le g_\lambda\le a_\lambda$ and $1\le c_\lambda\le a_\lambda$.

:::

::: {.proof}

1. $g_\lambda\ge1$ since $\lambda$ is an eigenvalue, and $c_\lambda\ge1$ by @cor-minimal-and-characteristic-same-roots.

2. Extend a basis $v_1,\dots,v_g$ of $E(\lambda)$ to a basis of $V$. Then $[\alpha]=\begin{bmatrix}\lambda I_g&\ast\\0&C\end{bmatrix}$, and $\chi_\alpha(t)=(t-\lambda)^g\det(tI-C)$ by @lem-block-triangular-determinant. So $(t-\lambda)^g$ divides $\chi_\alpha$: $g_\lambda\le a_\lambda$.

3. $m_\alpha\mid\chi_\alpha$ (@thm-cayley-hamilton), so $c_\lambda\le a_\lambda$.

:::

::: {#fig-jordan-normal-form-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell, fill=primaryLight] (2.00,0.00) rectangle (2.75,0.45);
\draw[cell, fill=primaryLight] (2.75,0.00) rectangle (3.50,0.45);
\node[lab, tick] at (2.75,-0.22) {$g_\lambda=2$};
\draw[cell, fill=accentLight] (3.50,0.00) rectangle (4.25,0.45);
\node[lab, anchor=east] at (1.90,0.23) {$E(\lambda)$};
\draw[cell, fill=accentLight] (2.00,-0.90) rectangle (2.75,-0.45);
\draw[cell, fill=accentLight] (2.75,-0.90) rectangle (3.50,-0.45);
\draw[cell, fill=accentLight] (3.50,-0.90) rectangle (4.25,-0.45);
\node[lab, tick] at (3.12,-1.12) {$a_\lambda=3$};
\node[lab, anchor=east] at (1.90,-0.68) {$\ker(\alpha-\lambda\iota)^n$};
\node[lab, note, anchor=west] at (4.6,-0.2) {$1\le g_\lambda\le a_\lambda$};
\end{tikzpicture}
\end{center}
```

The eigenspace sits inside the generalised eigenspace, whose dimension is the algebraic multiplicity. Equality $g_\lambda=a_\lambda$ for every $\lambda$ is diagonalisability (@cor-diagonalisable-iff-multiplicities).

:::

::: {#cor-diagonalisable-iff-multiplicities .corollary name="Diagonalisability in terms of multiplicities"}

If $\chi_\alpha$ splits over $F$ (for instance $F=\mathbb C$), the following are equivalent: $\alpha$ is diagonalisable; $a_\lambda=g_\lambda$ for every eigenvalue $\lambda$; $c_\lambda=1$ for every eigenvalue $\lambda$.

:::

::: {.proof}

1. Since $\chi_\alpha$ splits, $\sum_\lambda a_\lambda=n$. By @thm-diagonalizable-iff-eigenspaces, $\alpha$ is diagonalisable iff $\sum_\lambda g_\lambda=n$, and since $g_\lambda\le a_\lambda$ for each $\lambda$ this happens iff $g_\lambda=a_\lambda$ for all $\lambda$.

2. $m_\alpha$ has the same roots as $\chi_\alpha$, all in $F$, so $m_\alpha=\prod_\lambda(t-\lambda)^{c_\lambda}$; it is a product of distinct linear factors iff all $c_\lambda=1$, which is diagonalisability by @thm-diagonalisability-minimal-polynomial.

:::

::: {#def-jordan-normal-form .definition name="Jordan normal form"}

A matrix is in *Jordan normal form* if it is block diagonal,
$$\begin{bmatrix}J_{n_1}(\lambda_1)&&\\&\ddots&\\&&J_{n_k}(\lambda_k)\end{bmatrix},$$
with Jordan blocks $J_m(\lambda)$ (@def-jordan-block) on the diagonal; the $\lambda_i$ need not be distinct.

:::

::: {#fig-jordan-normal-form-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0,0) rectangle (4.5,-4.5);
\draw[hl cell] (0.0,0.0) rectangle (2.25,-2.25); \node[lab, tick] at (1.125,-1.125) {$J_3(\lambda_1)$};
\draw[hl cell] (2.25,-2.25) rectangle (3.75,-3.75); \node[lab, tick] at (3.0,-3.0) {$J_2(\lambda_1)$};
\draw[hl cell] (3.75,-3.75) rectangle (4.5,-4.5); \node[lab, tick] at (4.125,-4.125) {$J_1(\lambda_2)$};
\node[lab, note, anchor=west, align=left] at (4.9,-2.0) {zeros outside the diagonal blocks;\\each block: one eigenvalue on its diagonal, $1$s just above};
\end{tikzpicture}
\end{center}
```

The shape of a Jordan normal form, here $J_3(\lambda_1)\oplus J_2(\lambda_1)\oplus J_1(\lambda_2)$. For $\lambda_1$ the algebraic multiplicity is $3+2=5$ (total block size) and the geometric multiplicity is $2$ (number of blocks).

:::

::: {#thm-jordan-normal-form .theorem name="Jordan normal form theorem"}

Every $A\in\operatorname{Mat}_n(\mathbb C)$ is similar to a matrix in Jordan normal form, which is unique up to the order of the blocks. More generally, this holds over any field $F$ for every $A$ whose characteristic polynomial splits over $F$. For each eigenvalue $\lambda$, the number of blocks $J_m(\lambda)$ is the number of independent eigenvectors for $\lambda$, and $A$ is diagonalisable exactly when every block is $1\times1$.

:::

Existence is proved in @sec-math-linear-algebra-endomorphisms-generalized-eigenspaces (@thm-jordan-normal-form-existence); the block counts are @thm-jordan-block-count with $r=1$, and diagonalisability is @cor-diagonalisable-iff-multiplicities; uniqueness follows from the next theorem, because it computes the number of blocks of each size from $\alpha$ alone.

::: {#thm-jordan-block-count .theorem name="Counting Jordan blocks"}

If $[\alpha]$ is in Jordan normal form, then for $r\ge1$ the number of blocks $J_m(\lambda)$ with $m\ge r$ is
$$n\big((\alpha-\lambda\iota)^r\big)-n\big((\alpha-\lambda\iota)^{r-1}\big).$$
Consequently, for each eigenvalue $\lambda$: $a_\lambda$ is the total size of the blocks with eigenvalue $\lambda$; $g_\lambda$ is the number of these blocks; and $c_\lambda$ is the size of the largest.

:::

::: {.proof}

1. Nullity is additive over the diagonal blocks, so it suffices to compute $n\big((J_m(\mu)-\lambda I)^r\big)$ for one block.

2. If $\mu\ne\lambda$, then $J_m(\mu)-\lambda I$ is upper triangular with non-zero diagonal $\mu-\lambda$, hence invertible (@lem-determinant-transpose, @thm-determinant-invertible), and so are its powers: nullity $0$.

3. If $\mu=\lambda$, then $N=J_m(\lambda)-\lambda I$ sends $e_1\mapsto0$ and $e_k\mapsto e_{k-1}$, so $N^r$ sends $e_k\mapsto e_{k-r}$ (and to $0$ if $k\le r$). Its kernel is $\langle e_1,\dots,e_{\min(r,m)}\rangle$, of dimension $\min(r,m)$.

4. Hence $\min(r,m)-\min(r-1,m)$, which is $1$ if $m\ge r$ and $0$ otherwise, is the block's contribution to the difference. Summing over blocks gives the formula.

5. With $r=1$: $g_\lambda=n(\alpha-\lambda\iota)$ is the number of $\lambda$-blocks. The Jordan matrix is upper triangular, so $\chi_\alpha=\prod_i(t-\lambda_i)^{n_i}$, and $a_\lambda$ is the total size of the $\lambda$-blocks.

6. For $c_\lambda$: by step 3, $(J_m(\lambda)-\lambda I)^r=0$ exactly when $r\ge m$, and by step 2 the factor $(J_m(\mu)-\lambda I)^r$ is invertible for $\mu\ne\lambda$. So $p(t)=\prod_\lambda(t-\lambda)^{s_\lambda}$, with $s_\lambda$ the largest $\lambda$-block size, kills every block. If one exponent is lowered to $s_\lambda-1$, the largest $\lambda$-block $J$ is not killed: $p(J)$ is $(J-\lambda I)^{s_\lambda-1}\ne0$ times invertible factors. Since $m_\alpha$ divides $p$ and has every eigenvalue as a root (@cor-minimal-and-characteristic-same-roots), $m_\alpha=p$ and $c_\lambda=s_\lambda$.

:::

::: {#fig-jordan-normal-form-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[hl dot] at (0.00,0.00) {};
\node[dot] at (0.00,-0.60) {};
\node[dot] at (0.00,-1.20) {};
\node[lab, tick] at (0.00,0.4) {$J_3$};
\node[hl dot] at (0.80,0.00) {};
\node[dot] at (0.80,-0.60) {};
\node[lab, tick] at (0.80,0.4) {$J_2$};
\node[hl dot] at (1.60,0.00) {};
\node[dot] at (1.60,-0.60) {};
\node[lab, tick] at (1.60,0.4) {$J_2$};
\node[hl dot] at (2.40,0.00) {};
\node[lab, tick] at (2.40,0.4) {$J_1$};
\node[lab, anchor=west] at (3.0,0.00) {$r=1$: 4 blocks of size $\ge1$};
\node[lab, anchor=west] at (3.0,-0.60) {$r=2$: 3 blocks of size $\ge2$};
\node[lab, anchor=west] at (3.0,-1.20) {$r=3$: 1 blocks of size $\ge3$};
\node[lab, anchor=west] at (3.0,-1.9) {(row lengths $=n(\beta^r)-n(\beta^{r-1})$)};
\end{tikzpicture}
\end{center}
```

The nilpotent Jordan form $J_3(0)\oplus J_2(0)\oplus J_2(0)\oplus J_1(0)$ drawn as columns of dots, one column per block. Row $r$ has as many dots as there are blocks of size at least $r$, which @thm-jordan-block-count reads off from the nullities: here $4,3,1$, the jumps in $n(\beta^r)=0,4,7,8$. Top dots (highlighted) span the kernel.

:::

::: {#exm-jordan-normal-form .example name="Finding a Jordan normal form"}

Let $A=\begin{bmatrix}3&1&0\\-1&1&0\\1&1&2\end{bmatrix}$. Then $\chi_A(t)=(t-2)^3$, so $a_2=3$, and
$$A-2I=\begin{bmatrix}1&1&0\\-1&-1&0\\1&1&0\end{bmatrix},\qquad (A-2I)^2=0.$$
So $n(A-2I)=2$: two blocks; $n((A-2I)^2)-n(A-2I)=1$: one block of size $\ge2$. The Jordan normal form is $J_2(2)\oplus J_1(2)$, and $m_A=(t-2)^2$. A Jordan basis: take $w=e_1$ (not in $\ker(A-2I)$), $v_1=(A-2I)w=(1,-1,1)^{\mathsf T}$, $v_2=w$, and $v_3=e_3\in\ker(A-2I)$ independent of $v_1$. With $P=[v_1\ v_2\ v_3]$,
$$P^{-1}AP=\begin{bmatrix}2&1&0\\0&2&0\\0&0&2\end{bmatrix}.$$

:::

::: {#fig-jordan-normal-form-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.000,1.100) rectangle (0.550,1.650);
\node[lab] at (0.275,1.375) {$2$};
\draw[hl cell] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$1$};
\draw[cell frame] (1.100,1.100) rectangle (1.650,1.650);
\node[lab] at (1.375,1.375) {$0$};
\draw[hl cell] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$0$};
\draw[hl cell] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$2$};
\draw[cell frame] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$0$};
\draw[cell frame] (0.000,-0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$0$};
\draw[cell frame] (0.550,-0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$0$};
\draw[cell, fill=primaryLight] (1.100,-0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$2$};
\node[lab, note] at (0.825,-0.350) {$P^{-1}AP$};
\node[small vertex] (w) at (5.2,1.1) {$v_2$}; \node[small vertex] (v1) at (3.8,1.1) {$v_1$}; \node[lab] (z1) at (2.6,1.1) {$\mathbf 0$};
\node[small vertex] (v3) at (3.8,0.2) {$v_3$}; \node[lab] (z3) at (2.6,0.2) {$\mathbf 0$};
\draw[->, emph] (w) -- (v1); \draw[->, emph] (v1) -- (z1); \draw[->, emph] (v3) -- (z3);
\node[lab, note, anchor=west, align=left] at (5.8,0.6) {arrows: $A-2I$;\\$v_2=e_1$, $v_1=(1,-1,1)$, $v_3=e_3$};
\end{tikzpicture}
\end{center}
```

@exm-jordan-normal-form: one chain of length $2$ and one of length $1$ give the blocks $J_2(2)$ and $J_1(2)$. A chain is read from its top vector, here $v_2$, down to $\mathbf 0$.

:::

::: {#rmk-jordan-normal-form-1 .remark name="What the invariants do not determine"}

The characteristic polynomial, the minimal polynomial and the geometric multiplicities together do not always determine the Jordan form. $J_3(0)\oplus J_3(0)\oplus J_1(0)$ and $J_3(0)\oplus J_2(0)\oplus J_2(0)$ are both $7\times7$ with $\chi=t^7$, $m=t^3$ and three blocks, yet they are not similar: the ranks of their squares are $2$ and $1$, as @thm-jordan-block-count says they must differ.

:::
