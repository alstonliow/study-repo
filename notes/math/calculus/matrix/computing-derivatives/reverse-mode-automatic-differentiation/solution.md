<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18s096-8-q1" status="draft"}
Assume $f$ is twice continuously differentiable. Let $M=\partial(\nabla_xf)/\partial p$, the $n\times N$ matrix of mixed second derivatives $M_{ik}=\partial^2f/\partial x_i\partial p_k$.

1. *The left side.* $h=g(z)$ with $z=\nabla_xf(x,p)$. Changing only $p$, $dz=M\,dp$, so $dh=\nabla g(z)^{\mathsf T}M\,dp$ and $\nabla_ph=M^{\mathsf T}\nabla g(z)$.

2. *The right side.* Fix $w=\nabla g(z)$ and $p$. By the chain rule, $\frac{\partial}{\partial\alpha}\nabla_pf(x+\alpha w,p)\big|_{\alpha=0}=\frac{\partial(\nabla_pf)}{\partial x}\,w$, where $\frac{\partial(\nabla_pf)}{\partial x}$ is the $N\times n$ matrix with entries $\partial^2f/\partial p_k\partial x_i$.

3. Mixed partial derivatives of a $C^2$ function commute, so $\frac{\partial(\nabla_pf)}{\partial x}=M^{\mathsf T}$, and the two sides agree.

4. *Cost.* The right side is one directional (forward-mode) derivative of the reverse-mode gradient $\nabla_pf$: by @prp-forward-over-reverse it costs a small multiple of one evaluation of $f$, and the $n\times N$ matrix $M$ is never formed.

*Example* (in Python, with the gradients written by hand in place of reverse mode and a centred difference in place of the dual number): $f(x,p)=\sin(p^{\mathsf T}Ax)$ with a random $4\times3$ matrix $A$, and $g(z)=\tfrac12\lVert z\rVert^2$, so $\nabla g(z)=z$, $\nabla_xf=\cos(s)A^{\mathsf T}p$, $\nabla_pf=\cos(s)Ax$ with $s=p^{\mathsf T}Ax$.

```python
import numpy as np
rng = np.random.default_rng(0)
n, N = 3, 4
A = rng.standard_normal((N, n)); x = rng.standard_normal(n); p = rng.standard_normal(N)
grad_x = lambda x, p: np.cos(p @ A @ x) * (A.T @ p)
grad_p = lambda x, p: np.cos(p @ A @ x) * (A @ x)
h = lambda x, p: 0.5 * grad_x(x, p) @ grad_x(x, p)

w, eps = grad_x(x, p), 1e-6                      # w = ∇g(z) = z
formula = (grad_p(x + eps*w, p) - grad_p(x - eps*w, p)) / (2*eps)
fd = np.array([(h(x, p + eps*e) - h(x, p - eps*e)) / (2*eps) for e in np.eye(N)])
print(formula, fd)
```

Both give $(-0.469085,\,-0.222573,\,-1.452336,\,1.690206)$; they differ by $6\times10^{-10}$.
:::
