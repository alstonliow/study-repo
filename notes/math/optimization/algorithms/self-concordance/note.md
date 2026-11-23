---
title: "Self-Concordant Functions"
sources: [ee364a-10]
requires: [math/optimization/algorithms/newtons-method-for-minimization]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on unconstrained minimization, in our own wording; proofs written out in steps; the convergence theorem is stated without proof. -->

The classical analysis of Newton's method depends on constants $m$, $M$, $L$ that change under a change of coordinates, although the method does not. Self-concordance is an affine-invariant condition that gives an iteration bound with no unknown constants, and it covers the logarithmic barriers used by interior-point methods.

::: {#def-self-concordant .definition name="Self-concordant function"}

A convex $f:\mathbb{R}\to\mathbb{R}$ is *self-concordant* if
$$\lvert f'''(x)\rvert\le2f''(x)^{3/2}\qquad\text{for all }x\in\operatorname{dom}f.$$
A convex $f:\mathbb{R}^n\to\mathbb{R}$ is self-concordant if its restriction $g(t)=f(x+tv)$ to every line is.

:::

::: {#fig-self-concordance-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) -- (2.4,-0.3) -- (3.2,1) -- (2.3,2.3) -- (0.3,1.9) -- cycle;
\draw[emph] (0,0) -- (2.4,-0.3) -- (3.2,1) -- (2.3,2.3) -- (0.3,1.9) -- cycle;
\draw[hl] (0.51,0.68) -- (0.52,0.62) -- (0.55,0.56) -- (0.58,0.5) -- (0.62,0.45) -- (0.66,0.39) -- (0.71,0.35) -- (0.76,0.3) -- (0.82,0.27) -- (0.88,0.23) -- (0.94,0.2) -- (1.01,0.18) -- (1.08,0.16) -- (1.16,0.15) -- (1.23,0.14) -- (1.31,0.14) -- (1.39,0.14) -- (1.46,0.15) -- (1.54,0.17) -- (1.61,0.19) -- (1.69,0.21) -- (1.76,0.24) -- (1.82,0.28) -- (1.89,0.32) -- (1.95,0.36) -- (2,0.41) -- (2.06,0.46) -- (2.1,0.52) -- (2.14,0.58) -- (2.18,0.64) -- (2.2,0.7) -- (2.23,0.76) -- (2.24,0.83) -- (2.25,0.89) -- (2.25,0.96) -- (2.25,1.02) -- (2.24,1.08) -- (2.22,1.15) -- (2.19,1.2) -- (2.16,1.26) -- (2.13,1.32) -- (2.08,1.37) -- (2.04,1.41) -- (1.98,1.46) -- (1.93,1.49) -- (1.86,1.53) -- (1.8,1.56) -- (1.73,1.58) -- (1.66,1.6) -- (1.58,1.61) -- (1.51,1.62) -- (1.43,1.62) -- (1.36,1.62) -- (1.28,1.61) -- (1.2,1.59) -- (1.13,1.57) -- (1.06,1.55) -- (0.99,1.52) -- (0.92,1.48) -- (0.85,1.44) -- (0.79,1.4) -- (0.74,1.35) -- (0.69,1.3) -- (0.64,1.24) -- (0.6,1.18) -- (0.57,1.12) -- (0.54,1.06) -- (0.52,1) -- (0.5,0.93) -- (0.49,0.87) -- (0.49,0.8) -- (0.49,0.74) -- (0.51,0.68) -- cycle;
\fill[ink] (1.37,0.88) circle[pt];
\draw[hl] (2.04,-0.09) -- (2.06,-0.11) -- (2.09,-0.12) -- (2.12,-0.13) -- (2.15,-0.13) -- (2.19,-0.13) -- (2.22,-0.13) -- (2.26,-0.12) -- (2.3,-0.11) -- (2.34,-0.09) -- (2.38,-0.07) -- (2.42,-0.05) -- (2.46,-0.02) -- (2.5,0.01) -- (2.54,0.04) -- (2.58,0.07) -- (2.61,0.11) -- (2.65,0.15) -- (2.68,0.19) -- (2.71,0.24) -- (2.74,0.28) -- (2.76,0.33) -- (2.79,0.37) -- (2.81,0.42) -- (2.82,0.46) -- (2.84,0.51) -- (2.85,0.56) -- (2.85,0.6) -- (2.86,0.64) -- (2.86,0.68) -- (2.85,0.72) -- (2.85,0.76) -- (2.84,0.79) -- (2.82,0.82) -- (2.81,0.85) -- (2.79,0.87) -- (2.76,0.89) -- (2.74,0.91) -- (2.71,0.92) -- (2.68,0.93) -- (2.65,0.93) -- (2.61,0.93) -- (2.58,0.93) -- (2.54,0.92) -- (2.5,0.91) -- (2.46,0.89) -- (2.42,0.87) -- (2.38,0.85) -- (2.34,0.82) -- (2.3,0.79) -- (2.26,0.76) -- (2.22,0.73) -- (2.19,0.69) -- (2.15,0.65) -- (2.12,0.61) -- (2.09,0.56) -- (2.06,0.52) -- (2.04,0.47) -- (2.01,0.43) -- (1.99,0.38) -- (1.98,0.34) -- (1.96,0.29) -- (1.95,0.24) -- (1.95,0.2) -- (1.94,0.16) -- (1.94,0.12) -- (1.95,0.08) -- (1.95,0.04) -- (1.96,0.01) -- (1.98,-0.02) -- (1.99,-0.05) -- (2.01,-0.07) -- (2.04,-0.09) -- cycle;
\fill[ink] (2.4,0.4) circle[pt];
\draw[hl] (0.37,1.08) -- (0.4,1.07) -- (0.43,1.06) -- (0.45,1.05) -- (0.48,1.05) -- (0.52,1.05) -- (0.55,1.06) -- (0.58,1.06) -- (0.61,1.08) -- (0.64,1.09) -- (0.68,1.11) -- (0.71,1.13) -- (0.74,1.15) -- (0.77,1.18) -- (0.79,1.21) -- (0.82,1.24) -- (0.85,1.27) -- (0.87,1.31) -- (0.89,1.34) -- (0.91,1.38) -- (0.93,1.42) -- (0.94,1.46) -- (0.95,1.5) -- (0.96,1.54) -- (0.97,1.57) -- (0.97,1.61) -- (0.97,1.65) -- (0.97,1.69) -- (0.96,1.72) -- (0.95,1.75) -- (0.94,1.79) -- (0.93,1.82) -- (0.91,1.84) -- (0.9,1.87) -- (0.88,1.89) -- (0.85,1.91) -- (0.83,1.92) -- (0.8,1.93) -- (0.77,1.94) -- (0.75,1.95) -- (0.72,1.95) -- (0.68,1.95) -- (0.65,1.94) -- (0.62,1.94) -- (0.59,1.92) -- (0.56,1.91) -- (0.52,1.89) -- (0.49,1.87) -- (0.46,1.85) -- (0.43,1.82) -- (0.41,1.79) -- (0.38,1.76) -- (0.35,1.73) -- (0.33,1.69) -- (0.31,1.66) -- (0.29,1.62) -- (0.27,1.58) -- (0.26,1.54) -- (0.25,1.5) -- (0.24,1.46) -- (0.23,1.43) -- (0.23,1.39) -- (0.23,1.35) -- (0.23,1.31) -- (0.24,1.28) -- (0.25,1.25) -- (0.26,1.21) -- (0.27,1.18) -- (0.29,1.16) -- (0.3,1.13) -- (0.32,1.11) -- (0.35,1.09) -- (0.37,1.08) -- cycle;
\fill[ink] (0.6,1.5) circle[pt];
\draw[hl] (1.15,1.74) -- (1.15,1.7) -- (1.16,1.67) -- (1.18,1.64) -- (1.2,1.61) -- (1.22,1.59) -- (1.25,1.56) -- (1.29,1.54) -- (1.32,1.51) -- (1.36,1.49) -- (1.41,1.48) -- (1.45,1.46) -- (1.5,1.45) -- (1.56,1.44) -- (1.61,1.43) -- (1.67,1.43) -- (1.72,1.43) -- (1.78,1.43) -- (1.84,1.43) -- (1.89,1.44) -- (1.95,1.45) -- (2,1.46) -- (2.06,1.48) -- (2.11,1.49) -- (2.16,1.51) -- (2.2,1.54) -- (2.25,1.56) -- (2.29,1.59) -- (2.32,1.61) -- (2.36,1.64) -- (2.38,1.67) -- (2.41,1.7) -- (2.43,1.74) -- (2.44,1.77) -- (2.45,1.8) -- (2.45,1.83) -- (2.45,1.86) -- (2.45,1.9) -- (2.44,1.93) -- (2.42,1.96) -- (2.4,1.99) -- (2.38,2.01) -- (2.35,2.04) -- (2.31,2.06) -- (2.28,2.09) -- (2.24,2.11) -- (2.19,2.12) -- (2.15,2.14) -- (2.1,2.15) -- (2.04,2.16) -- (1.99,2.17) -- (1.93,2.17) -- (1.88,2.17) -- (1.82,2.17) -- (1.76,2.17) -- (1.71,2.16) -- (1.65,2.15) -- (1.6,2.14) -- (1.54,2.12) -- (1.49,2.11) -- (1.44,2.09) -- (1.4,2.06) -- (1.35,2.04) -- (1.31,2.01) -- (1.28,1.99) -- (1.24,1.96) -- (1.22,1.93) -- (1.19,1.9) -- (1.17,1.86) -- (1.16,1.83) -- (1.15,1.8) -- (1.15,1.77) -- (1.15,1.74) -- cycle;
\fill[ink] (1.8,1.8) circle[pt];
\end{tikzpicture}
\end{center}
```

Dikin ellipsoids $\{y\mid(y-x)^{\mathsf T}\nabla^2\phi(x)(y-x)<1\}$ of the self-concordant log barrier $\phi$ of a pentagon at four points. Each lies inside the domain, and they shrink and flatten near the boundary: the Hessian measures distance to the boundary in its own geometry.

:::

::: {#exm-self-concordant .example name="Self-concordant functions"}

1. Linear and convex quadratic functions ($f'''=0$).

