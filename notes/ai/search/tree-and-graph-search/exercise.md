::: {#prob-graph-search-code .problem .coding origin="adapted" source="res-ucb-cs188-projects-search" solution="withheld"}
Implement graph search (@def-tree-search) with the depth-first and breadth-first strategies (@def-uninformed-strategies) as one function `graph_search(start, succ, is_end, strategy)`.

- `start` is the start state; states are hashable values.
- `succ(s)` returns the list of states reachable from `s` in one action. Costs play no part here.
- `is_end(s)` says whether `s` is an end state.
- `strategy` is `"dfs"` (the fringe is a stack) or `"bfs"` (the fringe is a queue).

The fringe holds paths, lists of states starting with `start`. Expand a path by adding one new path for each successor, in the order `succ` lists them. Test a path for an end state when it is *removed* from the fringe, not when it is added. Keep a closed set of expanded states and skip a removed path whose last state is in it, so that `succ` is called at most once per state. Return the first path removed whose last state is an end state, or `None` if the fringe runs empty.

With these rules the answer is fully determined, so the tests check the exact path.

```{.python .starter}
def graph_search(start, succ, is_end, strategy):
    """Return the path (list of states) found by graph search with the
    given strategy ("dfs" or "bfs"), or None if no end state is reachable."""
    ...
```

```{.python .tests}
graph = {"S": ["A", "B"], "A": ["C", "D"], "B": ["D", "G"], "C": ["S"], "D": ["G"], "G": []}


def run(start, strategy, goal="G", g=graph):
    calls = []

    def succ(s):
        calls.append(s)
        return g[s]

    path = graph_search(start, succ, lambda s: s == goal, strategy)
    assert len(calls) == len(set(calls)), f"states expanded twice: {calls}"
    return path, calls


def test_bfs_small_graph():
    path, calls = run("S", "bfs")
    assert path == ["S", "B", "G"]
    assert calls == ["S", "A", "B", "C", "D"], f"expanded {calls}"


def test_dfs_small_graph():
    path, calls = run("S", "dfs")
    assert path == ["S", "B", "G"]
    assert calls == ["S", "B"], f"expanded {calls}"


def test_dfs_goes_deep():
    g = {"S": ["G", "A"], "A": ["B"], "B": ["G"], "G": []}
    assert run("S", "dfs", g=g)[0] == ["S", "A", "B", "G"]
    assert run("S", "bfs", g=g)[0] == ["S", "G"]


def test_cycle_and_unreachable():
    g = {"X": ["Y"], "Y": ["X", "Z"], "Z": ["Y"], "G": []}
    for strategy in ("dfs", "bfs"):
        path, calls = run("X", strategy, g=g)
        assert path is None and sorted(calls) == ["X", "Y", "Z"]


def test_start_is_end():
    for strategy in ("dfs", "bfs"):
        assert run("G", strategy)[0] == ["G"]


def test_bfs_fewest_steps_on_grid():
    # a 4 x 3 grid without walls; BFS finds a path with the fewest moves
    def succ(s):
        x, y = s
        return [(x + dx, y + dy) for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]
                if 0 <= x + dx < 4 and 0 <= y + dy < 3]
    path = graph_search((0, 0), succ, lambda s: s == (3, 2), "bfs")
    assert len(path) == 6 and path[0] == (0, 0) and path[-1] == (3, 2)
    assert all(abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1 for a, b in zip(path, path[1:]))
    path = graph_search((0, 0), succ, lambda s: s == (3, 2), "dfs")
    assert path[0] == (0, 0) and path[-1] == (3, 2) and len(path) == len(set(path))
```
:::
