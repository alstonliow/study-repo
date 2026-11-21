::: {.problem #prob-cs231na-3-q4 origin="external" source="cs231na-3-q4"}
Why does CLIP's learning depend on the batch size? If the batch size is fixed, what strategy can we use to learn rich image features?
:::

::: {.problem #prob-cs231na-3-q5 origin="external" source="cs231na-3-q5"}
CLIP learns to align image and text representations in a shared latent space using a contrastive loss. How would you extend this idea to more than two modalities?
:::

::: {.problem #prob-cs231na-3-q8 origin="external" source="cs231na-3-q8"}
If you train a segmentation model on CLIP ViT's patch features, do you expect it to perform better or worse than DINO? Why should that be the case?
:::

::: {#prob-nt-xent-code .problem .coding origin="adapted" source="res-stanford-cs231n-assignments-ps3" packages="numpy"}
Write `nt_xent_loss(z, tau)` for the SimCLR loss of @def-simclr. `z` has shape `(2N, d)`: rows $k$ and $k+N$ (0-based, $k<N$) are the two views of image $k$. Return the scalar $L$, using cosine similarities (@def-cosine-similarity) and no Python loop over the examples.

```{.python .starter}
import numpy as np


def nt_xent_loss(z, tau):
    """SimCLR contrastive loss of 2N projected views."""
    ...
```

```{.python .tests}
import numpy as np


def slow(z, tau):
    n2 = z.shape[0]
    N = n2 // 2
    u = z / np.linalg.norm(z, axis=1, keepdims=True)
    S = u @ u.T / tau
    total = 0.0
    for i in range(n2):
        j = (i + N) % n2
        den = sum(np.exp(S[i, k]) for k in range(n2) if k != i)
        total += -np.log(np.exp(S[i, j]) / den)
    return total / n2


def test_matches_definition():
    rng = np.random.default_rng(9)
    z = rng.normal(size=(6, 4))
    assert np.isclose(nt_xent_loss(z, 0.5), slow(z, 0.5))


def test_scale_invariance_and_lower_bound():
    rng = np.random.default_rng(10)
    z = rng.normal(size=(8, 3))
    assert np.isclose(nt_xent_loss(z, 0.2), nt_xent_loss(5 * z, 0.2))
    tau, N = 0.2, 4
    assert nt_xent_loss(z, tau) >= np.log(1 + (2 * N - 2) * np.exp(-2 / tau)) - 1e-12


def test_perfect_pairs_two_images():
    # views of image 0 point one way, views of image 1 the opposite way
    z = np.array([[1.0, 0.0], [-1.0, 0.0], [2.0, 0.0], [-3.0, 0.0]])
    tau = 0.5
    expected = -np.log(np.exp(2.0) / (np.exp(2.0) + 2 * np.exp(-2.0)))
    assert np.isclose(nt_xent_loss(z, tau), expected)
```
:::
