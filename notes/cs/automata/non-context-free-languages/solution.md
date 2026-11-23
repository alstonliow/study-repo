<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-2-q18" status="draft"}
(a)

1. Let $P=(Q_P,\Sigma,\Gamma,\delta_P,q_P,F_P)$ be a PDA for $C$ and $D=(Q_D,\Sigma,\delta_D,q_D,F_D)$ a DFA for $R$.

2. Build a PDA $P'$ with states $Q_P\times Q_D$, start state $(q_P,q_D)$ and accept states $F_P\times F_D$. When $P$ reads an input symbol $a$, $P'$ makes the same move in the first component and moves the second to $\delta_D(\cdot,a)$. When $P$ makes an $\varepsilon$-move (on the input), $P'$ makes it and leaves the second component unchanged.

3. A branch of $P'$ on $w$ is a branch of $P$ on $w$ paired with the run of $D$ on $w$. So $P'$ accepts $w$ iff $P$ accepts $w$ and $D$ accepts $w$, and $C\cap R$ is context free.

(b) Suppose $A$ were a CFL. By (a), $A\cap\mathtt a^*\mathtt b^*\mathtt c^*=\{\mathtt a^n\mathtt b^n\mathtt c^n\mid n\ge0\}$ would be context free, but it is not (pumping lemma for CFLs). So $A$ is not a CFL.
:::

::: {.solution for="prob-sipser3e-2-q32" status="draft"}
1. Suppose $C$ is context free, with pumping length $p$. Take $s=1^p3^p2^p4^p\in C$.

2. Write $s=uvxyz$ with $|vxy|\le p$ and $|vy|\ge1$. Because $|vxy|\le p$, the part $vxy$ meets at most two neighbouring blocks: $1$s and $3$s, or $3$s and $2$s, or $2$s and $4$s (or only one block).

3. Consider $uv^0xy^0z=uxz$, which removes the symbols of $vy$. The two pairs that must balance are $(1,2)$ and $(3,4)$, and in the block order $1,3,2,4$ no two partners are neighbours. So $vy$ contains some symbol, say $1$, whose partner ($2$) it does not contain.

4. Removing $vy$ then changes the count of that symbol but not of its partner, so the counts of $1$s and $2$s (or of $3$s and $4$s) differ in $uxz$. Hence $uxz\notin C$, contradicting the pumping lemma. So $C$ is not context free.
:::
