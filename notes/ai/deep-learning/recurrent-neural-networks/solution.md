<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs231na-2-q7" status="draft"}
*Advantage.* The vocabulary is tiny (letters, digits, punctuation: tens of symbols instead of thousands of words), so the embedding matrix and the output layer, which dominate the parameter count of a word-level model, become small. The model also has no out-of-vocabulary problem: it can spell rare or new words.

*Disadvantage.* Captions become several times longer as sequences (about five characters per word). The RNN needs more steps per caption, so training and sampling are slower, and dependencies between words now span many more steps, which makes them harder to learn because gradients vanish over long spans (@thm-rnn-gradient-flow). The model must also spend capacity learning to spell, and it can produce non-words.
:::

::: {.solution for="prob-rnn-bptt-code" status="draft"}
```{.python}
import numpy as np


def rnn_bptt(x, h0, Wx, Wh, b, dh):
    """Forward pass of a vanilla RNN, then gradients by backpropagation through time."""
    T = x.shape[0]
    hs = [h0]
    for t in range(T):
        hs.append(np.tanh(x[t] @ Wx + hs[-1] @ Wh + b))
    dx, dWx, dWh, db = np.zeros_like(x), np.zeros_like(Wx), np.zeros_like(Wh), np.zeros_like(b)
    carry = np.zeros_like(h0)
    for t in range(T - 1, -1, -1):
        a = (1 - hs[t + 1] ** 2) * (dh[t] + carry)
        dx[t] = a @ Wx.T
        dWx += np.outer(x[t], a)
        dWh += np.outer(hs[t], a)
        db += a
        carry = a @ Wh.T
    return dx, carry, dWx, dWh, db
```

1. The backward loop is the algorithm of @def-bptt in row-vector form: `carry` is the gradient reaching $\mathbf h_t$ from step $t+1$, added to the output gradient `dh[t]`.
2. After the last iteration `carry` is the gradient on $\mathbf h_0$.
3. In the scalar test, $\partial h_4/\partial x_1=(1-h_1^2)\,\partial h_4/\partial h_1$, and $\partial h_4/\partial h_1\approx0.104$ as in @exm-rnn-gradient-flow.
:::
