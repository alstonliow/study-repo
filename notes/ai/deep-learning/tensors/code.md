<!-- Added 2026-11-18 for Stanford CS221 Lecture 1 (tensors); our own NumPy code, run once locally for the printed output. -->

::: {#exm-tensors-code-1 .example name="Shape, views, broadcasting and batched products in NumPy" origin="self"}

Needs NumPy. The slice `y` is a view, so writing to it changes `x`; `b` is broadcast over the first two axes; `x @ w` multiplies each of the two $3\times4$ slices by the same $4\times2$ matrix.

```{.python .runnable packages="numpy"}
import numpy as np
x = np.arange(24.0).reshape(2, 3, 4)   # rank 3, shape (2, 3, 4)
print(x.ndim, x.shape, x.size)
y = x[1, :, :]                          # slice: shape (3, 4), a view
y[0, 0] = -1.0
print(x[1, 0, 0])                       # the original changed too
b = np.array([10.0, 20.0, 30.0, 40.0])  # shape (4,) broadcasts over (2, 3, 4)
print((x + b)[0, 0])
w = np.ones((4, 2))
print((x @ w).shape)                    # batched matrix product
```

```text
3 (2, 3, 4) 24
-1.0
[10. 21. 32. 43.]
(2, 3, 2)
```

:::

::: {#exm-tensors-code-2 .example name="Loop versus one tensor operation" origin="self"}

Needs NumPy. The same $120\times120$ matrix product by a Python triple loop and by `@`; the results agree and the tensor operation is more than a hundred times faster (exact times depend on the machine).

```{.python .runnable packages="numpy"}
import numpy as np, time
n = 120
a = np.random.default_rng(0).random((n, n))
b = np.random.default_rng(1).random((n, n))
t = time.perf_counter()
c = [[sum(a[i, k] * b[k, j] for k in range(n)) for j in range(n)] for i in range(n)]
loop = time.perf_counter() - t
t = time.perf_counter()
d = a @ b
vec = time.perf_counter() - t
print(np.allclose(c, d), f"loop/vectorized time ratio > 100: {loop / vec > 100}")
```

```text
True loop/vectorized time ratio > 100: True
```

:::
