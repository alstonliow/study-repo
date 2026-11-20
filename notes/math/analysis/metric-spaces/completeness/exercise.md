::: {.problem #prob-camib-ats-2-q5 origin="external" source="camib-ats-2-q5"}
For each $k \in \mathbb{N}_0$, define the metric space $C^k([a,b])$ as the space of $k$ times continuously differentiable real-valued functions on $[a,b]$ endowed with the metric
$$d_{C^k}(f,g) = \sum_{j=0}^k\sup_{x\in[a,b]}\left|\frac{d^jf}{dx^j}(x) - \frac{d^jg}{dx^j}(x)\right|.$$

(a) Show that $C^k([a,b])$ is a complete metric space.

(b) Show that the map $f \mapsto \int_a^x f(y)\,dy$ is a continuous map from $C^k([a,b])$ to $C^{k+1}([a,b])$.

(c) Show that the map $f \mapsto f'$ is a continuous map from $C^{k+1}([a,b])$ to $C^k([a,b])$.
:::

::: {.problem #prob-camib-ats-2-q8 origin="external" source="camib-ats-2-q8"}
In this question we consider spaces of real sequences.

(a) Justify that the metric space $\ell^\infty$, of bounded real sequences and equipped with metric $d((x_n),(y_n)) = \sup_{n\in\mathbb{N}}|x_n - y_n|$, is complete.

(b) Consider the space $\ell^2 = \{(x_n) \in \mathbb{R}^{\mathbb{N}} \mid \sum x_n^2 \text{ converges}\}$ with
$$d((x_n),(y_n)) = \sqrt{\sum_{n=1}^\infty(x_n - y_n)^2}.$$
Show that $d$ is a well-defined metric on $\ell^2$ and that $(\ell^2, d)$ is complete.
:::
