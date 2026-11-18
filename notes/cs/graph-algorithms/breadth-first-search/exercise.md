::: {.problem #prob-mit6006s20-5-q3 origin="external" source="mit6006s20-5-q3"}
**Short-Circuitry**

Star-crossed androids Romie-0 and Julie-8 are planning an engagement party and want to invite all their robotic friends. Unfortunately, many pairs of their friends can't be in the same room without short-circuiting. Romie-0 has an idea to throw two parties instead: inviting some friends to the first party, and the rest to the second. Ideally, everyone would get invited to a party, but nobody would go to the same party as someone that would make them short-circuit. Julie-8 points out to Romie-0 that this might not be possible, for example if they have three friends who all make each other short-circuit. Given the $n$ short-circuiting pairs of friends, describe an $O(n)$-time algorithm to determine whether Romie-0 and Julie-8 can invite all of their friends to two peaceful parties, without anyone short-circuiting.
:::

::: {.problem #prob-mit6006s20-5-q4 origin="external" source="mit6006s20-5-q4"}
**Ancient Avenue**

The ancient kingdom of Pesomotamia was a fertile land near the Euphris and Tigrates rivers. Newly-discovered clay tablets show a map of the kingdom on an $n\times n$ square grid, with each square either:

- part of a river, labeled as `'euphris'` or `'tigrates'`; or
- not part of a river, labeled with a string: the name of the farmer who owned the square plot of land.

The tablets accompanying the map state that ancient merchants built a trade route connecting the two rivers: a path along edges of the grid from some grid intersection adjacent to a `'euphris'` square to a grid intersection adjacent to a `'tigrates'` square. The tablets also state that the route:

- did not use any edge between two squares owned by the same farmer (so as not to trample crops); and
- was the shortest such path between the rivers (assume a shortest such path is unique).

Given the labeled map, describe an $O(n^2)$-time algorithm to determine path of the ancient trade route.
:::

::: {.problem #prob-mit6006s20-5-q5 origin="external" source="mit6006s20-5-q5"}
**Statum Quest**

Liza Pover is a hero on a quest for free pizza in the Statum Center, a large labyrinth with some of the best free food in the entire Technological Institute of Mathachusetts. Many unsuspecting victims have ventured into the labyrinth in search of free food, but few have escaped victorious. Luckily, Liza has downloaded a map from `bplansc.tim.edu` consisting of locations $L$ (including rooms, hallways, staircases, and elevators) and doors $D$ which connect pairs of locations. One location $e\in L$ is marked as the entrance/exit: Liza's path must begin and end here. A subset $\Pi\subset L$ of locations each contain a free pizza. Liza's goal is to enter the maze, grab one pizza, and leave as quickly as possible.

Each door $d=(\ell_1,\ell_2)$ connects two locations $\ell_1$ and $\ell_2$ and may be one-way (can be traversed only from $\ell_1$ to $\ell_2$) or two-way (can be traversed in either direction). In addition, each door $d$ may require card access to one of the four Statum Center labs — See-Sail, TOPS, S3C, and DSW. A card-access door of type $t\in\{\text{SeeSail},\text{TOPS},\text{S3C},\text{DPW}\}$ can only be traversed after Liza acquires the matching key card, where the key card of type $t$ is in a known location $\ell_t$.

Describe an $O(|L|+|D|)$-time algorithm to find a viable path from $e$ to $e$ that collects at least one pizza from $\Pi$ (and possibly some of the key cards along the way to open some doors), and minimizes the number of times that Liza has to walk through a door.

(Footnotes: Formerly known as freshmen. We model an entire elevator column as one location, with a door to each floor location it can access. Super Secret Spider Consortium. Department of Speechlore and Wisdomlove.)
:::

::: {.problem #prob-mit6006s20-5-q6 origin="external" source="mit6006s20-5-q6"}
**6.006 Tilt**

6.006 Tilt is a puzzle game played on a Tilt board: an $n\times n$ square grid, where grid square contains either a fixed obstacle, a movable slider, or neither (the grid square is empty).

A Tilt move consists of tilting a board in any of the four cardinal directions (up, left, down or right), causing each slider to slide maximally in that direction until it hits either: the edge of the board, an obstacle, or another slider that cannot slide any further. A Tilt move results in a new Tilt board configuration.

Given a Tilt board $B$ with one grid square $t$ labeled as the target, a sequence of $k$ Tilt moves solves 6.006 Tilt puzzle $(B,t)$ if applying the moves in sequence to $B$ results in a Tilt board configuration $B'$ that contains a slider in square $t$.

The figure below shows a small 6.006 Tilt puzzle and a solution using the fewest possible moves $k=8$. Obstacles are shown in black, movable sliders are circles, and the target square is shaded gray.

We represent an $n\times n$ board configuration $B$ using a length-$n$ tuple of length-$n$ tuples, each representing a row of the configuration, where the grid square in row $y$ (from the top) and column $x$ (from the left) is `B[y][x]`, equal to either character `'#'` (an obstacle), `'o'` (a slider), or `'.'` (neither). We represent the target square by a tuple `t = (xt, yt)` where the puzzle is solved when `B[yt][xt] = 'o'`. Your code template has a function `move(B, d)` which computes a move from board `B` in direction `d` in $O(n^2)$ time.

(a) Given a Tilt puzzle with starting $n\times n$ board $B$ containing $b$ fixed obstacles and $s$ movable sliders, argue that the number of board configurations reachable from $B$ is at most $C(n,b,s)=\frac1{s!}\prod_{i=0}^{s-1}(n^2-b-i)$.

(b) If Tilt board configuration $B$ can reach another Tilt board configuration $B'$ by a single move, we call $B'$ a successor of $B$, and $B$ a predecessor of $B'$. Argue that a board configuration $B$ may have $\Omega(n^s)$ predecessors, but has at most $r=O(1)$ successors.

(c) Given a 6.006 Tilt puzzle $(B,t)$, describe an algorithm to return a move sequence that solves the puzzle in the fewest moves, or return that no such move sequence exists. If the puzzle's shortest solution uses $k$ moves ($k=\infty$ if the puzzle is not solvable), your algorithm should run in $O(n^2\min\{r^k,C(n,b,s)\})$ time.

(d) Write a Python function `solve_tilt(B, t)` that implements your algorithm from part (d) using the template code provided. You can download the code template and some test cases from the website.

*Note (these notes):* The original shows an example puzzle with an 8-move solution as a sequence of pictures; it is not reproduced.
:::

::: {.problem #prob-mit6006r-9-q2 origin="external" source="mit6006r-9-q2"}
Given an unweighted graph $G=(V,E)$, find a shortest path from $s$ to $t$ having an odd number of edges.
:::
