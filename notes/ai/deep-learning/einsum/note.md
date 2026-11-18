---
title: "Einsum and Named Axes"
sources: [cs221-1]
requires: [ai/deep-learning/tensors]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 1 (einops), in our own wording. -->

Code such as "transpose the last two axes, then multiply" is easy to get wrong, because axes are referred to by position. Einstein summation (*einsum*) instead gives every axis a name and states the shape of the result; the einops library adds the same notation for reductions and reshapes.

::: {#def-einsum .definition name="Einsum"}

Give each axis of the input tensors $x^{(1)},\dots,x^{(r)}$ a name, so that each input is labelled by a list of names, and name the output's axes by a list $O$ of some of these names. Axes with the same name must have the same size. The *einsum* $x^{(1)},\dots,x^{(r)}\to O$ is the tensor indexed by the names in $O$ with

$$
y[O]=\sum_{\text{names not in }O}\ \prod_{t=1}^{r}x^{(t)}[\text{its names}],
$$

the sum running over all values of the names that are absent from the output.

:::

Names in the output are kept (the product is taken entrywise along them, as a batch); names absent from the output are summed over. In einops a name `...` stands for any number of leading axes that are carried along unchanged.

::: {#exm-einsum-matrix-product .example name="Products as einsums"}

1. Matrix product: $x$ of shape $(n,m)$ labelled $(\text{seq1},\text{hidden})$, $y$ of shape $(m,p)$ labelled $(\text{hidden},\text{seq2})$, output $(\text{seq1},\text{seq2})$. The rule gives $z[i,j]=\sum_l x[i,l]\,y[l,j]$, the matrix product $xy$.

2. Batched products against transposes: $x$ labelled $(\text{batch},\text{seq1},\text{hidden})$ and $y$ labelled $(\text{batch},\text{seq2},\text{hidden})$, output $(\text{batch},\text{seq1},\text{seq2})$. Then $z[b,i,j]=\sum_l x[b,i,l]\,y[b,j,l]$, which positional code writes as $x$ times $y$ with its last two axes swapped. Here the batch axis is kept and only $\text{hidden}$ is summed.

3. With one input $x$ labelled $(i,j)$: output $(j,i)$ is the transpose, output $()$ is the sum of all entries, and a single input labelled $(i,i)$ with output $()$ is the trace.

:::

::: {#def-tensor-reduction .definition name="Reduction"}

A *reduction* of a tensor along some named axes applies an operation such as sum, mean, max or min over all values of those names, for each fixed value of the remaining names. The result keeps only the remaining axes. For example, reducing $x$ labelled $(\text{batch},\text{seq},\text{hidden})$ to $(\text{batch},\text{seq})$ by sum gives $y[b,s]=\sum_h x[b,s,h]$.

:::

::: {#def-rearrange .definition name="Rearrange"}

A *rearrange* changes how the entries of a tensor are arranged into axes without changing them: it permutes axes, splits one axis of size $ab$ into two axes of sizes $a$ and $b$, or merges two adjacent axes into one. Splitting an axis $(h\,d)$ of size $ab$ into $(h,d)$ sends entry index $i$ to $(\lfloor i/b\rfloor,\ i\bmod b)$; merging is the inverse.

:::

::: {#exm-einsum-heads .example name="Transforming each head separately"}

Let $x$ have shape $(3,8)$, labelled $(\text{seq},\text{total})$, where $\text{total}$ is really two axes $(\text{heads},\text{hidden1})$ of sizes $2$ and $4$ merged. To multiply each head's $4$-vector by the same matrix $w$ labelled $(\text{hidden1},\text{hidden2})$ of shape $(4,4)$:

1. rearrange $(\text{seq},(\text{heads}\ \text{hidden1}))\to(\text{seq},\text{heads},\text{hidden1})$, shape $(3,2,4)$;
2. einsum $(\dots,\text{hidden1}),(\text{hidden1},\text{hidden2})\to(\dots,\text{hidden2})$, shape $(3,2,4)$;
3. rearrange $(\text{seq},\text{heads},\text{hidden2})\to(\text{seq},(\text{heads}\ \text{hidden2}))$, shape $(3,8)$.

Each step states the shapes, so a wrong axis is visible in the code rather than hidden in a position such as $-2$.

:::

::: {#fig-einsum-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \c in {0,...,7} { \draw[cell frame] ({0.42*\c},0) rectangle ({0.42*\c+0.42},0.42); }
\foreach \c in {0,...,3} { \draw[hl cell] ({0.42*\c},0) rectangle ({0.42*\c+0.42},0.42); }
\node[lab] at (1.68,0.75) {$\text{total}=(\text{heads}\ \text{hidden1})$, size $8$};
\node[lab] at (0.84,-0.3) {head $0$};
\node[lab] at (2.52,-0.3) {head $1$};
\draw[->] (3.6,0.21) -- node[lab,above] {split} (4.6,0.21);
\foreach \c in {0,...,3} { \draw[hl cell] ({4.9+0.42*\c},0.3) rectangle ({5.32+0.42*\c},0.72); }
\foreach \c in {0,...,3} { \draw[cell frame] ({4.9+0.42*\c},-0.3) rectangle ({5.32+0.42*\c},0.12); }
\node[lab, anchor=west] at (6.65,0.51) {head $0$};
\node[lab, anchor=west] at (6.65,-0.09) {head $1$};
\node[lab] at (5.74,1.05) {$(\text{heads},\text{hidden1})=(2,4)$};
\end{tikzpicture}
\end{center}
```

Splitting one row of $x$ in the example: the axis of size $8$ becomes two axes of sizes $(2,4)$, entry $i$ going to head $\lfloor i/4\rfloor$, position $i\bmod 4$.

:::

::: {#rmk-einsum-1 .remark name="Cost of an einsum"}

Computed directly, an einsum loops once over every combination of values of all names, kept and summed, so it costs the product of the sizes of all distinct names. For the matrix product that is $nmp$. With three or more inputs, the order in which pairs are contracted can change this cost a great deal; libraries choose an order for you.

:::
