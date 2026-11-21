<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-ee364ahw-4-q1" status="draft"}
(a) The objective is $x^TQx+f^Tx$ with $Q=\begin{bmatrix}1&-\frac12\\-\frac12&2\end{bmatrix}\succ0$ and $f=(-1,0)$, so it is strictly convex and the optimal point is unique. Solving numerically (we used SciPy's SLSQP in place of CVX) gives
$$x^\star=\big(-\tfrac73,\ \tfrac16\big)\approx(-2.333,\,0.167),\qquad p^\star=\tfrac{74}{9}\approx8.222.$$
All three constraints are active at $x^\star$: $-\frac73+\frac13=-2$, $-\frac73-\frac23=-3$, $-\frac{35}3+\frac{38}3=1$.

Stationarity $2Qx^\star+f+A^T\lambda=0$ reads, with $2Qx^\star+f=(-\frac{35}6,3)$,
$$\lambda_1+\lambda_2+5\lambda_3=\tfrac{35}6,\qquad2\lambda_1-4\lambda_2+76\lambda_3=-3.$$
Three active constraints in $\mathbf{R}^2$ make the dual optimum non-unique: the solutions are
$$\lambda=\big(\tfrac{61}{18}-16s,\ \tfrac{22}9+11s,\ s\big),\qquad0\le s\le\tfrac{61}{288},$$
all nonnegative. Any of them, with $x^\star$, satisfies the KKT conditions (@def-kkt-conditions): primal feasibility (all constraints hold with equality), $\lambda\succeq0$, complementary slackness (every constraint is active), and stationarity by construction. We take $s=0$: $\lambda^\star=(3.389,\,2.444,\,0)$. (A solver may return a different point of this segment, for example $s\approx0.08$.)

(b) By @thm-global-sensitivity the prediction $p^\star_{\rm pred}=p^\star-\lambda_1^\star\delta_1-\lambda_2^\star\delta_2$ is a lower bound for every dual optimal $\lambda^\star$. With our $\lambda^\star$ and numerically solved perturbed problems:

| $\delta_1$ | $\delta_2$ | $p^\star_{\rm pred}$ | $p^\star_{\rm exact}$ |
|---|---|---|---|
| $0$ | $0$ | $8.222$ | $8.222$ |
| $0$ | $-0.1$ | $8.467$ | $8.706$ |
| $0$ | $0.1$ | $7.978$ | $7.980$ |
| $-0.1$ | $0$ | $8.561$ | $8.565$ |
| $-0.1$ | $-0.1$ | $8.806$ | $8.816$ |
| $-0.1$ | $0.1$ | $8.317$ | $8.319$ |
| $0.1$ | $0$ | $7.883$ | $8.222$ |
| $0.1$ | $-0.1$ | $8.128$ | $8.706$ |
| $0.1$ | $0.1$ | $7.639$ | $7.752$ |

The inequality $p^\star_{\rm pred}\le p^\star_{\rm exact}$ holds in every row. Because the dual optimum is not unique, $p^\star(u)$ is not differentiable at this $u$, and the predictions are exact only to first order in some directions.
:::
