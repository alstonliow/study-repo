::: {.problem #prob-cs188hw-3-q1 origin="external" source="cs188hw-3-q1"}
**Games.** Alice, Eve, and Bob are playing a multiplayer game. Each game state consists of three numbers where the left value represents Alice's score, the middle value represents Eve's score, and the right value represents Bob's score. Alice makes the first move, followed by Eve, and finally Bob. All scores for a single player are between 1 and 9 inclusive. In all pruning scenarios, remember that we do not prune on equality.

Rather than trying to maximize their individual scores, Alice and Bob decide to work together to maximize their combined score, hoping that this will allow them to score higher. At each of Alice's and Bob's nodes, they will choose the option that maximizes left value + right value.

Eve overhears their plan and decides that instead of maximizing her own score, she will try to minimize Alice and Bob's combined score. Alice and Bob are aware of Eve's strategy. Let the value of a node be the sum of the left and right scores of the node. Answer the following questions based on the game tree shown below.

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm, scale=0.85]
\draw[cell frame] (-0.63,-0.21) rectangle (-0.21,0.21);
\draw[cell frame] (-0.21,-0.21) rectangle (0.21,0.21);
\draw[cell frame] (0.21,-0.21) rectangle (0.63,0.21);
\coordinate (rt) at (0.00,0.21); \coordinate (rb) at (0.00,-0.21);
\draw[cell frame] (-4.23,-1.51) rectangle (-3.81,-1.09);
\draw[cell frame] (-3.81,-1.51) rectangle (-3.39,-1.09);
\draw[cell frame] (-3.39,-1.51) rectangle (-2.97,-1.09);
\coordinate (e0t) at (-3.60,-1.09); \coordinate (e0b) at (-3.60,-1.51);
\draw[cell frame] (2.97,-1.51) rectangle (3.39,-1.09);
\draw[cell frame] (3.39,-1.51) rectangle (3.81,-1.09);
\draw[cell frame] (3.81,-1.51) rectangle (4.23,-1.09);
\coordinate (e1t) at (3.60,-1.09); \coordinate (e1b) at (3.60,-1.51);
\draw[cell frame] (-6.03,-2.81) rectangle (-5.61,-2.39);
\draw[cell frame] (-5.61,-2.81) rectangle (-5.19,-2.39);
\draw[cell frame] (-5.19,-2.81) rectangle (-4.77,-2.39);
\coordinate (b0t) at (-5.40,-2.39); \coordinate (b0b) at (-5.40,-2.81);
\draw[cell frame] (-2.43,-2.81) rectangle (-2.01,-2.39);
\draw[cell frame] (-2.01,-2.81) rectangle (-1.59,-2.39);
\draw[cell frame] (-1.59,-2.81) rectangle (-1.17,-2.39);
\coordinate (b1t) at (-1.80,-2.39); \coordinate (b1b) at (-1.80,-2.81);
\draw[cell frame] (1.17,-2.81) rectangle (1.59,-2.39);
\draw[cell frame] (1.59,-2.81) rectangle (2.01,-2.39);
\draw[cell frame] (2.01,-2.81) rectangle (2.43,-2.39);
\coordinate (b2t) at (1.80,-2.39); \coordinate (b2b) at (1.80,-2.81);
\draw[cell frame] (4.77,-2.81) rectangle (5.19,-2.39);
\draw[cell frame] (5.19,-2.81) rectangle (5.61,-2.39);
\draw[cell frame] (5.61,-2.81) rectangle (6.03,-2.39);
\coordinate (b3t) at (5.40,-2.39); \coordinate (b3b) at (5.40,-2.81);
\draw[cell frame] (-6.93,-4.11) rectangle (-6.51,-3.69);
\node[lab] at (-6.72,-3.90) {$2$};
\draw[cell frame] (-6.51,-4.11) rectangle (-6.09,-3.69);
\draw[cell frame] (-6.09,-4.11) rectangle (-5.67,-3.69);
\node[lab] at (-5.88,-3.90) {$2$};
\coordinate (l0t) at (-6.30,-3.69); \coordinate (l0b) at (-6.30,-4.11);
\node[lab] at (-6.30,-4.4) {A};
\draw[cell frame] (-5.13,-4.11) rectangle (-4.71,-3.69);
\node[lab] at (-4.92,-3.90) {$7$};
\draw[cell frame] (-4.71,-4.11) rectangle (-4.29,-3.69);
\draw[cell frame] (-4.29,-4.11) rectangle (-3.87,-3.69);
\node[lab] at (-4.08,-3.90) {$5$};
\coordinate (l1t) at (-4.50,-3.69); \coordinate (l1b) at (-4.50,-4.11);
\node[lab] at (-4.50,-4.4) {B};
\draw[cell frame] (-3.33,-4.11) rectangle (-2.91,-3.69);
\node[lab] at (-3.12,-3.90) {$9$};
\draw[cell frame] (-2.91,-4.11) rectangle (-2.49,-3.69);
\draw[cell frame] (-2.49,-4.11) rectangle (-2.07,-3.69);
\node[lab] at (-2.28,-3.90) {$X$};
\coordinate (l2t) at (-2.70,-3.69); \coordinate (l2b) at (-2.70,-4.11);
\node[lab] at (-2.70,-4.4) {C};
\draw[cell frame] (-1.53,-4.11) rectangle (-1.11,-3.69);
\node[lab] at (-1.32,-3.90) {$8$};
\draw[cell frame] (-1.11,-4.11) rectangle (-0.69,-3.69);
\draw[cell frame] (-0.69,-4.11) rectangle (-0.27,-3.69);
\node[lab] at (-0.48,-3.90) {$5$};
\coordinate (l3t) at (-0.90,-3.69); \coordinate (l3b) at (-0.90,-4.11);
\node[lab] at (-0.90,-4.4) {D};
\draw[cell frame] (0.27,-4.11) rectangle (0.69,-3.69);
\node[lab] at (0.48,-3.90) {$1$};
\draw[cell frame] (0.69,-4.11) rectangle (1.11,-3.69);
\draw[cell frame] (1.11,-4.11) rectangle (1.53,-3.69);
\node[lab] at (1.32,-3.90) {$Y$};
\coordinate (l4t) at (0.90,-3.69); \coordinate (l4b) at (0.90,-4.11);
\node[lab] at (0.90,-4.4) {E};
\draw[cell frame] (2.07,-4.11) rectangle (2.49,-3.69);
\node[lab] at (2.28,-3.90) {$2$};
\draw[cell frame] (2.49,-4.11) rectangle (2.91,-3.69);
\draw[cell frame] (2.91,-4.11) rectangle (3.33,-3.69);
\node[lab] at (3.12,-3.90) {$4$};
\coordinate (l5t) at (2.70,-3.69); \coordinate (l5b) at (2.70,-4.11);
\node[lab] at (2.70,-4.4) {F};
\draw[cell frame] (3.87,-4.11) rectangle (4.29,-3.69);
\node[lab] at (4.08,-3.90) {$5$};
\draw[cell frame] (4.29,-4.11) rectangle (4.71,-3.69);
\draw[cell frame] (4.71,-4.11) rectangle (5.13,-3.69);
\node[lab] at (4.92,-3.90) {$3$};
\coordinate (l6t) at (4.50,-3.69); \coordinate (l6b) at (4.50,-4.11);
\node[lab] at (4.50,-4.4) {G};
\draw[cell frame] (5.67,-4.11) rectangle (6.09,-3.69);
\node[lab] at (5.88,-3.90) {$6$};
\draw[cell frame] (6.09,-4.11) rectangle (6.51,-3.69);
\draw[cell frame] (6.51,-4.11) rectangle (6.93,-3.69);
\node[lab] at (6.72,-3.90) {$1$};
\coordinate (l7t) at (6.30,-3.69); \coordinate (l7b) at (6.30,-4.11);
\node[lab] at (6.30,-4.4) {H};
\draw (rb) -- (e0t);
\draw (rb) -- (e1t);
\draw (e0b) -- (b0t);
\draw (e0b) -- (b1t);
\draw (e1b) -- (b2t);
\draw (e1b) -- (b3t);
\draw (b0b) -- (l0t);
\draw (b0b) -- (l1t);
\draw (b1b) -- (l2t);
\draw (b1b) -- (l3t);
\draw (b2b) -- (l4t);
\draw (b2b) -- (l5t);
\draw (b3b) -- (l6t);
\draw (b3b) -- (l7t);
\end{tikzpicture}
\end{center}
```

*Figure 1: Game tree where Alice is the root maximizer, Eve is the minimizer, and Bob is the bottom maximizer. Eve's score at each node (center cell) is not shown for simplicity.*

1. Solve the game tree shown in Figure 1. What is the value of the root node?

   6 12 13 Depends on the value of X only. Depends on the value of Y only. Depends on the values of both X and Y. None of the above
2. Without pruning, which of the following are possible values for the right minimizer?

   $<6$ 6 7 8 $>8$
3. Which of the following nodes are guaranteed to be pruned when running alpha-beta pruning on the game tree above? If there are nodes that may or may not be pruned depending on the values of $X$ and $Y$, do not select them.

   A D G B E H C F None of the above
4. Which of the following nodes may or may not be pruned depending on the values of $X$ and $Y$? Do not select any nodes from the previous part which are guaranteed to be pruned regardless of the values for $X$ and $Y$.

   A D G B E H C F None of the above

Eve now decides that in addition to minimizing Alice and Bob's scores, she also wants to maximize her own score. Her new strategy is to choose the option that maximizes her own score minus Alice and Bob's combined score. That is, at Eve's turn, she will choose the option that maximizes middle value $-$ (left value + right value). Alice and Bob are aware of this new strategy. Using the same game tree shown above, assume that we can choose any number between 1 and 9 (inclusive) for $X$, $Y$, and Eve's score at each leaf node.

5. True/False: Compared to Eve's strategy in part (a), Eve's new strategy will result in an equal or higher final score for Eve in any leaf node configuration.

   True False
6. True/False: Compared to Eve's strategy in part (a), Eve's new strategy will result in an equal or higher final combined score for Alice and Bob in any leaf node configuration.

   True False
7. Which of the following leaf nodes could possibly be the game outcome if all players play optimally according to their strategy?

   A C E G B D F H
8. Is it possible to prune in this scenario?
   - Yes because scores in each cell are bounded between 1 and 9.
   - Yes but not for the reason above.
   - No because Alice, Bob, and Eve are all acting as maximizers.
   - No but not for the reason above.

Eve is fed up with Alice and Bob teaming up and quits the game. Alice and Bob continue playing and decide to use brand new strategies that incorporate Eve's score for fun. This new game setup can be represented in the diagram below. In each of the following scenarios, Alice and Bob are aware of each other's strategies.

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\draw[cell frame] (-0.63,-0.21) rectangle (-0.21,0.21);
\draw[cell frame] (-0.21,-0.21) rectangle (0.21,0.21);
\draw[cell frame] (0.21,-0.21) rectangle (0.63,0.21);
\fill[ink] (-0.52,0.23) -- (-0.32,0.23) -- (-0.42,0.40) -- cycle;
\coordinate (rt) at (0.00,0.21); \coordinate (rb) at (0.00,-0.21);
\node[lab] at (-1.4,0) {Alice};
\draw[cell frame] (-2.53,-1.51) rectangle (-2.11,-1.09);
\draw[cell frame] (-2.11,-1.51) rectangle (-1.69,-1.09);
\draw[cell frame] (-1.69,-1.51) rectangle (-1.27,-1.09);
\fill[ink] (-1.58,-1.07) -- (-1.38,-1.07) -- (-1.48,-0.90) -- cycle;
\coordinate (b0t) at (-1.90,-1.09); \coordinate (b0b) at (-1.90,-1.51);
\draw[cell frame] (1.27,-1.51) rectangle (1.69,-1.09);
\draw[cell frame] (1.69,-1.51) rectangle (2.11,-1.09);
\draw[cell frame] (2.11,-1.51) rectangle (2.53,-1.09);
\fill[ink] (2.22,-1.07) -- (2.42,-1.07) -- (2.32,-0.90) -- cycle;
\coordinate (b1t) at (1.90,-1.09); \coordinate (b1b) at (1.90,-1.51);
\node[lab] at (-3.3,-1.3) {Bob};
\draw[cell frame] (-3.48,-2.81) rectangle (-3.06,-2.39);
\draw[cell frame] (-3.06,-2.81) rectangle (-2.64,-2.39);
\draw[cell frame] (-2.64,-2.81) rectangle (-2.22,-2.39);
\coordinate (l0t) at (-2.85,-2.39); \coordinate (l0b) at (-2.85,-2.81);
\node[lab] at (-2.85,-3.1) {A};
\draw[cell frame] (-1.58,-2.81) rectangle (-1.16,-2.39);
\draw[cell frame] (-1.16,-2.81) rectangle (-0.74,-2.39);
\draw[cell frame] (-0.74,-2.81) rectangle (-0.32,-2.39);
\coordinate (l1t) at (-0.95,-2.39); \coordinate (l1b) at (-0.95,-2.81);
\node[lab] at (-0.95,-3.1) {B};
\draw[cell frame] (0.32,-2.81) rectangle (0.74,-2.39);
\draw[cell frame] (0.74,-2.81) rectangle (1.16,-2.39);
\draw[cell frame] (1.16,-2.81) rectangle (1.58,-2.39);
\coordinate (l2t) at (0.95,-2.39); \coordinate (l2b) at (0.95,-2.81);
\node[lab] at (0.95,-3.1) {C};
\draw[cell frame] (2.22,-2.81) rectangle (2.64,-2.39);
\draw[cell frame] (2.64,-2.81) rectangle (3.06,-2.39);
\draw[cell frame] (3.06,-2.81) rectangle (3.48,-2.39);
\coordinate (l3t) at (2.85,-2.39); \coordinate (l3b) at (2.85,-2.81);
\node[lab] at (2.85,-3.1) {D};
\draw (rb) -- (b0t);
\draw (rb) -- (b1t);
\draw (b0b) -- (l0t);
\draw (b0b) -- (l1t);
\draw (b1b) -- (l2t);
\draw (b1b) -- (l3t);
\end{tikzpicture}
\end{center}
```

