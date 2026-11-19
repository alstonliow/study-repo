---
title: "Particle Filtering"
sources: [cs188-19]
requires: [ai/temporal-models/hidden-markov-models, ai/bayesian-networks/likelihood-weighting]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 19 (particle filtering: representation, elapse time, observe, resample; robot localisation, SLAM), in our own wording; the consistency argument is our addition, reusing the likelihood-weighting proof; the example numbers are our own. -->

The forward algorithm (@thm-forward-algorithm) stores a probability for every state and sums over all predecessors at each step. When the state space is huge or continuous (a robot's position and heading, a ghost on a large grid), that is impossible. Particle filtering keeps a sample of states instead and moves the sample, so that frequent states stay frequent.

::: {#def-particle-filtering .definition name="Particle filtering"}

A *particle filter* represents the belief $B_t$ by a list of $N$ *particles*, states $x^{(1)},\dots,x^{(N)}$ (repetitions allowed); the approximate belief $\hat B_t(x)$ is the fraction of particles equal to $x$. One step, on evidence $e_{t+1}$:

1. (*elapse time*) replace each particle $x^{(k)}$ by a state drawn from $P(X_{t+1}\mid X_t=x^{(k)})$;
2. (*observe*) give each particle the weight $w^{(k)}=P(e_{t+1}\mid x^{(k)})$;
3. (*resample*) draw $N$ new particles independently from the old ones, each chosen with probability proportional to its weight; the new particles are unweighted.

The initial particles are drawn from $P(X_1)$ and then weighted by $e_1$ and resampled.

:::

```{=latex}
\begin{algorithm}
\caption{Particle filtering, one time step}
\begin{algorithmic}
\INPUT Particles $x^{(1)},\dots,x^{(N)}$, evidence $e$
\OUTPUT New particles
\FOR{$k=1$ \textbf{to} $N$}
    \STATE draw $x^{(k)}$ from $P(X'\mid X=x^{(k)})$ \COMMENT{elapse time}
    \STATE $w^{(k)}\gets P(e\mid x^{(k)})$ \COMMENT{observe}
\ENDFOR
\FOR{$k=1$ \textbf{to} $N$}
    \STATE $y^{(k)}\gets x^{(j)}$ with probability $w^{(j)}/\sum_iw^{(i)}$ \COMMENT{resample}
\ENDFOR
\RETURN $y^{(1)},\dots,y^{(N)}$
\end{algorithmic}
\end{algorithm}
```

The cost per step is $O(N)$ samples, independent of the number of states. Elapsing time is prior sampling of the next state (@def-probabilistic-program); observing is likelihood weighting (@def-likelihood-weighting) with the new evidence; resampling turns weighted particles back into unweighted ones, so that particles with low weight die out and the effort goes where the probability is.

::: {#prp-particle-filter-step .proposition name="One step of the particle filter is consistent"}

Suppose the particles at time $t$ are independent draws from the exact belief $B_t$. Then for every state $x'$, the weighted fraction $\sum_kw^{(k)}\mathbf 1\{x^{(k)}=x'\}\big/\sum_kw^{(k)}$ after the observe step converges to $B_{t+1}(x')$ with probability $1$ as $N\to\infty$, and the resampled particles are draws from this weighted distribution.

:::

::: {.proof}

1. After the elapse step each particle is drawn, independently of the others, from $\sum_xB_t(x)P(X_{t+1}\mid x)=B'_{t+1}$, by the elapse-time formula of @thm-forward-algorithm.
2. A particle's weight is $P(e_{t+1}\mid x^{(k)})$, so $\mathbb E\bigl[w\,\mathbf 1\{x=x'\}\bigr]=B'_{t+1}(x')P(e_{t+1}\mid x')$ and $\mathbb E[w]=\sum_{x}B'_{t+1}(x)P(e_{t+1}\mid x)$.
3. By the strong law of large numbers the numerator and denominator divided by $N$ converge to these expectations, so the ratio converges to $B'_{t+1}(x')P(e_{t+1}\mid x')/\sum_xB'_{t+1}(x)P(e_{t+1}\mid x)=B_{t+1}(x')$ by the observe formula.
4. Resampling chooses particle $j$ with probability $w^{(j)}/\sum_iw^{(i)}$, so each new particle equals $x'$ with probability equal to the weighted fraction.

:::

The resampled particles are not exactly independent draws from $B_{t+1}$ (they share ancestors), so errors can accumulate over time; with enough particles the filter tracks the belief well in practice.

::: {#exm-particle-filter-weather .example name="Ten particles"}

In the weather HMM of @exm-forward-weather, suppose that after the elapse step on day 3 the ten particles are $6$ rain and $4$ sun. The evidence "no umbrella" has $P(\text{no umbrella}\mid\text{rain})=0.2$ and $P(\text{no umbrella}\mid\text{sun})=0.7$, so the rain particles weigh $6\cdot0.2=1.2$ in total and the sun particles $4\cdot0.7=2.8$. Resampling draws ten particles, each rain with probability $1.2/4=0.3$; the expected new count is $3$ rain and $7$ sun, close to the exact belief $B_3(\text{rain})\approx0.316$.

:::

::: {#fig-particle-filtering-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\draw[cell frame] (0.000,1.400) rectangle (0.550,1.950);
\node[lab] at (0.275,1.675) {$R$};
\draw[cell frame] (0.550,1.400) rectangle (1.100,1.950);
\node[lab] at (0.825,1.675) {$R$};
\draw[cell frame] (1.100,1.400) rectangle (1.650,1.950);
\node[lab] at (1.375,1.675) {$R$};
\draw[cell frame] (1.650,1.400) rectangle (2.200,1.950);
\node[lab] at (1.925,1.675) {$R$};
\draw[cell frame] (2.200,1.400) rectangle (2.750,1.950);
\node[lab] at (2.475,1.675) {$R$};
\draw[cell frame] (2.750,1.400) rectangle (3.300,1.950);
\node[lab] at (3.025,1.675) {$R$};
\draw[cell frame] (3.300,1.400) rectangle (3.850,1.950);
\node[lab] at (3.575,1.675) {$S$};
\draw[cell frame] (3.850,1.400) rectangle (4.400,1.950);
\node[lab] at (4.125,1.675) {$S$};
\draw[cell frame] (4.400,1.400) rectangle (4.950,1.950);
\node[lab] at (4.675,1.675) {$S$};
\draw[cell frame] (4.950,1.400) rectangle (5.500,1.950);
\node[lab] at (5.225,1.675) {$S$};
\node[lab, anchor=east] at (-0.100,1.675) {after elapse};
\draw[cell frame] (0.000,0.700) rectangle (0.550,1.250);
\node[lab] at (0.275,0.975) {$0.2$};
\draw[cell frame] (0.550,0.700) rectangle (1.100,1.250);
\node[lab] at (0.825,0.975) {$0.2$};
\draw[cell frame] (1.100,0.700) rectangle (1.650,1.250);
\node[lab] at (1.375,0.975) {$0.2$};
\draw[cell frame] (1.650,0.700) rectangle (2.200,1.250);
\node[lab] at (1.925,0.975) {$0.2$};
\draw[cell frame] (2.200,0.700) rectangle (2.750,1.250);
\node[lab] at (2.475,0.975) {$0.2$};
\draw[cell frame] (2.750,0.700) rectangle (3.300,1.250);
\node[lab] at (3.025,0.975) {$0.2$};
\draw[hl cell] (3.300,0.700) rectangle (3.850,1.250);
\node[lab] at (3.575,0.975) {$0.7$};
\draw[hl cell] (3.850,0.700) rectangle (4.400,1.250);
\node[lab] at (4.125,0.975) {$0.7$};
\draw[hl cell] (4.400,0.700) rectangle (4.950,1.250);
\node[lab] at (4.675,0.975) {$0.7$};
\draw[hl cell] (4.950,0.700) rectangle (5.500,1.250);
\node[lab] at (5.225,0.975) {$0.7$};
\node[lab, anchor=east] at (-0.100,0.975) {weights};
\draw[cell frame] (0.000,-0.300) rectangle (0.550,0.250);
\node[lab] at (0.275,-0.025) {$R$};
\draw[cell frame] (0.550,-0.300) rectangle (1.100,0.250);
\node[lab] at (0.825,-0.025) {$R$};
\draw[cell frame] (1.100,-0.300) rectangle (1.650,0.250);
\node[lab] at (1.375,-0.025) {$R$};
\draw[cell frame] (1.650,-0.300) rectangle (2.200,0.250);
\node[lab] at (1.925,-0.025) {$S$};
\draw[cell frame] (2.200,-0.300) rectangle (2.750,0.250);
\node[lab] at (2.475,-0.025) {$S$};
\draw[cell frame] (2.750,-0.300) rectangle (3.300,0.250);
\node[lab] at (3.025,-0.025) {$S$};
\draw[cell frame] (3.300,-0.300) rectangle (3.850,0.250);
\node[lab] at (3.575,-0.025) {$S$};
\draw[cell frame] (3.850,-0.300) rectangle (4.400,0.250);
\node[lab] at (4.125,-0.025) {$S$};
\draw[cell frame] (4.400,-0.300) rectangle (4.950,0.250);
\node[lab] at (4.675,-0.025) {$S$};
\draw[cell frame] (4.950,-0.300) rectangle (5.500,0.250);
\node[lab] at (5.225,-0.025) {$S$};
\node[lab, anchor=east] at (-0.100,-0.025) {resampled};
\end{tikzpicture}
\end{center}
```

One particle-filter step in @exm-particle-filter-weather (R rain, S sun): after elapsing time six particles say rain; the evidence "no umbrella" weighs each sun particle $3.5$ times as much as a rain particle; resampling draws ten new particles with $P(\text{rain})=0.3$, here a typical outcome of $3$ rain and $7$ sun.

:::

::: {#rmk-particle-filtering-practice .remark name="Particles in practice"}

A state with no particle has estimated probability $0$, even if the true belief is not small, and the filter cannot recover it until some particle moves there; with too few particles all may collapse onto a few states (*particle depletion*), so implementations add some random particles or reinitialise when all weights are near $0$. Particle filters are the standard method for *robot localisation*: the state is the robot's pose, the transition model is its noisy motion and the sensor model compares sonar or laser readings with a map; the particle cloud starts spread over the whole map and contracts to the true pose. In *SLAM* (simultaneous localisation and mapping) each particle also carries its own estimate of the map.

:::
