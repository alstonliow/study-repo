---
title: "Digit DP"
sources: []
requires: [cs/algorithm-design/subproblem-design]
status: draft
---

<!-- Added 2026-11-26 for the CSES problem Counting Numbers, in our own wording. TODO: add a source. -->

How many integers in $[a,b]$ have some property of their decimal digits (no two equal adjacent digits, digit sum divisible by $7$, ...)? When the range is huge ($b\sim10^{18}$), count digit by digit.

::: {#def-digit-dp .definition name="Digit dynamic program"}

For an upper bound $N=d_1d_2\dots d_L$ (decimal digits) count the integers $0\le x\le N$ with the property by choosing the digits of $x$ from the left, padded to $L$ digits with leading zeros. A state is $(i,\text{tight},\text{rest})$:

- $i$ is the number of digits already chosen;
- $\text{tight}$ says whether the chosen digits equal $d_1\dots d_i$, so the next digit is at most $d_{i+1}$ (otherwise any digit $0..9$ is allowed);
- $\text{rest}$ is whatever the property needs to remember (the previous digit, the digit sum modulo $7$, whether a nonzero digit has appeared yet).

Let $F(i,\text{tight},\text{rest})$ be the number of ways to choose the remaining digits.

:::

::: {#thm-digit-dp .theorem name="Digit DP"}

The recurrence $F(L,\cdot,\text{rest})=[\text{rest is accepted}]$ and

$$
F(i,t,r)=\sum_{c=0}^{u}F\bigl(i+1,\; t\wedge(c=u),\; \delta(r,c)\bigr),\qquad u=\begin{cases}d_{i+1}&t\\9&\text{otherwise,}\end{cases}
$$

where $\delta$ updates the memory with the chosen digit $c$ (and rejects invalid choices, contributing $0$), gives the number $F(0,\text{true},r_0)$ of integers in $[0,N]$ with the property. The number of states is $L\cdot 2\cdot|\text{rest}|$, each with $10$ transitions. The count for $[a,b]$ is $F_b-F_{a-1}$.

:::

::: {.proof}

1. *Bijection.* Padded strings of length $L$ correspond to the integers in $[0,10^L-1]$. A string is $\le N$ iff at the first position where it differs from $N$ its digit is smaller, which is exactly the case where the tight flag is dropped; as long as the flag holds the next digit is at most $d_{i+1}$.

2. *Correct state.* The future choices and the final verdict depend on the prefix only through $(i,t,r)$, so $F$ is well defined and the recurrence sums over the possible next digits.

3. *Leading zeros.* If the property must ignore leading zeros (for example "no two equal adjacent digits" would otherwise reject $00$), keep a flag in $r$ saying whether a nonzero digit has been placed and do not update the memory while it is false.

4. *Difference.* The numbers in $[a,b]$ are those in $[0,b]$ but not in $[0,a-1]$.

:::

::: {#exm-digit-dp-1 .example name="No equal adjacent digits up to 25"}

Count the $0\le x\le25$ with no two equal adjacent digits. Of the $26$ numbers exactly $11$ and $22$ are bad, so the answer is $24$. The DP finds this without listing: the first digit $0$ or $1$ drops the tight flag and allows any second digit except the first digit itself, and the first digit $2$ keeps the flag, so the second digit is at most $5$ and not $2$.

:::

::: {#fig-digit-dp-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (a) at (0,0) {tight, $d=2$};
\node[box] (b) at (3,0.8) {$c=0,1$: free};
\node[hl box] (c) at (3,-0.8) {$c=2$: tight};
\draw[->] (a) -- (b); \draw[->] (a) -- (c);
\node[box] (d) at (6.4,-0.8) {$c\le5$};
\draw[->] (c) -- (d);
\end{tikzpicture}
\end{center}
```

@exm-digit-dp-1: for $N=25$ the first digit $0$ or $1$ drops the tight flag (all second digits are allowed), the first digit $2$ keeps it (second digit at most $5$).

:::
