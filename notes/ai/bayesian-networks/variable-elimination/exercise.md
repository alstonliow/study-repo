::: {.problem #prob-cs188hw-7-q1 origin="external" source="cs188hw-7-q1"}
**Bayes Nets.** Consider the following Bayes Net that has four variables $E$, $S$, $M$, and $B$. The associated probabilities are also given in the following tables.

| $E$ | $P(E)$ |
|---|---|
| $+e$ | 0.4 |
| $-e$ | 0.6 |

| $M$ | $P(M)$ |
|---|---|
| $+m$ | 0.1 |
| $-m$ | 0.9 |

| $E$ | $M$ | $S$ | $P(S\mid E,M)$ |
|---|---|---|---|
| $+e$ | $+m$ | $+s$ | 1.0 |
| $+e$ | $+m$ | $-s$ | 0.0 |
| $+e$ | $-m$ | $+s$ | 0.8 |
| $+e$ | $-m$ | $-s$ | 0.2 |
| $-e$ | $+m$ | $+s$ | 0.3 |
| $-e$ | $+m$ | $-s$ | 0.7 |
| $-e$ | $-m$ | $+s$ | 0.1 |
| $-e$ | $-m$ | $-s$ | 0.9 |

| $M$ | $B$ | $P(B\mid M)$ |
|---|---|---|
| $+m$ | $+b$ | 1.0 |
| $+m$ | $-b$ | 0.0 |
| $-m$ | $+b$ | 0.1 |
| $-m$ | $-b$ | 0.9 |

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.2cm, y=1.1cm]
\node[vertex] (E) at (0,1) {$E$};
\node[vertex] (M) at (2,1) {$M$};
\node[vertex] (S) at (1,0) {$S$};
\node[vertex] (B) at (3,0) {$B$};
\draw[->] (E) -- (S);
\draw[->] (M) -- (S);
\draw[->] (M) -- (B);
\end{tikzpicture}
\end{center}
```

*Figure 1: Bayes Net and probability tables.*

**In the following five questions, do not just answer with a numerical value. Write explicitly what probability expression you are calculating. For instance you should write $P(A)P(B)=0.2$ instead of just 0.2.**

1. Write an expression to compute the value of the joint distribution $P(-e,-s,-m,-b)$. What is its value?
2. Write an expression to compute the value of $P(+b)$. What is its value?
3. Write an expression to compute the value of $P(+m\mid+b)$. What is its value?
4. Write an expression to compute the value of $P(+m\mid+s,+b,+e)$. What is its value?
5. Write an expression to compute the value of $P(+e\mid+m)$. What is its value?

Now consider the following Bayes Net in which all variables are binary. We want to compute the query $P(B,D\mid+f)$, so we run variable elimination with the variable elimination ordering being $A,C,E,G$.

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.2cm, y=0.9cm]
\node[vertex] (A) at (0,2) {$A$};
\node[vertex] (B) at (0,1) {$B$};
\node[vertex] (C) at (0,0) {$C$};
\node[vertex] (D) at (-1,-1) {$D$};
\node[vertex] (E) at (0,-2) {$E$};
\node[vertex] (F) at (1,-3) {$F$};
\node[vertex] (G) at (2,-2) {$G$};
\draw[->] (A) -- (B);
\draw[->] (B) -- (C);
\draw[->] (C) -- (D);
\draw[->] (C) -- (E);
\draw[->] (D) -- (E);
\draw[->] (C) -- (F);
\draw[->] (E) -- (F);
\draw[->] (C) -- (G);
\draw[->] (F) -- (G);
\end{tikzpicture}
\end{center}
```

*Figure 2: Bayes Net.*

After observing evidence on $F$, we have the following factors:
$$
P(A),\ P(B\mid A),\ P(C\mid B),\ P(D\mid C),\ P(E\mid C,D),\ P(+f\mid C,E),\ P(G\mid C,+f)
$$
When we eliminate the variable $A$, we then create a new factor $f_1(B)=\sum_aP(B\mid a)\cdot P(a)$ and the remaining factors are:
$$
f_1(B),\ P(C\mid B),\ P(D\mid C),\ P(E\mid C,D),\ P(+f\mid C,E),\ P(G\mid C,+f).
$$

