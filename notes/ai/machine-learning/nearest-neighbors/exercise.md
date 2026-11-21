::: {.problem #prob-cs231na-1-q2 origin="external" source="cs231na-1-q2"}
We can also use other distance metrics such as L1 distance.
For pixel values $p_{ij}^{(k)}$ at location $(i,j)$ of some image $I_k$,

the mean $\mu$ across all pixels over all images is $$\mu=\frac{1}{nhw}\sum_{k=1}^n\sum_{i=1}^{h}\sum_{j=1}^{w}p_{ij}^{(k)}$$
And the pixel-wise mean $\mu_{ij}$ across all images is
$$\mu_{ij}=\frac{1}{n}\sum_{k=1}^np_{ij}^{(k)}.$$
The general standard deviation $\sigma$ and pixel-wise standard deviation $\sigma_{ij}$ is defined similarly.

Which of the following preprocessing steps will not change the performance of a Nearest Neighbor classifier that uses L1 distance? Select all that apply. To clarify, both training and test examples are preprocessed in the same way.

1. Subtracting the mean $\mu$ ($\tilde{p}_{ij}^{(k)}=p_{ij}^{(k)}-\mu$.)
2. Subtracting the per pixel mean $\mu_{ij}$  ($\tilde{p}_{ij}^{(k)}=p_{ij}^{(k)}-\mu_{ij}$.)
3. Subtracting the mean $\mu$ and dividing by the standard deviation $\sigma$.
4. Subtracting the pixel-wise mean $\mu_{ij}$ and dividing by the pixel-wise standard deviation $\sigma_{ij}$.
5. Rotating the coordinate axes of the data, which means rotating all the images by the same angle. Empty regions in the image caused by rotation are padded with a same pixel value and no interpolation is performed.
:::

::: {.problem #prob-cs231na-1-q3 origin="external" source="cs231na-1-q3"}
Which of the following statements about $k$-Nearest Neighbor ($k$-NN) are true in a classification setting, and for all $k$? Select all that apply.
1. The decision boundary of the k-NN classifier is linear.
2. The training error of a 1-NN will always be lower than or equal to that of 5-NN.
3. The test error of a 1-NN will always be lower than that of a 5-NN.
4. The time needed to classify a test example with the k-NN classifier grows with the size of the training set.
5. None of the above.
:::

::: {#prob-knn-predict-code .problem .coding origin="adapted" source="res-stanford-cs231n-assignments-ps1" packages="numpy"}
Implement the $k$-nearest neighbour classifier (@def-k-nearest-neighbors) with the $L_2$ distance, without a Python loop over the training or the test points. Write `knn_predict(X_train, y_train, X_test, k)`.

- `X_train` has shape `(N, D)`, `y_train` holds integer labels of shape `(N,)`, `X_test` has shape `(M, D)`.
- Compute all $M\times N$ squared distances at once, using $\lVert\mathbf a-\mathbf b\rVert^2=\lVert\mathbf a\rVert^2-2\,\mathbf a\cdot\mathbf b+\lVert\mathbf b\rVert^2$.
- Return the predicted labels, shape `(M,)`. Among equally distant training points prefer the smaller index; among equally frequent labels prefer the smaller label.

```{.python .starter}
import numpy as np


def knn_predict(X_train, y_train, X_test, k):
    """Labels predicted by k-NN with the L2 distance."""
    ...
```

```{.python .tests}
import numpy as np

X = np.array([[0, 0], [1, 0], [0, 1], [2, 2], [3, 2], [2, 3], [1.2, 1.4]])
y = np.array([0, 0, 0, 1, 1, 1, 1])


def test_seven_points():
    q = np.array([[1.0, 1.0]])
    assert knn_predict(X, y, q, 1).tolist() == [1]
    assert knn_predict(X, y, q, 3).tolist() == [0]
    assert knn_predict(X, y, q, 7).tolist() == [1]


def test_training_points_and_many_queries():
    assert knn_predict(X, y, X, 1).tolist() == y.tolist()
    Q = np.array([[3.0, 3.0], [-1.0, -1.0], [0.5, 0.4]])
    assert knn_predict(X, y, Q, 3).tolist() == [1, 0, 0]


def test_label_tie_goes_to_smaller_label():
    Xt = np.array([[0.0], [2.0]])
    assert knn_predict(Xt, np.array([1, 0]), np.array([[1.0]]), 2).tolist() == [0]
```
:::
