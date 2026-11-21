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
