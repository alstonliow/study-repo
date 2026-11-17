---
title: "Covariance and Correlation"
sources: [cs70-16.4]
requires: [math/probability/discrete/functions-of-random-variables]
aliases: [math/probability/covariance-and-correlation]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 16 (cs70-16.4), in our own wording; proofs written out in steps. -->

## Covariance

::: {#def-covariance .definition name="Covariance"}

With $\mu_X=E[X]$ and $\mu_Y=E[Y]$, the *covariance* of $X$ and $Y$ is
$$\mathrm{Cov}(X,Y)=E[(X-\mu_X)(Y-\mu_Y)].$$

:::

::: {#prp-covariance-properties .proposition name="Properties of covariance"}

1. $\mathrm{Cov}(X,Y)=E[XY]-E[X]E[Y]$.

2. If $X$ and $Y$ are independent, then $\mathrm{Cov}(X,Y)=0$.

3. $\mathrm{Cov}(X,X)=\mathrm{Var}(X)$.

4. Covariance is bilinear: for constants $a_i,b_j$,
   $$\mathrm{Cov}\Bigl(\sum_i a_iX_i,\ \sum_j b_jY_j\Bigr)=\sum_i\sum_j a_ib_j\,\mathrm{Cov}(X_i,Y_j).$$

5. $\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)+2\,\mathrm{Cov}(X,Y)$.

:::

::: {.proof}

1. Expand and use linearity: $E[(X-\mu_X)(Y-\mu_Y)]=E[XY]-\mu_XE[Y]-\mu_YE[X]+\mu_X\mu_Y=E[XY]-\mu_X\mu_Y$.

2. By @thm-expectation-of-product, $E[XY]=E[X]E[Y]$ for independent $X,Y$; use part 1.

3. Put $Y=X$ in @def-covariance and compare with @def-variance-standard-deviation.

4. By part 1 it is enough to expand $E\bigl[\sum_i a_iX_i\sum_j b_jY_j\bigr]$ and $E\bigl[\sum_i a_iX_i\bigr]E\bigl[\sum_j b_jY_j\bigr]$ as double sums by linearity, and subtract term by term.

5. By parts 3 and 4, $\mathrm{Var}(X+Y)=\mathrm{Cov}(X+Y,X+Y)=\mathrm{Cov}(X,X)+\mathrm{Cov}(Y,Y)+2\,\mathrm{Cov}(X,Y)$, using $\mathrm{Cov}(X,Y)=\mathrm{Cov}(Y,X)$.

:::

::: {#rmk-covariance-and-correlation-2 .remark name="The converse fails"}

Zero covariance does not imply independence. For example, let $X$ be $-1$, $0$ or $1$ with probability $\frac13$ each, and $Y=X^2$. Then $E[XY]=E[X^3]=0=E[X]E[Y]$, so $\mathrm{Cov}(X,Y)=0$, but $Y$ is determined by $X$. Part 5 shows that the variance of a sum is the sum of the variances exactly when the covariance is $0$ (@thm-variance-of-an-independent-sum is the independent case).

:::

## Correlation

::: {#def-correlation .definition name="Correlation"}

If $\sigma_X>0$ and $\sigma_Y>0$, the *correlation* of $X$ and $Y$ is
$$\mathrm{Corr}(X,Y)=\frac{\mathrm{Cov}(X,Y)}{\sigma_X\,\sigma_Y}.$$

:::

::: {#fig-covariance-and-correlation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[primary] (-0.141,-0.004) circle[radius=1.6pt]; \fill[primary] (-0.124,-0.187) circle[radius=1.6pt]; \fill[primary] (-0.512,-0.511) circle[radius=1.6pt]; \fill[primary] (0.612,0.652) circle[radius=1.6pt]; \fill[primary] (0.570,0.573) circle[radius=1.6pt]; \fill[primary] (0.217,0.240) circle[radius=1.6pt];
\fill[primary] (-0.916,-0.620) circle[radius=1.6pt]; \fill[primary] (0.279,0.370) circle[radius=1.6pt]; \fill[primary] (-0.930,-1.255) circle[radius=1.6pt]; \fill[primary] (-0.489,-0.553) circle[radius=1.6pt]; \fill[primary] (0.168,0.140) circle[radius=1.6pt]; \fill[primary] (0.287,0.104) circle[radius=1.6pt];
\fill[primary] (0.170,0.247) circle[radius=1.6pt]; \fill[primary] (-0.364,0.084) circle[radius=1.6pt]; \fill[primary] (0.306,0.562) circle[radius=1.6pt]; \fill[primary] (-0.341,-0.484) circle[radius=1.6pt]; \fill[primary] (-0.189,-0.196) circle[radius=1.6pt]; \fill[primary] (0.348,0.372) circle[radius=1.6pt];
\fill[primary] (-0.246,-0.451) circle[radius=1.6pt]; \fill[primary] (-0.286,0.035) circle[radius=1.6pt]; \fill[primary] (-0.444,-0.341) circle[radius=1.6pt]; \fill[primary] (0.235,-0.146) circle[radius=1.6pt]; \fill[primary] (0.027,0.337) circle[radius=1.6pt]; \fill[primary] (-1.108,-1.074) circle[radius=1.6pt];
\fill[primary] (-0.058,-0.248) circle[radius=1.6pt]; \fill[primary] (0.274,0.231) circle[radius=1.6pt]; \fill[primary] (-0.806,-0.527) circle[radius=1.6pt]; \fill[primary] (0.368,0.558) circle[radius=1.6pt]; \fill[primary] (0.792,0.800) circle[radius=1.6pt]; \fill[primary] (0.066,-0.252) circle[radius=1.6pt];
\fill[primary] (0.338,0.158) circle[radius=1.6pt]; \fill[primary] (-0.249,-0.527) circle[radius=1.6pt]; \fill[primary] (-0.532,-0.606) circle[radius=1.6pt]; \fill[primary] (0.709,0.151) circle[radius=1.6pt]; \fill[primary] (-0.802,-0.664) circle[radius=1.6pt]; \fill[primary] (0.794,0.853) circle[radius=1.6pt];
\fill[primary] (-1.045,-1.265) circle[radius=1.6pt]; \fill[primary] (0.197,0.000) circle[radius=1.6pt]; \fill[primary] (-0.616,-0.320) circle[radius=1.6pt]; \fill[primary] (0.606,0.583) circle[radius=1.6pt];
\draw[faint] (-1.4,-1.4) rectangle (1.4,1.4);
\node[lab] at (0,-1.8) {$\rho\approx0.9$};
\fill[primary] (3.535,0.239) circle[radius=1.6pt]; \fill[primary] (4.277,0.340) circle[radius=1.6pt]; \fill[primary] (3.685,0.301) circle[radius=1.6pt]; \fill[primary] (2.537,0.705) circle[radius=1.6pt]; \fill[primary] (3.925,0.291) circle[radius=1.6pt]; \fill[primary] (2.314,-0.349) circle[radius=1.6pt];
\fill[primary] (3.863,-0.996) circle[radius=1.6pt]; \fill[primary] (3.299,0.561) circle[radius=1.6pt]; \fill[primary] (2.679,0.886) circle[radius=1.6pt]; \fill[primary] (3.704,-0.083) circle[radius=1.6pt]; \fill[primary] (3.579,0.357) circle[radius=1.6pt]; \fill[primary] (3.466,0.630) circle[radius=1.6pt];
\fill[primary] (3.036,-0.228) circle[radius=1.6pt]; \fill[primary] (3.973,0.015) circle[radius=1.6pt]; \fill[primary] (2.916,0.521) circle[radius=1.6pt]; \fill[primary] (4.206,-0.245) circle[radius=1.6pt]; \fill[primary] (2.641,-0.074) circle[radius=1.6pt]; \fill[primary] (3.318,-0.164) circle[radius=1.6pt];
\fill[primary] (4.173,-0.565) circle[radius=1.6pt]; \fill[primary] (4.093,-0.698) circle[radius=1.6pt]; \fill[primary] (2.967,0.347) circle[radius=1.6pt]; \fill[primary] (4.021,0.472) circle[radius=1.6pt]; \fill[primary] (3.590,0.078) circle[radius=1.6pt]; \fill[primary] (3.484,0.316) circle[radius=1.6pt];
\fill[primary] (3.303,0.153) circle[radius=1.6pt]; \fill[primary] (3.715,0.000) circle[radius=1.6pt]; \fill[primary] (3.820,0.311) circle[radius=1.6pt]; \fill[primary] (4.506,0.179) circle[radius=1.6pt]; \fill[primary] (3.165,-0.205) circle[radius=1.6pt]; \fill[primary] (3.393,0.508) circle[radius=1.6pt];
\fill[primary] (3.215,0.212) circle[radius=1.6pt]; \fill[primary] (4.411,-1.265) circle[radius=1.6pt]; \fill[primary] (2.782,0.134) circle[radius=1.6pt]; \fill[primary] (3.619,0.131) circle[radius=1.6pt]; \fill[primary] (3.163,0.360) circle[radius=1.6pt]; \fill[primary] (3.555,-0.287) circle[radius=1.6pt];
\fill[primary] (4.665,0.195) circle[radius=1.6pt]; \fill[primary] (3.095,-0.055) circle[radius=1.6pt]; \fill[primary] (3.276,-0.035) circle[radius=1.6pt]; \fill[primary] (2.135,-0.268) circle[radius=1.6pt];
\draw[faint] (2.0,-1.4) rectangle (4.8,1.4);
\node[lab] at (3.4,-1.8) {$\rho\approx0$};
\fill[primary] (7.355,-0.779) circle[radius=1.6pt]; \fill[primary] (6.763,0.262) circle[radius=1.6pt]; \fill[primary] (7.271,-0.066) circle[radius=1.6pt]; \fill[primary] (5.864,0.757) circle[radius=1.6pt]; \fill[primary] (6.612,0.318) circle[radius=1.6pt]; \fill[primary] (7.400,-1.184) circle[radius=1.6pt];
\fill[primary] (7.399,-0.886) circle[radius=1.6pt]; \fill[primary] (7.176,-0.696) circle[radius=1.6pt]; \fill[primary] (6.897,0.199) circle[radius=1.6pt]; \fill[primary] (6.718,0.120) circle[radius=1.6pt]; \fill[primary] (7.238,-0.361) circle[radius=1.6pt]; \fill[primary] (6.751,0.411) circle[radius=1.6pt];
\fill[primary] (7.377,-0.589) circle[radius=1.6pt]; \fill[primary] (8.065,-1.265) circle[radius=1.6pt]; \fill[primary] (7.303,-0.516) circle[radius=1.6pt]; \fill[primary] (6.873,0.103) circle[radius=1.6pt]; \fill[primary] (6.922,0.043) circle[radius=1.6pt]; \fill[primary] (5.960,0.394) circle[radius=1.6pt];
\fill[primary] (7.138,-0.535) circle[radius=1.6pt]; \fill[primary] (6.235,0.156) circle[radius=1.6pt]; \fill[primary] (7.497,-0.448) circle[radius=1.6pt]; \fill[primary] (7.610,-0.954) circle[radius=1.6pt]; \fill[primary] (6.801,-0.274) circle[radius=1.6pt]; \fill[primary] (7.221,0.002) circle[radius=1.6pt];
\fill[primary] (6.310,0.815) circle[radius=1.6pt]; \fill[primary] (7.343,-0.532) circle[radius=1.6pt]; \fill[primary] (5.715,1.265) circle[radius=1.6pt]; \fill[primary] (6.747,-0.097) circle[radius=1.6pt]; \fill[primary] (7.020,-0.100) circle[radius=1.6pt]; \fill[primary] (7.624,-0.986) circle[radius=1.6pt];
\fill[primary] (7.425,-0.206) circle[radius=1.6pt]; \fill[primary] (7.599,-0.762) circle[radius=1.6pt]; \fill[primary] (6.391,0.612) circle[radius=1.6pt]; \fill[primary] (6.863,-0.027) circle[radius=1.6pt]; \fill[primary] (7.583,-0.768) circle[radius=1.6pt]; \fill[primary] (5.537,1.044) circle[radius=1.6pt];
\fill[primary] (5.780,1.114) circle[radius=1.6pt]; \fill[primary] (6.974,-0.303) circle[radius=1.6pt]; \fill[primary] (6.795,0.204) circle[radius=1.6pt]; \fill[primary] (6.843,0.279) circle[radius=1.6pt];
\draw[faint] (5.4,-1.4) rectangle (8.2,1.4);
\node[lab] at (6.8,-1.8) {$\rho\approx-0.9$};
\end{tikzpicture}
\end{center}
```

Samples of pairs $(X,Y)$ with correlation about $0.9$, $0$ and $-0.9$. The closer $|\rho|$ is to $1$, the closer the points lie to a line.

:::

::: {#thm-correlation-bound .theorem name="Correlation lies between -1 and 1"}

If $\sigma_X>0$ and $\sigma_Y>0$, then $-1\le\mathrm{Corr}(X,Y)\le1$.

:::

::: {.proof}

1. Standardise: let $\tilde X=(X-\mu_X)/\sigma_X$ and $\tilde Y=(Y-\mu_Y)/\sigma_Y$. Then $E[\tilde X]=E[\tilde Y]=0$ and $E[\tilde X^2]=E[\tilde Y^2]=1$.

2. By part 1 of @prp-covariance-properties and linearity, $E[\tilde X\tilde Y]=\dfrac{E[(X-\mu_X)(Y-\mu_Y)]}{\sigma_X\sigma_Y}=\mathrm{Corr}(X,Y)$.

3. A square is never negative, so
   $$0\le E[(\tilde X-\tilde Y)^2]=2-2E[\tilde X\tilde Y],\qquad 0\le E[(\tilde X+\tilde Y)^2]=2+2E[\tilde X\tilde Y].$$

4. Hence $-1\le E[\tilde X\tilde Y]\le1$, and by step 2 this is the claim.

:::

::: {#rmk-covariance-and-correlation-3 .remark name="When the bound is reached"}

The proof shows that $\mathrm{Corr}(X,Y)=1$ exactly when $E[(\tilde X-\tilde Y)^2]=0$, that is when $\tilde X=\tilde Y$ with probability $1$. Then $Y=aX+b$ with $a>0$. Likewise $\mathrm{Corr}(X,Y)=-1$ gives $Y=aX+b$ with $a<0$. The sign of the covariance shows the direction of the association; the correlation also measures its strength on a fixed scale.

:::
