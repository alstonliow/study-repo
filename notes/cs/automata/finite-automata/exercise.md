<!-- Sipser problems assigned in MIT 18.404J (Fall 2020) problem sets, which cite them by number only.
     Statements verbatim from the 3rd edition (owner decision 2026-11-23, meta/SPEC.md §10). -->

<!-- Sipser 1.32; 18.404J PS1 Q1 -->
::: {.problem #prob-sipser3e-1-q32 origin="external" source="sipser3e-1-q32"}
Let
$$\Sigma_3=\left\{\begin{bmatrix}0\\0\\0\end{bmatrix},\begin{bmatrix}0\\0\\1\end{bmatrix},\begin{bmatrix}0\\1\\0\end{bmatrix},\dots,\begin{bmatrix}1\\1\\1\end{bmatrix}\right\}.$$
$\Sigma_3$ contains all size 3 columns of 0s and 1s. A string of symbols in $\Sigma_3$ gives three rows of 0s and 1s. Consider each row to be a binary number and let
$$B=\{w\in\Sigma_3^*\mid \text{the bottom row of } w \text{ is the sum of the top two rows}\}.$$
For example,
$$\begin{bmatrix}0\\0\\1\end{bmatrix}\begin{bmatrix}1\\0\\0\end{bmatrix}\begin{bmatrix}1\\1\\0\end{bmatrix}\in B,\quad\text{but}\quad\begin{bmatrix}0\\0\\1\end{bmatrix}\begin{bmatrix}1\\0\\1\end{bmatrix}\notin B.$$
Show that $B$ is regular. (Hint: Working with $B^{\mathcal R}$ is easier. You may assume the result claimed in Problem 1.31.)
:::

<!-- Sipser 1.41; 18.404J PS1 Q2 -->
::: {.problem #prob-sipser3e-1-q41 origin="external" source="sipser3e-1-q41"}
For languages $A$ and $B$, let the *perfect shuffle* of $A$ and $B$ be the language
$$\{w\mid w=a_1b_1\cdots a_kb_k,\text{ where } a_1\cdots a_k\in A \text{ and } b_1\cdots b_k\in B,\text{ each } a_i,b_i\in\Sigma\}.$$
Show that the class of regular languages is closed under perfect shuffle.
:::

<!-- Sipser 1.59; 18.404J PS1 Q8 -->
::: {.problem #prob-sipser3e-1-q59 origin="external" source="sipser3e-1-q59"}
Let $M=(Q,\Sigma,\delta,q_0,F)$ be a DFA and let $h$ be a state of $M$ called its "home". A *synchronizing sequence* for $M$ and $h$ is a string $s\in\Sigma^*$ where $\delta(q,s)=h$ for every $q\in Q$. (Here we have extended $\delta$ to strings, so that $\delta(q,s)$ equals the state where $M$ ends up when $M$ starts at state $q$ and reads input $s$.) Say that $M$ is *synchronizable* if it has a synchronizing sequence for some state $h$. Prove that if $M$ is a $k$-state synchronizable DFA, then it has a synchronizing sequence of length at most $k^3$. Can you improve upon this bound?
:::
