---
title: "Expectation Maximization"
sources: [cs221-18]
requires: [ai/bayesian-networks/parameter-learning]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 18 (learning with unobserved variables, EM), in our own wording. The example data and the run are our own; the monotonicity of EM is stated without proof, as in the lecture. -->

Often some variables are never observed: a film's genre $G$ is hidden, and only the two users' ratings $R_1,R_2$ are seen. Maximum likelihood still applies, to the observed data: with hidden variables $H$ and observed $E$,

$$
\max_\theta\sum_{e\in\mathcal D}\log P(E=e;\theta)=\max_\theta\sum_{e\in\mathcal D}\log\sum_hP(H=h,E=e;\theta).
$$

The sum inside the logarithm couples all parameters, so count and normalize no longer applies. It is a chicken-and-egg problem: knowing $\theta$ we could infer $H$, and knowing $H$ we could count.

::: {#def-expectation-maximization .definition name="Expectation maximization"}

*Expectation maximization* (EM) starts from initial parameters $\theta$ and alternates:

1. *E-step*: for each example $e$ and each value $h$ of the hidden variables, compute the weight $q_e(h)=P(H=h\mid E=e;\theta)$ by probabilistic inference;
2. *M-step*: treat each completed example $(h,e)$ as data with weight $q_e(h)$, and set $\theta$ to the count-and-normalize estimate (@def-count-normalize) with these weighted counts.

:::

```{=latex}
\begin{algorithm}
\caption{Expectation maximization}
\begin{algorithmic}
\INPUT Bayesian network with hidden variables $H$, observed data $\mathcal D$ of $E$, initial $\theta$, number of iterations $T$
\OUTPUT Parameters $\theta$
\FOR{$t=1$ \TO $T$}
    \FOR{each $e\in\mathcal D$ and each value $h$}
        \STATE $q_e(h)\gets P(H=h\mid E=e;\theta)$ \COMMENT{E-step}
    \ENDFOR
    \STATE $\theta\gets$ count and normalize, counting each $(h,e)$ with weight $q_e(h)$ \COMMENT{M-step}
\ENDFOR
\RETURN $\theta$
\end{algorithmic}
\end{algorithm}
```

Each iteration does not decrease the likelihood of the observed data, so EM converges, but in general to a local maximum only. It must start from a non-uniform $\theta$ to break the symmetry between the values of $H$, and it can recover the hidden variable only up to renaming its values (drama and comedy may come out swapped). In effect it clusters the data, letting the hidden variable explain it.

::: {#exm-expectation-maximization-1 .example name="Clustering films by two ratings"}

Let $G\in\{d,c\}$ be hidden, and let users rate a film like ($1$) or dislike ($0$), with one shared $p_R(1\mid g)$ for both users. The observed data are $(1,1)$, $(1,1)$, $(0,0)$, $(0,0)$, $(1,0)$. Start from $p_G=(\tfrac12,\tfrac12)$, $p_R(1\mid d)=0.6$, $p_R(1\mid c)=0.4$. The E-step gives the examples $(1,1)$ weight $0.692$ on $d$, the examples $(0,0)$ weight $0.308$ on $d$, and $(1,0)$ weight $\tfrac12$. The M-step gives $p_G=(\tfrac12,\tfrac12)$ and $p_R(1\mid d)\approx0.654$, $p_R(1\mid c)\approx0.346$. Further iterations give $0.725$, $0.799$, $0.853$, $0.877$ for $p_R(1\mid d)$: EM amplifies the initial preference and separates a cluster of liked films from one of disliked films.

:::

::: {#fig-expectation-maximization-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm,y=3cm]
\draw[->] (0,0) -- (5.6,0) node[lab,anchor=north east] {iteration};
\draw[->] (0,0) -- (0,1.1) node[lab,anchor=north west] {probability};
\foreach \t in {1,...,5} { \node[lab,tick] at (\t,-0.06) {\t}; }
\foreach \y in {0.5,1} { \node[lab,tick] at (-0.25,\y) {\y}; }
\draw[hl] plot coordinates {(0,0.6) (1,0.654) (2,0.725) (3,0.799) (4,0.853) (5,0.877)};
\draw[emph] plot coordinates {(0,0.4) (1,0.346) (2,0.275) (3,0.201) (4,0.147) (5,0.123)};
\node[lab,anchor=west] at (5.1,0.877) {$p_R(1\mid d)$};
\node[lab,anchor=west] at (5.1,0.123) {$p_R(1\mid c)$};
\end{tikzpicture}
\end{center}
```

Five iterations of EM on @exm-expectation-maximization-1: the two clusters' probabilities of a like move apart.

:::