2. $f(x)=-\log x$: $f''=1/x^2$, $f'''=-2/x^3$, so $\lvert f'''\rvert=2(f'')^{3/2}$, with equality.

3. $f(x)=x\log x-\log x$ on $x>0$: $f''=\frac{x+1}{x^2}$, $f'''=-\frac{x+2}{x^3}$; then $\frac{\lvert f'''\rvert}{(f'')^{3/2}}=\frac{x+2}{(x+1)^{3/2}}\le2$ for $x>0$.

:::

::: {#prp-self-concordant-calculus .proposition name="Self-concordant calculus"}

1. If $f$ is self-concordant and $a\ge1$, then $af$ is self-concordant.

2. Sums of self-concordant functions are self-concordant.

3. If $f$ is self-concordant, so is $f(Ax+b)$.

Hence the log barrier $-\sum_{i=1}^m\log(b_i-a_i^{\mathsf T}x)$ on $\{x\mid a_i^{\mathsf T}x<b_i\}$ and $-\log\det X$ on $\mathbb S^n_{++}$ are self-concordant.

:::

::: {.proof}

1. $\lvert af'''\rvert\le2a(f'')^{3/2}=2a^{-1/2}(af'')^{3/2}\le2(af'')^{3/2}$ for $a\ge1$.

2. For $f_1+f_2$ on a line: $\lvert f_1'''+f_2'''\rvert\le2\big((f_1'')^{3/2}+(f_2'')^{3/2}\big)\le2(f_1''+f_2'')^{3/2}$, since $u^{3/2}+v^{3/2}\le(u+v)^{3/2}$ for $u,v\ge0$.

3. A line in $x$ maps to a line in $Ax+b$, so the restriction of $f(Ax+b)$ to a line is a restriction of $f$ to a line.

4. Each term $-\log(b_i-a_i^{\mathsf T}x)$ is $-\log$ composed with an affine map. For $-\log\det(X+tV)=-\log\det X-\sum_i\log(1+t\lambda_i)$ (as in @exm-log-det-concave), each term is $-\log$ of an affine function of $t$.

:::

::: {#thm-self-concordant-newton .theorem name="Convergence for self-concordant functions"}

If $f$ is self-concordant and strictly convex with closed sublevel sets, Newton's method with backtracking line search ($\alpha,\beta$ fixed) reaches $f(x)-p^\star\le\epsilon$ in at most
$$\frac{f(x^{(0)})-p^\star}{\gamma}+\log_2\log_2(1/\epsilon)$$
iterations, where $\gamma=\frac{\alpha\beta(1-2\alpha)^2}{20-8\alpha}$ depends only on the line search parameters. There are two phases: while $\lambda(x)>\eta=(1-2\alpha)/4$, each step decreases $f$ by at least $\gamma$; once $\lambda(x)\le\eta$, full steps are taken and $2\lambda(x^+)\le(2\lambda(x))^2$.

:::

::: {#fig-self-concordance-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (4.4,0) node[lab, right] {$k$};
\draw[->, faint] (0,-2.6) -- (0,0.9) node[lab, above] {};
\draw[hl] (0,0.24) -- (0.4,0.19) -- (0.8,0.04) -- (1.2,-0.03) -- (1.6,-0.14) -- (2,-0.31) -- (2.4,-0.62) -- (2.8,-1.21) -- (3.2,-2.37) -- (3.6,-2.4) -- (4,-2.4) -- (4.4,-2.4) -- (4.8,-2.4) -- (5.2,-2.4);
\fill[ink] (0,0.24) circle[pt];
\fill[ink] (0.4,0.19) circle[pt];
\fill[ink] (0.8,0.04) circle[pt];
\fill[ink] (1.2,-0.03) circle[pt];
\fill[ink] (1.6,-0.14) circle[pt];
\fill[ink] (2,-0.31) circle[pt];
\fill[ink] (2.4,-0.62) circle[pt];
\fill[ink] (2.8,-1.21) circle[pt];
\fill[ink] (3.2,-2.37) circle[pt];
\fill[ink] (3.6,-2.4) circle[pt];
\fill[ink] (4,-2.4) circle[pt];
\fill[ink] (4.4,-2.4) circle[pt];
\fill[ink] (4.8,-2.4) circle[pt];
\fill[ink] (5.2,-2.4) circle[pt];
\node[lab, tick, left] at (0,0) {$10^0$};
\node[lab, tick, left] at (0,-2) {$10^{-10}$};
\draw[faint, dashed] (0,-2) -- (4.2,-2);
\node[lab] at (3,-1.4) {$f(x^{(k)})-p^\star$};
\end{tikzpicture}
\end{center}
```

Damped Newton on the self-concordant $c^{\mathsf T}x+\phi(x)$ ($\phi$ the pentagon's log barrier). While $\lambda(x)>\eta$ each step decreases $f$ by at least a fixed amount; once $\lambda(x)\le\eta$ full steps are taken and the error falls quadratically, reaching machine precision a few steps later.

:::

::: {#rmk-self-concordance-1 .remark name="About the theorem"}

We state @thm-self-concordant-newton without proof. The bound is affine invariant, and in practice it is very pessimistic: the constant $1/\gamma$ is about $375$ for $\alpha=0.1$, $\beta=0.8$, while observed iteration counts are small (often under $20$). Its value is that the count depends only on the initial suboptimality, which interior-point complexity bounds exploit (@sec-math-optimization-algorithms-phase-one-and-complexity).

:::

::: {#prp-self-concordant-gap .proposition name="Newton decrement bounds the gap"}

For strictly convex self-concordant $f$ and $\lambda(x)\le0.68$,
$$p^\star\ge f(x)-\lambda(x)^2.$$

:::

::: {.proof}

We state this bound without proof; it follows from integrating the self-concordance inequality along the Newton direction. It justifies the stopping rule $\lambda^2\le\epsilon$ for self-concordant functions.

:::
