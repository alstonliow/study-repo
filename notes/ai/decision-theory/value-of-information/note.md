---
title: "Value of Information"
sources: [cs188-17]
requires: [ai/decision-theory/decision-networks]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 17 (value of perfect information, its properties, imperfect information, POMDPs), in our own wording; proofs written out in steps; the numbers continue our umbrella example and were checked by an exact computation in Python. -->

Information costs time or money: a test, a survey, a look out of the window. Decision networks (@def-decision-network) tell us how much it is worth, before we know what it will say.

::: {#def-vpi .definition name="Value of perfect information"}

Let $e$ be the current evidence and $E'$ a chance variable not yet observed whose value will be learnt before acting. The *value of perfect information* about $E'$ is
$$
\mathrm{VPI}(E'\mid e)=\Bigl(\sum_{e'}P(e'\mid e)\,\mathrm{MEU}(e,e')\Bigr)-\mathrm{MEU}(e),
$$
the expected maximum expected utility after observing $E'$, minus the maximum expected utility now. For several variables $E_1,\dots,E_k$ observed together, $e'$ ranges over their joint values.

:::

The sum is an average over the possible observations of the best we can do after each; we do not know which one we will see, which is why it is an expectation.

::: {#exm-vpi-umbrella .example name="What a forecast is worth"}

In @exm-umbrella-decision, $\mathrm{MEU}(\emptyset)=70$. Observing the forecast gives
$$
P(\text{bad})\,\mathrm{MEU}(\text{bad})+P(\text{good})\,\mathrm{MEU}(\text{good})=0.31\cdot\tfrac{18.2}{0.31}+0.69\cdot\tfrac{63}{0.69}=81.2,
$$
so $\mathrm{VPI}(F)=11.2$. Observing the weather itself gives $0.3\cdot70+0.7\cdot100=91$ (take the umbrella exactly when it rains), so $\mathrm{VPI}(W)=21$. The forecast is worth less because it is sometimes wrong; and once $W$ is known, $F$ is worthless, $\mathrm{VPI}(F\mid W)=0$, since $F$ is independent of everything else given $W$.

:::

::: {#thm-vpi-properties .theorem name="Properties of VPI"}

Suppose observing variables does not depend on the action taken. Then:

1. (*non-negative*) $\mathrm{VPI}(E'\mid e)\ge0$ for every $E'$ and $e$;
2. (*not additive*) in general $\mathrm{VPI}(E_j,E_k\mid e)\ne\mathrm{VPI}(E_j\mid e)+\mathrm{VPI}(E_k\mid e)$;
3. (*order-independent*) $\displaystyle\mathrm{VPI}(E_j,E_k\mid e)=\mathrm{VPI}(E_j\mid e)+\sum_{e_j}P(e_j\mid e)\,\mathrm{VPI}(E_k\mid e,e_j)$, and the same with $j$ and $k$ exchanged.

:::

::: {.proof}

1. Since observing $E'$ is unaffected by the action, $P(x\mid e,a)=\sum_{e'}P(e'\mid e)P(x\mid e,e',a)$, so $\mathrm{EU}(a\mid e)=\sum_{e'}P(e'\mid e)\,\mathrm{EU}(a\mid e,e')$.
2. For every action $a$, $\mathrm{EU}(a\mid e,e')\le\mathrm{MEU}(e,e')$. Averaging with weights $P(e'\mid e)$ and using step 1, $\mathrm{EU}(a\mid e)\le\sum_{e'}P(e'\mid e)\mathrm{MEU}(e,e')$. Taking the maximum over $a$ on the left gives part 1. In words: one may always ignore the observation and act as before, so information cannot hurt in expectation.
3. Part 2 is shown by @exm-vpi-umbrella: observing $F$ and $W$ together is worth exactly $\mathrm{VPI}(W)=21$ (after seeing $W$ the forecast changes nothing), while $\mathrm{VPI}(F)+\mathrm{VPI}(W)=32.2$.
4. Part 3. Write $M_0=\mathrm{MEU}(e)$, $M_j=\sum_{e_j}P(e_j\mid e)\mathrm{MEU}(e,e_j)$ and $M_{jk}=\sum_{e_j,e_k}P(e_j,e_k\mid e)\mathrm{MEU}(e,e_j,e_k)$. Then $\mathrm{VPI}(E_j,E_k\mid e)=M_{jk}-M_0=(M_j-M_0)+(M_{jk}-M_j)$. The first bracket is $\mathrm{VPI}(E_j\mid e)$. Using $P(e_j,e_k\mid e)=P(e_j\mid e)P(e_k\mid e,e_j)$, the second is
$$
\sum_{e_j}P(e_j\mid e)\Bigl(\sum_{e_k}P(e_k\mid e,e_j)\mathrm{MEU}(e,e_j,e_k)-\mathrm{MEU}(e,e_j)\Bigr)=\sum_{e_j}P(e_j\mid e)\,\mathrm{VPI}(E_k\mid e,e_j).
$$
The left side $M_{jk}-M_0$ is symmetric in $j,k$, so the same holds with them exchanged.

:::

Non-negativity holds for expected value only: a particular observation can lower the maximum expected utility (a bad forecast lowers it from $70$ to $58.7$). It also assumes the agent uses the information correctly; for people, knowing something can hurt (it may be used against them, or cause worry). Information is worth something only if it can change the decision: if every outcome of $E'$ leaves the same action optimal, $\mathrm{VPI}(E'\mid e)=0$.

::: {#rmk-imperfect-information-pomdp .remark name="Imperfect information and POMDPs"}

Noisy observations need no new definition: a noisy sensor is a separate chance variable, a child of the quantity it measures, as the forecast $F$ is of $W$, and its VPI is computed as above. An agent should acquire information when its VPI exceeds its cost, choosing greedily the most valuable observation at each step (a myopic but common strategy, since computing the value of a sequence of observations is much harder). When an agent acts over time without seeing the state, it faces a *partially observable MDP* (POMDP): its state of knowledge is a *belief state*, a distribution over states, updated by filtering (@sec-ai-temporal-models-hidden-markov-models); a POMDP is an MDP over belief states, and its optimal policy automatically weighs the value of information-gathering actions.

:::
