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

::: {#fig-language-models-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (t0) at (0.0,0) {the};
\node[box] (t1) at (1.5,0) {cat};
\node[box] (t2) at (3.0,0) {sat};
\node[box] (t3) at (4.5,0) {on};
\draw[map, faint] (t0.north) to[out=60, in=120] (t1.north);
\draw[map, faint] (t0.north) to[out=60, in=120] (t2.north);
\draw[map, faint] (t1.north) to[out=60, in=120] (t2.north);
\draw[map, faint] (t0.north) to[out=60, in=120] (t3.north);
\draw[map, faint] (t1.north) to[out=60, in=120] (t3.north);
\draw[map, faint] (t2.north) to[out=60, in=120] (t3.north);
\node[lab, text=accent] at (6.0,0) {?};
\draw[map, hl] (t3) -- (5.8,0);
\end{tikzpicture}
\end{center}
```

An autoregressive model factorises $P(x_1,\dots,x_n)=\prod_tP(x_t\mid x_{<t})$: each token is predicted from all the tokens before it (arcs), never from later ones

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

::: {#fig-language-models-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.0,-0.0) rectangle (0.7,-0.45);
\draw[hl cell] (0.7,-0.0) rectangle (1.4,-0.45);
\node[tick] at (1.05,-0.22) {$2/3$};
\draw[hl cell] (1.4,-0.0) rectangle (2.10,-0.45);
\node[tick] at (1.75,-0.22) {$1/3$};
\draw[cell frame] (2.10,-0.0) rectangle (2.8,-0.45);
\draw[cell frame] (2.8,-0.0) rectangle (3.5,-0.45);
\draw[cell frame] (3.5,-0.0) rectangle (4.2,-0.45);
\draw[cell frame] (0.0,-0.45) rectangle (0.7,-0.9);
\draw[cell frame] (0.7,-0.45) rectangle (1.4,-0.9);
\draw[cell frame] (1.4,-0.45) rectangle (2.10,-0.9);
\draw[hl cell] (2.10,-0.45) rectangle (2.8,-0.9);
\node[tick] at (2.45,-0.67) {$1/2$};
\draw[hl cell] (2.8,-0.45) rectangle (3.5,-0.9);
\node[tick] at (3.15,-0.67) {$1/2$};
\draw[cell frame] (3.5,-0.45) rectangle (4.2,-0.9);
\draw[cell frame] (0.0,-0.9) rectangle (0.7,-1.35);
\draw[cell frame] (0.7,-0.9) rectangle (1.4,-1.35);
\draw[cell frame] (1.4,-0.9) rectangle (2.10,-1.35);
\draw[hl cell] (2.10,-0.9) rectangle (2.8,-1.35);
\node[tick] at (2.45,-1.12) {$1$};
\draw[cell frame] (2.8,-0.9) rectangle (3.5,-1.35);
\draw[cell frame] (3.5,-0.9) rectangle (4.2,-1.35);
\draw[cell frame] (0.0,-1.35) rectangle (0.7,-1.8);
\draw[cell frame] (0.7,-1.35) rectangle (1.4,-1.8);
\draw[cell frame] (1.4,-1.35) rectangle (2.10,-1.8);
\draw[cell frame] (2.10,-1.35) rectangle (2.8,-1.8);
\draw[cell frame] (2.8,-1.35) rectangle (3.5,-1.8);
\draw[hl cell] (3.5,-1.35) rectangle (4.2,-1.8);
\node[tick] at (3.85,-1.57) {$1$};
\draw[cell frame] (0.0,-1.8) rectangle (0.7,-2.25);
\draw[cell frame] (0.7,-1.8) rectangle (1.4,-2.25);
\draw[cell frame] (1.4,-1.8) rectangle (2.10,-2.25);
\draw[cell frame] (2.10,-1.8) rectangle (2.8,-2.25);
\draw[cell frame] (2.8,-1.8) rectangle (3.5,-2.25);
\draw[hl cell] (3.5,-1.8) rectangle (4.2,-2.25);
\node[tick] at (3.85,-2.02) {$1$};
\draw[hl cell] (0.0,-2.25) rectangle (0.7,-2.7);
\node[tick] at (0.35,-2.47) {$1$};
\draw[cell frame] (0.7,-2.25) rectangle (1.4,-2.7);
\draw[cell frame] (1.4,-2.25) rectangle (2.10,-2.7);
\draw[cell frame] (2.10,-2.25) rectangle (2.8,-2.7);
\draw[cell frame] (2.8,-2.25) rectangle (3.5,-2.7);
\draw[cell frame] (3.5,-2.25) rectangle (4.2,-2.7);
\node[tick, left] at (0,-0.22) {the};
\node[tick, above] at (0.35,0) {the};
\node[tick, left] at (0,-0.67) {cat};
\node[tick, above] at (1.05,0) {cat};
\node[tick, left] at (0,-1.12) {dog};
\node[tick, above] at (1.75,0) {dog};
\node[tick, left] at (0,-1.57) {sat};
\node[tick, above] at (2.45,0) {sat};
\node[tick, left] at (0,-2.02) {ran};
\node[tick, above] at (3.15,0) {ran};
\node[tick, left] at (0,-2.47) {.};
\node[tick, above] at (3.85,0) {.};
\end{tikzpicture}
\end{center}
```

The bigram estimates of @exm-bigram-model as a table: row = previous token, column = next token. Each row is a conditional distribution; empty cells have probability $0$

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

::: {#fig-language-models-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (b0) at (0.0,0) {pretraining};
\node[box] (b1) at (3.4,0) {instruction tuning};
\draw[map] (b0) -- (b1);
\node[hl box] (b2) at (6.8,0) {reward model $r_\phi$};
\draw[map] (b1) -- (b2);
\node[hl box] (b3) at (10.2,0) {RL against $r_\phi$};
\draw[map] (b2) -- (b3);
\end{tikzpicture}
\end{center}
```

The training pipeline of a chat model: pretraining on text, supervised instruction tuning, then the two RLHF stages, fitting a reward model to human comparisons and optimising the policy against it

:::

Comparisons are easier for people to give consistently than absolute scores or ideal answers. The penalty matters because the reward model is only an approximation: a policy free to maximise it finds responses that score highly without being good (*reward hacking*), an instance of how hard it is to state precisely what should be optimised.
