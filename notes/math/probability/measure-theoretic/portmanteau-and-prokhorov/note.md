---
title: "The Portmanteau Theorem, Tightness and Prokhorov's Theorem"
sources: [camiii-ap-4]
requires: [math/probability/measure-theoretic/weak-convergence]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Advanced Probability (lecture notes), Section 4, in our own wording; proofs written out in steps. -->

Weak convergence (@def-weak-convergence) compares measures only through bounded continuous test functions, so it says little about the measure of a given set: $\delta_{x_n}\to\delta_x$ weakly when $x_n\to x$, yet $\delta_{x_n}(\{x\})=0\not\to1$. The portmanteau theorem says exactly which sets still behave. Let $(M,d)$ be a metric space with its Borel σ-algebra, and write $\mu(f)=\int f\,d\mu$.

::: {#thm-portmanteau .theorem name="Portmanteau theorem"}

For Borel probability measures $\mu_n,\mu$ on $M$ the following are equivalent:

1. $\mu_n\Rightarrow\mu$ (weak convergence).
2. $\liminf_n\mu_n(G)\ge\mu(G)$ for every open $G$.
3. $\limsup_n\mu_n(A)\le\mu(A)$ for every closed $A$.
4. $\mu_n(A)\to\mu(A)$ for every Borel $A$ with $\mu(\partial A)=0$.
5. (if $M=\mathbb R$) $F_{\mu_n}(x)\to F_\mu(x)$ at every continuity point $x$ of $F_\mu$, where $F_\mu(x)=\mu((-\infty,x])$.

:::

::: {.proof}

1. *(1)⇒(2).* For open $G$ put $f_N(x)=1\wedge N\,d(x,G^c)$. Then $f_N$ is continuous, $f_N\le\mathbf 1_G$ and $f_N\uparrow\mathbf 1_G$. So $\liminf_n\mu_n(G)\ge\lim_n\mu_n(f_N)=\mu(f_N)\to\mu(G)$ as $N\to\infty$ (monotone convergence).

2. *(2)⇔(3)* by taking complements.

3. *(2)+(3)⇒(4).* If $\mu(\partial A)=0$ then $\mu(\mathring A)=\mu(A)=\mu(\bar A)$. Then $\liminf\mu_n(A)\ge\liminf\mu_n(\mathring A)\ge\mu(\mathring A)=\mu(A)$ and $\limsup\mu_n(A)\le\limsup\mu_n(\bar A)\le\mu(\bar A)=\mu(A)$.

4. *(4)⇒(1).* For bounded continuous $f\ge0$, $\mu(f)=\int_0^\infty\mu(f\ge t)\,dt$ (Tonelli). Since $\partial\{f\ge t\}\subseteq\{f=t\}$ and the sets $\{f=t\}$ are disjoint, $\mu(f=t)>0$ for at most countably many $t$. For all other $t$, (4) gives $\mu_n(f\ge t)\to\mu(f\ge t)$; bounded convergence yields $\mu_n(f)\to\mu(f)$. For general $f$ add a constant.

5. *(4)⇒(5).* If $x$ is a continuity point of $F_\mu$, then $\mu(\partial(-\infty,x])=\mu(\{x\})=0$, so $F_{\mu_n}(x)=\mu_n((-\infty,x])\to F_\mu(x)$.

6. *(5)⇒(2) for $M=\mathbb R$* (and then (2) gives (1) on $\mathbb R$). For an open interval $(a,b)$ and continuity points $a\le a'\le b'\le b$ of $F_\mu$, $\mu_n((a,b))\ge F_{\mu_n}(b')-F_{\mu_n}(a')$ so $\liminf\mu_n((a,b))\ge\mu((a',b'])$; taking the supremum over such $a',b'$ (continuity points are dense) gives $\ge\mu((a,b))$. An open set is a countable disjoint union of open intervals; Fatou for sums gives (2).

:::

::: {#exm-weak-convergence-sets .example name="What can go wrong"}

1. $\delta_{x_n}\Rightarrow\delta_x$ if $x_n\to x$, but $\delta_{x_n}(\{x\})=0$ for $x_n\ne x$: the closed set $\{x\}$ has $\mu(\partial A)=1\ne0$ and (4) does not apply, only the inequality (3).
2. On $[0,1]$, $\mu_n=\frac1n\sum_{k=1}^n\delta_{k/n}\Rightarrow$ Lebesgue measure, since $\mu_n(f)$ is a Riemann sum of $f$. Yet $\mu_n(\mathbb Q)=1$ and $\lambda(\mathbb Q)=0$.

:::

::: {#fig-portmanteau-and-prokhorov-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-0.2,0) -- (6.2,0);
\draw[box] (1.0,0.1) rectangle (4.0,0.7);
\node[lab] at (2.5,0.4) {$A$};
\foreach \x in {4.0,3.7,3.5,3.35} {\node[small vertex, fill=accentLight, draw=accent] at (\x,1.3) {};}
\node[small vertex, fill=accentLight, draw=accent] at (4.0,2.2) {};
\node[tick] at (4.0,2.6) {$\delta_x$ with $x\in\partial A$};
\draw[faint, ->] (3.35,1.2) -- (3.95,0.8);
\node[lab, text=accent] at (5.1,1.3) {$\delta_{x_n}\to\delta_x$};
\end{tikzpicture}
\end{center}
```

Mass can sit just outside the boundary of $A$ and enter in the limit: for $A=[1,4]$ and $x=4$, the points $x_n>4$ approach $x$ from outside. Weak convergence only forbids mass from *leaving* closed sets in the limit ($\limsup\mu_n(A)\le\mu(A)$).

:::

::: {#def-tight .definition name="Tightness"}

A sequence of probability measures $(\mu_n)$ on $M$ is *tight* if for every $\varepsilon>0$ there is a compact $K\subseteq M$ with $\sup_n\mu_n(M\setminus K)\le\varepsilon$.

:::

Every sequence on a compact space is tight. Tightness prevents mass from escaping to infinity: $\mu_n(A)=\lambda(A\cap[n,n+1])$ on $\mathbb R$ gives $\mu_n(S)\to0$ for every bounded $S$, so a weak limit would be the zero measure, not a probability measure.

::: {#thm-prokhorov .theorem name="Prokhorov's theorem (on $\mathbb R$)"}

Every tight sequence $(\mu_n)$ of probability measures on $\mathbb R$ has a weakly convergent subsequence (with a probability measure as limit). (The theorem holds on any complete separable metric space; we prove $M=\mathbb R$.)

:::

::: {.proof}

1. Let $x_1,x_2,\dots$ enumerate $\mathbb Q$ and $F_n=F_{\mu_n}$. Since $0\le F_n\le1$, a diagonal argument (Bolzano–Weierstrass repeatedly) gives a subsequence with $F_{n_k}(x_i)\to F(x_i)$ for every $i$.

2. $F$ is non-decreasing on $\mathbb Q$; extend it to $\mathbb R$ by $F(x)=\inf_{q>x}F(q)$. Then $F$ is non-decreasing and right-continuous.

3. Let $x$ be a continuity point of $F$ and $\varepsilon>0$. Choose rationals $s<x<t$ with $F(t)-F(s)<\varepsilon/2$ and $k$ so large that $|F_{n_k}-F|<\varepsilon/4$ at $s$ and $t$. By monotonicity of $F_{n_k}$ and $F$: $|F_{n_k}(x)-F(x)|\le|F(t)-F(s)|+|F_{n_k}(s)-F(s)|+|F_{n_k}(t)-F(t)|\le\varepsilon$.

4. By tightness, for each $\varepsilon$ there is $N$ with $\mu_n((-\infty,-N])\le\varepsilon$ and $\mu_n((N,\infty))\le\varepsilon$ for all $n$. Thus $F(-N)\le\varepsilon$ and $F(N)\ge1-\varepsilon$ in the limit, so $F(x)\to0$ at $-\infty$ and $\to1$ at $+\infty$: $F$ is a distribution function, of a probability measure $\mu$. By step 3 and (5)⇒(1) of @thm-portmanteau, $\mu_{n_k}\Rightarrow\mu$.

:::

::: {#lem-levy-tightness .lemma name="Tails from the characteristic function"}

Let $X$ be a real random variable with characteristic function $\varphi$ and law $\mu_X$. For all $\lambda>0$,

$$
\mu_X(\{|x|\ge\lambda\})\le c\,\lambda\int_0^{1/\lambda}\big(1-\operatorname{Re}\varphi(t)\big)\,dt,\qquad c=(1-\sin1)^{-1}.
$$

:::

::: {.proof}

1. For $M\ge1$, $\int_0^M(1-\cos t)\,dt=M-\sin M\ge M(1-\sin1)$. With $M=|x|/\lambda$ this gives $\mathbf 1_{\{|x|\ge\lambda\}}\le c\,\frac\lambda{|x|}\int_0^{|x|/\lambda}(1-\cos t)\,dt$.

2. The substitution $t\mapsto|x|t$ turns the right side into $c\lambda\int_0^{1/\lambda}(1-\cos(xt))\,dt$. Integrate against $\mu_X$ and use $\operatorname{Re}\varphi(t)=E[\cos(Xt)]$ (Tonelli).

:::

::: {#thm-levy-continuity-strong .theorem name="Lévy's continuity theorem, strong form" related="thm-levy-continuity"}

Let $X_n$ be real random variables with $\varphi_{X_n}(t)\to\psi(t)$ for every $t$, where $\psi$ is continuous at $0$ and $\psi(0)=1$. Then $\psi=\varphi_X$ for some random variable $X$ and $X_n\Rightarrow X$.

:::

::: {.proof}

1. *Tightness.* Given $\varepsilon>0$, continuity of $\psi$ at $0$ gives $\lambda$ with $c\lambda\int_0^{1/\lambda}(1-\operatorname{Re}\psi(t))\,dt<\varepsilon/2$. By bounded convergence, $c\lambda\int_0^{1/\lambda}(1-\operatorname{Re}\varphi_{X_n})\,dt\to c\lambda\int_0^{1/\lambda}(1-\operatorname{Re}\psi)\,dt$, so for $n\ge n_0$ this integral is $\le\varepsilon$; by @lem-levy-tightness $\mu_{X_n}(|x|\ge\lambda)\le\varepsilon$. Enlarging $\lambda$ handles the finitely many $n<n_0$.

2. *Subsequential limits.* By @thm-prokhorov every subsequence has a further subsequence converging weakly to some $\mu$; then $\varphi_\mu=\lim\varphi_{X_{n_k}}=\psi$ (as $e^{itx}$ is bounded continuous), so every subsequential limit has characteristic function $\psi$, hence the same law by uniqueness (@thm-characteristic-function-uniqueness).

3. *Whole sequence.* If $\mu_n\not\Rightarrow\mu$, there are a bounded continuous $f$, $\varepsilon>0$ and a subsequence with $|\mu_{n_k}(f)-\mu(f)|>\varepsilon$; no further subsequence can converge to $\mu$, contradicting step 2. So $X_n\Rightarrow X$.

:::
