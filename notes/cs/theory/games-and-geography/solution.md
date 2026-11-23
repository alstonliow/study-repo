<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-8-q15" status="draft"}
1. *In PSPACE.* Evaluate the game tree recursively. A position is the list of cards placed so far with their sides, so the depth is the number of cards and each level stores one choice. The space is polynomial.

2. *Hardness: reduce from $\mathit{TQBF}$.* Take $\Psi=\exists x_1\forall x_2\cdots\exists x_n\,\psi$ with $\psi$ in 3cnf; by adding dummy variables we may assume the quantifiers alternate. Apply the construction of @prob-sipser3e-7-q26 to $\psi$. This gives a 3cnf-formula $\phi'$ over $x_1,\dots,x_n$, new variables $z_1,\dots,z_m$ and one variable $b$.

3. *Cards and order.* Make one card per variable of $\phi'$ as in @prob-sipser3e-7-q28. Then all positions are blocked iff the chosen sides form a $\ne$-assignment of $\phi'$. Give Player II "blank" cards (every position punched), which never block anything. The order of play is: I places $b$; II a blank; then I places $x_1$, II places $x_2$, and so on through $x_n$; then I places $z_1,\dots,z_m$, with II placing blanks in between.

4. *If I chooses $b$ false.* For fixed $x$, the proof of @prob-sipser3e-7-q26 shows that values of the $z_i$ completing a $\ne$-assignment exist iff $\psi(x)$ is true. So I can win iff $\Psi$ is true.

5. *If I chooses $b$ true.* Negating a $\ne$-assignment gives another one. So a completion exists iff $\psi(\overline{x_1},\dots,\overline{x_n})$ is true. The quantified formula with every $x_i$ negated has the same truth value as $\Psi$.

6. Either way Player I has a winning strategy iff $\Psi$ is true. The construction takes polynomial time, so the problem is PSPACE-complete.
:::

::: {.solution for="prob-sipser3e-8-q10" status="draft"}
1. *Recursive evaluation.* $\mathrm{WIN}(B)$ decides whether the player to move in position $B$ can force a win for X. If X already has five in a row, X has won. If O does, or if the board is full, X has not won.

2. *Recursion.* Otherwise, try every empty cell, place the mover's marker, and evaluate the resulting position recursively. If X is to move, X wins iff some move leads to a position won by X. If O is to move, X wins iff every move leads to a position won by X.

3. *Space.* Each move fills a cell, so the recursion depth is at most $n^2$. Each level stores one position, $O(n^2)$ cells, plus a loop index. The total space is $O(n^4)$, polynomial in the input size $\Theta(n^2)$.

4. So $\mathit{GM}\in\mathrm{PSPACE}$.
:::
