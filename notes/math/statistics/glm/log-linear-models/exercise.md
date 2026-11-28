::: {.problem #prob-camii-sms-4-q10 origin="external" source="camii-sms-4-q10"}
Agresti (1990) gives the table below, relating mothers' education to fathers' education for a sample of eminent black Americans (defined as persons having a biographical sketch in the publication *Who's Who Among Black Americans*).

| Mother's education | Father's education 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 1 | 81 | 3 | 9 | 11 |
| 2 | 14 | 8 | 9 | 6 |
| 3 | 43 | 7 | 43 | 18 |
| 4 | 21 | 6 | 24 | 87 |

The categories 1–4 indicate increasing levels of education. We wish to model the entries $Y_{ij}$ as components of a multinomial random vector with corresponding probabilities $p_{ij}$ where
$$p_{ij}=\begin{cases}\eta\varphi_i+(1-\eta)\alpha_i\beta_j,&\text{for }i=j,\\(1-\eta)\alpha_i\beta_j,&\text{for }i\neq j,\end{cases}$$
and
$$0\le\eta<1,\qquad\alpha_i,\beta_j>0,\ \varphi_i\ge0,\qquad\sum_i\varphi_i=\sum_i\alpha_i=\sum_j\beta_j=1.$$
Give an interpretation of this model. Why might we expect that $\eta>0$ for our data?

Now model the $Y_{ij}$ as independent Poisson random variables with means $\mu_{ij}=\exp(\alpha+x_{ij}^{\mathsf T}\theta)$. We wish to choose the covariates $x_{ij}$ such that if we maximise the Poisson likelihood, with non-negativity constraints on some components of $\theta$, we obtain an estimate $\hat\theta$ which yields fitted values $\hat\mu_{ij}=\exp(\hat\alpha+x_{ij}^{\mathsf T}\hat\theta)$ equal to those from the multinomial model above. Describe how the $x_{ij}$ can be chosen, and what non-negativity constraints should be applied.
:::
