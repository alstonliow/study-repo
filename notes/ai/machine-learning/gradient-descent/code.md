<!-- Added 2026-11-18 for Stanford CS221 Lecture 2: the lecture's gradient descent code for linear regression, adapted (MIT licence, see NOTICES.md). -->

::: {#exm-gradient-descent-code-1 .example name="Gradient descent for linear regression" origin="adapted" source="cs221-2"}

Needs NumPy. Ten steps on the data of @exm-linear-regression-1, as in @fig-gradient-descent-1.

```{.python .runnable packages="numpy"}
# Adapted from the CS221 lecture code: Parameters1D dataclass replaced by two floats, helpers inlined, plotting dropped.
import numpy as np

training_data = [(1, 4), (2, 6), (4, 7)]  # (hours studied, exam score)

def train_loss(w, b):
    return np.mean([(w * x + b - y) ** 2 for x, y in training_data])

def grad_train_loss(w, b):
    grads = [2 * (w * x + b - y) * np.array([x, 1]) for x, y in training_data]
    return np.mean(grads, axis=0)

w, b = 0.0, 1.0
learning_rate = 0.01
for step in range(10):
    g = grad_train_loss(w, b)
    w, b = w - learning_rate * g[0], b - learning_rate * g[1]
print(round(train_loss(w, b), 3), round(w, 3), round(b, 3))
```

```text
1.747 1.279 1.524
```

:::
