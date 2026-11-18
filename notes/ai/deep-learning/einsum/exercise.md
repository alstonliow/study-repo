::: {.problem #prob-cs221hw-1-q1 origin="external" source="cs221hw-1-q1"}
(a) **Linear Algebra Complexity:** Suppose you have two matrices $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{n \times p}$. What is the time complexity of computing their product $AB$ using the standard matrix multiplication algorithm? Express your answer using big-O notation and briefly justify why.

*Expected:* The time complexity in big-O notation and a 1-2 sentence explanation.

(b) **Einstein Summation (Written):** Given $X \in \mathbb R^{n\times d}$ and $\mathbf w \in \mathbb R^d$: (i) Write an `einsum` string for $X\mathbf w$; (ii) for the pairwise dot-product matrix $XX^\top$; (iii) for $\operatorname{diag}(X^\top X)$ (column-wise squared norms). For each string, briefly explain why it computes the requested quantity.

*Expected:* Use the `einops` format (e.g., `'n d, d m -> n m'`) rather than the `np.einsum` format (e.g., `'nd, dm -> nm'`).

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::
