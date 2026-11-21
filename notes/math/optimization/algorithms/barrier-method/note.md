---
title: "The Barrier Method"
sources: [ee364a-12]
requires: [math/optimization/algorithms/equality-constrained-minimization, math/optimization/algorithms/self-concordance]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on interior-point methods, in our own wording; proofs written out in steps. The example central path was computed in Python. -->

Inequality constraints are handled by a logarithmic barrier that blows up at the boundary. Minimizing the objective plus a scaled barrier traces the central path, which leads to the solution; the barrier method follows it with Newton's method.

::: {#def-log-barrier .definition name="Logarithmic barrier, central path"}

For the convex problem minimize $f_0(x)$ subject to $f_i(x)\le0$, $Ax=b$, with a strictly feasible point, the *logarithmic barrier* is
$$\phi(x)=-\sum_{i=1}^m\log(-f_i(x)),\qquad\operatorname{dom}\phi=\{x\mid f_i(x)<0\}.$$
For $t>0$ let $x^\star(t)$ solve the *centering problem* minimize $tf_0(x)+\phi(x)$ subject to $Ax=b$. The curve $\{x^\star(t)\mid t>0\}$ is the *central path*.

:::

::: {#thm-central-path-duality-gap .theorem name="Dual points on the central path"}

Each central point gives a dual feasible point with duality gap $m/t$:
$$\lambda_i^\star(t)=-\frac{1}{tf_i(x^\star(t))},\quad\nu^\star(t)=\frac wt,\qquad f_0(x^\star(t))-p^\star\le\frac mt,$$
where $w$ is the multiplier of the centering problem. Hence $x^\star(t)\to$ optimal as $t\to\infty$.

:::

::: {.proof}

1. Optimality for the centering problem: $t\nabla f_0(x^\star)+\sum_i\frac{1}{-f_i(x^\star)}\nabla f_i(x^\star)+A^{\mathsf T}w=0$.

2. Divide by $t$: $\nabla f_0(x^\star)+\sum_i\lambda_i^\star\nabla f_i(x^\star)+A^{\mathsf T}\nu^\star=0$ with $\lambda_i^\star=-1/(tf_i(x^\star))>0$. So $x^\star$ minimizes the convex function $L(\cdot,\lambda^\star,\nu^\star)$.

3. Hence $g(\lambda^\star,\nu^\star)=L(x^\star,\lambda^\star,\nu^\star)=f_0(x^\star)+\sum_i\lambda_i^\star f_i(x^\star)=f_0(x^\star)-m/t$, using $Ax^\star=b$.

4. Weak duality gives $p^\star\ge g(\lambda^\star,\nu^\star)=f_0(x^\star)-m/t$.

:::

::: {#rmk-barrier-method-1 .remark name="Centrality as perturbed KKT"}

The central point satisfies the KKT conditions (@def-kkt-conditions) except that complementary slackness is replaced by $-\lambda_if_i(x)=1/t$. As $t\to\infty$ this approaches $\lambda_if_i(x)=0$.

:::

::: {#def-barrier-method .definition name="Barrier method"}

Given strictly feasible $x$, $t:=t^{(0)}>0$, $\mu>1$ and tolerance $\epsilon>0$, repeat:

1. *Centering*: compute $x^\star(t)$ by Newton's method (@def-newton-step-equality) started at $x$;
2. *Update*: $x:=x^\star(t)$;
3. *Stopping criterion*: quit if $m/t<\epsilon$;
4. *Increase* $t$: $t:=\mu t$.

:::

```{=latex}
\begin{algorithm}
\caption{Barrier method}
\begin{algorithmic}
\INPUT strictly feasible $x$, $t>0$, $\mu>1$, tolerance $\epsilon>0$
\STATE $x\gets\operatorname{argmin}\{tf_0+\phi\mid Ax=b\}$ by Newton's method started at $x$
\WHILE{$m/t\ge\epsilon$}
  \STATE $t\gets\mu t$
  \STATE $x\gets\operatorname{argmin}\{tf_0+\phi\mid Ax=b\}$ by Newton's method started at $x$
\ENDWHILE
\RETURN $x$
\end{algorithmic}
\end{algorithm}
```

::: {#prp-barrier-outer-iterations .proposition name="Number of centering steps"}

The barrier method stops after exactly
$$\Big\lceil\frac{\log(m/(\epsilon t^{(0)}))}{\log\mu}\Big\rceil$$
centering steps (plus the initial one), with $f_0(x)-p^\star<\epsilon$.

:::

::: {.proof}

1. After $k$ updates $t=\mu^kt^{(0)}$, and the test $m/t<\epsilon$ holds once $\mu^k>m/(\epsilon t^{(0)})$.

2. At that point the gap bound of @thm-central-path-duality-gap is $m/t<\epsilon$.

:::

::: {#exm-central-path-lp .example name="Central path of a small LP"}

Take the one-dimensional LP minimize $x$ subject to $0\le x\le1$ ($m=2$). The centering problem minimizes $tx-\log x-\log(1-x)$; setting the derivative $t-1/x+1/(1-x)$ to $0$ gives
$$x^\star(t)=\frac{t+2-\sqrt{t^2+4}}{2t},$$
which decreases from $\frac12$ (as $t\to0$) to $0$. At $t=10$, $x^\star\approx0.0902$ and the gap bound is $m/t=0.2$; the actual gap is $0.0902$.

:::

::: {#rmk-barrier-method-2 .remark name="Choosing $\mu$"}

Large $\mu$ means few centering steps but more Newton steps per centering; small $\mu$ the reverse. In practice $\mu$ between about $10$ and $100$ gives a total of a few dozen Newton steps, nearly independent of problem size.

:::

::: {#rmk-barrier-method-3 .remark editor="No figure: the central path of the one-variable example is the single curve given by the formula, and realistic central paths (LPs with many constraints) are too high-dimensional to draw."}

The duality gap bound $m/t$ is guaranteed, not just observed, which is why the stopping rule of the barrier method needs no estimate of $p^\star$.

:::
