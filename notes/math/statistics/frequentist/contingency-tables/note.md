---
title: "Contingency Tables: Independence, Homogeneity and Composite Nulls"
sources: [camib-st-10, camib-sts-2-q4, camib-sts-2-q6, camib-sts-2-q7]
requires: [math/statistics/inference/parametric-tests, math/probability/distributions/multinomial-distribution]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part IB Statistics (Lent 2025, lecturer's notes), Lecture 10 and Example Sheet 2 (questions 4, 6, 7), in our own wording; proofs written out in steps. Pearson's statistic and the asymptotic likelihood ratio test are in math/statistics/inference/parametric-tests; the chi-square goodness-of-fit recipe and the remark on homogeneity are in math/statistics/frequentist/chi-square-and-f-tests. The numbers were recomputed by a short script. -->

Counts cross-classified by two factors form a contingency table. Testing whether the factors are independent is a goodness-of-fit test with a composite null, and the likelihood ratio and Pearson statistics are computed from the expected counts that the null's maximum likelihood estimators give.

::: {#thm-independence-test .theorem name="Chi-squared test of independence"}

Let $(X_1,Y_1),\dots,(X_n,Y_n)$ be iid pairs with $X_i\in\{1,\dots,r\}$, $Y_i\in\{1,\dots,c\}$, and let $N_{xy}=\#\{i:(X_i,Y_i)=(x,y)\}$, so that $(N_{xy})\sim\mathrm{Multinomial}(n;(p_{xy}))$ (@def-multinomial-distribution). To test
$$H_0:\ p_{xy}=p_{x+}p_{+y}\ \text{for all }x,y\qquad\text{against}\qquad H_1:\ (p_{xy})\text{ unrestricted},$$
write $N_{x+}=\sum_yN_{xy}$, $N_{+y}=\sum_xN_{xy}$ and $E_{xy}=N_{x+}N_{+y}/n$. Then

1. the maximum likelihood estimators are $\hat p_{xy}=N_{xy}/n$ under $H_1$ and $\hat p_{x+}=N_{x+}/n$, $\hat p_{+y}=N_{+y}/n$ under $H_0$, so $n\hat p_{x+}\hat p_{+y}=E_{xy}$;
2. $2\log\Lambda=2\sum_{x,y}N_{xy}\log\dfrac{N_{xy}}{E_{xy}}\approx\sum_{x,y}\dfrac{(N_{xy}-E_{xy})^2}{E_{xy}}$ (Pearson's statistic), and both are approximately $\chi^2_{(r-1)(c-1)}$ under $H_0$ for large $n$.

:::

::: {.proof}

1. The log-likelihood under $H_1$ is $\sum_{x,y}N_{xy}\log p_{xy}$ up to a constant; maximising subject to $\sum p_{xy}=1$ gives $\hat p_{xy}=N_{xy}/n$ (Gibbs' inequality, or a Lagrange multiplier).

2. Under $H_0$ the log-likelihood is $\sum_xN_{x+}\log p_{x+}+\sum_yN_{+y}\log p_{+y}$. It separates into a term in $(p_{x+})$ and a term in $(p_{+y})$, each maximised on its own simplex by the observed proportions, giving the stated estimators.

3. Therefore
$$2\log\Lambda=2\sum_{x,y}N_{xy}\log\frac{N_{xy}/n}{(N_{x+}/n)(N_{+y}/n)}=2\sum_{x,y}N_{xy}\log\frac{N_{xy}}{E_{xy}},$$
and for $N_{xy}/E_{xy}\approx1$ the expansion $2O\log(O/E)\approx(O-E)^2/E$ (using that $\sum(O-E)=0$) yields Pearson's statistic, as in @thm-pearson-chi-square-limit.

4. The number of free parameters is $rc-1$ under $H_1$ and $(r-1)+(c-1)$ under $H_0$, so the degrees of freedom is $rc-1-(r-1)-(c-1)=(r-1)(c-1)$, by the asymptotic likelihood ratio theorem (@thm-likelihood-ratio-test).

:::

::: {#exm-car-changes .example name="Old car against new car"}

Five hundred people who recently changed car reported the size of their old and new car.

| old $\backslash$ new | large | medium | small | total |
|---|---|---|---|---|
| large | 56 | 52 | 42 | 150 |
| medium | 50 | 83 | 67 | 200 |
| small | 18 | 51 | 81 | 150 |
| total | 124 | 186 | 190 | 500 |

The expected counts $E_{xy}=N_{x+}N_{+y}/n$ are $(37.2,55.8,57.0)$, $(49.6,74.4,76.0)$, $(37.2,55.8,57.0)$. Pearson's statistic is $36.2$ (and $2\log\Lambda=36.5$) on $(3-1)(3-1)=4$ degrees of freedom, with $p$-value about $3\times10^{-7}$: old and new size are strongly dependent. The Pearson residuals $(O-E)/\sqrt E$ show where: large cars are followed by large cars ($+3.1$) and small by small ($+3.2$), while small-after-large and large-after-small are rare ($-2.0$, $-3.2$).

:::

::: {#fig-contingency-tables-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.4cm,y=1cm]
\foreach \i/\j/\v/\s in {0/0/3.08/hl, 1/0/-0.51/faint, 2/0/-1.99/faint,
                         0/1/0.06/faint, 1/1/1.00/faint, 2/1/-1.03/faint,
                         0/2/-3.15/hl, 1/2/-0.64/faint, 2/2/3.18/hl}
  \node[box, \s] at (\i,-\j) {$\v$};
\node[lab] at (0,0.8) {large};
\node[lab] at (1,0.8) {medium};
\node[lab] at (2,0.8) {small};
\node[lab, left] at (-0.8,0) {large};
\node[lab, left] at (-0.8,-1) {medium};
\node[lab, left] at (-0.8,-2) {small};
\node[lab] at (1,1.4) {new car};
\node[lab, rotate=90] at (-2.0,-1) {old car};
\end{tikzpicture}
\end{center}
```

Pearson residuals for the car data. The highlighted cells ($|r|>3$) carry most of the departure from independence: customers tend to stay with the size they had.

:::

::: {#thm-homogeneity-test .theorem name="Test of homogeneity"}

Suppose the row totals $n_x=N_{x+}$ are fixed by the design and the rows are independent, $(N_{x1},\dots,N_{xc})\sim\mathrm{Multinomial}(n_x;p_{1|x},\dots,p_{c|x})$ for $x=1,\dots,r$. To test $H_0:\ p_{y|x}$ does not depend on $x$ against unrestricted $p_{y|x}$, the generalised likelihood ratio statistic and Pearson's statistic are exactly those of @thm-independence-test, with the same expected counts $E_{xy}=n_xN_{+y}/n$ and the same $(r-1)(c-1)$ degrees of freedom.

:::

::: {.proof}

1. The log-likelihood is $\sum_{x,y}N_{xy}\log p_{y|x}$. Without restriction each row is maximised by $\hat p_{y|x}=N_{xy}/n_x$.

2. Under $H_0$ with common $p_y$ the log-likelihood is $\sum_yN_{+y}\log p_y$, maximised at $\hat p_y=N_{+y}/n$.

3. The fitted counts under $H_0$ are $n_x\hat p_y=n_xN_{+y}/n=E_{xy}$, so
$$2\log\Lambda=2\sum_{x,y}N_{xy}\log\frac{N_{xy}/n_x}{N_{+y}/n}=2\sum_{x,y}N_{xy}\log\frac{N_{xy}}{E_{xy}},$$
the statistic of @thm-independence-test. The parameter count is $r(c-1)-(c-1)=(r-1)(c-1)$.

:::

::: {#exm-hardy-weinberg .example name="A composite null: Hardy–Weinberg equilibrium"}

For a gene with alleles $A$ and $a$ and genotype frequencies $(p_{AA},p_{Aa},p_{aa})$, Hardy–Weinberg equilibrium says $(p_{AA},p_{Aa},p_{aa})=(\theta^2,2\theta(1-\theta),(1-\theta)^2)$. Among $n=1612$ scarlet tiger moths $1469$ were $AA$, $138$ were $Aa$ and $5$ were $aa$.

1. The null likelihood is $\theta^{2N_{AA}+N_{Aa}}(1-\theta)^{N_{Aa}+2N_{aa}}$ up to a constant, so $\hat\theta=(2N_{AA}+N_{Aa})/(2n)=3076/3224=0.954$.

2. The expected counts are $n\hat\theta^2=1467.4$, $2n\hat\theta(1-\hat\theta)=141.2$, $n(1-\hat\theta)^2=3.4$; Pearson's statistic is $0.83$ and $2\log\Lambda=0.73$.

3. The alternative has $3-1=2$ free parameters and the null $1$, so the reference distribution is $\chi^2_{1}$ and the $p$-value is $0.36$ for Pearson's statistic: no evidence against equilibrium (the expected count $3.4$ is small, so the approximation is rough).

:::
