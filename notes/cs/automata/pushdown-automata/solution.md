<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-2-q22" status="draft"}
A PDA $P$ for $C$ chooses nondeterministically between two checks; $x\ne y$ iff $|x|\ne|y|$ or the strings differ at some position $i\le\min(|x|,|y|)$.

1. *Different lengths.* Push $\$$, then push one $X$ for each symbol of $x$. After $\#$, pop one $X$ for each symbol of $y$. If $y$ has a symbol left when $\$$ is on top ($|y|>|x|$), go to an accept state that reads the rest of $y$. If the input ends while an $X$ is still on the stack ($|x|>|y|$), accept: for this, an $\varepsilon$-move that pops an $X$ leads to an accept state.

2. *Different symbols at the same position.* Push $\$$. While reading $x$, push an $X$ for each symbol, and at some point guess that the next symbol is position $i$: read it, remember it as $c\in\{0,1\}$ in the state, and stop pushing. Read the rest of $x$ without using the stack. After $\#$, pop one $X$ per symbol of $y$; when $\$$ is on top, the next symbol $d$ of $y$ is position $i$. If $d\ne c$, go to an accept state that reads the rest of the input.

3. *Correctness.* A branch accepts only when it has found a length difference or a position $i$ with $x_i\ne y_i$, so it accepts only strings in $C$. Conversely, if $x\ne y$, one of the two checks finds such a witness on some branch.

4. So $C$ is recognized by a PDA and is context free.
:::
