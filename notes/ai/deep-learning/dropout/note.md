---
title: "Dropout and Other Regularizers for Networks"
sources: [cs231n-6, cs231na-2]
requires: [ai/deep-learning/neural-networks, ai/machine-learning/regularization-and-model-selection]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS231n course notes (Neural networks part 2: regularization, dropout, noise in the forward pass) and Assignment 2 (dropout), in our own wording; the expectation proposition and its proof are our own. -->

Besides the $\ell_2$ and $\ell_1$ penalties of @def-regularization, networks are regularized by constraints on the weights and by noise injected in the forward pass. Dropout is the most used of the latter.

::: {#def-dropout .definition name="Inverted dropout"}

Let $p\in(0,1]$ be the *keep probability*. In training mode, a *dropout* layer maps $\mathbf{h}\in\mathbb{R}^m$ to

$$
\tilde{\mathbf{h}}=\frac1p\,\mathbf{r}\odot\mathbf{h},\qquad r_1,\dots,r_m\ \text{independent},\ \Pr(r_j=1)=p,\ \Pr(r_j=0)=1-p,
$$

with a fresh mask $\mathbf{r}$ for every example and every forward pass. In test mode it is the identity. Its backward pass multiplies the upstream gradient by the same $\frac1p\mathbf{r}$.

:::

::: {#fig-dropout-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0.750) -- (1.8,1.500);
\draw[faint] (0,0.750) -- (1.8,0.750);
\draw (0,0.750) -- (1.8,0.000);
\draw (0,0.750) -- (1.8,-0.750);
\draw[faint] (0,0.750) -- (1.8,-1.500);
\draw (0,0.000) -- (1.8,1.500);
\draw[faint] (0,0.000) -- (1.8,0.750);
\draw (0,0.000) -- (1.8,0.000);
\draw (0,0.000) -- (1.8,-0.750);
\draw[faint] (0,0.000) -- (1.8,-1.500);
\draw (0,-0.750) -- (1.8,1.500);
\draw[faint] (0,-0.750) -- (1.8,0.750);
\draw (0,-0.750) -- (1.8,0.000);
\draw (0,-0.750) -- (1.8,-0.750);
\draw[faint] (0,-0.750) -- (1.8,-1.500);
\draw[faint] (1.8,1.500) -- (3.6,1.500);
\draw (1.8,1.500) -- (3.6,0.750);
\draw (1.8,1.500) -- (3.6,0.000);
\draw[faint] (1.8,1.500) -- (3.6,-0.750);
\draw (1.8,1.500) -- (3.6,-1.500);
\draw[faint] (1.8,0.750) -- (3.6,1.500);
\draw[faint] (1.8,0.750) -- (3.6,0.750);
\draw[faint] (1.8,0.750) -- (3.6,0.000);
\draw[faint] (1.8,0.750) -- (3.6,-0.750);
\draw[faint] (1.8,0.750) -- (3.6,-1.500);
\draw[faint] (1.8,0.000) -- (3.6,1.500);
\draw (1.8,0.000) -- (3.6,0.750);
\draw (1.8,0.000) -- (3.6,0.000);
\draw[faint] (1.8,0.000) -- (3.6,-0.750);
\draw (1.8,0.000) -- (3.6,-1.500);
\draw[faint] (1.8,-0.750) -- (3.6,1.500);
\draw (1.8,-0.750) -- (3.6,0.750);
\draw (1.8,-0.750) -- (3.6,0.000);
\draw[faint] (1.8,-0.750) -- (3.6,-0.750);
\draw (1.8,-0.750) -- (3.6,-1.500);
\draw[faint] (1.8,-1.500) -- (3.6,1.500);
\draw[faint] (1.8,-1.500) -- (3.6,0.750);
\draw[faint] (1.8,-1.500) -- (3.6,0.000);
\draw[faint] (1.8,-1.500) -- (3.6,-0.750);
\draw[faint] (1.8,-1.500) -- (3.6,-1.500);
\draw[faint] (3.6,1.500) -- (5.4,0.375);
\draw[faint] (3.6,1.500) -- (5.4,-0.375);
\draw (3.6,0.750) -- (5.4,0.375);
\draw (3.6,0.750) -- (5.4,-0.375);
\draw (3.6,0.000) -- (5.4,0.375);
\draw (3.6,0.000) -- (5.4,-0.375);
\draw[faint] (3.6,-0.750) -- (5.4,0.375);
\draw[faint] (3.6,-0.750) -- (5.4,-0.375);
\draw (3.6,-1.500) -- (5.4,0.375);
\draw (3.6,-1.500) -- (5.4,-0.375);
\node[small vertex] at (0,0.750) {};
\node[small vertex] at (0,0.000) {};
\node[small vertex] at (0,-0.750) {};
\node[small vertex] at (1.8,1.500) {};
\node[small vertex, draw=rule, text=rule] at (1.8,0.750) {$\times$};
\node[small vertex] at (1.8,0.000) {};
\node[small vertex] at (1.8,-0.750) {};
\node[small vertex, draw=rule, text=rule] at (1.8,-1.500) {$\times$};
\node[small vertex, draw=rule, text=rule] at (3.6,1.500) {$\times$};
\node[small vertex] at (3.6,0.750) {};
\node[small vertex] at (3.6,0.000) {};
\node[small vertex, draw=rule, text=rule] at (3.6,-0.750) {$\times$};
\node[small vertex] at (3.6,-1.500) {};
\node[small vertex] at (5.4,0.375) {};
\node[small vertex] at (5.4,-0.375) {};
\end{tikzpicture}
\end{center}
```

One training forward pass of a network with dropout on its two hidden layers: the dropped units ($\times$) and their connections are absent for this example and this step, and the kept units are scaled by $1/p$. The next pass draws a new mask.

:::

```{=latex}
\begin{algorithm}
\caption{Inverted dropout}
\begin{algorithmic}
\INPUT activations $\mathbf{h}$, keep probability $p$, mode
\OUTPUT $\tilde{\mathbf{h}}$
\IF{mode is training}
    \STATE draw $r_j\sim\text{Bernoulli}(p)$ independently for every entry
    \RETURN $\mathbf{r}\odot\mathbf{h}/p$ \COMMENT{keep $\mathbf{r}$ for the backward pass}
\ELSE
    \RETURN $\mathbf{h}$
\ENDIF
\end{algorithmic}
\end{algorithm}
```

::: {#prp-dropout-expectation .proposition name="Inverted dropout preserves expectations"}

For fixed $\mathbf{h}$, $\mathbb E[\tilde{\mathbf{h}}]=\mathbf{h}$, and $\operatorname{Var}(\tilde h_j)=\frac{1-p}{p}h_j^2$. Without the factor $\frac1p$, the expected training output would be $p\,\mathbf{h}$ while the test output is $\mathbf{h}$.

:::

::: {.proof}

1. $\mathbb E[r_j]=p$, so $\mathbb E[\tilde h_j]=\frac1p\,p\,h_j=h_j$.
2. $\mathbb E[r_j^2]=\mathbb E[r_j]=p$, so $\mathbb E[\tilde h_j^2]=\frac{p}{p^2}h_j^2=\frac1ph_j^2$ and $\operatorname{Var}(\tilde h_j)=\bigl(\frac1p-1\bigr)h_j^2$.
3. Without the factor, $\mathbb E[r_jh_j]=ph_j$.

:::

::: {#fig-dropout-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw (0,0) -- (3.6,0);
\path[bar] (0.10,0) rectangle (0.50,0.80);
\path[bar] (0.70,0) rectangle (1.10,1.20);
\path[bar] (1.30,0) rectangle (1.70,0.50);
\path[bar] (1.90,0) rectangle (2.30,1.00);
\path[bar] (2.50,0) rectangle (2.90,0.70);
\path[bar] (3.10,0) rectangle (3.50,0.90);
\node[tick, below] at (1.8,-0.05) {$\mathbf h$};
\draw[map] (3.8,0.6) -- node[tick, above] {$\frac1p\,\mathbf r\odot$} (5.0,0.6);
\begin{scope}[xshift=5.2cm]
\draw (0,0) -- (3.6,0);
\path[hl cell] (0.10,0) rectangle (0.50,1.19);
\node[tick] at (0.90,0.15) {$0$};
\path[hl cell] (1.30,0) rectangle (1.70,0.75);
\path[hl cell] (1.90,0) rectangle (2.30,1.49);
\node[tick] at (2.70,0.15) {$0$};
\path[hl cell] (3.10,0) rectangle (3.50,1.34);
\node[tick, below] at (1.8,-0.05) {$\tilde{\mathbf h}$};
\end{scope}
\end{tikzpicture}
\end{center}
```

Inverted dropout with keep probability $p=\tfrac23$: dropped units become $0$ and the kept ones are scaled up by $1/p$, so $E[\tilde{\mathbf h}]=\mathbf h$

:::

Dividing by $p$ at training time means the test-time network needs no change. Without it, the next layer would see inputs about $1/p$ times larger at test time than during training, and its pre-activations, and the network's predictions, would be systematically off. The older form scales by $p$ at test time instead, which is equivalent but puts work in the deployed model.

::: {#rmk-dropout-ensemble .remark name="Dropout as an ensemble"}

Each mask selects a subnetwork, and the subnetworks share their weights; training with dropout trains an exponentially large family of them, one sampled per step. The test-time network approximates the average of their predictions (exactly so for a single linear layer, by @prp-dropout-expectation). Units cannot rely on particular other units being present, which discourages co-adaptation. Typical keep probabilities are $p=0.5$ for hidden layers of fully connected networks, larger for inputs and convolutional layers. A smaller $p$ regularizes more and slows training.

:::

::: {#rmk-dropout-other-regularizers .remark name="Noise in the forward pass and weight constraints"}

Dropout is one case of a general recipe: make the training forward pass random, and average out the randomness at test time (analytically, or by sampling). Other cases are *DropConnect*, which drops individual weights, data augmentation (random crops and flips), and the batch statistics of batch normalization. Two weight-based regularizers are also used with networks:

1. *Max-norm constraints*: after each update, project every unit's incoming weight vector onto the ball $\lVert\mathbf{w}\rVert_2\le c$ (typically $c$ is $3$ or $4$). The weights cannot explode even with large learning rates.
2. *$\ell_1$ regularization*, alone or with $\ell_2$ (the *elastic net*), drives many weights to exactly zero and makes units use a sparse subset of their inputs; plain $\ell_2$ usually works better unless sparsity is wanted.

Biases are usually not regularized. In practice one global $\ell_2$ strength, chosen by validation, is combined with dropout.

:::
