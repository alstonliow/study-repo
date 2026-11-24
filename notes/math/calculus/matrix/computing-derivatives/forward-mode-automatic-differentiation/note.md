---
title: "Forward-Mode Automatic Differentiation and Dual Numbers"
sources: [mit18s096-8]
requires: [math/calculus/matrix/computing-derivatives/newtons-method-for-systems]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.S096 Matrix Calculus (IAP 2023), course notes Chapter 8, Sections 8.1-8.2 (automatic differentiation via dual numbers, the Babylonian square root, easy forward mode, naive symbolic differentiation), in our own wording; the iteration table is ours, run in Python; proofs written out in steps. -->

*Automatic differentiation* (AD) computes exact derivatives of a program, not of a formula: it applies the chain rule to each elementary operation as the program runs. Forward mode carries, next to every value, its derivative in one chosen direction. The cleanest way to say this is with dual numbers.

::: {#def-dual-numbers .definition name="Dual numbers"}

A *dual number* is a formal expression $a+b\,\epsilon$ with $a,b\in\mathbb{R}$ and the rule $\epsilon^2=0$. Hence

$$
(a+b\epsilon)\pm(c+d\epsilon)=(a\pm c)+(b\pm d)\epsilon,\qquad (a+b\epsilon)(c+d\epsilon)=ac+(ad+bc)\epsilon,
$$

$$
\frac{a+b\epsilon}{c+d\epsilon}=\frac ac+\frac{bc-ad}{c^2}\,\epsilon\quad(c\neq0),
$$

and a smooth function $g$ is extended by $g(a+b\epsilon)=g(a)+g'(a)\,b\,\epsilon$.

:::

The rules are exactly the differential rules: $b$ plays the role of $da$, and $\epsilon^2=0$ drops the second-order terms. The division rule follows from $(c+d\epsilon)\bigl(\tfrac ac+\tfrac{bc-ad}{c^2}\epsilon\bigr)=a+b\epsilon$.

::: {#thm-dual-numbers-differentiate .theorem name="Programs on dual numbers compute derivatives"}

Let a program compute $y=f(x)$ from $x\in\mathbb{R}$ by a finite sequence of the operations $+,-,\times,\div$ and smooth elementary functions $g$. Running the same program on the input $x+1\cdot\epsilon$ with the rules of @def-dual-numbers produces

$$
f(x)+f'(x)\,\epsilon .
$$

:::

```{=latex}
\begin{algorithm}
\caption{Forward-mode differentiation with dual numbers}
\begin{algorithmic}
\INPUT a program computing $v_N=f(x)$ through $v_1,\dots,v_N$; a point $x$
\STATE $(v_0,\dot v_0)\gets(x,1)$
\FOR{$j=1$ \TO $N$}
  \STATE $v_j\gets\phi_j(\text{parents})$
  \STATE $\dot v_j\gets\sum_{\text{parents }u}\frac{\partial\phi_j}{\partial u}\,\dot u$ \COMMENT{the $\epsilon$-part rules}
\ENDFOR
\RETURN $(v_N,\dot v_N)=(f(x),f'(x))$
\end{algorithmic}
\end{algorithm}
```

::: {.proof}

1. Call the intermediate values $v_1,\dots,v_N$, each computed from earlier values (or $x$) by one operation, with $v_N=y$. Claim: on dual input each $v_j$ becomes $v_j+v_j'\epsilon$, where $v_j'=dv_j/dx$.

2. The input $x+1\epsilon$ satisfies the claim since $dx/dx=1$.

3. Suppose the claim holds for all earlier values. If $v_j=v_a v_b$, then $(v_a+v_a'\epsilon)(v_b+v_b'\epsilon)=v_av_b+(v_a'v_b+v_av_b')\epsilon$, and $v_a'v_b+v_av_b'$ is $dv_j/dx$ by the product rule. The cases $\pm$ and $\div$ are the sum and quotient rules.

4. If $v_j=g(v_a)$, then $g(v_a+v_a'\epsilon)=g(v_a)+g'(v_a)v_a'\epsilon$, and $g'(v_a)v_a'$ is $dv_j/dx$ by the chain rule.

5. By induction the claim holds for $v_N=f(x)$.

:::

::: {#exm-babylonian-square-root-dual .example name="Differentiating the Babylonian square root"}

The program $t_0=1$, $t_{k+1}=\tfrac12\bigl(t_k+x/t_k\bigr)$ computes $\sqrt x$ (it is Newton's method for $t^2-x=0$). Run it on $x+\epsilon$ for $x=2$ and write $t_k+t_k'\epsilon$:

| $k$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|---|
| $t_k$ | $1$ | $1.5$ | $1.4166667$ | $1.4142157$ | $1.4142136$ |
| $t_k'$ | $0$ | $0.5$ | $0.3611111$ | $0.3535659$ | $0.3535534$ |

The dual parts follow $t_{k+1}'=\tfrac12\bigl(t_k'+(t_k-x\,t_k')/t_k^2\bigr)$, by the division rule. They converge to $1/(2\sqrt2)=0.35355339\ldots$, the derivative of $\sqrt x$ at $2$, although no line of the program mentions a square root or its derivative.

:::

::: {#fig-forward-mode-automatic-differentiation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\node[box] (x) at (0,0) {$x+1\epsilon$};
\node[box] (a) at (3,0.8) {$x/t_k+(\cdots)\epsilon$};
\node[box] (b) at (3,-0.8) {$t_k+t_k'\epsilon$};
\node[hl box] (c) at (6.6,0) {$t_{k+1}+t_{k+1}'\epsilon$};
\draw[map] (x) -- (a); \draw[map] (b) -- (a);
\draw[map] (a) -- node[lab, above] {$\tfrac12(\cdot+\cdot)$} (c); \draw[map] (b) -- (c);
\draw[map, faint] (c) to[bend left=30] node[lab, below] {next iteration} (b);
\end{tikzpicture}
\end{center}
```

Forward mode in one loop iteration: every value travels together with its derivative, and each operation updates both parts at once. The cost is a small constant times the cost of the program itself.

:::

::: {#prp-forward-mode-jvp .proposition name="Forward mode gives Jacobian–vector products"}

Let $f:\mathbb{R}^n\to\mathbb{R}^m$ be computed by a program as in @thm-dual-numbers-differentiate, and $v\in\mathbb{R}^n$. Running the program on the input $x+v\,\epsilon$ (dual part $v_i$ in component $i$) gives $f(x)+J(x)v\,\epsilon$. Computing the full Jacobian this way takes $n$ runs, one for each $v=e_i$.

:::

::: {.proof}

1. Restrict $f$ to the line $\alpha\mapsto x+\alpha v$. By @thm-dual-numbers-differentiate applied to this one-variable program, the output is $f(x)+\frac{d}{d\alpha}f(x+\alpha v)\big|_0\,\epsilon$.

2. By @def-directional-derivative-operator that derivative is $f'(x)[v]=J(x)v$.

3. Column $i$ of $J$ is $Je_i$, so $n$ runs give all columns.

:::

::: {#rmk-forward-mode-automatic-differentiation-1 .remark name="Why not symbolic differentiation"}

Differentiating a program symbolically, by writing out the formula for $t_k$ as an expression in $x$ and differentiating it, makes the expressions grow quickly: $t_3$ is already a nested rational function, and its derivative written out has many repeated subexpressions. AD never builds the expression; it works with numbers, reusing each intermediate value, so the cost stays proportional to the cost of the program. Forward mode is the right choice when there are few inputs and many outputs; for one output and many inputs, reverse mode (@sec-math-calculus-matrix-computing-derivatives-reverse-mode-automatic-differentiation) is far cheaper.

:::

::: {#fig-forward-mode-automatic-differentiation-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\draw[cell frame] (0,0) rectangle (2,2); \node[lab] at (1,1) {$J$};
\draw[hl cell] (0.6,0) rectangle (0.9,2);
\node[lab, below] at (1,-0.1) {one forward run: $Jv$, a column};
\draw[cell frame] (4.5,0) rectangle (6.5,2); \node[lab] at (5.5,1) {$J$};
\draw[hl cell] (4.5,1.1) rectangle (6.5,1.4);
\node[lab, below] at (5.5,-0.1) {one reverse run: $w^{\mathsf T}J$, a row};
\end{tikzpicture}
\end{center}
```

A forward-mode run produces one column of the Jacobian (more precisely one Jacobian–vector product); a reverse-mode run produces one row. For a scalar output the whole gradient is a single row.

:::
