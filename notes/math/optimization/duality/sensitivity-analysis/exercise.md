::: {.problem #prob-ee364ahw-4-q1 origin="external" source="ee364ahw-4-q1"}
*Numerical perturbation analysis example.* Consider the quadratic program
$$\begin{array}{ll}\text{minimize}&x_1^2+2x_2^2-x_1x_2-x_1\\ \text{subject to}&x_1+2x_2\le u_1\\ &x_1-4x_2\le u_2,\\ &5x_1+76x_2\le1,\end{array}$$
with variables $x_1$, $x_2$, and parameters $u_1$, $u_2$.

(a) Solve this QP, for parameter values $u_1=-2$, $u_2=-3$, to find optimal primal variable values $x_1^\star$ and $x_2^\star$, and optimal dual variable values $\lambda_1^\star$, $\lambda_2^\star$ and $\lambda_3^\star$. Let $p^\star$ denote the optimal objective value. Verify that the KKT conditions hold for the optimal primal and dual variables you found (within reasonable numerical accuracy).

*Hint:* See §3.7 of the CVX users' guide to find out how to retrieve optimal dual variables. To specify the quadratic objective, use `quad_form()`.

(b) We will now solve some perturbed versions of the QP, with
$$u_1=-2+\delta_1,\qquad u_2=-3+\delta_2,$$
where $\delta_1$ and $\delta_2$ each take values from $\{-0.1,0,0.1\}$. (There are a total of nine such combinations, including the original problem with $\delta_1=\delta_2=0$.) For each combination of $\delta_1$ and $\delta_2$, make a prediction $p^\star_{\rm pred}$ of the optimal value of the perturbed QP, and compare it to $p^\star_{\rm exact}$, the exact optimal value of the perturbed QP (obtained by solving the perturbed QP). Put your results in the two righthand columns in a table with the form shown below. Check that the inequality $p^\star_{\rm pred}\le p^\star_{\rm exact}$ holds.

| $\delta_1$ | $\delta_2$ | $p^\star_{\rm pred}$ | $p^\star_{\rm exact}$ |
|---|---|---|---|
| $0$ | $0$ | | |
| $0$ | $-0.1$ | | |
| $0$ | $0.1$ | | |
| $-0.1$ | $0$ | | |
| $-0.1$ | $-0.1$ | | |
| $-0.1$ | $0.1$ | | |
| $0.1$ | $0$ | | |
| $0.1$ | $-0.1$ | | |
| $0.1$ | $0.1$ | | |
:::