6. When we eliminate $C$ next, what is the new factor $f_2$ we obtain? Furthermore, list the leftover factors.
7. When we eliminate $E$ next, what is the new factor $f_3$ we obtain? Furthermore, list the leftover factors.
8. When we eliminate $G$ next, what is the new factor $f_4$ we obtain? Furthermore, list the leftover factors.
9. How can we compute $P(B,D\mid+f)$ using the factors from Q1.8? Explain in a couple of sentences.
10. Between $f_1$, $f_2$, $f_3$, and $f_4$, which is the largest factor (or equivalently whose table has the most rows)?
11. For the same query $P(B,D\mid+f)$, find a new variable elimination ordering that minimizes the size of the largest factor created. Fill in your ordering and generated factors below. Hint: The largest factor should have only 2 variables.

    | Variable Eliminated | Factor Generated |
    |---|---|

*Note (these notes):* Networks redrawn. The local file of the HW7 solutions is a web page, not the solutions, so these answers were checked only by our own computation.
:::

::: {.problem #prob-cs188d-7-q1 origin="external" source="cs188d-7-q1"}
**Variable Elimination.** Using the same Bayes Net (shown below), we want to compute $P(Y\mid+z)$. All variables have binary domains. Assume we run variable elimination to compute the answer to this query, with the following variable elimination ordering: $X,T,U,V,W$.

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.2cm, y=1.1cm]
\node[vertex] (T) at (2,2) {$T$};
\node[vertex] (U) at (0,1) {$U$};
\node[vertex] (V) at (1.4,1) {$V$};
\node[vertex] (W) at (2.6,1) {$W$};
\node[vertex] (X) at (4,1) {$X$};
\node[vertex] (Y) at (2,0) {$Y$};
\node[vertex] (Z) at (4,0) {$Z$};
\draw[->] (T) -- (U);
\draw[->] (T) -- (V);
\draw[->] (T) -- (W);
\draw[->] (T) -- (X);
\draw[->] (V) -- (Y);
\draw[->] (W) -- (Y);
\draw[->] (X) -- (Z);
\end{tikzpicture}
\end{center}
```

Complete the following description of the factors generated in this process:

After inserting evidence, we have the following factors to start out with:
$$
P(T),\ P(U\mid T),\ P(V\mid T),\ P(W\mid T),\ P(X\mid T),\ P(Y\mid V,W),\ P(+z\mid X)
$$

(a) When eliminating $X$ we generate a new factor $f_1$ as follows, which leaves us with the factors:
$$
f_1(+z\mid T)=\sum_xP(x\mid T)P(+z\mid x)\qquad P(T),\ P(U\mid T),\ P(V\mid T),\ P(W\mid T),\ P(Y\mid V,W),\ f_1(+z\mid T)
$$

(b) When eliminating $T$ we generate a new factor $f_2$ as follows, which leaves us with the factors:

(c) When eliminating $U$ we generate a new factor $f_3$ as follows, which leaves us with the factors:

(d) When eliminating $V$ we generate a new factor $f_4$ as follows, which leaves us with the factors:

(e) When eliminating $W$ we generate a new factor $f_5$ as follows, which leaves us with the factors:

(f) How would you obtain $P(Y\mid+z)$ from the factors left above:

(g) What is the size of the largest factor that gets generated during the above process?

(m) Does there exist a better elimination ordering (one which generates smaller largest factors)?

*Note (these notes):* Network redrawn from the factors listed in the statement.
:::

::: {#prob-join-factors-code .problem .coding origin="adapted" source="res-ucb-cs188-projects-tracking" solution="withheld" packages="numpy"}
Represent a factor (@def-factor) as a pair `(scope, table)`: `scope` is a tuple of distinct variable names and `table` a NumPy array with one axis per variable, in the order of `scope`. A variable with $k$ values takes the values `0, ..., k-1`, and a variable has the same number of values in every factor where it appears.

Write `join_factors(factors)`, the join of a non-empty list of factors. The scope of the result lists the variables in the order of their first appearance, going through the factors in order and through each scope in order. Do not change the input arrays.

```{.python .starter}
import numpy as np


