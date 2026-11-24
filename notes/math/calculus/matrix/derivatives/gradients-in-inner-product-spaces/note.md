---
title: "Gradients in Inner Product Spaces"
sources: [mit18s096-5]
requires: [math/calculus/matrix/derivatives/jacobians-and-kronecker-products, math/linear-algebra/inner-product-spaces/inner-products]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.S096 Matrix Calculus (IAP 2023), course notes Chapter 5 (the Frobenius inner product and norm, gradients in Hilbert spaces, weighted inner products, norms and Banach spaces), in our own wording; the examples are ours, checked in Python; proofs written out in steps. The entrywise matrix gradient of @def-matrix-gradient is the Frobenius case of the definition here. -->

The derivative $f'(x)$ needs only a norm, to say what "small" means. The *gradient* of a scalar function needs more: an inner product, which turns the linear form $f'(x)$ into a vector of the input space. Changing the inner product changes the gradient, though not the derivative.

::: {#def-frobenius-inner-product .definition name="Frobenius inner product and norm"}

On $\mathbb{R}^{m\times n}$ the *Frobenius inner product* and *Frobenius norm* are

$$
\langle A,B\rangle_F=\operatorname{tr}(A^{\mathsf T}B)=\sum_{i,j}a_{ij}b_{ij}=(\operatorname{vec}A)^{\mathsf T}\operatorname{vec}B,\qquad \lVert A\rVert_F=\sqrt{\langle A,A\rangle_F}.
$$

:::

The Frobenius inner product is the ordinary dot product of the vectorized matrices (@def-vec), so it inherits all the axioms of an inner product.

::: {#def-gradient-inner-product .definition name="Gradient in an inner product space" related="def-gradient-from-differential def-matrix-gradient"}

Let $V$ be a finite-dimensional real inner product space and $f:V\to\mathbb{R}$ differentiable at $x$. The *gradient* $\nabla f(x)\in V$ is the unique vector with

$$
df=f'(x)[dx]=\langle\nabla f(x),dx\rangle\qquad\text{for all }dx\in V.
$$

On matrices the default is the Frobenius inner product, so $df=\operatorname{tr}\bigl(\nabla f(A)^{\mathsf T}dA\bigr)$.

:::

::: {#prp-gradient-exists .proposition name="The gradient exists and is unique"}

In a finite-dimensional real inner product space $V$, every linear form $\ell:V\to\mathbb{R}$ is $\ell(v)=\langle g,v\rangle$ for exactly one $g\in V$. Hence $\nabla f(x)$ in @def-gradient-inner-product exists and is unique.

:::

::: {.proof}

1. Take an orthonormal basis $e_1,\dots,e_n$ of $V$ and put $g=\sum_i\ell(e_i)\,e_i$.

2. For $v=\sum_iv_ie_i$, linearity gives $\ell(v)=\sum_iv_i\ell(e_i)=\langle g,v\rangle$.

3. If also $\ell(v)=\langle h,v\rangle$ for all $v$, then $\langle g-h,v\rangle=0$ for $v=g-h$, so $g=h$. (This is @lem-riesz-finite-dimensional.)

:::

::: {#fig-gradients-in-inner-product-spaces-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\node[box] (dx) at (0,0) {$dx\in V$};
\node[box] (df) at (4.5,0) {$df\in\mathbb{R}$};
\node[hl box] (g) at (2.25,-1.6) {$\nabla f(x)\in V$};
\draw[map] (dx) -- node[lab, above] {$f'(x)$ (needs a norm)} (df);
\draw[map, hl] (g) -- node[lab, right] {$\langle\nabla f,\cdot\rangle$} (df);
\node[lab] at (2.25,-2.4) {the inner product picks the vector that represents $f'(x)$};
\end{tikzpicture}
\end{center}
```

The derivative of a scalar function is a linear form. The gradient is the vector of the input space that represents it through the inner product, so it has the shape of the input.

:::

::: {#exm-gradients-frobenius .example name="Frobenius gradients"}

1. *Bilinear form.* Let $f(A)=x^{\mathsf T}Ay$ with fixed $x\in\mathbb{R}^m$, $y\in\mathbb{R}^n$. Then $df=x^{\mathsf T}dA\,y=\operatorname{tr}(yx^{\mathsf T}dA)=\operatorname{tr}\bigl((xy^{\mathsf T})^{\mathsf T}dA\bigr)$, so $\nabla f=xy^{\mathsf T}$.

2. *Frobenius norm.* Let $f(A)=\lVert A\rVert_F$ for $A\neq0$. From $f^2=\operatorname{tr}(A^{\mathsf T}A)$, $2f\,df=\operatorname{tr}(dA^{\mathsf T}A+A^{\mathsf T}dA)=2\operatorname{tr}(A^{\mathsf T}dA)$, so $\nabla f=A/\lVert A\rVert_F$. For $A=\begin{bmatrix}3&4\\0&0\end{bmatrix}$, $\lVert A\rVert_F=5$ and $\nabla f=\begin{bmatrix}0.6&0.8\\0&0\end{bmatrix}$.

:::

::: {#prp-weighted-gradient .proposition name="The gradient depends on the inner product"}

Let $W$ be symmetric positive definite and give $\mathbb{R}^n$ the inner product $\langle x,y\rangle_W=x^{\mathsf T}Wy$. If $\nabla f$ is the gradient for the standard dot product, the gradient for $\langle\cdot,\cdot\rangle_W$ is

$$
\nabla^{(W)}f=W^{-1}\nabla f .
$$

:::

::: {.proof}

1. The derivative does not depend on the inner product: $df=(\nabla f)^{\mathsf T}dx$.

2. We need $g$ with $g^{\mathsf T}W\,dx=(\nabla f)^{\mathsf T}dx$ for all $dx$, that is $Wg=\nabla f$, using $W^{\mathsf T}=W$.

3. $W$ is invertible, so $g=W^{-1}\nabla f$.

:::

::: {#exm-weighted-gradient .example name="Changing the inner product"}

For $f(x)=x^{\mathsf T}Ax$ with $A=\begin{bmatrix}1&2\\0&3\end{bmatrix}$ at $x=(1,-1)$, the standard gradient is $(0,-4)$ (@exm-differential-quadratic-form). With $W=\operatorname{diag}(1,4)$, the weighted gradient is $(0,-1)$. Both give the same $df$ for every $dx$, and steepest descent with the weighted gradient takes a different step.

:::

::: {#rmk-gradients-in-inner-product-spaces-1 .remark name="Derivatives need only a norm"}

A *Banach space* is a complete normed vector space. @def-derivative-linear-operator makes sense in any Banach space, also infinite-dimensional ones such as spaces of functions, where the derivative is moreover required to be a bounded linear operator. On a finite-dimensional space all norms are equivalent (@sec-math-analysis-metric-spaces-normed-spaces), so whether $f$ is differentiable, and what $f'(x)$ is, does not depend on the norm. A gradient needs a *Hilbert space*, a complete inner product space; the functional case is @sec-math-calculus-matrix-functionals-and-random-functions-calculus-of-variations.

:::

::: {#fig-gradients-in-inner-product-spaces-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\draw[faint] (-2.2,0) -- (2.2,0); \draw[faint] (0,-2.2) -- (0,2.2);
\draw[set] (0,0) circle (1.4);
\draw[set, hl] (0,0) ellipse (1.4 and 0.7);
\draw[map] (0,0) -- (0,-2) node[lab, right] {$\nabla f=(0,-4)/2$};
\draw[map, hl] (0,0) -- (0,-0.5);
\node[lab, left] at (-1.5,-0.45) {$\nabla^{(W)}f=(0,-1)/2$};
\node[lab] at (1.9,1.3) {$x^{\mathsf T}x=c$};
\node[lab] at (2.1,-0.8) {$x^{\mathsf T}Wx=c$};
\end{tikzpicture}
\end{center}
```

Unit balls of the standard and the weighted inner product with $W=\operatorname{diag}(1,4)$. The weighted length of the second coordinate counts four times, so the weighted gradient shrinks that component by $4$ (both arrows drawn at half length).

:::
