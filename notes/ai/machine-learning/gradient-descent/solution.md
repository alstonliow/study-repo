<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs221hw-1-q3" status="draft"}
1. Derivative: $f'(\theta)=2\sum_i w_i(\theta-x_i)=2\big(\theta\sum_i w_i-\sum_i w_ix_i\big)$.
2. Setting $f'(\theta)=0$ gives the weighted mean
$$\theta^*=\frac{\sum_{i=1}^n w_ix_i}{\sum_{i=1}^n w_i}.$$
3. Minimum: $f''(\theta)=2\sum_i w_i>0$ because every $w_i>0$. So $f$ is strictly convex and $\theta^*$ is its unique global minimum.
4. Negative weights: if $\sum_i w_i<0$, then $f''<0$, $f$ is a downward parabola, $\theta^*$ is a maximum and $f(\theta)\to-\infty$ as $|\theta|\to\infty$, so there is no minimum. If $\sum_i w_i=0$, $f$ is linear (or constant) and $\theta^*$ is undefined, with again no minimum unless $\sum_i w_ix_i=0$. Even when $\sum_i w_i>0$, a negative weight pushes $\theta^*$ away from that point, and $\theta^*$ can fall outside the range of the $x_i$.
:::

::: {.solution for="prob-cs188hw-10-q1" status="draft"}
1. **A, C and D.** Gradient ascent (@def-gradient-descent with the sign reversed) steps along the gradient, perpendicular to the contour through the current point, by $\alpha$ times its length. A shows small steps of shrinking length following the gradient to the maximum. C is a too-large rate in the steep direction: each step overshoots across the narrow axis of the ellipses, but by less each time, so the zigzag converges. D is a still larger rate: the overshoot grows and the iterates diverge. B moves *along* contours, around the maximum, never uphill; no gradient step does that.
2. **The first two.** Perturbing a converged solution and climbing again (a basin-hopping restart) and running from many starting points both explore several basins and keep the best local maximum found (@def-hill-climbing, random restarts). A random sign makes half the steps go downhill: a random walk, no better at finding good maxima. An ever-growing rate eventually overshoots and diverges.
3. **$b\leftarrow b-\alpha\sum_i\bigl(c+bx_1^{(i)}-y^{(i)}\bigr)x_1^{(i)}$.** By the chain rule $\partial\,\text{loss}/\partial b=\sum_i(\hat y^{(i)}-y^{(i)})x_1^{(i)}$, and gradient descent subtracts $\alpha$ times the gradient.
4. **Linear.** Logistic regression predicts $1$ exactly when $\boldsymbol w\cdot\boldsymbol x+b>0$ (@def-logistic-regression), a hyperplane in feature space; the sigmoid only turns the score into a probability. (Here $y$ is the exclusive or of $x_1$ and $x_2$, so no linear boundary classifies all four points correctly.)
5. **Zero training error, and overfitting.** Three ReLU layers of width $10$ can represent exclusive or (@sec-ai-deep-learning-neural-networks) and have hundreds of parameters for four examples, so training can fit them exactly; with so little data such a fit says little about new data (@def-overfitting). It certainly does not underfit, and zero test error on unseen data cannot be expected.
6. **The first and the third.** Choosing the more probable label is the rule; with two labels it means $P(y'=1\mid\boldsymbol x')\ge0.5$ (ties broken towards $1$). The second and fourth conditions hold for every probability ($P\ge0$ and $P(1-P)\ge0$), so they always predict $1$.
:::

::: {.solution for="prob-gradient-descent-least-squares-code" status="draft"}
```{.python}
import numpy as np


def least_squares_gd(A, b, w0, eta, steps):
    """Gradient descent on 0.5 * ||A w - b||^2; return (w, losses)."""
    w = np.array(w0, dtype=float)              # a copy, so w0 is unchanged
    losses = []
    for _ in range(steps + 1):
        r = A @ w - b                          # residual
        losses.append(0.5 * float(r @ r))
        if len(losses) <= steps:
            w = w - eta * (A.T @ r)
    return w, losses
```

1. Expanding $F(\mathbf w)=\tfrac12(A\mathbf w-\mathbf b)^\top(A\mathbf w-\mathbf b)$ gives $\nabla F(\mathbf w)=A^\top(A\mathbf w-\mathbf b)$, the transpose of $A$ applied to the residual.
2. Each pass records $F$ at the current point and then steps, except after the last record, so the list has `steps + 1` values.
3. $F$ is $L$-smooth with $L=\lVert A\rVert_2^2$, the largest eigenvalue of $A^\top A$; with $\eta=1/L$ the loss never increases (@thm-descent-lemma). In the last test $\eta=3>2/L=2$, and each step multiplies $w$ by $1-3=-2$.
:::

::: {.solution for="prob-mit18065ps-22-q6" status="draft"}
$f(\mathbf{x})=\frac12\mathbf{x}^{\mathsf T}A^{\mathsf T}A\mathbf{x}-\mathbf{b}^{\mathsf T}A\mathbf{x}+\frac12\mathbf{b}^{\mathsf T}\mathbf{b}$ has gradient $A^{\mathsf T}A\mathbf{x}-A^{\mathsf T}\mathbf{b}=A^{\mathsf T}(A\mathbf{x}-\mathbf{b})$. So
$$\mathbf{x}_{k+1}=\mathbf{x}_k-s_kA^{\mathsf T}(A\mathbf{x}_k-\mathbf{b}).$$
Each step multiplies by $A$ and $A^{\mathsf T}$ and never forms $A^{\mathsf T}A$; a fixed point solves the normal equations.
:::

::: {.solution for="prob-mit18065ps-25-q1" status="draft"}
1. $\nabla F=\big(-2(y-x),\ 2y+2(y-x)\big)=(2x-2y,\ 4y-2x)$. At $(1,1)$: $\nabla F=(0,2)$.

2. $(x_1,y_1)=(1,1)-\frac12(0,2)=(1,0)$.

3. Remark: this step does not lower $F$ ($F(1,0)=1=F(1,1)$). The Hessian $\begin{bmatrix}2&-2\\-2&4\end{bmatrix}$ has eigenvalues $3\pm\sqrt5$, and gradient descent with a fixed step converges only for $s<2/(3+\sqrt5)\approx0.38$ (@thm-gradient-descent-quadratic-rate). With $s=\frac12$ the next iterates are $(0,1)$, $(1,-1)$, $(-1,2)$ with $F=2,5,13$: they diverge.
:::
