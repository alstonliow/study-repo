---
title: "Language Models: Pretraining, Fine-Tuning and RLHF"
sources: [cs188-24]
requires: [ai/deep-learning/attention-and-transformers]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 24 (autoregressive models, large language models, self-supervised pre-training, transfer, fine-tuning, instruction tuning, reinforcement learning from human feedback), in our own wording; the bigram example is our own. The lecture's closing discussion of concept spaces and multimodal models is not covered. -->

A language model assigns probabilities to sequences of tokens. Built from a transformer (@def-transformer-block) and trained on a large share of the text on the web, it becomes a general-purpose system; three training stages turn it from a predictor of text into an assistant.

::: {#def-autoregressive-model .definition name="Autoregressive language model"}

An *autoregressive language model* gives the probability of a token sequence $x_1,\dots,x_T$ by the chain rule (@thm-chain-rule) as
$$
P_\theta(x_1,\dots,x_T)=\prod_{t=1}^{T}P_\theta(x_t\mid x_1,\dots,x_{t-1}),
$$
modelling each factor directly: a transformer with a causal mask (@def-self-attention) reads $x_1,\dots,x_{t-1}$ and outputs a softmax over the vocabulary at every position at once. It *generates* text by sampling $x_t$ from $P_\theta(\cdot\mid x_{<t})$, appending it and repeating.

:::

The causal mask makes the prediction at position $t$ depend only on earlier tokens, so one pass over a training sequence yields $T$ predictions. Sampling at a *temperature* $\tau$ divides the scores by $\tau$ before the softmax: $\tau<1$ sharpens the distribution towards the most likely token, $\tau>1$ flattens it.

::: {#prp-next-token-mle .proposition name="Next-token cross entropy is maximum likelihood"}

The average next-token cross-entropy loss (@def-cross-entropy-loss) over a training text equals $-\frac1T\log P_\theta(x_1,\dots,x_T)$, so minimising it maximises the likelihood of the text.

:::

::: {.proof}

1. The cross-entropy loss at position $t$, with the true next token $x_t$ as a one-hot target, is $-\log P_\theta(x_t\mid x_{<t})$.
2. Summing over $t$ and using the chain-rule factorisation, $\sum_t-\log P_\theta(x_t\mid x_{<t})=-\log\prod_tP_\theta(x_t\mid x_{<t})=-\log P_\theta(x_1,\dots,x_T)$.
3. Dividing by $T$ does not change the minimiser, and $-\log$ is decreasing.

:::

::: {#exm-bigram-model .example name="A bigram model"}

The simplest autoregressive model conditions only on the previous token and estimates each factor by counting (maximum likelihood, @thm-count-normalize-mle). From the text "the cat sat . the cat ran . the dog sat ." the estimates are $P(\text{cat}\mid\text{the})=\tfrac23$, $P(\text{dog}\mid\text{the})=\tfrac13$, $P(\text{sat}\mid\text{cat})=P(\text{ran}\mid\text{cat})=\tfrac12$ and $P(\text{.}\mid\text{sat})=1$, so "the cat sat ." gets probability $\tfrac23\cdot\tfrac12\cdot1=\tfrac13$ given its first word, while "the dog ran ." gets $0$, because "dog ran" never occurred. A transformer conditions on the whole prefix and shares what it learns between similar tokens through embeddings (@def-word-embedding), so it gives plausible but unseen sequences positive probability.

:::

::: {#def-pretraining-finetuning .definition name="Pretraining, fine-tuning, instruction tuning"}

*Pretraining* trains a language model on a very large unlabelled corpus with the next-token loss; it is *self-supervised*, since the targets are the text itself. *Fine-tuning* continues training a pretrained model, on a smaller dataset for a particular task. *Instruction tuning* fine-tunes on examples of prompts paired with good responses written by people, so that the model answers requests instead of merely continuing text.

:::

Predicting the next word of arbitrary text well requires grammar, facts and some reasoning, so pretraining builds representations that transfer to many tasks with little labelled data. The same idea works for other data: an image model can be pretrained by predicting masked patches of images.

::: {#def-rlhf .definition name="Reinforcement learning from human feedback"}

*Reinforcement learning from human feedback* (RLHF) starts from an instruction-tuned model $\pi_{\text{ref}}$.

1. People compare pairs of responses $y_w\succ y_l$ to the same prompt $x$. A *reward model* $r_\phi(x,y)$ is trained so that $P(y_w\succ y_l)=\sigma\bigl(r_\phi(x,y_w)-r_\phi(x,y_l)\bigr)$ (@def-logistic-function) fits the comparisons, by minimising $-\log\sigma\bigl(r_\phi(x,y_w)-r_\phi(x,y_l)\bigr)$.
2. The language model, viewed as a stochastic policy (@def-stochastic-policy) that chooses tokens, is trained by policy gradient (@thm-policy-gradient) to maximise
$$
\mathbb E_{y\sim\pi_\theta(\cdot\mid x)}\bigl[r_\phi(x,y)\bigr]-\beta\,\mathrm{KL}\bigl(\pi_\theta(\cdot\mid x)\,\|\,\pi_{\text{ref}}(\cdot\mid x)\bigr),
$$
where the KL penalty with weight $\beta>0$ keeps it close to $\pi_{\text{ref}}$.

:::

Comparisons are easier for people to give consistently than absolute scores or ideal answers. The penalty matters because the reward model is only an approximation: a policy free to maximise it finds responses that score highly without being good (*reward hacking*), an instance of how hard it is to state precisely what should be optimised.
