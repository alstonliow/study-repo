---
title: "Monitoring Training, Hyperparameter Search and Ensembles"
sources: [cs231n-7]
requires: [ai/deep-learning/momentum-and-adaptive-methods, ai/deep-learning/gradient-checking, ai/machine-learning/generalization]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS231n course notes (Neural networks part 3: babysitting the learning process, hyperparameter optimization, model ensembles), in our own wording; the two propositions and their proofs are our own; the numbers were computed in Python. -->

Training a network well is an experimental process: watch a few quantities during training, adjust the hyperparameters, and repeat. This note collects the standard signals and the standard search procedure.

::: {#rmk-training-diagnostics-loss .remark name="Reading the loss curve"}

Plot the training loss per iteration (or per epoch, the number of passes over the training data). With a learning rate that is too high the loss falls fast and then levels off at a high value, or explodes; too low, and it decreases slowly and almost linearly; a good rate decreases fast and keeps improving. The wiggle around the trend reflects the batch size: smaller minibatches give noisier curves. A loss that becomes NaN usually means a learning rate far too high or a numerical bug (for example $\log0$).

:::

::: {#fig-training-diagnostics-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (6.4,0) node[lab, right] {epoch};
\draw[->] (0,0) -- (0,2.8) node[lab, above] {loss};
\draw[faint, domain=0:6, samples=80, smooth, variable=\x] plot ({\x}, {2.4*exp(-0.15*\x)+0.2});
\draw[emph, domain=0:6, samples=80, smooth, variable=\x] plot ({\x}, {2.4*exp(-1.6*\x)+0.9});
\draw[hl, domain=0:6, samples=80, smooth, variable=\x] plot ({\x}, {2.4*exp(-0.8*\x)+0.25});
\node[tick] at (5.5,1.25) {too low};
\node[tick] at (5.5,0.75) {too high};
\node[tick, text=accent] at (5.5,0.4) {good};
\end{tikzpicture}
\end{center}
```

Typical loss curves: too low a learning rate decays slowly, too high a rate drops fast and stalls at a high loss, and a good rate decreases steadily to a low value

:::

::: {#rmk-training-diagnostics-accuracy .remark name="Training versus validation accuracy"}

The gap between training and validation accuracy measures overfitting (@def-overfitting). A large gap that keeps growing calls for stronger regularization (more $\ell_2$, more dropout, more data); no gap at all, with both accuracies low, suggests the model is too small or too regularized. Validation accuracy is checked every epoch, and the parameters with the best validation accuracy are kept (*early stopping*).

:::

::: {#fig-training-diagnostics-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (6.4,0) node[lab, right] {epoch};
\draw[->] (0,0) -- (0,2.8) node[lab, above] {accuracy};
\draw[emph, domain=0:6, samples=80, smooth, variable=\x] plot ({\x}, {2.4-2.0*exp(-0.7*\x)});
\draw[hl, domain=0:6, samples=80, smooth, variable=\x] plot ({\x}, {1.7-1.3*exp(-0.9*\x)});
\draw[<->] (5.4,1.69) -- node[tick, right] {gap} (5.4,2.35);
\node[tick] at (2.0,2.2) {training};
\node[tick, text=accent] at (2.4,1.25) {validation};
\end{tikzpicture}
\end{center}
```

A large gap between training and validation accuracy signals overfitting: regularise more or get more data. No gap at all suggests the model could be larger

:::

::: {#rmk-training-diagnostics-ratio .remark name="Update size and activations"}

The ratio of the size of an update to the size of the weights, $\lVert\Delta W\rVert/\lVert W\rVert$, computed per layer, should be around $10^{-3}$: much smaller means the learning rate is too low, much larger that it is too high. Histograms of each layer's activations and gradients reveal saturated units (@prp-sigmoid-saturation), dead ReLUs, or a bad initialization scale; for image models, the first-layer weights should look like smooth, structured filters, not noise.

:::

::: {#def-random-hyperparameter-search .definition name="Random hyperparameter search"}

*Random search* chooses $n$ hyperparameter settings independently at random from a search region and trains one model per setting. Scale parameters such as the learning rate and the regularization strength are drawn *on a log scale*, $\eta=10^u$ with $u$ uniform on an interval like $[-6,-1]$; others, such as the dropout keep probability, uniformly. The search is *staged*: a coarse range with short runs (one epoch or less), then a narrower range around the best results with longer runs.

:::

::: {#prp-random-search-coverage .proposition name="Why random search beats grid search"}

1. If the validation error depends essentially on one of two hyperparameters, a grid of $n=m^2$ settings tries only $m$ values of it, while $n$ random settings try $n$ distinct values with probability $1$.
2. If a fraction $q$ of the search region gives near-optimal results, $n$ random settings find at least one such setting with probability $1-(1-q)^n$.

:::

::: {.proof}

1. The grid points share $m$ values in each coordinate. Random coordinates drawn from a continuous distribution are distinct with probability $1$.
2. Each setting misses the good region with probability $1-q$, independently, so all $n$ miss it with probability $(1-q)^n$.

:::

::: {#fig-training-diagnostics-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[faint] (0.0,0) rectangle (3.0,3);
\node[dot] at (0.500,0.500) {};
\draw[hl] (0.500,-0.15) -- (0.500,-0.45);
\node[dot] at (0.500,1.500) {};
\draw[hl] (0.500,-0.15) -- (0.500,-0.45);
\node[dot] at (0.500,2.500) {};
\draw[hl] (0.500,-0.15) -- (0.500,-0.45);
\node[dot] at (1.500,0.500) {};
\draw[hl] (1.500,-0.15) -- (1.500,-0.45);
\node[dot] at (1.500,1.500) {};
\draw[hl] (1.500,-0.15) -- (1.500,-0.45);
\node[dot] at (1.500,2.500) {};
\draw[hl] (1.500,-0.15) -- (1.500,-0.45);
\node[dot] at (2.500,0.500) {};
\draw[hl] (2.500,-0.15) -- (2.500,-0.45);
\node[dot] at (2.500,1.500) {};
\draw[hl] (2.500,-0.15) -- (2.500,-0.45);
\node[dot] at (2.500,2.500) {};
\draw[hl] (2.500,-0.15) -- (2.500,-0.45);
\node[lab] at (1.5,3.35) {grid};
\node[lab,tick,anchor=north] at (1.5,-0.5) {important parameter};
\draw[faint] (4.0,0) rectangle (7.0,3);
\node[dot] at (6.415,2.424) {};
\draw[hl] (6.415,-0.15) -- (6.415,-0.45);
\node[dot] at (5.546,0.857) {};
\draw[hl] (5.546,-0.15) -- (5.546,-0.45);
\node[dot] at (4.162,1.150) {};
\draw[hl] (4.162,-0.15) -- (4.162,-0.45);
\node[dot] at (5.225,0.136) {};
\draw[hl] (5.225,-0.15) -- (5.225,-0.45);
\node[dot] at (4.146,2.998) {};
\draw[hl] (4.146,-0.15) -- (4.146,-0.45);
\node[dot] at (5.957,0.704) {};
\draw[hl] (5.957,-0.15) -- (5.957,-0.45);
\node[dot] at (5.305,2.923) {};
\draw[hl] (5.305,-0.15) -- (5.305,-0.45);
\node[dot] at (6.693,2.533) {};
\draw[hl] (6.693,-0.15) -- (6.693,-0.45);
\node[dot] at (5.177,1.479) {};
\draw[hl] (5.177,-0.15) -- (5.177,-0.45);
\node[lab] at (5.5,3.35) {random};
\node[lab,tick,anchor=north] at (5.5,-0.5) {important parameter};
\end{tikzpicture}
\end{center}
```

Nine settings of two hyperparameters, by grid and by random search. If only the horizontal one matters, the grid tries three of its values (ticks below each square), the random search nine.

:::

For $q=0.05$, $20$ random settings succeed with probability $0.64$ and $60$ settings with probability $0.95$. Best values at the edge of the search range mean the range should be extended. A single validation split is usually enough for networks, since cross validation (@def-cross-validation) multiplies an already large training cost.

::: {#def-model-ensemble .definition name="Model ensemble"}

An *ensemble* of models $f_1,\dots,f_M$ predicts with the average $\bar f=\frac1M\sum_mf_m$ of their outputs (scores or probabilities). The members can be independently initialized copies of one model, the best few settings of a hyperparameter search, or snapshots of one training run (checkpoints from different epochs).

:::

::: {#prp-ensemble-squared-error .proposition name="Averaging does not increase squared error"}

For a target $y$ and predictions $f_1,\dots,f_M\in\mathbb{R}$, with $\bar f$ their mean,

$$
(\bar f-y)^2=\frac1M\sum_{m}(f_m-y)^2-\frac1M\sum_m(f_m-\bar f)^2\ \le\ \frac1M\sum_m(f_m-y)^2 .
$$

:::

::: {.proof}

1. Write $f_m-y=(f_m-\bar f)+(\bar f-y)$ and square: $(f_m-y)^2=(f_m-\bar f)^2+2(f_m-\bar f)(\bar f-y)+(\bar f-y)^2$.
2. Averaging over $m$, the middle term vanishes because $\frac1M\sum_m(f_m-\bar f)=0$, so $\frac1M\sum_m(f_m-y)^2=\frac1M\sum_m(f_m-\bar f)^2+(\bar f-y)^2$.
3. Rearranging gives the identity; the subtracted term is non-negative.

:::

The ensemble gains most when its members disagree (the subtracted term is their spread), which is why independently trained networks help more than nearby checkpoints of one run. Ensembles reliably add a few per cent of accuracy, at $M$ times the cost at test time. A cheap variant keeps an exponentially decaying average of the weights during training and evaluates with it.
