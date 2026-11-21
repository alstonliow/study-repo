<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs231na-2-q3" status="draft"}
**Answer:** 3 is analogous to batch normalization, 2 to layer normalization.

1. Batch normalization normalizes each feature using statistics computed across the examples of the batch (@def-batch-normalization). Subtracting the mean image of the dataset (step 3) does the same for each pixel position, using statistics computed across images.
2. Layer normalization normalizes each example using statistics computed across its own features (@def-layer-normalization). Scaling each image so that the values of all its pixels sum to $1$ (step 2) uses one statistic of the whole image, computed within that image alone.
3. Step 1 uses a separate statistic for each row of each image, a normalization over groups of features (closer to group normalization), and step 4 is a non-linear thresholding; neither matches.
:::

::: {.solution for="prob-cs231na-2-q4" status="draft"}
**Answer:** 2.

1. Layer normalization estimates a mean and a variance from the $D$ features of a single example. With few features these estimates are very noisy, and the normalization distorts the representation: for $D=2$, any two unequal values are mapped to $\pm1$ (when $\varepsilon=0$), whatever they were. So it works poorly when the feature dimension is very small.
2. Depth is not a problem: layer normalization is used in very deep transformers precisely to keep training stable (@def-transformer-block).
3. A high regularization strength does not interact specially with layer normalization; the normalized outputs do not depend on the scale of the previous weights (as in @prp-batch-normalization-scale), so a strong penalty is not the issue.
:::

::: {.solution for="prob-batchnorm-backward-code" status="draft"}
```{.python}
import numpy as np


def batchnorm_backward(dout, x, gamma, eps=1e-5):
    """Gradients of training-mode batch normalization."""
    N = x.shape[0]
    s = np.sqrt(x.var(axis=0) + eps)
    xh = (x - x.mean(axis=0)) / s
    dbeta = dout.sum(axis=0)
    dgamma = (dout * xh).sum(axis=0)
    dx = gamma / (N * s) * (N * dout - dbeta - xh * dgamma)
    return dx, dgamma, dbeta
```

1. With $g_i$ the upstream gradient, $\sum_kg_k$ is `dbeta` and $\sum_kg_k\hat x_k$ is `dgamma`, so @thm-batch-normalization-backward needs no further sums.
2. A constant upstream gradient is the direction the normalization removes: the mean of $N g_i$ equals $\sum_kg_k$ and $\sum_k\hat x_k=0$, so `dx` is zero.
:::
