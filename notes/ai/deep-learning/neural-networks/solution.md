<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs221hw-2-q2" status="draft"}
**(a)** Average of $\text{so}=[0.1,0]$ and $\text{angry}=[-0.6,-0.8]$:
$$\mathbf x=\tfrac12\big([0.1,0]+[-0.6,-0.8]\big)=[-0.25,\,-0.4].$$
Benefit: every tweet, whatever its length, becomes a dense vector of the same small dimension, and similar words give similar tweet vectors. Limitation: averaging ignores word order and dilutes strong words, so "not happy" and "happy not", or a long tweet with one key word, are hard to tell apart.

**(b)**

| Node/Variable | Formula/Computation | Value |
|---|---|---|
| $x$ | NA | $[-0.250,\,-0.400]$ |
| $\mathbf h$ | $\text{ReLU}(\mathbf W^{(1)}\mathbf x+\mathbf b^{(1)})=\text{ReLU}([-0.25-0.2+0.1,\ 0.125-0.4-0.2])=\text{ReLU}([-0.350,-0.475])$ | $[0.000,\,0.000]$ |
| $z$ | $\mathbf W^{(2)}\mathbf h+b^{(2)}=0+0.3$ | $0.300$ |
| $\hat y$ | $\sigma(0.3)=1/(1+e^{-0.3})$ | $0.574$ |

Both hidden pre-activations are negative, so both ReLUs output $0$ and the prediction is fixed by the output bias alone.

**(c)** With $y_{\text{true}}=0$ the loss is $L=-\log(1-\hat y)=-\log 0.426\approx 0.854$.

| Gradient | Formula (Chain Rule) | Value |
|---|---|---|
| $\frac{\partial L}{\partial \hat y}$ | $\frac{1}{1-\hat y}$ (for $y_{\text{true}}=0$) | $2.350$ |
| $\frac{\partial L}{\partial z}$ | $\frac{\partial L}{\partial \hat y}\cdot\hat y(1-\hat y)=\hat y-y_{\text{true}}$ | $0.574$ |
| $\frac{\partial L}{\partial \mathbf h}$ | $\frac{\partial L}{\partial z}\,\mathbf W^{(2)\top}$ | $[0.460,\,-0.345]$ |
| $\frac{\partial L}{\partial \mathbf W^{(2)}}$ | $\frac{\partial L}{\partial z}\,\mathbf h^\top$ | $[0.000,\,0.000]$ |
| $\frac{\partial L}{\partial b^{(2)}}$ | $\frac{\partial L}{\partial z}$ | $0.574$ |
| $\frac{\partial L}{\partial \mathbf W^{(1)}}$ | $\big(\frac{\partial L}{\partial \mathbf h}\odot\mathbb 1[\mathbf W^{(1)}\mathbf x+\mathbf b^{(1)}>0]\big)\mathbf x^\top$ | all entries $0.000$ |
| $\frac{\partial L}{\partial \mathbf b^{(1)}}$ | $\frac{\partial L}{\partial \mathbf h}\odot\mathbb 1[\mathbf W^{(1)}\mathbf x+\mathbf b^{(1)}>0]$ | $[0.000,\,0.000]$ |

Because both ReLUs are inactive, their derivative is $0$, so no gradient reaches the first layer, and $\mathbf W^{(2)}$ gets none because $\mathbf h=\mathbf 0$. On this example only $b^{(2)}$ learns.

**(d)** Positive words (amazing $[0.8,0.6]$, love $[0.9,0.4]$) sit together in the first quadrant, negative words (scared, hate, angry) together in the third, and neutral words (this, about, of) at or near the origin. So direction encodes polarity and distance from the origin roughly encodes strength: similar meanings get nearby vectors. Bag-of-words gives every word its own orthogonal axis, so "love" is as far from "amazing" as from "hate"; embeddings share statistical strength between related words and generalise to words the classifier saw rarely.
:::

::: {.solution for="prob-mlp-average-embedding-code" status="draft"}
```{.python}
import numpy as np


def mlp_probs(texts, emb, W1, b1, W2, b2):
    """Class probabilities of an MLP on the average word embedding of each text."""
    d = W1.shape[1]
    X = np.zeros((len(texts), d))
    for i, text in enumerate(texts):
        vecs = [emb[t] for t in text.lower().split() if t in emb]
        if vecs:
            X[i] = np.mean(vecs, axis=0)
    H = np.maximum(X @ W1.T + b1, 0)           # hidden units, one row per text
    Z = H @ W2.T + b2                          # logits
    E = np.exp(Z - Z.max(axis=1, keepdims=True))
    return E / E.sum(axis=1, keepdims=True)
```

1. Averaging the embeddings turns a text of any length into one vector of shape `(d,)`; it is the bag-of-words vector of the text multiplied by the matrix whose rows are the embeddings.
2. With one text per row of `X`, the layer $W_1\mathbf x+\mathbf b_1$ for all texts at once is `X @ W1.T + b1`; `np.maximum(·, 0)` is the ReLU.
3. The softmax subtracts the row maximum before exponentiating, so large logits do not overflow.
:::
