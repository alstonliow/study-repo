<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs221hw-2-q1" status="draft"}
**(a)** In the vocabulary order [about, amazing, angry, day, hate, love, of, scared, so, spiders, this, tomorrow, waiting, worried], "so" occurs twice and "worried", "about", "tomorrow" once each:
$$f(x)=[1,0,0,0,0,0,0,0,2,0,0,1,0,1].$$

**(b)**

1. Exponentials: $e^{2}\approx 7.389$, $e^{1}\approx 2.718$, $e^{-1}\approx 0.368$.
2. Sum: $7.389+2.718+0.368\approx 10.475$.
3. Divide each by the sum:
$$\mathbf p\approx[0.705,\ 0.259,\ 0.035].$$

**(c)**

1. With a one-hot $\mathbf y$, only the true class survives in the sum: $\text{Loss}_{\text{CE}}=-\log p_{\text{Anger}}=-\log 0.7\approx 0.357$.
2. As $p_{\text{Anger}}\to 1$, $-\log p_{\text{Anger}}\to 0$: a confident correct prediction costs almost nothing. The loss decreases monotonically in the correct-class probability, and it grows without bound as that probability tends to $0$, so confident mistakes are punished hardest.

**(d)**

1. Write $\log p_j=z_j-\log\sum_m e^{z_m}$, so $\text{Loss}_{\text{CE}}=-\sum_j y_jz_j+\big(\sum_j y_j\big)\log\sum_m e^{z_m}$.
2. Since $\mathbf y$ is one-hot, $\sum_j y_j=1$.
3. Differentiate in $z_k$: the first term gives $-y_k$; the second gives $\frac{e^{z_k}}{\sum_m e^{z_m}}=p_k$.
4. Hence
$$\frac{\partial\,\text{Loss}_{\text{CE}}}{\partial z_k}=p_k-y_k.$$
5. Intuition: the gradient is the prediction error. For the true class $p_k-1<0$, so gradient descent raises its logit; for every other class $p_k>0$, so their logits are lowered, each in proportion to how much probability it wrongly took. When the prediction is already right ($\mathbf p=\mathbf y$), the gradient vanishes and nothing changes.
:::

::: {.solution for="prob-softmax-regression-code" status="draft"}
```{.python}
import numpy as np


def softmax(Z):
    """Row-wise softmax of a 2-D array, without overflow."""
    E = np.exp(Z - Z.max(axis=1, keepdims=True))
    return E / E.sum(axis=1, keepdims=True)


def train_softmax_regression(X, y, K, eta, epochs):
    """Full-batch gradient descent on the mean cross entropy loss; return (W, b)."""
    n, d = X.shape
    W, b = np.zeros((K, d)), np.zeros(K)
    Y = np.eye(K)[y]                           # one-hot targets, shape (n, K)
    for _ in range(epochs):
        G = softmax(X @ W.T + b) - Y           # dLoss/dlogits for each example
        W -= eta * G.T @ X / n
        b -= eta * G.mean(axis=0)
    return W, b
```

1. Subtracting the row maximum leaves the softmax unchanged (@prp-softmax-shift) and makes every exponent at most $0$, so `np.exp` cannot overflow.
2. The gradient of the loss of one example with respect to its logits is $\operatorname{softmax}(\mathbf z)-\mathbf e_y$ (@thm-cross-entropy-gradient). By the chain rule its gradient with respect to $W$ is the outer product of this vector with $\mathbf x$, and with respect to $\mathbf b$ the vector itself.
3. Stacking the examples as rows, the mean of the outer products is `G.T @ X / n`, one matrix product instead of a loop.
:::

::: {.solution for="prob-cs231na-1-q4" status="draft"}
1. With small random weights, all scores $W\mathbf{x}$ are close to $0$.
2. The softmax of (nearly) equal scores is (nearly) uniform: each of the $10$ CIFAR-10 classes gets probability about $1/10$ (@def-softmax).
3. The cross entropy loss of an example is $-\log$ of the probability of its correct class, so about $-\log0.1=\log10\approx2.303$, and the average over the training set is the same. A loss far from this at initialization signals a bug or a badly scaled initialization (@sec-ai-deep-learning-gradient-checking).
:::
