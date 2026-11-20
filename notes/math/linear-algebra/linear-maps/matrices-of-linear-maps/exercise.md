::: {.problem #prob-camib-las-1-q10 origin="external" source="camib-las-1-q10"}
Let $Y$ and $Z$ be subspaces of the finite dimensional $\mathbb{F}$-vector spaces $V$ and $W$, respectively. Suppose that $\alpha\colon V \to W$ is a linear map such that $\alpha(Y) \subseteq Z$.

(i) Show that $\alpha$ induces well-defined linear maps $\alpha|_Y\colon Y \to Z$ via $\alpha|_Y(y) = \alpha(y)$ and $\overline{\alpha}\colon V/Y \to W/Z$ via $\overline{\alpha}(v + Y) = \alpha(v) + Z$.

Consider a basis $\mathcal{B}_V = \{v_1, \dots, v_n\}$ for $V$ containing a basis $\mathcal{B}_Y = \{v_1, \dots, v_k\}$ for $Y$ and a basis $\mathcal{B}_W = \{w_1, \dots, w_m\}$ for $W$ containing a basis $\mathcal{B}_Z = \{w_1, \dots, w_l\}$ for $Z$. Recall from lectures that $\mathcal{B}_{V/Y} = \{v_{k+1} + Y, \dots, v_n + Y\}$ is a basis for $V/Y$ and that $\mathcal{B}_{W/Z} = \{w_{l+1} + Z, \dots, w_m + Zv\}$ is a basis for $W/Z$.

(ii) Describe the relationship between the three matrices:
$$A = [\alpha]^{\mathcal{B}_V}_{\mathcal{B}_W} \in \mathcal{M}_{m\times n}(\mathbb{F});\quad B = [\alpha|_Y]^{\mathcal{B}_Y}_{\mathcal{B}_Z} \in \mathcal{M}_{l\times k}(\mathbb{F}) \quad\text{and}\quad C = [\overline{\alpha}]^{\mathcal{B}_{V/Y}}_{\mathcal{B}_{W/Z}} \in \mathcal{M}_{(m-l)\times(n-k)}(\mathbb{F}).$$

(iii) Show that $R = \{\beta \in \mathcal{L}(V, W) : \beta(Y) \le Z\}$ is a subspace of the space $\mathcal{L}(V, W)$ of all linear maps from $V$ to $W$. What is the dimension of $R$?

*Note (these notes):* "$w_m + Zv$" is printed so on the sheet; $w_m + Z$ is meant.
:::
