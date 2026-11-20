::: {.problem #prob-camib-las-3-q8 origin="external" source="camib-las-3-q8"}
Prove the Generalised Eigenspace Decomposition Theorem (stated in lectures).

*Note (these notes):* The theorem is @thm-generalized-eigenspace-decomposition: if $m_\alpha(t)=\prod_{i=1}^k(t-\lambda_i)^{c_i}$ with distinct $\lambda_i$, then $V=\bigoplus_i\ker(\alpha-\lambda_i\iota)^{c_i}$. The note proves it with Bézout; the solution gives a second proof.
:::

::: {.problem #prob-camib-las-3-q10 origin="external" source="camib-las-3-q10"}
Let $V$ be a vector space of dimension $n$ and $\alpha$ an endomorphism of $V$ with $\alpha^n = 0$ but $\alpha^{n-1} \ne 0$. Without appealing to Jordan Normal Form, show that there is a vector $y$ such that $(y, \alpha(y), \alpha^2(y), \dots, \alpha^{n-1}(y))$ is a basis for $V$. What is the matrix representation of $\alpha$ with respect to this basis? And the matrix representation of $\alpha^k$, for an arbitrary positive integer $k$?

Show that if $\beta$ is an endomorphism of $V$ which commutes with $\alpha$, then $\beta = p(\alpha)$ for some polynomial $p$. [Hint: consider $\beta(y)$.] What is the form of the matrix for $\beta$ with respect to the above basis?
:::
