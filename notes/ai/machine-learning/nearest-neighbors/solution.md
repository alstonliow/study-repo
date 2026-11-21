<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs231na-1-q2" status="draft"}
**Answer:** 1, 2 and 3.

1. Subtracting $\mu$ or the per-pixel mean $\mu_{ij}$ subtracts the same number from a given pixel position in every image, so every difference $p^{(k)}_{ij}-p^{(l)}_{ij}$, and hence every $L_1$ distance, is unchanged (@prp-knn-invariance, item 1).
2. Subtracting $\mu$ and dividing by one $\sigma>0$ multiplies every $L_1$ distance by $1/\sigma$. The order of the distances from a test image to the training images is unchanged, so the neighbours and the predictions are unchanged (item 2).
3. Dividing by the pixel-wise $\sigma_{ij}$ weights the pixel positions differently, and the order of distances can change: with two pixels, $\sigma_{11}=1$, $\sigma_{12}=10$, a test image $(0,0)$ and training images $(1,0)$ and $(0,2)$, the nearest training image changes from $(1,0)$ to $(0,2)$ (the counterexample in the proof of @prp-knn-invariance). So 4 can change the performance.
4. Rotating the coordinate axes is an orthogonal map of $\mathbb{R}^D$. It preserves $L_2$ distances but not $L_1$ distances, whose ratios can change by different factors for different pairs (item 3 of @prp-knn-invariance), so 5 can change the performance of the $L_1$ classifier.
:::

::: {.solution for="prob-cs231na-1-q3" status="draft"}
**Answer:** 2 and 4.

1. False. With $k=1$ the decision boundary consists of pieces of the perpendicular bisectors between training points of different classes (a union of Voronoi cell boundaries). It is piecewise linear, not a single hyperplane: the seven points of @exm-knn-seven-points cannot be separated by one line in the way the 1-NN rule separates them.
2. True. Each training point is at distance $0$ from itself, so with distinct training inputs it is its own nearest neighbour and $1$-NN has zero training error (@prp-knn-cost); a $5$-NN classifier can only do as well or worse. (With duplicate inputs carrying different labels both can err, but $1$-NN still errs no more often under the same tie-breaking.)
3. False. $1$-NN fits label noise and often has higher test error than $5$-NN; which is better depends on the data, and $k$ is chosen by validation.
4. True. Classifying one example computes its distance to all $N$ training points, $O(ND)$ time (@prp-knn-cost).
5. False, since 2 and 4 hold.
:::

::: {.solution for="prob-knn-predict-code" status="draft"}
```{.python}
import numpy as np


def knn_predict(X_train, y_train, X_test, k):
    """Labels predicted by k-NN with the L2 distance."""
    d2 = (np.sum(X_test**2, axis=1)[:, None] - 2 * X_test @ X_train.T
          + np.sum(X_train**2, axis=1)[None, :])
    nearest = np.argsort(d2, axis=1, kind="stable")[:, :k]
    labels = y_train[nearest]
    K = int(y_train.max()) + 1
    counts = np.stack([(labels == c).sum(axis=1) for c in range(K)], axis=1)
    return np.argmax(counts, axis=1)
```

1. The expansion of the squared distance turns the $M\times N$ distance matrix into one matrix product plus two broadcast vectors of squared norms (@def-broadcasting).
2. A stable sort keeps the smaller index first among equal distances; the first $k$ columns are the neighbours.
3. Counting each label per row and taking `argmax`, which returns the first maximum, prefers the smaller label on ties.
:::
