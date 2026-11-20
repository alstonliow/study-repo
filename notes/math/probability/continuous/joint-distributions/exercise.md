::: {.problem #prob-eecs126hw-3-q2 origin="external" source="eecs126hw-3-q2"}
**Joint Density for Exponential Distribution.**

(a) If $X\sim\text{Exponential}(\lambda)$ and $Y\sim\text{Exponential}(\mu)$, $X$ and $Y$ independent, compute $P(X<Y)$.

(b) If $X_k$, $1\le k\le n$ are independent and exponentially distributed with parameters $\lambda_1,\dots,\lambda_n$, show that $\min_{1\le k\le n}X_k\sim\text{Exponential}(\sum_{j=1}^{n}\lambda_j)$.

(c) Deduce that
$$P\bigl(X_i=\min_{1\le k\le n}X_k\bigr)=\frac{\lambda_i}{\sum_{j=1}^{n}\lambda_j}.$$
:::

::: {.problem #prob-eecs126hw-3-q1 origin="external" source="eecs126hw-3-q1"}
**Graphical Density.** Figure 1 shows the joint density $f_{X,Y}$ of the random variables $X$ and $Y$.

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0)--(4.6,0) node[lab,anchor=west] {$X$};
\draw[->] (0,0)--(0,3.6) node[lab,anchor=south] {$Y$};
\draw (1,0)--(1,-0.08) node[lab,tick,below] {$1$};
\draw (2,0)--(2,-0.08) node[lab,tick,below] {$2$};
\draw (3,0)--(3,-0.08) node[lab,tick,below] {$3$};
\draw (4,0)--(4,-0.08) node[lab,tick,below] {$4$};
\draw (0,1)--(-0.08,1) node[lab,tick,left] {$1$};
\draw (0,2)--(-0.08,2) node[lab,tick,left] {$2$};
\draw (0,3)--(-0.08,3) node[lab,tick,left] {$3$};
\draw[regionA, sharp corners] (1,1) rectangle (2,3);
\draw[regionA, sharp corners] (2,2) rectangle (3,3);
\draw[regionA, sharp corners] (3,1) rectangle (4,3);
\node[lab] at (1.5,2) {$A$};
\node[lab] at (2.5,2.5) {$2A$};
\node[lab] at (3.5,2) {$A$};
\end{tikzpicture}
\end{center}
```

(a) Find $A$ and sketch $f_X$, $f_Y$, and $f_{X\mid X+Y\le3}$.

(b) Find $E[X\mid Y=y]$ for $1\le y\le3$ and $E[Y\mid X=x]$ for $1\le x\le4$.

(c) Find $\operatorname{cov}(X,Y)$.
:::

::: {.problem #prob-mit6041f10-5-q1 origin="external" source="mit6041f10-5-q1"}
Random variables $X$ and $Y$ are distributed according to the joint PDF
$$f_{X,Y}(x,y) = \begin{cases} ax, & \text{if } 1 \leq x \leq y \leq 2,\\ 0, & \text{otherwise.}\end{cases}$$

(a) Evaluate the constant $a$.
(b) Determine the marginal PDF $f_Y(y)$.
(c) Determine the expected value of $\frac{1}{X}$, given that $Y = \frac{3}{2}$.
:::

::: {.problem #prob-mit6041f10-5-q5 origin="external" source="mit6041f10-5-q5"}
The random variables $X$ and $Y$ are described by a joint PDF which is constant within the unit area quadrilateral with vertices $(0, 0)$, $(0, 1)$, $(1, 2)$, and $(1, 1)$.

(a) Are $X$ and $Y$ independent?
(b) Find the marginal PDFs of $X$ and $Y$.
(c) Find the expected value of $X + Y$.
(d) Find the variance of $X + Y$.
:::

::: {.problem #prob-mit1805s22-5-q1 origin="external" source="mit1805s22-5-q1"}
Aching joints
Suppose $X$ and $Y$ have joint pdf $f(x, y) = c(x^2 + xy)$ on $[0, 1] \times [0, 1]$.

(a) Find $c$ and the joint cdf $F(x, y)$.

(b) Find the marginal cumulative distribution functions $F_X$ and $F_Y$ and the marginal pdf $f_X$ and $f_Y$.

(c) Find $E[X]$ and $\mathrm{Var}(X)$.

(d) Find the covariance and correlation of $X$ and $Y$.

(e) Are $X$ and $Y$ independent?
:::

::: {.problem #prob-mit1805s22-5-q4 origin="external" source="mit1805s22-5-q4"}
Don't be late!
Alicia and Bernardo are trying to meet for lunch and both will arrive, independently of each other, uniformly and at random between noon and 1pm. Let $A$ and $B$ be the number of minutes after noon at which Alicia and Bernardo arrive, respectively. Then $A$ and $B$ are independent uniformly distributed random variables on $[0, 60]$.

Hint: For parts (c-e) you might find it easiest to find the fraction of the square $[0, 60]\times[0, 60]$ filled by the event.

(a) Find the joint pdf $f(a, b)$ and joint cdf $F(a, b)$.

(b) Find the probability that Alicia arrives before 12:30.

(c) Find the probability that Alicia arrives before 12:15 and Bernardo arrives between 12:30 and 12:45 in two ways:

(i) By using the fact that $A$ and $B$ are independent.

(ii) By shading the corresponding area of the square $[0, 60] \times [0, 60]$ and finding what proportion of the square is shaded.

(d) Find the probability that Alicia arrives less than five minutes after Bernardo. (Hint: use method (ii) from part (c).)

(e) Now suppose that Alicia and Bernardo are both rather impatient and will leave if they have to wait more than 15 minutes for the other to arrive. What is the probability that Alicia and Bernardo will have lunch together?
:::
