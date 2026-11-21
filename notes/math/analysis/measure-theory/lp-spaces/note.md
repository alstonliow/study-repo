---
title: "Lp Spaces, Completeness and Orthogonal Projection in L2"
sources: [camii-pm-4]
requires: [math/analysis/measure-theory/integral-inequalities, math/analysis/measure-theory/convergence-theorems]
status: draft
---

<!-- Added 2026-11-21 from Cambridge Part II Probability and Measure (Michaelmas 2016 lecture notes), Sections 4.2 and 4.3, in our own wording; proofs written out in steps. The projection theorem for random variables (math/probability/estimation/linear-estimation) is the special case of a probability space. -->

::: {#def-lp-space .definition name="$L^p$ spaces"}

Let $(E,\mathcal E,\mu)$ be a measure space and $1\le p\le\infty$. $\mathcal L^p=\mathcal L^p(E,\mathcal E,\mu)$ is the set of measurable $f:E\to\mathbb R$ with $\|f\|_p<\infty$, where

$$
\|f\|_p=\Big(\int_E|f|^p\,d\mu\Big)^{1/p}\quad(p<\infty),\qquad\|f\|_\infty=\inf\{c\ge0:\ |f|\le c\ \text{a.e.}\}.
$$

$L^p$ is the quotient of $\mathcal L^p$ by the relation $f\sim g\iff f=g$ a.e.

:::

$\mathcal L^p$ is a vector space by Minkowski (@thm-minkowski-inequality), and $\|\cdot\|_p$ is a seminorm on it with $\|f\|_p=0$ exactly when $f=0$ a.e. (@thm-integral-linear-monotone; for $p=\infty$, $|f|\le\frac1n$ a.e. for all $n$). So $\|\cdot\|_p$ is a norm on $L^p$ (@def-norm). As usual we treat elements of $L^p$ as functions, remembering that they are defined only up to null sets. If $\mu(E)<\infty$ and $p\le r$, Hölder with exponents $\frac rp$ and its conjugate gives $\|f\|_p\le\mu(E)^{\frac1p-\frac1r}\|f\|_r$, so $L^r\subseteq L^p$.

::: {#thm-lp-complete .theorem name="$L^p$ is complete (Riesz–Fischer)"}

For $1\le p\le\infty$, $L^p$ is a Banach space: every Cauchy sequence $(f_n)$ in $L^p$ converges in $L^p$ to some $f\in L^p$. Moreover, a subsequence converges to $f$ almost everywhere.

:::

::: {.proof}

1. Let $p<\infty$. Choose $n_1<n_2<\cdots$ with $\|f_{n_{k+1}}-f_{n_k}\|_p\le2^{-k}$. Put $S=\sum_k|f_{n_{k+1}}-f_{n_k}|$.

2. By monotone convergence and Minkowski applied to partial sums, $\|S\|_p\le\sum_k2^{-k}=1$, so $S<\infty$ a.e. Off this null set the series $f_{n_1}+\sum_k(f_{n_{k+1}}-f_{n_k})$ converges absolutely; call its sum $f$, and put $f=0$ on the null set. Then $f$ is measurable and $f_{n_k}\to f$ a.e.

3. Fix $\varepsilon>0$ and $N$ with $\|f_n-f_m\|_p\le\varepsilon$ for $n,m\ge N$. For $n\ge N$, Fatou's lemma (@thm-fatou-lemma) along the subsequence gives
$$\|f_n-f\|_p^p=\mu\big(\liminf_k|f_n-f_{n_k}|^p\big)\le\liminf_k\|f_n-f_{n_k}\|_p^p\le\varepsilon^p .$$

4. So $f_n-f\in L^p$, hence $f\in L^p$, and $\|f_n-f\|_p\to0$.

5. For $p=\infty$: the set $N=\bigcup_{n,m}\{|f_n-f_m|>\|f_n-f_m\|_\infty\}$ is a countable union of null sets. Off $N$ the sequence is uniformly Cauchy, so it converges uniformly to some $f$ (set $f=0$ on $N$), and $\|f_n-f\|_\infty\le\sup_{m\ge n}\|f_n-f_m\|_\infty\to0$.

:::

## $L^2$ as a Hilbert space

$L^2$ carries the inner product $\langle f,g\rangle=\mu(fg)$, finite by Cauchy–Schwarz, with $\langle f,f\rangle=\|f\|_2^2$. By @thm-lp-complete it is a *Hilbert space*: a complete inner product space. Expanding the inner product gives

$$
\|f+g\|_2^2=\|f\|_2^2+2\langle f,g\rangle+\|g\|_2^2,\qquad\|f+g\|_2^2+\|f-g\|_2^2=2\|f\|_2^2+2\|g\|_2^2,
$$

Pythagoras ($\langle f,g\rangle=0$ gives $\|f+g\|^2=\|f\|^2+\|g\|^2$) and the parallelogram law.

::: {#thm-l2-orthogonal-projection .theorem name="Orthogonal projection in $L^2$" generalizes="thm-projection-random-variables"}

Let $V$ be a closed subspace of $L^2$. Every $f\in L^2$ has a unique decomposition

$$
f=v+u,\qquad v\in V,\quad\langle u,w\rangle=0\ \text{for all }w\in V .
$$

The *orthogonal projection* $v$ is the unique point of $V$ nearest to $f$: $\|f-v\|_2=\inf_{w\in V}\|f-w\|_2$.

:::

::: {.proof}

1. Let $d=\inf_{w\in V}\|f-w\|_2$ and choose $w_n\in V$ with $\|f-w_n\|_2\to d$.

2. The parallelogram law applied to $f-w_n$ and $f-w_m$ gives
$$\|w_n-w_m\|_2^2=2\|f-w_n\|_2^2+2\|f-w_m\|_2^2-4\Big\|f-\tfrac{w_n+w_m}2\Big\|_2^2 .$$
The midpoint lies in $V$, so the last norm is at least $d$, and the right side tends to $2d^2+2d^2-4d^2=0$. So $(w_n)$ is Cauchy.

3. By completeness $w_n\to v$ in $L^2$, and $v\in V$ because $V$ is closed. Continuity of the norm gives $\|f-v\|_2=d$.

4. Let $u=f-v$ and $w\in V$. For real $t$, $v+tw\in V$, so $g(t)=\|u-tw\|_2^2=\|u\|_2^2-2t\langle u,w\rangle+t^2\|w\|_2^2\ge d^2=g(0)$. A quadratic with a minimum at $t=0$ has zero derivative there: $\langle u,w\rangle=0$.

5. Uniqueness: if $f=v+u=v'+u'$ are two such decompositions, then $v-v'=u'-u$ lies in $V$ and is orthogonal to $V$, hence to itself, so it is $0$. The nearest-point characterisation follows from Pythagoras: $\|f-w\|_2^2=\|u\|_2^2+\|v-w\|_2^2$ for $w\in V$.

:::

::: {#fig-lp-spaces-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (-0.5,-0.6) -- (4.2,-0.6) -- (5.2,0.9) -- (0.5,0.9) -- cycle;
\node[lab] at (4.4,0.6) {$V$};
\draw[->, emph] (0.6,0) -- (3.2,2.6) node[lab, above] {$f$};
\draw[->, emph] (0.6,0) -- (3.2,0.2) node[lab, below right] {$v$};
\draw[->, hl] (3.2,0.2) -- (3.2,2.6);
\node[lab, right, text=accent] at (3.2,1.4) {$u=f-v\perp V$};
\draw[faint] (3.0,0.185) -- (3.0,0.385) -- (3.2,0.4);
\end{tikzpicture}
\end{center}
```

Orthogonal projection onto a closed subspace $V$ of $L^2$: $f=v+u$ with $v\in V$ the nearest point and $u$ orthogonal to $V$. Completeness of $L^2$ makes the minimising sequence converge.

:::

::: {#prp-conditional-expectation-projection .proposition name="Conditional expectation on a partition is a projection" related="thm-mmse-conditional-expectation"}

Let $(\Omega,\mathcal F,\Pr)$ be a probability space, $G_1,G_2,\dots$ a partition of $\Omega$ into events of positive probability, $\mathcal G=\sigma(G_n:n\ge1)$, and $X\in L^2(\Pr)$. Then

$$
Y=\sum_n\frac{E[X\mathbf 1_{G_n}]}{\Pr(G_n)}\,\mathbf 1_{G_n}
$$

is the orthogonal projection of $X$ onto the closed subspace $L^2(\mathcal G)$ of $\mathcal G$-measurable elements of $L^2$. It is the *conditional expectation* $E[X\mid\mathcal G]$.

:::

::: {.proof}

1. $\mathcal G$ consists of all unions of some of the $G_n$, so a $\mathcal G$-measurable $W$ is constant on each $G_n$: $W=\sum_na_n\mathbf 1_{G_n}$. Write $b_n=E[X\mathbf 1_{G_n}]/\Pr(G_n)$.

2. $L^2(\mathcal G)$ is closed: an $L^2$-limit of $\mathcal G$-measurable functions has an a.e.-convergent subsequence (@thm-lp-complete), whose limit is $\mathcal G$-measurable.

3. $Y\in L^2$: by Cauchy–Schwarz on $G_n$, $b_n^2\Pr(G_n)\le E[X^2\mathbf 1_{G_n}]$; sum over $n$.

4. $X-Y$ is orthogonal to $L^2(\mathcal G)$: for $W=\sum a_n\mathbf 1_{G_n}\in L^2$, $E[(X-Y)\mathbf 1_{G_n}]=E[X\mathbf 1_{G_n}]-b_n\Pr(G_n)=0$, and summing (justified by dominated convergence, with $|(X-Y)W|$ integrable) gives $E[(X-Y)W]=0$.

5. By uniqueness in @thm-l2-orthogonal-projection, $Y$ is the projection.

:::

So $E[X\mid\mathcal G]$ is the best mean-square prediction of $X$ from the information in $\mathcal G$. The covariance of $X,Y\in L^2(\Pr)$ is $\operatorname{Cov}(X,Y)=\langle X-E[X],\,Y-E[Y]\rangle$, and $\operatorname{Var}(X)=\|X-E[X]\|_2^2$ (@def-covariance).
