::: {.problem #prob-mit18065ps-24-q5 origin="external" source="mit18065ps-24-q5"}
Find the optimal (minimizing) strategy for $X$ to choose rows. Find the optimal (maximizing) strategy for $Y$ to choose columns. What is the payoff from $X$ to $Y$ at this optimal minimax point $\mathbf{x}^*,\mathbf{y}^*$ ?
$$\text{Payoff matrices}\qquad\begin{bmatrix}1&2\\4&8\end{bmatrix}\qquad\begin{bmatrix}1&4\\8&2\end{bmatrix}$$
:::

::: {.problem #prob-mit6854ps-4-q1 origin="external" source="mit6854ps-4-q1"}
In a *0-sum 2-player game*, Alice has a choice of $n$ so-called *pure strategies* and Bob has a choice of $m$ pure strategies. If Alice picks strategy $i$ and Bob picks strategy $j$, then the *payoff* is $a_{ij}$, meaning $a_{ij}$ dollars are transfered from Alice to Bob. So Bob makes money if $a_{ij}$ is positive, but Alice makes money if $a_{ij}$ is negative. Thus, Alice wants to pick a strategy that minimizes the payoff while Bob wants a strategy that maximizes the payoff. The matrix $A=(a_{ij})$ is called the *payoff matrix*.

It is well known that to play these games well, you need to use a *mixed* strategy—a random choice from among pure strategies. A mixed strategy is just a particular probability distribution over pure strategies: you flip coins and then play the selected pure strategy. If Alice has mixed strategy $x$, meaning he plays strategy $i$ with probability $x_i$, and Bob has mixed strategy $y$, then it is easy to prove that the expected payoff in the resulting game is $x^TAy$. Alice wants to minimize this expected payoff while Bob wants to maximize it. Our goal is to understand what strategies each player should play.

We'll start by making the pessimal assumption for Alice that whichever strategy she picks, Bob will play best possible strategy against her. In other words, given Alice's strategy $x$, Bob will pick a strategy $y$ that achieves $\max_yx^TAy$. Thus, Alice wants to find a distribution $x$ that minimizes $\max_yx^TAy$. Similarly, Bob wants a $y$ to maximize $\min_xx^TAy$. So we are interested in solving the following 2 problems:
$$\min_{x:\sum x_i=1,x\ge0}\ \max_{y:\sum y_j=1,y\ge0}x^TAy$$
$$\max_{y:\sum y_j=1,y\ge0}\ \min_{x:\sum x_i=1,x\ge0}x^TAy$$
Unfortunately, these look like nonlinear programs!

1. Show that if Alice's mixed strategy is known, then Bob has a pure strategy serving as his best response.
2. Show how to convert each program above into a linear program, and thus find an optimal strategy for both players in polynomial time.
3. Use strong duality (applied to the LP you built in the previous part) to argue that the above two quantities are *equal*.

The second statement shows that the strategies $x$ and $y$, besides being optimal, are in *Nash Equilibrium*: even if each player knows the other's strategy, there is no point in changing strategies. This was proven by Von Neumann and was actually one of the ideas that led to the discovery of strong duality.
:::
