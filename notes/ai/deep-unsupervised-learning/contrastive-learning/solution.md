<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs231na-3-q4" status="draft"}
1. CLIP's loss is a classification over the batch: each image must pick its own caption among the $N$ captions in the minibatch, and vice versa (@def-clip). The other $N-1$ pairs are the negatives. With a small batch the task is easy, since few and mostly unrelated negatives are enough to tell apart, so the loss gives little pressure to learn fine distinctions; the best achievable loss itself depends on the number of negatives (@prp-nt-xent-batch-size). Larger batches supply more, and harder, negatives per step.
2. With a fixed batch size one can enlarge the set of negatives without enlarging the batch: keep a queue (memory bank) of embeddings from recent batches and use them as extra negatives, computed by a slowly updated momentum copy of the encoder so that they stay consistent (as in MoCo); or mine hard negatives; or switch to an objective that needs no negatives, such as the self-distillation of DINO (@def-dino).
:::

::: {.solution for="prob-cs231na-3-q5" status="draft"}
1. Give each modality (image, text, audio, depth, ...) its own encoder, all mapping into one shared embedding space with normalized vectors.
2. For every pair of modalities that occur together in the data, add a symmetric contrastive loss of the CLIP form (@def-clip) between their embeddings, and train on the sum of these losses.
3. Paired data for all modalities at once is rare, so one modality can serve as a hub: pair every other modality with images only. Alignment to the hub then makes, for example, audio and text embeddings comparable even though they were never paired directly.
:::

::: {.solution for="prob-cs231na-3-q8" status="draft"}
**Expected:** worse with CLIP than with DINO.

1. Segmentation needs patch features that say what is at each location and where object boundaries are.
2. CLIP is trained only to align a global image embedding with a caption (@def-clip); nothing in its loss rewards the individual patch features for being locally meaningful, so the spatial information in them is weak.
3. DINO matches the outputs of small local crops to those of large global crops of the same image (@def-dino), which forces the features of parts to be consistent with the whole; its patch features separate objects, parts and background (@sec-ai-deep-unsupervised-learning-contrastive-learning). A segmentation head on DINO's patch features therefore has more to work with.
:::

::: {.solution for="prob-nt-xent-code" status="draft"}
```{.python}
import numpy as np


def nt_xent_loss(z, tau):
    """SimCLR contrastive loss of 2N projected views."""
    n2 = z.shape[0]
    N = n2 // 2
    u = z / np.linalg.norm(z, axis=1, keepdims=True)
    S = u @ u.T / tau
    np.fill_diagonal(S, -np.inf)
    S = S - S.max(axis=1, keepdims=True)
    log_den = np.log(np.exp(S).sum(axis=1))
    pos = S[np.arange(n2), (np.arange(n2) + N) % n2]
    return float(np.mean(log_den - pos))
```

1. Setting the diagonal to $-\infty$ removes $k=i$ from each denominator.
2. Each row is a log-softmax; subtracting the row maximum first keeps the exponentials finite (@prp-softmax-shift).
3. The partner of row $i$ is row $(i+N)\bmod 2N$, and the mean over all $2N$ rows is $L$.
:::
