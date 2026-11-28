---
title: "Utilities and Rational Preferences"
sources: [cs188-7]
requires: [math/probability/random-variables/expectation-and-variance]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 7 (utilities, preferences, lotteries, rationality axioms, the MEU principle, human utilities, money, insurance), in our own wording; the representation theorem is proved in steps; numbers checked by a short Python computation. -->

Expectimax (@def-game-recurrences) averages utilities, so their actual values matter, not only their order: with outcomes worth $0$, $40$ and $50$, the lottery "$0$ or $50$ with equal chance" is worse than a sure $40$, but after the order-preserving change to $0$, $40$, $900$ it is better. This note asks where such numbers come from, and shows that they exist whenever preferences obey a few consistency rules.

::: {#def-lottery-preference .definition name="Lottery, preference"}

Let $\mathcal S$ be a finite set of *outcomes* (prizes). A *lottery* $L=[p_1,S_1;\ \dots;\ p_n,S_n]$ gives outcome $S_i$ with probability $p_i$; an outcome $S$ is identified with the lottery $[1,S]$, and a lottery whose prizes are themselves lotteries is identified with the lottery over outcomes it induces (so only the final probabilities of the outcomes matter). An agent's *preferences* are a relation on lotteries: $A\succ B$ ($A$ is preferred to $B$), $A\sim B$ (indifference), and $A\succeq B$ meaning $A\succ B$ or $A\sim B$.

:::

::: {#def-rational-preferences .definition name="Rational preferences"}

Preferences are *rational* if for all lotteries $A,B,C$:

1. (*orderability*) exactly one of $A\succ B$, $B\succ A$, $A\sim B$ holds;
2. (*transitivity*) $A\succeq B$ and $B\succeq C$ imply $A\succeq C$, and if one of the two is strict so is the conclusion;
3. (*continuity*) if $A\succ B\succ C$, there is $p\in(0,1)$ with $[p,A;\,1-p,C]\sim B$;
4. (*substitutability*) if $A\sim B$, then $[p,A;\,1-p,C]\sim[p,B;\,1-p,C]$;
5. (*monotonicity*) if $A\succ B$, then $[p,A;\,1-p,B]\succeq[q,A;\,1-q,B]$ if and only if $p\ge q$.

:::

Violating them is costly. An agent with the intransitive preferences $A\succ B\succ C\succ A$ would pay a small amount to trade $C$ for $B$, then $B$ for $A$, then $A$ for $C$, and end where it began, poorer; repeating the cycle drains it of all its money.

::: {#thm-meu-representation .theorem name="Rational preferences have a utility function"}

If preferences on lotteries over a finite set of outcomes are rational, there is a function $U$ on outcomes such that, writing
$$
U\bigl([p_1,S_1;\ \dots;\ p_n,S_n]\bigr)=\sum_{i=1}^{n}p_iU(S_i),
$$
for all lotteries $A,B$ we have $A\succeq B$ if and only if $U(A)\ge U(B)$.

:::

::: {.proof}

1. By orderability and transitivity the outcomes can be sorted by preference; let $b$ be a most preferred and $w$ a least preferred one. If $b\sim w$, all outcomes are equally good, and so are all lotteries (step 4 below with $U$ constant); take $U=0$. Assume $b\succ w$ and write $L_p=[p,b;\,1-p,w]$.
2. By monotonicity, $L_p\succeq L_q$ if and only if $p\ge q$; so $L_p\sim L_q$ only for $p=q$.
3. For each outcome $S$ there is a unique $u_S\in[0,1]$ with $S\sim L_{u_S}$: take $u_S=1$ if $S\sim b$, $u_S=0$ if $S\sim w$, and otherwise $b\succ S\succ w$ and continuity gives $u_S$. Uniqueness follows from step 2 and transitivity. Set $U(S)=u_S$.
4. Let $A=[p_1,S_1;\dots;p_n,S_n]$. Replacing $S_1$ by $L_{u_{S_1}}$ does not change the lottery's standing, by substitutability (the rest of $A$ forms the lottery $C$); repeat for each $i$, using transitivity. The result is a compound lottery that gives $b$ with probability $\sum_ip_iu_{S_i}=U(A)$ and $w$ otherwise, so $A\sim L_{U(A)}$.
5. For lotteries $A,B$, by step 4 and transitivity $A\succeq B$ if and only if $L_{U(A)}\succeq L_{U(B)}$, which by step 2 holds if and only if $U(A)\ge U(B)$.

:::

So a rational agent behaves as if it maximised expected utility, even if it never computes a number: this is the *principle of maximum expected utility* (MEU), which expectimax and MDPs (@def-mdp) put into practice. The utility function is not unique: $U'=aU+c$ with $a>0$ represents the same preferences, since expected values transform the same way, and no other transformation does in general. For deterministic choices (no lotteries) any increasing transformation would do, but that is not enough once risk is involved.

::: {#def-certainty-equivalent .definition name="Utility of money, risk attitude"}

For lotteries over amounts of money, the *expected monetary value* of $L$ is $\mathrm{EMV}(L)=\sum_ip_ix_i$, and its *certainty equivalent* is the sure amount $x$ with $U(x)=U(L)$. The agent is *risk-averse* if $U(L)<U(\mathrm{EMV}(L))$ for every lottery with more than one prize (equivalently, $U$ is strictly concave), *risk-neutral* if $U$ is linear and *risk-seeking* if $U$ is strictly convex.

:::

A risk-averse agent values a lottery at less than its expected value; the difference $\mathrm{EMV}(L)-x$ is the most it would pay to be rid of the risk, which is what makes insurance possible.

::: {#exm-insurance .example name="Insurance"}

An agent with $U(x)=\sqrt{x}$ faces $L=[0.5,\$1000;\ 0.5,\$0]$. Then $\mathrm{EMV}(L)=500$ but $U(L)=0.5\sqrt{1000}\approx15.81$, whose certainty equivalent is $15.81^{2}=250$ dollars. The agent is indifferent between the gamble and a sure $\$250$, so it would sell the gamble for any amount above $\$250$. A risk-neutral insurer who buys it for, say, $\$400$ expects to gain $\$100$, and the agent is better off too: the $\$250$ gap between expected value and certainty equivalent is shared between them.

:::

::: {#rmk-human-utilities .remark name="Humans are not quite rational"}

Utilities of people can be measured by comparing an outcome with *standard lotteries* $L_p=[p,\text{best};1-p,\text{worst}]$, as in step 3 of the proof; units such as micromorts (a one-in-a-million chance of death) arise this way. Measured preferences break the axioms in systematic ways. In the Allais paradox most people prefer a sure $\$3000$ to an $80\%$ chance of $\$4000$, yet prefer a $20\%$ chance of $\$4000$ to a $25\%$ chance of $\$3000$; the second pair is the first with all probabilities multiplied by $\tfrac14$, and for any $U$ with $U(0)=0$ the first preference says $U(3000)>0.8\,U(4000)$ while the second says $0.2\,U(4000)>0.25\,U(3000)$, a contradiction. Such findings matter for modelling people, not for designing agents, which can be made to follow the axioms.

:::
