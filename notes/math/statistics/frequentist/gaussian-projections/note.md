---
title: "Orthogonal Projections of Gaussian Noise"
sources: [camib-st-11, camib-st-13, camib-st-14, camib-st-15, camib-sts-3-q3]
requires: [math/statistics/frequentist/t-tests]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part IB Statistics (Lent 2025, lecturer's notes), Lectures 11, 13, 14 and 15 and Example Sheet 3 (question 3), in our own wording; proofs written out in steps. -->

The distribution theory of the normal linear model rests on one geometric fact: spherical Gaussian noise splits into independent pieces along orthogonal subspaces, and the squared length of each piece is $\sigma^2$ times a chi-squared variable whose degrees of freedom is the dimension of the subspace.

::: {#prp-projection-rank-trace .proposition name="Projection matrices"}

Let $P\in\mathbb R^{n\times n}$ be an *orthogonal projection matrix*, that is $P^{\mathsf T}=P$ and $P^2=P$. Then

1. $P=UU^{\mathsf T}$ where the columns of $U\in\mathbb R^{n\times r}$, $r=\operatorname{rank}P$, form an orthonormal basis of the column space of $P$;
2. the eigenvalues of $P$ are $0$ and $1$, and $\operatorname{rank}P=\operatorname{tr}P$;
3. $I-P$ is also an orthogonal projection matrix;
4. $\|y\|^2=\|Py\|^2+\|(I-P)y\|^2$ for all $y\in\mathbb R^n$.

:::

::: {.proof}

1. Let $U$ have orthonormal columns spanning $\operatorname{col}(P)$. Each column of $P$ lies in this space, so $P=UB$ for some $B$. Since $P^2=P$ we have $P(Uv)=Uv$ for all $v$ (as $Uv\in\operatorname{col}P$ is a combination of columns of $P$ and $P$ fixes them), so $PU=U$ and $U^{\mathsf T}P^{\mathsf T}=U^{\mathsf T}$. By symmetry $U^{\mathsf T}P=U^{\mathsf T}$, whence $B=U^{\mathsf T}P=U^{\mathsf T}$ and $P=UU^{\mathsf T}$.

2. If $Pv=\lambda v$ with $v\ne0$ then $\lambda v=P^2v=\lambda^2v$, so $\lambda\in\{0,1\}$. $P$ is symmetric hence diagonalisable, and the number of eigenvalues equal to $1$ is its rank; the trace is the sum of the eigenvalues, so $\operatorname{tr}P=\operatorname{rank}P$. (Alternatively $\operatorname{tr}UU^{\mathsf T}=\operatorname{tr}U^{\mathsf T}U=\operatorname{tr}I_r=r$.)

3. $(I-P)^{\mathsf T}=I-P$ and $(I-P)^2=I-2P+P^2=I-P$.

4. $\|y\|^2=\|Py\|^2+\|(I-P)y\|^2+2y^{\mathsf T}P(I-P)y$ and $P(I-P)=P-P^2=0$.

:::

::: {#thm-gaussian-projection .theorem name="Projection of spherical Gaussian noise"}

Let $\varepsilon\sim N_n(0,\sigma^2I_n)$ and let $P$ be an orthogonal projection matrix of rank $r$. Then

1. $P\varepsilon\sim N_n(0,\sigma^2P)$ and $(I-P)\varepsilon\sim N_n(0,\sigma^2(I-P))$ are independent;
2. $\|P\varepsilon\|^2/\sigma^2\sim\chi^2_r$ and $\|(I-P)\varepsilon\|^2/\sigma^2\sim\chi^2_{n-r}$.

:::

::: {.proof}

1. Write $P=UU^{\mathsf T}$ with $U\in\mathbb R^{n\times r}$ (@prp-projection-rank-trace), and complete $U$ by a matrix $V\in\mathbb R^{n\times(n-r)}$ to an orthogonal matrix $Q=(U\ V)$; the columns of $V$ span $\operatorname{col}(P)^\perp$, and $I-P=VV^{\mathsf T}$.

2. By @thm-jointly-gaussian-properties (part 2), $Q^{\mathsf T}\varepsilon\sim N(0,\sigma^2Q^{\mathsf T}Q)=N(0,\sigma^2I_n)$. Its first $r$ coordinates $U^{\mathsf T}\varepsilon$ and last $n-r$ coordinates $V^{\mathsf T}\varepsilon$ are therefore independent, each a vector of iid $N(0,\sigma^2)$ variables.

3. $P\varepsilon=U(U^{\mathsf T}\varepsilon)$ and $(I-P)\varepsilon=V(V^{\mathsf T}\varepsilon)$ are functions of these two independent vectors, hence independent. Their covariances are $\sigma^2UU^{\mathsf T}=\sigma^2P$ and $\sigma^2(I-P)$.

4. Since $U$ has orthonormal columns, $\|P\varepsilon\|^2=\|U^{\mathsf T}\varepsilon\|^2$, a sum of $r$ squares of independent $N(0,\sigma^2)$ variables; divided by $\sigma^2$ it is $\chi^2_r$ (@prp-chi-square-gamma). The same argument gives $\chi^2_{n-r}$.

:::

::: {#fig-gaussian-projections-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\fill[faint, opacity=0.25] (-0.5,0) -- (5,0) -- (6,1.2) -- (0.5,1.2) -- cycle;
\node[lab] at (5.2,0.3) {$\operatorname{col}(P)$};
\node[small vertex] (O) at (2.5,0.5) {};
\node[lab, below] at (2.5,0.45) {$0$};
\node[hl dot] (E) at (4.2,2.4) {};
\node[lab, above right] at (4.2,2.4) {$\varepsilon$};
\node[small vertex] (PE) at (4.2,0.9) {};
\draw[emph] (2.5,0.5) -- (4.2,0.9);
\draw[hl] (4.2,0.9) -- (4.2,2.4);
\node[lab, left] at (4.1,1.7) {$(I-P)\varepsilon$};
\node[lab, below right] at (3.9,0.75) {$P\varepsilon$};
\draw[->, emph] (2.5,0.5) -- (4.2,2.4);
\end{tikzpicture}
\end{center}
```

The noise vector $\varepsilon$ splits into its component $P\varepsilon$ in the subspace and the orthogonal remainder $(I-P)\varepsilon$. For Gaussian noise the two components are independent and the squared lengths are $\sigma^2\chi^2$ with $r$ and $n-r$ degrees of freedom.

:::

::: {#exm-projection-sample-variance .example name="The sample mean and variance as projections"}

Let $X_1,\dots,X_n$ be iid $N(\mu,\sigma^2)$ and write $X=\mu\mathbf 1+\varepsilon$ with $\mathbf 1=(1,\dots,1)^{\mathsf T}$. Let $P=\mathbf 1\mathbf 1^{\mathsf T}/n$, the projection onto $\operatorname{span}(\mathbf 1)$, of rank $1$.

1. $PX=\bar X\mathbf 1$ and $(I-P)X=(X_i-\bar X)_i$; the second does not depend on $\mu$ since $(I-P)\mathbf 1=0$, so $(I-P)X=(I-P)\varepsilon$.

2. By @thm-gaussian-projection, $\bar X$ is independent of $S_{XX}=\sum_i(X_i-\bar X)^2=\|(I-P)\varepsilon\|^2$, and $S_{XX}/\sigma^2\sim\chi^2_{n-1}$.

This recovers @thm-normal-sample-theory, and with it the $t$ statistic $\sqrt n(\bar X-\mu)/\sqrt{S_{XX}/(n-1)}\sim t_{n-1}$.

:::
