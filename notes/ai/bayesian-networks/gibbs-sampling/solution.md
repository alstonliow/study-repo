<!-- Solutions marked status="draft" were written by Claude in our own words,
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-gibbs-sampling-code" status="draft"}
```{.python}
def joint(net, x):
    p = 1.0
    for var, (parents, cpt) in net.items():
        p *= cpt[tuple(x[u] for u in parents)].get(x[var], 0.0)
    return p


def gibbs_sampling(net, query, evidence, init, sweeps, rng):
    """Estimate P(query | evidence) by Gibbs sampling: dict value -> fraction."""
    x = dict(init)
    free = [v for v in net if v not in evidence]
    values = {v: sorted({val for row in net[v][1].values() for val in row}, key=repr) for v in free}
    counts = {}
    for _ in range(sweeps):
        for v in free:
            weights = []
            for val in values[v]:
                x[v] = val
                weights.append(joint(net, x))
            x[v] = rng.choices(values[v], weights=weights)[0]
        counts[x[query]] = counts.get(x[query], 0) + 1
    return {q: c / sweeps for q, c in counts.items()}
```

1. The conditional distribution of $X_i$ given all the other variables is proportional to the joint probability with $x_i$ set to each value in turn, as in the definition; `rng.choices` with these weights samples from it without normalising them first.
2. Only the factors of $X_i$ and of its children depend on $x_i$ (its Markov blanket, @prp-gibbs-markov-blanket), so a faster version would multiply only those; the full joint is simpler and gives the same distribution.
3. Evidence variables are never resampled, so every state of the chain agrees with the evidence. Starting from a state of positive probability, every later state has positive probability too, so the weights never all vanish.
4. Successive sweeps are correlated, so Gibbs sampling needs more sweeps than independent samples for the same accuracy; in exchange it never rejects a sample.
:::
