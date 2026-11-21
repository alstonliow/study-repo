---
title: "Recurrent Neural Networks"
sources: [cs231n-12, cs231na-2]
requires: [ai/deep-learning/training-deep-networks, ai/machine-learning/text-representation]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS231n course notes (Recurrent neural networks: recurrence, character-level language model, multilayer RNNs, vanilla RNN gradient flow) and Assignment 2 (image captioning with vanilla RNNs), in our own wording; the gradient theorem, its proof and the example are our own (numbers computed in Python). -->

Feed-forward and convolutional networks map one fixed-size input to one output. Many problems involve sequences: a caption generated word by word from an image, a video classified from its frames, text modelled character by character. A *recurrent neural network* (RNN) applies the same function at every time step and carries a hidden state from one step to the next.

::: {#def-vanilla-rnn .definition name="Vanilla recurrent neural network"}

A *vanilla RNN* with hidden size $m$ has parameters $W_{hh}\in\mathbb{R}^{m\times m}$, $W_{xh}\in\mathbb{R}^{m\times d}$, $\mathbf{b}\in\mathbb{R}^m$ and an output layer $W_{hy},\mathbf{b}_y$. Given inputs $\mathbf{x}_1,\dots,\mathbf{x}_T\in\mathbb{R}^d$ and an initial state $\mathbf{h}_0$, it computes

$$
\mathbf{h}_t=\tanh\bigl(W_{hh}\mathbf{h}_{t-1}+W_{xh}\mathbf{x}_t+\mathbf{b}\bigr),\qquad \mathbf{y}_t=W_{hy}\mathbf{h}_t+\mathbf{b}_y,\qquad t=1,\dots,T.
$$

The same parameters are used at every step, so the network handles sequences of any length.

:::

Unrolled over time, the RNN is an ordinary computation graph (@def-computation-graph) of depth $T$ with shared weights. Depending on the task it is used *many-to-many* (an output at every step, as in language modelling), *many-to-one* (only $\mathbf{y}_T$, as in classifying a sequence) or *one-to-many* (one input, a generated sequence, as in captioning).

::: {#def-char-rnn .definition name="Character-level language model"}

For a vocabulary of $V$ characters, a *character-level RNN language model* reads the one-hot vectors (@def-one-hot) of a text $c_1,\dots,c_T$ and treats $\mathbf{y}_t\in\mathbb{R}^V$ as logits for the next character: it is trained to minimize $\sum_{t=1}^{T-1}-\log\operatorname{softmax}(\mathbf{y}_t)_{c_{t+1}}$, the cross entropy loss (@def-cross-entropy-loss) at every step. To generate text, it samples $c_{t+1}$ from $\operatorname{softmax}(\mathbf{y}_t)$ and feeds it back as the next input.

:::

Image captioning works the same way with words: a convolutional network turns the image into a code (its last hidden layer, @sec-ai-deep-learning-network-visualization), a learnt linear map of the code gives $\mathbf{h}_0$, and the RNN generates the caption one word at a time from a start token until an end token. A word-level model has a large vocabulary but short sequences; a character-level one a tiny vocabulary and output layer but sequences several times longer, which makes long-range dependencies harder to learn.

::: {#def-bptt .definition name="Backpropagation through time"}

*Backpropagation through time* (BPTT) is backpropagation (@def-backpropagation) on the unrolled graph: the forward pass computes $\mathbf{h}_1,\dots,\mathbf{h}_T$ and the losses, and the backward pass goes from $t=T$ down to $1$, adding the gradient contributions of every step to the shared $W_{hh},W_{xh},\mathbf{b}$. *Truncated* BPTT processes a long sequence in chunks of, say, $100$ steps, carrying the hidden state forward across chunks but backpropagating only within each chunk.

:::

```{=latex}
\begin{algorithm}
\caption{Backpropagation through time for a vanilla RNN}
\begin{algorithmic}
\INPUT inputs $\mathbf{x}_{1..T}$, $\mathbf{h}_0$, parameters, upstream gradients $\partial L/\partial\mathbf{h}_t$ from the outputs
\OUTPUT gradients of $W_{hh},W_{xh},\mathbf{b}$
\STATE forward: compute and store $\mathbf{h}_1,\dots,\mathbf{h}_T$
\STATE $\mathbf{d}\gets\mathbf 0$; all parameter gradients $\gets0$
\FOR{$t=T,T-1,\dots,1$}
    \STATE $\mathbf{d}\gets\mathbf{d}+\partial L/\partial\mathbf{h}_t$ \COMMENT{gradient on $\mathbf{h}_t$ from the output and from step $t+1$}
    \STATE $\mathbf{a}\gets(1-\mathbf{h}_t^2)\odot\mathbf{d}$ \COMMENT{through $\tanh$}
    \STATE $\nabla W_{hh}\mathrel{+}=\mathbf{a}\mathbf{h}_{t-1}^{\mathsf T}$; $\nabla W_{xh}\mathrel{+}=\mathbf{a}\mathbf{x}_t^{\mathsf T}$; $\nabla\mathbf{b}\mathrel{+}=\mathbf{a}$
    \STATE $\mathbf{d}\gets W_{hh}^{\mathsf T}\mathbf{a}$ \COMMENT{passed to $\mathbf{h}_{t-1}$}
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

::: {#thm-rnn-gradient-flow .theorem name="Gradient flow in a vanilla RNN"}

For $s<t$,

$$
\frac{\partial\mathbf{h}_t}{\partial\mathbf{h}_s}=\prod_{k=t}^{s+1}D_kW_{hh},\qquad D_k=\operatorname{diag}\bigl(1-\mathbf{h}_k^2\bigr),
$$

the product taken with $k$ decreasing from left to right. Consequently $\bigl\lVert\partial\mathbf{h}_t/\partial\mathbf{h}_s\bigr\rVert_2\le\sigma_{\max}(W_{hh})^{\,t-s}$, where $\sigma_{\max}$ is the largest singular value; if $\sigma_{\max}(W_{hh})<1$, the gradient from step $t$ to step $s$ vanishes geometrically in $t-s$.

:::

::: {.proof}

1. $\mathbf{h}_k=\tanh(\mathbf{z}_k)$ with $\mathbf{z}_k=W_{hh}\mathbf{h}_{k-1}+W_{xh}\mathbf{x}_k+\mathbf{b}$, and $\tanh'(z)=1-\tanh^2z$ (@prp-sigmoid-saturation), so the Jacobian of one step is $\partial\mathbf{h}_k/\partial\mathbf{h}_{k-1}=D_kW_{hh}$.
2. The chain rule over the steps $s+1,\dots,t$ multiplies these Jacobians, giving the product.
3. The entries of $D_k$ lie in $(0,1]$, so $\lVert D_k\rVert_2\le1$; and $\lVert W_{hh}\rVert_2=\sigma_{\max}(W_{hh})$. Submultiplicativity of the operator norm gives the bound.

:::

If instead $\sigma_{\max}(W_{hh})>1$ and the units are not saturated, the gradient can grow geometrically: the scalar picture of @prp-vanishing-exploding-gradients, with the matrix $W_{hh}$ applied $t-s$ times.

::: {#exm-rnn-gradient-flow .example name="A scalar RNN forgets"}

With $m=d=1$, $W_{hh}=0.5$, $W_{xh}=1$, $b=0$, $h_0=0$ and inputs $1,0,0,0$, the states are $h_1,\dots,h_4=0.7616,\ 0.3634,\ 0.1797,\ 0.0896$. The factors $W_{hh}(1-h_k^2)$ for $k=2,3,4$ are $0.434,\ 0.484,\ 0.496$, so $\partial h_4/\partial h_1\approx0.104$: after three steps the first input's influence on the gradient is cut by a factor of about ten.

:::

::: {#fig-recurrent-neural-networks-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\node[box] (h0) at (0,0) {$h_0=0$};
\node[box] (h1) at (2.2,0) {$h_1=0.762$};
\node[lab] (x1) at (2.2,-1.2) {$x_1=1$};
\draw[->] (x1) -- (h1);
\draw[->] (h0) -- (h1);
\node[box] (h2) at (4.4,0) {$h_2=0.363$};
\node[lab] (x2) at (4.4,-1.2) {$x_2=0$};
\draw[->] (x2) -- (h2);
\draw[->] (h1) -- (h2);
\node[box] (h3) at (6.60,0) {$h_3=0.180$};
\node[lab] (x3) at (6.60,-1.2) {$x_3=0$};
\draw[->] (x3) -- (h3);
\draw[->] (h2) -- (h3);
\node[box] (h4) at (8.8,0) {$h_4=0.090$};
\node[lab] (x4) at (8.8,-1.2) {$x_4=0$};
\draw[->] (x4) -- (h4);
\draw[->] (h3) -- (h4);
\node[lab,tick] at (3.30,0.55) {$\times0.434$};
\node[lab,tick] at (5.5,0.55) {$\times0.484$};
\node[lab,tick] at (7.70,0.55) {$\times0.496$};
\draw[hl,->] (8.8,1.0) -- (2.2,1.0) node[lab,anchor=east] {gradient};
\end{tikzpicture}
\end{center}
```

The scalar RNN of @exm-rnn-gradient-flow unrolled over four steps. Backpropagation through time sends the gradient from $h_4$ back along the chain, multiplying it at each step by $W_{hh}(1-h_k^2)$, so that $\partial h_4/\partial h_1\approx0.104$.

:::

::: {#def-gradient-clipping .definition name="Gradient clipping"}

*Gradient clipping* with threshold $c>0$ replaces a gradient $\mathbf{g}$ by $c\,\mathbf{g}/\lVert\mathbf{g}\rVert$ whenever $\lVert\mathbf{g}\rVert>c$, keeping its direction and bounding its size.

:::

Clipping controls exploding gradients; vanishing gradients need a different architecture, the LSTM of @sec-ai-deep-learning-lstm. *Multilayer* RNNs stack $L$ recurrent layers, the hidden states of layer $\ell$ being the inputs of layer $\ell+1$; two to four layers are common.
