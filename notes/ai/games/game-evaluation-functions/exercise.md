::: {.problem #prob-cs221hw-5-q1 origin="external" source="cs221hw-5-q1"}
(a) Before you code up Pac-Man as a minimax agent, notice that instead of just one ghost, Pac-Man could have multiple ghosts as adversaries. We will extend the minimax algorithm from class, which had only one min stage for a single adversary, to the more general case of multiple adversaries. In particular, *your minimax tree will have multiple min layers (one for each ghost) for every max layer*.

Formally, consider the limited depth tree minimax search with evaluation functions taught in class. Suppose there are $n+1$ agents on the board, numbered $0, \ldots, n$, where agent $0$ is Pac-Man and the rest are ghosts. Pac-Man acts as a max agent, and the ghosts act as min agents. A single *depth* consists of all $n+1$ agents making a move, so depth 2 search will involve Pac-Man and each ghost moving two times. In other words, a depth of 2 corresponds to a height of $2(n+1)$ in the minimax game tree (see diagram below).


The diagram draws two branches per node to keep it readable. In the actual game, each node has one branch per legal action of the agent whose turn it is: up to four (North, South, East, West), and fewer when walls block the way.

**Comment:** In reality, all the agents move simultaneously. In our formulation, actions at the same depth happen at the same time in the real game. To simplify things, we process Pac-Man and ghosts sequentially. You should just make sure you process all of the ghosts before decrementing the depth.

Before diving into the recurrence, let's understand our notation. In the recurrence for $V_{\text{minmax}}(s,d)$, $s$ represents the current state, and $d$ represents the current depth in the game tree, with $d = d_{\text{max}}$ indicating the root of the tree (initial state) and decreasing as we go deeper into the tree.

Write the recurrence for $V_{\text{minmax}}(s,d)$ in math as a *piecewise function*. You should express your answer in terms of the following functions:

$\text{IsEnd}(s)$, which tells you if $s$ is an end state.

$\text{Utility}(s)$, the utility of a state $s$, which is invoked at the end states.

$\text{Eval}(s)$, an evaluation function for the state $s$.

$\text{Player}(s)$, which returns the player whose turn it is in state $s$. Ensure you specify conditions like $\textrm{if}~ \text{Player}(s) = 0$ clearly.

$\text{Actions}(s)$, which returns the possible actions that can be taken from state $s$.

$\text{Succ}(s,a)$, which returns the successor state resulting from taking an action $a$ at a certain state $s$.

You may use $n$ anywhere in your solution without explicitly passing it in as an argument. You should not have $d_{\text{max}}$ in your solution. Please stick to notations and terms as described here, and avoid introducing personal variations without clear definitions. Remember, clarity is essential. You may use any relevant notation introduced in lecture.

**Hint:** It will be helpful to review the depth-limited recurrence in the "Evaluation functions" part of the Games I lecture.

*Expected:* The recurrence for $V_{\text{minmax}}(s,d)$ in math as a *piecewise function*, in terms of the functions listed above.

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4). The handout's diagram of a depth-2 tree is not reproduced: it shows Pac-Man's max layer followed by one min layer per ghost, repeated twice.
:::

::: {.problem #prob-cs221hw-5-q3 origin="external" source="cs221hw-5-q3"}
(a) Random ghosts are of course not optimal minimax agents, so modeling them with minimax search is not optimal. Instead, write down the recurrence for $V_{\text{exptmax}}(s,d)$, which is the maximum expected utility against ghosts that each follow the random policy (each ghost chooses a legal move uniformly at random).

*Expected:* Your recurrence should resemble that of problem 1a (including the depth argument $d$), which means that you should write it in terms of the same functions that were specified in problem 1a.

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::
