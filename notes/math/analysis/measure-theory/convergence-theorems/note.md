---
title: "Fatou's Lemma, Dominated Convergence and Differentiation under the Integral"
sources: [camii-pm-3]
requires: [math/analysis/measure-theory/lebesgue-integral, math/analysis/real/integration/fundamental-theorem-of-calculus]
status: draft
---

<!-- Added 2026-11-21 from Cambridge Part II Probability and Measure (Michaelmas 2016 lecture notes), Sections 3.2 and 3.4, in our own wording; proofs written out in steps. The continuity of parameter integrals is our own addition. -->

When does $\lim_n\int f_n=\int\lim_nf_n$? Monotone convergence (@thm-monotone-convergence-integral) handles increasing sequences. Two more theorems cover most other cases. $(E,\mathcal E,\mu)$ is a measure space.

::: {#exm-limits-and-integrals-fail .example name="Mass can escape"}

On $\mathbb R$ with Lebesgue measure, each of the following sequences tends to $0$ pointwise, yet every term has integral $1$:

$$
f_n=\mathbf 1_{[n,n+1]}\ \text{(escape to infinity)},\qquad f_n=n\mathbf 1_{(0,1/n)}\ \text{(concentration)},\qquad f_n=\tfrac1n\mathbf 1_{[0,n]}\ \text{(spreading out)} .
$$

:::

::: {#fig-convergence-theorems-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.1,0) -- (3.3,0);
\node[tick] at (1.6,-0.3) {escape};
\draw[faint] (4.10,0) -- (7.5,0);
\node[tick] at (5.80,-0.3) {concentrate};
\draw[faint] (7.30,0) -- (10.7,0);
\node[tick] at (9.0,-0.3) {spread};
\draw[emph] (0.2,0) rectangle (1.0,0.8);
\draw[emph] (1.2,0) rectangle (2.0,0.8);
\draw[emph] (2.2,0) rectangle (3.0,0.8);
\node[tick] at (3.0,0.6) {$\cdots$};
\draw[emph] (4.2,0) rectangle (5.40,0.67);
\draw[emph] (4.2,0) rectangle (4.80,1.33);
\draw[emph] (4.2,0) rectangle (4.50,2.67);
\draw[emph] (7.4,0) rectangle (8.20,1.00);
\draw[emph] (7.4,0) rectangle (9.00,0.50);
\draw[emph] (7.4,0) rectangle (10.60,0.25);
\end{tikzpicture}
\end{center}
```

Three ways for $f_n\to0$ pointwise while $\int f_n=1$: the mass moves off to infinity, piles up near a point, or spreads out thinly. No integrable function dominates any of these sequences.

:::

::: {#thm-fatou-lemma .theorem name="Fatou's lemma"}

For measurable $f_n:E\to[0,\infty]$,

$$
\mu\big(\liminf_nf_n\big)\le\liminf_n\mu(f_n).
$$

:::

::: {.proof}

1. Put $g_n=\inf_{k\ge n}f_k$. These are measurable (@prp-measurable-closure) and $g_n\uparrow\liminf_nf_n$.

2. For $k\ge n$, $g_n\le f_k$, so $\mu(g_n)\le\inf_{k\ge n}\mu(f_k)$.

3. By monotone convergence $\mu(\liminf f_n)=\lim_n\mu(g_n)\le\lim_n\inf_{k\ge n}\mu(f_k)=\liminf_n\mu(f_n)$.

:::

The examples above show that the inequality can be strict.

::: {#thm-dominated-convergence .theorem name="Dominated convergence theorem"}

Let $f_n,f$ be measurable with $f_n\to f$ pointwise a.e., and suppose there is an integrable $g$ with $|f_n|\le g$ for all $n$. Then $f_n$ and $f$ are integrable and

$$
\mu(|f_n-f|)\to0,\qquad\text{in particular}\qquad\mu(f_n)\to\mu(f).
$$

:::

::: {.proof}

1. Changing all functions on a null set does not change any integral (@thm-integral-linear-monotone), so assume $f_n\to f$ and $|f_n|\le g$ everywhere. Then $|f|\le g$, and $f_n$, $f$ are integrable.

2. The functions $2g-|f_n-f|$ are non-negative and tend to $2g$. By Fatou,
$$\mu(2g)\le\liminf_n\mu(2g-|f_n-f|)=\mu(2g)-\limsup_n\mu(|f_n-f|).$$

3. $\mu(2g)$ is finite, so $\limsup_n\mu(|f_n-f|)\le0$. Finally $|\mu(f_n)-\mu(f)|\le\mu(|f_n-f|)$.

:::

::: {#cor-bounded-convergence-finite-measure .corollary name="Bounded convergence on a finite measure space"}

If $\mu(E)<\infty$, $f_n\to f$ a.e. and $|f_n|\le C$ for a constant $C$, then $\mu(f_n)\to\mu(f)$.

:::

::: {.proof}

The constant $C$ is integrable because $\mu(E)<\infty$; apply dominated convergence.

:::

## Integrals depending on a parameter

::: {#prp-parameter-integral-continuous .proposition name="Continuity of a parameter integral"}

Let $U\subseteq\mathbb R$ and $f:U\times E\to\mathbb R$ with $x\mapsto f(t,x)$ measurable for each $t$, $t\mapsto f(t,x)$ continuous for each $x$, and $|f(t,x)|\le g(x)$ for an integrable $g$. Then $F(t)=\int_Ef(t,x)\,d\mu(x)$ is continuous on $U$.

:::

::: {.proof}

Let $t_n\to t$ in $U$. Then $f(t_n,\cdot)\to f(t,\cdot)$ pointwise with $|f(t_n,\cdot)|\le g$, so $F(t_n)\to F(t)$ by dominated convergence. Sequential continuity is continuity.

:::

::: {#thm-differentiation-under-integral .theorem name="Differentiation under the integral sign"}

Let $U\subseteq\mathbb R$ be open and $f:U\times E\to\mathbb R$ such that

1. $x\mapsto f(t,x)$ is integrable for every $t\in U$;
2. $t\mapsto f(t,x)$ is differentiable for every $x\in E$;
3. $\big|\frac{\partial f}{\partial t}(t,x)\big|\le g(x)$ for all $t,x$, with $g$ integrable.

Then $x\mapsto\frac{\partial f}{\partial t}(t,x)$ is integrable, $F(t)=\int_Ef(t,x)\,d\mu(x)$ is differentiable on $U$, and

$$
F'(t)=\int_E\frac{\partial f}{\partial t}(t,x)\,d\mu(x).
$$

:::

::: {.proof}

1. Fix $t\in U$ and $h_n\to0$, $h_n\neq0$, with $t+h_n\in U$. The difference quotients $q_n(x)=\frac{f(t+h_n,x)-f(t,x)}{h_n}$ are measurable and tend to $\frac{\partial f}{\partial t}(t,x)$. So the partial derivative is measurable, and integrable because it is bounded by $g$.

2. By the mean value theorem $q_n(x)=\frac{\partial f}{\partial t}(s,x)$ for some $s$ between $t$ and $t+h_n$, provided the segment lies in $U$, which holds for large $n$ since $U$ is open. Hence $|q_n|\le g$.

3. By dominated convergence $\frac{F(t+h_n)-F(t)}{h_n}=\mu(q_n)\to\mu\big(\frac{\partial f}{\partial t}(t,\cdot)\big)$. As this holds for every sequence $h_n\to0$, $F$ is differentiable at $t$ with the stated derivative.

:::

::: {#prp-change-of-variables-lebesgue .proposition name="Change of variables on an interval"}

Let $\phi:[a,b]\to\mathbb R$ be continuously differentiable and increasing. For every bounded Borel $g$ on $[\phi(a),\phi(b)]$,

$$
\int_{\phi(a)}^{\phi(b)}g(y)\,dy=\int_a^bg(\phi(x))\,\phi'(x)\,dx .
$$

:::

::: {.proof}

1. Let $V$ be the set of bounded Borel $g$ for which the formula holds. It is a vector space by linearity of both sides.

2. For $g=\mathbf 1_{[u,v]}$ with $[u,v]\subseteq[\phi(a),\phi(b)]$, $g\circ\phi$ is the indicator of an interval $[s,r]$ with $\phi(s)=u$, $\phi(r)=v$ (by the intermediate value theorem, $\phi$ being increasing), and the right-hand side is $\int_s^r\phi'=\phi(r)-\phi(s)=v-u$ by the fundamental theorem of calculus (@thm-ftc-integrable-derivative). The constant $1$ is the case $[u,v]=[\phi(a),\phi(b)]$.

3. If $0\le g_n\uparrow g$ with $g_n\in V$ and $g$ bounded, both sides converge by monotone convergence (note $\phi'\ge0$), so $g\in V$.

4. The closed intervals with $\emptyset$ form a π-system generating the Borel sets, so the monotone class theorem (@thm-monotone-class) gives all bounded Borel $g$.

:::