def join_factors(factors):
    """Pointwise product of the factors, as a (scope, table) pair."""
    ...
```

```{.python .tests}
import numpy as np

f = (("A", "B"), np.array([[0.1, 0.9], [0.6, 0.4]]))      # f(a, b)
g = (("B", "C"), np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]))   # g(b, c)


def test_chain():
    scope, t = join_factors([f, g])
    assert scope == ("A", "B", "C")
    assert t.shape == (2, 2, 3)
    assert np.isclose(t[0, 1, 2], 0.9 * 6.0) and np.isclose(t[1, 0, 1], 0.6 * 2.0)


def test_scope_order_and_permuted_axes():
    gt = (("C", "B"), g[1].T)                       # the same factor, axes swapped
    scope, t = join_factors([gt, f])
    assert scope == ("C", "B", "A")
    assert np.isclose(t[2, 1, 0], 6.0 * 0.9) and np.isclose(t[1, 0, 1], 2.0 * 0.6)


def test_disjoint_scopes_outer_product():
    a = (("X",), np.array([2.0, 3.0]))
    b = (("Y",), np.array([5.0, 7.0, 11.0]))
    scope, t = join_factors([a, b])
    assert scope == ("X", "Y") and np.allclose(t, np.outer([2, 3], [5, 7, 11]))


def test_same_scope_and_single_factor():
    scope, t = join_factors([f, f])
    assert scope == ("A", "B") and np.allclose(t, f[1] ** 2)
    scope, t = join_factors([g])
    assert scope == ("B", "C") and np.allclose(t, g[1])


def test_three_factors_and_inputs_unchanged():
    h = (("C", "A"), np.array([[1.0, 0.5], [2.0, 0.0], [1.0, 1.0]]))
    before = [x[1].copy() for x in (f, g, h)]
    scope, t = join_factors([f, g, h])
    assert scope == ("A", "B", "C")
    for a in range(2):
        for b in range(2):
            for c in range(3):
                assert np.isclose(t[a, b, c], f[1][a, b] * g[1][b, c] * h[1][c, a])
    assert all(np.array_equal(x[1], y) for x, y in zip((f, g, h), before))
```
:::

::: {#prob-eliminate-code .problem .coding origin="adapted" source="res-ucb-cs188-projects-tracking" solution="withheld" packages="numpy"}
With factors represented as in @prob-join-factors-code, write `eliminate(factor, var)`, which sums out the variable `var` (@def-factor) from `factor`. The scope of the result keeps the other variables in their order. Eliminating the only variable leaves a factor with the empty scope `()` and a 0-dimensional table.

```{.python .starter}
import numpy as np


def eliminate(factor, var):
    """Sum var out of factor = (scope, table); return the new (scope, table)."""
    ...
```

```{.python .tests}
import numpy as np

t3 = np.arange(24, dtype=float).reshape(2, 3, 4)
f = (("A", "B", "C"), t3)


def test_middle_variable():
    scope, t = eliminate(f, "B")
    assert scope == ("A", "C")
    assert t.shape == (2, 4)
    assert np.isclose(t[1, 2], t3[1, 0, 2] + t3[1, 1, 2] + t3[1, 2, 2])


def test_first_and_last_variable():
    scope, t = eliminate(f, "A")
    assert scope == ("B", "C") and np.allclose(t, t3[0] + t3[1])
    scope, t = eliminate(f, "C")
    assert scope == ("A", "B") and np.allclose(t, t3.sum(axis=2))


def test_marginal_of_a_joint():
    joint = (("Rain", "Traffic"), np.array([[0.08, 0.02], [0.09, 0.81]]))
    scope, t = eliminate(joint, "Rain")
    assert scope == ("Traffic",) and np.allclose(t, [0.17, 0.83])


def test_to_empty_scope():
    scope, t = eliminate((("X",), np.array([0.25, 0.5, 0.25])), "X")
    assert scope == () and np.ndim(t) == 0 and np.isclose(t, 1.0)


