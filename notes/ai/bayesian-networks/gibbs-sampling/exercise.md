::: {#prob-gibbs-sampling-code .problem .coding origin="adapted" source="res-stanford-cs221-hw-bayesian"}
Estimate a conditional distribution in a Bayesian network by Gibbs sampling (@def-gibbs-sampling). The network is stored as in @prob-bn-joint-probability-code; the starter provides `joint`, the joint probability of a full assignment.

Write `gibbs_sampling(net, query, evidence, init, sweeps, rng)`.

- `init` is a full assignment that agrees with `evidence` and has positive probability. Start from a copy of it.
- One *sweep* visits every variable not in `evidence`, in the order of `net`, and replaces its value by a sample from its conditional distribution given the current values of all other variables. The values of a variable are the keys of the rows of its table.
- After each sweep record the value of `query`. Return a dict from each value $q$ of `query` to the fraction of the `sweeps` sweeps after which `query` equalled $q$ (values that never occur may be left out). `rng` is a `random.Random`; use it for all randomness.

```{.python .starter}
def joint(net, x):
    p = 1.0
    for var, (parents, cpt) in net.items():
        p *= cpt[tuple(x[u] for u in parents)].get(x[var], 0.0)
    return p


def gibbs_sampling(net, query, evidence, init, sweeps, rng):
    """Estimate P(query | evidence) by Gibbs sampling: dict value -> fraction."""
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
    scores = {}
    for vals in itertools.product([0, 1], repeat=4):
        x = dict(zip("CSRW", vals))
        if all(x[v] == e for v, e in evidence.items()):
            scores[x[query]] = scores.get(x[query], 0) + joint(net, x)
    z = sum(scores.values())
    return {q: s / z for q, s in scores.items()}


def test_close_to_exact():
    rng = random.Random(11)
    for query, evidence in [("R", {"W": 1}), ("C", {"W": 1, "S": 0}), ("S", {"R": 1})]:
        init = {"C": 1, "S": 1, "R": 1, "W": 1}
        init.update(evidence)
        est = gibbs_sampling(net, query, evidence, init, 20000, rng)
        ex = exact(query, evidence)
        for q in (0, 1):
            assert abs(est.get(q, 0) - ex[q]) < 0.03, (query, evidence, est, ex)


def test_evidence_and_init_unchanged():
    init = {"C": 0, "S": 0, "R": 1, "W": 1}
    before = dict(init)
    est = gibbs_sampling(net, "W", {"W": 1}, init, 200, random.Random(2))
    assert est == {1: 1.0}
    assert init == before, "init was modified"


def test_deterministic_child():
    copy = {"X": ((), {(): {"a": 0.3, "b": 0.7}}), "Y": (("X",), {("a",): {"a": 1.0}, ("b",): {"b": 1.0}})}
    est = gibbs_sampling(copy, "X", {"Y": "a"}, {"X": "a", "Y": "a"}, 300, random.Random(3))
    assert est == {"a": 1.0}
```
:::
