---
title: "Bayesian Networks and Exact Inference"
sources: [cs221-16]
requires: [ai/deep-learning/einsum, math/probability/foundations/bayes-theorem, math/probability/discrete/random-variables]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 16 (joint distributions as tensors, Bayesian networks, probabilistic inference, explaining away), in our own wording. Marginalization and conditioning are the rules of @sec-math-probability-foundations-conditional-probability and @sec-math-probability-foundations-bayes-theorem; this note only adds the tensor view and links them. -->

Search, MDPs and games represent the world by a single state. A *model-based* alternative represents it by a set of random variables (sunshine, rain, traffic, ...) and their joint distribution, and answers questions by probabilistic reasoning. Changing one part of such a model (a reward, a sensor) leaves the rest intact.

::: {#def-probabilistic-inference .definition name="Joint distribution as a tensor, probabilistic inference"}

For discrete random variables $X_1,\dots,X_n$, the joint distribution $P(X_1=x_1,\dots,X_n=x_n)$ is a tensor of rank $n$ with one axis per variable (@sec-ai-deep-learning-tensors). Given *evidence* $E=e$ for some variables $E$ and a set $Q$ of *query* variables, *probabilistic inference* computes the conditional distribution $P(Q\mid E=e)$:

1. *select* the entries consistent with the evidence, $P(Q,E=e,R)$, where $R$ are the remaining variables;
2. *marginalize* $R$: $P(Q,E=e)=\sum_rP(Q,E=e,R=r)$;
3. *normalize*: divide by $P(E=e)=\sum_qP(Q=q,E=e)$.

:::

Steps 1–2 are an einsum (@def-einsum) over the axes of $R$ with the evidence axes fixed, and step 3 is the definition of conditional probability (@def-conditional-probability). For example, with $P(S{=}0,R{=}0)=0.20$, $P(S{=}0,R{=}1)=0.08$, $P(S{=}1,R{=}0)=0.70$, $P(S{=}1,R{=}1)=0.02$ (sunshine $S$, rain $R$), marginalizing gives $P(S=1)=0.72$, and conditioning gives $P(S=0\mid R=1)=0.08/0.10=0.8$.

The joint table has $\prod_i\lvert\text{Domain}(X_i)\rvert$ entries, exponentially many. A Bayesian network writes it as a product of small local tables.

::: {#def-bayesian-network .definition name="Bayesian network"}

A *Bayesian network* over random variables $X_1,\dots,X_n$ consists of a directed acyclic graph with the variables as vertices and, for each variable $X_i$, a *local conditional distribution* $p(x_i\mid x_{\text{Parents}(i)})$ given all its parents at once. It defines the joint distribution

$$
P(X_1=x_1,\dots,X_n=x_n)=\prod_{i=1}^{n}p\bigl(x_i\mid x_{\text{Parents}(i)}\bigr).
$$

:::

Lowercase $p$ denotes the local distributions, given by definition, and uppercase $P$ the joint distribution and anything derived from it. There is one local distribution per variable, not per edge. The product is a probability distribution: summing out the variables in reverse topological order, each local distribution sums to $1$. An edge usually means direct influence; the graph and the local distributions are modelling choices.

::: {#exm-bayesian-network-alarm .example name="Burglary, earthquake, alarm"}

Burglaries $B$ and earthquakes $E$ happen independently, each with probability $\epsilon=0.05$, and either one sets off the alarm $A$: $p(a\mid b,e)=\mathbf{1}[a=\max(b,e)]$. The joint distribution is $P(B=b,E=e,A=a)=p(b)\,p(e)\,p(a\mid b,e)$. Then $P(B=1)=0.05$;

$$
P(B=1\mid A=1)=\frac{P(B=1,A=1)}{P(A=1)}=\frac{0.05}{1-0.95^2}=\frac{0.05}{0.0975}\approx0.513;
$$

and $P(B=1\mid A=1,E=1)=\dfrac{0.05\cdot0.05}{0.05}=0.05$. Hearing the alarm makes a burglary likely, but learning that there was an earthquake makes it unlikely again: the earthquake *explains away* the alarm.

:::

::: {#fig-bayesian-networks-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[vertex] (B) at (0,1) {$B$};
\node[vertex] (E) at (2,1) {$E$};
\node[vertex] (A) at (1,0) {$A$};
\draw[->] (B) -- (A); \draw[->] (E) -- (A);
\node[lab] at (1,-0.75) {alarm};
\node[vertex] (C) at (4.5,1) {$C$};
\node[vertex] (Al) at (6.5,1) {$A$};
\node[vertex] (H) at (5.5,0) {$H$};
\node[vertex] (I) at (7.5,0) {$I$};
\draw[->] (C) -- (H); \draw[->] (Al) -- (H); \draw[->] (Al) -- (I);
\node[lab] at (6,-0.75) {medical diagnosis};
\end{tikzpicture}
\end{center}
```

The graphs of @exm-bayesian-network-alarm and @exm-bayesian-network-diagnosis. Each variable has one local conditional distribution given all of its parents.

:::

::: {#rmk-bayesian-networks-1 .remark name="Explaining away"}

In general, if two causes $B$ and $E$ each make an effect $A$ more likely, then given $A=1$, also observing one cause lowers the probability of the other: $P(B=1\mid A=1,E=1)<P(B=1\mid A=1)$. This happens even though the causes are independent. It is a reasoning pattern that follows from the definitions, not something built into the model.

:::

::: {#exm-bayesian-network-diagnosis .example name="Cold or allergies"}

Cold $C$ and allergies $A$ have $p(C{=}1)=0.1$ and $p(A{=}1)=0.2$. Cough $H$ follows $\max(c,a)$ with probability $0.9$ (and is wrong with probability $0.1$); itchy eyes $I$ follow $a$ with probability $0.9$. The joint distribution is $p(c)\,p(a)\,p(h\mid c,a)\,p(i\mid a)$. Selecting, marginalizing and normalizing gives $P(C=1\mid H=1)\approx0.278$, but $P(C=1\mid H=1,I=1)\approx0.133$. Itchy eyes do not cause the cough, but they make allergies likely ($P(A=1\mid H=1)\approx0.556$ rises to $0.918$), and allergies explain away the cough.

:::

```{=latex}
\begin{algorithm}
\caption{Exact inference by enumeration}
\begin{algorithmic}
\INPUT Bayesian network over $X_1,\dots,X_n$, evidence $E=e$, query variables $Q$
\OUTPUT The table $P(Q\mid E=e)$
\FOR{each value $q$ of $Q$}
    \STATE $f(q)\gets\sum_{r}\prod_{i=1}^np\bigl(x_i\mid x_{\text{Parents}(i)}\bigr)$, where $x=(q,e,r)$ and $r$ ranges over values of the other variables
\ENDFOR
\STATE $Z\gets\sum_qf(q)$ \COMMENT{$Z=P(E=e)$}
\RETURN $f/Z$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-bayesian-networks-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.3cm,y=0.5cm]
\node[lab] at (0,0) {$b$}; \node[lab] at (1,0) {$e$}; \node[lab] at (2,0) {$a$}; \node[lab] at (3.3,0) {$P(b,e,a)$};
\foreach \r/\b/\e/\a/\p/\st in {1/0/0/0/0.9025/faint, 2/0/1/1/0.0475/, 3/1/0/1/0.0475/, 4/1/1/1/0.0025/} {
  \node[lab] at (0,-\r) {$\b$}; \node[lab] at (1,-\r) {$\e$}; \node[lab] at (2,-\r) {$\a$}; \node[lab] at (3.3,-\r) {$\p$};
}
\draw[faint] (-0.3,-1) -- (3.9,-1);
\node[lab,anchor=west] at (4.2,-2) {$b=0$: $0.0475$};
\node[lab,anchor=west] at (4.2,-3.5) {$b=1$: $0.0475+0.0025=0.05$};
\node[lab,anchor=west] at (4.2,-5) {$P(B=1\mid A=1)=0.05/0.0975\approx0.513$};
\end{tikzpicture}
\end{center}
```

Exact inference of $P(B\mid A=1)$ in the alarm network: of the four assignments with non-zero probability, select those with $a=1$ (the first is struck out), marginalize $E$ for each value of $b$, and normalize by $P(A=1)=0.0975$.

:::

::: {#rmk-bayesian-networks-2 .remark name="Language models are Bayesian networks"}

An autoregressive language model over tokens $X_1,\dots,X_T$ is a Bayesian network with an edge from every earlier token to each later one and local distributions $p(x_t\mid x_1,\dots,x_{t-1})$ computed by one neural network. Generating text samples forward; probabilistic inference would run backwards, for example finding the prompts $P(X_1,X_2,X_3\mid X_4=x_4,X_5=x_5,X_6=x_6)$ likely to produce a given response.

:::
