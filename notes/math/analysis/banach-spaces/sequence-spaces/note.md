---
title: "Sequence Spaces and Their Duals"
sources: [camii-lan-1, camii-lans-1]
requires: [math/analysis/banach-spaces/bounded-linear-maps, math/analysis/measure-theory/integral-inequalities]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Linear Analysis (lecture notes), Sections 1.1 and 1.5, and Example Sheet 1 (questions 1, 4, 5), in our own wording; proofs written out in steps. -->

The sequence spaces are the basic infinite-dimensional examples, and computing their duals shows what "the dual" means concretely. Hölder's inequality is used as proved in @sec-math-analysis-measure-theory-integral-inequalities (for sums it is the same statement for counting measure).

::: {#def-sequence-spaces .definition name="The spaces $\ell^p$, $\ell^\infty$ and $c_0$"}

For $1\le p<\infty$, $\ell^p$ is the space of scalar sequences $x=(x_n)$ with $\|x\|_p=\big(\sum_n|x_n|^p\big)^{1/p}<\infty$. Further $\ell^\infty$ is the space of bounded sequences with $\|x\|_\infty=\sup_n|x_n|$, and $c_0\subseteq\ell^\infty$ is the subspace of sequences tending to $0$. Write $e_n$ for the $n$-th unit sequence.

:::

::: {#thm-sequence-spaces-complete .theorem name="Completeness of the sequence spaces"}

$\ell^p$ ($1\le p\le\infty$) and $c_0$ are Banach spaces.

:::

::: {.proof}

1. Let $(x^{(k)})$ be Cauchy in $\ell^p$. Each coordinate sequence $(x^{(k)}_n)_k$ is Cauchy in $\mathbb F$, so converges to some $x_n$.

2. Fix $\varepsilon>0$ and $N$ with $\|x^{(k)}-x^{(l)}\|_p<\varepsilon$ for $k,l\ge N$. For each finite $M$, $\sum_{n\le M}|x^{(k)}_n-x^{(l)}_n|^p<\varepsilon^p$; let $l\to\infty$, then $M\to\infty$, to get $\|x^{(k)}-x\|_p\le\varepsilon$ for $k\ge N$.

3. In particular $x-x^{(N)}\in\ell^p$, so $x\in\ell^p$, and $x^{(k)}\to x$. For $p=\infty$ the same argument works with suprema.

4. $c_0$ is a closed subspace of $\ell^\infty$: if $x^{(k)}\to x$ in $\ell^\infty$ with $x^{(k)}\in c_0$, given $\varepsilon$ pick $k$ with $\|x-x^{(k)}\|_\infty<\varepsilon/2$ and then $n_0$ beyond which $|x^{(k)}_n|<\varepsilon/2$; so $|x_n|<\varepsilon$ for $n\ge n_0$. A closed subspace of a Banach space is Banach (@thm-closed-subspace-complete).

:::

::: {#prp-inclusions-lp .proposition name="Inclusions between the sequence spaces"}

For $1\le p<q<\infty$, $\ell^p\subsetneq\ell^q\subsetneq c_0\subsetneq\ell^\infty$, and $\|x\|_q\le\|x\|_p$. The union $\bigcup_{p<\infty}\ell^p$ is a proper subset of $c_0$.

:::

::: {.proof}

1. If $x\in\ell^p$ then $|x_n|\to0$, and $|x_n|\le\|x\|_p$ for all $n$. For $n$ large $|x_n|\le1$, so $|x_n|^q\le|x_n|^p$ and $x\in\ell^q$. Normalising $\|x\|_p=1$ gives $|x_n|\le1$ and $\sum|x_n|^q\le\sum|x_n|^p=1$, so $\|x\|_q\le\|x\|_p$ in general.

2. The inclusions are strict: $x_n=n^{-1/p}$ lies in $\ell^q$ but not in $\ell^p$; $x_n=1/\log(n+1)$ lies in $c_0$ but in no $\ell^p$ (this also shows the union is proper); $(1,1,1,\dots)\in\ell^\infty\setminus c_0$.

:::

::: {#fig-sequence-spaces-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,0) ellipse (3.6 and 1.6); \node[lab] at (3.0,0) {$\ell^\infty$};
\draw[faint] (-0.3,0) ellipse (2.7 and 1.3); \node[lab] at (2.1,0) {$c_0$};
\draw[faint] (-0.6,0) ellipse (1.8 and 1.0); \node[lab] at (1.2,0) {$\ell^q$};
\draw[emph] (-0.9,0) ellipse (0.9 and 0.6); \node[lab] at (-0.9,0) {$\ell^p$};
\end{tikzpicture}
\end{center}
```

For $p<q<\infty$: $\ell^p\subsetneq\ell^q\subsetneq c_0\subsetneq\ell^\infty$.

:::

::: {#thm-dual-lp .theorem name="Duals of the sequence spaces"}

Let $1\le p<\infty$ and let $q\in(1,\infty]$ be the conjugate exponent, $\frac1p+\frac1q=1$. Then $y\mapsto\varphi_y$, $\varphi_y(x)=\sum_nx_ny_n$, is an isometric isomorphism $\ell^q\to(\ell^p)^*$. Likewise $(c_0)^*\cong\ell^1$ isometrically, so in particular $(\ell^1)^*\cong\ell^\infty$ and $(c_0)^{*}\cong\ell^1$.

:::

::: {.proof}

1. *Well defined and norm at most $\|y\|_q$.* By Hölder, $\sum|x_ny_n|\le\|x\|_p\|y\|_q$, so $\varphi_y$ is a bounded linear functional with $\|\varphi_y\|\le\|y\|_q$. (For $p=1$ this is $|\sum x_ny_n|\le\|x\|_1\sup|y_n|$.)

2. *Norm equals $\|y\|_q$.* For $1<p<\infty$ test on $x_n=|y_n|^{q-1}\overline{\operatorname{sgn}y_n}$ (truncated to finitely many terms): this gives $\varphi_y(x)=\sum|y_n|^q$ and $\|x\|_p=(\sum|y_n|^q)^{1/p}$, so $\|\varphi_y\|\ge(\sum|y_n|^q)^{1/q}$. For $p=1$ test on $e_n$: $\varphi_y(e_n)=y_n$ and $\|e_n\|_1=1$.

3. *Onto.* Let $\varphi\in(\ell^p)^*$ and put $y_n=\varphi(e_n)$. The finitely supported sequences are dense in $\ell^p$ (since $p<\infty$), and $\varphi$ and $\varphi_y$ agree on them. So $\varphi=\varphi_y$ once we know $y\in\ell^q$: apply $\varphi$ to the truncated test vector of step 2 to get $\sum_{n\le N}|y_n|^q\le\|\varphi\|(\sum_{n\le N}|y_n|^q)^{1/p}$, hence $(\sum_{n\le N}|y_n|^q)^{1/q}\le\|\varphi\|$ for all $N$.

4. *$c_0$.* The same proof with $c_0$ in place of $\ell^p$ and $\ell^1$ in place of $\ell^q$: the finitely supported sequences are dense in $c_0$, and testing on $x_n=\overline{\operatorname{sgn}y_n}$ for $n\le N$ shows $\sum_{n\le N}|y_n|\le\|\varphi\|$.

:::

::: {#rmk-sequence-spaces-1 .remark name="$\ell^\infty$ has a larger dual"}

The same map $\ell^1\to(\ell^\infty)^*$ is an isometric embedding but is **not** onto: finitely supported sequences are not dense in $\ell^\infty$, and the Hahn–Banach theorem produces functionals (Banach limits) vanishing on $c_0$. So $\ell^1$ is the dual of $c_0$, and $\ell^\infty$ is the dual of $\ell^1$, but $c_0$ is not reflexive (@sec-math-analysis-banach-spaces-double-dual).

:::
