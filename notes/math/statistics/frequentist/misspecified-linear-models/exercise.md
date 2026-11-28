::: {.problem #prob-camii-sms-1-q11 origin="external" source="camii-sms-1-q11"}
(Tripos 2022/II/13J) Consider the following R code:

```
> n <- 1000000
> sigma_z <- 1; sigma_x1 <- 0.5; sigma_x2 <- 1; sigma_y <- 2; beta <- 2
> Z <- sigma_z * rnorm(n)
> X1 <- Z + sigma_x1 * rnorm(n)
> X2 <- Z + sigma_x2 * rnorm(n)
> Y <- beta * Z + sigma_y * rnorm(n)
> lm(Y ~ Z)
Coefficients:
(Intercept)            Z
  -0.003089     1.999780
> lm(Y ~ X1)
Coefficients:
(Intercept)           X1
  -0.002904     1.600521
> lm(Y ~ X2)
Coefficients:
(Intercept)           X2
  -0.002672     0.997499
```

Describe the phenomenon you see from the output above, then give a mathematical explanation to this phenomenon. Do you expect the slope coefficient in the second model to be generally smaller than that in the first model? Do you think modifying (for example, doubling) the value of `sigma_y` will substantially alter the slope coefficient in the second model? Justify your answer.
:::
