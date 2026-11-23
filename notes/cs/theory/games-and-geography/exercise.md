<!-- Sipser problems assigned in MIT 18.404J (Fall 2020) problem sets, which cite them by number only.
     Statements verbatim from the 3rd edition (owner decision 2026-11-23, meta/SPEC.md §10). -->

<!-- Sipser 8.15; 18.404J PS5 Q3 -->
::: {.problem #prob-sipser3e-8-q15 origin="external" source="sipser3e-8-q15"}
Consider the following two-person version of the language $\mathit{PUZZLE}$ that was described in Problem 7.28. Each player starts with an ordered stack of puzzle cards. The players take turns placing the cards in order in the box and may choose which side faces up. Player I wins if all hole positions are blocked in the final stack, and Player II wins if some hole position remains unblocked. Show that the problem of determining which player has a winning strategy for a given starting configuration of the cards is PSPACE-complete.
:::

<!-- Sipser 8.10; 18.404J PS5 Q4 -->
::: {.problem #prob-sipser3e-8-q10 origin="external" source="sipser3e-8-q10"}
The Japanese game *go-moku* is played by two players, "X" and "O," on a $19\times19$ grid. Players take turns placing markers, and the first player to achieve five of her markers consecutively in a row, column, or diagonal is the winner. Consider this game generalized to an $n\times n$ board. Let
$$\mathit{GM}=\{\langle B\rangle\mid B \text{ is a position in generalized go-moku, where player "X" has a winning strategy}\}.$$
By a *position* we mean a board with markers placed on it, such as may occur in the middle of a play of the game, together with an indication of which player moves next. Show that $\mathit{GM}\in\mathrm{PSPACE}$.
:::
