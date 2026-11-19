---
title: "Local Search: Min-Conflicts, Hill Climbing and Simulated Annealing"
sources: [cs188-5]
requires: [ai/constraint-satisfaction/constraint-satisfaction-problems, math/probability/markov-chains/invariant-distributions]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 5 (iterative improvement for CSPs, min-conflicts, local search, hill climbing, simulated annealing, genetic algorithms), in our own wording; the 4-queens run was checked by a short Python simulation. The stationary-distribution property of simulated annealing is our addition, proved from the Markov chain notes. -->

Backtracking builds a solution one variable at a time. *Local search* instead keeps one complete assignment, possibly violating constraints, and improves it by small changes. It uses constant memory and often finds solutions of huge problems fast, but it is incomplete: it may never find a solution that exists, and it cannot prove that none exists.

::: {#def-min-conflicts .definition name="Min-conflicts"}

*Min-conflicts* starts from a complete assignment of a CSP and repeats: choose at random a variable involved in a violated constraint, and reassign it the value that violates the fewest constraints given the other variables (ties broken at random). It stops at a solution or after a step limit.

:::

```{=latex}
\begin{algorithm}
\caption{Min-conflicts}
\begin{algorithmic}
\INPUT CSP, step limit $L$
\OUTPUT A solution, or failure
\STATE $\alpha\gets$ a complete assignment
\FOR{$t=1$ \textbf{to} $L$}
    \IF{$\alpha$ is a solution}
        \RETURN $\alpha$
    \ENDIF
    \STATE $X\gets$ a random variable in a violated constraint
    \STATE $\alpha(X)\gets\operatorname{arg\,min}_{x\in D_X}$ (number of violated constraints with $X=x$)
\ENDFOR
\RETURN failure
\end{algorithmic}
\end{algorithm}
```

::: {#exm-min-conflicts-four-queens .example name="Min-conflicts on 4-queens"}

In @exm-n-queens-csp with $N=4$, let $h$ be the number of attacking pairs. From $(Q_1,\dots,Q_4)=(1,1,1,1)$, all in row 1 with $h=6$, one run of min-conflicts moves $Q_1$ to row $2$ ($h=4$), then $Q_2$ to row $4$ ($h=1$: only $Q_3,Q_4$ share row $1$), then $Q_4$ to row $3$, where it is attacked by no queen: $(2,4,1,3)$, $h=0$, a solution. Had the third step chosen $Q_3$ instead, every row for $Q_3$ would have one conflict, and the run would stay at $h=1$ until a later random choice picked $Q_4$.

:::

::: {#fig-local-search-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\draw[cell frame] (0.00,0.00) rectangle (0.38,0.38);
\draw[cell frame] (0.00,0.38) rectangle (0.38,0.76);
\draw[cell frame] (0.00,0.76) rectangle (0.38,1.14);
\draw[cell frame] (0.00,1.14) rectangle (0.38,1.52);
\draw[cell frame] (0.38,0.00) rectangle (0.76,0.38);
\draw[cell frame] (0.38,0.38) rectangle (0.76,0.76);
\draw[cell frame] (0.38,0.76) rectangle (0.76,1.14);
\draw[cell frame] (0.38,1.14) rectangle (0.76,1.52);
\draw[cell frame] (0.76,0.00) rectangle (1.14,0.38);
\draw[cell frame] (0.76,0.38) rectangle (1.14,0.76);
\draw[cell frame] (0.76,0.76) rectangle (1.14,1.14);
\draw[cell frame] (0.76,1.14) rectangle (1.14,1.52);
\draw[cell frame] (1.14,0.00) rectangle (1.52,0.38);
\draw[cell frame] (1.14,0.38) rectangle (1.52,0.76);
\draw[cell frame] (1.14,0.76) rectangle (1.52,1.14);
\draw[cell frame] (1.14,1.14) rectangle (1.52,1.52);
\node[dot] at (0.19,0.19) {};
\node[dot] at (0.57,0.19) {};
\node[dot] at (0.95,0.19) {};
\node[dot] at (1.33,0.19) {};
\node[lab, tick, align=center] at (0.76,-0.32) {$h=6$};
\draw[cell frame] (2.10,0.00) rectangle (2.48,0.38);
\draw[cell frame] (2.10,0.38) rectangle (2.48,0.76);
\draw[cell frame] (2.10,0.76) rectangle (2.48,1.14);
\draw[cell frame] (2.10,1.14) rectangle (2.48,1.52);
\draw[cell frame] (2.48,0.00) rectangle (2.86,0.38);
\draw[cell frame] (2.48,0.38) rectangle (2.86,0.76);
\draw[cell frame] (2.48,0.76) rectangle (2.86,1.14);
\draw[cell frame] (2.48,1.14) rectangle (2.86,1.52);
\draw[cell frame] (2.86,0.00) rectangle (3.24,0.38);
\draw[cell frame] (2.86,0.38) rectangle (3.24,0.76);
\draw[cell frame] (2.86,0.76) rectangle (3.24,1.14);
\draw[cell frame] (2.86,1.14) rectangle (3.24,1.52);
\draw[cell frame] (3.24,0.00) rectangle (3.62,0.38);
\draw[cell frame] (3.24,0.38) rectangle (3.62,0.76);
\draw[cell frame] (3.24,0.76) rectangle (3.62,1.14);
\draw[cell frame] (3.24,1.14) rectangle (3.62,1.52);
\node[dot] at (2.29,0.57) {};
\node[dot] at (2.67,0.19) {};
\node[dot] at (3.05,0.19) {};
\node[dot] at (3.43,0.19) {};
\node[lab, tick, align=center] at (2.86,-0.32) {$h=4$};
\draw[->] (1.60,0.76) -- (2.00,0.76);
\draw[cell frame] (4.20,0.00) rectangle (4.58,0.38);
\draw[cell frame] (4.20,0.38) rectangle (4.58,0.76);
\draw[cell frame] (4.20,0.76) rectangle (4.58,1.14);
\draw[cell frame] (4.20,1.14) rectangle (4.58,1.52);
\draw[cell frame] (4.58,0.00) rectangle (4.96,0.38);
\draw[cell frame] (4.58,0.38) rectangle (4.96,0.76);
\draw[cell frame] (4.58,0.76) rectangle (4.96,1.14);
\draw[cell frame] (4.58,1.14) rectangle (4.96,1.52);
\draw[cell frame] (4.96,0.00) rectangle (5.34,0.38);
\draw[cell frame] (4.96,0.38) rectangle (5.34,0.76);
\draw[cell frame] (4.96,0.76) rectangle (5.34,1.14);
\draw[cell frame] (4.96,1.14) rectangle (5.34,1.52);
\draw[cell frame] (5.34,0.00) rectangle (5.72,0.38);
\draw[cell frame] (5.34,0.38) rectangle (5.72,0.76);
\draw[cell frame] (5.34,0.76) rectangle (5.72,1.14);
\draw[cell frame] (5.34,1.14) rectangle (5.72,1.52);
\node[dot] at (4.39,0.57) {};
\node[dot] at (4.77,1.33) {};
\node[dot] at (5.15,0.19) {};
\node[dot] at (5.53,0.19) {};
\node[lab, tick, align=center] at (4.96,-0.32) {$h=1$};
\draw[->] (3.70,0.76) -- (4.10,0.76);
\draw[cell frame] (6.30,0.00) rectangle (6.68,0.38);
\draw[cell frame] (6.30,0.38) rectangle (6.68,0.76);
\draw[cell frame] (6.30,0.76) rectangle (6.68,1.14);
\draw[cell frame] (6.30,1.14) rectangle (6.68,1.52);
\draw[cell frame] (6.68,0.00) rectangle (7.06,0.38);
\draw[cell frame] (6.68,0.38) rectangle (7.06,0.76);
\draw[cell frame] (6.68,0.76) rectangle (7.06,1.14);
\draw[cell frame] (6.68,1.14) rectangle (7.06,1.52);
\draw[cell frame] (7.06,0.00) rectangle (7.44,0.38);
\draw[cell frame] (7.06,0.38) rectangle (7.44,0.76);
\draw[cell frame] (7.06,0.76) rectangle (7.44,1.14);
\draw[cell frame] (7.06,1.14) rectangle (7.44,1.52);
\draw[cell frame] (7.44,0.00) rectangle (7.82,0.38);
\draw[cell frame] (7.44,0.38) rectangle (7.82,0.76);
\draw[cell frame] (7.44,0.76) rectangle (7.82,1.14);
\draw[cell frame] (7.44,1.14) rectangle (7.82,1.52);
\node[dot] at (6.49,0.57) {};
\node[dot] at (6.87,1.33) {};
\node[dot] at (7.25,0.19) {};
\node[dot] at (7.63,0.95) {};
\node[lab, tick, align=center] at (7.06,-0.32) {$h=0$};
\draw[->] (5.80,0.76) -- (6.20,0.76);
\end{tikzpicture}
\end{center}
```

The run of min-conflicts in @exm-min-conflicts-four-queens: from all queens in row $1$ ($h=6$ attacking pairs), moving $Q_1$, then $Q_2$, then $Q_4$ reaches a solution.

:::

Empirically, min-conflicts from a random start solves $n$-queens in a number of steps that hardly grows with $n$, even for millions of queens, and the same holds for random CSPs except near a critical ratio of constraints to variables, where problems are hardest.

The same idea applies to any optimisation problem over states with a notion of neighbouring states and an objective $E$ to maximise (for a CSP, minus the number of violated constraints).

::: {#def-hill-climbing .definition name="Hill climbing"}

*Hill climbing* starts at some state and repeatedly moves to the neighbour with the largest $E$, as long as that is larger than the current value; then it stops and returns the current state.

:::

Hill climbing stops at a *local maximum*, a state no neighbour improves, which need not be a *global maximum*. It also stalls on *plateaus* (flat regions; allowing a limited number of sideways moves helps) and on *ridges* (where every single move goes down although a combination goes up). *Random restarts* repeat it from random states and keep the best result; if one run succeeds with probability $p$, the expected number of runs is $1/p$ (a geometric distribution).

::: {#def-simulated-annealing .definition name="Simulated annealing"}

*Simulated annealing* keeps a current state $x$ and a *temperature* $T>0$ that decreases over time according to a *schedule*. At each step it picks a random neighbour $x'$; if $E(x')\ge E(x)$ it moves to $x'$, and otherwise it moves with probability $e^{(E(x')-E(x))/T}$.

:::

::: {#fig-local-search-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\draw[emph] plot[smooth] coordinates {(0.00,0.154) (0.10,0.160) (0.20,0.170) (0.30,0.188) (0.40,0.219) (0.50,0.269) (0.60,0.343) (0.70,0.446) (0.80,0.579) (0.90,0.737) (1.00,0.910) (1.10,1.078) (1.20,1.220) (1.30,1.316) (1.40,1.350) (1.50,1.316) (1.60,1.221) (1.70,1.078) (1.80,0.910) (1.90,0.739) (2.00,0.582) (2.10,0.451) (2.20,0.352) (2.30,0.285) (2.40,0.247) (2.50,0.235) (2.60,0.246) (2.70,0.279) (2.80,0.336) (2.90,0.418) (3.00,0.529) (3.10,0.669) (3.20,0.838) (3.30,1.034) (3.40,1.248) (3.50,1.468) (3.60,1.682) (3.70,1.871) (3.80,2.021) (3.90,2.117) (4.00,2.150) (4.10,2.117) (4.20,2.021) (4.30,1.871) (4.40,1.682) (4.50,1.468) (4.60,1.248) (4.70,1.034) (4.80,0.838) (4.90,0.668) (5.00,0.528) (5.10,0.416) (5.20,0.331) (5.30,0.270) (5.40,0.226) (5.50,0.197)};
\draw[->] (0,0) -- (5.8,0) node[lab, anchor=west] {state};
\draw[->] (0,0) -- (0,2.6) node[lab, anchor=south] {$E$};
\node[dot] at (0.6,0.34) {};
\draw[->, hl] (0.6,0.49) to[bend left=20] (1.35,1.47);
\node[lab, tick, anchor=east] at (1.15,1.55) {local maximum};
\node[lab, tick] at (4.0,2.40) {global maximum};
\draw[->, dashed] (1.6,1.32) to[bend left=30] (3.2,0.99);
\node[lab, tick] at (2.6,1.85) {downhill move};
\end{tikzpicture}
\end{center}
```

Hill climbing from the left stops at the local maximum (solid arrow). Simulated annealing sometimes accepts a downhill move (dashed), which can carry it into the slope of the global maximum.

:::

At high temperature almost every move is accepted and the search wanders; as $T$ falls, downhill moves become rare and the search settles near a maximum. Uphill moves are always accepted, so the downhill ones are the escape route from local maxima.

::: {#prp-annealing-boltzmann .proposition name="Fixed-temperature annealing samples the Boltzmann distribution"}

Let the state space be finite, every state have exactly $k$ neighbours, the neighbour relation be symmetric and the resulting chain be irreducible. For a fixed $T$, simulated annealing is a Markov chain with invariant distribution
$$
\pi_T(x)=\frac{e^{E(x)/T}}{\sum_{y}e^{E(y)/T}},
$$
and as $T\to0$, $\pi_T$ puts all its mass on the global maxima of $E$, equally divided among them.

:::

::: {.proof}

1. The next state depends only on the current one, so the process is a Markov chain (@def-markov-chain). For neighbours $x\ne x'$ its transition probability is
$$
P(x,x')=\frac1k\min\bigl(1,e^{(E(x')-E(x))/T}\bigr).
$$
2. Then $\pi_T(x)P(x,x')=\frac{1}{kZ}\min\bigl(e^{E(x)/T},e^{E(x')/T}\bigr)$ with $Z=\sum_ye^{E(y)/T}$, which is symmetric in $x,x'$. So $\pi_T(x)P(x,x')=\pi_T(x')P(x',x)$ for neighbours, and trivially for non-neighbours (both sides $0$) and for $x=x'$ (*detailed balance*).
3. Summing detailed balance over $x$: $\sum_x\pi_T(x)P(x,x')=\pi_T(x')\sum_xP(x',x)=\pi_T(x')$. So $\pi_T$ is invariant (@def-invariant-distribution).
4. Let $E^{*}=\max E$ and $m$ the number of maximisers. Dividing numerator and denominator by $e^{E^{*}/T}$, $\pi_T(x)=e^{(E(x)-E^{*})/T}\big/\sum_ye^{(E(y)-E^{*})/T}$. As $T\to0$ each term with $E(y)<E^{*}$ tends to $0$ and each with $E(y)=E^{*}$ equals $1$, so $\pi_T(x)\to1/m$ for maximisers and $\to0$ otherwise.

