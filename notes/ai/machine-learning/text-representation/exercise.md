::: {#prob-bag-of-words-code .problem .coding origin="adapted" source="res-stanford-cs221-hw-sentiment" packages="numpy"}
Compute bag-of-words features (@def-bag-of-words) for a list of texts. Write `bag_of_words(texts, vocab=None)`.

- Tokenize a text by lower-casing it and splitting it on whitespace.
- If `vocab` is `None`, build it from `texts`: a dict that maps each distinct token to an index, numbered `0, 1, 2, ...` in order of first appearance. Otherwise use the given `vocab` and ignore tokens that are not in it.
- Return the pair `(vocab, X)`, where `X` is a float array of shape `(len(texts), len(vocab))` whose row `i` is the bag-of-words vector of text `i`: entry `v` is the number of tokens of the text with index `v`, divided by the number of tokens of the text that are in `vocab`. A row with no such token is all zeros.

```{.python .starter}
import numpy as np


def bag_of_words(texts, vocab=None):
    """Return (vocab, X): token -> index, and one row of token fractions per text."""
    ...
```

```{.python .tests}
import numpy as np


def test_build_vocab():
    vocab, X = bag_of_words(["Good movie", "bad movie , bad acting"])
    assert vocab == {"good": 0, "movie": 1, "bad": 2, ",": 3, "acting": 4}
    assert X.shape == (2, 5)
    assert np.allclose(X, [[0.5, 0.5, 0, 0, 0], [0, 0.2, 0.4, 0.2, 0.2]])


def test_given_vocab_ignores_unknown_tokens():
    vocab = {"good": 0, "bad": 1}
    v, X = bag_of_words(["GOOD good fun", "nothing known", "bad"], vocab)
    assert v is vocab or v == vocab
    assert np.allclose(X, [[1, 0], [0, 0], [0, 1]])


def test_rows_sum_to_one():
    _, X = bag_of_words(["a b a c", "c c", "  spaced   out  "])
    assert np.allclose(X.sum(axis=1), 1.0)


def test_empty_text():
    vocab, X = bag_of_words(["", "x"])
    assert vocab == {"x": 0} and np.allclose(X, [[0], [1]])
```
:::
