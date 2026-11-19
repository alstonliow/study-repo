::: {.problem #prob-cs188hw-2-q1 origin="external" source="cs188hw-2-q1"}
**Secret Santa.** The CS 188 staff members are playing Secret Santa! Each person brings a gift to the table, intending for a different person to receive that gift. However, past TA Albert, furious that he was not invited to participate, removes all the name cards on each gift so that none of the staff members know whose gift is whose!

The gifts are: AI textbook (A), Backgammon (B), Chess (C), Dinosaur toy (D), Easter egg (E), Flying drone (F) and Game of "Go" (G).

The participants are: Angela, Danial, Jonathan, Regina, Ryan, Saathvik, Yanlai.

Angela and Regina are juniors and everybody else is a senior.

While the staff members have forgotten which gift is for who, Albert has left them some clues.

1. Each person should receive exactly one gift.
2. Any person whose name starts with R (Ryan, Regina) should not receive the AI textbook.
3. The Easter egg and Flying drone are for people of different grades.
4. The Flying drone and the Game of Go are for people of the same grade.
5. Any person whose name ends with a consonant (Danial, Jonathan, Ryan, Saathvik) should not receive the Chess set.

We frame this problem as a CSP, with the variable being a person, and the domain being the item they receive.

1. Given just these clues, we use local search to try to find a satisfying assignment. We'll initialize the assignments alphabetically (i.e. assign the $i$th person in alphabetical order to the $i$th gift in alphabetical order). Which of the variables are conflicted in this assignment?
   - Angela
   - Danial
   - Jonathan
   - Regina
   - Ryan
   - Saathvik
   - Yanlai
   - None of the above
2. Because of the first clue, our iterative improvement strategy involves swapping the values of two variables. What is the minimum number of swaps needed for us to get an assignment that satisfies the above constraints?

   0 1 2 3 4 5
3. Say we randomly choose to swap Ryan's value with someone else and use min-conflicts to decide who to swap with. Which of the people could be selected by the min-conflicts heuristic for Ryan to swap with?
   - Angela
   - Danial
   - Jonathan
   - Regina
   - Ryan
   - Saathvik
   - Yanlai
   - None of the above

Now Albert gives a few more clues:

6. One of Angela, Jonathan, Saathvik, or Yanlai should get Backgammon.
7. The person who should get Backgammon and the person who should get the Dinosaur have names with the same number of letters.
8. Regina's name contains the letter of the gift she should receive (i.e. A, E, or G).

The TAs restart with all the variables unassigned, then enforce all unary constraints and perform arc consistency.

4. Do we have enough information to fully deduce the value of any of the variables?

   Yes No
5. How many values are left in Ryan's domain?

   1 2 3 4 5 6 7
6. Using the MRV heuristic, which variable(s) could be assigned next? Select multiple if there's a tie.
   - Angela
   - Danial
   - Jonathan
   - Regina
   - Ryan
   - Saathvik
   - Yanlai
   - None of the above

   How many values are in their domain?

   1 2 3 4 5 6 7
7. Breaking ties alphabetically, we assign the first MRV variable then enforce arc consistency. Now, how many values are left in Angela's Domain?

   1 2 3 4 5 6 7

Albert now gives one last clue:

9. The Easter egg should go to a TA whose grade is a senior.

We want to use this information to solve our CSP.

Hint: We may have to backtrack assignments from a previous part.

8. Do we have enough information to fully deduce the value of any of the variables?

   Yes No
9. Complete a full recursive backtracking search and identify a satisfying assignment. Apply the MRV heuristic when needed and break any ties alphabetically. Which gift does each person get?
   - Angela: A B C D E F G
   - Danial: A B C D E F G
   - Jonathan: A B C D E F G
   - Regina: A B C D E F G
   - Ryan: A B C D E F G
   - Saathvik: A B C D E F G
   - Yanlai: A B C D E F G
10. Which variable is assigned last in the backtracking search?

    Angela Jonathan Ryan Yanlai Danial Regina Saathvik
:::

::: {.problem #prob-cs188d-2-q1 origin="external" source="cs188d-2-q1"}
**CSPs: Trapped Pacman.** Pacman is trapped! He is surrounded by mysterious corridors, each of which leads to either a pit (P), a ghost (G), or an exit (E). In order to escape, he needs to figure out which corridors, if any, lead to an exit and freedom, rather than the certain doom of a pit or a ghost.

The one sign of what lies behind the corridors is the wind: a pit produces a strong breeze (S) and an exit produces a weak breeze (W), while a ghost doesn't produce any breeze at all. Unfortunately, Pacman cannot measure the strength of the breeze at a specific corridor. Instead, he can stand *between* two adjacent corridors and feel the max of the two breezes. For example, if he stands between a pit and an exit he will sense a strong (S) breeze, while if he stands between an exit and a ghost, he will sense a weak (W) breeze. The measurements for all intersections are shown in the figure below.

Also, while the total number of exits might be zero, one, or more, Pacman knows that two neighboring squares will *not* both be exits.

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.2cm, y=1.2cm]
\node[lab] at (0,0) {Pacman};
\node[vertex] (c1) at (0.00,1.30) {1};
\node[vertex] (c2) at (1.13,0.65) {2};
\node[vertex] (c3) at (1.13,-0.65) {3};
\node[vertex] (c4) at (0.00,-1.30) {4};
\node[vertex] (c5) at (-1.13,-0.65) {5};
\node[vertex] (c6) at (-1.13,0.65) {6};
\node[lab, emph] at (0.62,1.07) {S};
\node[lab, emph] at (1.23,0.00) {W};
\node[lab, emph] at (0.62,-1.07) {W};
\node[lab, emph] at (-0.62,-1.07) {S};
\node[lab, emph] at (-1.23,-0.00) {S};
\node[lab, emph] at (-0.62,1.07) {S};
\end{tikzpicture}
\end{center}
```

Pacman models this problem using variables $X_i$ for each corridor $i$ and domains P, G, and E.

(a) State the binary and/or unary constraints for this CSP (either implicitly or explicitly).

(b) Suppose we assign $X_1$ to E. Perform forward checking after this assignment. Also, enforce unary constraints.

| $X_1$ | | | E |
|---|---|---|---|
| $X_2$ | P | G | E |
| $X_3$ | P | G | E |
| $X_4$ | P | G | E |
| $X_5$ | P | G | E |
| $X_6$ | P | G | E |

(c) Suppose forward checking returns the following set of possible assignments:

| $X_1$ | P | | |
|---|---|---|---|
| $X_2$ | | G | E |
| $X_3$ | | G | E |
| $X_4$ | | G | E |
| $X_5$ | P | | |
| $X_6$ | P | G | E |

According to MRV, which variable or variables could the solver assign first?

(d) Assume that Pacman knows that $X_6=G$. List all the solutions of this CSP or none if no solutions exist.

*Note (these notes):* Figure redrawn: corridors $1$ to $6$ lie around Pacman in a ring, and each letter between two neighbouring corridors is the breeze felt there.
:::
