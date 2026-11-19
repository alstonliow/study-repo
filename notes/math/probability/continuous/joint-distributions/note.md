---
title: "Joint Distributions"
sources: [eecs126hw-3]
requires: [math/probability/continuous/exponential-distribution, math/probability/discrete/covariance-and-correlation]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley EECS126 (Fall 2021), Homework 3, in our own wording; proofs written out in steps. -->

Several continuous random variables defined on the same experiment are described together by one joint density (@def-joint-density). This note adds marginals, conditioning and changes of variables.

::: {#def-marginal-conditional-density .definition name="Marginal and conditional densities"}

Let $X,Y$ have joint density $f_{X,Y}$ (@def-joint-density). The *marginal* densities are
$$f_X(x)=\int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dy,\qquad f_Y(y)=\int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dx,$$
and where $f_X(x)>0$ the *conditional density* of $Y$ given $X=x$ is
$$f_{Y\mid X}(y\mid x)=\frac{f_{X,Y}(x,y)}{f_X(x)}.$$

:::

$X$ and $Y$ are independent (@def-continuous-independence) exactly when $f_{X,Y}(x,y)=f_X(x)f_Y(y)$ for (almost) all $x,y$. Expectations are computed as in the discrete case with sums replaced by integrals: $E[g(X,Y)]=\iint g(x,y)f_{X,Y}(x,y)\,dx\,dy$.

::: {#exm-joint-density-triangle .example name="Uniform on a triangle"}

Let $(X,Y)$ be uniform on the triangle $0\le y\le x\le1$, which has area $\tfrac12$, so $f_{X,Y}=2$ there. Then $f_X(x)=\int_0^x2\,dy=2x$ on $[0,1]$, and given $X=x$ the conditional density of $Y$ is $2/(2x)=1/x$ on $[0,x]$: $Y$ is uniform on $[0,x]$, and $E[Y\mid X]=X/2$.

:::

::: {#thm-change-of-variables-density .theorem name="Change of variables"}

Let $(X,Y)$ have joint density $f_{X,Y}$ supported on an open set $D$, and let $g:D\to g(D)$ be one-to-one and continuously differentiable with non-zero Jacobian determinant $J_g$. Then $(U,V)=g(X,Y)$ has density
$$f_{U,V}(u,v)=\frac{f_{X,Y}\bigl(g^{-1}(u,v)\bigr)}{\bigl|J_g\bigl(g^{-1}(u,v)\bigr)\bigr|},\qquad(u,v)\in g(D).$$

:::

::: {.proof}

1. For a set $B\subseteq g(D)$, $\Pr((U,V)\in B)=\Pr((X,Y)\in g^{-1}(B))=\iint_{g^{-1}(B)}f_{X,Y}(x,y)\,dx\,dy$.

2. Substitute $(x,y)=g^{-1}(u,v)$. The multivariable substitution rule multiplies by $|J_{g^{-1}}(u,v)|=1/|J_g(g^{-1}(u,v))|$, so the integral equals $\iint_Bf_{X,Y}(g^{-1}(u,v))/|J_g(g^{-1}(u,v))|\,du\,dv$.

3. This holds for every $B$, so the integrand is the density of $(U,V)$.

:::

::: {#prp-min-of-exponentials .proposition name="Minimum of independent exponentials"}

Let $X_1,\dots,X_n$ be independent with $X_i\sim\operatorname{Exp}(\lambda_i)$, and $\lambda=\sum_i\lambda_i$. Then $M=\min_iX_i\sim\operatorname{Exp}(\lambda)$, and the index $I$ of the minimum satisfies $\Pr(I=i)=\lambda_i/\lambda$, independently of $M$.

:::

::: {.proof}

1. $\Pr(M>t)=\prod_i\Pr(X_i>t)=\prod_ie^{-\lambda_it}=e^{-\lambda t}$, so $M\sim\operatorname{Exp}(\lambda)$.

2. Let $Y=\min_{j\ne i}X_j$, which is $\operatorname{Exp}(\lambda-\lambda_i)$ by step 1 and independent of $X_i$. Then
   $$\Pr(I=i,\,M>t)=\Pr(Y>X_i>t)=\int_t^\infty\lambda_ie^{-\lambda_ix}e^{-(\lambda-\lambda_i)x}\,dx=\frac{\lambda_i}{\lambda}e^{-\lambda t}.$$

3. Hence $\Pr(I=i,M>t)=\Pr(I=i)\Pr(M>t)$ with $\Pr(I=i)=\lambda_i/\lambda$ (take $t=0$).

:::

This is the basic "race of exponential clocks" behind Poisson processes and continuous-time Markov chains (@sec-math-probability-random-processes-poisson-process).
