<!-- Solutions marked status="draft" were written by Claude in our own words,
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-em-hidden-variable-code" status="draft"}
```{.python}
import copy


def joint(net, x):
    p = 1.0
    for var, (parents, cpt) in net.items():
        p *= cpt[tuple(x[u] for u in parents)].get(x[var], 0.0)
    return p


def em(structure, net, data, hidden, iterations):
    """Run EM for one hidden variable; return the new tables."""
    net = copy.deepcopy(net)
    for _ in range(iterations):
        counts = {v: {u: {x: 0.0 for x in structure[v][1]} for u in cpt}
                  for v, (_, cpt) in net.items()}
        for e in data:
            # E-step: weights q_e(h), proportional to the joint of the completed example
            done = [dict(e, **{hidden: h}) for h in structure[hidden][1]]
            w = [joint(net, x) for x in done]
            z = sum(w)
            # M-step counts: each completed example with weight q_e(h)
            for x, wx in zip(done, w):
                for v, (parents, _) in net.items():
                    counts[v][tuple(x[u] for u in parents)][x[v]] += wx / z
        for v, (parents, cpt) in net.items():
            for u, row in counts[v].items():
                total = sum(row.values())
                if total > 0:
                    cpt[u] = {x: c / total for x, c in row.items()}
    return net
```

1. The E-step needs $P(\text{hidden}=h\mid e)$, which is the joint probability of the completed example divided by the sum over all $h$. With one hidden variable this sum has one term per value, so no general inference algorithm is needed.
2. The M-step is count and normalize (@def-count-normalize) with fractional counts: each example contributes weight $q_e(h)$ to the rows selected by its completion with $h$, and the weights of one example sum to $1$.
3. `dict(e, **{hidden: h})` builds the completed example without changing `e`, and `copy.deepcopy` keeps the caller's tables unchanged.
4. Each round of EM never lowers the likelihood of the data, which the second test checks; EM converges to a local maximum or saddle point, so the result depends on the initial tables.
:::
