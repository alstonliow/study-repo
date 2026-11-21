::: {.problem #prob-cs231na-3-q2 origin="external" source="cs231na-3-q2"}
Despite their recent success in large-scale image recognition tasks, ViTs often lag behind traditional CNNs when trained on smaller datasets. What underlying factor contribute to this performance gap? What techniques can be used to improve the performance of ViTs on small datasets?
:::

::: {.problem #prob-cs231na-3-q3 origin="external" source="cs231na-3-q3"}
How does the computational cost of the self-attention layers in a ViT change if we independently make the following changes? Please ignore the computation cost of QKV and output projection.

(i) Double the hidden dimension.
(ii) Double the height and width of the input image.
(iii) Double the patch size.
(iv) Double the number of layers.
:::

::: {#prob-patchify-code .problem .coding origin="adapted" source="res-stanford-cs231n-assignments-ps3" packages="numpy"}
Write `patchify(images, P)` for the first step of the patch embedding of @def-patch-embedding: turn images of shape `(N, C, H, W)` ($P$ divides $H$ and $W$) into an array of shape `(N, HW/P**2, C*P*P)`. Patches are numbered row by row (left to right, then top to bottom), and each patch is flattened in the order channel, then row, then column within the patch (that is, like `images[n, :, rows, cols].reshape(-1)`). Use reshapes and transposes, not loops.

```{.python .starter}
import numpy as np


def patchify(images, P):
    """Cut images into flattened P-by-P patches, shape (N, number of patches, C*P*P)."""
    ...
```

```{.python .tests}
import numpy as np


def test_shapes_and_order():
    rng = np.random.default_rng(8)
    x = rng.normal(size=(2, 3, 8, 12))
    p = patchify(x, 4)
    assert p.shape == (2, 6, 48)
    # patch 4 is the second patch of the second patch row: rows 4..7, columns 4..7
    assert np.allclose(p[1, 4], x[1, :, 4:8, 4:8].reshape(-1))
    assert np.allclose(p[0, 0], x[0, :, 0:4, 0:4].reshape(-1))


def test_patch_size_one_and_whole_image():
    x = np.arange(2 * 2 * 3, dtype=float).reshape(1, 2, 2, 3)
    assert np.allclose(patchify(x, 1)[0, 5], x[0, :, 1, 2])
    y = np.arange(16.0).reshape(1, 1, 4, 4)
    assert np.allclose(patchify(y, 4), y.reshape(1, 1, 16))
```
:::
