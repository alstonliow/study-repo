---
title: "The Kalman Filter"
sources: [eecs126-11, eecs126hw-14, eecs126d-13]
requires: [math/probability/estimation/jointly-gaussian]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley EECS126 (Fall 2021), note "A Geometric Derivation of the Scalar Kalman Filter", Homework 14 and Discussion 13, in our own wording; proofs written out in steps. -->

The Kalman filter tracks a hidden state that evolves linearly with noise, from noisy linear observations. It updates the linear least squares estimate (@thm-llse) one observation at a time, at constant cost per step.

::: {#def-linear-system .definition name="Scalar linear system"}

The state $X_n$ and the observation $Y_n$ satisfy
$$X_n=aX_{n-1}+V_n,\qquad Y_n=cX_n+W_n,\qquad n\ge1,$$
where $X_0,V_1,W_1,V_2,W_2,\dots$ are uncorrelated, of mean $0$, with $\operatorname{Var}(V_n)=\sigma_V^2$, $\operatorname{Var}(W_n)=\sigma_W^2$, and $\operatorname{Var}(X_0)=\sigma_0^2$.

:::

Write $\hat X_{n\mid m}=L[X_n\mid Y_1,\dots,Y_m]$ and $\sigma_{n\mid m}^2=E[(X_n-\hat X_{n\mid m})^2]$, with $\hat X_{0\mid0}=0$ and $\sigma^2_{0\mid0}=\sigma_0^2$.

::: {#thm-kalman-filter .theorem name="Scalar Kalman filter"}

For $n\ge1$:
$$\begin{aligned}
\hat X_{n\mid n-1}&=a\hat X_{n-1\mid n-1},&\sigma^2_{n\mid n-1}&=a^2\sigma^2_{n-1\mid n-1}+\sigma_V^2,\\
\hat X_{n\mid n}&=\hat X_{n\mid n-1}+k_n\bigl(Y_n-c\hat X_{n\mid n-1}\bigr),&k_n&=\frac{c\,\sigma^2_{n\mid n-1}}{c^2\sigma^2_{n\mid n-1}+\sigma_W^2},\\
\sigma^2_{n\mid n}&=(1-k_nc)\,\sigma^2_{n\mid n-1}.
\end{aligned}$$

:::

::: {.proof}

1. *Predict.* $V_n$ is orthogonal to $Y_1,\dots,Y_{n-1}$ (these involve only $X_0$, earlier $V$'s and $W$'s), so $L[V_n\mid Y_{1:n-1}]=0$ and $\hat X_{n\mid n-1}=a\hat X_{n-1\mid n-1}$. The prediction error $a(X_{n-1}-\hat X_{n-1\mid n-1})+V_n$ is a sum of orthogonal terms, which gives $\sigma^2_{n\mid n-1}$.

2. *Innovation.* Similarly $L[Y_n\mid Y_{1:n-1}]=c\hat X_{n\mid n-1}$, so the innovation is $\tilde Y_n=Y_n-c\hat X_{n\mid n-1}=c(X_n-\hat X_{n\mid n-1})+W_n$, with variance $c^2\sigma^2_{n\mid n-1}+\sigma_W^2$.

3. *Update.* By @thm-orthogonal-update, $\hat X_{n\mid n}=\hat X_{n\mid n-1}+k_n\tilde Y_n$ with $k_n=\operatorname{Cov}(X_n,\tilde Y_n)/\operatorname{Var}(\tilde Y_n)$, and $\operatorname{Cov}(X_n,\tilde Y_n)=c\,\sigma^2_{n\mid n-1}$ because $X_n-\hat X_{n\mid n-1}$ is orthogonal to $\hat X_{n\mid n-1}$.

4. *Error.* By @thm-llse the update lowers the error by $\operatorname{Cov}(X_n,\tilde Y_n)^2/\operatorname{Var}(\tilde Y_n)=k_nc\,\sigma^2_{n\mid n-1}$.

:::

::: {#fig-kalman-filter-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (p) at (0,0) {predict\\$\hat X_{n\mid n-1}=a\hat X_{n-1\mid n-1}$};
\node[hl box] (u) at (6,0) {update with $Y_n$\\$\hat X_{n\mid n}=\hat X_{n\mid n-1}+k_n(Y_n-c\hat X_{n\mid n-1})$};
\draw[map] (p) -- node[edge label] {$\sigma^2_{n\mid n-1}$} (u);
\draw[map] (u.south) to[bend left=25] node[edge label] {$n\to n+1$} (p.south);
\end{tikzpicture}
\end{center}
```

Each step of the Kalman filter predicts the state from the last estimate, then corrects the prediction by the gain $k_n$ times the innovation $Y_n-c\hat X_{n\mid n-1}$

:::

```{=latex}
\begin{algorithm}
\caption{Scalar Kalman filter}
\begin{algorithmic}
\INPUT $a,c,\sigma_V^2,\sigma_W^2,\sigma_0^2$; observations $Y_1,\dots,Y_N$
\OUTPUT Estimates $\hat X_{n\mid n}$ and error variances $\sigma^2_{n\mid n}$
\STATE $\hat x\gets0$; $s\gets\sigma_0^2$
\FOR{$n=1$ \textbf{to} $N$}
    \STATE $\hat x\gets a\hat x$; $s\gets a^2s+\sigma_V^2$ \COMMENT{predict}
    \STATE $k\gets cs/(c^2s+\sigma_W^2)$
    \STATE $\hat x\gets\hat x+k(Y_n-c\hat x)$; $s\gets(1-kc)s$ \COMMENT{update}
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

The gains $k_n$ and variances do not depend on the observations, so they can be computed in advance. If all the variables are jointly Gaussian, $\hat X_{n\mid n}=E[X_n\mid Y_{1:n}]$ is the best estimate of any form (@thm-jointly-gaussian-conditional), and the filter is the forward algorithm (@thm-forward-algorithm) for a hidden Markov model with Gaussian state.

::: {#exm-kalman-random-walk .example name="Tracking a random walk"}

Take $a=c=1$ and $\sigma_V^2=\sigma_W^2=\sigma_0^2=1$. The recursion gives
$$k_1=\tfrac23,\quad k_2=0.625,\quad k_3\approx0.619,\quad k_4\approx0.618,\ \dots$$
and $\sigma^2_{n\mid n}=k_n$. The gain converges to the fixed point of $k=\frac{k+1}{k+2}$, namely $k=\frac{\sqrt5-1}{2}\approx0.618$: the steady-state filter puts weight $0.618$ on each new observation.

:::

::: {#fig-kalman-filter-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,1.15) -- (6.4,1.15) node[lab, right] {$n$};
\draw[emph] (0.200,1.834) -- (0.400,1.607) -- (0.600,1.720) -- (0.800,1.848) -- (1.000,1.628) -- (1.200,1.917) -- (1.400,1.819) -- (1.600,1.878) -- (1.800,1.888) -- (2.000,2.379) -- (2.200,2.673) -- (2.400,2.934) -- (2.600,2.786) -- (2.800,3.060) -- (3.000,3.372) -- (3.200,3.859) -- (3.400,3.495) -- (3.600,3.305) -- (3.800,3.336) -- (4.000,3.482) -- (4.200,3.521) -- (4.400,4.145) -- (4.600,4.160) -- (4.800,3.736) -- (5.000,3.981) -- (5.200,4.074) -- (5.400,4.630) -- (5.600,4.389) -- (5.800,4.106) -- (6.000,4.403);
\draw[hl] (0.200,2.019) -- (0.400,1.601) -- (0.600,1.997) -- (0.800,1.697) -- (1.000,1.650) -- (1.200,1.818) -- (1.400,1.783) -- (1.600,1.712) -- (1.800,1.875) -- (2.000,2.182) -- (2.200,2.304) -- (2.400,2.729) -- (2.600,2.765) -- (2.800,2.895) -- (3.000,3.472) -- (3.200,4.012) -- (3.400,3.761) -- (3.600,3.657) -- (3.800,3.506) -- (4.000,3.390) -- (4.200,3.347) -- (4.400,3.763) -- (4.600,3.694) -- (4.800,3.574) -- (5.000,3.972) -- (5.200,3.925) -- (5.400,4.181) -- (5.600,4.404) -- (5.800,4.275) -- (6.000,4.348);
\node[hollow dot] at (0.20,2.23) {};
\node[hollow dot] at (0.40,1.35) {};
\node[hollow dot] at (0.60,2.24) {};
\node[hollow dot] at (0.80,1.51) {};
\node[hollow dot] at (1.00,1.62) {};
\node[hollow dot] at (1.20,1.92) {};
\node[hollow dot] at (1.40,1.76) {};
\node[hollow dot] at (1.60,1.67) {};
\node[hollow dot] at (1.80,1.98) {};
\node[hollow dot] at (2.00,2.37) {};
\node[hollow dot] at (2.20,2.38) {};
\node[hollow dot] at (2.40,2.99) {};
\node[hollow dot] at (2.60,2.79) {};
\node[hollow dot] at (2.80,2.97) {};
\node[hollow dot] at (3.00,3.83) {};
\node[hollow dot] at (3.20,4.34) {};
\node[hollow dot] at (3.40,3.61) {};
\node[hollow dot] at (3.60,3.59) {};
\node[hollow dot] at (3.80,3.41) {};
\node[hollow dot] at (4.00,3.32) {};
\node[hollow dot] at (4.20,3.32) {};
\node[hollow dot] at (4.40,4.02) {};
\node[hollow dot] at (4.60,3.65) {};
\node[hollow dot] at (4.80,3.50) {};
\node[hollow dot] at (5.00,4.22) {};
\node[hollow dot] at (5.20,3.90) {};
\node[hollow dot] at (5.40,4.34) {};
\node[hollow dot] at (5.60,4.54) {};
\node[hollow dot] at (5.80,4.20) {};
\node[hollow dot] at (6.00,4.39) {};
\node[tick, right] at (6.1,4.55) {$X_n$};
\node[tick, right, text=accent] at (6.1,4.20) {$\hat X_{n\mid n}$};
\end{tikzpicture}
\end{center}
```

A simulated random walk $X_n$ (black), its noisy observations $Y_n$ (circles) and the Kalman estimate $\hat X_{n\mid n}$, which tracks the state much more closely than the raw observations

:::

::: {#fig-kalman-filter-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.950,0.950);
\node[lab] at (0.475,0.475) {$0.667$};
\draw[cell frame] (0.950,0.000) rectangle (1.900,0.950);
\node[lab] at (1.425,0.475) {$0.625$};
\draw[cell frame] (1.900,0.000) rectangle (2.850,0.950);
\node[lab] at (2.375,0.475) {$0.619$};
\draw[cell frame] (2.850,0.000) rectangle (3.800,0.950);
\node[lab] at (3.325,0.475) {$0.618$};
\draw[cell frame] (3.800,0.000) rectangle (4.750,0.950);
\node[lab] at (4.275,0.475) {$0.618$};
\draw[hl cell] (4.750,0.000) rectangle (5.700,0.950);
\node[lab] at (5.225,0.475) {$0.618$};
\node[lab, anchor=east] at (-0.100,0.475) {$k_n$};
\node[lab,tick] at (0.475,-0.2) {$n=1$};
\node[lab,tick] at (1.425,-0.2) {$n=2$};
\node[lab,tick] at (2.375,-0.2) {$n=3$};
\node[lab,tick] at (3.325,-0.2) {$n=4$};
\node[lab,tick] at (4.275,-0.2) {$n=5$};
\node[lab,tick] at (5.225,-0.2) {$n=6$};
\node[lab,anchor=west] at (5.850,0.475) {$\to\frac{\sqrt5-1}{2}\approx0.618$};
\end{tikzpicture}
\end{center}
```

Kalman gains $k_n$ for the random walk with $a=c=1$ and all variances $1$. They are computed before any observation arrives and settle within a few steps at the steady-state gain $0.618$; the error variance $\sigma^2_{n\mid n}$ equals $k_n$ here.

:::

::: {#rmk-kalman-vector .remark name="Vector case"}

For $X_n=AX_{n-1}+V_n$, $Y_n=CX_n+W_n$ with covariances $\Sigma_V,\Sigma_W$, the same steps give the covariance recursion $\Sigma_{n\mid n-1}=A\Sigma_{n-1\mid n-1}A^{\mathsf T}+\Sigma_V$, the gain $K_n=\Sigma_{n\mid n-1}C^{\mathsf T}(C\Sigma_{n\mid n-1}C^{\mathsf T}+\Sigma_W)^{-1}$ and $\Sigma_{n\mid n}=(I-K_nC)\Sigma_{n\mid n-1}$.

:::
