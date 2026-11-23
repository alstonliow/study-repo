<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-2-q24" status="draft"}
1. *Split.* $\mathtt a^i\mathtt b^j\in E$ iff $j<i$, or $i<j<2i$, or $j>2i$. A union of context-free languages is context free, so it is enough to give a grammar for each part.

2. *$j<i$:* $S_1\to\mathtt aS_1\mathtt b\mid\mathtt aA$, $A\to\mathtt aA\mid\varepsilon$. Each step matches one $\mathtt a$ with one $\mathtt b$, and at least one extra $\mathtt a$ is added.

3. *$j>2i$:* $S_3\to\mathtt aS_3\mathtt b\mathtt b\mid C$, $C\to\mathtt bC\mid\mathtt b$. Each $\mathtt a$ is matched with two $\mathtt b$'s, and at least one extra $\mathtt b$ is added. This also covers $i=0$, $j\ge1$.

4. *$i<j<2i$:* write $j=i+m$ with $1\le m\le i-1$. Then each $\mathtt a$ is matched with either one or two $\mathtt b$'s, with both kinds used at least once. Track which kinds have been used with the variables $X_{00},X_{10},X_{01},X_{11}$ (first index: a single $\mathtt b$ used; second: a double $\mathtt{bb}$ used):
$$\begin{aligned}
X_{00}&\to\mathtt aX_{10}\mathtt b\mid\mathtt aX_{01}\mathtt{bb}, &
X_{10}&\to\mathtt aX_{10}\mathtt b\mid\mathtt aX_{11}\mathtt{bb},\\
X_{01}&\to\mathtt aX_{01}\mathtt{bb}\mid\mathtt aX_{11}\mathtt b, &
X_{11}&\to\mathtt aX_{11}\mathtt b\mid\mathtt aX_{11}\mathtt{bb}\mid\varepsilon,
\end{aligned}$$
with start variable $X_{00}$.

5. With $S\to S_1\mid X_{00}\mid S_3$, the grammar generates $E$, so $E$ is context free.
:::

::: {.solution for="prob-sipser3e-2-q27" status="draft"}
(a) The string $w=\mathtt{if\ condition\ then\ if\ condition\ then\ a{:=}1\ else\ a{:=}1}$ has two parse trees. In the first, the root uses $\langle\mathrm{STMT}\rangle\to\langle\mathrm{IF\text-THEN}\rangle$, and the inner statement is an $\langle\mathrm{IF\text-THEN\text-ELSE}\rangle$ (the $\mathtt{else}$ belongs to the second $\mathtt{if}$). In the second, the root uses $\langle\mathrm{IF\text-THEN\text-ELSE}\rangle$, whose first statement is an $\langle\mathrm{IF\text-THEN}\rangle$ (the $\mathtt{else}$ belongs to the first $\mathtt{if}$). Two parse trees give two leftmost derivations, so $G$ is ambiguous.

(b) Attach each $\mathtt{else}$ to the nearest unmatched $\mathtt{then}$. Write $\mathtt{ict}$ for $\mathtt{if\ condition\ then}$:
$$\begin{aligned}
\langle\mathrm{STMT}\rangle&\to\langle\mathrm{M}\rangle\mid\langle\mathrm{U}\rangle\\
\langle\mathrm{M}\rangle&\to\mathtt{ict}\ \langle\mathrm{M}\rangle\ \mathtt{else}\ \langle\mathrm{M}\rangle\mid\mathtt{a{:=}1}\\
\langle\mathrm{U}\rangle&\to\mathtt{ict}\ \langle\mathrm{STMT}\rangle\mid\mathtt{ict}\ \langle\mathrm{M}\rangle\ \mathtt{else}\ \langle\mathrm{U}\rangle
\end{aligned}$$

1. *Same language.* Every string derived here is derived by $G$ (map $\langle\mathrm M\rangle,\langle\mathrm U\rangle$ to $\langle\mathrm{STMT}\rangle$). Conversely, every parse tree of $G$ can be rearranged so that each $\mathtt{else}$ pairs with the nearest unpaired $\mathtt{then}$ before it, without changing the string, and such a tree is a parse tree of the new grammar.

2. *Unambiguous.* In a string of the language, reading left to right, the pairing "each $\mathtt{else}$ with the nearest unpaired $\mathtt{then}$" is forced, like matching brackets. In the new grammar the part between a $\mathtt{then}$ and its $\mathtt{else}$ is a $\langle\mathrm M\rangle$, which has no unpaired $\mathtt{then}$, so every parse tree realizes exactly this pairing. The pairing fixes which rule is used at each $\mathtt{if}$, so there is only one parse tree.
:::

::: {.solution for="prob-sipser3e-2-q26" status="draft"}
1. In Chomsky normal form a derivation of a nonempty string uses only rules $A\to BC$ and $A\to a$ (the rule $S\to\varepsilon$ only derives $\varepsilon$, and $S$ never appears on a right-hand side).

2. Track the number of variables in the current string. It starts at $1$ (just $S$). A rule $A\to BC$ raises it by $1$; a rule $A\to a$ lowers it by $1$ and adds one terminal.

3. At the end the string is $w$: $n$ terminals and $0$ variables. Terminals are only created by $A\to a$, one each, so exactly $n$ such steps are used. If $m$ steps use $A\to BC$, then $1+m-n=0$, so $m=n-1$.

4. Every derivation of $w$ therefore has exactly $n+(n-1)=2n-1$ steps.
:::
