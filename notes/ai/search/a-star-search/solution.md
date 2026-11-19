<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs188hw-1-q2" status="draft"}
A heuristic is admissible if $h(s)\le$ the true cost from $s$ (@def-admissible-heuristic); in particular $h=0$ at every goal state. Two facts are used throughout: Pacman covers at most $3$ squares of Manhattan distance per timestep (walking covers $1$, the bus $3$), and a heuristic that can be positive at a goal state is not admissible.

1. **Only "Manhattan distance divided by 4".** Since Pacman reduces his Manhattan distance to the university by at most $3$ per timestep, the true cost is at least $\text{MD}/3\ge\text{MD}/4$. Plain Manhattan distance overestimates when the bus carries Pacman most of the way ($3$ squares per timestep). The distance to the bus is positive when Pacman stands on the university and the bus is elsewhere. The distance from the stop nearest Pacman to the university is positive when Pacman is at the university but the route is far away.
2. **None of the above.** Each listed heuristic can be positive at the goal: the distance to the bus whenever the bus is elsewhere; the bus-to-stop distance divided by $3$ likewise; the constant $\frac13$ always; and their minimum whenever all three are positive (the bus away from both Pacman and the stop).
3. **Only the first.** Let $h=\min\bigl(\text{MD}(P,U),\min_{\text{stops }s}\text{MD}(s,U)\bigr)$. If Pacman reaches the university on foot from now on, the cost is at least $\text{MD}(P,U)\ge h$. Otherwise his last bus ride takes at least one timestep and leaves him at most one square from some stop, so the remaining cost is at least $1+(\min_s\text{MD}(s,U)-1)\ge h$. At the goal $\text{MD}(P,U)=0$, so $h=0$. The number of rides so far is at least $1$ at the goal (he must ride once), so it is not admissible. The third is positive at the goal whenever no stop is at the university.
4. **Only the minimum divided by 3.** Pacman must end at the university, so the cost is at least $\text{MD}(P,U)/3\ge h_{\min}$. The sum divided by $3$ contains $\text{MD}(\text{RSF},U)/3>0$ (the grid's width minus one, over $3$) even at the goal, and the maximum of the two equals the sum.
5. **The second and the third.** Xavier walks one square per timestep and must reach the university, so the cost is at least $\text{MD}(X,U)$; Pacman covers at most $3$ squares per timestep and must reach it too, so the cost is at least $\text{MD}(P,U)/3$. Half the Pacman–Xavier distance overestimates when Pacman rides the bus towards Xavier: the gap then closes by up to $4$ squares per timestep, and if they meet next to the university the total cost is about $\text{MD}(P,X)/4+1$, below $\text{MD}(P,X)/2$ for large distances.
:::

::: {.solution for="prob-cs188d-1-q2" status="draft"}
(a) **$4MN(V_{\max}+1)$.** A state must record the position ($MN$ squares), the direction faced ($4$) and the current velocity ($0,1,\dots,V_{\max}$), because the legal actions and their effects depend on all three.

(b) **No.** One action can move the agent up to $V_{\max}$ squares. For example, with $V_{\max}\ge3$ the actions fast, fast, fast, slow, slow, slow move it $1+2+3+2+1+0=9$ squares in a straight line and park it, in $6$ actions, while the Manhattan distance is $9$: an overestimate.

(c) **$h=d_{\text{Manhattan}}/V_{\max}$.** Every action changes the position by at most $V_{\max}$ squares (turns by none), so reaching the exit needs at least $d_{\text{Manhattan}}/V_{\max}$ actions, whatever the walls. A sharper bound also uses the velocity profile: from rest to rest along a straight line, $k$ actions cover at most about $k^{2}/4$ squares, since the velocity must rise and fall by $1$ per action; but the simple bound is already admissible and non-trivial.

(d) **Complete, but not necessarily optimal.** The state space is finite and graph search expands each state at most once, so A\* still finds a solution if one exists; but the optimality argument (@thm-a-star-tree-admissible, @thm-a-star-correct) needs the heuristic never to overestimate, and with an overestimating $h$ the first end state removed may not be the cheapest.

(e) An inadmissible heuristic can be much closer to the true cost on most states (for example $d_{\text{Manhattan}}$ itself here), so A\* expands far fewer nodes and finds a good, often optimal, plan faster; this trades guaranteed optimality for speed.
:::
