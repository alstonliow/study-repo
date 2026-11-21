<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs231na-3-q2" status="draft"}
*Factor.* A ViT has much weaker inductive biases than a CNN (@sec-ai-deep-learning-vision-transformers). A convolutional network assumes locality and translation equivariance through small shared filters, which are right for images and need not be learnt. A ViT lets every patch attend to every other from the first layer and must learn from the data that nearby patches matter and that the same pattern can appear anywhere; with little data it overfits instead.

*Remedies.* Pretrain on a large dataset (with labels or self-supervised, @sec-ai-unsupervised-learning-contrastive-learning) and fine-tune; use strong data augmentation and regularization (random crops, mixing of images, stochastic depth, weight decay); distil from a CNN teacher; build in locality with a convolutional stem, smaller patches or local attention windows.
:::

::: {.solution for="prob-cs231na-3-q3" status="draft"}
The self-attention cost is $\Theta(LN^2d)$ with $N=HW/P^2$ tokens of width $d$ and $L$ layers (@prp-vit-attention-cost).

1. (i) Doubling $d$ doubles the cost.
2. (ii) Doubling $H$ and $W$ multiplies $N$ by $4$, so the cost by $16$.
3. (iii) Doubling $P$ divides $N$ by $4$, so the cost by $16$.
4. (iv) Doubling $L$ doubles the cost.
:::

::: {.solution for="prob-patchify-code" status="draft"}
```{.python}
import numpy as np


def patchify(images, P):
    """Cut images into flattened P-by-P patches, shape (N, number of patches, C*P*P)."""
    N, C, H, W = images.shape
    x = images.reshape(N, C, H // P, P, W // P, P)
    x = x.transpose(0, 2, 4, 1, 3, 5)          # N, patch row, patch column, C, row, column
    return x.reshape(N, (H // P) * (W // P), C * P * P)
```

1. Splitting the height into (patch row, row within the patch) and the width likewise is a reshape that moves no data.
2. Moving the patch indices before the channel puts all entries of one patch together in the order channel, row, column; the final reshape merges the patch indices row by row (@def-rearrange).
:::
