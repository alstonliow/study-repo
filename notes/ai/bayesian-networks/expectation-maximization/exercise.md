::: {#prob-em-hidden-variable-code .problem .coding origin="adapted" source="res-stanford-cs221-hw-bayesian"}
Learn the tables of a Bayesian network in which one variable is never observed, by expectation maximization (@def-expectation-maximization). Networks are stored as in @prob-bn-joint-probability-code and structures as in @prob-bn-mle-code; the starter provides `joint`.

Write `em(structure, net, data, hidden, iterations)`.

- `net` holds the initial tables. `hidden` is the unobserved variable, and every example in `data` assigns all the other variables.
- *E-step*: for each example $e$ and each value $h$ of `hidden`, compute the weight $q_e(h)=P(\text{hidden}=h\mid e)$ under the current tables.
- *M-step*: complete each example with each value $h$, count the completed example with weight $q_e(h)$, and set every table to the normalized weighted counts. A row whose weighted counts are all $0$ keeps its current probabilities.
- Return the tables after `iterations` rounds of E-step and M-step, in the same format. Do not change `net`.

```{.python .starter}
def joint(net, x):
    p = 1.0
    for var, (parents, cpt) in net.items():
        p *= cpt[tuple(x[u] for u in parents)].get(x[var], 0.0)
    return p


def em(structure, net, data, hidden, iterations):
    """Run EM for one hidden variable; return the new tables."""
    ...
```

```{.python .tests}
import copy
import math

# H is hidden; two annotators A and B report it, each with its own error rate
structure = {"H": ((), [0, 1]), "A": (("H",), [0, 1]), "B": (("H",), [0, 1])}
init = {
    "H": ((), {(): {0: 0.5, 1: 0.5}}),
    "A": (("H",), {(0,): {0: 0.8, 1: 0.2}, (1,): {0: 0.2, 1: 0.8}}),
    "B": (("H",), {(0,): {0: 0.6, 1: 0.4}, (1,): {0: 0.4, 1: 0.6}}),
}
data = [{"A": 1, "B": 1}, {"A": 1, "B": 0}, {"A": 0, "B": 0}, {"A": 1, "B": 1}]


def log_likelihood(net):
    return sum(math.log(sum(joint(net, dict(e, H=h)) for h in (0, 1))) for e in data)


def test_one_iteration_by_hand():
    net = em(structure, init, data, "H", 1)
    # q(H=1 | e): (1,1): 0.48/0.56 = 6/7; (1,0): 0.32/0.44 = 8/11; (0,0): 0.08/0.56 = 1/7
    q = [6 / 7, 8 / 11, 1 / 7, 6 / 7]
    s1 = sum(q)
    assert abs(net["H"][1][()][1] - s1 / 4) < 1e-12
    a1 = (q[0] + q[1] + q[3]) / s1            # P(A=1 | H=1)
    assert abs(net["A"][1][(1,)][1] - a1) < 1e-12
    b1 = (q[0] + q[3]) / s1                   # P(B=1 | H=1)
    assert abs(net["B"][1][(1,)][1] - b1) < 1e-12
    b0 = (2 * (1 - q[0])) / (4 - s1)          # P(B=1 | H=0)
    assert abs(net["B"][1][(0,)][1] - b0) < 1e-12


def test_likelihood_never_decreases():
    previous = log_likelihood(init)
    for k in range(1, 8):
        current = log_likelihood(em(structure, init, data, "H", k))
        assert current >= previous - 1e-12
        previous = current


def test_tables_valid_and_net_unchanged():
    before = copy.deepcopy(init)
    net = em(structure, init, data, "H", 3)
    assert init == before, "net was modified"
    for var, (parents, cpt) in net.items():
        assert parents == init[var][0]
        for row in cpt.values():
            assert set(row) == {0, 1} and abs(sum(row.values()) - 1) < 1e-12


def test_zero_iterations():
    assert em(structure, init, data, "H", 0) == init
```
:::
