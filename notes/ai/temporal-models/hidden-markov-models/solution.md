<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs188hw-9-q1" status="draft"}
The task is filtering, $\operatorname{arg\,max}_sP(S_t=s\mid e_{0:t})$ (@def-filtering). The evidence $E_t$ depends on $S_t$ only through $A_t$, with $X_t$ unobserved, so the sensor model of the hidden chain $S$ is $P(e_t\mid S_t)=\sum_{x,a}P(e_t\mid x,a)P(x)P(a\mid S_t)$.

1. **Yes; all five tables.** Variable elimination computes $P(S_t\mid e_{0:t})$ exactly (@thm-variable-elimination), and the hidden $A$'s and $X$'s must be summed out with their own tables.
2. **No.** Value iteration solves MDPs; there are no actions or rewards here.
3. **Yes; all five.** Gibbs sampling resamples each hidden variable from its distribution given its Markov blanket (@def-gibbs-sampling), which involves every table: $S$'s transitions and $P(A\mid S)$, and for $A_t$ and $X_t$ the evidence table $P(E\mid X,A)$ and $P(X_t)$.
4. **Yes; all five.** Prior sampling draws every variable, evidence included, from its table; keeping the samples that match the evidence (rejection) estimates the posterior, though very inefficiently for long evidence sequences.
5. **Yes; all five.** Particles over $S_t$ are moved with $P(S_t\mid S_{t-1})$ (and drawn initially from $P(S_0)$), and weighted by $P(e_t\mid S_t)$ above, which needs the other three tables (@def-particle-filtering).
6. **$\sum_{S_{t-1}}P(S_t\mid S_{t-1})B(S_{t-1})$:** the elapse-time step involves only the chain $S$ (@thm-forward-algorithm). $A_t$ belongs to the observation step; $A_{t-1}$ was already accounted for in $B(S_{t-1})$.
7. **$\sum_{x}\sum_{a}P(E_t\mid x,a)P(x)P(a\mid S_t)$**, the likelihood $P(E_t\mid S_t)$ obtained by summing out the unobserved parents $X_t$ and $A_t$.
8. **The first option.** At $t+1$ there is no evidence, so its observation step disappears: elapse twice, then observe $E_{t+2}$. The fourth option invents an observation at $t+1$ and the second sums over an evidence value that is not observed. The third gives the same numbers as the first, but the double sum costs $O(|S|^{3})$ if computed as written, against $O(|S|^{2})$ for two single steps.
9. **Only the third.** Students in the same semester share the parents $A_t$ and $X_t$ (common causes, not observed), so their feedback is dependent. Feedback in different semesters is linked through the chain $S$. The elapse step does not involve evidence at all, so it is unchanged.
10. **$f(x)=x^{60}(1-x)^{40}$.** With independent feedback (given $S_t$) the likelihood of all $100$ observations is the product of the single likelihoods: $x$ for each $+e$ and $1-x$ for each $-e$. (The order of the students is given, so no binomial coefficient appears; it would cancel on normalising anyway.)
:::
