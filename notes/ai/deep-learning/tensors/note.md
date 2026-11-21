---
title: "Tensors"
sources: [cs221-1]
requires: [math/linear-algebra/systems/matrix-multiplication]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 1 (tensors), in our own wording. -->

In machine learning, data, model parameters, gradients and intermediate results are all stored as tensors: multi-dimensional arrays of numbers that generalize vectors and matrices. Computations are written as a few whole-tensor operations rather than loops over entries.

::: {#def-tensor .definition name="Tensor, shape, rank"}

A *tensor* of *shape* $(n_1,\dots,n_k)$ is an array $x$ of real numbers with one entry

$$
x[i_1,\dots,i_k]\in\mathbb{R},\qquad 0\le i_j<n_j\ (j=1,\dots,k),
$$

for each tuple of indices. The number $k$ of indices is its *rank* (or number of *dimensions* or *axes*), and $n_j$ is the size of axis $j$. A scalar is a rank-$0$ tensor, a vector a rank-$1$ tensor and a matrix a rank-$2$ tensor. The tensor has $n_1n_2\cdots n_k$ entries.

:::

Indices start at $0$, as in code. Rank here counts axes; it is not the rank of a matrix in linear algebra.

::: {#exm-tensor-shapes .example name="Typical shapes"}

A dataset of $N$ points in $\mathbb{R}^D$ is a tensor of shape $(N,D)$: examples are *batched* along the first axis. $N$ sequences of length $L$ with a vector in $\mathbb{R}^D$ at each position form a tensor of shape $(N,L,D)$. $N$ colour images of height $H$ and width $W$ with $C=3$ channels form a tensor of shape $(N,H,W,C)$. A layer of a neural network that maps $\mathbb{R}^{D_{\text{in}}}$ to $\mathbb{R}^{D_{\text{out}}}$ stores a weight tensor of shape $(D_{\text{in}},D_{\text{out}})$, and a whole model's parameters are a collection of such tensors.

:::

::: {#def-tensor-slice .definition name="Slice, view"}

Fixing some indices of a tensor, or restricting them to a range, gives a *slice*. For a tensor $x$ of shape $(n_1,n_2,n_3)$, the slice $x[i,:,:]$ is the matrix $\bigl(x[i,j,l]\bigr)_{j,l}$ of shape $(n_2,n_3)$, and $x[:,:,l]$ has shape $(n_1,n_2)$. In array libraries, slices (and transposes and reshapes, when possible) are *views*: they share storage with the original tensor, so writing to one changes the other.

:::

::: {#fig-tensors-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \i/\st in {2/cell frame,1/hl cell,0/cell frame} {
  \foreach \r in {0,1,2} {
    \foreach \c in {0,1,2,3} {
      \draw[\st] ({0.55*\c+0.35*\i},{-0.55*\r+0.35*\i}) rectangle ({0.55*\c+0.55+0.35*\i},{-0.55*\r+0.55+0.35*\i});
    }
  }
}
\node[lab] at (1.45,-1.55) {$x$, shape $(3,3,4)$};
\node[lab] at (0.5,1.35) {$i=0,1,2$};
\foreach \r in {0,1,2} { \foreach \c in {0,1,2,3} {
  \draw[hl cell] ({4.2+0.55*\c},{0.35-0.55*\r}) rectangle ({4.75+0.55*\c},{0.9-0.55*\r}); } }
\node[lab] at (5.3,-1.55) {$x[1,:,:]$, shape $(3,4)$};
\end{tikzpicture}
\end{center}
```

A rank-$3$ tensor of shape $(3,3,4)$ drawn as three stacked $3\times4$ matrices, and the slice $x[1,:,:]$ (highlighted), a matrix of shape $(3,4)$.

:::

::: {#def-elementwise-operation .definition name="Elementwise operation"}

For a function $f:\mathbb{R}\to\mathbb{R}$ and a tensor $x$, the tensor $f(x)$ has the same shape and entries $f(x[i_1,\dots,i_k])$. Likewise, for $g:\mathbb{R}^2\to\mathbb{R}$ and tensors $x,y$ of the same shape, $g(x,y)$ has entries $g(x[\mathbf{i}],y[\mathbf{i}])$; this covers $x+y$, $x-y$, the entrywise product $x\odot y$ and $x/y$.

:::

::: {#def-broadcasting .definition name="Broadcasting"}

An elementwise operation on tensors of different shapes first *broadcasts* them to a common shape: shapes are aligned from the last axis, missing leading axes are treated as size $1$, and an axis of size $1$ is repeated to match the other tensor's size on that axis. Two sizes that differ and are both larger than $1$ are an error. For example, a tensor of shape $(N,D)$ plus a vector of shape $(D,)$ adds the vector to every row.

:::

::: {#fig-tensors-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.00,0.00) rectangle (0.45,-0.45);
\node[tick] at (0.23,-0.23) {$1$};
\draw[cell frame] (0.00,-0.45) rectangle (0.45,-0.90);
\node[tick] at (0.23,-0.68) {$2$};
\draw[cell frame] (0.00,-0.90) rectangle (0.45,-1.35);
\node[tick] at (0.23,-1.12) {$3$};
\node[lab] at (0.8,-0.67) {$+$};
\draw[cell frame] (1.20,-0.45) rectangle (1.65,-0.90);
\node[tick] at (1.43,-0.68) {$10$};
\draw[cell frame] (1.65,-0.45) rectangle (2.10,-0.90);
\node[tick] at (1.88,-0.68) {$20$};
\draw[cell frame] (2.10,-0.45) rectangle (2.55,-0.90);
\node[tick] at (2.33,-0.68) {$30$};
\draw[cell frame] (2.55,-0.45) rectangle (3.00,-0.90);
\node[tick] at (2.77,-0.68) {$40$};
\node[lab] at (3.35,-0.67) {$=$};
\draw[hl cell] (3.70,0.00) rectangle (4.15,-0.45);
\node[tick] at (3.93,-0.23) {$11$};
\draw[hl cell] (4.15,0.00) rectangle (4.60,-0.45);
\node[tick] at (4.38,-0.23) {$21$};
\draw[hl cell] (4.60,0.00) rectangle (5.05,-0.45);
\node[tick] at (4.83,-0.23) {$31$};
\draw[hl cell] (5.05,0.00) rectangle (5.50,-0.45);
\node[tick] at (5.28,-0.23) {$41$};
\draw[hl cell] (3.70,-0.45) rectangle (4.15,-0.90);
\node[tick] at (3.93,-0.68) {$12$};
\draw[hl cell] (4.15,-0.45) rectangle (4.60,-0.90);
\node[tick] at (4.38,-0.68) {$22$};
\draw[hl cell] (4.60,-0.45) rectangle (5.05,-0.90);
\node[tick] at (4.83,-0.68) {$32$};
\draw[hl cell] (5.05,-0.45) rectangle (5.50,-0.90);
\node[tick] at (5.28,-0.68) {$42$};
\draw[hl cell] (3.70,-0.90) rectangle (4.15,-1.35);
\node[tick] at (3.93,-1.12) {$13$};
\draw[hl cell] (4.15,-0.90) rectangle (4.60,-1.35);
\node[tick] at (4.38,-1.12) {$23$};
\draw[hl cell] (4.60,-0.90) rectangle (5.05,-1.35);
\node[tick] at (4.83,-1.12) {$33$};
\draw[hl cell] (5.05,-0.90) rectangle (5.50,-1.35);
\node[tick] at (5.28,-1.12) {$43$};
\node[tick, below] at (0.22,-1.4) {$(3,1)$};
\node[tick, below] at (2.1,-0.95) {$(1,4)$};
\node[tick, below] at (4.6,-1.4) {$(3,4)$};
\end{tikzpicture}
\end{center}
```

Broadcasting a $(3,1)$ column against a $(1,4)$ row: each axis of size $1$ is repeated to match the other, and the sum has shape $(3,4)$

:::

::: {#def-batched-matrix-multiplication .definition name="Batched matrix multiplication" related="def-matrix-product"}

For a tensor $x$ of shape $(B,n,m)$ and a matrix $w$ of shape $(m,p)$, the product $x\,w$ has shape $(B,n,p)$ with

$$
(x\,w)[b,i,j]=\sum_{l=0}^{m-1}x[b,i,l]\,w[l,j],
$$

that is, every slice $x[b,:,:]$ is multiplied by the same $w$ ($w$ is broadcast over the batch axis). More generally, matrix multiplication acts on the last two axes and broadcasts over all leading axes.

:::

::: {#fig-tensors-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \b in {1,0} { \foreach \r in {0,1} { \foreach \c in {0,1,2} {
  \draw[cell frame] ({0.5*\c+0.3*\b},{-0.5*\r+0.3*\b}) rectangle ({0.5*\c+0.5+0.3*\b},{-0.5*\r+0.5+0.3*\b}); } } }
\node[lab] at (1.0,-1.1) {$x$: $(2,2,3)$};
\node[lab] at (2.35,0.0) {$\times$};
\foreach \r in {0,1,2} { \foreach \c in {0,1} {
  \draw[hl cell] ({2.8+0.5*\c},{0.5-0.5*\r}) rectangle ({3.3+0.5*\c},{1.0-0.5*\r}); } }
\node[lab] at (3.3,-1.1) {$w$: $(3,2)$};
\node[lab] at (4.35,0.0) {$=$};
\foreach \b in {1,0} { \foreach \r in {0,1} { \foreach \c in {0,1} {
  \draw[cell frame] ({4.8+0.5*\c+0.3*\b},{-0.5*\r+0.3*\b}) rectangle ({5.3+0.5*\c+0.3*\b},{-0.5*\r+0.5+0.3*\b}); } } }
\node[lab] at (5.5,-1.1) {$x\,w$: $(2,2,2)$};
\end{tikzpicture}
\end{center}
```

Batched matrix multiplication: each of the $B=2$ slices of $x$ (shape $2\times3$) is multiplied by the same $w$ (shape $3\times2$), giving $B=2$ slices of shape $2\times2$.

:::

::: {#rmk-tensors-1 .remark name="Vectorize"}

The same result can often be computed by a Python loop over entries or by one tensor operation. The tensor operation runs as optimized compiled code (on a GPU for large tensors) and is typically orders of magnitude faster, so computations should be expressed as a few tensor operations whenever possible. Finding such an expression is a small puzzle; @sec-ai-deep-learning-einsum gives a notation that keeps the axes legible.

:::
