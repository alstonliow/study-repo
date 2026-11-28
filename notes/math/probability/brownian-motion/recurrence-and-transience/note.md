---
title: "Recurrence and Transience of Brownian Motion"
sources: [camiii-ap-5]
requires: [math/probability/brownian-motion/harmonic-functions-and-dirichlet-problem]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Advanced Probability (lecture notes), Section 5.3, in our own wording; proofs written out in steps. -->

Whether Brownian motion returns to where it started depends on the dimension, as for the simple random walk: recurrent in dimensions $1$ and $2$ (in the sense below), transient from dimension $3$.

::: {#thm-brownian-recurrence .theorem name="Recurrence and transience"}

Let $B$ be Brownian motion in $\mathbb R^d$ started at $x$.

1. ($d=1$) *Point recurrent*: for every $z$, $\{t:B_t=z\}$ is unbounded a.s.
2. ($d=2$) *Neighbourhood recurrent*: for every non-empty open $U$, $\{t:B_t\in U\}$ is unbounded a.s.; yet $B$ does not visit points: $\Pr_x(B_t=z\text{ for some }t>0)=0$ for $z\ne x$.
3. ($d\ge3$) *Transient*: $|B_t|\to\infty$ almost surely.

:::

::: {.proof}

1. *$d=1$.* $\sup_tB_t=\infty$ and $\inf_tB_t=-\infty$ a.s. (@prp-brownian-path-properties), and the path is continuous, so every level is visited at arbitrarily late times.

2. *$d=2$: exit probabilities.* Consider the annulus $\varepsilon\le|y|\le R$ around $0$ and $x$ in it. Let $\varphi\in C^2_b$ with $\varphi(y)=\log|y|$ on the annulus; $\log|y|$ is harmonic in the plane minus the origin. By the martingale $\varphi(B_t)-\frac12\int_0^t\Delta\varphi(B_s)\,ds$ (stated in @sec-math-probability-brownian-motion-harmonic-functions-and-dirichlet-problem), stopped at $H=S_\varepsilon\wedge S_R$ (where $S_\lambda=\inf\{t:|B_t|=\lambda\}$, a.s. finite for $x$ in the annulus) the process $M_{t\wedge H}$ is bounded, so optional stopping gives $E_x[\log|B_H|]=\log|x|$, i.e.
$$
\log\varepsilon\,\Pr_x(S_\varepsilon<S_R)+\log R\,\Pr_x(S_R<S_\varepsilon)=\log|x|,\qquad\Pr_x(S_\varepsilon<S_R)=\frac{\log R-\log|x|}{\log R-\log\varepsilon}.\tag{$*$}
$$

3. *Neighbourhood recurrence.* Let $R\to\infty$: $S_R\to\infty$ a.s., and $(*)$ gives $\Pr_x(S_\varepsilon<\infty)=1$ for all $x$ — the path hits every ball around $0$; by the Markov property it does so at arbitrarily late times (restart at a late time). Translating gives all open sets.

4. *No point visits.* For $z=0\ne x$ let $\varepsilon\to0$ in $(*)$: $\Pr_x(S_\varepsilon<S_R)\to0$ for fixed $R$, then $R\to\infty$: $\Pr_x(\text{hit }0)=0$.

5. *$d\ge3$* (take $d=3$, higher $d$ by projection). Take $\varphi(y)=1/|y|$ on $\varepsilon\le|y|\le R$, harmonic there. As in 2, $\Pr_x(S_\varepsilon<S_R)=\dfrac{|x|^{-1}-R^{-1}}{\varepsilon^{-1}-R^{-1}}$, and letting $R\to\infty$, $\Pr_x(S_\varepsilon<\infty)=\varepsilon/|x|$.

6. Start at $0$ and let $A_n=\{|B_t|\ge n\text{ for all }t\ge T_{n^3}\}$, where $T_{n^3}$ is the first time $|B|=n^3$. By the strong Markov property and step 5, $\Pr(A_n^c)=n/n^3=n^{-2}$ (the probability to return to the ball of radius $n$ from distance $n^3$). Since $\sum n^{-2}<\infty$, Borel–Cantelli shows that a.s. all but finitely many $A_n$ occur, so $|B_t|\to\infty$.

:::

::: {#fig-recurrence-and-transience-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[box] (0,0) circle (0.5);
\draw[box] (0,0) circle (2.0);
\node[tick] at (0,-0.9) {$\varepsilon$};
\node[tick] at (0,-2.4) {$R$};
\node[small vertex] at (1.2,0.9) {};
\node[tick] at (1.45,1.1) {$x$};
\draw[emph] (1.2,0.9) -- (0.9,0.3) -- (0.6,0.1) -- (0.45,0.15);
\draw[hl, dashed] (1.2,0.9) -- (1.6,1.1) -- (1.9,1.2);
\node[lab, text=accent] at (5.5,0.3) {$\Pr(S_\varepsilon<S_R)$};
\node[lab] at (5.5,-0.3) {$d=2$: $\tfrac{\log R-\log|x|}{\log R-\log\varepsilon}\to1$};
\node[lab] at (5.5,-0.9) {$d=3$: $\tfrac{|x|^{-1}-R^{-1}}{\varepsilon^{-1}-R^{-1}}\to\tfrac\varepsilon{|x|}$};
\end{tikzpicture}
\end{center}
```

From $x$ in the annulus, the path either reaches the inner circle (radius $\varepsilon$) or the outer one first. Letting $R\to\infty$, the inner circle is reached with probability $1$ in the plane, but only with probability $\varepsilon/|x|<1$ in $\mathbb R^3$.

:::
