---
title: "Reverse-Mode Automatic Differentiation"
sources: [mit18s096-8]
requires: [math/calculus/matrix/computing-derivatives/forward-mode-automatic-differentiation, math/calculus/matrix/derivatives/hessians-and-bilinear-maps]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.S096 Matrix Calculus (IAP 2023), course notes Chapter 8, Sections 8.3-8.4 (automatic differentiation on computational graphs, reverse mode on graphs, forward versus reverse mode, forward-over-reverse second derivatives), in our own wording; the example is ours, checked in Python against centred differences; proofs written out in steps. Backpropagation for scalar nodes is @def-computation-graph and @def-backpropagation (from CS221 and CS231n); this note states reverse mode for vector- and matrix-valued nodes and compares it with forward mode. -->

Reverse mode runs the chain rule from the output back to the inputs. For a scalar output it delivers the whole gradient for a small constant times the cost of computing the function, however many inputs there are. Backpropagation in neural networks is reverse mode on a particular graph.

::: {#def-reverse-mode .definition name="Reverse-mode accumulation" related="def-backpropagation"}

Let a program compute a scalar $f$ from an input $x$ through intermediate values $v_1,\dots,v_N=f$ (vectors or matrices), each $v_j=\phi_j(\text{its parents})$. For each value $v$, its *adjoint* $\bar v$ is the gradient of $f$ with respect to $v$, so that $df=\langle\bar v,dv\rangle$ when only $v$ changes. *Reverse mode*:

1. *Forward pass:* run the program and store the intermediate values.
2. *Backward pass:* set $\bar v_N=1$; for $j=N,N-1,\dots$, send to each parent $u$ of $v_j$ the contribution $\bigl(\partial\phi_j/\partial u\bigr)^{*}\,\bar v_j$, the adjoint (transpose) of the partial derivative applied to $\bar v_j$, and let $\bar u$ be the sum of the contributions it receives.

The result is $\bar x=\nabla f(x)$.

:::

```{=latex}
\begin{algorithm}
\caption{Reverse-mode accumulation}
\begin{algorithmic}
\INPUT a program computing scalar $v_N=f(x)$ through $v_1,\dots,v_N$; a point $x$
\FOR{$j=1$ \TO $N$}
  \STATE $v_j\gets\phi_j(\text{parents})$; store $v_j$
\ENDFOR
\STATE $\bar v_N\gets1$; all other adjoints $\gets0$
\FOR{$j=N$ \TO $1$ step $-1$}
  \FORALL{parents $u$ of $v_j$}
    \STATE $\bar u\gets\bar u+\bigl(\partial\phi_j/\partial u\bigr)^{*}\bar v_j$
  \ENDFOR
\ENDFOR
\RETURN $\bar x=\nabla f(x)$
\end{algorithmic}
\end{algorithm}
```

Each step applies a transposed Jacobian to a vector: a *vector–Jacobian product*. For example, a node $y=Ax$ sends $\bar x=A^{\mathsf T}\bar y$, and an elementwise node $z=g(y)$ sends $\bar y=g'(y)\circ\bar z$, where $\circ$ is the elementwise product.

::: {#thm-reverse-mode-correct .theorem name="Correctness and cost of reverse mode" related="thm-backpropagation"}

The backward pass of @def-reverse-mode returns $\bar x=\nabla f(x)$. If each vector–Jacobian product costs at most a constant $c$ times the cost of the operation $\phi_j$ itself, the gradient costs at most about $(1+c)$ times the cost of evaluating $f$, independently of the dimension of $x$; the price is the memory for the stored intermediate values.

:::

::: {.proof}

1. Process the nodes in reverse order. When $v_j$ is reached, all its children have been processed, so $\bar v_j$ is complete: $df=\sum_{\text{children }w}\langle\bar w,\partial\phi_w/\partial v_j\,[dv_j]\rangle$ by the chain rule (@thm-chain-rule-linear-operators), since $v_j$ influences $f$ only through its children.

2. Moving the linear map to the other side of the inner product, $\langle\bar w,L[dv_j]\rangle=\langle L^{*}\bar w,dv_j\rangle$, so $\bar v_j=\sum_wL_w^{*}\bar w$, which is what the pass computes. By induction from $\bar v_N=1$, every adjoint is correct, in particular $\bar x$.

3. *Cost.* Each node is visited once in each pass, and its backward work is at most $c$ times its forward work. Summing over nodes gives the bound.

:::

::: {#exm-reverse-mode-automatic-differentiation-1 .example name="A gradient in three backward steps"}

Let $f(x)=\sum_i\sin^2\bigl((Ax)_i\bigr)$ with $A=\begin{bmatrix}1&2\\0&-1\\1&1\end{bmatrix}$ and $x=(0.5,0.25)$. The forward pass stores $y=Ax=(1,-0.25,0.75)$, $z=\sin y=(0.8415,-0.2474,0.6816)$ and $f=z^{\mathsf T}z=1.2339$. The backward pass:

1. $f=z^{\mathsf T}z$ gives $\bar z=2z$;
2. $z=\sin y$ gives $\bar y=\cos y\circ\bar z$;
3. $y=Ax$ gives $\bar x=A^{\mathsf T}\bar y=(1.9068,\,3.2955)$.

Centred differences in Python agree to eight digits. With $n$ inputs instead of $2$, the backward pass would still be three vector operations.

:::

::: {#fig-reverse-mode-automatic-differentiation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\node[box] (x) at (0,0) {$x$};
\node[box] (y) at (2.4,0) {$y=Ax$};
\node[box] (z) at (5,0) {$z=\sin y$};
\node[box] (f) at (7.5,0) {$f=z^{\mathsf T}z$};
\draw[map] (x) -- (y); \draw[map] (y) -- (z); \draw[map] (z) -- (f);
\draw[map, hl] (f) to[bend left=40] node[lab, below] {$\bar z=2z$} (z);
\draw[map, hl] (z) to[bend left=40] node[lab, below] {$\bar y=\cos y\circ\bar z$} (y);
\draw[map, hl] (y) to[bend left=40] node[lab, below] {$\bar x=A^{\mathsf T}\bar y$} (x);
\node[lab] at (3.7,0.75) {forward pass: values};
\node[lab] at (3.7,-1.55) {backward pass: adjoints};
\end{tikzpicture}
\end{center}
```

Reverse mode on @exm-reverse-mode-automatic-differentiation-1. The forward pass stores $y$ and $z$; the backward pass turns the adjoint of each node into the adjoint of its parent by one transposed Jacobian.

:::

::: {#prp-forward-versus-reverse .proposition name="Forward versus reverse mode"}

Let $f:\mathbb{R}^n\to\mathbb{R}^m$ be computed by a program of cost $T$. The full Jacobian costs about $n\,T$ in forward mode ($n$ Jacobian–vector products, @prp-forward-mode-jvp) and about $m\,T$ in reverse mode ($m$ vector–Jacobian products, one per output), each up to a small constant factor. Forward mode is cheaper when $n\ll m$, reverse mode when $m\ll n$; for gradients ($m=1$) reverse mode wins.

:::

::: {.proof}

1. A forward run with dual input direction $v$ costs a constant times $T$ and produces $Jv$; the $n$ choices $v=e_i$ give all columns.

2. A reverse run seeded with $\bar f=w$ (in place of $1$) costs a constant times $T$ by @thm-reverse-mode-correct and produces $J^{\mathsf T}w$; the $m$ choices $w=e_i$ give all rows.

3. This is @prp-chain-rule-cost applied to the chain of Jacobians of the program: forward mode multiplies from the input side, reverse mode from the output side.

:::

::: {#prp-forward-over-reverse .proposition name="Hessian–vector products by forward over reverse"}

Let $f:\mathbb{R}^n\to\mathbb{R}$ be twice differentiable, computed by a program of cost $T$. Running the reverse-mode gradient program on dual input $x+v\,\epsilon$ returns $\nabla f(x)+H(x)v\,\epsilon$, so a Hessian–vector product costs a constant times $T$, without forming the $n\times n$ Hessian.

:::

::: {.proof}

1. The reverse pass is itself a program $x\mapsto\nabla f(x)$ built from elementary operations.

2. By @prp-forward-mode-jvp, running it on $x+v\epsilon$ gives $\nabla f(x)+J_{\nabla f}(x)v\,\epsilon$.

3. The Jacobian of $\nabla f$ is the Hessian (@def-hessian-matrix).

:::

::: {#exm-reverse-mode-automatic-differentiation-2 .example name="A Hessian–vector product"}

For $f$ of @exm-reverse-mode-automatic-differentiation-1, $\nabla f=A^{\mathsf T}\sin(2Ax)$ since $2\sin y\cos y=\sin2y$, so $H=2A^{\mathsf T}\operatorname{diag}(\cos 2Ax)A$. With $v=(1,0)$ this gives $Hv=(-0.6908,-1.5231)$, which is also what a centred difference of $\nabla f$ along $v$ gives.

:::

::: {#rmk-reverse-mode-automatic-differentiation-1 .remark name="What AD systems do"}

Real AD tools record the forward pass (a *tape*) or transform the source code, and ship hand-written vector–Jacobian rules for large operations such as matrix multiplication, linear solves (@thm-differential-inverse), determinants (@thm-jacobi-formula) and eigendecompositions (@thm-symmetric-eigendecomposition-differential). Writing such a rule by hand for one expensive step, and checking it with @def-finite-difference-check, is the usual way to make AD fast on structured problems.

:::
