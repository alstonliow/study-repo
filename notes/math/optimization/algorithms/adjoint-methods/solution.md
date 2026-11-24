<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit18s096ps-2-q1" status="draft"}
(a) Put $x=A^{-1}b$ and $s=c^{\mathsf T}x$, so $f=s^2$.

1. $df=2s\,c^{\mathsf T}dx$, and by @thm-differential-inverse $dx=d(A^{-1})b=-A^{-1}dA\,x$.

2. So $df=-2s\,c^{\mathsf T}A^{-1}\,dA\,x$, and replacing $dA$ by $\partial A/\partial p_1=e_1e_2^{\mathsf T}+e_2e_1^{\mathsf T}$,

$$\frac{\partial f}{\partial p_1}=-2\,(c^{\mathsf T}A^{-1}b)\;c^{\mathsf T}A^{-1}\bigl(e_1e_2^{\mathsf T}+e_2e_1^{\mathsf T}\bigr)A^{-1}b .$$

(b) Group $-2s\,c^{\mathsf T}A^{-1}$ as one row vector $v^{\mathsf T}$, the adjoint (@def-adjoint-linear). Since $A=A^{\mathsf T}$, $v=A^{-1}(-2s\,c)$.

1. Solve $Ax=b$ (tridiagonal, $\Theta(n)$); set $s=c^{\mathsf T}x$ and $f=s^2$.
2. Solve $Av=-2s\,c$ (tridiagonal, $\Theta(n)$).
3. Then $df=v^{\mathsf T}dA\,x$, and $\partial A/\partial p_k=e_ke_{k+1}^{\mathsf T}+e_{k+1}e_k^{\mathsf T}$ gives $\partial f/\partial p_k=v_kx_{k+1}+v_{k+1}x_k$ for $k=1,\dots,n-1$: $\Theta(1)$ each, $\Theta(n)$ in all.

The cost is independent of how many parameters there are beyond the $\Theta(n)$ loop, which is the point of the adjoint method (@thm-adjoint-gradient).

(c) A Python version with a banded solver:

```python
import numpy as np
from scipy.linalg import solve_banded

def tridiag_solve(a, p, rhs):
    ab = np.zeros((3, len(a)))
    ab[0, 1:], ab[1, :], ab[2, :-1] = p, a, p
    return solve_banded((1, 1), ab, rhs)

def f_and_grad(a, p, b, c):
    x = tridiag_solve(a, p, b)               # x = A^{-1} b
    s = c @ x
    v = tridiag_solve(a, p, -2 * s * c)      # adjoint solve
    return s**2, v[:-1] * x[1:] + v[1:] * x[:-1]

rng = np.random.default_rng(0)
n = 8
a, p = rng.standard_normal(n), rng.standard_normal(n - 1)
b, c = rng.standard_normal(n), rng.standard_normal(n)
f0, g = f_and_grad(a, p, b, c)
dp = 1e-7 * rng.standard_normal(n - 1)
f1, _ = f_and_grad(a, p + dp, b, c)
print(f1 - f0, g @ dp)
```

It prints $4.780812\times10^{-6}$ and $4.780809\times10^{-6}$: relative difference $5\times10^{-7}$, the size expected for a forward difference with this step (@thm-finite-difference-error).
:::
