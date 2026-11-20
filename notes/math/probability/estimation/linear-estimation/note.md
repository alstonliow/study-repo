---
title: "Linear and Nonlinear Estimation"
sources: [eecs126-10, eecs126hw-14, eecs126d-13]
requires: [math/probability/discrete/conditional-expectation, math/probability/discrete/covariance-and-correlation, math/linear-algebra/orthogonality/orthonormal-bases-and-gram-schmidt]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley EECS126 (Fall 2021), note "The Hilbert Space of Random Variables", Homework 14 and Discussion 13, in our own wording; proofs written out in steps. -->

We observe $Y$ and want to estimate $X$ by a function $g(Y)$ with the smallest *mean squared error* $E[(X-g(Y))^2]$. The key is to treat random variables as vectors.

::: {#def-random-variable-inner-product .definition name="Inner product of random variables"}

On random variables with finite second moment, define
$$\langle X,Y\rangle=E[XY],\qquad\|X\|=\sqrt{E[X^2]}.$$
$X$ and $Y$ are *orthogonal*, $X\perp Y$, if $E[XY]=0$.

:::

This is an inner product (identifying variables that are equal with probability $1$), and the space is complete, a Hilbert space. Mean squared error is squared distance, so the best estimator in a subspace is the orthogonal projection onto it.

::: {#thm-projection-random-variables .theorem name="Projection theorem"}

Let $\mathcal S$ be a closed subspace. Then $\hat X\in\mathcal S$ minimises $E[(X-Z)^2]$ over $Z\in\mathcal S$ if and only if
$$X-\hat X\perp Z\quad\text{for every }Z\in\mathcal S.$$

:::

::: {.proof}

1. *If.* For $Z\in\mathcal S$, $\hat X-Z\in\mathcal S$, so $\|X-Z\|^2=\|X-\hat X\|^2+\|\hat X-Z\|^2\ge\|X-\hat X\|^2$ (Pythagoras, the cross term $2E[(X-\hat X)(\hat X-Z)]$ vanishes).

2. *Only if.* If $E[(X-\hat X)Z]=c\ne0$ for some $Z\in\mathcal S$, then $\hat X+tZ$ with $t=c/\|Z\|^2$ has squared error $\|X-\hat X\|^2-c^2/\|Z\|^2$, smaller.

:::

::: {#fig-linear-estimation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.1]
\fill[tintA] (-2,-0.7) -- (2.2,-0.7) -- (3,0.6) -- (-1.2,0.6) -- cycle;
\draw[primary] (-2,-0.7) -- (2.2,-0.7) -- (3,0.6) -- (-1.2,0.6) -- cycle;
\node[lab, primary] at (2.6,-0.45) {$\mathcal S$};
\draw[->, emph] (0,0) -- (1.4,2.1) node[lab, above] {$X$};
\draw[->, hl] (0,0) -- (1.4,0.1) node[lab, below right] {$\hat X$};
\draw[dashed] (1.4,0.1) -- node[lab, right] {$X-\hat X$} (1.4,2.1);
\draw (1.4,0.35) -- (1.2,0.34) -- (1.2,0.09);
\draw[->, emph, secondary] (0,0) -- (-1.1,0.3) node[lab, above] {$Z$};
\end{tikzpicture}
\end{center}
```

The projection theorem: the best estimate $\hat X$ in the subspace $\mathcal S$ is the foot of the perpendicular from $X$, so the error $X-\hat X$ is orthogonal to every $Z$ in $\mathcal S$. Lengths are measured by $\sqrt{E[Z^2]}$.

:::

::: {#thm-llse .theorem name="Linear least squares estimate"}

The best estimate of $X$ of the form $a+bY$ (with $\operatorname{Var}(Y)>0$) is
$$L[X\mid Y]=E[X]+\frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(Y)}\bigl(Y-E[Y]\bigr),$$
with mean squared error $\operatorname{Var}(X)-\dfrac{\operatorname{Cov}(X,Y)^2}{\operatorname{Var}(Y)}$. For a vector $Y$ with invertible covariance $\Sigma_Y$, $L[X\mid Y]=E[X]+\Sigma_{XY}\Sigma_Y^{-1}(Y-E[Y])$.

:::

::: {.proof}

1. The subspace is spanned by $1$ and $Y$. By @thm-projection-random-variables, the error $X-a-bY$ must be orthogonal to $1$ and to $Y-E[Y]$.

2. Orthogonality to $1$: $E[X]=a+bE[Y]$, so $\hat X=E[X]+b(Y-E[Y])$.

3. Orthogonality to $Y-E[Y]$: $E[(X-E[X]-b(Y-E[Y]))(Y-E[Y])]=\operatorname{Cov}(X,Y)-b\operatorname{Var}(Y)=0$.

4. The error is $E[(\tilde X-b\tilde Y)^2]=\operatorname{Var}(X)-2b\operatorname{Cov}(X,Y)+b^2\operatorname{Var}(Y)$ with $\tilde X=X-E[X]$, $\tilde Y=Y-E[Y]$; substitute $b$. The vector case is the same computation with matrices.

:::

::: {#thm-mmse-conditional-expectation .theorem name="The MMSE estimate is the conditional expectation"}

Among all functions $g$ with $E[g(Y)^2]<\infty$, the mean squared error $E[(X-g(Y))^2]$ is minimised by
$$\mathrm{MMSE}[X\mid Y]=E[X\mid Y].$$

:::

::: {.proof}

1. The functions $g(Y)$ form a closed subspace, so by @thm-projection-random-variables it suffices that $X-E[X\mid Y]\perp g(Y)$ for every $g$.

2. By the tower property (@thm-total-expectation), $E[(X-E[X\mid Y])g(Y)]=E\bigl[g(Y)\,E[X-E[X\mid Y]\mid Y]\bigr]=0$.

:::

::: {#exm-llse-signal-noise .example name="Signal in noise"}

Let $Y=X+W$ with $X$ and $W$ independent, mean $0$, $\operatorname{Var}(X)=\sigma^2$, $\operatorname{Var}(W)=\tau^2$. Then $\operatorname{Cov}(X,Y)=\sigma^2$ and $\operatorname{Var}(Y)=\sigma^2+\tau^2$, so
$$L[X\mid Y]=\frac{\sigma^2}{\sigma^2+\tau^2}Y,\qquad\text{error }\frac{\sigma^2\tau^2}{\sigma^2+\tau^2}.$$
With $\sigma=\tau=1$, the estimate is $Y/2$ with error $\tfrac12$. If $X$ and $W$ are Gaussian, this linear estimate is also the MMSE (@thm-jointly-gaussian-conditional).

:::

::: {#thm-orthogonal-update .theorem name="Orthogonal updates"}

If $Z$ is orthogonal to $1$ and to $Y$ (that is, uncorrelated with $Y$ and of mean $0$), then
$$L[X\mid Y,Z]=L[X\mid Y]+L[X\mid Z]-E[X].$$
In general, a new observation $Z$ contributes only through its *innovation* $\tilde Z=Z-L[Z\mid Y]$: $L[X\mid Y,Z]=L[X\mid Y]+L[X-E[X]\mid\tilde Z]$.

:::

::: {.proof}

1. The span of $1,Y,Z$ is the orthogonal sum of the span of $1,Y$ and the line through $Z$, so the projection onto it is the sum of the two projections; the term $E[X]$ is the projection onto $1$, counted twice.

2. For general $Z$, the span of $1,Y,Z$ equals that of $1,Y,\tilde Z$, and $\tilde Z\perp1,Y$ by @thm-projection-random-variables; apply step 1 with $\tilde Z$.

:::

Orthogonal updates are what make the Kalman filter recursive (@sec-math-probability-estimation-kalman-filter). Linear regression is the same projection with the empirical distribution of the data points in place of the true joint distribution.
