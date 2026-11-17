<!-- Migrated from 1058note exercises/chapters/08-counting-combinatorics.tex (CN 8.10 Exercises). -->

::: {.problem #prob-counting-04 origin="external" source="fit1058-cn-8.10-q4"}
The Melbourne city centre grid has five "horizontal" streets (Flinders,
Collins, Bourke, Lonsdale, La Trobe, from south to north) and nine
"vertical" streets (Spencer, King, William, Queen, Elizabeth, Swanston,
Russell, Exhibition, Spring, from west to east), giving $4\times8=32$ square
blocks.

You start at the corner of Flinders and Swanston, and walk along main streets,
never turning back, always going further away from your starting point.

(a) How many routes are there to the corner of William and La Trobe?
    Express your answer using a counting expression, then evaluate it.
(b) How many such routes do not meet Russell Street and take you four
    block-lengths away? Give the total and the number of routes to each
    intersection at this distance. Comment on the relationship among
    these numbers.
(c) How many shortest routes are there from the south-west corner
    (Flinders and Spencer) to the north-east corner (Spring and La
    Trobe)?
:::

::: {.problem #prob-counting-08 origin="external" source="fit1058-cn-8.10-q8"}
Determine the numbers of $n$-digit positive integers that have their digits

(a) in ascending order;
(b) in descending order;
(c) in nondecreasing order;
(d) in nonincreasing order.
:::

::: {.problem #prob-counting-09 origin="external" source="fit1058-cn-8.10-q9"}
**Poker.** A standard deck has 52 cards in four suits
$\spadesuit,\clubsuit,\diamondsuit,\heartsuit$ of 13 cards each, with ranks
$2,3,\dots,10,J,Q,K,A$ ($J,Q,K,A=11,12,13,14$). The Ace can also stand for 1,
but not both low and high in the same hand. A poker hand is a set of five
cards. Five cards are *consecutive* if their ranks are in numerical
sequence (A,2,3,4,5 and 10,J,Q,K,A are allowed, but there is no wrap-around,
e.g. Q,K,A,2,3 is not consecutive).

How many poker hands are there of each type:

(a) no restriction at all;
(b) straight flush: five consecutive cards in the same suit;
(c) four of a kind: four of the five cards have the same rank;
(d) full house: three cards of one rank, two of another;
(e) flush: all five cards the same suit, ranks not all consecutive;
(f) straight: five consecutive cards, not all in the same suit;
(g) three of a kind: three of the same rank, the other two of
    different ranks to those three and to each other;
(h) pair of pairs: two pairs of different ranks, and a fifth card of a
    different rank to the others;
(i) one pair: a single pair, the other three cards of different ranks
    to the pair and to each other;
(j) nothing: none of the types (b)--(i).
:::

::: {.problem #prob-cs70-10-q1 origin="external" source="cs70-10.6-q1"}
Provide a direct combinatorial proof of Corollary 10.1.

*Note (these notes):* Corollary 10.1 of CS70 Note 10 is @cor-alternating-sum.
:::

::: {.problem #prob-cs70hw-6-q5 origin="external" source="cs70hw-6-q5"}
**Maze.**

(a) Given a $4 \times 4$ grid, how many different paths from $(0, 0)$ to $(4, 4)$ satisfy the following condition:

- You can only go from $(x, y)$ to either $(x + 1, y)$ or $(x, y + 1)$

(b) Given a $4 \times 4$ grid, how many different paths from $(0, 0)$ to $(4, 4)$ satisfy the following condition:

- You can only go from $(x, y)$ to either $(x + 1, y)$ or $(x, y + 1)$
- You cannot go to points $(x, y)$ where $y > x$, in other word, you cannot cross line $y = x$

(c) How many sequences of 4 pairs of parentheses are mismatched? An example of a matched sequence of paretheses is ()()()(), while a mismatched sequence is )))(((.
:::

::: {.problem #prob-cs70hw-7-q3 origin="external" source="cs70hw-7-q3"}
**Maze in general and Trees too!!!** Given an maze of sidelength $n$ where one starts at $(0, 0)$ and goes to $(n, n)$.

(a) How many shortest paths are there that go from $(0, 0)$ to $(n, n)$?

(b) Extending the width by 1, how many shortest paths are there that go from $(0, 0)$ to $(n-1, n+1)$.

(c) Now consider shortest paths that meet the conditions which only use to points $(x, y)$ where $y \le x$. That is, the path cannot cross line $y = x$.

  i. Give an expression using part (a) and (b), that counts the number of paths. (Hint: consider what happens after a shortest that crosses $y = x$ at $(i, i)$, that is, the remaining path starting from $(i, i + 1)$ and then continuing to $(n, n)$. If in the remainder of the path, one exchanges the y-direction moves with x-direction moves and vice versa, where does one end up?

  ii. A different tack is to derive a recursive formula. We call these paths $n$-legal paths for a maze of sidelength $n$, and let $F_n$ be the number of $n$-legal paths. Consider a path, and let $i < n$ be the largest value where the path contains $(i, i)$, argue the number of paths is then $F_i * F_{n-i-1}$. (Hint: if $i = 0$, what are your first and last moves, and where is the remainder of the path allowed to go.)

  iii. Give a recursive formula for the number of spanning trees of a complete graph $K_n$ for $n \ge 3$, where each non-root node has degree 3 or 1, and at most 1 node has degree 2? Two trees are different if and only if either left-subtree is different or right-subtree is different. (Notice something about your formula and the maze problem. Neat!)

*Note (these notes):* Part (c)iii is unclear as stated; the solution counts binary trees by their left and right subtrees, as the official solution does.
:::
