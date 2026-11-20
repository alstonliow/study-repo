<!-- Solutions marked status="draft" were written by Claude in our own words,
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-depth-limited-minimax-code" status="draft"}
```{.python}
def minimax(game, s, depth):
    """Return (value, action) of state s, searching depth rounds."""
    if game.is_end(s):
        return game.utility(s), None
    i = game.agent(s)
    if i == 0 and depth == 0:
        return game.evaluate(s), None
    best_value, best_action = None, None
    for a in game.actions(s):
        t = game.succ(s, a)
        # a round ends when the next agent to move is agent 0 again
        next_depth = depth - 1 if game.agent(t) == 0 and i != 0 else depth
        v, _ = minimax(game, t, next_depth)
        if best_value is None or (v > best_value if i == 0 else v < best_value):
            best_value, best_action = v, a
    return best_value, best_action
```

1. The two base cases come first: an end state has its utility, and a cut-off state at agent 0's turn has its evaluation.
2. The depth drops by one when control passes from the last opponent back to agent 0, so `depth` rounds allow `depth` moves of each agent. The test `game.agent(t) == 0 and i != 0` also works when an end state follows, since then the depth is not used.
3. Only a strictly better value replaces the current best, which keeps the first action among ties.
4. With $b$ actions per state and $k$ agents the search visits $O(b^{kd})$ states; this is why the depth is limited and an evaluation function is needed.
:::

::: {.solution for="prob-expectimax-code" status="draft"}
```{.python}
def expectimax(game, s, depth):
    """Return (value, action) of state s against uniformly random opponents."""
    if game.is_end(s):
        return game.utility(s), None
    i = game.agent(s)
    if i == 0 and depth == 0:
        return game.evaluate(s), None
    values = []
    for a in game.actions(s):
        t = game.succ(s, a)
        next_depth = depth - 1 if game.agent(t) == 0 and i != 0 else depth
        values.append(expectimax(game, t, next_depth)[0])
    if i != 0:
        return sum(values) / len(values), None
    best = max(range(len(values)), key=values.__getitem__)   # first maximum
    return values[best], game.actions(s)[best]
```

1. The recursion is that of minimax with one change: at an opponent's state the minimum becomes the mean, the expectation under the uniform policy $\pi_{\text{opp}}$.
2. `max` over indices returns the first index with the largest value, so ties go to the first action.
3. The value is now the expected utility of agent 0 if it plays the expectimax policy against random opponents. Minimax is pessimistic when the opponents are random: in the second test it settles for $5$ where the expected value of the other branch is $50$.
:::
