---
title: "Gibbs Sampling"
sources: [cs221-17]
requires: [ai/bayesian-networks/rejection-sampling, math/probability/markov-chains/invariant-distributions]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 17 (Gibbs sampling, Markov blankets, when sampling methods are slow), in our own wording. The proposition that the target distribution is invariant is our own addition, linking to @sec-math-probability-markov-chains-invariant-distributions; proofs written out in steps. The run in the figure is our own. -->

Rejection sampling starts every sample from scratch and wastes the samples that miss the evidence. Gibbs sampling instead changes one variable at a time, starting from the previous sample, and never leaves the evidence.

::: {#def-gibbs-sampling .definition name="Gibbs sampling"}

To estimate $P(Q\mid E=e)$ in a Bayesian network, *Gibbs sampling* starts from any full assignment $x$ with $E=e$ and positive probability. It then repeatedly visits each non-evidence variable $X_i$ and replaces $x_i$ by a sample from its conditional distribution given all the other variables,

$$
P(X_i=v\mid X_{-i}=x_{-i})=\frac{P(x_1,\dots,x_{i-1},v,x_{i+1},\dots,x_n)}{\sum_{v'}P(x_1,\dots,x_{i-1},v',x_{i+1},\dots,x_n)},
$$

where $X_{-i}$ denotes all variables except $X_i$. After each sweep it records the value of $Q$, and it estimates $P(Q=q\mid E=e)$ by the fraction of sweeps with $Q=q$.

:::

The normalizer sums only over the values of $X_i$, so the joint table is never built. Each sample satisfies the evidence, so nothing is rejected; but consecutive samples are dependent, so more of them are needed.

```{=latex}
\begin{algorithm}
\caption{Gibbs sampling}
\begin{algorithmic}
\INPUT Bayesian network, evidence $E=e$, query $Q$, initial assignment $x$ with $x_E=e$, number of sweeps $m$
\OUTPUT Estimate of $P(Q\mid E=e)$
\STATE $N(q)\gets0$ for all values $q$
\FOR{$t=1$ \TO $m$}
    \FOR{each variable $X_i$ not in $E$}
        \STATE $w(v)\gets p(v\mid x_{\text{Parents}(i)})\prod_{j:\,i\in\text{Parents}(j)}p\bigl(x_j\mid x_{\text{Parents}(j)}\bigr)\big|_{x_i=v}$ for each value $v$
        \STATE draw $x_i$ with probability $w(x_i)/\sum_vw(v)$
    \ENDFOR
    \STATE $N(x_Q)\gets N(x_Q)+1$
\ENDFOR
\RETURN $N/m$
\end{algorithmic}
\end{algorithm}
```

The weights $w$ use only some factors of the joint probability; the next proposition says why that is enough.

::: {#def-markov-blanket .definition name="Markov blanket"}

The *Markov blanket* of a variable in a Bayesian network consists of its parents, its children, and the other parents of its children.

:::

::: {#prp-gibbs-markov-blanket .proposition name="Resampling needs only the Markov blanket"}

$P(X_i=v\mid X_{-i}=x_{-i})$ is proportional, as a function of $v$, to

$$
p\bigl(v\mid x_{\text{Parents}(i)}\bigr)\prod_{j:\ i\in\text{Parents}(j)}p\bigl(x_j\mid x_{\text{Parents}(j)}\bigr)\Big|_{x_i=v},
$$

which depends only on the values of the Markov blanket of $X_i$.

:::

::: {.proof}

1. By @def-bayesian-network the joint probability is a product with one factor per variable. Factor $j$ involves $x_i$ only if $j=i$ or $X_i$ is a parent of $X_j$.

2. All other factors are the same for every value $v$ of $X_i$, so they cancel between numerator and denominator in @def-gibbs-sampling.

3. The remaining factors mention $X_i$, its parents, its children and the children's other parents, which is the Markov blanket.

:::

On a chain $A\to B\to C\to D\to E$, resampling $C$ uses only $p(c\mid b)\,p(d\mid c)$; its Markov blanket is $\{B,D\}$. With the Markov blanket, one sweep costs $O(n\,\lvert\text{Domain}\rvert\,\lvert\text{MarkovBlanket}\rvert)$ instead of $O(n^2\lvert\text{Domain}\rvert)$.

::: {#prp-gibbs-invariant .proposition name="The conditional distribution is invariant"}

Each resampling step leaves $P(\cdot\mid E=e)$ invariant: if $x$ is distributed according to $P(\cdot\mid E=e)$ before $X_i$ is resampled, it is distributed so afterwards.

:::

::: {.proof}

1. Write $\mu=P(\cdot\mid E=e)$. Before the step, $x_{-i}$ has the marginal distribution $\mu(x_{-i})$.

2. The step keeps $x_{-i}$ and draws $x_i$ from $\mu(x_i\mid x_{-i})$, which equals $P(X_i=x_i\mid X_{-i}=x_{-i})$ because $x_{-i}$ already contains $E=e$.

3. So afterwards the pair has probability $\mu(x_{-i})\,\mu(x_i\mid x_{-i})=\mu(x)$.

:::

So the sequence of samples is a Markov chain (a *Markov chain Monte Carlo* method) with invariant distribution $P(\cdot\mid E=e)$ (@sec-math-probability-markov-chains-invariant-distributions). When the chain is irreducible and aperiodic its distribution converges to this one, and the averages converge to the conditional probabilities. How fast the chain forgets its start is its *mixing* time.

::: {#exm-gibbs-telephone .example name="Telephone"}

$A$ picks a bit uniformly at random; $B$ receives it, flipped with probability $0.2$; $C$ receives $B$'s bit, again flipped with probability $0.2$. Given $C=1$, exactly $P(A=1\mid C=1)=0.8^2+0.2^2=0.68$. Gibbs sampling starts at $(A,B)=(0,0)$ and alternates: $A$ given $B=b$ is drawn with weights $p(a)\,p(b\mid a)$, and $B$ given $A=a$, $C=1$ with weights $p(b\mid a)\,p(C{=}1\mid b)$; for $a=1$ this gives $P(B=1\mid A=1,C=1)=\frac{0.64}{0.64+0.04}\approx0.94$. In one run the running estimate of $P(A=1\mid C=1)$ was $0.30$ after $10$ sweeps, $0.58$ after $100$ and $0.674$ after $1000$.

:::

::: {#fig-gibbs-sampling-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (5.4,0) node[lab,anchor=north east] {sweeps};
\draw[->] (0,0) -- (0,3.3) node[lab,anchor=north west] {estimate of $P(A=1\mid C=1)$};
\foreach \t in {250,500,750,1000} { \node[lab,tick] at ({\t/200},-0.25) {\t}; }
\foreach \y in {0.5,1} { \node[lab,tick] at (-0.3,{3*\y}) {\y}; }
\draw[faint,dashed] (0,2.04) -- (5,2.04) node[lab,anchor=west] {$0.68$};
\draw[hl] plot coordinates {(0.005,0.000) (0.025,1.800) (0.050,0.900) (0.125,1.080) (0.250,1.260) (0.375,1.600) (0.500,1.740) (0.625,1.848) (0.750,1.860) (0.875,1.869) (1.000,1.845) (1.125,1.920) (1.250,1.896) (1.375,1.876) (1.500,1.950) (1.625,2.031) (1.750,2.031) (1.875,2.040) (2.000,2.070) (2.125,2.096) (2.250,2.113) (2.375,2.122) (2.500,2.094) (2.625,2.074) (2.750,2.062) (2.875,2.050) (3.000,2.050) (3.125,2.050) (3.250,2.049) (3.375,2.071) (3.500,2.040) (3.625,2.040) (3.750,2.036) (3.875,2.036) (4.000,2.044) (4.125,2.040) (4.250,2.040) (4.375,2.043) (4.500,2.033) (4.625,2.030) (4.750,2.024) (4.875,2.022) (5.000,2.022)};
\end{tikzpicture}
\end{center}
```

Running estimate during one run of Gibbs sampling on the telephone example (@exm-gibbs-telephone); the dashed line is the exact value $0.68$.

:::

::: {#rmk-gibbs-sampling-1 .remark name="When each method is slow"}

Rejection sampling is slow when the evidence is rare; Gibbs sampling clamps the evidence and does not care. Gibbs sampling is slow when unobserved variables are strongly dependent, because it changes one at a time. In the alarm network given $A=1$, moving from $(B,E)=(0,1)$ to $(1,0)$ must pass through the rare state $(1,1)$, since $(0,0)$ is impossible, so the chain stays in one mode for a long time. If two variables must always be equal, changing either alone has probability $0$ and the chain never moves, although rejection sampling (with no evidence) works perfectly.

:::
