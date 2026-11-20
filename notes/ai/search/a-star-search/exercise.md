::: {.problem #prob-cs188hw-1-q2 origin="external" source="cs188hw-1-q2"}
**Pacman Goes to School!** Pacman lives far from his university, so he decides to model his daily commute as a search problem. He imagines the city of Berkeley as an $M$ by $N$ square grid, where his apartment is the top left square; his goal is to reach Dwinelle Hall, located in the bottom right square in the fewest number of timesteps. He can move left, right, up, or down, as long as he stays within the grid.

There is a single fixed bus route on the grid, where a bus travels in a loop at a constant rate of three squares per timestep. Any square along this route is a valid bus stop. Pacman knows the bus route, and if he's on the same square as the bus, he can hop on and travel at a rate of three squares per timestep along the bus route. He can stay on the bus for any number of timesteps and get off at any square adjacent to the route. However, Pacman's Clipper card only allows one ride per commute, so he can only board and disembark from the bus route at most once during his trip.

Below is an example initial state on a 6 by 6 grid. The arrows represent the bus route. Note that this is just an example route, and the actual bus route may vary. For the following questions, consider the general case, not this specific example. Additionally, consider each part separately (i.e., do not carry over assumptions).

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\draw[cell frame] (0.0,0.0) rectangle (0.6,-0.6);
\draw[cell frame] (0.6,0.0) rectangle (1.2,-0.6);
\draw[cell frame] (1.2,0.0) rectangle (1.8,-0.6);
\draw[cell frame] (1.8,0.0) rectangle (2.4,-0.6);
\draw[cell frame] (2.4,0.0) rectangle (3.0,-0.6);
\draw[cell frame] (3.0,0.0) rectangle (3.6,-0.6);
\draw[cell frame] (0.0,-0.6) rectangle (0.6,-1.2);
\draw[cell frame] (0.6,-0.6) rectangle (1.2,-1.2);
\draw[cell frame] (1.2,-0.6) rectangle (1.8,-1.2);
\draw[cell frame] (1.8,-0.6) rectangle (2.4,-1.2);
\draw[cell frame] (2.4,-0.6) rectangle (3.0,-1.2);
\draw[cell frame] (3.0,-0.6) rectangle (3.6,-1.2);
\draw[cell frame] (0.0,-1.2) rectangle (0.6,-1.8);
\draw[cell frame] (0.6,-1.2) rectangle (1.2,-1.8);
\draw[cell frame] (1.2,-1.2) rectangle (1.8,-1.8);
\draw[cell frame] (1.8,-1.2) rectangle (2.4,-1.8);
\draw[cell frame] (2.4,-1.2) rectangle (3.0,-1.8);
\draw[cell frame] (3.0,-1.2) rectangle (3.6,-1.8);
\draw[cell frame] (0.0,-1.8) rectangle (0.6,-2.4);
\draw[cell frame] (0.6,-1.8) rectangle (1.2,-2.4);
\draw[cell frame] (1.2,-1.8) rectangle (1.8,-2.4);
\draw[cell frame] (1.8,-1.8) rectangle (2.4,-2.4);
\draw[cell frame] (2.4,-1.8) rectangle (3.0,-2.4);
\draw[cell frame] (3.0,-1.8) rectangle (3.6,-2.4);
\draw[cell frame] (0.0,-2.4) rectangle (0.6,-3.0);
\draw[cell frame] (0.6,-2.4) rectangle (1.2,-3.0);
\draw[cell frame] (1.2,-2.4) rectangle (1.8,-3.0);
\draw[cell frame] (1.8,-2.4) rectangle (2.4,-3.0);
\draw[cell frame] (2.4,-2.4) rectangle (3.0,-3.0);
\draw[cell frame] (3.0,-2.4) rectangle (3.6,-3.0);
\draw[cell frame] (0.0,-3.0) rectangle (0.6,-3.6);
\draw[cell frame] (0.6,-3.0) rectangle (1.2,-3.6);
\draw[cell frame] (1.2,-3.0) rectangle (1.8,-3.6);
\draw[cell frame] (1.8,-3.0) rectangle (2.4,-3.6);
\draw[cell frame] (2.4,-3.0) rectangle (3.0,-3.6);
\draw[cell frame] (3.0,-3.0) rectangle (3.6,-3.6);
\draw[->, hl] (0.90,-0.90) -- (2.70,-0.90) -- (2.70,-2.70) -- (0.90,-2.70) -- (0.90,-0.90);
\node[lab] at (0.30,-0.30) {P};
\node[lab] at (3.30,-3.30) {U};
\end{tikzpicture}
\end{center}
```



1. Which of the following are admissible heuristics? Select all that apply.
   - The Manhattan distance between Pacman and the university.
   - The Manhattan distance between Pacman and the university divided by 4.
   - The Manhattan distance between Pacman and the bus.
   - The Manhattan distance between the closest bus stop to Pacman and the university.
   - None of the above.
2. Suppose Pacman knows there is at least one bus stop adjacent to the university. Which of the following are admissible heuristics? Select all that apply.
   - The Manhattan distance between Pacman and the bus.
   - The Manhattan distance between the bus and the stop next to the university divided by 3.
   - $\frac{1}{3}$ for all states.
   - The minimum of the above heuristics.
   - None of the above.
3. Suppose that there are $B$ different buses with their own routes. Pacman can now ride the bus multiple times, but he must also ride a bus at least once. Which of the following are admissible heuristics? Select all that apply.
   - The minimum of the Manhattan distances between every bus stop and the university, and Pacman and the university.
   - The number of times Pacman has ridden the bus so far.
   - The Manhattan distance from Pacman to the closest bus stop plus the distance from that bus stop to the university divided by three.
   - None of the above.
4. Suppose Pacman now wants to work out at the RSF (the campus gym), located in the bottom left square of the grid. It doesn't matter if he goes before or after reaching the university, but he must visit both locations. Below is an example initial state with the RSF represented by a dumbbell in the bottom left corner:

   ```{=latex}
   \begin{center}
   \begin{tikzpicture}[x=1cm, y=1cm]
   \draw[cell frame] (0.0,0.0) rectangle (0.6,-0.6);
   \draw[cell frame] (0.6,0.0) rectangle (1.2,-0.6);
   \draw[cell frame] (1.2,0.0) rectangle (1.8,-0.6);
   \draw[cell frame] (1.8,0.0) rectangle (2.4,-0.6);
   \draw[cell frame] (2.4,0.0) rectangle (3.0,-0.6);
   \draw[cell frame] (3.0,0.0) rectangle (3.6,-0.6);
   \draw[cell frame] (0.0,-0.6) rectangle (0.6,-1.2);
   \draw[cell frame] (0.6,-0.6) rectangle (1.2,-1.2);
   \draw[cell frame] (1.2,-0.6) rectangle (1.8,-1.2);
   \draw[cell frame] (1.8,-0.6) rectangle (2.4,-1.2);
   \draw[cell frame] (2.4,-0.6) rectangle (3.0,-1.2);
   \draw[cell frame] (3.0,-0.6) rectangle (3.6,-1.2);
   \draw[cell frame] (0.0,-1.2) rectangle (0.6,-1.8);
   \draw[cell frame] (0.6,-1.2) rectangle (1.2,-1.8);
   \draw[cell frame] (1.2,-1.2) rectangle (1.8,-1.8);
   \draw[cell frame] (1.8,-1.2) rectangle (2.4,-1.8);
   \draw[cell frame] (2.4,-1.2) rectangle (3.0,-1.8);
   \draw[cell frame] (3.0,-1.2) rectangle (3.6,-1.8);
   \draw[cell frame] (0.0,-1.8) rectangle (0.6,-2.4);
   \draw[cell frame] (0.6,-1.8) rectangle (1.2,-2.4);
   \draw[cell frame] (1.2,-1.8) rectangle (1.8,-2.4);
   \draw[cell frame] (1.8,-1.8) rectangle (2.4,-2.4);
   \draw[cell frame] (2.4,-1.8) rectangle (3.0,-2.4);
   \draw[cell frame] (3.0,-1.8) rectangle (3.6,-2.4);
   \draw[cell frame] (0.0,-2.4) rectangle (0.6,-3.0);
   \draw[cell frame] (0.6,-2.4) rectangle (1.2,-3.0);
   \draw[cell frame] (1.2,-2.4) rectangle (1.8,-3.0);
   \draw[cell frame] (1.8,-2.4) rectangle (2.4,-3.0);
   \draw[cell frame] (2.4,-2.4) rectangle (3.0,-3.0);
   \draw[cell frame] (3.0,-2.4) rectangle (3.6,-3.0);
   \draw[cell frame] (0.0,-3.0) rectangle (0.6,-3.6);
   \draw[cell frame] (0.6,-3.0) rectangle (1.2,-3.6);
   \draw[cell frame] (1.2,-3.0) rectangle (1.8,-3.6);
   \draw[cell frame] (1.8,-3.0) rectangle (2.4,-3.6);
   \draw[cell frame] (2.4,-3.0) rectangle (3.0,-3.6);
   \draw[cell frame] (3.0,-3.0) rectangle (3.6,-3.6);
   \draw[->, hl] (0.90,-0.90) -- (2.70,-0.90) -- (2.70,-2.70) -- (0.90,-2.70) -- (0.90,-0.90);
   \node[lab] at (0.30,-0.30) {P};
   \node[lab] at (3.30,-3.30) {U};
   \node[lab] at (0.30,-3.30) {R};
   \end{tikzpicture}
   \end{center}
   ```



   Which of the following are admissible heuristics? Select all that apply.
   - The minimum of the Manhattan distances between Pacman and the RSF, the RSF and the university, and Pacman and the university, divided by 3.
   - The sum of the Manhattan distances between Pacman and the RSF, the RSF and the university, and Pacman and the university, divided by 3.
   - The maximum of the above heuristics.
   - None of the above.
5. Suppose Pacman and his friend Xavier want to go to the university together today. Xavier lives in an apartment in the top right corner of the grid and wants to meet up with Pacman somewhere before they move together to the university. Assume that Xavier moves independently from Pacman, one space per timestep, and that they must meet in another square before either of them can go to the university. Xavier cannot take the bus, with or without Pacman (although Pacman can still take it alone). In this updated search problem, you can control both Pacman and Xavier.

   Below is an example initial state with Xavier's apartment in the top right corner. Xavier is currently in his apartment:

   ```{=latex}
   \begin{center}
   \begin{tikzpicture}[x=1cm, y=1cm]
   \draw[cell frame] (0.0,0.0) rectangle (0.6,-0.6);
   \draw[cell frame] (0.6,0.0) rectangle (1.2,-0.6);
   \draw[cell frame] (1.2,0.0) rectangle (1.8,-0.6);
   \draw[cell frame] (1.8,0.0) rectangle (2.4,-0.6);
   \draw[cell frame] (2.4,0.0) rectangle (3.0,-0.6);
   \draw[cell frame] (3.0,0.0) rectangle (3.6,-0.6);
   \draw[cell frame] (0.0,-0.6) rectangle (0.6,-1.2);
   \draw[cell frame] (0.6,-0.6) rectangle (1.2,-1.2);
   \draw[cell frame] (1.2,-0.6) rectangle (1.8,-1.2);
   \draw[cell frame] (1.8,-0.6) rectangle (2.4,-1.2);
   \draw[cell frame] (2.4,-0.6) rectangle (3.0,-1.2);
   \draw[cell frame] (3.0,-0.6) rectangle (3.6,-1.2);
   \draw[cell frame] (0.0,-1.2) rectangle (0.6,-1.8);
   \draw[cell frame] (0.6,-1.2) rectangle (1.2,-1.8);
   \draw[cell frame] (1.2,-1.2) rectangle (1.8,-1.8);
   \draw[cell frame] (1.8,-1.2) rectangle (2.4,-1.8);
   \draw[cell frame] (2.4,-1.2) rectangle (3.0,-1.8);
   \draw[cell frame] (3.0,-1.2) rectangle (3.6,-1.8);
   \draw[cell frame] (0.0,-1.8) rectangle (0.6,-2.4);
   \draw[cell frame] (0.6,-1.8) rectangle (1.2,-2.4);
   \draw[cell frame] (1.2,-1.8) rectangle (1.8,-2.4);
   \draw[cell frame] (1.8,-1.8) rectangle (2.4,-2.4);
   \draw[cell frame] (2.4,-1.8) rectangle (3.0,-2.4);
   \draw[cell frame] (3.0,-1.8) rectangle (3.6,-2.4);
   \draw[cell frame] (0.0,-2.4) rectangle (0.6,-3.0);
   \draw[cell frame] (0.6,-2.4) rectangle (1.2,-3.0);
   \draw[cell frame] (1.2,-2.4) rectangle (1.8,-3.0);
   \draw[cell frame] (1.8,-2.4) rectangle (2.4,-3.0);
   \draw[cell frame] (2.4,-2.4) rectangle (3.0,-3.0);
   \draw[cell frame] (3.0,-2.4) rectangle (3.6,-3.0);
   \draw[cell frame] (0.0,-3.0) rectangle (0.6,-3.6);
   \draw[cell frame] (0.6,-3.0) rectangle (1.2,-3.6);
   \draw[cell frame] (1.2,-3.0) rectangle (1.8,-3.6);
   \draw[cell frame] (1.8,-3.0) rectangle (2.4,-3.6);
   \draw[cell frame] (2.4,-3.0) rectangle (3.0,-3.6);
   \draw[cell frame] (3.0,-3.0) rectangle (3.6,-3.6);
   \draw[->, hl] (0.90,-0.90) -- (2.70,-0.90) -- (2.70,-2.70) -- (0.90,-2.70) -- (0.90,-0.90);
   \node[lab] at (0.30,-0.30) {P};
   \node[lab] at (3.30,-3.30) {U};
   \node[lab] at (3.30,-0.30) {X};
   \end{tikzpicture}
   \end{center}
   ```



   Which of the following are admissible heuristics? Select all that apply.
   - The Manhattan distance between Pacman and Xavier divided by 2.
   - The Manhattan distance from Xavier to the university.
   - The Manhattan distance from Pacman to the university divided by 3.
   - None of the above.

*Note (these notes):* The example grids are redrawn schematically: P is Pacman's apartment, U the university, R the RSF and X Xavier's apartment; the arrows show one possible bus loop.
:::

::: {.problem #prob-cs188d-1-q2 origin="external" source="cs188d-1-q2"}
**Search and Heuristics.** Imagine a car-like agent wishes to exit a maze like the one shown below:

1. The agent is directional and at all times faces some direction $d\in(N,S,E,W)$.
2. With a single action, the agent can *either* move forward at an adjustable velocity $v$ *or* turn. The turning actions are *left* and *right*, which change the agent's direction by 90 degrees. Turning is only permitted when the velocity is zero (and leaves it at zero).
3. The moving actions are *fast* and *slow*. *Fast* increments the velocity by 1 and *slow* decrements the velocity by 1; in both cases the agent then moves a number of squares equal to its NEW adjusted velocity (see example below).
4. A consequence of this formulation is that it is **impossible** for the agent to move in the same nonzero velocity for two consecutive timesteps.
5. Any action that would result in a collision with a wall or reduce $v$ below 0/above a maximum speed $V_{\max}$ is illegal.
6. The agent's goal is to find a plan which parks it (stationary) on the exit square using as few actions (time steps) as possible.

As an example: if at timestep $t$ the agent's current velocity is 2, by taking the *fast* action, the agent first increases the velocity to 3 and move 3 squares forward, such that at timestep $t+1$ the agent's current velocity will be 3 and will be 3 squares away from where it was at timestep $t$. If instead the agent takes the *slow* action, it first decreases its velocity to 1 and then moves 1 square forward, such that at timestep $t+1$ the agent's current velocity will be 1 and will be 1 squares away from where it was at timestep $t$. If, with an instantaneous velocity of 1 at timestep $t+1$, it takes the slow action again, the agent's current velocity will become 0, and it will not move at timestep $t+1$. Then at timestep $t+2$, it will be free to turn if it wishes. Note that the agent could not have turned at timestep $t+1$ when it had a current velocity of 1, because it has to be stationary to turn.

(a) If the grid is $M$ by $N$, what is the size of the state space? Justify your answer. You should assume that all configurations are reachable from the start state.

(b) Is the Manhattan distance from the agent's location to the exit's location admissible? Why or why not?

(c) State and justify a non-trivial admissible heuristic for this problem which is not the Manhattan distance to the exit.

(d) If we used an inadmissible heuristic in A* graph search, would the search be complete? Would it be optimal?

(e) Give a possible advantage that an inadmissible heuristic might have over an admissible one.

*Note (these notes):* The handout refers to a maze picture that is not present in the PDF; the questions do not depend on it.
:::

::: {#prob-a-star-route-code .problem .coding origin="adapted" source="res-stanford-cs221-hw-route"}
Implement A\* search (@def-a-star-search) as a function `a_star(start, succ, is_end, h)`.

- `start`, `succ` and `is_end` describe a search problem as in @prob-ucs-route-code: `succ(s)` returns a list of pairs `(t, c)`, one for each action from `s`, leading to state `t` at cost `c >= 0`.
- `h(s)` is a consistent heuristic (@def-consistent-heuristic): a number that estimates the cheapest cost from `s` to an end state.

Return a triple `(cost, path, explored)`: `path` is the list of states of a minimum-cost path from `start` to an end state, `cost` is its cost under the *original* costs, and `explored` is the number of distinct states removed from the frontier, the end state included. Return `None` if no end state can be reached.

You may run uniform cost search on the modified costs, as in the definition, or order the frontier by past cost plus heuristic; both explore the same states.

```{.python .starter}
import heapq


def a_star(start, succ, is_end, h):
    """Return (cost, path, explored) for a cheapest path from start to an
    end state, or None if no end state is reachable."""
    ...
```

```{.python .tests}
import math


def line(lo, hi):
    """States lo..hi on a line; a step left or right costs 1."""
    return lambda s: [(t, 1) for t in (s - 1, s + 1) if lo <= t <= hi]


def test_line_with_heuristic():
    cost, path, explored = a_star(0, line(-10, 10), lambda s: s == 10, lambda s: 10 - s)
    assert cost == 10, "the cost must be the original cost, not the modified one"
    assert path == list(range(11))
    assert explored == 11, f"explored {explored} states; A* should explore only 0..10"


def test_line_without_heuristic():
    cost, path, explored = a_star(0, line(-10, 10), lambda s: s == 10, lambda s: 0)
    assert (cost, path) == (10, list(range(11)))
    assert explored >= 20, "with h = 0, A* is UCS and also explores the left half"


def test_road_map():
    # cities in the plane; roads cost their length, h is the straight-line distance
    xy = {"S": (0, 0), "A": (3, 5), "B": (6, 0), "D": (-4, 0), "G": (9, 4)}
    roads = {"S": ["A", "B", "D"], "A": ["S", "G"], "B": ["S", "G"], "D": ["S", "G"], "G": ["A", "B", "D"]}
    succ = lambda s: [(t, math.dist(xy[s], xy[t])) for t in roads[s]]
    h = lambda s: math.dist(xy[s], xy["G"])
    cost, path, explored = a_star("S", succ, lambda s: s == "G", h)
    assert path == ["S", "B", "G"]
    assert math.isclose(cost, 11.0)
    assert "D" not in path and explored <= 4


def test_unreachable():
    g = {"A": [("B", 1)], "B": [], "C": []}
    assert a_star("A", lambda s: g[s], lambda s: s == "C", lambda s: 0) is None


def test_start_is_end():
    assert a_star(5, line(0, 9), lambda s: s == 5, lambda s: abs(5 - s)) == (0, [5], 1)
```
:::

::: {#prob-visit-all-heuristic-code .problem .coding origin="adapted" source="res-ucb-cs188-projects-search" solution="withheld"}
An agent in a grid maze must visit a set of target cells, in any order, for example the four corners of the maze or every cell that holds food. It moves one cell north, south, east or west per step, at cost $1$, and cannot enter a wall. A state is a pair `(pos, left)`: `pos = (x, y)` is the agent's cell and `left` is the `frozenset` of targets not yet visited. Entering a target removes it from `left`; the end states are those with `left` empty.

Write a heuristic `visit_all_heuristic(s)` for this problem that

- is consistent (@def-consistent-heuristic) and therefore admissible (@prp-consistent-admissible), on every maze;
- is $0$ at end states;
- is at least the Manhattan distance from `pos` to the farthest target in `left`.

The heuristic gets only the state, not the walls. A relaxed problem (@def-relaxed-search-problem, @thm-relaxation-consistent) suggests consistent choices, and the maximum of consistent heuristics is consistent (@thm-max-heuristic). A larger heuristic makes A\* explore fewer states; try to beat the farthest-target bound when few targets are left.

```{.python .starter}
def visit_all_heuristic(s):
    """Consistent lower bound on the number of moves needed from s = (pos, left)
    to visit every cell in left."""
    ...
```

```{.python .tests}
from collections import deque


def maze_problem(rows, targets):
    """rows: strings, '#' a wall; row 0 is the top, (x, y) = (column, row)."""
    free = {(x, y) for y, r in enumerate(rows) for x, ch in enumerate(r) if ch != "#"}

    def succ(s):
        (x, y), left = s
        out = []
        for p in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if p in free:
                out.append((p, left - {p}))
        return out
    return free, succ


def true_costs(free, succ, targets):
    """Exact cost to the end for every state, by BFS backwards from the end states."""
    import itertools
    states = [(p, frozenset(c)) for p in free for k in range(len(targets) + 1)
              for c in itertools.combinations(sorted(targets), k) if p not in c]
    pred = {s: [] for s in states}
    for s in states:
        for t in succ(s):
            pred[t].append(s)
    dist = {s: 0 for s in states if not s[1]}
    queue = deque(dist)
    while queue:
        t = queue.popleft()
        for s in pred[t]:
            if s not in dist:
                dist[s] = dist[t] + 1
                queue.append(s)
    return states, dist


def check(rows, targets):
    free, succ = maze_problem(rows, targets)
    states, dist = true_costs(free, succ, targets)
    for s in states:
        h = visit_all_heuristic(s)
        pos, left = s
        if not left:
            assert h == 0, f"h{s} = {h}, expected 0 at an end state"
        far = max((abs(pos[0] - q[0]) + abs(pos[1] - q[1]) for q in left), default=0)
        assert h >= far, f"h{s} = {h} is below the farthest-target distance {far}"
        if s in dist:
            assert h <= dist[s], f"h{s} = {h} exceeds the true cost {dist[s]}"
        for t in succ(s):
            assert h <= 1 + visit_all_heuristic(t), f"not consistent on {s} -> {t}"


def test_corners_open_room():
    rows = ["......", "......", "......", "......"]
    check(rows, {(0, 0), (5, 0), (0, 3), (5, 3)})


def test_corners_with_walls():
    rows = ["#######",
            "#.....#",
            "#.###.#",
            "#.#...#",
            "#.....#",
            "#######"]
    check(rows, {(1, 1), (5, 1), (1, 4), (5, 4)})


def test_scattered_food():
    rows = ["#########",
            "#...#...#",
            "#.#.#.#.#",
            "#.......#",
            "#########"]
    check(rows, {(1, 1), (3, 2), (7, 1), (5, 3), (2, 3)})


def test_single_target_is_tight():
    # with one target left and no walls in the way, the Manhattan distance is exact
    assert visit_all_heuristic(((2, 2), frozenset({(5, 6)}))) == 7
    assert visit_all_heuristic(((2, 2), frozenset())) == 0
```
:::
