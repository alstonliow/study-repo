---
title: "Nested Models, the F-Test and Analysis of Variance"
sources: [camib-st-12, camib-st-14, camib-st-15, camib-sts-3-q7, camib-sts-3-q10, camii-sms-1-q1, camii-sms-1-q2, camii-sms-1-q4, camii-sms-1-q12]
requires: [math/statistics/frequentist/gaussian-projections, math/statistics/frequentist/regression-inference, math/statistics/inference/composite-hypotheses]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part IB Statistics (Lent 2025, lecturer's notes), Lectures 12, 14 and 15 and Example Sheet 3 (questions 7, 10), in our own wording; proofs written out in steps. The balanced one-way ANOVA and the F test of a linear constraint $G\beta=\lambda$ are in math/statistics/frequentist/chi-square-and-f-tests and math/statistics/frequentist/regression-inference; this note gives the geometric (projection) form, valid for unequal group sizes. -->

Testing a smaller linear model against a larger one is a statement about two nested subspaces of $\mathbb R^n$. Orthogonal projections turn it into an $F$-test, and one-way analysis of variance, the two-sample $t$-test and the $t$-test for a single coefficient all become special cases.

::: {#thm-nested-projections .theorem name="Nested projections of Gaussian noise"}

Let $X=(X_0\ X_1)$ have full column rank $p$, with $X_0\in\mathbb R^{n\times p_0}$ ($0<p_0<p$), and let $P$ and $P_0$ be the orthogonal projection matrices onto $\operatorname{col}(X)$ and $\operatorname{col}(X_0)$. Then $PP_0=P_0P=P_0$, and for $\varepsilon\sim N_n(0,\sigma^2I_n)$ the vectors $P_0\varepsilon$, $(P-P_0)\varepsilon$, $(I-P)\varepsilon$ are independent, with
$$\frac{\|P_0\varepsilon\|^2}{\sigma^2}\sim\chi^2_{p_0},\qquad\frac{\|(P-P_0)\varepsilon\|^2}{\sigma^2}\sim\chi^2_{p-p_0},\qquad\frac{\|(I-P)\varepsilon\|^2}{\sigma^2}\sim\chi^2_{n-p}.$$

:::

::: {.proof}

1. $P$ fixes every vector of $\operatorname{col}(X)\supseteq\operatorname{col}(X_0)$, so $PP_0=P_0$; transposing, $P_0P=P_0$.

2. $P-P_0$ is symmetric and $(P-P_0)^2=P-PP_0-P_0P+P_0=P-P_0$, so it is an orthogonal projection matrix of rank $\operatorname{tr}(P-P_0)=p-p_0$ (@prp-projection-rank-trace). It projects onto the orthogonal complement of $\operatorname{col}(X_0)$ inside $\operatorname{col}(X)$.

3. The three matrices $P_0$, $P-P_0$, $I-P$ sum to $I$ and are mutually orthogonal: $P_0(P-P_0)=P_0-P_0=0$, $(P-P_0)(I-P)=P-P-P_0+P_0=0$, and $P_0(I-P)=0$. So their ranges are mutually orthogonal subspaces of dimensions $p_0$, $p-p_0$, $n-p$.

4. Choose orthonormal bases of the three ranges and stack them as the columns of an orthogonal matrix $Q$. As in the proof of @thm-gaussian-projection, $Q^{\mathsf T}\varepsilon\sim N(0,\sigma^2I_n)$, and the three blocks of coordinates are independent with iid $N(0,\sigma^2)$ entries. The three projected vectors are functions of the three blocks and their squared lengths are sums of $p_0$, $p-p_0$, $n-p$ squares.

:::

::: {#fig-anova-nested-models-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[->, muted] (0,0) -- (6.5,0) node[lab, right] {$\operatorname{col}(X_0)$};
\draw[->, muted] (0,0) -- (3,1.6) node[lab, above right] {$\operatorname{col}(X)$};
\node[small vertex] (Y) at (5.3,2.6) {};
\node[lab, above right] at (5.3,2.6) {$Y$};
\node[small vertex] (PY) at (4.6,2.45) {};
\draw[faint] (5.3,2.6) -- (4.6,2.45);
\node[small vertex] (P0Y) at (3.2,0) {};
\draw[emph] (0,0) -- (3.2,0);
\draw[hl] (3.2,0) -- (2.2,1.17);
\draw[faint] (0,0) -- (5.3,2.6);
\node[lab, below] at (3.2,-0.1) {$P_0Y$};
\end{tikzpicture}
\end{center}
```

The data vector $Y$ is projected onto the full model space $\operatorname{col}(X)$ and onto the sub-model space $\operatorname{col}(X_0)$. The part of $Y$ that the full model explains beyond the sub-model is $(P-P_0)Y$; the leftover is $(I-P)Y$. The $F$-test compares the squared lengths of these two pieces, scaled by their dimensions.

:::

::: {#thm-nested-f-test .theorem name="F-test for nested linear models"}

Let $Y\sim N_n(\mu,\sigma^2I_n)$ with $\sigma^2$ unknown, and test $H_0:\mu\in\operatorname{col}(X_0)$ against $H_1:\mu\in\operatorname{col}(X)\setminus\operatorname{col}(X_0)$, with $X_0,X,P_0,P$ as in @thm-nested-projections. Put
$$F=\frac{\|(P-P_0)Y\|^2/(p-p_0)}{\|(I-P)Y\|^2/(n-p)} .$$
Then the generalised likelihood ratio statistic is an increasing function of $F$, and under $H_0$, $F\sim F_{p-p_0,\,n-p}$. Hence the size $\alpha$ generalised likelihood ratio test rejects $H_0$ when $F>F_{p-p_0,n-p}(\alpha)$, the upper $\alpha$ quantile.

:::

::: {.proof}

1. For a model with mean $X\beta$ the log-likelihood is $-\frac n2\log\sigma^2-\|Y-X\beta\|^2/(2\sigma^2)$ up to a constant. Maximising over $\beta$ gives the projection $PY$ (least squares) and then over $\sigma^2$ gives $\hat\sigma^2=\mathrm{RSS}/n$, so the maximum is $-\frac n2\log(\mathrm{RSS}/n)-\frac n2$, with $\mathrm{RSS}=\|(I-P)Y\|^2$. Under the sub-model, $\mathrm{RSS}_0=\|(I-P_0)Y\|^2$.

2. Hence $\Lambda=(\mathrm{RSS}_0/\mathrm{RSS})^{n/2}$. Since $I-P_0=(I-P)+(P-P_0)$ with orthogonal summands, $\mathrm{RSS}_0=\mathrm{RSS}+\|(P-P_0)Y\|^2$ and
$$\Lambda^{2/n}=1+\frac{\|(P-P_0)Y\|^2}{\|(I-P)Y\|^2}=1+\frac{p-p_0}{n-p}F,$$
an increasing function of $F$.

3. Under $H_0$, $\mu\in\operatorname{col}(X_0)$, so $(P-P_0)\mu=0$ and $(I-P)\mu=0$ (as $\operatorname{col}(X_0)\subseteq\operatorname{col}(X)$). Thus $(P-P_0)Y=(P-P_0)\varepsilon$ and $(I-P)Y=(I-P)\varepsilon$.

4. By @thm-nested-projections these are independent with squared lengths $\sigma^2\chi^2_{p-p_0}$ and $\sigma^2\chi^2_{n-p}$, so $F$ is a ratio of independent chi-squared variables divided by their degrees of freedom, which is $F_{p-p_0,n-p}$ (@def-f-distribution).

:::

::: {#def-anova-one-way .definition name="One-way ANOVA model and sums of squares"}

Observe $Y_{ij}=\mu_i+\varepsilon_{ij}$, $j=1,\dots,n_i$, $i=1,\dots,k$, with $\varepsilon_{ij}$ iid $N(0,\sigma^2)$ and $n=\sum_in_i$; test $H_0:\mu_1=\dots=\mu_k$. With group means $\bar Y_{i}$ and grand mean $\bar Y$ put
$$\mathrm{SSA}=\sum_{i=1}^kn_i(\bar Y_{i}-\bar Y)^2,\qquad\mathrm{SSE}=\sum_{i=1}^k\sum_{j=1}^{n_i}(Y_{ij}-\bar Y_i)^2,\qquad\mathrm{SST}=\sum_{i,j}(Y_{ij}-\bar Y)^2 .$$

:::

::: {#thm-anova-f-test .theorem name="One-way ANOVA as a nested model; the F-test"}

The one-way model is the linear model with $X$ the $n\times k$ matrix of group indicators (rank $k$), and $H_0$ is the sub-model $X_0=\mathbf 1$ ($p_0=1$). Then

1. $PY$ has entries $\bar Y_i$ and $P_0Y$ has all entries $\bar Y$;
2. $\mathrm{SSA}=\|(P-P_0)Y\|^2$, $\mathrm{SSE}=\|(I-P)Y\|^2$ and $\mathrm{SST}=\mathrm{SSA}+\mathrm{SSE}$;
3. the size $\alpha$ generalised likelihood ratio test rejects $H_0$ when
$$F=\frac{\mathrm{SSA}/(k-1)}{\mathrm{SSE}/(n-k)}>F_{k-1,n-k}(\alpha).$$

:::

::: {.proof}

1. Least squares on the group indicators fits each group by its mean, so $PY=(\bar Y_i)$; fitting a single constant gives $P_0Y=\bar Y\mathbf 1$.

2. Squaring entrywise gives $\|(P-P_0)Y\|^2=\sum_in_i(\bar Y_i-\bar Y)^2$ and $\|(I-P)Y\|^2=\sum_{i,j}(Y_{ij}-\bar Y_i)^2$. The identity $\mathrm{SST}=\|(I-P_0)Y\|^2=\mathrm{SSA}+\mathrm{SSE}$ is Pythagoras for the orthogonal summands $(P-P_0)Y$ and $(I-P)Y$.

3. Apply @thm-nested-f-test with $p=k$, $p_0=1$.

:::

::: {#exm-anova-table .example name="ANOVA table"}

The quantities are customarily arranged in a table.

| Source | Sum of squares | d.f. | Mean square | $F$ |
|---|---|---|---|---|
| between groups | $\mathrm{SSA}$ | $k-1$ | $\mathrm{MSA}=\mathrm{SSA}/(k-1)$ | $\mathrm{MSA}/\mathrm{MSE}$ |
| within groups | $\mathrm{SSE}$ | $n-k$ | $\mathrm{MSE}=\mathrm{SSE}/(n-k)$ | |
| total | $\mathrm{SST}$ | $n-1$ | | |

:::

::: {#exm-anova-fruit-flies .example name="Three control groups of fruit flies"}

In an experiment on the lifespan of male fruit flies, three control groups of $25$ flies had mean lifespans $63.56$, $64.80$, $63.36$ days with sample standard deviations $16.45$, $15.65$, $14.54$. Here $k=3$, $n=75$, $\bar Y=63.91$, and
$$\mathrm{SSA}=25\sum_i(\bar Y_i-\bar Y)^2\approx30.4,\qquad\mathrm{SSE}=24\sum_is_i^2\approx17\,450,\qquad F=\frac{30.4/2}{17450/72}\approx0.063 .$$
The $p$-value $P(F_{2,72}>0.063)\approx0.94$: there is no evidence that the control groups differ.

:::

::: {#prp-two-sample-t-f .proposition name="Two groups: the t-test and the F-test coincide"}

For $k=2$ with groups of sizes $n$ and $m$ and pooled variance estimate $\hat\sigma^2=\mathrm{SSE}/(n+m-2)$, the $F$ statistic of @thm-anova-f-test equals the square of the two-sample $t$ statistic
$$T=\frac{\bar A-\bar B}{\hat\sigma\sqrt{1/n+1/m}},$$
so rejecting for $|T|>t_{n+m-2}(\alpha/2)$ and for $F>F_{1,n+m-2}(\alpha)$ are the same test.

:::

::: {.proof}

1. With $\bar Y=(n\bar A+m\bar B)/(n+m)$, $\bar A-\bar Y=\frac m{n+m}(\bar A-\bar B)$ and $\bar B-\bar Y=-\frac n{n+m}(\bar A-\bar B)$. So $\mathrm{SSA}=\bigl(\frac{nm^2}{(n+m)^2}+\frac{mn^2}{(n+m)^2}\bigr)(\bar A-\bar B)^2=\frac{nm}{n+m}(\bar A-\bar B)^2$.

2. Since $k-1=1$, $F=\mathrm{SSA}/\hat\sigma^2=\dfrac{(\bar A-\bar B)^2}{\hat\sigma^2(1/n+1/m)}=T^2$.

3. If $T\sim t_\nu$ then $T^2\sim F_{1,\nu}$ (a $\chi^2_1$ divided by an independent $\chi^2_\nu/\nu$), and $|T|>t_\nu(\alpha/2)$ if and only if $T^2>F_{1,\nu}(\alpha)$.

:::

::: {#rmk-f-test-special-cases .remark name="One test, many cases"}

The nested $F$-test of @thm-nested-f-test contains Student's two-sided $t$-test of $H_0:\mu=\mu_0$ (take $X=\mathbf 1$ and the sub-model $\mu=0$ after subtracting $\mu_0$; the proofs above work verbatim with $P_0=0$, $p_0=0$), the $t$-test of a single coefficient $\beta_j=\beta_{0j}$ (the sub-model deletes the $j$-th column), one-way ANOVA, and the two-sample test. For a chain of nested spaces $M_0\subset M_1\subset\dots\subset M_k=\mathbb R^n$ the pieces $(P_j-P_{j-1})Y$ are mutually orthogonal, which is the basis of sequential ANOVA tables.

:::
