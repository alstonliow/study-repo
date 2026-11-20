---
title: "Computation Graphs and Backpropagation"
sources: [cs221-4]
requires: [ai/deep-learning/einsum, ai/machine-learning/gradient-descent, cs/graph-algorithms/depth-first-search]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 4 (computation graphs, backpropagation), in our own wording. The correctness theorem and cost statement are our own formulation of the lecture's algorithm; proofs written out in steps. The chain rule itself is @thm-chain-rule-several-variables. -->

Gradient descent needs the gradient of the training loss. Working it out by hand is tedious and error-prone, but every such function is built from a few primitive operations (addition, multiplication, $\exp$, $\log$, matrix products, ...), each with a known derivative. Backpropagation (reverse-mode automatic differentiation) combines these local derivatives by the chain rule, for any function so built.

::: {#def-computation-graph .definition name="Computation graph"}

A *computation graph* is a directed acyclic graph whose nodes hold values. An *input node* (leaf) holds a given value, such as data or a parameter. Every other node $v$ applies a primitive function $f_v$ to the values of its *dependencies* $u_1,\dots,u_k$ (its in-neighbours): $\text{value}(v)=f_v(\text{value}(u_1),\dots,\text{value}(u_k))$. One node, the *root*, holds the scalar output, such as the loss. The *forward pass* computes all values in a topological order (@sec-cs-graph-algorithms-depth-first-search), so each node is computed after its dependencies.

:::

::: {#def-backpropagation .definition name="Backpropagation"}

After a forward pass, *backpropagation* computes $\text{grad}(v)=\partial\,\text{root}/\partial\,\text{value}(v)$ for every node $v$. It sets $\text{grad}(\text{root})=1$ and $\text{grad}(v)=0$ for the other nodes, then visits the nodes in reverse topological order; at each non-input node $v$ with dependencies $u_1,\dots,u_k$ it adds, for each $i$,

$$
\text{grad}(u_i)\ \mathrel{+}=\ \text{grad}(v)\cdot\frac{\partial f_v}{\partial u_i}\bigl(\text{value}(u_1),\dots,\text{value}(u_k)\bigr).
$$

:::

For tensor-valued nodes, $\text{grad}(v)$ has the shape of $\text{value}(v)$ and the product is the corresponding contraction; for example, if $v=u_1u_2$ is a matrix product, $u_1$ receives $\text{grad}(v)\,\text{value}(u_2)^{\mathsf T}$.

```{=latex}
\begin{algorithm}
\caption{Backpropagation}
\begin{algorithmic}
\INPUT Computation graph with root $r$
\OUTPUT $\text{grad}(v)=\partial r/\partial v$ for every node $v$
\STATE $v_1,\dots,v_n\gets$ the nodes in topological order (so $v_n=r$)
\FOR{$j=1$ \TO $n$}
    \STATE compute $\text{value}(v_j)$ from its dependencies \COMMENT{forward pass}
    \STATE $\text{grad}(v_j)\gets0$
\ENDFOR
\STATE $\text{grad}(r)\gets1$
\FOR{$j=n$ \TO $1$ \textbf{step} $-1$}
    \FOR{each dependency $u$ of $v_j$}
        \STATE $\text{grad}(u)\gets\text{grad}(u)+\text{grad}(v_j)\cdot\partial f_{v_j}/\partial u$ \COMMENT{backward pass}
    \ENDFOR
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

::: {#thm-backpropagation .theorem name="Correctness and cost of backpropagation"}

If every primitive function is differentiable, backpropagation returns $\text{grad}(v)=\partial\,\text{root}/\partial\,\text{value}(v)$ for every node $v$, where the root is viewed as a function of $\text{value}(v)$ with everything not downstream of $v$ held fixed. It evaluates one local derivative per edge, so for scalar nodes its cost is a constant multiple of the cost of the forward pass.

:::

::: {.proof}

1. Fix a node $v\ne\text{root}$ and let $w_1,\dots,w_m$ be the nodes that have $v$ as a dependency (its out-neighbours). The root depends on $\text{value}(v)$ only through $\text{value}(w_1),\dots,\text{value}(w_m)$. By the chain rule (@thm-chain-rule-several-variables),
$$
\frac{\partial\,\text{root}}{\partial\,v}=\sum_{i=1}^{m}\frac{\partial\,\text{root}}{\partial\,w_i}\cdot\frac{\partial f_{w_i}}{\partial v}.
$$

2. We show by induction along the reverse topological order that when the backward loop reaches $v$, $\text{grad}(v)$ already equals $\partial\,\text{root}/\partial v$. For the root this is the initial value $1$.

3. For $v\ne\text{root}$, each $w_i$ comes after $v$ in topological order, so it is processed before $v$ in the backward loop. By the induction hypothesis $\text{grad}(w_i)=\partial\,\text{root}/\partial w_i$ at that moment, and processing $w_i$ adds exactly the $i$-th term of the sum in step 1 to $\text{grad}(v)$. No other node adds to $\text{grad}(v)$. So when $v$ is reached, $\text{grad}(v)$ equals the sum, which is $\partial\,\text{root}/\partial v$.

4. The forward pass evaluates each $f_v$ once and the backward pass evaluates each partial derivative $\partial f_v/\partial u$ once, one per edge $(u,v)$; for the primitives in use, a partial derivative costs at most a constant times the primitive itself.

:::

::: {#exm-backpropagation-1 .example name="A small graph"}

Let $y=(x_1+x_2)^2$ at $x_1=2$, $x_2=3$, built as $z=x_1+x_2$ and $y=z^2$. The forward pass gives $z=5$, $y=25$. Backward: $\text{grad}(y)=1$; then $y=z^2$ gives $\text{grad}(z)=1\cdot2z=10$; then $z=x_1+x_2$ gives $\text{grad}(x_1)=\text{grad}(x_2)=10\cdot1=10$. Indeed $\partial y/\partial x_1=2(x_1+x_2)=10$.

:::

::: {#fig-backpropagation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[vertex] (x1) at (0,1) {$x_1$};
\node[vertex] (x2) at (0,-1) {$x_2$};
\node[vertex] (z) at (2.6,0) {$+$};
\node[vertex] (y) at (5.0,0) {$(\cdot)^2$};
\draw[->] (x1) -- node[edge label,above] {$\times1$} (z);
\draw[->] (x2) -- node[edge label,below] {$\times1$} (z);
\draw[->] (z) -- node[edge label,above] {$\times2z$} (y);
\node[lab,anchor=east] at (-0.45,1) {value $2$, \textbf{grad} $\mathbf{10}$};
\node[lab,anchor=east] at (-0.45,-1) {value $3$, \textbf{grad} $\mathbf{10}$};
\node[lab] at (2.9,0.8) {$z=5$, \textbf{grad} $\mathbf{10}$};
\node[lab] at (5.0,0.8) {$y=25$, \textbf{grad} $\mathbf{1}$};
\end{tikzpicture}
\end{center}
```

The computation graph of @exm-backpropagation-1. Values flow left to right in the forward pass; gradients (bold) flow right to left, each multiplied by the local derivative written on the edge.

:::

::: {#exm-backpropagation-2 .example name="Gradient of a least squares objective"}

Let $X$ be an $n\times d$ data matrix, $\mathbf{y}\in\mathbb{R}^n$ the targets and $\mathcal O(\mathbf{w})=\lVert X\mathbf{w}-\mathbf{y}\rVert^2$. Build it as $\mathbf{p}=X\mathbf{w}$ (predictions), $\mathbf{r}=\mathbf{p}-\mathbf{y}$ (residuals), $\mathcal O=\mathbf{r}\cdot\mathbf{r}$. Backward: $\text{grad}(\mathbf{r})=2\mathbf{r}$, $\text{grad}(\mathbf{p})=2\mathbf{r}$ (subtracting a constant has derivative $1$), and $\text{grad}(\mathbf{w})=X^{\mathsf T}(2\mathbf{r})=2X^{\mathsf T}(X\mathbf{w}-\mathbf{y})$. Setting this to zero gives the normal equations of @thm-least-squares-normal-equations.

:::

::: {#rmk-backpropagation-1 .remark name="Values and nodes"}

Libraries such as PyTorch and JAX build the computation graph automatically while the forward pass runs, from ordinary-looking tensor code. A tensor used as a node passes gradients back to its dependencies; a value detached from the graph (`detach()`), or computed while gradients are switched off (as at prediction time), is treated as a constant and blocks them.

:::
