---
title: "The Contraction Mapping Theorem"
sources: [camib-at-a5]
requires: [math/analysis/metric-spaces/continuous-maps]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Analysis II (Michaelmas 2015 lecture notes), Section 5.6, in our own wording; examples ours (fixed point of cos checked numerically); proofs written out in steps. -->

Many equations can be written as $x=f(x)$. If $f$ shrinks distances by a fixed factor on a complete space, the equation has exactly one solution, and iterating $f$ from any starting point finds it.

::: {#def-contraction .definition name="Contraction"}

A map $f:X\to X$ on a metric space is a *contraction* if there is $\lambda\in[0,1)$ with
$$d(f(x),f(y))\le\lambda\,d(x,y)\qquad\text{for all }x,y\in X,$$
that is, $f$ is Lipschitz with constant $\lambda<1$.

:::

::: {#fig-contraction-mapping-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (2.332,0.000) -- (2.397,0.137) -- (2.422,0.281) -- (2.397,0.425) -- (2.320,0.563) -- (2.191,0.690) -- (2.016,0.799) -- (1.804,0.886) -- (1.567,0.949) -- (1.317,0.989) -- (1.067,1.008) -- (0.826,1.012) -- (0.599,1.005) -- (0.388,0.995) -- (0.190,0.987) -- (0.000,0.984) -- (-0.190,0.987) -- (-0.388,0.995) -- (-0.599,1.005) -- (-0.826,1.012) -- (-1.067,1.008) -- (-1.317,0.989) -- (-1.567,0.949) -- (-1.804,0.886) -- (-2.016,0.799) -- (-2.191,0.690) -- (-2.320,0.563) -- (-2.397,0.425) -- (-2.422,0.281) -- (-2.397,0.137) -- (-2.332,0.000) -- (-2.235,-0.128) -- (-2.118,-0.246) -- (-1.991,-0.353) -- (-1.861,-0.452) -- (-1.734,-0.546) -- (-1.610,-0.638) -- (-1.486,-0.730) -- (-1.359,-0.823) -- (-1.221,-0.917) -- (-1.067,-1.008) -- (-0.892,-1.093) -- (-0.695,-1.166) -- (-0.477,-1.223) -- (-0.243,-1.260) -- (-0.000,-1.272) -- (0.243,-1.260) -- (0.477,-1.223) -- (0.695,-1.166) -- (0.892,-1.093) -- (1.067,-1.008) -- (1.221,-0.917) -- (1.359,-0.823) -- (1.486,-0.730) -- (1.610,-0.638) -- (1.734,-0.546) -- (1.861,-0.452) -- (1.991,-0.353) -- (2.118,-0.246) -- (2.235,-0.128) -- cycle;
\draw[emph] (2.332,0.000) -- (2.397,0.137) -- (2.422,0.281) -- (2.397,0.425) -- (2.320,0.563) -- (2.191,0.690) -- (2.016,0.799) -- (1.804,0.886) -- (1.567,0.949) -- (1.317,0.989) -- (1.067,1.008) -- (0.826,1.012) -- (0.599,1.005) -- (0.388,0.995) -- (0.190,0.987) -- (0.000,0.984) -- (-0.190,0.987) -- (-0.388,0.995) -- (-0.599,1.005) -- (-0.826,1.012) -- (-1.067,1.008) -- (-1.317,0.989) -- (-1.567,0.949) -- (-1.804,0.886) -- (-2.016,0.799) -- (-2.191,0.690) -- (-2.320,0.563) -- (-2.397,0.425) -- (-2.422,0.281) -- (-2.397,0.137) -- (-2.332,0.000) -- (-2.235,-0.128) -- (-2.118,-0.246) -- (-1.991,-0.353) -- (-1.861,-0.452) -- (-1.734,-0.546) -- (-1.610,-0.638) -- (-1.486,-0.730) -- (-1.359,-0.823) -- (-1.221,-0.917) -- (-1.067,-1.008) -- (-0.892,-1.093) -- (-0.695,-1.166) -- (-0.477,-1.223) -- (-0.243,-1.260) -- (-0.000,-1.272) -- (0.243,-1.260) -- (0.477,-1.223) -- (0.695,-1.166) -- (0.892,-1.093) -- (1.067,-1.008) -- (1.221,-0.917) -- (1.359,-0.823) -- (1.486,-0.730) -- (1.610,-0.638) -- (1.734,-0.546) -- (1.861,-0.452) -- (1.991,-0.353) -- (2.118,-0.246) -- (2.235,-0.128) -- cycle;
\node[dot] at (-1.5,-0.3) {}; \node[lab, below] at (-1.5,-0.3) {$x$}; \node[dot] at (1.5,0.4) {}; \node[lab, below] at (1.5,0.4) {$y$};
\draw[faint, dashed] (-1.5,-0.3) -- (1.5,0.4);
\node[hl dot] at (-0.5,0.4) {}; \node[lab, above] at (-0.5,0.4) {$f(x)$}; \node[hl dot] at (0.6,0.65) {}; \node[lab, above] at (0.6,0.65) {$f(y)$};
\draw[hl] (-0.5,0.4) -- (0.6,0.65);
\draw[map] (-1.5,-0.25) to[bend left=20] (-0.55,0.35); \draw[map] (1.5,0.45) to[bend right=20] (0.65,0.6);
\end{tikzpicture}
\end{center}
```

A contraction brings every pair of points closer by at least a fixed factor $k<1$: $d(f(x),f(y))\le k\,d(x,y)$.

:::

```{=latex}
\begin{algorithm}
\caption{Fixed-point iteration}
\begin{algorithmic}
\INPUT A contraction $f:X\to X$ with constant $\lambda$, a starting point $x_0\in X$, a tolerance $\varepsilon>0$
\OUTPUT A point within $\varepsilon$ of the fixed point of $f$
\STATE $n\gets0$
\REPEAT
    \STATE $x_{n+1}\gets f(x_n)$; $n\gets n+1$
\UNTIL{$\frac{\lambda}{1-\lambda}\,d(x_n,x_{n-1})<\varepsilon$}
\RETURN $x_n$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-contraction-mapping .theorem name="Contraction mapping theorem"}

Let $X$ be a non-empty complete metric space and $f:X\to X$ a contraction with constant $\lambda$. Then $f$ has exactly one fixed point $x^*$. For every $x_0\in X$ the iterates $x_{n+1}=f(x_n)$ converge to $x^*$, and
$$d(x_n,x^*)\le\frac{\lambda^n}{1-\lambda}d(x_1,x_0),\qquad d(x_n,x^*)\le\frac{\lambda}{1-\lambda}d(x_n,x_{n-1}).$$

:::

::: {.proof}

1. *Steps shrink geometrically.* By induction, $d(x_{n+1},x_n)=d(f(x_n),f(x_{n-1}))\le\lambda\,d(x_n,x_{n-1})\le\dots\le\lambda^nd(x_1,x_0)$.

2. *The iterates are Cauchy.* For $m>n$, by the triangle inequality and step 1,
$$d(x_m,x_n)\le\sum_{k=n}^{m-1}d(x_{k+1},x_k)\le\sum_{k=n}^{\infty}\lambda^kd(x_1,x_0)=\frac{\lambda^n}{1-\lambda}d(x_1,x_0),$$
which tends to $0$ as $n\to\infty$.

3. *The limit is a fixed point.* $X$ is complete, so $x_n\to x^*$ for some $x^*$. A contraction is continuous, so $x_{n+1}=f(x_n)\to f(x^*)$; but also $x_{n+1}\to x^*$, so $f(x^*)=x^*$ by uniqueness of limits (@prp-limit-unique-metric).

4. *Uniqueness.* If $f(x)=x$ and $f(y)=y$, then $d(x,y)=d(f(x),f(y))\le\lambda\,d(x,y)$, so $(1-\lambda)d(x,y)\le0$ and $x=y$.

5. *Error bounds.* Let $m\to\infty$ in step 2 (the metric is continuous in each variable) to get the first bound. Applying it to the sequence started at $x_{n-1}$, whose first step is $d(x_n,x_{n-1})$, gives $d(x_n,x^*)\le\frac{\lambda}{1-\lambda}d(x_n,x_{n-1})$, which justifies the stopping rule of the algorithm.

:::

::: {#fig-contraction-mapping-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.2,0) -- (5.0,0);
\node[dot] at (0.000,0.000) {};
\node[dot] at (2.250,0.000) {};
\node[dot] at (3.375,0.000) {};
\node[dot] at (3.938,0.000) {};
\node[dot] at (4.219,0.000) {};
\node[dot] at (4.359,0.000) {};
\draw[->, emph] (0.000,0.15) to[bend left=40] (2.250,0.15);
\draw[->, emph] (2.250,0.15) to[bend left=40] (3.375,0.15);
\draw[->, emph] (3.375,0.15) to[bend left=40] (3.938,0.15);
\draw[->, emph] (3.938,0.15) to[bend left=40] (4.219,0.15);
\node[hl dot] at (4.500,0.000) {};\node[lab, below] at (4.5,-0.05) {$x^*$};
\node[lab, below] at (0.000,-0.05) {$x_0$};
\node[lab, below] at (2.250,-0.05) {$x_1$};
\node[lab, below] at (3.375,-0.05) {$x_2$};
\end{tikzpicture}
\end{center}
```

Iterating a contraction with constant $\frac12$: each step is at most half the previous one, so the steps add up and $x_n$ converges to the unique fixed point $x^*$.

:::

::: {#exm-contraction-cosine .example name="Solving $x=\cos x$"}

On $X=[0,1]$, complete as a closed subset of $\mathbb R$ (@thm-closed-subspace-complete), $f(x)=\cos x$ maps $X$ into $[\cos1,1]\subseteq X$. By the mean value theorem $|\cos x-\cos y|\le\sin1\cdot|x-y|$ on $[0,1]$, and $\sin1\approx0.841<1$. So $\cos x=x$ has exactly one solution in $[0,1]$, $x^*\approx0.739085$, and the iterates from $x_0=1$ are $0.5403,\ 0.8576,\ 0.6543,\ 0.7935,\dots$, oscillating towards it (@fig-contraction-mapping-1).

:::

::: {#fig-contraction-mapping-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (4.32,0) node[lab, anchor=west] {$x$};
\draw[->] (0,0) -- (0,4.32);
\node[lab,tick, anchor=north] at (4.00,0) {$1$};
\node[lab,tick, anchor=north east] at (0,0) {$0$};
\node[lab,tick, anchor=east] at (0,4.00) {$1$};
\draw[faint] (0,0) -- (4.00,4.00) node[lab, anchor=south west] {$y=x$};
\draw[emph, primary, domain=0:1, samples=50] plot ({4.0*\x},{4.0*cos(\x r)}) node[lab, anchor=west] {$y=\cos x$};
\draw[accent] (4.000,0.000) -- (4.000,2.161) -- (2.161,2.161) -- (2.161,3.430) -- (3.430,3.430) -- (3.430,2.617) -- (2.617,2.617) -- (2.617,3.174) -- (3.174,3.174) -- (3.174,2.805) -- (2.805,2.805) -- (2.805,3.056) -- (3.056,3.056);
\node[lab,tick, anchor=north] at (4.000,-0.05) {$x_0$};
\draw[faint] (4.000,0) -- (4.000,0.08);
\node[lab,tick, anchor=north] at (2.161,-0.05) {$x_1$};
\draw[faint] (2.161,0) -- (2.161,0.08);
\node[lab,tick, anchor=north] at (3.430,-0.05) {$x_2$};
\draw[faint] (3.430,0) -- (3.430,0.08);
\node[lab,tick, anchor=north] at (2.617,-0.05) {$x_3$};
\draw[faint] (2.617,0) -- (2.617,0.08);
\node[hl dot] at (2.956,2.956) {};
\node[lab, anchor=east] at (2.05,2.956) {$x^*$};
\draw[faint] (2.05,2.956) -- (2.856,2.956);
\end{tikzpicture}
\end{center}
```

Fixed-point iteration for $\cos$ on $[0,1]$ from $x_0=1$: each step goes vertically to the graph and horizontally to the diagonal, spiralling in to $x^*\approx0.739$.

:::

::: {#rmk-contraction-mapping-hypotheses .remark name="Each hypothesis is needed"}

1. *Completeness:* $f(x)=\frac x2$ is a contraction of $(0,1]$ with no fixed point; the iterates converge to $0$, outside the space.
2. *A uniform $\lambda<1$:* $f(x)=x+\frac1x$ on $[1,\infty)$ satisfies $|f(x)-f(y)|=|x-y|\bigl(1-\frac1{xy}\bigr)<|x-y|$ for $x\ne y$, yet $f(x)>x$ always, so there is no fixed point.
3. *$f$ maps $X$ into $X$:* this must be checked, as in @exm-contraction-cosine, and often determines the choice of $X$.

:::

::: {#cor-contraction-iterate .corollary name="A contracting iterate is enough"}

Let $X$ be non-empty and complete and $f:X\to X$. If some iterate $f^m=f\circ\dots\circ f$ is a contraction, then $f$ has exactly one fixed point.

:::

::: {.proof}

1. By @thm-contraction-mapping, $f^m$ has a unique fixed point $x^*$.

2. Then $f^m(f(x^*))=f(f^m(x^*))=f(x^*)$, so $f(x^*)$ is also a fixed point of $f^m$; by uniqueness $f(x^*)=x^*$.

3. Any fixed point of $f$ is a fixed point of $f^m$, hence equals $x^*$.

:::

The theorem is used in @sec-math-analysis-metric-spaces-picard-lindelof to solve differential equations, and in @sec-math-analysis-differentiation-inverse-function-theorem to invert maps; in both cases $X$ is a space of functions or a closed ball.
