<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs188hw-2-q1" status="draft"}
We treat clue 1 as "all different" (a binary $\ne$ between every two people), clues 2, 5, 6, 8, 9 as unary constraints, and clues 3, 4, 7 as binary constraints between every two people: for instance, under clue 3 two people of the same grade may not hold E and F. Arc consistency means AC-3 (@def-ac3) on these binary constraints. Juniors are Angela and Regina. The answers were checked by running AC-3 and backtracking in Python.

1. **Jonathan, Ryan, Saathvik.** The alphabetical assignment is Angela A, Danial B, Jonathan C, Regina D, Ryan E, Saathvik F, Yanlai G. Jonathan (ends in a consonant) has C, violating clue 5; Ryan (E) and Saathvik (F) are both seniors, violating clue 3. Clues 2 and 4 hold (F and G both go to seniors).
2. **2.** One swap cannot fix both violations (checked over all $21$ swaps; a single swap that moves C away from Jonathan leaves E and F with two seniors or creates a new violation). Two swaps suffice: Angela$\leftrightarrow$Jonathan (Angela C, Jonathan A) and Regina$\leftrightarrow$Ryan (Regina E, Ryan D); now E goes to a junior and F to a senior, F and G both to seniors, and no forbidden letter is held.
3. **Regina.** Min-conflicts chooses the partner leaving the fewest violations. Swapping with Regina gives Regina E (junior) and Ryan D, which fixes clue 3 and leaves only Jonathan's violation ($1$ conflict); every other partner leaves $2$ (for example swapping with Saathvik just exchanges E and F between two seniors).
4. **No.** After the unary constraints Regina has $\{E,G\}$ (clue 8 with clue 2), Ryan $\{D,E,F,G\}$, Danial $\{A,D,E,F,G\}$; arc consistency removes nothing more that matters, and no domain is a single value.
5. **4:** $\{D,E,F,G\}$. Clue 2 removes A, clue 5 C, clue 6 B. Arc consistency keeps D: for each other person on their own, there is a value compatible with Ryan $=D$. (Taking all people together, Ryan cannot get D, since the Backgammon would then need another four-letter name; but this follows only from all seven variables at once, through "all different", which arc consistency does not see.)
6. **Regina, with 2 values** $\{E,G\}$; every other domain has at least $4$.
7. **5.** With Regina $=E$ (alphabetically first), arc consistency removes E from everyone else and, since Regina is a junior, F from Angela (clue 3: F must go to the other grade). Angela keeps $\{A,B,C,D,G\}$. (Again, a reasoning over all variables would also remove G, because G must go with F to a senior.)
8. **Yes.** Clue 9 removes E from the juniors, so Regina $=G$.
9. **Angela F, Danial A, Jonathan B, Regina G, Ryan E, Saathvik D, Yanlai C.** Backtracking with MRV, alphabetical ties and arc consistency after each assignment:
   1. Regina $=G$ (one value). Arc consistency leaves Ryan $\{D,E\}$, Danial $\{A,D,E\}$, Jonathan, Saathvik $\{A,B,D,E\}$, Angela $\{A,B,C,D,F\}$, Yanlai $\{A,B,C,D,E\}$; seniors lose F, because F must go with G to a junior.
   2. Ryan $=D$ (two values, first alphabetically). Then Backgammon would need a four-letter name, so B disappears everywhere; Danial is left with $\{A,E\}$, and both of its values empty another domain. Backtrack.
   3. Ryan $=E$. Danial $\{A,D\}$ is now the MRV variable: Danial $=A$, after which Angela $=\{F\}$ and Yanlai $=\{C\}$ (only they may hold C), Jonathan and Saathvik $\{B,D\}$.
   4. Angela $=F$, Yanlai $=C$, Jonathan $=B$ (both have two values; alphabetical), Saathvik $=D$. Check: E (Ryan, senior) and F (Angela, junior) differ in grade; F and G both go to juniors; B and D go to Jonathan and Saathvik, both eight letters; Regina's G is in her name; nobody holds a forbidden letter.

   The CSP has one other solution, with Jonathan and Saathvik exchanging B and D; the search finds this one first.
10. **Saathvik.** The order of assignment is Regina, Ryan, Danial, Angela, Yanlai, Jonathan, Saathvik.
:::

::: {.solution for="prob-cs188d-2-q1" status="draft"}
(a) Indices are cyclic ($X_7=X_1$). A weak breeze between $i$ and $i+1$ means neither corridor is a pit and at least one is an exit; a strong breeze means at least one is a pit. With the measurements $S$ between $1,2$; $W$ between $2,3$ and $3,4$; $S$ between $4,5$, $5,6$ and $6,1$:

- unary: $X_2\ne P$, $X_3\ne P$, $X_4\ne P$;
- binary: $X_1=P\lor X_2=P$; $X_2=E\lor X_3=E$; $X_3=E\lor X_4=E$; $X_4=P\lor X_5=P$; $X_5=P\lor X_6=P$; $X_6=P\lor X_1=P$;
- no neighbouring exits: $\lnot(X_i=E\land X_{i+1}=E)$ for $i=1,\dots,6$.

(b) Unary constraints leave $X_2,X_3,X_4\in\{G,E\}$. Forward checking from $X_1=E$ (@def-forward-checking) removes from $X_2$ every value not allowed with $X_1=E$: the strong breeze between $1$ and $2$ forces $X_2=P$, which is already gone, so **$X_2$'s domain becomes empty** and this assignment fails. On the other side, $X_6$ must be $P$ (strong breeze between $6$ and $1$, and no two exits). The table is $X_1\{E\}$, $X_2\{\}$, $X_3\{G,E\}$, $X_4\{G,E\}$, $X_5\{P,G,E\}$, $X_6\{P\}$.

(c) **$X_1$ or $X_5$**, each with one value left (@def-mrv-lcv).

(d) With $X_6=G$, the strong breezes next to corridor $6$ force $X_5=P$ and $X_1=P$; these also satisfy the breezes at $1,2$ and $4,5$. The weak breezes need an exit among $X_2,X_3$ and among $X_3,X_4$, all in $\{G,E\}$, with no two neighbouring exits. Either $X_3=E$, and then $X_2=X_4=G$, or $X_3=G$, and then $X_2=X_4=E$ (corridors $2$ and $4$ are not neighbours). The solutions are
$$
(X_1,\dots,X_6)=(P,G,E,G,P,G)\quad\text{and}\quad(P,E,G,E,P,G).
$$
:::
