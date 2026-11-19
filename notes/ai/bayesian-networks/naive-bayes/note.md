---
title: "Naive Bayes"
sources: [cs188-20]
requires: [ai/bayesian-networks/parameter-learning, ai/machine-learning/generalization]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 20 (model-based classification, naive Bayes for digits and text, inference, parameter estimation, smoothing), in our own wording; the spam numbers are our own and were computed exactly in Python. Training, held-out and test data are in @sec-ai-machine-learning-generalization. -->

A classifier predicts a label $y$ (spam or ham, the digit in an image) from features $f_1,\dots,f_n$. One way is *model-based*: build a Bayesian network (@def-bayesian-network) relating the label and the features, learn its tables from labelled examples, and classify by inference.

::: {#def-naive-bayes .definition name="Naive Bayes"}

The *naive Bayes* model for a label $Y$ and features $F_1,\dots,F_n$ is the Bayesian network $Y\to F_i$ for every $i$: the features are conditionally independent given the label, and
$$
P(Y=y,F_1=f_1,\dots,F_n=f_n)=P(y)\prod_{i=1}^{n}P(f_i\mid y).
$$
Its prediction for features $f$ is $\operatorname{arg\,max}_yP(y\mid f)=\operatorname{arg\,max}_y\,P(y)\prod_iP(f_i\mid y)$.

:::

The assumption is almost never true (the words of an email are not independent given its class), but it makes the model tiny: $|Y|$ entries for the prior and $n\,|Y|\,|F|$ for the features, against $|Y|\,|F|^{n}$ for a full joint table, and inference is a single pass over the features. Products of many small probabilities underflow, so in practice one compares $\log P(y)+\sum_i\log P(f_i\mid y)$.

::: {#exm-naive-bayes-features .example name="Two feature designs"}

- *Digits*: one Boolean feature per pixel (on or off), so $P(F_{ij}=\text{on}\mid Y=y)$ is a table of $784$ numbers for each digit $y$ in a $28\times28$ image.
- *Text (bag of words)*: one feature $W_k$ per position $k$ in the document, whose value is the word at that position, with the same table $P(W\mid Y)$ at every position. The order of the words is ignored; only their counts matter.

:::

The tables are learnt from training data by counting and normalising, which is maximum likelihood (@thm-count-normalize-mle): $\hat P(y)$ is the fraction of examples with label $y$ and $\hat P(f_i\mid y)$ the fraction of those with $F_i=f_i$. Maximum likelihood overfits: a word never seen in spam during training gets $\hat P(\text{word}\mid\text{spam})=0$, and then a single occurrence makes any email certain to be ham, whatever else it contains. Laplace smoothing (@def-laplace-smoothing) pretends every value was seen $\lambda$ extra times; the strength $\lambda$ is a hyperparameter, tuned on held-out data.

::: {#exm-naive-bayes-spam .example name="A spam filter"}

Training data: $4$ spam and $6$ ham emails, with Boolean features "contains *free*" and "contains *meeting*". *Free* occurs in $3$ spam and $1$ ham email, *meeting* in $0$ spam and $4$ ham emails. So $\hat P(\text{spam})=0.4$. Maximum likelihood gives $\hat P(\textit{meeting}\mid\text{spam})=0$, so every email containing *meeting* is classified as ham with certainty. With Laplace smoothing, $\lambda=1$, each Boolean feature adds $1$ to both counts:
$$
\hat P(\textit{free}\mid\text{spam})=\tfrac{3+1}{4+2}=\tfrac23,\quad \hat P(\textit{meeting}\mid\text{spam})=\tfrac16,\quad \hat P(\textit{free}\mid\text{ham})=\tfrac{1+1}{6+2}=\tfrac14,\quad \hat P(\textit{meeting}\mid\text{ham})=\tfrac58.
$$
An email containing both words scores $0.4\cdot\tfrac23\cdot\tfrac16=\tfrac{2}{45}$ for spam and $0.6\cdot\tfrac14\cdot\tfrac58=\tfrac{3}{32}$ for ham, so $P(\text{spam}\mid f)=\tfrac{64}{199}\approx0.32$: probably ham, but not certainly. An email with *free* and without *meeting* gets $P(\text{spam}\mid f)=\tfrac{320}{401}\approx0.80$.

:::

::: {#rmk-naive-bayes-odds .remark name="Which features matter"}

The ratio $P(f_i\mid\text{spam})/P(f_i\mid\text{ham})$ says how strongly feature value $f_i$ points to spam; in the example the presence of *free* multiplies the odds of spam by $\tfrac{2/3}{1/4}=\tfrac83$ and the presence of *meeting* divides them by $\tfrac{5/8}{1/6}=\tfrac{15}{4}$. Sorting words by this ratio shows what a trained filter has learnt; with too little smoothing the top of the list is filled with rare words seen once.

:::
