::: {.problem #prob-mit18s096ps-1-q0 origin="external" source="mit18s096ps-1-q0"}
The hyperbolic Corgi notebook may be found at <https://mit-c25.netlify.app/notebooks/1_hyperbolic_corgi>. Compute the $2 \times 2$ Jacobian matrix for each of the following image transformations from that notebook:

(a) rotate($\theta$): $(x,y)\rightarrow (\cos(\theta)x + \sin(\theta)y, -\sin(\theta)x + \cos(\theta)y)$

(b) hyperbolic\_rotate($\theta$): $(x,y)\rightarrow(\cosh(\theta)x+\sinh(\theta)y,\sinh(\theta)x + \cosh(\theta)y )$

(c) nonlin\_shear($\theta$): $(x, y) \rightarrow (x, y + \theta x^2)$

(d) warp($\theta$): $(x, y) \rightarrow \mbox{rotate}(\theta \sqrt{x^2+y^2})(x, y)$
:::

::: {.problem #prob-mit18s096ps-1-q1 origin="external" source="mit18s096ps-1-q1"}
(a) Suppose that $L[x]$ is a linear operation (for $x$ in some vector space $V$, with outputs $L[x]$ in some other vector space $W$). If $f(x) = L[x] + y$ for a constant $y \in W$, what is $f'(x)$ (in terms of $L$ and/or $y$)?

(b) Give the derivatives of $f(A) = A^T$ (transpose) and $g(A) = 1 + \operatorname{tr} A$ (trace) as special cases of the rule you derived in the previous part.
:::
