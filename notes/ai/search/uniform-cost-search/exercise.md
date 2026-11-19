::: {.problem #prob-cs221hw-3-q1 origin="external" source="cs221hw-3-q1"}
Consider an infinite city consisting of locations $(x,y)$ where $x, y$ are integers. From each location $(x,y)$, one can go east, west, north, or south. These movements are what we refer to as 'actions'. Specifically, an action is a change in the (x, y) coordinates: (+1, 0) represents moving east, (-1, 0) represents moving west, (0, +1) represents moving north, and (0, -1) represents moving south.

You start at $(0,0)$ and want to go to $(m, n)$, where $m, n \geq 0$. We can define the following search problem to capture this:

- $s_\text{start} = (0,0)$
- $\text{Actions}(s) = \{ (+1, 0), (-1, 0), (0, +1), (0, -1) \}$
- $\text{Succ}(s, a) = s + a$ (i.e., the successor function, where $s$ is the state vector (location) and $a$ is the action (one of the above))
- $\text{Cost}((x,y), a) = 1 + \max(x, 0)$ (i.e., it is more expensive as $x$ increases)
- $\text{IsEnd}(s) = \mathbf{1}[s = (m,n)]$

(a) What is the minimum cost of reaching location $(m,n)$ (note that $m,n \geq 0$) starting from location $(0,0)$ in the above city? Describe one possible path achieving the minimum cost. Is it unique (i.e., are there multiple paths that achieve the minimum cost)? Note that the cost of the actions depends on the x-coordinate of the current state.

*Expected:* Provide an expression for the minimum cost and explain how you got it. In addition, please provide 1 - 2 sentences describing one possible minimum cost path and state whether it is unique.

(b) How will Uniform Cost Search (UCS) behave on this problem? Mark the following as true or false:

1.  UCS will never terminate because the number of states is infinite.
2.  UCS will return the minimum cost path and explore only locations between $(0,0)$ and $(m,n)$; that is, $(x,y)$ such that $0 \le x \le m$ and $0 \le y \le n$.
3.  UCS will return the minimum cost path and explore only locations whose past costs (the minimum cost to reach that location from $(0,0)$) are less than or equal to the minimum cost from $(0,0)$ to $(m,n)$.

*Expected:* T/F for each subpart. No justification needed.

(c) Now consider running UCS on an arbitrary graph, where each state is a node of the graph, to find the minimum cost path from a start state to an end state. In particular, the graph is not necessarily the one which was studied in the previous two parts of this question. Mark the following as true or false:

1.  If you add a connection between two nodes of the graph, the minimum cost from any start state to any end state cannot go up.
2.  If you make the cost of an action from some state small enough (possibly negative), that action will show up in the path returned by UCS, assuming that a path from the start state to the end state exists.
3.  If you increase the cost of each action by 1, the minimum cost path does not change (even though its cost does).

*Expected:* T/F for each subpart. No justification needed.

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::

::: {#prob-ucs-route-code .problem .coding origin="adapted" source="res-stanford-cs221-hw-route"}
Implement uniform cost search (@def-uniform-cost-search) as a function `ucs(start, succ, is_end)`.

- `start` is the start state. States are any hashable values: strings, tuples, or tuples holding a `frozenset`.
- `succ(s)` returns a list of pairs `(t, c)`: from state `s` one action leads to state `t` at cost `c >= 0`.
- `is_end(s)` says whether `s` is an end state. Several states may be end states, for example every location that carries some tag.

Return a pair `(cost, path)`, where `path` is the list of states of a minimum-cost path from `start` to an end state (both included) and `cost` is its cost. Return `None` if no end state can be reached. Explore each state at most once, and stop as soon as an end state is removed from the frontier, so that the function also works on infinite state spaces whose costs are positive.

The tests also run `ucs` on a route with *unordered waypoints*: the path must pass through every waypoint, in any order, before it stops at the end. The state is then a pair (location, set of waypoints visited so far); see the helper `waypoint_problem` in the tests.

```{.python .starter}
import heapq


def ucs(start, succ, is_end):
    """Return (cost, path) of a cheapest path from start to an end state,
    or None if no end state is reachable."""
    ...
```

```{.python .tests}
def check(result, cost, start, succ, is_end):
    assert result is not None, "expected a path, got None"
    c, path = result
    assert c == cost, f"cost {c}, expected {cost}"
    assert path[0] == start and is_end(path[-1]), "path must run from start to an end state"
    steps = sum(min(w for t, w in succ(a) if t == b) for a, b in zip(path, path[1:]))
    assert steps == cost, f"the path costs {steps}, not {cost}"


graph = {"A": [("B", 1), ("C", 4)], "B": [("C", 1), ("D", 5)], "C": [("D", 1)], "D": []}
succ = lambda s: graph[s]


def test_small_graph():
    assert ucs("A", succ, lambda s: s == "D") == (3, ["A", "B", "C", "D"])


def test_start_is_end():
    assert ucs("A", succ, lambda s: s == "A") == (0, ["A"])


def test_unreachable():
    assert ucs("D", succ, lambda s: s == "A") is None


def test_several_end_states():
    assert ucs("A", succ, lambda s: s in {"C", "D"}) == (2, ["A", "B", "C"])


def test_zero_cost_cycle():
    g = {"X": [("Y", 0)], "Y": [("X", 0), ("Z", 2)], "Z": []}
    assert ucs("X", lambda s: g[s], lambda s: s == "Z") == (2, ["X", "Y", "Z"])


def test_infinite_city():
    # moving in x costs 1 + max(x, 0); the cheapest cost to (m, n) is n + m(m+1)/2
    def city(s):
        x, y = s
        return [((x + dx, y + dy), 1 + max(x, 0)) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
    for m, n in [(0, 0), (2, 1), (3, 2)]:
        check(ucs((0, 0), city, lambda s: s == (m, n)), n + m * (m + 1) // 2, (0, 0), city, lambda s: s == (m, n))


def waypoint_problem(roads, tags, end_tag, waypoint_tags):
    """States (location, frozenset of waypoint tags seen). roads: {loc: [(loc2, cost)]}."""
    def succ(s):
        loc, seen = s
        return [((t, seen | (tags.get(t, set()) & waypoint_tags)), c) for t, c in roads[loc]]
    def is_end(s):
        loc, seen = s
        return end_tag in tags.get(loc, set()) and seen == waypoint_tags
    return succ, is_end


def test_unordered_waypoints():
    # a road a - b - c - d - e, each link costing 1 in both directions
    line = "abcde"
    roads = {u: [] for u in line}
    for u, v in zip(line, line[1:]):
        roads[u].append((v, 1))
        roads[v].append((u, 1))
    tags = {"a": {"gas"}, "e": {"food"}, "c": {"home"}}
    succ_w, end_w = waypoint_problem(roads, tags, "home", frozenset({"gas", "food"}))
    start = ("c", frozenset())
    # c -> a (gas) -> e (food) -> c costs 2 + 4 + 2 = 8
    check(ucs(start, succ_w, end_w), 8, start, succ_w, end_w)
    succ_1, end_1 = waypoint_problem(roads, tags, "home", frozenset({"food"}))
    check(ucs(start, succ_1, end_1), 4, start, succ_1, end_1)
```
:::
