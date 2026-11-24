::: {.problem #prob-mit1803ps-35-q1 origin="external" source="mit1803ps-35-q1"}
[Exponential matrix]

(a) We have seen that a complex number $z = a + bi$ determines a matrix $A(z)$ in the following way: $A(a + bi) = \begin{pmatrix}a&-b\\b&a\end{pmatrix}$. This matrix represents the operation of multiplication by $z$, in the sense that if $z(x + yi) = v + wi$ then $A(z)\begin{pmatrix}x\\y\end{pmatrix} = \begin{pmatrix}v\\w\end{pmatrix}$. What is $e^{A(z)t}$? What is $A(e^{zt})$?

(b) Say that a pair of solutions $x_1(t)$, $x_2(t)$ of the equation $m\ddot x + b\dot x + kx = 0$ is normalized at $t = 0$ if:
$$x_1(0) = 1,\quad \dot x_1(0) = 0;\qquad x_2(0) = 0,\quad \dot x_2(0) = 1 .$$
For example, find the normalized pair of solutions to $\ddot x + 2\dot x + 2x = 0$. Then find $e^{At}$ where $A$ is the companion matrix for the operator $D^2 + 2D + 2I$.

(c) Suppose that $e^{3t}\begin{pmatrix}1\\1\end{pmatrix}$ and $e^{2t}\begin{pmatrix}1\\2\end{pmatrix}$ satisfy the equation $\dot u = Au$.

(i) Find solutions $u_1(t)$ and $u_2(t)$ such that $u_1(0) = \begin{pmatrix}1\\0\end{pmatrix}$ and $u_2(0) = \begin{pmatrix}0\\1\end{pmatrix}$.

(ii) Find $e^{At}$.

(iii) Find $A$.
:::
