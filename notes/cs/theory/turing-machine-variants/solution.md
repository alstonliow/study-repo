<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-3-q12" status="draft"}
1. *Left reset is no stronger.* An ordinary TM simulates RESET by marking the leftmost cell at the start and moving left until it reaches the mark. So every language recognized by a TM with left reset is Turing-recognizable.

2. *Left reset is no weaker.* A TM with left reset $R$ simulates an ordinary TM $M$. Right moves are copied directly. The tape alphabet of $R$ adds two marked copies of each symbol: a dot (the cell $M$'s head is on) and a hat (a candidate cell).

3. *Simulating a left move from cell $m$.* After writing, $R$ dots the current cell and resets. If cell 1 is dotted, then $m=1$; an ordinary TM stays put, so $R$ removes the dot and is done. Otherwise $R$ hats cell 1.

4. *Search loop.* From the hatted cell, $R$ moves right once.
   - If this cell is dotted, then the hatted cell is $m-1$: $R$ removes the dot, resets, scans right to the hat, removes it, and stays there.
   - Otherwise $R$ resets, scans right to the hat, removes it, moves right one cell, hats that cell and repeats.

   Every step moves right or resets, so $R$ never needs a left move.

5. The loop ends after at most $m-1$ rounds with the head on cell $m-1$ and the tape unchanged. So $R$ follows $M$'s computation and accepts the same strings, and the two models recognize the same class.
:::

::: {.solution for="prob-sipser3e-3-q18" status="draft"}
1. *($\Rightarrow$)* Let $M$ decide $A$. The enumerator runs $M$ on $s_1,s_2,s_3,\dots$, the strings of $\Sigma^*$ in standard order, and prints $s_i$ when $M$ accepts it. Each run halts, so every string of $A$ is printed, and in standard order.

2. *($\Leftarrow$), $A$ finite.* Every finite language is decidable: a TM can store the list of its strings.

3. *($\Leftarrow$), $A$ infinite.* Let $E$ enumerate $A$ in standard order. On input $w$, run $E$ and watch what it prints. If it prints $w$, accept. If it prints a string that comes after $w$ in standard order, reject: by the order, $w$ will never be printed.

4. Since $A$ is infinite, $E$ eventually prints a string after $w$, so this machine always halts. It decides $A$.
:::
