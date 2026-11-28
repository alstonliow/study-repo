---
title: "The Arzelà–Ascoli Theorem"
sources: [camii-lan-3, camii-lans-3]
requires: [math/analysis/topology/compact-spaces]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Linear Analysis (lecture notes), Section 3.3, and Example Sheet 3 (question 13), in our own wording; proofs written out in steps. Peano's existence theorem, which the lecture notes derive from this theorem, is not written out. -->

A bounded sequence of continuous functions need not have a uniformly convergent subsequence; bounded and equicontinuous families do. This is the compactness criterion in $C(K)$.

::: {#def-equicontinuous .definition name="Equicontinuous family"}

Let $K$ be a compact metric space. A family $\mathcal F\subseteq C(K)$ is *equicontinuous* if for every $\varepsilon>0$ there is $\delta>0$ such that $|f(x)-f(y)|<\varepsilon$ for all $f\in\mathcal F$ and all $x,y$ with $d(x,y)<\delta$. (For a compact Hausdorff space: for every $x$ and $\varepsilon$ there is a neighbourhood $U$ of $x$ with $|f(y)-f(x)|<\varepsilon$ for $y\in U$ and all $f\in\mathcal F$; on a compact metric space this is equivalent to the uniform version.)

:::

::: {#exm-not-compact-families .example name="Families that fail"}

On $K=[0,1]$ the sequence $f_n=n$ is equicontinuous but unbounded, with no convergent subsequence. The sequence $f_n(x)=x^n$ is bounded by $1$ but not equicontinuous at $1$; it converges pointwise to a discontinuous function, so no subsequence converges uniformly.

:::

::: {#thm-arzela-ascoli .theorem name="Arzelà–Ascoli theorem"}

Let $K$ be a compact metric space. A subset $\mathcal F\subseteq C(K)$ is relatively compact (has compact closure) in the sup norm if and only if it is bounded and equicontinuous. Equivalently, every bounded equicontinuous sequence in $C(K)$ has a uniformly convergent subsequence.

:::

::: {.proof}

1. *Necessity.* A relatively compact set is totally bounded (@thm-compact-iff-complete-totally-bounded), so bounded. Given $\varepsilon$ choose a finite $\varepsilon/3$-net $f_1,\dots,f_m$ of $\mathcal F$. Each $f_i$ is uniformly continuous, so there is $\delta$ with $|f_i(x)-f_i(y)|<\varepsilon/3$ for $d(x,y)<\delta$ and all $i$. For any $f\in\mathcal F$ pick $f_i$ with $\|f-f_i\|<\varepsilon/3$; then $|f(x)-f(y)|<\varepsilon$ for $d(x,y)<\delta$.

2. *Sufficiency, a diagonal argument.* Let $(f_n)$ be bounded and equicontinuous. $K$ is compact metric, hence separable: take a countable dense set $D=\{x_1,x_2,\dots\}$. The sequences $(f_n(x_j))_n$ are bounded in $\mathbb F$, so by Bolzano–Weierstrass and a diagonal extraction there is a subsequence $(g_n)$ with $g_n(x_j)$ convergent for every $j$.

3. *The subsequence is uniformly Cauchy.* Let $\varepsilon>0$ and take $\delta$ from equicontinuity for $\varepsilon/3$. Cover $K$ by finitely many balls $B(x_{j_i},\delta)$ with centres in $D$ (density and compactness). Choose $N$ with $|g_n(x_{j_i})-g_m(x_{j_i})|<\varepsilon/3$ for all $i$ and $n,m\ge N$. For any $x\in K$ pick $i$ with $d(x,x_{j_i})<\delta$; then
$$|g_n(x)-g_m(x)|\le|g_n(x)-g_n(x_{j_i})|+|g_n(x_{j_i})-g_m(x_{j_i})|+|g_m(x_{j_i})-g_m(x)|<\varepsilon.$$

4. So $(g_n)$ is Cauchy in the complete space $C(K)$ and converges uniformly. Applying this to sequences in $\mathcal F$ shows $\mathcal F$ is relatively sequentially compact, hence relatively compact in the metric space $C(K)$.

:::

::: {#fig-arzela-ascoli-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (0,0) -- (5.2,0); \draw[->, faint] (0,0) -- (0,3);
\draw[emph, domain=0:5, samples=40] plot (\x,{1.5+0.7*sin(\x*70)});
\draw[faint, domain=0:5, samples=40] plot (\x,{1.2+0.6*sin(\x*70+40)});
\draw[faint, domain=0:5, samples=40] plot (\x,{1.9+0.5*sin(\x*70-30)});
\draw[hl] (2.0,1.0) rectangle (2.6,1.5); \node[lab, right] at (2.7,1.2) {$\delta,\varepsilon$};
\end{tikzpicture}
\end{center}
```

A bounded equicontinuous family: all curves stay in a band and wiggle at most $\varepsilon$ over any interval of length $\delta$.

:::

::: {#cor-lipschitz-compact .corollary name="A compact family of Lipschitz functions"}

For $L,M>0$ the set $\{f\in C[0,1]:\|f\|_\infty\le M,\ |f(x)-f(y)|\le L|x-y|\}$ is compact in $C[0,1]$.

:::

::: {.proof}

It is bounded and equicontinuous (take $\delta=\varepsilon/L$), so relatively compact; it is closed because the two defining conditions are preserved under uniform limits.

:::

::: {#exm-montel .example name="Montel-type compactness for holomorphic functions"}

Let $U\subseteq\mathbb C$ be open and $(f_n)$ holomorphic functions uniformly bounded on every compact subset. By Cauchy's estimate $|f_n'(z)|\le M/r$ on a disc of radius $r$ about $z$, so on each compact disc the $f_n$ are uniformly Lipschitz, hence equicontinuous. Applying @thm-arzela-ascoli on an exhaustion of $U$ by compact discs and a diagonal argument yields a subsequence converging uniformly on compact subsets.
<!-- Cauchy's estimate is from complex analysis and is not proved in these notes. -->

:::