*Figure 2: Game tree where Alice is the root and Bob controls the nodes in the middle level. Black triangles above a cell indicate that the cell's value contains the current player's score. (As a reminder, Bob's score is the right value and Alice's score is the left value.)*

9. Alice and Bob agree to use the following strategy: each player maximizes their own score **plus** the average of the remaining two scores at each node. Assume that you can assign any value between 1 to 9 (inclusive) to all the leaf node scores. Is it possible to prune in this scenario?
   - Yes.
   - No because Alice and Bob are both acting as maximizers.
   - No because Alice and Bob are both acting as expectimax nodes.
   - No but not for the above reasons.
10. Alice and Bob decide to follow a new strategy: each player maximizes their own score **minus** the average of the remaining two scores at each node. Assume that you can assign any value between 1 to 9 (inclusive) to all the leaf node scores. Is it possible to prune in this scenario?
    - Yes.
    - No because Alice and Bob are both acting as maximizers.
    - No because Alice and Bob are both acting as expectimax nodes.
    - No because Alice and Bob are maximizing different values which are not directly adversarial.
    - No but not for the above reasons.

*Note (these notes):* Figures redrawn; Bob's nodes in Figure 1 have children $(A,B)$, $(C,D)$, $(E,F)$, $(G,H)$, and the leaves show (left, middle, right) values with Eve's middle value hidden.
:::
