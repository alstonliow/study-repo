::: {.problem #prob-mit6006s20-7-q2 origin="external" source="mit6006s20-7-q2"}
**Caged Cats**

Ting Kiger is an eccentric personality who owns $n$ pet tigers and $n^2$ cages.

- Each tiger $i$ has known positive integer age $a_i$ and size $s_i$ (no two have the same age or size).
- Each cage $j$ has known positive integer capacity $c_j$ and distance $d_j$ from Ting's bedroom (no two have the same capacity or distance).

Ting needs to assign each tiger its own cage.

- Ting favors older tigers and wants them to sleep closer to his bedroom, i.e., any two tigers $x$ and $y$ with ages $a_x<a_y$ must be assigned to cages $X$ and $Y$ respectively such that $d_Y<d_X$.
- A tiger $i$ assigned to cage $c_j$ will experience positive discomfort $s_i-c_j$ if $s_i>c_j$, but will not experience any discomfort if $s_i\le c_j$.

Describe an $O(n^3)$-time algorithm to assign tigers to cages that favors older tigers and minimizes the total discomfort experienced by the tigers.

*Note (these notes):* Problem Set 7 begins: "Please solve each of the following problems using dynamic programming. For each problem, be sure to define a set of subproblems, relate the subproblems recursively, argue the relation is acyclic, provide base cases, construct a solution to the original problem from the subproblems, and analyze running time. Correct but inefficient dynamic programs will be awarded significant partial credit."
:::

::: {.problem #prob-mit6006s20-7-q4 origin="external" source="mit6006s20-7-q4"}
**Pizza Partitioning**

Liza Pover and her little brother Lie Pover want to share a round pizza pie that has been cut into $2n$ equal sector slices along rays from the center at angles $\alpha_i=i\pi/n$ for $i\in\{0,1,\dots,2n\}$, where $\alpha_0=\alpha_{2n}$. Each slice $i$ between angles $\alpha_i$ and $\alpha_{i+1}$ has a known integer tastiness $t_i$ (which might be negative). To be "fair" to her little brother, Liza decides to eat slices in the following way:

- They will each take turns choosing slices of pizza to eat: Liza starts as the chooser.
- If there is only one slice remaining, the chooser eats that slice, and eating stops.
- Otherwise the chooser does the following:
  - Angle $\alpha_i$ is proper if there is at least one uneaten slice on either side of the line passing through the center of the pizza at angle $\alpha_i$.
  - The chooser picks any number $i\in\{1,\dots,2n\}$ where $\alpha_i$ is proper, and eats all uneaten slices counter-clockwise around the pizza from angle $\alpha_i$ to angle $\alpha_i+\pi$.
  - Once the chooser has eaten, the other sibling becomes the chooser, and eating continues.

Liza wants to maximize the total tastiness of slices she will eat. Describe an $O(n^3)$-time algorithm to find the maximum total tastiness Liza can guarantee herself via this selection process.

*Note (these notes):* Problem Set 7 begins: "Please solve each of the following problems using dynamic programming. For each problem, be sure to define a set of subproblems, relate the subproblems recursively, argue the relation is acyclic, provide base cases, construct a solution to the original problem from the subproblems, and analyze running time. Correct but inefficient dynamic programs will be awarded significant partial credit."
:::

::: {.problem #prob-mit6006s20-7-q5 origin="external" source="mit6006s20-7-q5"}
**Shorting Stocks**

Bordan Jelfort is a short seller at a financial trading firm. He has collected stock price information from $s$ different companies $C=(c_0,\dots,c_{s-1})$ for $n$ consecutive days. Stock price information for a company $c_i$ is a chronological sequence $P_i=(p_0,\dots,p_{nk-1})$ of $nk$ prices, where each price is a positive integer and prices $\{p_{kj},\dots,p_{kj+k-1}\}$ all occur on day $j$ for $j\in\{0,\dots,n-1\}$. The shorting value of a company is the length of the longest chronological subsequence of strictly decreasing prices for that company that doesn't skip days: if the sequence contains two prices on different days $i$ and $j$ with $i<j$, then the sequence must also contain at least one price from every day in $\{i,\dots,j\}$.

(a) Describe an $O(snk^2)$-time algorithm to determine which company $c_i$ has the highest shorting value, and return a longest subsequence $S$ of decreasing subsequences of prices from $P_i$ that doesn't skip days.

(b) Write a Python function `short_company(C, P, n, k)` that implements your algorithm from part (a) using the template code provided. You can download the code template and some test cases from the website.

```python
def short_company(C, P, n, k):
    '''
    Input:  C | Tuple of s = |C| strings representing names of companies
            P | Tuple of s lists each of size nk representing prices
            n | Number of days of price information
            k | Number of prices in one day
    Output: c | Name of a company with highest shorting value
            S | List containing a longest subsequence of
              | decreasing prices from c that doesn't skip days
    '''
    c = C[0]
    S = []
    ##################
    # YOUR CODE HERE #
    ##################
    return (c, S)
```

*Note (these notes):* Problem Set 7 begins: "Please solve each of the following problems using dynamic programming. For each problem, be sure to define a set of subproblems, relate the subproblems recursively, argue the relation is acyclic, provide base cases, construct a solution to the original problem from the subproblems, and analyze running time. Correct but inefficient dynamic programs will be awarded significant partial credit."
:::

::: {.problem #prob-mit6006r-15-q1 origin="external" source="mit6006r-15-q1"}
**Simplified Blackjack**

We define a simplified version of the game blackjack between one player and a dealer. A deck of cards is an ordered sequence of $n$ cards $D=(c_1,\dots,c_n)$, where each card $c_i$ is an integer between $1$ and $10$ inclusive (unlike in real blackjack, aces will always have value $1$). Blackjack is played in rounds. In one round, the dealer will draw the top two cards from the deck (initially $c_1$ and $c_2$), then the player will draw the next two cards (initially $c_3$ and $c_4$), and then the player may either choose to draw or not draw one additional card (a hit).

The player wins the round if the value of the player's hand (i.e., the sum of cards drawn by the player in the round) is $\le 21$ and exceeds the value of the dealer's hand; otherwise, the player loses the round. The game ends when a round ends with fewer than $5$ cards remaining in the deck. Given a deck of $n$ cards with a known order, describe an $O(n)$-time algorithm to determine the maximum number of rounds the player can win by playing simplified blackjack with the deck.
:::

::: {.problem #prob-mit6006r-15-q2 origin="external" source="mit6006r-15-q2"}
**Text Justification**

Text Justification is the problem of fitting a sequence of $n$ space separated words into a column of lines with constant width $s$, to minimize the amount of white-space between words. Each word can be represented by its width $w_i<s$. A good way to minimize white space in a line is to minimize *badness* of a line. Assuming a line contains words from $w_i$ to $w_j$, the badness of the line is defined as $b(i,j)=(s-(w_i+\dots+w_j))^3$ if $s>(w_i+\dots+w_j)$, and $b(i,j)=\infty$ otherwise. A good text justification would then partition words into lines to minimize the sum total of badness over all lines containing words. The cubic power heavily penalizes large white space in a line. Microsoft Word uses a greedy algorithm to justify text that puts as many words into a line as it can before moving to the next line. This algorithm can lead to some really bad lines. LaTeX on the other hand formats text to minimize this measure of white space using a dynamic program. Describe an $O(n^2)$ algorithm to fit $n$ words into a column of width $s$ that minimizes the sum of badness over all lines.
:::

::: {.problem #prob-mit6046r-5-q1 origin="external" source="mit6046r-5-q1"}
**Rectangular blocks**

Given a set of $n$ rectangular three-dimensional blocks, where block $B_i$ has length $l_i$, width $w_i$, and height $h_i$, all real numbers, find the maximum height of a tower of blocks that is as tall as possible, using any subset of the blocks, such that the tower respects the following constraints:

1. Blocks cannot be rotated: the length always refers to the east-west direction, the width is always north-south, and the height is always up-down.
2. Block $B_i$ can be stacked on top of block $B_j$ only if $l_i\le l_j$ and $w_i\le w_j$, that is, the two dimensions of the base of block $B_i$ are no greater than those of block $B_j$.
:::

::: {.problem #prob-mit6006-16-q1 origin="external" source="mit6006-16-q1"}
Speed up to $O(|A|\log|A|)$ by doing only $O(\log|A|)$ work per subproblem, via AVL tree augmentation

*Note (these notes):* This refers to the longest increasing subsequence DP of @exm-lis, which spends $O(|A|)$ work per subproblem.
:::

::: {.problem #prob-mit6006-16-q2 origin="external" source="mit6006-16-q2"}
Speed up to $\Theta(n^2)$ time by precomputing all sums $\sum_{k=i}^{j}v_k$ in $\Theta(n^2)$ time, via dynamic programming (!)

*Note (these notes):* This refers to the first solution of the alternating coin game, @exm-coin-game, where computing the sum inside each subproblem takes $\Theta(n)$ work and $\Theta(n^3)$ in total.
:::
