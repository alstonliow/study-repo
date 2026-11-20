::: {.problem #prob-camib-las-2-q4 origin="external" source="camib-las-2-q4"}
Let $A$ and $B$ be $n \times n$ matrices over a field $\mathbb{F}$. Show that the $2n \times 2n$ matrix
$$C = \begin{pmatrix} I & -B \\ A & 0 \end{pmatrix} \text{ can be transformed into } D = \begin{pmatrix} I & 0 \\ A & AB \end{pmatrix}$$
by elementary column operations (which you should specify). By considering the determinants of $C$ and $D$, obtain another proof that $\det(AB) = \det(A)\det(B)$.
:::

::: {.problem #prob-camib-las-2-q6 origin="external" source="camib-las-2-q6"}
Let $A$, $B$ be $n \times n$ matrices over the field $\mathbb{F}$, where $n \ge 2$. Show that, if $A$ and $B$ are non-singular, then:
$$(i)\ \operatorname{adj}(AB) = \operatorname{adj}(B)\operatorname{adj}(A), \qquad (ii)\ \det(\operatorname{adj} A) = (\det A)^{n-1}, \qquad (iii)\ \operatorname{adj}(\operatorname{adj} A) = (\det A)^{n-2} A.$$
Show that the rank of the adjugate matrix is
$$\operatorname{rk}(\operatorname{adj} A) = \begin{cases} n & \text{if } \operatorname{rk}(A) = n \\ 1 & \text{if } \operatorname{rk}(A) = n-1 \\ 0 & \text{if } \operatorname{rk}(A) \le n-2. \end{cases}$$
Do (i)-(iii) hold if $A$ is singular? [Hint: for (i) consider $A + \lambda I$ for $\lambda \in \mathbb{F}$.]
:::
