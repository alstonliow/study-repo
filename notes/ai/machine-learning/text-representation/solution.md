<!-- Solutions marked status="draft" were written by Claude in our own words,
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-bag-of-words-code" status="draft"}
```{.python}
import numpy as np


def bag_of_words(texts, vocab=None):
    """Return (vocab, X): token -> index, and one row of token fractions per text."""
    tokens = [t.lower().split() for t in texts]
    if vocab is None:
        vocab = {}
        for ts in tokens:
            for t in ts:
                vocab.setdefault(t, len(vocab))
    X = np.zeros((len(texts), len(vocab)))
    for i, ts in enumerate(tokens):
        known = [vocab[t] for t in ts if t in vocab]
        for v in known:
            X[i, v] += 1
        if known:
            X[i] /= len(known)
    return vocab, X
```

1. `setdefault(t, len(vocab))` gives a new token the next free index and leaves a known token alone, which numbers tokens in order of first appearance.
2. Each row first counts tokens and then divides by the number of known tokens, so it is the average of their one-hot vectors.
3. `split()` with no argument splits on any run of whitespace and drops empty strings, so an empty text has no tokens and a zero row.
:::
