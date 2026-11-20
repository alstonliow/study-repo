<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-ats-4-q13" status="draft"}
(a) $\det$ is a polynomial in the entries, hence continuous, and $GL_n(\mathbb{R}) = \det^{-1}(\mathbb{R}\setminus\{0\})$ is the preimage of an open set.

(b)

1. Expanding the determinant, $\det(I + K) = 1 + \operatorname{tr}K + R(K)$, where $R$ is a sum of products of at least two entries of $K$, so $|R(K)| \le C\|K\|^2$ for $\|K\| \le 1$.

2. For $A$ invertible, $\det(A + H) = \det A\,\det(I + A^{-1}H) = \det A + \det A\operatorname{tr}(A^{-1}H) + \det A\,R(A^{-1}H)$, and the last term is $O(\|H\|^2)$. So $D\det|_A(H) = \det A\operatorname{tr}(A^{-1}H)$.

(c)

1. For $A = I + K$ near $I$, $\det A\cdot A^{-1} = \operatorname{adj}(A)$, so $D\det|_{I+K}(H) = \operatorname{tr}(\operatorname{adj}(I+K)H)$.

2. $(I + K)^{-1} = I - K + O(\|K\|^2)$ (Neumann series) and $\det(I + K) = 1 + \operatorname{tr}K + O(\|K\|^2)$, so $\operatorname{adj}(I + K) = I + (\operatorname{tr}K)I - K + O(\|K\|^2)$.

3. Hence $D\det|_{I+K}(H) = \operatorname{tr}H + \operatorname{tr}K\operatorname{tr}H - \operatorname{tr}(KH) + O(\|K\|^2)\|H\|$. So $A \mapsto D\det|_A$ is differentiable at $I$, and
$$D^2\det|_I(K,H) = \operatorname{tr}K\operatorname{tr}H - \operatorname{tr}(KH),$$
a symmetric bilinear map. (Checked symbolically for a sample pair of $3\times3$ matrices.)
:::
