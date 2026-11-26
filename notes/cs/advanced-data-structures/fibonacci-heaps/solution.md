<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6854ps-1-q1" status="draft"}
1. *Two nodes.* Insert keys $a<b<c$ and do `extract-min`. The roots $b,c$ have degree $0$ and are linked: $b$ with the single child $c$, a chain of $2$ nodes.

2. *From a chain of $k\ge2$ nodes to $k+1$.* Let the chain have root $x$ (degree $1$). Insert three keys $y_1<y_2<y_3$, all smaller than every key in the heap, and do `extract-min`, which removes $y_1$. Consolidation sees the roots $y_2,y_3$ (degree $0$) and $x$ (degree $1$): whatever the order, $y_3$ is linked below $y_2$, giving degree $1$, and then $x$ is linked below $y_2$ (smaller key), giving $y_2$ the two children $y_3$ and $x$. Linking does not mark anything.

3. Now `delete(y_3)`: `decrease-key` cuts $y_3$ from the root $y_2$ (a root is never marked, so no cascade), and `extract-min` removes $y_3$; consolidation finds the single root $y_2$. The heap is $y_2$ with one child $x$, whose subtree is the old chain: a chain of $k+1$ nodes.

4. Repeating steps 2–3 $n-2$ times gives a chain on $n$ elements.
:::

::: {.solution for="prob-mit6854ps-1-q2" status="draft"}
*(a) Decrease-key.* For a non-root node $x$ let $\ell(x)\in\{0,\dots,k-1\}$ be the number of children it lost since it last became a child, and use
$$\Phi=t(H)+\frac2{k-1}\sum_x\ell(x).$$

1. A `decrease-key` that triggers $c$ cascading cuts does $c+1$ cuts, cost $c+1$, and creates $c+1$ new roots.

2. Each cascading cut removes a node with $\ell=k-1$ (it would reach $k$), so $\sum\ell$ drops by $c(k-1)$; the last parent gains $1$.

3. Amortized cost $\le(c+1)+(c+1)+\frac2{k-1}\big(1-c(k-1)\big)=2+\frac2{k-1}$, a constant that decreases with $k$ (it is $4$ for the original $k=2$ with $\Phi=t+2m$).

*Delete-min.* Its amortized cost is $O(D(n))$ as before, where $D(n)$ bounds the degrees; resetting $\ell$ of the children that become roots only lowers $\Phi$. Now when the $i$-th child $y_i$ of $x$ was linked, $x$ had at least $i-1$ children, so $y_i$ had degree at least $i-1$; it has lost at most $k-1$ children since, so its degree is at least $i-k$. With $s_d$ the least size of a subtree whose root has degree $d$:
$$s_d\ge1+\sum_{i=1}^ds_{\max(0,i-k)},\qquad\text{hence } s_d-s_{d-1}\ge s_{d-k}\ (d>k).$$
So $s_d\ge r_k^{\,d}$ up to a constant, where $r_k>1$ is the root of $r^k=r^{k-1}+1$, and $D(n)\le\log_{r_k}n+O(1)$. For $k=2$, $r_2=\varphi$. Since $r_k$ decreases towards $1$ as $k$ grows, $\log_{r_k}n=\ln n/\ln r_k$ is a larger constant multiple of $\log n$: delete-min becomes more expensive by a constant factor.

*(b)* Writing $r_k=1+x$, the equation $(1+x)^{k-1}x=1$ gives $x\approx\ln k/k$, so the bound is $D(n)=O\big(\tfrac{k}{\log k}\log n\big)$, logarithmic only for $k=O(1)$. One cannot do much better in general: for $i\le k$ the child $y_i$ may lose all its $i-1$ children without being cut, so a node of degree $k$ can have only $k+1$ nodes in its subtree. If $k$ grows faster than $\log n$ (for instance $k=\sqrt n$), ranks of order $k$, far above $\log n$, become possible. So $k$ cannot grow with $n$ in general if ranks are to stay logarithmic (a slowly growing $k=O(\log n)$ still keeps the trivial bound rank $\le k$ but not the $O(\log n)$ bound from the recurrence).
:::
