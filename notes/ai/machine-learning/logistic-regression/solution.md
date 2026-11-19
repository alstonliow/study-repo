<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs188d-11-q1" status="draft"}
Write $\gamma=\mathbf w\cdot\mathbf x$ and $h=s(\gamma)$. This is the $\{0,1\}$-label form of @thm-logistic-loss-gradient.

(a)
1. $s(\gamma)=(1+e^{-\gamma})^{-1}$, so by the chain rule $s'(\gamma)=e^{-\gamma}(1+e^{-\gamma})^{-2}$.
2. Write $e^{-\gamma}/(1+e^{-\gamma})=1-1/(1+e^{-\gamma})=1-s(\gamma)$.
3. Hence $s'(\gamma)=\dfrac{1}{1+e^{-\gamma}}\cdot\dfrac{e^{-\gamma}}{1+e^{-\gamma}}=s(\gamma)\bigl(1-s(\gamma)\bigr)$.

(b)
1. $\dfrac{\partial\gamma}{\partial w_j}=x_j$, so by part (a) $\dfrac{\partial h}{\partial w_j}=h(1-h)x_j$.
2. Differentiating the loss, $\dfrac{dL}{dw_j}=-\Bigl[\dfrac{y}{h}-\dfrac{1-y}{1-h}\Bigr]h(1-h)x_j=-\bigl[y(1-h)-(1-y)h\bigr]x_j$.
3. Expanding the bracket, $y-yh-h+yh=y-h$, so
$$
\frac{dL}{dw_j}=\bigl(h(\mathbf x)-y\bigr)x_j.
$$

(c) Collecting the components, $\nabla_{\mathbf w}L=\bigl(h(\mathbf x)-y\bigr)\mathbf x$: the prediction error times the input.

(d) $\mathbf w\leftarrow\mathbf w-\eta\bigl(h(\mathbf x)-y\bigr)\mathbf x$ for the current sample $(\mathbf x,y)$ (@def-stochastic-gradient-descent). The weights move towards $\mathbf x$ when the prediction is too low ($h<y$) and away from it when too high, in proportion to the error.
:::
