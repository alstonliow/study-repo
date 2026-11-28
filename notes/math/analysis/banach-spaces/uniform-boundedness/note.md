---
title: "The Uniform Boundedness Principle"
sources: [camii-lan-2, camii-lans-2]
requires: [math/analysis/banach-spaces/baire-category]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Linear Analysis (lecture notes), Section 2.2, in our own wording; proofs written out in steps. The Fourier-series application is stated and proved here in outline form only (the divergence of Fourier series of a continuous function at a point). -->

A family of bounded operators that is bounded at every point is bounded in norm, provided the domain is complete. The proof is a direct use of Baire's theorem.

::: {#thm-banach-steinhaus .theorem name="Banach–Steinhaus theorem (uniform boundedness principle)"}

Let $X$ be a Banach space, $Y$ a normed space and $\{T_\alpha\}_{\alpha\in A}\subseteq B(X,Y)$. If $\sup_\alpha\|T_\alpha x\|<\infty$ for every $x\in X$, then $\sup_\alpha\|T_\alpha\|<\infty$.

:::

::: {.proof}

1. For $n\ge1$ let $F_n=\{x\in X:\|T_\alpha x\|\le n\text{ for all }\alpha\}=\bigcap_\alpha\{x:\|T_\alpha x\|\le n\}$. This is closed, being an intersection of closed sets.

2. By hypothesis $X=\bigcup_nF_n$. By @thm-baire some $F_N$ has non-empty interior: $B(x_0,r)\subseteq F_N$.

3. For $\|z\|<r$ and every $\alpha$, $\|T_\alpha z\|\le\|T_\alpha(x_0+z)\|+\|T_\alpha x_0\|\le2N$.

4. So for $\|x\|\le1$, $\|T_\alpha x\|=\frac2r\|T_\alpha(\tfrac r2x)\|\le\frac{4N}r$ for all $\alpha$, giving $\sup_\alpha\|T_\alpha\|\le4N/r$.

:::

::: {#fig-uniform-boundedness-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,0) circle (0.9); \node[lab] at (0,-1.2) {$B(0,r)$};
\draw[emph] (3,0) circle (0.9); \node[lab] at (3,-1.2) {$B(x_0,r)\subseteq F_N$};
\node[dot] at (3,0) {}; \node[lab, above] at (3,0.05) {$x_0$};
\draw[map] (0.9,0.3) to[bend left=20] (2.1,0.3); \node[lab, above] at (1.5,0.7) {$+x_0$};
\end{tikzpicture}
\end{center}
```

A ball inside $F_N$ gives $\|T_\alpha z\|\le2N$ on a ball about $0$.

:::

::: {#cor-pointwise-limit-operator .corollary name="Pointwise limits of bounded operators"}

Let $X$ be Banach, $Y$ normed, $T_n\in B(X,Y)$ with $T_nx$ convergent for every $x$. Then $Tx=\lim T_nx$ defines $T\in B(X,Y)$ with $\|T\|\le\liminf\|T_n\|$ and $\sup_n\|T_n\|<\infty$.

:::

::: {.proof}

1. $T$ is linear as a pointwise limit of linear maps. The sequence $(T_nx)$ is convergent, hence bounded, so @thm-banach-steinhaus gives $M=\sup\|T_n\|<\infty$.

2. $\|Tx\|=\lim\|T_nx\|\le\liminf\|T_n\|\,\|x\|$.

:::

::: {#cor-weak-bounded .corollary name="Weakly bounded sets are bounded"}

Let $X$ be a normed space and $S\subseteq X$. If $\sup_{x\in S}|F(x)|<\infty$ for every $F\in X^*$, then $S$ is bounded.

:::

::: {.proof}

Apply @thm-banach-steinhaus to $\{Jx:x\in S\}\subseteq B(X^*,\mathbb F)$, where $X^*$ is Banach (@cor-dual-banach), and use $\|Jx\|=\|x\|$ (@thm-canonical-embedding-isometry).

:::

::: {#exm-completeness-needed .example name="Completeness of the domain is needed"}

On the space $c_{00}$ of finitely supported sequences with the sup norm, put $T_nx=n\,x_n$. For each $x$, $T_nx=0$ eventually, so $\sup_n|T_nx|<\infty$, but $\|T_n\|=n$ is unbounded. $c_{00}$ is not complete, in line with the theorem.

:::

::: {#prp-fourier-divergence .proposition name="Divergence of Fourier series of continuous functions"}

There is a continuous $2\pi$-periodic function whose Fourier series diverges at $0$.

:::

::: {.proof}

1. Let $X$ be the Banach space of continuous $2\pi$-periodic functions with the sup norm, and $S_nf(0)=\sum_{|k|\le n}\hat f(k)=\frac1{2\pi}\int f(t)D_n(t)\,dt$ with the Dirichlet kernel $D_n(t)=\frac{\sin((n+\frac12)t)}{\sin(t/2)}$. Each $S_n:f\mapsto S_nf(0)$ is a bounded functional.

2. Its norm is $\|S_n\|=\frac1{2\pi}\int|D_n|=:L_n$ (approximate $\operatorname{sgn}D_n$ by continuous functions of sup norm at most $1$). The standard estimate, obtained by comparing $|\sin|$ with its mean value on each period of $\sin((n+\tfrac12)t)$, is $L_n\ge\frac4{\pi^2}\log n\to\infty$.

3. If every continuous $f$ had a convergent Fourier series at $0$, then $\sup_n|S_nf|<\infty$ for each $f$, hence $\sup\|S_n\|<\infty$ by @thm-banach-steinhaus, contradicting step 2.

:::
