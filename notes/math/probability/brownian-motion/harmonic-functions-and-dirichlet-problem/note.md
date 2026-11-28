---
title: "Harmonic Functions and the Dirichlet Problem via Brownian Motion"
sources: [camiii-ap-5]
requires: [math/probability/brownian-motion/strong-markov-and-reflection, math/calculus/multivariable/differentiation/partial-differential-equations]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Advanced Probability (lecture notes), Section 5.2, in our own wording; proofs written out in steps. -->

For a Markov chain, a harmonic function composed with the chain is a martingale (@exm-martingales-examples). Brownian motion is the continuous analogue, and it solves Laplace's equation with prescribed boundary values: the value at $x$ is the average of the boundary data seen by a Brownian path started at $x$.

::: {#def-harmonic-function .definition name="Domain, harmonic function"}

A *domain* is an open connected set $D\subseteq\mathbb R^d$. A function $u:D\to\mathbb R$ is *harmonic* if it is twice continuously differentiable with $\Delta u=\sum_{i=1}^d\partial^2u/\partial x_i^2=0$.

:::

::: {#lem-mean-value-property .lemma name="Mean value property"}

For measurable, locally bounded $u:D\to\mathbb R$ the following are equivalent:

1. $u$ is harmonic.
2. $u(x)=\frac1{\operatorname{Vol}B(x,r)}\int_{B(x,r)}u(y)\,dy$ whenever $B(x,r)\subseteq D$.
3. $u(x)=\frac1{\operatorname{Area}\partial B(x,r)}\int_{\partial B(x,r)}u(y)\,dS(y)$ whenever $B(x,r)\subseteq D$.

:::

This is standard vector calculus (it is not reproved here). Consequently, if $\mu$ is a probability measure whose density depends only on $|x|$ (rotation invariant), then $u(x)=\int u(x+y)\,d\mu(y)$ for harmonic $u$ (when the ball around $x$ lies in $D$).

::: {#lem-independent-freezing .lemma name="Freezing the known variable"}

If $X$ is $\mathcal G$-measurable, $Y$ is independent of $\mathcal G$ and $f(X,Y)$ is integrable, then $E[f(X,Y)\mid\mathcal G]=h(X)$ where $h(z)=E[f(z,Y)]$.

:::

This follows from Fubini and $\mu_{(X,Y)}=\mu_X\otimes\mu_Y$.

::: {#thm-harmonic-martingale .theorem name="Harmonic functions give martingales"}

Let $B$ be standard Brownian motion in $\mathbb R^d$ and $u:\mathbb R^d\to\mathbb R$ harmonic with $E|u(x+B_t)|<\infty$ for all $x,t$. Then $(u(B_t))_{t\ge0}$ is an $(\mathcal F_{t+})$-martingale.

:::

::: {.proof}

For $s\le t$, $B_t=B_s+(B_t-B_s)$ with $B_t-B_s$ independent of $\mathcal F_{s+}$ and rotation-invariant (Gaussian). By @lem-independent-freezing, $E[u(B_t)\mid\mathcal F_{s+}]=h(B_s)$ with $h(z)=E[u(z+B_t-B_s)]$. By the mean value property over spheres (a rotation-invariant average over $\mu=N(0,(t-s)I)$, a mixture of spheres), $h(z)=u(z)$. So $E[u(B_t)\mid\mathcal F_{s+}]=u(B_s)$.

:::

::: {#rmk-ito-martingale .remark name="The general statement (not proved here)"}

For $f\in C^2_b(\mathbb R^d)$, $X_t=f(B_t)-\frac12\int_0^t\Delta f(B_s)\,ds$ is a martingale. The simple random walk explains the $\frac12\Delta$: with $S_n$ the walk, $E[f(S_{n+1})\mid S_1,\dots,S_n]-f(S_n)=\frac12\big(f(S_n+1)+f(S_n-1)-2f(S_n)\big)=\frac12\tilde\Delta f(S_n)$, the discrete second derivative, so $f(S_n)-\frac12\sum_{i<n}\tilde\Delta f(S_i)$ is a martingale. For harmonic $f$ the correction vanishes.

:::

::: {#prp-maximum-principle .proposition name="Maximum principle"}

Let $u:\bar D\to\mathbb R$ be continuous and harmonic in $D$. If $u$ attains its maximum in $D$, then $u$ is constant; if $D$ is bounded the maximum over $\bar D$ is attained on $\partial D$. Consequently, if $u,u'$ are harmonic in $D$, continuous on $\bar D$ and agree on $\partial D$ ($D$ bounded), then $u=u'$.

:::

The first claims follow from the mean value property; for the last, $u-u'$ is harmonic and vanishes on $\partial D$, so both its maximum and minimum are $0$.

::: {#def-poincare-cone .definition name="Poincaré cone condition"}

A domain $D$ satisfies the *Poincaré cone condition* if for every $x\in\partial D$ there are an open cone $C$ with vertex $x$ and $\delta>0$ with $C\cap B(x,\delta)\cap D=\emptyset$.

:::

For instance, the plane with a slit removed, $D=\mathbb R^2\setminus(\{0\}\times\mathbb R_{\ge0})$, does not satisfy the condition at the tip $0$ of the slit.

::: {#lem-cone-hitting .lemma name="Avoiding a cone"}

Let $C$ be an open cone in $\mathbb R^d$ with vertex $0$ and, for $\lambda>0$, $T_\lambda=\inf\{t:|B_t|=\lambda\}$ (exit time of $B(0,\lambda)$), $T_C=\inf\{t:B_t\in C\}$. There is $a\in[0,1)$ such that $\Pr_x(T_1<T_C)\le a^k$ whenever $|x|\le2^{-k}$.

:::

::: {.proof}

1. Put $a=\sup_{|x|\le1/2}\Pr_x(T_1<T_C)$. By Blumenthal (@prp-brownian-path-properties 4) and a continuity argument, $a<1$: starting near $0$, the path enters the cone before leaving the unit ball with probability bounded away from $0$.

2. Let $|x|\le2^{-k}$. To exit $B(0,1)$ before entering the cone, the path must first exit $B(0,2^{-k+1})$ without entering the cone (probability $\le a$ by scaling), then from the boundary point exit $B(0,2^{-k+2})$ without entering the cone (probability $\le a$ by the strong Markov property and scaling), and so on for $k$ stages. Multiplying, $\Pr_x(T_1<T_C)\le a^k$.

:::

::: {#thm-dirichlet-problem .theorem name="The Dirichlet problem"}

Let $D$ be a bounded domain satisfying the Poincaré cone condition, $\varphi:\partial D\to\mathbb R$ continuous, and $T_{\partial D}=\inf\{t:B_t\in\partial D\}$ (a.s. finite). Then

$$
u(x)=E_x\big[\varphi(B_{T_{\partial D}})\big]
$$

is the unique continuous function on $\bar D$ with $u=\varphi$ on $\partial D$ and $\Delta u=0$ in $D$. Here $E_x$ means $B_0=x$.

:::

::: {.proof}

Uniqueness is @prp-maximum-principle.

1. *$u$ is harmonic in $D$.* For $x\in D$ and small $\delta$, let $\tau=T_{\partial B(x,\delta)}$. By the strong Markov property and the tower property, $u(x)=E_x[u(B_\tau)]$, and by rotation invariance $B_\tau$ is uniform on $\partial B(x,\delta)$. So $u$ satisfies the spherical mean value property, hence is harmonic and continuous inside $D$.

2. *Boundary values.* $u=\varphi$ on $\partial D$ since $T_{\partial D}=0$ there.

3. *Continuity at the boundary.* Let $x\in\partial D$ and $\varepsilon>0$; by continuity of $\varphi$ choose $\delta$ with $|\varphi(y)-\varphi(x)|\le\varepsilon$ for $y\in\partial D$, $|y-x|<\delta$, and (shrinking $\delta$) a cone $C$ at $x$ with $C\cap B(x,\delta)\cap D=\emptyset$. For $z\in\bar D$ with $|z-x|\le\delta2^{-k}$: if the path hits $\partial D$ before leaving $B(x,\delta)$ then $|\varphi(B_T)-\varphi(x)|\le\varepsilon$; otherwise it left $B(x,\delta)$ without entering the cone (since $D$ avoids the cone inside the ball, hitting $\partial D$ requires reaching it). Hence
$$
|u(z)-\varphi(x)|\le\varepsilon+2\|\varphi\|_\infty\Pr_z(T_{\partial B(x,\delta)}<T_C)\le\varepsilon+2\|\varphi\|_\infty a^k,
$$
by @lem-cone-hitting and scaling. This tends to $\varepsilon$ as $k\to\infty$, so $u(z)\to\varphi(x)$ as $z\to x$.

:::

::: {#fig-harmonic-functions-and-dirichlet-problem-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[box] (0,0) .. controls (0,3) and (5,3.2) .. (5,0.5) .. controls (5,-0.5) and (0,-1) .. (0,0);
\node[small vertex] (x) at (2.2,1.2) {};
\node[tick] at (2.2,1.55) {$x$};
\draw[emph] (2.2,1.2) -- (2.6,1.5) -- (2.5,0.8) -- (3.1,1.0) -- (3.4,1.7) -- (3.9,1.4) -- (4.3,2.0) -- (4.75,2.15);
\node[small vertex, fill=accentLight, draw=accent] at (4.75,2.15) {};
\node[tick] at (5.5,2.35) {$B_{T_{\partial D}}$};
\node[lab, text=accent] at (1.2,0.2) {$u(x)=E_x[\varphi(B_T)]$};
\end{tikzpicture}
\end{center}
```

The solution at $x$ is the expected boundary value at the point where Brownian motion started at $x$ first reaches the boundary: averaging boundary values by exit position gives a harmonic function.

:::
