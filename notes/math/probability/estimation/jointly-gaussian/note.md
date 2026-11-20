---
title: "Jointly Gaussian Random Variables"
sources: [eecs126hw-12, eecs126hw-13, eecs126d-12, eecs126d-13]
requires: [math/probability/estimation/linear-estimation, math/probability/continuous/transforms]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley EECS126 (Fall 2021), Homeworks 12–13 and Discussions 12–13, in our own wording; proofs written out in steps. -->

Gaussian vectors are the setting in which linear estimation is optimal and uncorrelated means independent.

::: {#def-jointly-gaussian .definition name="Jointly Gaussian"}

A random vector $X=(X_1,\dots,X_n)$ is *jointly Gaussian* if every linear combination $a^{\mathsf T}X=\sum_ia_iX_i$ is a (possibly degenerate) normal random variable. Equivalently, $X=\mu+AZ$ for a vector $\mu$, a matrix $A$, and $Z$ a vector of independent $N(0,1)$ variables. We write $X\sim N(\mu,\Sigma)$ with mean $\mu$ and covariance $\Sigma=AA^{\mathsf T}$.

:::

::: {#thm-jointly-gaussian-properties .theorem name="Properties of jointly Gaussian vectors"}

Let $X\sim N(\mu,\Sigma)$.

1. The distribution is determined by $\mu$ and $\Sigma$: $E[e^{s^{\mathsf T}X}]=e^{s^{\mathsf T}\mu+\frac12s^{\mathsf T}\Sigma s}$.
2. $BX+c\sim N(B\mu+c,B\Sigma B^{\mathsf T})$.
3. If $\Sigma$ is invertible, $X$ has density $f(x)=\dfrac{1}{(2\pi)^{n/2}\sqrt{\det\Sigma}}\exp\bigl(-\tfrac12(x-\mu)^{\mathsf T}\Sigma^{-1}(x-\mu)\bigr)$.
4. If $(X,Y)$ is jointly Gaussian and $\operatorname{Cov}(X_i,Y_j)=0$ for all $i,j$, then $X$ and $Y$ are independent.

:::

::: {.proof}

1. $s^{\mathsf T}X$ is normal with mean $s^{\mathsf T}\mu$ and variance $s^{\mathsf T}\Sigma s$, so its MGF at $1$ is as stated (@thm-transform-properties and the normal MGF). The multivariate MGF determines the distribution.

2. $BX+c=(B\mu+c)+(BA)Z$, and $(BA)(BA)^{\mathsf T}=B\Sigma B^{\mathsf T}$.

3. Take $A=\Sigma^{1/2}$, invertible, and apply @thm-change-of-variables-density to $x=\mu+Az$ with the density $\prod_i\phi(z_i)=(2\pi)^{-n/2}e^{-\|z\|^2/2}$; $|\det A|=\sqrt{\det\Sigma}$ and $\|z\|^2=(x-\mu)^{\mathsf T}\Sigma^{-1}(x-\mu)$.

4. The covariance of $(X,Y)$ is block diagonal, so its MGF factorises into that of $X$ times that of $Y$; by uniqueness the joint law is the product of the marginals.

:::

::: {#exm-jointly-gaussian-counter .example name="Gaussian marginals are not enough"}

Let $X\sim N(0,1)$, let $S=\pm1$ be a fair sign independent of $X$, and $Y=SX$. Then $Y\sim N(0,1)$ and $\operatorname{Cov}(X,Y)=E[S]E[X^2]=0$, but $X$ and $Y$ are not independent ($|Y|=|X|$), and $X+Y$ equals $0$ with probability $\tfrac12$, so it is not normal: $(X,Y)$ is not jointly Gaussian.

:::

::: {#thm-jointly-gaussian-conditional .theorem name="Conditioning a Gaussian vector"}

If $(X,Y)$ is jointly Gaussian and $\Sigma_Y$ is invertible, then given $Y=y$, $X$ is Gaussian with
$$E[X\mid Y=y]=\mu_X+\Sigma_{XY}\Sigma_Y^{-1}(y-\mu_Y),\qquad\operatorname{Cov}(X\mid Y)=\Sigma_X-\Sigma_{XY}\Sigma_Y^{-1}\Sigma_{YX}.$$
In particular $E[X\mid Y]=L[X\mid Y]$: for jointly Gaussian variables the MMSE estimate is linear.

:::

::: {.proof}

1. Let $\hat X=L[X\mid Y]$, given by the formula above (@thm-llse), and $E=X-\hat X$.

2. $(E,Y)$ is a linear function of $(X,Y)$, hence jointly Gaussian, and $\operatorname{Cov}(E,Y)=0$ by the projection property. By @thm-jointly-gaussian-properties part 4, $E$ is independent of $Y$.

3. So given $Y=y$, $X=\hat X(y)+E$ with $E\sim N(0,\Sigma_E)$ unaffected by the conditioning. Its mean is $\hat X(y)$ and $\Sigma_E=\Sigma_X-\Sigma_{XY}\Sigma_Y^{-1}\Sigma_{YX}$ by direct computation.

:::

::: {#exm-jointly-gaussian-pair .example name="Two correlated normals"}

Let $X,Y$ be standard normal and jointly Gaussian with correlation $\rho$. Then $E[X\mid Y]=\rho Y$ and $\operatorname{Var}(X\mid Y)=1-\rho^2$. With $\rho=0.8$ and $Y=1$, $X$ is $N(0.8,0.36)$ given the observation.

:::

::: {#fig-jointly-gaussian-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.9]
\draw[->] (-2.8,0) -- (2.9,0) node[lab, right] {$x$};
\draw[->] (0,-2.8) -- (0,2.9) node[lab, above] {$y$};
\foreach \c/\s in {0.6/tintA,1.2/tintA,1.8/tintA} \fill[\s, rotate=45] (0,0) ellipse ({\c*1.342} and {\c*0.447});
\foreach \c in {0.6,1.2,1.8} \draw[primary, rotate=45] (0,0) ellipse ({\c*1.342} and {\c*0.447});
\draw[hl] (-2.24,-2.8) -- (2.24,2.8) node[lab, above] {$x=0.8\,y$};
\draw[faint, dashed] (-2.6,1.25) -- (2.6,1.25) node[lab, right] {$Y=1.25$};
\node[hl dot] at (1,1.25) {};
\end{tikzpicture}
\end{center}
```

Contours of the joint density of two standard normals with correlation $\rho=0.8$ (@exm-jointly-gaussian-pair). Conditioning on $Y=y$ cuts along a horizontal line; the conditional mean $E[X\mid Y=y]=0.8y$ lies on the highlighted line, which joins the points where the horizontal lines touch the contours.

:::
