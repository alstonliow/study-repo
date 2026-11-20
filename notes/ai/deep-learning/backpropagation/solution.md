<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs221hw-1-q2" status="draft"}
**(a)**

1. $\partial f/\partial w_j$: only the term $i=j$ depends on $w_j$, and $\frac{d}{dw_j}(w_j-c_j)^2=2(w_j-c_j)$.
2. Collecting the components, $\nabla f(\mathbf w)=2(\mathbf w-\mathbf c)$.
3. At $\mathbf w=\mathbf 0$: $\nabla f(\mathbf 0)=-2\mathbf c$.

**(c)**

1. Product:
$$C=AB=\begin{pmatrix}26&22\\79&44\end{pmatrix},\qquad s=26+22+79+44=171.$$
2. Write $s=\sum_{i,j}\sum_k A_{ik}B_{kj}$. The entry $A_{ik}$ appears once for every $j$, multiplied by $B_{kj}$, so
$$\frac{\partial s}{\partial A_{ik}}=\sum_j B_{kj}\quad(\text{row sum } k \text{ of } B).$$
The row sums of $B$ are $15,9,3$, the same for every $i$:
$$\frac{\partial s}{\partial A}=\begin{pmatrix}15&9&3\\15&9&3\end{pmatrix}=\mathbf 1_m\,(B\mathbf 1_p)^\top.$$
3. Symmetrically $B_{kj}$ appears once for every $i$, multiplied by $A_{ik}$:
$$\frac{\partial s}{\partial B_{kj}}=\sum_i A_{ik}\quad(\text{column sum } k \text{ of } A).$$
The column sums of $A$ are $6,6,9$, the same for every $j$:
$$\frac{\partial s}{\partial B}=\begin{pmatrix}6&6\\6&6\\9&9\end{pmatrix}=(A^\top\mathbf 1_m)\,\mathbf 1_p^\top.$$
:::

::: {.solution for="prob-backpropagation-gradient-check-code" status="draft"}
```{.python}
import numpy as np


def numerical_gradient(f, w, h=1e-5):
    """Central-difference estimate of the gradient of f at w (same shape as w)."""
    w = np.array(w, dtype=float)               # a private copy
    g = np.zeros_like(w)
    for i in np.ndindex(w.shape):
        old = w[i]
        w[i] = old + h
        up = f(w)
        w[i] = old - h
        down = f(w)
        w[i] = old
        g[i] = (up - down) / (2 * h)
    return g
```

1. `np.ndindex` runs over every index of an array of any shape, so the same loop serves vectors and matrices.
2. Working on a copy keeps the caller's array untouched; restoring `w[i]` after each pair of calls keeps the other coordinates at their original values.
3. The central difference has error $O(h^2)$ for smooth $f$ (the $h^1$ terms of the two Taylor expansions cancel), against $O(h)$ for the one-sided difference, so $h=10^{-5}$ gives about ten correct digits before rounding errors dominate.
4. Comparing this estimate with a backward pass at a few random points catches most mistakes in hand-written gradients, as in the third test.
:::
