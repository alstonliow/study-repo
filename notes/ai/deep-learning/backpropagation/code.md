<!-- Added 2026-11-18 for Stanford CS221 Lecture 4; our own minimal version of the lecture's computation-graph library (scalar nodes only). -->

::: {#exm-backpropagation-code-1 .example name="A tiny backpropagation library" origin="self"}

Needs NumPy. Each node stores its value, its dependencies and a function returning its local partial derivatives; `backpropagation` is the algorithm above. The second graph uses `w` three times, so its gradient is a sum of three contributions.

```{.python .runnable packages="numpy"}
import numpy as np

class Node:
    def __init__(self, f, df, *deps):
        self.deps, self.df = deps, df          # df(values) -> local partials
        self.value = f(*[d.value for d in deps])
        self.grad = 0.0

def Input(v):  return Node(lambda: np.array(v, dtype=float), None)
def Add(a, b): return Node(lambda x, y: x + y, lambda x, y: (1.0, 1.0), a, b)
def Mul(a, b): return Node(lambda x, y: x * y, lambda x, y: (y, x), a, b)
def Square(a): return Node(lambda x: x ** 2, lambda x: (2 * x,), a)

def topological_order(root):
    order, seen = [], set()
    def visit(v):
        if id(v) not in seen:
            seen.add(id(v))
            for d in v.deps: visit(d)
            order.append(v)
    visit(root)
    return order

def backpropagation(root):
    order = topological_order(root)
    for v in order: v.grad = 0.0
    root.grad = 1.0
    for v in reversed(order):
        if v.df is None: continue
        partials = v.df(*[d.value for d in v.deps])
        for d, p in zip(v.deps, partials):
            d.grad = d.grad + v.grad * p

x1, x2 = Input(2.0), Input(3.0)
y = Square(Add(x1, x2))          # (x1 + x2)^2
backpropagation(y)
print(y.value, x1.grad, x2.grad)
w = Input(0.5); z = Mul(Mul(w, w), w)   # w^3, w used three times
backpropagation(z)
print(z.value, w.grad)
```

```text
25.0 10.0 10.0
0.125 0.75
```

:::
