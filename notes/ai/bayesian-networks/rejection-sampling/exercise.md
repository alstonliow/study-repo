::: {#prob-rejection-sampling-code .problem .coding origin="adapted" source="res-stanford-cs221-hw-bayesian"}
Estimate a conditional distribution in a Bayesian network by rejection sampling (@def-rejection-sampling). The network is stored as in @prob-bn-joint-probability-code: a dict from each variable to `(parents, cpt)`, the variables in a topological order.

Write `rejection_sampling(net, query, evidence, n, rng)`.

- Draw `n` samples by *forward sampling*: visit the variables in the order of `net` and draw each one from its row of the table, given the values already drawn for its parents. `rng` is a `random.Random`; use it for all randomness.
- Accept the samples that agree with `evidence`, a dict from some variables to values.
- Return a dict from each value $q$ of the variable `query` to the fraction of accepted samples with `query` equal to $q$ (values that never occur may be left out), or `None` if no sample is accepted.

```{.python .starter}
def rejection_sampling(net, query, evidence, n, rng):
    """Estimate P(query | evidence) from n forward samples: dict value -> fraction."""
    ...
```

```{.python .tests}
import itertools
import random

net = {
    "C": ((), {(): {0: 0.5, 1: 0.5}}),
    "S": (("C",), {(0,): {0: 0.5, 1: 0.5}, (1,): {0: 0.9, 1: 0.1}}),
    "R": (("C",), {(0,): {0: 0.8, 1: 0.2}, (1,): {0: 0.2, 1: 0.8}}),
    "W": (("S", "R"), {(0, 0): {0: 0.99, 1: 0.01}, (0, 1): {0: 0.1, 1: 0.9},
                       (1, 0): {0: 0.1, 1: 0.9}, (1, 1): {0: 0.01, 1: 0.99}}),
}


def exact(query, evidence):
    """P(query | evidence) by summing the joint over all assignments."""
    scores = {}
    for vals in itertools.product([0, 1], repeat=4):
        x = dict(zip("CSRW", vals))
        if any(x[v] != e for v, e in evidence.items()):
            continue
        p = 1.0
        for var, (parents, cpt) in net.items():
            p *= cpt[tuple(x[u] for u in parents)][x[var]]
        scores[x[query]] = scores.get(x[query], 0) + p
    z = sum(scores.values())
    return {q: s / z for q, s in scores.items()}


def test_close_to_exact():
    rng = random.Random(10)
    for query, evidence in [("R", {"W": 1}), ("C", {"W": 1, "S": 0}), ("S", {})]:
        est = rejection_sampling(net, query, evidence, 20000, rng)
        ex = exact(query, evidence)
        for q in (0, 1):
            assert abs(est.get(q, 0) - ex[q]) < 0.02, (query, evidence, est, ex)


def test_impossible_evidence():
    certain = {"X": ((), {(): {0: 1.0, 1: 0.0}}), "Y": (("X",), {(0,): {0: 0.5, 1: 0.5}, (1,): {0: 0.5, 1: 0.5}})}
    assert rejection_sampling(certain, "Y", {"X": 1}, 500, random.Random(0)) is None


def test_deterministic_child():
    copy = {"X": ((), {(): {"a": 0.3, "b": 0.7}}), "Y": (("X",), {("a",): {"a": 1.0}, ("b",): {"b": 1.0}})}
    est = rejection_sampling(copy, "X", {"Y": "b"}, 300, random.Random(1))
    assert est == {"b": 1.0}
```
:::
