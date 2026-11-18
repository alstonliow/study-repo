<!-- Added 2026-11-18 for Stanford CS221 Lecture 3; our own vectorized NumPy code. -->

::: {#exm-logistic-regression-code-1 .example name="Logistic regression by gradient descent" origin="self"}

Needs NumPy. The run of @exm-logistic-regression-1, with all examples handled by one tensor operation per step.

```{.python .runnable packages="numpy"}
import numpy as np

X = np.array([[1.0, 2.0], [2.0, 0.0], [0.0, 0.0]])
y = np.array([-1.0, 1.0, -1.0])
sigma = lambda z: 1 / (1 + np.exp(-z))

w, b, eta = np.zeros(2), 0.0, 1.0
for step in range(20):
    m = y * (X @ w + b)                 # margins
    c = -sigma(-m) * y                  # dLoss/dlogit per example
    w, b = w - eta * (c @ X) / len(y), b - eta * c.mean()
m = y * (X @ w + b)
print(np.round(w, 2), round(b, 2))
print("logistic loss", round(np.mean(np.log(1 + np.exp(-m))), 3), "zero-one loss", np.mean(m <= 0))
```

```text
[ 1.92 -1.78] -1.51
logistic loss 0.111 zero-one loss 0.0
```

:::
