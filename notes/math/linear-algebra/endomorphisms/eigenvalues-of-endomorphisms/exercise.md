::: {.problem #prob-camib-las-2-q5 origin="external" source="camib-las-2-q5"}
Let $\alpha : V \to V$ be a linear map on a real finite dimensional vector space $V$ with $\operatorname{tr}(\alpha) = 0$.

(i) Show that, if $\alpha \ne 0$, there is a vector $\mathbf{v}$ with $\mathbf{v}, \alpha(\mathbf{v})$ linearly independent. Deduce that there is a basis for $V$ relative to which $\alpha$ is represented by a matrix $A$ with all of its diagonal entries equal to $0$.

(ii) Show that there are endomorphisms $\beta, \gamma$ of $V$ with $\alpha = \beta\gamma - \gamma\beta$.
:::

::: {.problem #prob-camib-las-3-q4 origin="external" source="camib-las-3-q4"}
Let $\alpha$ be an endomorphism of a complex vector space $V$. Show that if $\lambda$ is an eigenvalue for $\alpha$ then $\lambda^2$ is an eigenvalue for $\alpha^2$. Show further that every eigenvalue of $\alpha^2$ arises in this way. Are the eigenspaces $\operatorname{Ker}(\alpha - \lambda\,\mathrm{id}_V)$ and $\operatorname{Ker}(\alpha^2 - \lambda^2\,\mathrm{id}_V)$ necessarily the same?
:::

::: {.problem #prob-camib-las-3-q12 origin="external" source="camib-las-3-q12"}
Let $C$ be an $n \times n$ matrix over $\mathbb{C}$, and write $C = A + iB$, where $A$ and $B$ are real $n \times n$ matrices. By considering $\det(A + \lambda B)$ as a function of $\lambda$, show that if $C$ is invertible then there exists a real number $\lambda$ such that $A + \lambda B$ is invertible. Deduce that if two $n \times n$ real matrices $P$ and $Q$ are similar when regarded as matrices over $\mathbb{C}$, then they are similar as matrices over $\mathbb{R}$.
:::

::: {.problem #prob-camib-las-3-q13 origin="external" source="camib-las-3-q13"}
Let $f(x) = a_0 + a_1x + \dots + a_nx^n$, with $a_i \in \mathbb{C}$, and let $C$ be the *circulant* matrix
$$\begin{pmatrix} a_0 & a_1 & a_2 & \dots & a_n \\ a_n & a_0 & a_1 & \dots & a_{n-1} \\ a_{n-1} & a_n & a_0 & \dots & a_{n-2} \\ \vdots & & & \ddots & \vdots \\ a_1 & a_2 & a_3 & \dots & a_0 \end{pmatrix}.$$
Show that the determinant of $C$ is $\det C = \prod_{j=0}^n f(\zeta^j)$, where $\zeta = \exp(2\pi i/(n+1))$.
:::
