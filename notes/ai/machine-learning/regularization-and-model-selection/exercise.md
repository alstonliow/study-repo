::: {.problem #prob-camii-sms-2-q2 origin="external" source="camii-sms-2-q2"}
Show that the solution to the ridge regression problem
$$\hat\beta_\lambda=\operatorname*{arg\,min}_\beta\|Y-X\beta\|^2+\lambda\|\beta\|^2$$
is given by $\hat\beta_\lambda=(X^{\mathsf T}X+\lambda I)^{-1}X^{\mathsf T}Y$. Try to prove this result using two methods: (1) Matrix derivatives; (2) Treating ridge regression as solving the least squares problem for the following expanded design matrix and responses:
$$\tilde X=\begin{pmatrix}X\\\sqrt\lambda I_p\end{pmatrix},\qquad\tilde Y=\begin{pmatrix}Y\\0\end{pmatrix}.$$

*Note (these notes):* Sheet notation: $X$ is an $n\times p$ design matrix of full column rank, $P$ the orthogonal projection onto its column space, $X_0$ the first $p_0<p$ columns of $X$ and $P_0$ the orthogonal projection onto the column space of $X_0$; $Y\in\mathbb R^n$, $\hat\beta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y$, $\hat\beta_0=(X_0^{\mathsf T}X_0)^{-1}X_0^{\mathsf T}Y$, $\hat\sigma^2=\|(I-P)Y\|^2/(n-p)$. The normal linear model is $Y=X\beta+\varepsilon$, $\varepsilon\mid X\sim N_n(0,\sigma^2I)$.
:::
