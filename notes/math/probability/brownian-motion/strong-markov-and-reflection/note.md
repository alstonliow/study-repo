---
title: "The Strong Markov Property, the Reflection Principle and Brownian Martingales"
sources: [camiii-ap-5]
requires: [math/probability/brownian-motion/blumenthal-and-path-properties, math/probability/continuous-time/continuous-time-martingales]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Advanced Probability (lecture notes), Section 5.1, in our own wording; proofs written out in steps. -->

The simple Markov property restarts Brownian motion at a fixed time. The strong Markov property restarts it at a random stopping time, and combined with symmetry this gives the reflection principle and an exact formula for the running maximum.

::: {#thm-strong-markov .theorem name="Strong Markov property"}

Let $B$ be a standard Brownian motion in $\mathbb R^d$ and $T$ an a.s. finite stopping time with respect to $(\mathcal F_{t+})$. Then $\tilde B_t=B_{T+t}-B_T$ is a standard Brownian motion, independent of $\mathcal F_{T+}$.

:::

::: {.proof}

1. *Discrete $T_n=2^{-n}\lceil2^nT\rceil$.* Put $B^{(k)}_t=B_{t+k2^{-n}}-B_{k2^{-n}}$, a standard Brownian motion independent of $\mathcal F_{k2^{-n}+}$ (simple Markov property and @thm-independent-of-f-plus), and $B^*_t=B_{t+T_n}-B_{T_n}$. For a measurable set $A$ of paths and $E\in\mathcal F_{T_n+}$ (so $E\cap\{T_n=k2^{-n}\}\in\mathcal F_{k2^{-n}+}$):
$$
\Pr(\{B^*\in A\}\cap E)=\sum_{k\ge0}\Pr\big(\{B^{(k)}\in A\}\cap E\cap\{T_n=k2^{-n}\}\big)=\sum_k\Pr(B\in A)\Pr\big(E\cap\{T_n=k2^{-n}\}\big)=\Pr(B\in A)\Pr(E).
$$
Taking $E=\Omega$, $B^*$ is a standard Brownian motion; for general $E$ it is independent of $\mathcal F_{T_n+}\supseteq\mathcal F_{T+}$.

2. *Limit.* As $n\to\infty$, $T_n\downarrow T$ and by continuity the increments of $B^*$ converge a.s. to those of $\tilde B$. Almost sure convergence implies convergence in distribution, and all $B^*$ have the law of $B$; so $\tilde B$ is a standard Brownian motion. Independence of $\mathcal F_{T+}$ passes to the limit.

:::

::: {#thm-reflection-principle .theorem name="Reflection principle"}

With $B$ and $T$ as above, the reflected process $\tilde B_t=B_t\mathbf 1_{\{t<T\}}+(2B_T-B_t)\mathbf 1_{\{t\ge T\}}$ is a standard Brownian motion.

:::

::: {.proof}

1. By the strong Markov property, $B^T_t=B_{T+t}-B_T$ and $-B^T$ are standard Brownian motions independent of $\mathcal F_{T+}$, hence independent of $(B_t)_{t\le T}$. So the pairs $((B_t)_{t\le T},B^T)$ and $((B_t)_{t\le T},-B^T)$ have the same law on $C\times C$.

2. The concatenation map $\psi_T(X,Y)_t=X_t\mathbf 1_{\{t<T\}}+(X_T+Y_{t-T})\mathbf 1_{\{t\ge T\}}$ is measurable (approximate $T$ by discrete times) and continuous in $t$ when $Y_0=0$. The images of the two pairs have the same law: $\psi_T(B,B^T)=B$ and $\psi_T(B,-B^T)=\tilde B$.

:::

::: {#fig-strong-markov-and-reflection-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-0.2,0) -- (8.4,0) node[lab, right] {$t$};
\draw[faint] (0,2) -- (8,2);
\node[tick, left] at (0,2) {$b$};
\draw[emph] (0,0) -- (1,0.6) -- (2,0.3) -- (3,1.2) -- (4,2.0) -- (5,1.5) -- (6,1.7) -- (7,1.0) -- (8,1.3);
\draw[hl, dashed] (4,2.0) -- (5,2.5) -- (6,2.3) -- (7,3.0) -- (8,2.7);
\draw[faint] (4,0) -- (4,2);
\node[tick] at (4,-0.3) {$T$};
\node[lab, text=accent] at (7.0,0.45) {$B$};
\node[lab, text=accent] at (7.3,3.3) {$\tilde B$};
\end{tikzpicture}
\end{center}
```

After the first hitting time $T$ of level $b$ the path is replaced by its mirror image in the line $y=b$ (dashed); by the strong Markov property and symmetry the result has the same law as $B$.

:::

::: {#cor-reflection-maximum .corollary name="Law of the running maximum"}

Let $d=1$, $S_t=\sup_{s\le t}B_s$. For $b>0$ and $a\le b$,

$$
\Pr(S_t\ge b,\ B_t\le a)=\Pr(B_t\ge2b-a).
$$

In particular $S_t$ has the same law as $|B_t|$.

:::

::: {.proof}

1. Let $T=\inf\{t:B_t=b\}$, a.s. finite because $S_\infty=\infty$ (@prp-brownian-path-properties), and a stopping time (@prp-hitting-closed). With $\tilde B$ the reflected process, $\{S_t\ge b,\ B_t\le a\}=\{\tilde B_t\ge2b-a\}$, and $\tilde B$ is a Brownian motion, so the probability is $\Pr(B_t\ge2b-a)$.

2. Take $b=a$: $\Pr(S_t\ge a)=\Pr(S_t\ge a,B_t<a)+\Pr(S_t\ge a,B_t\ge a)=\Pr(B_t\ge a)+\Pr(B_t\ge a)=\Pr(|B_t|\ge a)$, using that $\{B_t\ge a\}\subseteq\{S_t\ge a\}$ and the symmetry of $B_t$.

:::

::: {#prp-brownian-martingales .proposition name="Brownian martingales"}

For a standard Brownian motion in $d=1$, each of the following is an $(\mathcal F_{t+})$-martingale:

1. $B_t$;
2. $B_t^2-t$;
3. $\exp\!\big(uB_t-\tfrac{u^2}2t\big)$ for $u\in\mathbb R$.

:::

::: {.proof}

For $s\le t$, $B_t-B_s$ is independent of $\mathcal F_{s+}$ with law $N(0,t-s)$.

1. $E[B_t-B_s\mid\mathcal F_{s+}]=E[B_t-B_s]=0$.

2. Write $B_t^2=(B_t-B_s)^2+2B_s(B_t-B_s)+B_s^2$. Conditioning, $E[B_t^2\mid\mathcal F_{s+}]=(t-s)+0+B_s^2$, so $E[B_t^2-t\mid\mathcal F_{s+}]=B_s^2-s$.

3. $E[e^{u(B_t-B_s)}\mid\mathcal F_{s+}]=e^{u^2(t-s)/2}$, hence $E[e^{uB_t-u^2t/2}\mid\mathcal F_{s+}]=e^{uB_s-u^2s/2}$.

:::
