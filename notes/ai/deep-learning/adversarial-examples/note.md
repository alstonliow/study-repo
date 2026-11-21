---
title: "Adversarial Examples"
sources: [cs231n-16, cs231n-10]
requires: [ai/deep-learning/network-visualization]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS231n course notes (Adversarial attacks: threat models, FGSM and its iterative form, one-pixel attack, adversarial training, defensive distillation, denoising; Understanding CNNs: fooling ConvNets), in our own wording; the optimality theorem, its proof and the example are our own. -->

Classifiers that match human accuracy can be fooled by changes to an input that a human does not notice. An *adversarial example* is an input $\mathbf{x}'=\mathbf{x}+\boldsymbol\delta$ with a small perturbation $\boldsymbol\delta$, typically $\lVert\boldsymbol\delta\rVert_\infty\le\varepsilon$ (no pixel changes by more than $\varepsilon$), that the model misclassifies although it classifies $\mathbf{x}$ correctly.

::: {#def-adversarial-threat-model .definition name="Threat models"}

An attack is described by when and what the adversary knows and wants.

1. *Evasion* attacks modify test inputs of a trained model; *poisoning* attacks modify the training data.
2. In a *white-box* attack the adversary knows the model, including its weights, and can compute gradients; in a *black-box* attack it can only query the model's outputs.
3. The goal is *confidence reduction*, *untargeted misclassification* (any wrong class), or *targeted misclassification* (a chosen class $t$).

:::

::: {#fig-adversarial-examples-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[emph] (-0.5,2.4) -- (3.6,-0.4);
\node[dot] (x) at (1.2,0.5) {};
\node[tick, left] at (x) {$\mathbf x$};
\draw[hl] (0.6,-0.1) rectangle (1.8,1.1);
\node[hl dot] at (1.8,1.1) {};
\node[tick, right] at (1.8,1.1) {$\mathbf x+\boldsymbol\eta$};
\node[tick] at (3.2,1.6) {other class};
\end{tikzpicture}
\end{center}
```

The threat model: the attacker may move $\mathbf x$ anywhere in the box $\lVert\boldsymbol\eta\rVert_\infty\le\varepsilon$; an adversarial example is a point of the box on the other side of the decision boundary

:::

::: {#def-fgsm .definition name="Fast gradient sign method"}

For a model with loss $J(\boldsymbol\theta,\mathbf{x},y)$ (for example the cross entropy loss, @def-cross-entropy-loss) and a budget $\varepsilon>0$, the *fast gradient sign method* (FGSM) produces

$$
\mathbf{x}'=\mathbf{x}+\varepsilon\,\operatorname{sign}\bigl(\nabla_{\mathbf{x}}J(\boldsymbol\theta,\mathbf{x},y)\bigr)\qquad\text{(untargeted)},\qquad
\mathbf{x}'=\mathbf{x}-\varepsilon\,\operatorname{sign}\bigl(\nabla_{\mathbf{x}}J(\boldsymbol\theta,\mathbf{x},t)\bigr)\qquad\text{(targeted at }t\text{)}.
$$

The *iterative* version repeats the step with a small $\varepsilon$, clipping $\mathbf{x}'$ back into the allowed set $\lVert\mathbf{x}'-\mathbf{x}\rVert_\infty\le\varepsilon_{\max}$ (and the valid pixel range) after each step, and stops as soon as the prediction changes.

:::

```{=latex}
\begin{algorithm}
\caption{Iterative fast gradient sign method (untargeted)}
\begin{algorithmic}
\INPUT model loss $J$, input $\mathbf{x}$ with label $y$, step $\varepsilon$, budget $\varepsilon_{\max}$, steps $T$
\OUTPUT perturbed input $\mathbf{x}'$
\STATE $\mathbf{x}'\gets\mathbf{x}$
\FOR{$t=1$ \TO $T$}
    \IF{the model misclassifies $\mathbf{x}'$}
        \RETURN $\mathbf{x}'$
    \ENDIF
    \STATE $\mathbf{x}'\gets\mathbf{x}'+\varepsilon\operatorname{sign}\bigl(\nabla_{\mathbf{x}}J(\boldsymbol\theta,\mathbf{x}',y)\bigr)$
    \STATE clip each entry of $\mathbf{x}'-\mathbf{x}$ to $[-\varepsilon_{\max},\varepsilon_{\max}]$
\ENDFOR
\RETURN $\mathbf{x}'$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-fgsm-optimal .theorem name="FGSM maximizes the linearized loss"}

Let $\mathbf{g}=\nabla_{\mathbf{x}}J(\boldsymbol\theta,\mathbf{x},y)\in\mathbb{R}^D$. Over all $\boldsymbol\delta$ with $\lVert\boldsymbol\delta\rVert_\infty\le\varepsilon$, the first-order change $\mathbf{g}\cdot\boldsymbol\delta$ of the loss is at most $\varepsilon\lVert\mathbf{g}\rVert_1$, and $\boldsymbol\delta=\varepsilon\operatorname{sign}(\mathbf{g})$ attains it.

:::

::: {.proof}

1. For each coordinate, $g_i\delta_i\le\lvert g_i\rvert\,\lvert\delta_i\rvert\le\varepsilon\lvert g_i\rvert$.
2. Summing, $\mathbf{g}\cdot\boldsymbol\delta\le\varepsilon\sum_i\lvert g_i\rvert=\varepsilon\lVert\mathbf{g}\rVert_1$.
3. For $\delta_i=\varepsilon\operatorname{sign}(g_i)$, each term is $\varepsilon\lvert g_i\rvert$, so equality holds.

:::

::: {#fig-adversarial-examples-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.2cm,y=1.2cm]
\draw[->] (-0.3,0) -- (3.4,0) node[lab,anchor=west] {$x_1$};
\draw[->] (0,-0.3) -- (0,2.6) node[lab,anchor=south] {$x_2$};
\draw[hl] (0.3,2.5) -- (3.2,0.05);
\node[lab,anchor=west] at (2.4,1.15) {boundary};
\draw[faint, dashed] (0.7,0.40) rectangle (1.60,1.3);
\node[dot] at (1.15, 0.85) {};
\node[lab,anchor=north east] at (1.15, 0.85) {$\mathbf x$};
\draw[->] (1.15, 0.85) -- (1.60,1.3);
\node[hl dot] at (1.60,1.3) {};
\node[lab,anchor=south west] at (1.60,1.3) {$\mathbf x+\varepsilon\operatorname{sign}(\mathbf g)$};
\end{tikzpicture}
\end{center}
```

FGSM against a linear classifier. Among the points of the box $\lVert\boldsymbol\delta\rVert_\infty\le\varepsilon$ (dashed), the score changes most at the corner in the direction $\operatorname{sign}(\mathbf g)$, which here lies across the decision boundary.

:::

::: {#exm-fgsm-linear .example name="Why high dimension helps the attacker"}

For a linear score $s=\mathbf{w}\cdot\mathbf{x}$, the perturbation $\varepsilon\operatorname{sign}(\mathbf{w})$ changes the score by $\varepsilon\lVert\mathbf{w}\rVert_1$. With $\mathbf{w}=(2,-1,3)$ and $\varepsilon=0.1$ the change is $0.6$. If the $D$ weights have average absolute value $m$, the change is $\varepsilon mD$: it grows linearly with the dimension, while the change of each pixel stays $\varepsilon$. For a $3\times32\times32$ image ($D=3072$), $\varepsilon=1/255$ and $m=0.1$, the score moves by about $1.2$, enough to flip many predictions.

:::

::: {#fig-adversarial-examples-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (6.4,0) node[lab, right] {dimension $d$};
\draw[->] (0,0) -- (0,2.6) node[lab, above] {$\mathbf w\cdot\boldsymbol\eta$};
\draw[hl] (0,0) -- (6,2.2);
\draw[faint, dashed] (0,0.5) -- (6,0.5);
\node[tick, right] at (6,0.5) {margin};
\end{tikzpicture}
\end{center}
```

For a linear score the FGSM perturbation $\boldsymbol\eta=\varepsilon\operatorname{sign}(\mathbf w)$ changes the score by $\varepsilon\lVert\mathbf w\rVert_1$, which grows linearly with the dimension: many tiny changes add up and cross any fixed margin

:::

So adversarial examples need no exotic non-linearity: models that behave almost linearly in their input (linear models, ReLU networks, LSTMs) are vulnerable precisely because they are easy to optimize. Adversarial examples often *transfer*: one crafted against one network also fools others trained on the same task, which enables black-box attacks through a substitute model. Attacks with other budgets exist; the *one-pixel attack* changes a single pixel, found by a derivative-free search (differential evolution) that needs only the model's output probabilities.

::: {#def-adversarial-training .definition name="Adversarial training"}

*Adversarial training* minimizes, instead of the training loss, the loss on perturbed examples,

$$
\min_{\boldsymbol\theta}\ \frac1N\sum_{i=1}^N\ \max_{\lVert\boldsymbol\delta\rVert_\infty\le\varepsilon}J(\boldsymbol\theta,\mathbf{x}_i+\boldsymbol\delta,y_i),
$$

approximating the inner maximum by FGSM or by a few iterative steps for each minibatch (often mixed with clean examples).

:::

::: {#rmk-adversarial-defences .remark name="Other defences"}

*Defensive distillation* trains a second network on the softened output probabilities (softmax at a high temperature) of a first one, which flattens the input gradients the attacks rely on. *Denoising* defences pass inputs through a learnt denoiser or a reconstruction step before classification. Both were later broken by attacks adapted to them; adversarial training remains the most reliable defence, at the cost of extra training time and some clean accuracy. A defence is credible only if it holds against an adversary who knows it.

:::
