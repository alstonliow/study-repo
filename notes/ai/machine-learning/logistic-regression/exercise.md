::: {.problem #prob-cs188d-11-q1 origin="external" source="cs188d-11-q1"}
**Optimization.** We would like to classify some data. We have $N$ samples, where each sample consists of a feature vector $\mathbf x=[x_1,\cdots,x_k]^T$ and a label $y\in\{0,1\}$.

Logistic regression produces predictions as follows:
$$
P(Y=1\mid X)=h(\mathbf x)=s\Bigl(\sum_iw_ix_i\Bigr)=\frac{1}{1+\exp\bigl(-(\sum_iw_ix_i)\bigr)}\qquad s(\gamma)=\frac{1}{1+\exp(-\gamma)}
$$
where $s(\gamma)$ is the logistic function, $\exp x=e^x$, and $\mathbf w=[w_1,\cdots,w_k]^T$ are the learned weights.

Let's find the weights $w_j$ for logistic regression using stochastic gradient descent. We would like to minimize the following loss function (called the cross-entropy loss) for each sample:
$$
L=-[y\ln h(\mathbf x)+(1-y)\ln(1-h(\mathbf x))]
$$

(a) Show that $s'(\gamma)=s(\gamma)(1-s(\gamma))$

(b) Find $\frac{dL}{dw_j}$. Use the fact from the previous part.

(c) Now, find a simple expression for $\nabla_{\mathbf w}L=[\frac{dL}{dw_1},\frac{dL}{dw_2},\dots,\frac{dL}{dw_k}]^T$

(d) Write the stochastic gradient descent update for $\mathbf w$. Our step size is $\eta$.
:::
