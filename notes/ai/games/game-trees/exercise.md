::: {#prob-depth-limited-minimax-code .problem .coding origin="adapted" source="res-stanford-cs221-hw-pacman"}
Implement depth-limited minimax (@def-game-recurrences) for a game with one maximizing agent and any number of minimizing opponents, as in a maze game with one player and several ghosts. Write `minimax(game, s, depth)`.

The game is an object with these methods:

- `game.agent(s)`: the index of the agent to move in state `s`. Agent `0` maximizes; agents `1, ..., k-1` minimize. They move in turn `0, 1, ..., k-1, 0, 1, ...`.
- `game.is_end(s)` and `game.utility(s)`: whether `s` is an end state, and its utility (for agent 0).
- `game.actions(s)` and `game.succ(s, a)`: the legal actions in `s` (a non-empty list for every state that is not an end state) and the state that action `a` leads to.
- `game.evaluate(s)`: an evaluation function, an estimate of the value of `s`.

`depth` counts *rounds*: one round is one move of every agent. Return the value of `s` together with a best action, as a pair `(value, action)`:

- if `s` is an end state, its utility with action `None`;
- if it is agent 0's turn and `depth == 0`, `game.evaluate(s)` with action `None`;
- otherwise the maximum (agent 0) or minimum (other agents) of the values of the successors, with an action attaining it, the first one in `game.actions(s)` among ties. A round ends after agent $k-1$ has moved.

```{.python .starter}
def minimax(game, s, depth):
    """Return (value, action) of state s, searching depth rounds."""
    ...
```

```{.python .tests}
class Tree:
    """A game given as nested lists: a number is an end state with that utility,
    a list holds the children. States are paths (tuples of child indices), the
    agents 0..k-1 move in turn, and evaluate(s) is the mean of the leaves below s."""
    def __init__(self, tree, k=2):
        self.tree, self.k, self.calls = tree, k, 0
    def node(self, s):
        t = self.tree
        for i in s:
            t = t[i]
        return t
    def agent(self, s):
        return len(s) % self.k
    def is_end(self, s):
        return not isinstance(self.node(s), list)
    def utility(self, s):
        self.calls += 1
        return self.node(s)
    def actions(self, s):
        return list(range(len(self.node(s))))
    def succ(self, s, a):
        return s + (a,)
    def evaluate(self, s):
        self.calls += 1
        leaves = []
        def walk(t):
            if isinstance(t, list):
                for c in t:
                    walk(c)
            else:
                leaves.append(t)
        walk(self.node(s))
        return sum(leaves) / len(leaves)


def test_two_players():
    g = Tree([[3, 12, 8], [2, 4, 6], [14, 5, 2]])
    assert minimax(g, (), 1) == (3, 0)
    assert minimax(g, (1,), 1) == (2, 0)


def test_end_state_and_depth_zero():
    g = Tree([[3, 12, 8], [2, 4, 6], [14, 5, 2]])
    assert minimax(g, (2, 0), 5) == (14, None)
    v, a = minimax(g, (), 0)                           # the mean of the nine leaves
    assert abs(v - 56 / 9) < 1e-9 and a is None


def test_three_agents():
    # agent 0, then two minimizers; one round reaches the leaves
    g = Tree([[[1, 9], [8, 7]], [[4, 5], [6, 3]]], k=3)
    assert minimax(g, (), 1) == (3, 1)


def test_depth_limit_uses_evaluation():
    g = Tree([[[[1, 9], [2, 2]], [[0, 0], [10, 10]]], [[[3, 3], [3, 3]], [[3, 3], [3, 3]]]])
    # depth 1: the depth-2 states are evaluated by the mean of their leaves,
    # 3.5 and 5 in the first branch, 3 and 3 in the second
    assert minimax(g, (), 1) == (3.5, 0)
    # depth 2 reaches the leaves: the first branch is then worth only min(2, 10)
    assert minimax(g, (), 2) == (3, 1)


def test_ties_keep_first_action():
    assert minimax(Tree([[5, 6], [5, 9], [4, 7]]), (), 1) == (5, 0)


def test_uneven_tree():
    g = Tree([7, [[4], 9], [1, [[20, 30]]]])
    assert minimax(g, (), 3) == (7, 0)
```
:::

::: {#prob-expectimax-code .problem .coding origin="adapted" source="res-stanford-cs221-hw-pacman"}
Change @prob-depth-limited-minimax-code to expectimax (@def-game-recurrences): the opponents no longer play optimally but choose each legal action with equal probability. Write `expectimax(game, s, depth)` with the same game interface, depth rule and return value `(value, action)`. At an opponent's state the value is the average of the values of the successors, and the action returned is `None`; agent 0 still maximizes, taking the first action among ties.

```{.python .starter}
def expectimax(game, s, depth):
    """Return (value, action) of state s against uniformly random opponents."""
    ...
```

```{.python .tests}
class Tree:
    """Nested-list game: numbers are end states, lists hold children; states are
    paths; agents 0..k-1 move in turn; evaluate(s) = mean of the leaves below s."""
    def __init__(self, tree, k=2):
        self.tree, self.k = tree, k
    def node(self, s):
        t = self.tree
        for i in s:
            t = t[i]
        return t
    def agent(self, s):
        return len(s) % self.k
    def is_end(self, s):
        return not isinstance(self.node(s), list)
    def utility(self, s):
        return self.node(s)
    def actions(self, s):
        return list(range(len(self.node(s))))
    def succ(self, s, a):
        return s + (a,)
    def evaluate(self, s):
        return -100.0


def test_two_players():
    g = Tree([[3, 12, 8], [2, 4, 6], [14, 5, 2]])
    v, a = expectimax(g, (), 1)
    assert abs(v - 23 / 3) < 1e-9 and a == 0
    v, a = expectimax(g, (1,), 1)
    assert abs(v - 4) < 1e-9 and a is None


def test_differs_from_minimax():
    # minimax prefers the safe branch; against a random opponent the risky one is better
    g = Tree([[5, 5], [0, 100]])
    assert expectimax(g, (), 1) == (50, 1)


def test_three_agents():
    g = Tree([[[1, 9], [8, 7]], [[4, 5], [6, 3]]], k=3)
    v, a = expectimax(g, (), 1)
    assert abs(v - 6.25) < 1e-9 and a == 0


def test_depth_limit():
    g = Tree([[[[1, 2]], [[3, 4]]], [[[5, 6]], [[7, 8]]]])
    assert expectimax(g, (), 1) == (-100.0, 0)
    v, a = expectimax(g, (), 2)
    assert abs(v - 6.5) < 1e-9 and a == 1
```
:::
