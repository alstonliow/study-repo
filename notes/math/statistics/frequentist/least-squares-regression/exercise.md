::: {.problem #prob-mit1805s22-6-q2 origin="external" source="mit1805s22-6-q2"}
Least squares
In this problem we will use maximum likelihood estimates to develop Gauss' method of least squares for fitting lines to data.

Bivariate data means data of the form
$$(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n).$$
For bivariate data the simple linear regression model assumes that, for some values of the parameters $a$ and $b$, we have
$$y_i = ax_i + b + \text{random measurement error}.$$
The model assumes the measurement errors are independent and identically distributed and follow a $N(0, \sigma^2)$ distribution. (The values $x_i$ may or may not be random.)

In general terms, we can say that the value of $x$ 'explains' the value of $y$ except for some random noise. Graphically, the model says to make a scatter plot and find the line that best fits the data. This is called a simple linear regression model.

It turns out that, under some assumptions about random variation of measurement error, one way to find a "best" line is by solving a maximum likelihood problem.

The goal is to find the values of the model parameters $a$ and $b$ that give the MLE for this model. To guide you, we note that the model says that
$$y_i \sim N(ax_i + b, \sigma^2).$$
Also remember that you know the density function for this distribution.

(a) For a general datum $(x_1, y_1)$ give the likelihood and log likelihood functions (these will be functions of $y_1$, $x_1$, $a$, $b$, and $\sigma$.)

(b) Consider the data $(1, 8)$, $(3, 2)$, $(5, 1)$. Assume that $\sigma = 3$ is a known constant and find the maximum likelihood estimate for $a$ and $b$.

Note: since there are two variables $a$ and $b$, in order to find a critical point you will have to take partial derivatives and set them equal to 0. This part of the problem takes a fair amount of tedius algebra --sorry.

Note: We gave you a specific value of $\sigma$, to avoid the distraction of one more symbol. If you look at your calculations, you should see that the value of $\sigma$ plays no role in finding the MLE for $a$ and $b$. We get the same answer no matter what the value.

(c) Use R to plot the data and the regression line you found in part (ii) The commands plot(x,y, pch=19) and abline() will come in handy. For abline be careful: the parameter a is the intercept and b is the slope -- exactly the opposite of our usage. Print the plot and turn it in.
:::
