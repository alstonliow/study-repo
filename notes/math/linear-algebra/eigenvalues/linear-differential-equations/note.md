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

::: {#fig-linear-differential-equations-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x={(1cm,0)}, y={(0,2.2cm)}]
\draw[->, muted] (0,0) -- (5.3,0) node[right, lab, tick] {$t$}; \draw[->, muted] (0,0) -- (0,1.2);
\draw[faint] (0,1) -- (-0.1,1) node[left, lab, tick] {$1$};
\draw[emph, primary] (0.000,1.000) -- (0.062,0.884) -- (0.125,0.785) -- (0.188,0.699) -- (0.250,0.626) -- (0.312,0.562) -- (0.375,0.506) -- (0.438,0.457) -- (0.500,0.415) -- (0.562,0.377) -- (0.625,0.344) -- (0.688,0.315) -- (0.750,0.289) -- (0.812,0.266) -- (0.875,0.245) -- (0.938,0.226) -- (1.000,0.209) -- (1.062,0.193) -- (1.125,0.179) -- (1.188,0.167) -- (1.250,0.155) -- (1.312,0.144) -- (1.375,0.135) -- (1.438,0.125) -- (1.500,0.117) -- (1.562,0.109) -- (1.625,0.102) -- (1.688,0.096) -- (1.750,0.090) -- (1.812,0.084) -- (1.875,0.078) -- (1.938,0.074) -- (2.000,0.069) -- (2.062,0.065) -- (2.125,0.061) -- (2.188,0.057) -- (2.250,0.053) -- (2.312,0.050) -- (2.375,0.047) -- (2.438,0.044) -- (2.500,0.041) -- (2.562,0.039) -- (2.625,0.036) -- (2.688,0.034) -- (2.750,0.032) -- (2.812,0.030) -- (2.875,0.028) -- (2.938,0.027) -- (3.000,0.025) -- (3.062,0.023) -- (3.125,0.022) -- (3.188,0.021) -- (3.250,0.019) -- (3.312,0.018) -- (3.375,0.017) -- (3.438,0.016) -- (3.500,0.015) -- (3.562,0.014) -- (3.625,0.013) -- (3.688,0.013) -- (3.750,0.012) -- (3.812,0.011) -- (3.875,0.010) -- (3.938,0.010) -- (4.000,0.009) -- (4.062,0.009) -- (4.125,0.008) -- (4.188,0.008) -- (4.250,0.007) -- (4.312,0.007) -- (4.375,0.006) -- (4.438,0.006) -- (4.500,0.006) -- (4.562,0.005) -- (4.625,0.005) -- (4.688,0.005) -- (4.750,0.004) -- (4.812,0.004) -- (4.875,0.004) -- (4.938,0.004) -- (5.000,0.003);
\draw[emph, accent] (0.000,0.000) -- (0.062,0.055) -- (0.125,0.098) -- (0.188,0.130) -- (0.250,0.153) -- (0.312,0.170) -- (0.375,0.181) -- (0.438,0.188) -- (0.500,0.192) -- (0.562,0.192) -- (0.625,0.191) -- (0.688,0.188) -- (0.750,0.183) -- (0.812,0.178) -- (0.875,0.172) -- (0.938,0.166) -- (1.000,0.159) -- (1.062,0.152) -- (1.125,0.145) -- (1.188,0.138) -- (1.250,0.131) -- (1.312,0.125) -- (1.375,0.118) -- (1.438,0.112) -- (1.500,0.106) -- (1.562,0.100) -- (1.625,0.095) -- (1.688,0.089) -- (1.750,0.084) -- (1.812,0.079) -- (1.875,0.075) -- (1.938,0.071) -- (2.000,0.066) -- (2.062,0.063) -- (2.125,0.059) -- (2.188,0.055) -- (2.250,0.052) -- (2.312,0.049) -- (2.375,0.046) -- (2.438,0.043) -- (2.500,0.041) -- (2.562,0.038) -- (2.625,0.036) -- (2.688,0.034) -- (2.750,0.032) -- (2.812,0.030) -- (2.875,0.028) -- (2.938,0.026) -- (3.000,0.025) -- (3.062,0.023) -- (3.125,0.022) -- (3.188,0.021) -- (3.250,0.019) -- (3.312,0.018) -- (3.375,0.017) -- (3.438,0.016) -- (3.500,0.015) -- (3.562,0.014) -- (3.625,0.013) -- (3.688,0.013) -- (3.750,0.012) -- (3.812,0.011) -- (3.875,0.010) -- (3.938,0.010) -- (4.000,0.009) -- (4.062,0.009) -- (4.125,0.008) -- (4.188,0.008) -- (4.250,0.007) -- (4.312,0.007) -- (4.375,0.006) -- (4.438,0.006) -- (4.500,0.006) -- (4.562,0.005) -- (4.625,0.005) -- (4.688,0.005) -- (4.750,0.004) -- (4.812,0.004) -- (4.875,0.004) -- (4.938,0.004) -- (5.000,0.003);
\node[lab, note, primary] at (0.9,0.75) {$u_1(t)$}; \node[lab, note, accent] at (1.4,0.35) {$u_2(t)$};
\end{tikzpicture}
\end{center}
```

The two components of the solution in @exm-two-tanks. The fast mode $e^{-3t}$ evens out the difference between $u_1$ and $u_2$ quickly; after that both decay together like $\frac12e^{-t}$.

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

::: {#fig-linear-differential-equations-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[x={(0.6cm,0)}]
\fill[tintC] (-2.4,-1.4) rectangle (0,1.4);
\fill[tintB] (0,-1.4) rectangle (1.6,1.4);
\draw[->, muted] (-2.5,0) -- (1.8,0) node[right, lab, tick] {$\operatorname{Re}\lambda$}; \draw[->, muted] (0,-1.5) -- (0,1.6) node[above, lab, tick] {$\operatorname{Im}\lambda$};
\fill[ink] (-0.6,0) circle[pt] node[above, lab, tick] {$-1$}; \fill[ink] (-1.8,0) circle[pt] node[above, lab, tick] {$-3$};
\node[lab, note, secondary] at (-1.2,-1.1) {decay}; \node[lab, note, accent] at (0.8,-1.1) {growth};
\node[lab, note, anchor=west] at (2.0,0.8) {$e^{\lambda t}=e^{(\operatorname{Re}\lambda)t}e^{i(\operatorname{Im}\lambda)t}$:};
\node[lab, note, anchor=west] at (2.0,0.3) {only the real part changes the size};
\end{tikzpicture}
\end{center}
```

Stability is decided by where the eigenvalues lie in the complex plane: all in the open left half-plane means every solution decays. The eigenvalues $-1$ and $-3$ of @exm-two-tanks are marked; the imaginary part only makes solutions oscillate.

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
