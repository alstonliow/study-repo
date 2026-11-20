<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs221hw-6-q3" status="draft"}
**(a)** $Y\rightarrow A_0$, $Y\rightarrow A_1$, $Y\rightarrow A_2$. Each label depends only on the true label, and the annotators are conditionally independent given $Y$, so there are no edges between the $A_i$.

**(b)** A perfect annotator copies $Y$:

| $y$ | $p(A_0=\text{good}\mid Y=y)$ | $p(A_0=\text{bad}\mid Y=y)$ |
|---|---|---|
| good | $1$ | $0$ |
| bad | $0$ | $1$ |

**(c)** A uniform guesser ignores $Y$:

| $y$ | $p(A_0=\text{good}\mid Y=y)$ | $p(A_0=\text{bad}\mid Y=y)$ |
|---|---|---|
| good | $0.5$ | $0.5$ |
| bad | $0.5$ | $0.5$ |
:::

::: {.solution for="prob-bn-mle-code" status="draft"}
```{.python}
import itertools


def mle(structure, data, pseudocount=0):
    """Count-and-normalize estimate of every table: dict var -> (parents, cpt)."""
    net = {}
    for var, (parents, domain) in structure.items():
        rows = itertools.product(*(structure[u][1] for u in parents))
        counts = {u: {v: pseudocount for v in domain} for u in rows}
        for x in data:
            counts[tuple(x[u] for u in parents)][x[var]] += 1
        cpt = {}
        for u, row in counts.items():
            total = sum(row.values())
            cpt[u] = {v: (c / total if total else 1 / len(domain)) for v, c in row.items()}
        net[var] = (parents, cpt)
    return net
```

1. `itertools.product` over the parents' domains lists every tuple of parent values, including those that never occur in the data; with no parents it yields the single empty tuple.
2. Each row starts at the pseudocount for every value, and each example adds $1$ to the entry given by its parent values and its own value. Normalizing a row gives $\hat p(x\mid u)$, with Laplace smoothing when the pseudocount is positive.
3. A row with no counts and no pseudocount carries no information; it is set to the uniform distribution so that the result is still a valid network.
:::
