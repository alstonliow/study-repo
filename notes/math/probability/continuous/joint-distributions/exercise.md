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
