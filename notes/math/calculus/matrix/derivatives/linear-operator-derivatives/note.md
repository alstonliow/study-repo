---
title: "Derivatives as Linear Operators"
sources: [mit18s096-1, mit18s096-2]
requires: [math/calculus/multivariable/differentiation/differentials-and-chain-rule, math/linear-algebra/linear-maps/linear-maps-and-isomorphisms]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.S096 Matrix Calculus (IAP 2023), course notes Chapters 1 (product rule) and 2 (derivatives as linear operators, directional derivatives, gradients, Jacobians, the chain rule and its cost), in our own wording; the examples are ours, checked in Python; proofs written out in steps. The rigorous Euclidean definition is @def-derivative-several-variables; this note states it for any normed spaces and works with differentials. -->

The derivative of a function is the *linear operator* that best approximates the change in its output. Writing it as a linear operator, rather than as a table of partial derivatives, lets the same rules (product rule, chain rule) work for inputs and outputs that are scalars, vectors, matrices or functions.

::: {#def-derivative-linear-operator .definition name="Derivative as a linear operator" related="def-derivative-several-variables"}

Let $V,W$ be normed vector spaces and $f:V\to W$. The *derivative* of $f$ at $x$ is the linear operator $f'(x):V\to W$ such that

$$
f(x+\delta x)-f(x)=f'(x)[\delta x]+o(\lVert\delta x\rVert)\qquad(\delta x\to0),
$$

if one exists. In *differential notation*, $dx$ is an arbitrarily small change of the input and

$$
df=f(x+dx)-f(x)=f'(x)[dx],
$$

where terms of higher order than $\lVert dx\rVert$ are dropped.

:::

::: {#rmk-linear-operator-derivatives-1 .remark name="One definition for every shape"}

The shapes follow from linearity alone. For $f:\mathbb{R}\to\mathbb{R}$, $f'(x)[dx]=f'(x)\,dx$ is multiplication by a number. For $f:\mathbb{R}^n\to\mathbb{R}^m$, $f'(x)$ is an $m\times n$ matrix, the Jacobian. For $f:\mathbb{R}^{n\times n}\to\mathbb{R}^{n\times n}$, $f'(A)$ maps matrices to matrices and is usually easiest to write as a formula in $dA$, not as a matrix.

:::

::: {#fig-linear-operator-derivatives-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.4cm, y=1.4cm]
\draw[->] (-0.2,0) -- (3.4,0) node[lab, right] {$x$};
\draw[->] (0,-0.2) -- (0,2.6);
\draw[domain=0.2:3.1, samples=40] plot (\x, {0.25*\x*\x});
\draw[hl, domain=0.6:3.1] plot (\x, {1*(\x-1.6)+0.64});
\fill (1.6,0.64) circle (1.5pt) node[lab, above left] {$f(x)$};
\draw[faint] (1.6,0.64) -- (2.8,0.64);
\draw[emph] (2.8,0.64) -- node[lab, right] {$df=f'(x)[dx]$} (2.8,1.84);
\draw[faint, dashed] (2.8,1.84) -- (2.8,1.96);
\node[lab, right] at (2.95,2.1) {$o(dx)$};
\draw[<->] (1.6,0.45) -- node[lab, below] {$dx$} (2.8,0.45);
\end{tikzpicture}
\end{center}
```

The derivative is the linear part of the change: along the tangent line the output changes by $df=f'(x)[dx]$; the true change differs from it by a term that vanishes faster than $dx$.

:::

::: {#def-directional-derivative-operator .definition name="Directional derivative" related="def-directional-derivative-several"}

If $f$ is differentiable at $x$, then for every direction $v\in V$

$$
f'(x)[v]=\frac{d}{d\alpha}f(x+\alpha v)\Big|_{\alpha=0},
$$

the rate of change of $f$ along the line through $x$ in direction $v$.

:::

::: {#def-gradient-from-differential .definition name="Gradient of a scalar function" related="def-gradient"}

Let $f:\mathbb{R}^n\to\mathbb{R}$ be differentiable at $x$. Then $f'(x)$ is a linear map $\mathbb{R}^n\to\mathbb{R}$, so it is a row vector, and the *gradient* $\nabla f(x)\in\mathbb{R}^n$ is the column vector with

$$
df=f'(x)[dx]=\nabla f(x)^{\mathsf T}dx\quad\text{for all }dx,\qquad\text{that is}\quad \nabla f(x)=f'(x)^{\mathsf T}.
$$

:::

The gradient has the shape of the input, and it is read off from $df$ once $df$ is written as (something)$^{\mathsf T}dx$.

::: {#thm-differential-product-rule .theorem name="Product rule for differentials"}

If $A(x)$ and $B(x)$ are differentiable matrix-valued functions whose product is defined, then

$$
d(AB)=(dA)\,B+A\,(dB).
$$

The order of the factors must be kept: in general $(dA)B\neq B\,dA$.

:::

::: {.proof}

1. Change $x$ by $dx$, so $A$ becomes $A+dA$ and $B$ becomes $B+dB$.

2. Expand: $(A+dA)(B+dB)-AB=(dA)B+A(dB)+(dA)(dB)$.

3. The last term is a product of two first-order changes, so it is of second order in $dx$ and is dropped.

4. No step used commutativity, so the order of each product is the order in $AB$.

:::

::: {#fig-linear-operator-derivatives-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\draw[cell frame] (0,0) rectangle (3,2); \node[lab] at (1.5,1) {$AB$};
\draw[hl cell] (3,0) rectangle (3.6,2); \node[lab] at (3.3,1) {$(dA)B$};
\draw[hl cell] (0,2) rectangle (3,2.5); \node[lab] at (1.5,2.25) {$A(dB)$};
\draw[cell frame, faint] (3,2) rectangle (3.6,2.5); \node[lab] at (4.6,2.25) {$(dA)(dB)$};
\draw[<->] (0,-0.25) -- node[lab, below] {$A$} (3,-0.25);
\draw[<->] (3,-0.25) -- node[lab, below] {$dA$} (3.6,-0.25);
\draw[<->] (-0.25,0) -- node[lab, left] {$B$} (-0.25,2);
\draw[<->] (-0.25,2) -- node[lab, left] {$dB$} (-0.25,2.5);
\end{tikzpicture}
\end{center}
```

For numbers the product rule is the area of a growing rectangle: the two thin strips are first order and the corner is second order. For matrices the same picture holds, but each strip keeps its factors in order.

:::

::: {#exm-differential-quadratic-form .example name="A quadratic form and the matrix square"}

1. Let $f(x)=x^{\mathsf T}Ax$ with a constant $A\in\mathbb{R}^{n\times n}$. By @thm-differential-product-rule, $df=dx^{\mathsf T}Ax+x^{\mathsf T}A\,dx$. The first term is a scalar, so it equals its transpose $x^{\mathsf T}A^{\mathsf T}dx$, and

   $$df=x^{\mathsf T}(A+A^{\mathsf T})\,dx,\qquad \nabla f=(A+A^{\mathsf T})x.$$

   For $A=\begin{bmatrix}1&2\\0&3\end{bmatrix}$ and $x=(1,-1)$ this gives $f(x)=2$ and $\nabla f=(0,-4)$.

2. Let $f(A)=A^2$ on $n\times n$ matrices. Then $f'(A)[dA]=dA\,A+A\,dA$. With $A=\begin{bmatrix}0&1\\0&0\end{bmatrix}$ and $dA=\begin{bmatrix}0&0\\1&0\end{bmatrix}$ this is the identity matrix, while the scalar guess $2A\,dA$ gives $\begin{bmatrix}2&0\\0&0\end{bmatrix}$.

:::

::: {#thm-chain-rule-linear-operators .theorem name="Chain rule for linear operators" related="thm-chain-rule-several-variables"}

If $g$ is differentiable at $x$ and $f$ is differentiable at $g(x)$, then $f\circ g$ is differentiable at $x$ and

$$
(f\circ g)'(x)=f'\bigl(g(x)\bigr)\,g'(x),
$$

the composition of the two linear operators: first $g'(x)$, then $f'(g(x))$.

:::

::: {.proof}

1. Write $dg=g'(x)[dx]$, the first-order change of $g$.

2. The output of $f$ changes by $f'(g(x))[dg]$ to first order, because its input changed by $dg$ plus a higher-order term, which $f'(g(x))$ maps to a higher-order term.

3. Hence $d(f\circ g)=f'(g(x))\bigl[g'(x)[dx]\bigr]$. The rigorous estimate of the remainders is the proof of @thm-chain-rule-several-variables, which uses only norms and so holds in any normed spaces.

:::

::: {#prp-chain-rule-cost .proposition name="The order of a Jacobian product matters"}

Let $f=f_3\circ f_2\circ f_1$ with $f_1:\mathbb{R}^n\to\mathbb{R}^p$, $f_2:\mathbb{R}^p\to\mathbb{R}^q$ and a scalar output $f_3:\mathbb{R}^q\to\mathbb{R}$, so $f'(x)=J_3J_2J_1$ with $J_3$ of size $1\times q$, $J_2$ of size $q\times p$, $J_1$ of size $p\times n$. Multiplying the usual way, an $a\times b$ by $b\times c$ product costs $abc$ scalar multiplications, and

1. *right to left* (forward mode), $J_3(J_2J_1)$, costs $qpn+qn$;
2. *left to right* (reverse mode), $(J_3J_2)J_1$, costs $qp+pn$.

When $n,p,q$ are all about $N$, forward order costs about $N^3$ and reverse order about $2N^2$.

:::

::: {.proof}

1. Right to left: $J_2J_1$ is $(q\times p)(p\times n)$, costing $qpn$; then $J_3$ times the $q\times n$ result costs $1\cdot q\cdot n$.

2. Left to right: $J_3J_2$ is $(1\times q)(q\times p)$, costing $qp$ and giving a row vector; then that row vector times $J_1$ costs $1\cdot p\cdot n$.

3. Reverse order never forms a matrix–matrix product, because a scalar output makes the leftmost factor a row vector and every partial product stays a row vector.

:::

::: {#fig-linear-operator-derivatives-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\draw[hl cell] (0,1.6) rectangle (1.6,1.8); \node[lab, above] at (0.8,1.8) {$J_3$};
\draw[cell frame] (2,0.2) rectangle (3.6,1.8); \node[lab] at (2.8,1) {$J_2$};
\draw[cell frame] (4,0.2) rectangle (5.6,1.8); \node[lab] at (4.8,1) {$J_1$};
\node[lab, right] at (6,1.5) {reverse: $(J_3J_2)J_1$, rows only};
\node[lab, right] at (6,0.6) {forward: $J_3(J_2J_1)$, a full product};
\draw[map, hl] (0.8,0) -- (5.2,0) node[lab, midway, below] {reverse mode sweeps this way};
\end{tikzpicture}
\end{center}
```

With a scalar output the leftmost Jacobian is a single row. Multiplying from the left keeps every intermediate a row (matrix–vector work); multiplying from the right first forms the square product $J_2J_1$ (matrix–matrix work). This is why gradients are computed in reverse mode (@sec-math-calculus-matrix-computing-derivatives-reverse-mode-automatic-differentiation).

:::
