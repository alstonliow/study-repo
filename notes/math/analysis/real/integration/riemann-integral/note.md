---
title: "The Riemann Integral"
sources: [cama1-7]
requires: [math/analysis/real/real-numbers/ordered-fields-and-completeness, math/calculus/single-variable/integrals/definite-integral]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Section 7.1, in our own wording; proofs written out in steps. @def-riemann-sum defines the integral as a limit of Riemann sums over equal subintervals; here it is defined by upper and lower sums over arbitrary dissections (Darboux's form), and @thm-regular-dissections connects the two. -->

The integral is defined directly, not as an antiderivative: many functions, such as $e^{-x^2}$, have no antiderivative in closed form but should still have an integral. The idea is to trap the area under $f$ between areas of rectangles lying above and below the graph.

## Upper and lower sums

::: {#def-dissection-upper-lower-sums .definition name="Dissection, upper and lower sums"}

A *dissection* of $[a,b]$ is a finite sequence $D: a=x_0<x_1<\cdots<x_n=b$. For a bounded $f:[a,b]\to\mathbb R$ let $M_i=\sup_{[x_{i-1},x_i]}f$ and $m_i=\inf_{[x_{i-1},x_i]}f$. The *upper* and *lower sums* are
$$U_D(f)=\sum_{i=1}^n(x_i-x_{i-1})M_i,\qquad L_D(f)=\sum_{i=1}^n(x_i-x_{i-1})m_i.$$
A dissection $D'$ *refines* $D$ if every point of $D$ is a point of $D'$. The *mesh* of $D$ is $\max_i(x_i-x_{i-1})$.

:::

Clearly $L_D(f)\le U_D(f)$. Refining can only improve both bounds:

::: {#lem-refinement-sums .lemma name="Refinement"}

If $D'$ refines $D$, then $U_{D'}(f)\le U_D(f)$ and $L_{D'}(f)\ge L_D(f)$. Consequently, for any two dissections $D_1,D_2$,
$$L_{D_1}(f)\le U_{D_2}(f).$$

:::

::: {.proof}

1. Suppose $D'$ adds one point $z\in(x_{i-1},x_i)$ to $D$. Only the $i$-th term of the upper sum changes: $(x_i-x_{i-1})M_i$ is replaced by $(z-x_{i-1})\sup_{[x_{i-1},z]}f+(x_i-z)\sup_{[z,x_i]}f$.

2. Both suprema are over subsets of $[x_{i-1},x_i]$, so each is at most $M_i$, and the new term is at most $(z-x_{i-1})M_i+(x_i-z)M_i=(x_i-x_{i-1})M_i$. So $U_{D'}(f)\le U_D(f)$.

3. A general refinement adds finitely many points one at a time, so induction gives the claim. For lower sums the infima can only increase, by the same argument.

4. For $D_1,D_2$, let $D$ consist of the points of both (their *common refinement*). Then $L_{D_1}(f)\le L_D(f)\le U_D(f)\le U_{D_2}(f)$.

:::

## The integral

::: {#def-riemann-integral-darboux .definition name="Riemann integral" related="def-riemann-sum"}

Let $f:[a,b]\to\mathbb R$ be bounded. Its *upper* and *lower integrals* are
$$\overline{\int_a^b}f=\inf_DU_D(f),\qquad\underline{\int_a^b}f=\sup_DL_D(f),$$
over all dissections $D$ of $[a,b]$. If they are equal, $f$ is *Riemann integrable* and the common value is $\int_a^bf(x)\,dx$.

:::

By @lem-refinement-sums every lower sum is at most every upper sum, so $\underline\int f\le\overline\int f$ always. An unbounded $f$ is not Riemann integrable: on some subinterval of every dissection it is unbounded, so some $M_i$ or $m_i$ is infinite.

::: {#exm-riemann-integral-1 .example name="Integrating $x$ from the definition"}

Let $f(x)=x$ on $[a,b]$ and $D$ any dissection. On $[x_{i-1},x_i]$ the supremum is $x_i$, and $x_i(x_i-x_{i-1})=\frac12(x_i^2-x_{i-1}^2)+\frac12(x_i-x_{i-1})^2$. Summing, the first parts telescope:
$$U_D(f)=\frac{b^2-a^2}2+\frac12\sum_{i=1}^n(x_i-x_{i-1})^2.$$
If the mesh of $D$ is less than $\delta$, the error is at most $\frac\delta2\sum(x_i-x_{i-1})=\frac\delta2(b-a)$. So $\overline\int f\le\frac{b^2-a^2}2$. In the same way $L_D(f)=\frac{b^2-a^2}2-\frac12\sum(x_i-x_{i-1})^2$ gives $\underline\int f\ge\frac{b^2-a^2}2$. Hence $\int_a^bx\,dx=\frac{b^2-a^2}2$.

:::

::: {#exm-dirichlet-function .example name="A function that is not Riemann integrable"}

Let $f(x)=1$ for rational $x\in[0,1]$ and $f(x)=0$ for irrational $x$. Every interval of positive length contains rationals and irrationals, so $M_i=1$ and $m_i=0$ for every dissection. Then $U_D(f)=1$ and $L_D(f)=0$ always, so the upper integral is $1$, the lower integral is $0$, and $f$ is not Riemann integrable.

The rationals are countable, so in a sense $f$ is $0$ "almost everywhere"; the Lebesgue integral, built on measure theory, assigns it the integral $0$. That integral handles limits far better and is the one used in probability.

:::

::: {#thm-riemann-criterion .theorem name="Riemann's criterion"}

A bounded $f:[a,b]\to\mathbb R$ is integrable if and only if for every $\varepsilon>0$ there is a dissection $D$ with
$$U_D(f)-L_D(f)<\varepsilon.$$

:::

::: {.proof}

1. ($\Rightarrow$) Let $I=\int_a^bf$ and $\varepsilon>0$. By the definitions of infimum and supremum there are $D_1,D_2$ with $U_{D_1}(f)<I+\frac\varepsilon2$ and $L_{D_2}(f)>I-\frac\varepsilon2$.

2. For their common refinement $D$, @lem-refinement-sums gives $U_D(f)-L_D(f)\le U_{D_1}(f)-L_{D_2}(f)<\varepsilon$.

3. ($\Leftarrow$) For every $D$, $\underline\int f\ge L_D(f)$ and $\overline\int f\le U_D(f)$, so $0\le\overline\int f-\underline\int f\le U_D(f)-L_D(f)$.

4. If the right side can be made less than any $\varepsilon>0$, the two integrals are equal.

:::

## Equal subintervals suffice

The definition allows all dissections, which makes common refinements easy. For an integrable function, the regular dissections of @def-riemann-sum already give the integral.

::: {#thm-regular-dissections .theorem name="Regular dissections"}

Let $f$ be integrable on $[a,b]$ and let $D_n$ divide $[a,b]$ into $n$ equal parts. Then
$$U_{D_n}(f)\to\int_a^bf\quad\text{and}\quad L_{D_n}(f)\to\int_a^bf.$$
Consequently every Riemann sum $\sum f(c_i)\Delta x$ over $D_n$ also tends to $\int_a^bf$.

:::

::: {.proof}

1. Let $I=\int_a^bf$, $|f|\le C$, and $\varepsilon>0$. Choose a dissection $D$ with $m$ interior points and $U_D(f)<I+\frac\varepsilon2$.

2. Let $D'$ be the common refinement of $D_n$ and $D$, so $U_{D'}(f)\le U_D(f)$. The sums $U_{D_n}(f)$ and $U_{D'}(f)$ differ only on the at most $m$ subintervals of $D_n$ that contain a point of $D$.

3. On such a subinterval, of length $\frac{b-a}n$, both sums contribute a value between $-C\frac{b-a}n$ and $C\frac{b-a}n$, so they differ by at most $2C\frac{b-a}n$. Hence $U_{D_n}(f)\le U_{D'}(f)+2Cm\frac{b-a}n<I+\frac\varepsilon2+2Cm\frac{b-a}n$.

4. For $n>4Cm(b-a)/\varepsilon$ this gives $I\le U_{D_n}(f)<I+\varepsilon$. So $U_{D_n}(f)\to I$; lower sums are similar.

5. A Riemann sum over $D_n$ lies between $L_{D_n}(f)$ and $U_{D_n}(f)$, so it tends to $I$ by the sandwich rule.

:::
