<!-- Solutions marked status="draft" were written by Claude in our own words,
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-rejection-sampling-code" status="draft"}
```{.python}
def forward_sample(net, rng):
    x = {}
    for var, (parents, cpt) in net.items():
        row = cpt[tuple(x[u] for u in parents)]
        u, acc = rng.random(), 0.0
        for value, p in row.items():
            acc += p
            if u < acc:
                break
        x[var] = value                         # the last value if rounding left u >= acc
    return x


def rejection_sampling(net, query, evidence, n, rng):
    """Estimate P(query | evidence) from n forward samples: dict value -> fraction."""
    counts = {}
    for _ in range(n):
        x = forward_sample(net, rng)
        if all(x[v] == e for v, e in evidence.items()):
            counts[x[query]] = counts.get(x[query], 0) + 1
    total = sum(counts.values())
    if total == 0:
        return None
    return {q: c / total for q, c in counts.items()}
```

1. Forward sampling visits the variables in topological order, so the parents of a variable already have values when it is drawn. One uniform number $u\in[0,1)$ and the running sum of the row's probabilities select the value whose interval contains $u$.
2. A forward sample has exactly the joint distribution of the network. Among the samples with $E=e$, the fraction with $Q=q$ therefore converges to $P(Q=q\mid E=e)$.
3. The expected number of accepted samples is $nP(E=e)$, so the method wastes most samples when the evidence is unlikely; with impossible evidence it accepts none and returns `None`.
:::
