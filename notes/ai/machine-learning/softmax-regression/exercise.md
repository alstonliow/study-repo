::: {.problem #prob-cs221hw-2-q1 origin="external" source="cs221hw-2-q1"}
Social media platforms like Twitter are rich sources of emotional expression. In this homework, you'll build classifiers to detect emotions in tweets using linear classification with cross-entropy loss and softmax activation. Consider the following dataset of 6 tweets, each labeled with exactly one emotion: **joy** (J), **anger** (A), or **fear** (F):

  Tweet                              Emotion   One-hot encoding
  ---------------------------------- --------- ------------------
  "amazing day"                    Joy       [1, 0, 0]
  "scared of spiders"              Fear      [0, 0, 1]
  "love this"                      Joy       [1, 0, 0]
  "so angry"                       Anger     [0, 1, 0]
  "so so worried about tomorrow"   Fear      [0, 0, 1]
  "hate waiting"                   Anger     [0, 1, 0]

Each tweet $x$ is mapped to a feature vector $f(x)$ using **bag-of-words representation** (you can think of it as word counts). Machine learning models don't directly take a string as input; instead, as you have learned, they work with tensors (e.g. expressed in NumPy or PyTorch). One way to convert strings to tensors is "bag-of-words" features, which treat input texts as a "bag of words" and represents them using a vector with the same length as our vocabulary. The resulting representation is a vector, where each position corresponds to a word in the vocabulary, and each value represents how many times that word appears in the input text. If we have a very large vocabulary, we would end up with a very sparse vector with many 0's.

For this problem, let's assume our vocabulary consists of all unique words in the tweets above: **{about, amazing, angry, day, hate, love, of, scared, so, spiders, this, tomorrow, waiting, worried}**.

To build our multi-class classifier, we use a weight matrix $\mathbf{W} \in \mathbb{R}^{d \times 3}$ where $d$ is the feature dimension (vocabulary size) and 3 is the number of classes. The model computes logits as $\mathbf{z} = \mathbf{W}^T f(x)$ and applies softmax to convert logits into probability values that sum to 1. Let $\mathbf{p}$ be the 3-dimensional vector of output probabilities, and $p_k$ be the probability that the input belongs to class $k$. The softmax probabilities are computed in the following way: $$p_k = \frac{e^{z_k}}{\sum_{j=1}^{3} e^{z_j}}$$

Then, given the softmax probabilities, the classifier will use argmax to choose the prediction class with the highest $p_k$.

The cross-entropy loss measures the difference between a model's predicted probabilities and the true probability distribution of the data. For a single example (with three output classes), it can be computed as follows: $$\text{Loss}_{\text{CE}}(x, \mathbf{y}, \mathbf{W}) = -\sum_{k=1}^{3} y_k \log p_k$$ where $\mathbf{y}$ is the one-hot encoded true label vector. Throughout this homework, $\log$ denotes the natural logarithm (base $e$).

(a) **Feature representation:** Using the vocabulary given above, write out the bag-of-words feature vector $f(x)$ for the tweet "so so worried about tomorrow".

*Expected:* A feature vector corresponding to the vocabulary in alphabetical order: [about, amazing, angry, day, hate, love, of, scared, so, spiders, this, tomorrow, waiting, worried].

(b) **Softmax computation:** Given logits $\mathbf{z} = [2.0, 1.0, -1.0]$ for the three classes [Joy, Anger, Fear], compute the softmax probabilities. Show your work.

*Expected:* The softmax probability vector $[P(\text{Joy}), P(\text{Anger}), P(\text{Fear})]$ with values rounded to 3 decimal places, along with your calculations of each $e^{z_k}$ and their sum.

(c) **Cross-entropy Loss:** For the tweet "so angry" with true label Anger (one-hot: [0, 1, 0]), suppose your model outputs probabilities $[0.2, 0.7, 0.1]$. Calculate the cross-entropy loss for this example, showing your work. Then explain what happens to the loss as the predicted probability for the correct class approaches 1.

*Expected:* 1.  The numerical cross-entropy loss value, rounded to 3 decimal places, with your calculation shown
2.  A brief explanation (2-3 sentences) of the loss behavior

(d) **Gradient analysis:** Derive $\frac{\partial \text{Loss}_{\text{CE}}}{\partial z_k}$, the gradient of the cross-entropy loss with respect to the logit $z_k$. Show the mathematical steps to find $\frac{\partial \text{Loss}_{\text{CE}}}{\partial z_k}$ and express your final answer in terms of $p_k$ and $y_k$ only. Then, explain intuitively why this expression makes sense for gradient-based learning.

*Expected:* 1.  Mathematical derivation showing the steps to compute $\frac{\partial \text{Loss}_{\text{CE}}}{\partial z_k}$. (Hint: you may need to use the chain rule.)
2.  Final gradient expression in terms of $p_k$ and $y_k$
3.  A brief intuitive explanation of why this gradient expression makes sense for learning (2-3 sentences)

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::

::: {#prob-softmax-regression-code .problem .coding origin="adapted" source="res-stanford-cs221-hw-sentiment" packages="numpy"}
Train a multiclass linear classifier with the cross entropy loss (@def-cross-entropy-loss) by full-batch gradient descent. Write two functions.

- `softmax(Z)`: the softmax (@def-softmax) of each row of a 2-D array `Z`. It must not overflow for large entries; use @prp-softmax-shift.
- `train_softmax_regression(X, y, K, eta, epochs)`: `X` has shape `(n, d)`, `y` holds class labels in `0, ..., K-1`. Start from $W=0$ (shape `(K, d)`) and $\mathbf b=\mathbf 0$ (shape `(K,)`), and take `epochs` gradient steps of size `eta` on the mean training loss $\frac1n\sum_i -\log\operatorname{softmax}(W\mathbf x_i+\mathbf b)_{y_i}$. Return `(W, b)`.

```{.python .starter}
import numpy as np


def softmax(Z):
    """Row-wise softmax of a 2-D array, without overflow."""
    ...


def train_softmax_regression(X, y, K, eta, epochs):
    """Full-batch gradient descent on the mean cross entropy loss; return (W, b)."""
    ...
```

```{.python .tests}
import numpy as np


def mean_loss(W, b, X, y):
    P = softmax(X @ W.T + b)
    return -np.mean(np.log(P[np.arange(len(y)), y]))


def test_softmax():
    P = softmax(np.array([[0.0, np.log(3.0)], [1000.0, 1000.0], [-1000.0, 0.0]]))
    assert np.allclose(P, [[0.25, 0.75], [0.5, 0.5], [0.0, 1.0]])
    assert np.all(np.isfinite(P))


def test_first_step():
    # from W = 0 every class has probability 1/K
    X = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    y = np.array([0, 1, 2])
    W, b = train_softmax_regression(X, y, 3, 0.3, 1)
    Y = np.eye(3)[y]
    assert np.allclose(W, -0.3 * (1 / 3 - Y).T @ X / 3)
    assert np.allclose(b, -0.3 * (1 / 3 - Y).mean(axis=0))


def test_learns_separable_data():
    X = np.array([[2.0, 0.0], [3.0, 1.0], [0.0, 2.0], [1.0, 3.0], [-2.0, -2.0], [-3.0, -1.0]])
    y = np.array([0, 0, 1, 1, 2, 2])
    W, b = train_softmax_regression(X, y, 3, 0.5, 300)
    assert W.shape == (3, 2) and b.shape == (3,)
    assert np.array_equal(np.argmax(X @ W.T + b, axis=1), y)
    zero = mean_loss(np.zeros((3, 2)), np.zeros(3), X, y)
    assert mean_loss(W, b, X, y) < 0.1 < zero


def test_large_features_stay_finite():
    X = np.array([[500.0], [-500.0]])
    W, b = train_softmax_regression(X, np.array([0, 1]), 2, 1.0, 20)
    assert np.all(np.isfinite(W)) and np.all(np.isfinite(b))
```
:::
