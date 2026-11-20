---
title: "Differential Equations and exp(At)"
sources: [mit1806-23]
requires: [math/linear-algebra/eigenvalues/diagonalization]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 23, in our own wording; proofs written out in steps. Example numbers checked with sympy. -->

A system of linear differential equations $\frac{d\mathbf{u}}{dt}=A\mathbf{u}$ with constant $A$ is solved by eigenvalues, as difference equations were (@cor-powers-and-difference-equations), with powers $\lambda^k$ replaced by exponentials $e^{\lambda t}$.

::: {#thm-pure-exponential-solutions .theorem name="Eigenvectors give exponential solutions"}

If $A\mathbf{x}=\lambda\mathbf{x}$, then $\mathbf{u}(t)=e^{\lambda t}\mathbf{x}$ solves $\frac{d\mathbf{u}}{dt}=A\mathbf{u}$. If $A$ has $n$ independent eigenvectors, the solution with $\mathbf{u}(0)=\mathbf{u}_0=c_1\mathbf{x}_1+\dots+c_n\mathbf{x}_n$ is
$$\mathbf{u}(t)=c_1e^{\lambda_1t}\mathbf{x}_1+\dots+c_ne^{\lambda_nt}\mathbf{x}_n.$$

:::

::: {.proof}

1. $\frac{d}{dt}e^{\lambda t}\mathbf{x}=\lambda e^{\lambda t}\mathbf{x}=e^{\lambda t}A\mathbf{x}=A(e^{\lambda t}\mathbf{x})$.

2. The equation is linear, so the combination is a solution, and at $t=0$ it equals $\mathbf{u}_0$.

3. Uniqueness: in the coordinates $\mathbf{v}=S^{-1}\mathbf{u}$ the system decouples into $\frac{dv_i}{dt}=\lambda_iv_i$, whose only solutions are $v_i(0)e^{\lambda_it}$.

:::

::: {#exm-two-tanks .example name="A coupled system"}

Take $\frac{du_1}{dt}=-2u_1+u_2$, $\frac{du_2}{dt}=u_1-2u_2$, $\mathbf{u}(0)=(1,0)$. The matrix $A=\begin{bmatrix}-2&1\\1&-2\end{bmatrix}$ has $\lambda_1=-1$ with $\mathbf{x}_1=(1,1)$ and $\lambda_2=-3$ with $\mathbf{x}_2=(1,-1)$. Since $(1,0)=\frac12\mathbf{x}_1+\frac12\mathbf{x}_2$,
$$\mathbf{u}(t)=\tfrac12e^{-t}(1,1)+\tfrac12e^{-3t}(1,-1).$$
Both terms decay, so $\mathbf{u}(t)\to\mathbf{0}$.

:::

::: {#fig-linear-differential-equations-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=3]
\draw[->] (-0.3,0) -- (1.25,0) node[lab, right] {$u_1$};
\draw[->] (0,-0.55) -- (0,0.85) node[lab, above] {$u_2$};
\draw[faint, dashed] (-0.2,-0.2) -- (0.8,0.8) node[lab, above] {$\mathbf x_1=(1,1)$};
\draw[faint, dashed] (-0.25,0.25) -- (0.5,-0.5) node[lab, right] {$\mathbf x_2=(1,-1)$};
\draw[hl, ->] plot[domain=0:3, samples=80] ({0.5*exp(-\x)+0.5*exp(-3*\x)},{0.5*exp(-\x)-0.5*exp(-3*\x)});
\node[dot] at (1,0) {};
\node[lab, below] at (1,0) {$\mathbf u(0)$};
\end{tikzpicture}
\end{center}
```

The solution of @exm-two-tanks in the $(u_1,u_2)$-plane. It starts at $(1,0)$; the $e^{-3t}$ part along $\mathbf x_2$ dies out first, so the path turns towards the slower eigenvector $\mathbf x_1$ and then decays to $\mathbf 0$ along it.

:::

::: {#thm-stability-of-linear-systems .theorem name="Stability"}

For diagonalizable $A$, every solution of $\frac{d\mathbf{u}}{dt}=A\mathbf{u}$ tends to $\mathbf{0}$ if and only if every eigenvalue has negative real part. If some $\operatorname{Re}\lambda>0$, some solutions blow up. A steady state $\mathbf{u}(t)\to c\,\mathbf{x}_1$ occurs when $\lambda_1=0$ and all other eigenvalues have negative real part.

:::

::: {.proof}

1. Write $\lambda=a+ib$. Then $\lvert e^{\lambda t}\rvert=e^{at}\lvert e^{ibt}\rvert=e^{at}$, since $\lvert e^{ibt}\rvert=\lvert\cos bt+i\sin bt\rvert=1$.

2. In the formula of @thm-pure-exponential-solutions each term tends to $\mathbf{0}$ iff its $a<0$, and a term with $a>0$ grows without bound when its $c_i\ne0$.

3. With $\lambda_1=0$ the first term is the constant $c_1\mathbf{x}_1$ and the others decay.

:::

For $2\times2$ real matrices: both eigenvalues have negative real part exactly when $\operatorname{tr}A<0$ and $\det A>0$.

::: {#def-matrix-exponential .definition name="Matrix exponential"}

For an $n\times n$ matrix $A$,
$$e^{At}=I+At+\frac{(At)^2}{2!}+\frac{(At)^3}{3!}+\cdots.$$
The series converges for every $A$ and $t$, and $\frac{d}{dt}e^{At}=Ae^{At}$, so $\mathbf{u}(t)=e^{At}\mathbf{u}_0$ solves $\frac{d\mathbf{u}}{dt}=A\mathbf{u}$ even when $A$ has too few eigenvectors.

:::

::: {#prp-exponential-diagonalizable .proposition name="exp(At) for diagonalizable A"}

If $A=S\Lambda S^{-1}$, then
$$e^{At}=Se^{\Lambda t}S^{-1},\qquad e^{\Lambda t}=\operatorname{diag}(e^{\lambda_1t},\dots,e^{\lambda_nt}).$$

:::

::: {.proof}

1. $(At)^k=S(\Lambda t)^kS^{-1}$ by @thm-diagonalization.

2. Summing the series term by term, $e^{At}=S\big(\sum_k(\Lambda t)^k/k!\big)S^{-1}$, and the series for a diagonal matrix is the diagonal matrix of scalar exponentials.

:::

::: {#rmk-linear-differential-equations-1 .remark name="Second-order equations"}

The equation $y''+by'+ky=0$ becomes a first-order system for $\mathbf{u}=(y',y)$:
$$\frac{d}{dt}\begin{bmatrix}y'\\y\end{bmatrix}=\begin{bmatrix}-b&-k\\1&0\end{bmatrix}\begin{bmatrix}y'\\y\end{bmatrix}.$$
The eigenvalues solve $\lambda^2+b\lambda+k=0$, the same equation as for trying $y=e^{\lambda t}$ directly.

:::
