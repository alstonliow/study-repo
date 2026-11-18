---
title: "Function Approximation"
sources: [cs221-10]
requires: [ai/reinforcement-learning/model-free-rl, ai/machine-learning/gradient-descent]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 10 (Q-learning with function approximation), in our own wording. The run in the example is our own (NumPy code in code.md); proof written out in steps. -->

Tabular methods keep one number $\hat Q(s,a)$ per state–action pair and learn each one separately: visiting location $37$ says nothing about location $38$. When states are images or sentences there are far too many to enumerate. *Function approximation* replaces the table by a parametrized function, chosen exactly as in supervised learning (hypothesis class, loss, optimizer; @sec-ai-machine-learning-supervised-learning).

::: {#def-q-function-approximation .definition name="Q-learning with function approximation"}

Let $\boldsymbol\phi(s,a)\in\mathbb{R}^d$ be a *feature vector* of a state and action, and $Q_\theta(s,a)$ a function of it with parameters $\theta$: *linear*, $Q_\theta(s,a)=\theta\cdot\boldsymbol\phi(s,a)$, or a neural network such as $\boldsymbol\alpha\cdot a(W\boldsymbol\phi(s,a))$. On each transition $(s,a,r,s')$, Q-learning takes the target $y=r+\gamma\max_{a'}Q_\theta(s',a')$ ($y=r$ at an end state), treats it as a constant, and takes a gradient step on the squared loss $\tfrac12(Q_\theta(s,a)-y)^2$:

$$
\theta\ \gets\ \theta-\eta\,\bigl(Q_\theta(s,a)-y\bigr)\,\nabla_\theta Q_\theta(s,a),
$$

which for a linear $Q_\theta$ is $\theta\gets\theta-\eta\,(Q_\theta(s,a)-y)\,\boldsymbol\phi(s,a)$.

:::

```{=latex}
\begin{algorithm}
\caption{Q-learning with linear function approximation}
\begin{algorithmic}
\INPUT Environment, features $\boldsymbol\phi$, learning rate $\eta$, exploration rate $\epsilon$, number of episodes $m$
\OUTPUT Parameters $\theta$
\STATE $\theta\gets\mathbf{0}$
\FOR{$i=1$ \TO $m$}
    \STATE $s\gets s_{\text{start}}$
    \WHILE{not $\text{IsEnd}(s)$}
        \STATE $a\gets$ $\epsilon$-greedy action for $Q_\theta(s,\cdot)=\theta\cdot\boldsymbol\phi(s,\cdot)$
        \STATE take $a$; observe $r$ and $s'$
        \STATE $y\gets r$ \textbf{if} $\text{IsEnd}(s')$ \textbf{else} $r+\gamma\max_{a'}\theta\cdot\boldsymbol\phi(s',a')$
        \STATE $\theta\gets\theta-\eta\,(\theta\cdot\boldsymbol\phi(s,a)-y)\,\boldsymbol\phi(s,a)$; \quad $s\gets s'$
    \ENDWHILE
\ENDFOR
\RETURN $\theta$
\end{algorithmic}
\end{algorithm}
```

::: {#prp-indicator-features-tabular .proposition name="Indicator features give tabular Q-learning"}

Let $\boldsymbol\phi(s,a)$ have one coordinate for each state–action pair, equal to $\mathbf{1}[(s,a)=(\tilde s,\tilde a)]$ in coordinate $(\tilde s,\tilde a)$. Then linear Q-learning with learning rate $\eta$ is tabular Q-learning (@def-q-learning) with the same learning rate, where $\hat Q(s,a)=\theta_{(s,a)}$.

:::

::: {.proof}

1. With these features $\theta\cdot\boldsymbol\phi(s,a)=\theta_{(s,a)}$, so $Q_\theta$ is the table $\theta$ and the two targets agree.

2. The update adds $-\eta(\theta_{(s,a)}-y)\boldsymbol\phi(s,a)$, which changes only coordinate $(s,a)$, by $-\eta(\hat Q(s,a)-y)$: the tabular update.

:::

The gain comes from features shared between states: an update in one state then moves the estimates of all states with similar features (*generalization*), at the price of being unable to represent every Q-function exactly. Choosing such features needs knowledge of what matters about a state (*abstraction*).

::: {#exm-function-approximation-1 .example name="Doubling features for the flaky tram"}

On the flaky tram with $n=100$ and $p=0.4$, roughly what matters is how many tram rides are left, $d(s)=\log_2(n/s)$. Take the four features $\boldsymbol\phi(s,a)=\bigl(\mathbf{1}[a=\text{walk}],\ \mathbf{1}[a=\text{tram}],\ \mathbf{1}[a=\text{walk}]\,d(s),\ \mathbf{1}[a=\text{tram}]\,d(s)\bigr)$. In one run of $30$ episodes ($\eta=0.01$, $\epsilon=0.2$; code in this note's code examples) linear Q-learning reaches $\theta\approx(-6.73,-1.61,-2.32,-3.49)$, so $Q_\theta(s,\text{walk})\approx-6.73-2.32\,d$ and $Q_\theta(s,\text{tram})\approx-1.61-3.49\,d$. The tram is preferred when $d<4.38$, that is $s\ge5$: the greedy policy walks to $5$, rides the tram to $80$ and walks the rest, with expected time $37.33$ against $99$ for walking (the optimum is $19.33$). Four parameters cover all $100$ states, but they cannot express the optimal policy, which walks a step between some rides; with enough data, indicator features eventually do better.

:::

::: {#fig-function-approximation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.8cm,y=0.12cm]
\draw[->] (0,0) -- (7.3,0) node[lab,anchor=west] {$d(s)$};
\draw[->] (0,0) -- (0,-32) node[lab,anchor=north west] {$Q_\theta$};
\foreach \d in {1,...,6} { \node[lab,tick] at (\d,1.5) {\d}; }
\foreach \q in {-10,-20,-30} { \node[lab,tick] at (-0.4,\q) {\q}; }
\draw[hl] (0,-6.73) -- (6.64,{-6.73-2.32*6.64}) node[lab,anchor=west] {walk};
\draw[emph] (0,-1.61) -- (6.64,{-1.61-3.49*6.64}) node[lab,anchor=west] {tram};
\draw[faint,dashed] (4.38,0) -- (4.38,-30);
\node[lab,anchor=north] at (4.38,-30) {$s\approx4.8$};
\end{tikzpicture}
\end{center}
```

The learned linear Q-values of @exm-function-approximation-1 as functions of $d(s)$. Left of the dashed line (large $s$) the tram looks better, right of it (small $s$) walking does.

:::

::: {#rmk-function-approximation-1 .remark name="Deep Q-learning"}

With a neural network $Q_\theta$ the same update is *deep Q-learning*. The target is not differentiated (a *stop-gradient*), because it is an estimate standing in for the true utility, not part of the prediction.

:::
