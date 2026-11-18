<!-- Added 2026-11-18 for Stanford CS221 Lecture 1 (einops). The first block is our own NumPy code; the second is the lecture's einops code with torch.ones replaced by np.ones (MIT licence, see NOTICES.md). -->

::: {#exm-einsum-code-1 .example name="Einsum in NumPy" origin="self"}

Needs NumPy. `np.einsum` writes each input's axes as letters; letters missing after `->` are summed over.

```{.python .runnable packages="numpy"}
import numpy as np
x = np.arange(6.0).reshape(2, 3)
y = np.arange(12.0).reshape(3, 4)
print(np.allclose(np.einsum("ij,jk->ik", x, y), x @ y))
print(np.einsum("ij->ji", x).shape, np.einsum("ij->", x))
s = np.arange(9.0).reshape(3, 3)
print(np.einsum("ii->", s), np.trace(s))
u = np.ones((2, 3, 4)); v = np.ones((2, 5, 4))
print(np.einsum("bik,bjk->bij", u, v).shape)
```

```text
True
(3, 2) 15.0
12.0 12.0
(2, 3, 5)
```

:::

::: {#exm-einsum-code-2 .example name="einops: einsum, reduce, rearrange" origin="adapted" source="cs221-1"}

Needs NumPy and einops. The heads example (@exm-einsum-heads) with named axes.

```{.python .runnable packages="numpy,einops"}
# Adapted from the CS221 lecture code: torch.ones replaced by np.ones, prints added.
import numpy as np
from einops import einsum, reduce, rearrange

x = np.ones((2, 3, 4))  # batch seq1 hidden
y = np.ones((2, 3, 4))  # batch seq2 hidden
z = einsum(x, y, "batch seq1 hidden, batch seq2 hidden -> batch seq1 seq2")
print(z.shape)

s = reduce(x, "... hidden -> ...", "sum")
print(s.shape)

x = np.ones((3, 8))  # seq total_hidden
w = np.ones((4, 4))  # hidden1 hidden2
x = rearrange(x, "... (heads hidden1) -> ... heads hidden1", heads=2)
x = einsum(x, w, "... hidden1, hidden1 hidden2 -> ... hidden2")
x = rearrange(x, "... heads hidden2 -> ... (heads hidden2)")
print(x.shape)
```

```text
(2, 3, 3)
(2, 3)
(3, 8)
```

:::
