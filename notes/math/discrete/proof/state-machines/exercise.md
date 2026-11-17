::: {.problem #prob-mit6042f10-2-q3 origin="external" source="mit6042f10-2-q3"}
The following problem is fairly tough until you hear a certain one-word clue. The solution is elegant but is slightly tricky, so don't hesitate to ask for hints!

During 6.042, the students are sitting in an $n \times n$ grid. A sudden outbreak of beaver flu (a rare variant of bird flu that lasts forever; symptoms include yearning for problem sets and craving for ice cream study sessions) causes some students to get infected. Here is an example where $n = 6$ and infected students are marked $\times$.

```
×       ×
  ×
    × ×
    ×
      ×   ×
```

Now the infection begins to spread every minute (in discrete time-steps). Two students are considered adjacent if they share an edge (i.e., front, back, left or right, but NOT diagonal); thus, each student is adjacent to 2, 3 or 4 others. A student is infected in the next time step if either

- the student was previously infected (since beaver flu lasts forever), or
- the student is adjacent to at least two already-infected students.

In the example, the infection spreads as shown below.

In this example, over the next few time-steps, all the students in class become infected.

**Theorem.** If fewer than $n$ students in class are initially infected, the whole class will never be completely infected.

Prove this theorem.

Hint: When one wants to understand how a system such as the above "evolves" over time, it is usually a good strategy to (1) identify an appropriate property of the system at the initial stage, and (2) prove, by induction on the number of time-steps, that the property is preserved at every time-step. So look for a property (of the set of infected students) that remains invariant as time proceeds.

If you are stuck, ask your recitation instructor for the one-word clue and even more hints!

*Note (these notes):* The pictures of the spreading infection are not reproduced; the starting picture is redrawn in text.
:::

::: {.problem #prob-mit6042f10-2-q6 origin="external" source="mit6042f10-2-q6"}
In the 15-puzzle, there are 15 lettered tiles and a blank square arranged in a $4 \times 4$ grid. Any lettered tile adjacent to the blank square can be slid into the blank. For example, a sequence of two moves is illustrated below:

```
A B C D      A B C D      A B C D
E F G H      E F G H      E F G H
I J K L  ->  I J K L  ->  I J   L
M O N        M O   N      M O K N
```

In the leftmost configuration shown above, the O and N tiles are out of order. Using only legal moves, is it possible to swap the N and the O, while leaving all the other tiles in their original position and the blank in the bottom right corner? In this problem, you will prove the answer is "no".

**Theorem.** No sequence of moves transforms the board below on the left into the board below on the right.

```
A B C D      A B C D
E F G H      E F G H
I J K L      I J K L
M O N        M N O
```

(a) We define the "order" of the tiles in a board to be the sequence of tiles on the board reading from the top row to the bottom row and from left to right within a row. For example, in the right board depicted in the above theorem, the order of the tiles is A, B, C, D, E, etc.

Can a row move change the order of the tiles? Prove your answer.

(b) How many pairs of tiles will have their relative order changed by a column move? More formally, for how many pairs of letters $L_1$ and $L_2$ will $L_1$ appear earlier in the order of the tiles than $L_2$ before the column move and later in the order after the column move? Prove your answer correct.

(c) We define an *inversion* to be a pair of letters $L_1$ and $L_2$ for which $L_1$ precedes $L_2$ in the alphabet, but $L_1$ appears after $L_2$ in the order of the tiles. For example, consider the following configuration:

```
A B C E
D H G F
I J K L
M N O
```

There are exactly four inversions in the above configuration: E and D, H and G, H and F, and G and F.

What effect does a row move have on the parity of the number of inversions? Prove your answer.

(d) What effect does a column move have on the parity of the number of inversions? Prove your answer.

(e) The previous problem part implies that we must make an odd number of column moves in order to exchange just one pair of tiles (N and O, say). But this is problematic, because each column move also knocks the blank square up or down one row. So after an odd number of column moves, the blank can not possibly be back in the last row, where it belongs! Now we can bundle up all these observations and state an invariant, a property of the puzzle that never changes, no matter how you slide the tiles around.

**Lemma.** In every configuration reachable from the position shown below, the parity of the number of inversions is different from the parity of the row containing the blank square.

```
row 1   A B C D
row 2   E F G H
row 3   I J K L
row 4   M O N
```

Prove this lemma.

(f) Prove the theorem that we originally set out to prove.

*Note (these notes):* In (b), a column move slides a tile vertically into the blank; the blank then moves to the tile's old square.
:::

::: {.problem #prob-mit6042f10-2-q7 origin="external" source="mit6042f10-2-q7"}
There are two types of creature on planet Char, Z-lings and B-lings. Furthermore, every creature belongs to a particular generation. The creatures in each generation reproduce according to certain rules and then die off. The subsequent generation consists entirely of their offspring.

The creatures of Char pair with a mate in order to reproduce. First, as many Z-B pairs as possible are formed. The remaining creatures form Z-Z pairs or B-B pairs, depending on whether there is an excess of Z-lings or of B-lings. If there are an odd number of creatures, then one in the majority species dies without reproducing. The number and type of offspring is determined by the types of the parents

- If both parents are Z-lings, then they have three Z-ling offspring.
- If both parents are B-lings, then they have two B-ling offspring and one Z-ling offspring.
- If there is one parent of each type, then they have one offspring of each type.

There are 200 Z-lings and 800 B-lings in the first generation. Use induction to prove that the number of Z-lings will always be at most twice the number of B-lings.

Hint: You may want to use a stronger hypothesis for the induction.
:::
