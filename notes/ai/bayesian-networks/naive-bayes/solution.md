<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs188hw-9-q2" status="draft"}
The model is $a\to s_p$, $a\to s_g$ (@def-naive-bayes); estimates are counts over the six examples (three per action).

1. $P(s_p=C\mid\text{left})=\frac13$ (the left examples have $s_p=B,C,A$), $P(s_p=A\mid\text{right})=\frac03=0$ (the right examples have $s_p=C,B,C$), and $P(\text{left})=\frac36=\frac12$.
2. **Left, then Right.** For $s_p=A$, $s_g=C$: left scores $\frac12\cdot\frac13\cdot\frac13=\frac1{18}$ ($s_g=C$ once among left), right scores $\frac12\cdot0\cdot\frac13=0$. For $s_p=C$, $s_g=B$: left scores $\frac12\cdot\frac13\cdot\frac13=\frac1{18}$, right scores $\frac12\cdot\frac23\cdot\frac13=\frac19$.
3. **The second, fourth and fifth.** The smoothing strength is a hyperparameter, tuned on validation data (@sec-ai-machine-learning-generalization): tuned on training data it would always prefer $k=0$, which fits the training data best, and tuned on the test set it would make the test accuracy an overestimate. With $k=0$, zero counts (like $P(s_p=A\mid\text{right})=0$ above) rule actions out on the strength of six examples: overfitting. As $k\to\infty$ every smoothed conditional tends to the uniform distribution, the same for both actions, so the posterior tends to the prior, here $\frac12$ for each action.
:::
