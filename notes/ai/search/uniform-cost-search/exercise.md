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