def test_input_unchanged():
    before = t3.copy()
    eliminate(f, "B")
    assert f[0] == ("A", "B", "C") and np.array_equal(t3, before)
```
:::

::: {#prob-variable-elimination-code .problem .coding origin="adapted" source="res-ucb-cs188-projects-tracking" solution="withheld" packages="numpy"}
Implement variable elimination (@def-variable-elimination) as `variable_elimination(cpts, query, evidence, order)`, with factors represented as in @prob-join-factors-code.

- `cpts` is the list of the network's conditional probability tables, one factor per variable; the scope of a variable's table holds the variable and its parents, in any order.
- `query` is one variable, `evidence` a dict from variables to observed values, and `order` the list of hidden variables (neither query nor evidence) in the order to eliminate them.

Return the posterior $P(\text{query}\mid\text{evidence})$ as a 1-D array that sums to $1$. Assume the evidence has positive probability. The exercise runs on its own, so write the join and the elimination again here (you may start from your answers to @prob-join-factors-code and @prob-eliminate-code). Never build the joint table of all the variables.

```{.python .starter}
import numpy as np


def variable_elimination(cpts, query, evidence, order):
    """P(query | evidence) by variable elimination, as a normalised 1-D array."""
    ...
```

```{.python .tests}
import itertools
import numpy as np

# Rain -> Traffic -> Late, Rain -> Umbrella (value 1 means "yes")
P_R = (("R",), np.array([0.9, 0.1]))
P_T = (("R", "T"), np.array([[0.8, 0.2], [0.1, 0.9]]))          # P(t | r), axes (r, t)
P_L = (("L", "T"), np.array([[0.9, 0.3], [0.1, 0.7]]))          # P(l | t), axes (l, t)
P_U = (("U", "R"), np.array([[0.8, 0.1], [0.2, 0.9]]))          # P(u | r), axes (u, r)
NET = [P_R, P_T, P_L, P_U]


def enumerate_posterior(cpts, query, evidence):
    """Reference answer by summing the full joint (fine for four binary variables)."""
    names = sorted({v for scope, _ in cpts for v in scope})
    sizes = {v: n for scope, t in cpts for v, n in zip(scope, t.shape)}
    out = np.zeros(sizes[query])
    for vals in itertools.product(*[range(sizes[v]) for v in names]):
        a = dict(zip(names, vals))
        if any(a[v] != x for v, x in evidence.items()):
            continue
        p = 1.0
        for scope, t in cpts:
            p *= t[tuple(a[v] for v in scope)]
        out[a[query]] += p
    return out / out.sum()


def test_rain_given_late():
    got = variable_elimination(NET, "R", {"L": 1}, ["T", "U"])
    assert np.allclose(got, enumerate_posterior(NET, "R", {"L": 1}))


def test_order_does_not_matter():
    a = variable_elimination(NET, "L", {"U": 1}, ["R", "T"])
    b = variable_elimination(NET, "L", {"U": 1}, ["T", "R"])
    assert np.allclose(a, b) and np.allclose(a, enumerate_posterior(NET, "L", {"U": 1}))


def test_no_evidence_is_the_marginal():
    got = variable_elimination(NET, "T", {}, ["R", "L", "U"])
    assert np.allclose(got, [0.9 * 0.8 + 0.1 * 0.1, 0.9 * 0.2 + 0.1 * 0.9])


def test_several_evidence_variables():
    got = variable_elimination(NET, "T", {"L": 0, "U": 1}, ["R"])
    assert np.allclose(got, enumerate_posterior(NET, "T", {"L": 0, "U": 1}))
    assert np.isclose(got.sum(), 1.0)


def test_three_valued_variable():
    A = (("A",), np.array([0.2, 0.5, 0.3]))
    B = (("A", "B"), np.array([[0.9, 0.1], [0.4, 0.6], [0.0, 1.0]]))
    C = (("B", "C"), np.array([[0.7, 0.3], [0.2, 0.8]]))
    net = [A, B, C]
    got = variable_elimination(net, "A", {"C": 1}, ["B"])
    assert got.shape == (3,) and np.allclose(got, enumerate_posterior(net, "A", {"C": 1}))
```
:::