:::

This is why a slow enough cooling schedule finds a global maximum with probability approaching $1$; but "slow enough" can mean longer than exhaustive search, and in practice schedules are tuned by experiment.

::: {#def-genetic-algorithm .definition name="Genetic algorithm"}

A *genetic algorithm* keeps a population of $k$ states encoded as strings. Each generation selects pairs of parents at random with probability increasing in their *fitness* $E$, forms each child by *crossover* (a prefix of one parent followed by the rest of the other, at a random cut point) and applies random *mutations* (changing a symbol with small probability).

:::

::: {#fig-local-search-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\draw[hl cell] (0.000,1.400) rectangle (0.550,1.950);
\node[lab] at (0.275,1.675) {$2$};
\draw[hl cell] (0.550,1.400) rectangle (1.100,1.950);
\node[lab] at (0.825,1.675) {$4$};
\draw[hl cell] (1.100,1.400) rectangle (1.650,1.950);
\node[lab] at (1.375,1.675) {$7$};
\draw[cell frame] (1.650,1.400) rectangle (2.200,1.950);
\node[lab] at (1.925,1.675) {$4$};
\draw[cell frame] (2.200,1.400) rectangle (2.750,1.950);
\node[lab] at (2.475,1.675) {$8$};
\draw[cell frame] (2.750,1.400) rectangle (3.300,1.950);
\node[lab] at (3.025,1.675) {$5$};
\draw[cell frame] (3.300,1.400) rectangle (3.850,1.950);
\node[lab] at (3.575,1.675) {$5$};
\draw[cell frame] (3.850,1.400) rectangle (4.400,1.950);
\node[lab] at (4.125,1.675) {$2$};
\node[lab, anchor=east] at (-0.100,1.675) {parent 1};
\draw[cell frame] (0.000,0.700) rectangle (0.550,1.250);
\node[lab] at (0.275,0.975) {$3$};
\draw[cell frame] (0.550,0.700) rectangle (1.100,1.250);
\node[lab] at (0.825,0.975) {$2$};
\draw[cell frame] (1.100,0.700) rectangle (1.650,1.250);
\node[lab] at (1.375,0.975) {$7$};
\draw[hl cell] (1.650,0.700) rectangle (2.200,1.250);
\node[lab] at (1.925,0.975) {$5$};
\draw[hl cell] (2.200,0.700) rectangle (2.750,1.250);
\node[lab] at (2.475,0.975) {$2$};
\draw[hl cell] (2.750,0.700) rectangle (3.300,1.250);
\node[lab] at (3.025,0.975) {$4$};
\draw[hl cell] (3.300,0.700) rectangle (3.850,1.250);
\node[lab] at (3.575,0.975) {$1$};
\draw[hl cell] (3.850,0.700) rectangle (4.400,1.250);
\node[lab] at (4.125,0.975) {$1$};
\node[lab, anchor=east] at (-0.100,0.975) {parent 2};
\draw[hl cell] (0.000,-0.300) rectangle (0.550,0.250);
\node[lab] at (0.275,-0.025) {$2$};
\draw[hl cell] (0.550,-0.300) rectangle (1.100,0.250);
\node[lab] at (0.825,-0.025) {$4$};
\draw[hl cell] (1.100,-0.300) rectangle (1.650,0.250);
\node[lab] at (1.375,-0.025) {$7$};
\draw[hl cell] (1.650,-0.300) rectangle (2.200,0.250);
\node[lab] at (1.925,-0.025) {$5$};
\draw[hl cell] (2.200,-0.300) rectangle (2.750,0.250);
\node[lab] at (2.475,-0.025) {$2$};
\draw[hl cell] (2.750,-0.300) rectangle (3.300,0.250);
\node[lab] at (3.025,-0.025) {$4$};
\draw[hl cell] (3.300,-0.300) rectangle (3.850,0.250);
\node[lab] at (3.575,-0.025) {$1$};
\draw[hl cell] (3.850,-0.300) rectangle (4.400,0.250);
\node[lab] at (4.125,-0.025) {$1$};
\node[lab, anchor=east] at (-0.100,-0.025) {child};
\draw[faint, dashed] (1.65,-0.4) -- (1.65,2.05);
\end{tikzpicture}
\end{center}
```

Crossover of two $8$-queens states written as row numbers per column, cut after column $3$: the child takes the first three columns from parent 1 and the rest from parent 2. A mutation would then change one entry at random.

:::

Crossover helps when good blocks of a string are meaningful on their own: in $8$-queens, with one row per column, the left columns of one good board and the right columns of another can combine into a better board. Like beam search (@def-beam-search), a genetic algorithm runs many searches at once and concentrates effort on the most promising ones.
