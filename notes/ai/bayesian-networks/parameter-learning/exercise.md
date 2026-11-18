::: {.problem #prob-cs221hw-6-q3 origin="external" source="cs221hw-6-q3"}
Later in life, you're a data engineer managing a team of human annotators. Your data consists of labels indicating whether a given conversation between an LLM and a human was **good** or **bad**.

But you've run into a problem: your annotators can't seem to perfectly agree on their ratings, no matter how careful you are in your instructions! You vaguely remember something about Bayesian networks from CS221, so you decide to use them to help you assess annotator quality.

For this problem, we'll assume you have the true labels for each conversation. (In the real world, this will not be the case!) Also assume that each annotator's label depends only on the true label of the conversation, and that annotators make mistakes independently of each other: once you know the true label, how one annotator labeled the conversation tells you nothing about how another one did.

(a) Let's consider a single conversation and three annotators who each label it. List the edges in the Bayesian network for this scenario, using the random variables $Y$, the true label of the conversation, and $A_0$, $A_1$, and $A_2$, the labels that the three annotators give it. Each variable takes the values $\text{good}$ and $\text{bad}$.

*Expected:* A list of edges in the Bayesian network, in the format of $\text{variable1} \rightarrow \text{variable2}$.

(b) Fill out the following table with the local conditional distribution $p(A_0 = a \mid Y = y)$ of a perfect annotator, who always gives the true label.

*Expected:* A completed table with the local conditional distribution.

  $y$              $p(A_0 = \text{good} \mid Y = y)$   $p(A_0 = \text{bad} \mid Y = y)$
  ------------------ --------------------------------------- --------------------------------------
  $\text{good}$                                           
  $\text{bad}$

(c) Fill out the following table with the local conditional distribution $p(A_0 = a \mid Y = y)$ of an annotator who guesses uniformly at random.

*Expected:* A completed table with the local conditional distribution.

  $y$              $p(A_0 = \text{good} \mid Y = y)$   $p(A_0 = \text{bad} \mid Y = y)$
  ------------------ --------------------------------------- --------------------------------------
  $\text{good}$                                           
  $\text{bad}$

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::
