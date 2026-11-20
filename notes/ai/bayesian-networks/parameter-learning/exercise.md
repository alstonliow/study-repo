::: {.problem #prob-cs221hw-6-q3 origin="external" source="cs221hw-6-q3"}
Later in life, you're a data engineer managing a team of human annotators. Your data consists of labels indicating whether a given conversation between an LLM and a human was **good** or **bad**.

But you've run into a problem: your annotators can't seem to perfectly agree on their ratings, no matter how careful you are in your instructions! You vaguely remember something about Bayesian networks from CS221, so you decide to use them to help you assess annotator quality.

For this problem, we'll assume you have the true labels for each conversation. (In the real world, this will not be the case!) Also assume that each annotator's label depends only on the true label of the conversation, and that annotators make mistakes independently of each other: once you know the true label, how one annotator labeled the conversation tells you nothing about how another one did.

(a) Let's consider a single conversation and three annotators who each label it. List the edges in the Bayesian network for this scenario, using the random variables $Y$, the true label of the conversation, and $A_0$, $A_1$, and $A_2$, the labels that the three annotators give it. Each variable takes the values $\text{good}$ and $\text{bad}$.

*Expected:* A list of edges in the Bayesian network, in the format of $\text{variable1} \rightarrow \text{variable2}$.

(b) Fill out the following table with the local conditional distribution $p(A_0 = a \mid Y = y)$ of a perfect annotator, who always gives the true label.

*Expected:* A completed table with the local conditional distribution.

  $y$              $p(A_0 = \text{good} \mid Y = y)$   $p(A_0 = \text{bad} \mid Y = y)$
  ------------------ --------------------------------------- --------------------------------------
  $\text{good}$                                           
  $\text{bad}$

(c) Fill out the following table with the local conditional distribution $p(A_0 = a \mid Y = y)$ of an annotator who guesses uniformly at random.

*Expected:* A completed table with the local conditional distribution.

  $y$              $p(A_0 = \text{good} \mid Y = y)$   $p(A_0 = \text{bad} \mid Y = y)$
  ------------------ --------------------------------------- --------------------------------------
  $\text{good}$                                           
  $\text{bad}$

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::

::: {#prob-bn-mle-code .problem .coding origin="adapted" source="res-stanford-cs221-hw-bayesian"}
Learn the tables of a Bayesian network from fully observed data by count and normalize (@def-count-normalize), optionally with Laplace smoothing (@def-laplace-smoothing). Every variable has its own table (no shared parameters).

Write `mle(structure, data, pseudocount=0)`.

- `structure` maps each variable to a pair `(parents, domain)`: a tuple of parent variables and the list of the variable's values.
- `data` is a list of full assignments, dicts from every variable to a value.
- Return the network in the format of @prob-bn-joint-probability-code: a dict from each variable to `(parents, cpt)`, where `cpt` has one row for every tuple of parent values (all combinations of the parents' domains, in the order of `parents`), and each row gives every value of the domain its estimated probability. Add `pseudocount` to every count before normalizing. A row whose counts are all $0$ is uniform.

```{.python .starter}
import itertools


def mle(structure, data, pseudocount=0):
    """Count-and-normalize estimate of every table: dict var -> (parents, cpt)."""
    ...
```

```{.python .tests}
def close(row, expected):
    return row.keys() == expected.keys() and all(abs(row[k] - expected[k]) < 1e-12 for k in row)


structure = {"G": ((), ["c", "d"]), "R": (("G",), [1, 2, 3])}
data = [{"G": "d", "R": 3}, {"G": "d", "R": 3}, {"G": "d", "R": 1}, {"G": "c", "R": 2}]


def test_counts():
    net = mle(structure, data)
    assert net["G"][0] == () and net["R"][0] == ("G",)
    assert close(net["G"][1][()], {"c": 0.25, "d": 0.75})
    assert close(net["R"][1][("d",)], {1: 1 / 3, 2: 0.0, 3: 2 / 3})
    assert close(net["R"][1][("c",)], {1: 0.0, 2: 1.0, 3: 0.0})


def test_laplace_smoothing():
    net = mle(structure, data, pseudocount=1)
    assert close(net["G"][1][()], {"c": 2 / 6, "d": 4 / 6})
    assert close(net["R"][1][("d",)], {1: 2 / 6, 2: 1 / 6, 3: 3 / 6})


def test_unseen_parent_values_are_uniform():
    s = {"A": ((), [0, 1]), "B": ((), [0, 1]), "C": (("A", "B"), ["x", "y"])}
    net = mle(s, [{"A": 0, "B": 1, "C": "x"}])
    assert set(net["C"][1]) == {(0, 0), (0, 1), (1, 0), (1, 1)}
    assert close(net["C"][1][(0, 1)], {"x": 1.0, "y": 0.0})
    assert close(net["C"][1][(1, 1)], {"x": 0.5, "y": 0.5})


def test_no_data():
    net = mle(structure, [])
    assert close(net["G"][1][()], {"c": 0.5, "d": 0.5})
```
:::
