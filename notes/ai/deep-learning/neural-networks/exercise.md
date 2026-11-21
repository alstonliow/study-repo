::: {.problem #prob-cs221hw-2-q2 origin="external" source="cs221hw-2-q2"}
In the previous problem, we used bag-of-words features for sentiment classification. It is now an outdated method of representing texts in machine learning due to many limitations. For example, it doesn't capture word relationships (e.g., "amazing" and "wonderful" are similar but treated as completely different features) and creates very sparse, high-dimensional vectors. In this problem, we'll explore how neural networks with word embeddings can address these issues.

We'll use the same set of tweets from Problem 1, but now represent each word with a dense 2-dimensional embedding vector. For simplicity, assume we have the following pre-trained word embeddings:

  Word       Embedding
  ---------- ----------------
  amazing    [0.8, 0.6]
  day        [0.2, 0.1]
  scared     [-0.5, -0.7]
  of         [0.0, 0.0]
  spiders    [-0.3, -0.4]
  love       [0.9, 0.4]
  this       [0.0, 0.0]
  so         [0.1, 0.0]
  angry      [-0.6, -0.8]
  worried    [-0.3, -0.6]
  about      [0.0, -0.1]
  tomorrow   [0.2, -0.2]
  hate       [-0.8, -0.5]
  waiting    [-0.1, -0.3]

For simplicity, we will focus on **binary sentiment classification (positive or negative)** instead of three-class classification for this problem only.

(a) **Embeddings via averaging:** One simple approach is to represent each tweet as the average of its word embeddings. Compute the averaged embedding representation for "so angry", showing your work. Comment on one advantage and one disadvantage of this approach.

*Expected:* 1.  A 2-dimensional averaged embedding vector, with your calculation shown
2.  Discuss one benefit and one limitation of creating embeddings for a text by averaging embeddings of its component words (2-3 sentences)

(b) **Forward pass:** Using the averaged representation for "so angry" from part (a), perform a forward pass step-by-step to find the predicted label $\hat{y}$. Show your intermediate calculations by filling in the table below.

For the sake of simplicity, we'll use a 2-input, 2-hidden neuron, 1-output architecture consisting of:

1.  **Input layer:** Word embeddings $\mathbf{x}$
2.  **Hidden layer:** 2 neurons with ReLU activation, where $\text{ReLU}(\mathbf{x}) = \max(0, \mathbf{x})$
3.  **Output layer:** 1 neuron (binary sentiment classification) with sigmoid activation

The forward pass equations are: $$\mathbf{h} = \text{ReLU}(\mathbf{W}^{(1)} \mathbf{x} + \mathbf{b}^{(1)})$$ $$z = \mathbf{W}^{(2)} \mathbf{h} + b^{(2)}$$ $$\hat{y} = \sigma(z) = \frac{1}{1 + e^{-z}}$$ where $\mathbf{x} = [x_1, x_2]^T$ is the 2D input representation, $\hat{y}$ is the predicted label, $\mathbf{W}^{(1)} \in \mathbb{R}^{2 \times 2}$, $\mathbf{b}^{(1)} \in \mathbb{R}^{2}$, $\mathbf{W}^{(2)} \in \mathbb{R}^{1 \times 2}$, and $b^{(2)} \in \mathbb{R}$.

**Network parameters:**
$$\mathbf{W}^{(1)} = \begin{bmatrix} 1.0 & 0.5 \\ -0.5 & 1.0 \end{bmatrix}, \quad \mathbf{b}^{(1)} = \begin{bmatrix} 0.1 \\ -0.2 \end{bmatrix}$$ $$\mathbf{W}^{(2)} = \begin{bmatrix} 0.8 & -0.6 \end{bmatrix}, \quad b^{(2)} = 0.3$$

**You should write your answers by copying and pasting the table below and filling its cells, or using bullet points to clearly state the value of each cell. Round numerical values to 3 decimal places.**

  Node/Variable     Formula/Computation   Value
  ----------------- --------------------- -------
  $x$             NA                    
  $\mathbf{h}$                         
  $z$                                   
  $\hat{y}$                            

*Expected:* 1.  Compute forward pass values at each node. Show your calculations for each step by filling in the table above

(c) **Backpropagation:** Using the same weights, bias and input vector as in part (b), first compute the loss value $L$. Then, perform backpropagation to compute gradients $\frac{\partial L}{\partial \mathbf{W}^{(1)}}$, $\frac{\partial L}{\partial \mathbf{b}^{(1)}}$, $\frac{\partial L}{\partial \mathbf{W}^{(2)}}$, and $\frac{\partial L}{\partial b^{(2)}}$. Assume the true label is $y_{\text{true}} = 0$ (negative sentiment) and we're using binary cross-entropy loss: $$L = -[y_{\text{true}} \log(\hat{y}) + (1 - y_{\text{true}}) \log(1 - \hat{y})]$$

**You should write your answers by copying and pasting the tables below and filling their cells, or using bullet points to clearly state the value of each cell. Round numerical values to 3 decimal places.**

  Variable   Formula/Computation   Value
  ---------- --------------------- -------
  $L$                            

  Gradient                                                Formula (Chain Rule)   Value
  ------------------------------------------------------- ---------------------- -------
  $\frac{\partial L}{\partial \hat{y}}$                                    
  $\frac{\partial L}{\partial z}$                                           
  $\frac{\partial L}{\partial \mathbf{h}}$                                 
  $\frac{\partial L}{\partial \mathbf{W}^{(2)}}$                          
  $\frac{\partial L}{\partial b^{(2)}}$                                    
  $\frac{\partial L}{\partial \mathbf{W}^{(1)}}$                          
  $\frac{\partial L}{\partial \mathbf{b}^{(1)}}$                          

*Expected:* 1.  Compute the loss value $L$, showing your calculation in the Formula/Computation column
2.  Starting from $\frac{\partial L}{\partial \hat{y}}$, compute gradients for each node working backwards and fill out the table given above. For the formula column, you should express each partial in terms of partials above it in the table (recall [backpropagation](https://stanford-cs221.github.io/lectures/?trace=backpropagation) from lecture!)
3.  Feel free to reuse values you already computed in part b

(d) **Embedding analysis:** Looking at the provided word embeddings, identify patterns in how positive emotion words (amazing, love), negative emotion words (scared, hate, angry), and neutral words (this, about, of) are positioned in the 2D embedding space. You don't have to plot anything for this problem; simply observe the patterns. What does this suggest about how word embeddings capture semantic relationships? Explain why embeddings might be more meaningful than the bag-of-words approach for capturing semantic relationships.

*Expected:* 1.  Describe the spatial clustering of different word types (1-2 sentences)
2.  Explain how embeddings capture semantic similarity and its advantage over the bag-of-words approach (1-2 sentences)

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::

::: {#prob-mlp-average-embedding-code .problem .coding origin="adapted" source="res-stanford-cs221-hw-sentiment" packages="numpy"}
Classify texts with a one-hidden-layer MLP (@def-multi-layer-perceptron) on averaged word embeddings. Write `mlp_probs(texts, emb, W1, b1, W2, b2)`.

- `emb` maps words to vectors of shape `(d,)`. Tokenize a text by lower-casing it and splitting it on whitespace. Its input $\mathbf x$ is the average of the embeddings of its tokens that are in `emb`, or the zero vector if none is.
- The network computes $\mathbf h=\operatorname{ReLU}(W_1\mathbf x+\mathbf b_1)$ with $W_1$ of shape `(m, d)`, then the logits $\mathbf z=W_2\mathbf h+\mathbf b_2$ with $W_2$ of shape `(K, m)`.
- Return an array of shape `(len(texts), K)` whose row `i` is $\operatorname{softmax}(\mathbf z)$ for text `i`.

```{.python .starter}
import numpy as np


def mlp_probs(texts, emb, W1, b1, W2, b2):
    """Class probabilities of an MLP on the average word embedding of each text."""
    ...
```

```{.python .tests}
import numpy as np

emb = {"good": np.array([1.0, 0.0]), "bad": np.array([-1.0, 0.0]), "plot": np.array([0.0, 2.0])}
W1, b1 = np.array([[1.0, 0.0], [-1.0, 0.0], [0.0, 1.0]]), np.zeros(3)
W2, b2 = np.array([[0.0, 2.0, 0.0], [2.0, 0.0, 0.0]]), np.array([0.0, 0.0])


def softmax(z):
    e = np.exp(z - z.max())
    return e / e.sum()


def test_hand_example():
    P = mlp_probs(["Good plot", "bad"], emb, W1, b1, W2, b2)
    # "good plot": x = (0.5, 1), h = (0.5, 0, 1), z = (0, 1)
    # "bad":       x = (-1, 0),  h = (0, 1, 0),   z = (2, 0)
    assert P.shape == (2, 2)
    assert np.allclose(P[0], softmax(np.array([0.0, 1.0])))
    assert np.allclose(P[1], softmax(np.array([2.0, 0.0])))


def test_unknown_words_and_empty_text():
    P = mlp_probs(["unknown words only", "", "good ???"], emb, W1, b1, W2, b2 + [0.0, 1.0])
    assert np.allclose(P[0], softmax(np.array([0.0, 1.0])))
    assert np.allclose(P[1], P[0])
    assert np.allclose(P[2], mlp_probs(["good"], emb, W1, b1, W2, b2 + [0.0, 1.0])[0])


def test_relu_and_rows_sum_to_one():
    rng = np.random.default_rng(3)
    big = {w: rng.normal(size=4) for w in "abcdef"}
    A1, c1, A2, c2 = rng.normal(size=(5, 4)), rng.normal(size=5), rng.normal(size=(3, 5)), rng.normal(size=3)
    texts = ["a b c", "d e f f", "a"]
    P = mlp_probs(texts, big, A1, c1, A2, c2)
    assert P.shape == (3, 3) and np.allclose(P.sum(axis=1), 1)
    x = (big["d"] + big["e"] + 2 * big["f"]) / 4
    assert np.allclose(P[1], softmax(A2 @ np.maximum(A1 @ x + c1, 0) + c2))
```
:::

::: {.problem #prob-mit18065ps-26-q4 origin="external" source="mit18065ps-26-q4"}
Explain with words or show with graphs why each of these statements about Continuous Piecewise Linear functions (CPL functions) is true :

M  The maximum $M(x,y)$ of two CPL functions $F_1(x,y)$ and $F_2(x,y)$ is CPL.

S  The sum $S(x,y)$ of two CPL functions $F_1(x,y)$ and $F_2(x,y)$ is CPL.

C  If the one-variable functions $y=F_1(x)$ and $z=F_2(y)$ are CPL, so is the composition $C(x)=z=F_2(F_1(x))$.
:::

::: {.problem #prob-mit18065ps-33-q5 origin="external" source="mit18065ps-33-q5"}
How many weights and biases are in a network with $m=N_0=4$ inputs in each feature vector $\mathbf{v}_0$ and $N=6$ neurons on each of the 3 hidden layers ? How many activation functions (ReLU) are in this network, before the final output ?

*Note (these notes):* The problem does not state the output size; the solution assumes a single output.
:::

::: {.problem #prob-cs231na-1-q8 origin="external" source="cs231na-1-q8"}
We've only asked you to implement ReLU, but there are a number of different activation functions that one could use in neural networks, each with its pros and cons. In particular, an issue commonly seen with activation functions is getting zero (or close to zero) gradient flow during backpropagation. Which of the following activation functions have this problem? If you consider these functions in the one dimensional case, what types of input would lead to this behaviour?
1. Sigmoid
2. ReLU
3. Leaky ReLU
:::

::: {#prob-two-layer-net-code .problem .coding origin="adapted" source="res-stanford-cs231n-assignments-ps1" packages="numpy"}
Write `two_layer_loss_grad(X, y, W1, b1, W2, b2, reg)` for a network with one ReLU hidden layer and a softmax output, trained with the cross entropy loss (@def-multi-layer-perceptron, @def-cross-entropy-loss).

- Rows of `X` (shape `(N, D)`) are examples; $H=\operatorname{ReLU}(XW_1+\mathbf b_1)$ with $W_1$ of shape `(D, M)`, scores $S=HW_2+\mathbf b_2$ with $W_2$ of shape `(M, K)`.
- The loss is the average cross entropy over the examples plus `reg * (np.sum(W1**2) + np.sum(W2**2))`.
- Return `(loss, grads)`, `grads` a dict with keys `"W1", "b1", "W2", "b2"`. Use the shift of @prp-softmax-shift for numerical stability.

```{.python .starter}
import numpy as np


def two_layer_loss_grad(X, y, W1, b1, W2, b2, reg):
    """Loss and gradients of a ReLU network with a softmax output."""
    ...
```

```{.python .tests}
import numpy as np

rng = np.random.default_rng(1)
X, y = rng.normal(size=(5, 3)), np.array([0, 2, 1, 2, 0])
P = {"W1": rng.normal(size=(3, 4)), "b1": rng.normal(size=4) * 0.1,
     "W2": rng.normal(size=(4, 3)), "b2": rng.normal(size=3) * 0.1}


def f(Q):
    return two_layer_loss_grad(X, y, Q["W1"], Q["b1"], Q["W2"], Q["b2"], 0.05)


def test_gradients_match_finite_differences():
    loss, grads = f(P)
    for name in P:
        num = np.zeros_like(P[name])
        for idx in np.ndindex(P[name].shape):
            Qp = {k: v.copy() for k, v in P.items()}
            Qm = {k: v.copy() for k, v in P.items()}
            Qp[name][idx] += 1e-6
            Qm[name][idx] -= 1e-6
            num[idx] = (f(Qp)[0] - f(Qm)[0]) / 2e-6
        assert grads[name].shape == P[name].shape
        assert np.allclose(grads[name], num, atol=1e-5), name


def test_zero_weights_give_log_k():
    Z = {"W1": np.zeros((3, 4)), "b1": np.zeros(4), "W2": np.zeros((4, 3)), "b2": np.zeros(3)}
    assert np.isclose(f(Z)[0], np.log(3))


def test_large_scores_are_stable():
    Q = dict(P)
    Q["b2"] = np.array([1000.0, 0.0, 0.0])
    loss, _ = f(Q)
    assert np.isfinite(loss)
```
:::
