---
title: "Generalization, Overfitting and Tuning"
sources: [cs188-20, cs188-21]
requires: [ai/machine-learning/supervised-learning]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 20 (training and testing, empirical risk minimisation, overfitting, generalisation, tuning on held-out data, features, errors, baselines, confidences) and the start of Lecture 21 (baselines and confidences), in our own wording; the polynomial example is our own, computed with NumPy (seed 2). -->

Minimising the training loss (@def-training-loss) is a means, not the goal: the goal is to predict well on inputs not seen during training. This note separates the two and describes how to measure and control the gap.

::: {#def-test-error .definition name="Training, held-out and test data; generalisation"}

Assume examples are drawn independently from a fixed distribution $\mathcal P$ over $\mathcal X\times\mathcal Y$. The *risk* (expected loss) of a predictor $f$ is $\mathbb E_{(x,y)\sim\mathcal P}\,\text{Loss}(x,y,f)$; minimising the training loss instead is *empirical risk minimisation*. A predictor *generalises* if its risk is close to its training loss.

Available labelled data is split into three disjoint parts: *training data*, used to fit the parameters; *held-out* (validation) data, used to choose *hyperparameters* (settings of the learning algorithm itself, such as a smoothing strength or a model size); and *test data*, used once, at the end, to estimate the risk of the final predictor.

:::

::: {#fig-generalization-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\path[bar] (0,0) rectangle (4.2,0.6);
\path[hl cell] (4.2,0) rectangle (5.8,0.6);
\draw[cell frame] (5.8,0) rectangle (7.6,0.6);
\node[tick, text=white] at (2.1,0.3) {training: fit parameters};
\node[tick] at (5.0,0.3) {validation};
\node[tick] at (6.7,0.3) {test};
\node[tick, below] at (5.0,0) {tune};
\node[tick, below] at (6.7,0) {report once};
\end{tikzpicture}
\end{center}
```

Splitting the data: parameters are fitted on the training set, hyperparameters are tuned on the validation set, and the test set is used once to estimate the test error

:::

The test data estimates the risk only if nothing about the predictor was chosen by looking at it; a test set used to make choices becomes, in effect, training data, and its error underestimates the risk. The same holds for the held-out data after much tuning, which is why a separate test set is kept.

::: {#def-overfitting .definition name="Overfitting, underfitting"}

A predictor *overfits* when it fits the training data much better than new data, typically because its hypothesis class (@def-hypothesis-class) is rich enough to fit the noise and accidents of a small sample. It *underfits* when it fits even the training data poorly, because the hypothesis class cannot express the regularities present.

:::

::: {#fig-generalization-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (6.2,0) node[lab, right] {model complexity};
\draw[->] (0,0) -- (0,2.8) node[lab, above] {error};
\draw[emph, domain=0.2:5.8, samples=80, smooth, variable=\x] plot ({\x}, {2.2*exp(-0.5*\x)+0.15});
\draw[hl, domain=0.2:5.8, samples=80, smooth, variable=\x] plot ({\x}, {2.0*exp(-0.55*\x)+0.06*(\x-0.5)^2+0.45});
\node[tick] at (5.2,0.35) {training};
\node[tick, text=accent] at (5.2,1.95) {test};
\node[tick] at (1.0,2.6) {underfit};
\node[tick] at (4.6,2.6) {overfit};
\end{tikzpicture}
\end{center}
```

Training error keeps falling as the model grows, but test error is U-shaped: beyond some point the extra capacity fits noise and the model overfits

:::

::: {#exm-overfitting-polynomials .example name="Polynomials of growing degree"}

Ten training inputs equally spaced in $[0,1]$ have outputs $\sin(2\pi x)$ plus Gaussian noise of standard deviation $0.3$ (so no predictor can have squared error below $0.09$ on average). Fitting polynomials by least squares and measuring the average squared error on $10\,000$ fresh examples, one run gives

| degree | training error | test error |
|---|---|---|
| $1$ | $0.22$ | $0.33$ |
| $3$ | $0.086$ | $0.12$ |
| $9$ | $0.000$ | $0.84$ |

A line underfits. Degree $9$ passes through all ten points (zero training error) but oscillates between them and does worst on new data. Degree $3$, which is never best on the training data, is best on new data.

:::

::: {#fig-generalization-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0.0,0) rectangle (3.2,2.4);
\draw[faint, domain=0.0:3.2, samples=60, smooth, variable=\x] plot ({\x}, {1.2+0.8*sin(deg(2*pi*(\x-0.0)/3.2))});
\draw[hl] (0.000,1.608) -- (0.027,1.600) -- (0.054,1.593) -- (0.081,1.586) -- (0.108,1.578) -- (0.134,1.571) -- (0.161,1.564) -- (0.188,1.557) -- (0.215,1.549) -- (0.242,1.542) -- (0.269,1.535) -- (0.296,1.527) -- (0.323,1.520) -- (0.350,1.513) -- (0.376,1.505) -- (0.403,1.498) -- (0.430,1.491) -- (0.457,1.484) -- (0.484,1.476) -- (0.511,1.469) -- (0.538,1.462) -- (0.565,1.454) -- (0.592,1.447) -- (0.618,1.440) -- (0.645,1.432) -- (0.672,1.425) -- (0.699,1.418) -- (0.726,1.410) -- (0.753,1.403) -- (0.780,1.396) -- (0.807,1.389) -- (0.834,1.381) -- (0.861,1.374) -- (0.887,1.367) -- (0.914,1.359) -- (0.941,1.352) -- (0.968,1.345) -- (0.995,1.337) -- (1.022,1.330) -- (1.049,1.323) -- (1.076,1.315) -- (1.103,1.308) -- (1.129,1.301) -- (1.156,1.294) -- (1.183,1.286) -- (1.210,1.279) -- (1.237,1.272) -- (1.264,1.264) -- (1.291,1.257) -- (1.318,1.250) -- (1.345,1.242) -- (1.371,1.235) -- (1.398,1.228) -- (1.425,1.220) -- (1.452,1.213) -- (1.479,1.206) -- (1.506,1.199) -- (1.533,1.191) -- (1.560,1.184) -- (1.587,1.177) -- (1.613,1.169) -- (1.640,1.162) -- (1.667,1.155) -- (1.694,1.147) -- (1.721,1.140) -- (1.748,1.133) -- (1.775,1.125) -- (1.802,1.118) -- (1.829,1.111) -- (1.855,1.104) -- (1.882,1.096) -- (1.909,1.089) -- (1.936,1.082) -- (1.963,1.074) -- (1.990,1.067) -- (2.017,1.060) -- (2.044,1.052) -- (2.071,1.045) -- (2.097,1.038) -- (2.124,1.030) -- (2.151,1.023) -- (2.178,1.016) -- (2.205,1.009) -- (2.232,1.001) -- (2.259,0.994) -- (2.286,0.987) -- (2.313,0.979) -- (2.339,0.972) -- (2.366,0.965) -- (2.393,0.957) -- (2.420,0.950) -- (2.447,0.943) -- (2.474,0.935) -- (2.501,0.928) -- (2.528,0.921) -- (2.555,0.914) -- (2.582,0.906) -- (2.608,0.899) -- (2.635,0.892) -- (2.662,0.884) -- (2.689,0.877) -- (2.716,0.870) -- (2.743,0.862) -- (2.770,0.855) -- (2.797,0.848) -- (2.824,0.840) -- (2.850,0.833) -- (2.877,0.826) -- (2.904,0.819) -- (2.931,0.811) -- (2.958,0.804) -- (2.985,0.797) -- (3.012,0.789) -- (3.039,0.782) -- (3.066,0.775) -- (3.092,0.767) -- (3.119,0.760) -- (3.146,0.753) -- (3.173,0.746) -- (3.200,0.738);
\node[dot] at (0.00,1.69) {};
\node[dot] at (0.36,1.10) {};
\node[dot] at (0.71,2.09) {};
\node[dot] at (1.07,1.76) {};
\node[dot] at (1.42,1.36) {};
\node[dot] at (1.78,0.87) {};
\node[dot] at (2.13,0.02) {};
\node[dot] at (2.49,0.36) {};
\node[dot] at (2.84,0.48) {};
\node[dot] at (3.20,2.00) {};
\node[tick, below] at (1.6,0) {degree $1$};
\draw[faint] (4.0,0) rectangle (7.2,2.4);
\draw[faint, domain=4.0:7.2, samples=60, smooth, variable=\x] plot ({\x}, {1.2+0.8*sin(deg(2*pi*(\x-4.0)/3.2))});
\draw[hl] (4.000,1.301) -- (4.027,1.366) -- (4.054,1.427) -- (4.081,1.485) -- (4.108,1.538) -- (4.134,1.588) -- (4.161,1.635) -- (4.188,1.678) -- (4.215,1.717) -- (4.242,1.754) -- (4.269,1.787) -- (4.296,1.817) -- (4.323,1.843) -- (4.350,1.867) -- (4.376,1.888) -- (4.403,1.906) -- (4.430,1.921) -- (4.457,1.933) -- (4.484,1.943) -- (4.511,1.950) -- (4.538,1.955) -- (4.565,1.957) -- (4.592,1.957) -- (4.618,1.954) -- (4.645,1.949) -- (4.672,1.942) -- (4.699,1.933) -- (4.726,1.922) -- (4.753,1.909) -- (4.780,1.894) -- (4.807,1.877) -- (4.834,1.859) -- (4.861,1.839) -- (4.887,1.817) -- (4.914,1.794) -- (4.941,1.769) -- (4.968,1.743) -- (4.995,1.715) -- (5.022,1.687) -- (5.049,1.657) -- (5.076,1.626) -- (5.103,1.594) -- (5.129,1.561) -- (5.156,1.527) -- (5.183,1.493) -- (5.210,1.457) -- (5.237,1.421) -- (5.264,1.385) -- (5.291,1.348) -- (5.318,1.310) -- (5.345,1.272) -- (5.371,1.234) -- (5.398,1.195) -- (5.425,1.157) -- (5.452,1.118) -- (5.479,1.079) -- (5.506,1.040) -- (5.533,1.002) -- (5.560,0.963) -- (5.587,0.925) -- (5.613,0.887) -- (5.640,0.850) -- (5.667,0.813) -- (5.694,0.776) -- (5.721,0.741) -- (5.748,0.705) -- (5.775,0.671) -- (5.802,0.638) -- (5.829,0.605) -- (5.855,0.573) -- (5.882,0.543) -- (5.909,0.513) -- (5.936,0.485) -- (5.963,0.458) -- (5.990,0.433) -- (6.017,0.408) -- (6.044,0.386) -- (6.071,0.364) -- (6.097,0.345) -- (6.124,0.327) -- (6.151,0.311) -- (6.178,0.296) -- (6.205,0.284) -- (6.232,0.274) -- (6.259,0.265) -- (6.286,0.259) -- (6.313,0.255) -- (6.339,0.253) -- (6.366,0.254) -- (6.393,0.257) -- (6.420,0.262) -- (6.447,0.270) -- (6.474,0.281) -- (6.501,0.294) -- (6.528,0.310) -- (6.555,0.329) -- (6.582,0.351) -- (6.608,0.376) -- (6.635,0.404) -- (6.662,0.435) -- (6.689,0.469) -- (6.716,0.506) -- (6.743,0.547) -- (6.770,0.591) -- (6.797,0.639) -- (6.824,0.690) -- (6.850,0.745) -- (6.877,0.804) -- (6.904,0.866) -- (6.931,0.932) -- (6.958,1.002) -- (6.985,1.076) -- (7.012,1.155) -- (7.039,1.237) -- (7.066,1.323) -- (7.092,1.414) -- (7.119,1.509) -- (7.146,1.609) -- (7.173,1.713) -- (7.200,1.821);
\node[dot] at (4.00,1.69) {};
\node[dot] at (4.36,1.10) {};
\node[dot] at (4.71,2.09) {};
\node[dot] at (5.07,1.76) {};
\node[dot] at (5.42,1.36) {};
\node[dot] at (5.78,0.87) {};
\node[dot] at (6.13,0.02) {};
\node[dot] at (6.49,0.36) {};
\node[dot] at (6.84,0.48) {};
\node[dot] at (7.20,2.00) {};
\node[tick, below] at (5.6,0) {degree $3$};
\draw[faint] (8.0,0) rectangle (11.2,2.4);
\draw[faint, domain=8.0:11.2, samples=60, smooth, variable=\x] plot ({\x}, {1.2+0.8*sin(deg(2*pi*(\x-8.0)/3.2))});
\draw[hl] (8.000,1.690) -- (8.027,1.472) -- (8.054,1.282) -- (8.081,1.121) -- (8.108,0.993) -- (8.134,0.898) -- (8.161,0.834) -- (8.188,0.801) -- (8.215,0.796) -- (8.242,0.816) -- (8.269,0.858) -- (8.296,0.918) -- (8.323,0.994) -- (8.350,1.080) -- (8.376,1.175) -- (8.403,1.275) -- (8.430,1.377) -- (8.457,1.478) -- (8.484,1.576) -- (8.511,1.670) -- (8.538,1.756) -- (8.565,1.835) -- (8.592,1.904) -- (8.618,1.963) -- (8.645,2.012) -- (8.672,2.051) -- (8.699,2.079) -- (8.726,2.097) -- (8.753,2.105) -- (8.780,2.104) -- (8.807,2.094) -- (8.834,2.077) -- (8.861,2.054) -- (8.887,2.024) -- (8.914,1.991) -- (8.941,1.953) -- (8.968,1.913) -- (8.995,1.871) -- (9.022,1.828) -- (9.049,1.785) -- (9.076,1.743) -- (9.103,1.701) -- (9.129,1.662) -- (9.156,1.624) -- (9.183,1.589) -- (9.210,1.556) -- (9.237,1.526) -- (9.264,1.498) -- (9.291,1.472) -- (9.318,1.448) -- (9.345,1.425) -- (9.371,1.404) -- (9.398,1.383) -- (9.425,1.363) -- (9.452,1.342) -- (9.479,1.320) -- (9.506,1.296) -- (9.533,1.270) -- (9.560,1.242) -- (9.587,1.211) -- (9.613,1.176) -- (9.640,1.137) -- (9.667,1.094) -- (9.694,1.047) -- (9.721,0.996) -- (9.748,0.941) -- (9.775,0.881) -- (9.802,0.818) -- (9.829,0.752) -- (9.855,0.683) -- (9.882,0.612) -- (9.909,0.540) -- (9.936,0.468) -- (9.963,0.396) -- (9.990,0.326) -- (10.017,0.258) -- (10.044,0.194) -- (10.071,0.135) -- (10.097,0.082) -- (10.124,0.036) -- (10.151,-0.002) -- (10.178,-0.031) -- (10.205,-0.050) -- (10.232,-0.060) -- (10.259,-0.058) -- (10.286,-0.045) -- (10.313,-0.022) -- (10.339,0.012) -- (10.366,0.057) -- (10.393,0.110) -- (10.420,0.172) -- (10.447,0.241) -- (10.474,0.314) -- (10.501,0.391) -- (10.528,0.468) -- (10.555,0.543) -- (10.582,0.613) -- (10.608,0.676) -- (10.635,0.727) -- (10.662,0.765) -- (10.689,0.786) -- (10.716,0.788) -- (10.743,0.769) -- (10.770,0.725) -- (10.797,0.658) -- (10.824,0.566) -- (10.850,0.451) -- (10.877,0.315) -- (10.904,0.164) -- (10.931,0.004) -- (11.146,0.339) -- (11.173,1.020) -- (11.200,1.998);
\node[dot] at (8.00,1.69) {};
\node[dot] at (8.36,1.10) {};
\node[dot] at (8.71,2.09) {};
\node[dot] at (9.07,1.76) {};
\node[dot] at (9.42,1.36) {};
\node[dot] at (9.78,0.87) {};
\node[dot] at (10.13,0.02) {};
\node[dot] at (10.49,0.36) {};
\node[dot] at (10.84,0.48) {};
\node[dot] at (11.20,2.00) {};
\node[tick, below] at (9.6,0) {degree $9$};
\end{tikzpicture}
\end{center}
```

Least squares polynomials of degree $1$, $3$ and $9$ fitted to ten noisy samples of $\sin(2\pi x)$ (faint). Degree $1$ underfits; degree $9$ passes through every point and swings wildly between them

:::

Training error always decreases as the hypothesis class grows; the risk first decreases and then increases. Ways to control overfitting all limit how closely the training data is followed: fewer or simpler features, a smaller hypothesis class, smoothing of estimated probabilities (@def-laplace-smoothing), regularisation (penalising large parameters), stopping iterative training early, and more training data, which makes accidents rarer.

::: {#rmk-tuning .remark name="Tuning hyperparameters"}

To tune a hyperparameter, train one predictor per candidate value on the training data, measure each on the held-out data, and keep the value with the lowest held-out error; then, often, retrain on training and held-out data together with that value. With little data, *cross-validation* rotates which part is held out and averages the errors.

:::

::: {#rmk-baselines-confidence .remark name="Baselines and confidences"}

A test accuracy means little without a *baseline*: the simplest sensible predictor, such as always predicting the most frequent label, or a published simple method. If $90\%$ of emails are ham, a filter with $90\%$ accuracy has learnt nothing. Many classifiers also report a *confidence*, such as $P(y\mid x)$ from naive Bayes (@def-naive-bayes) or logistic regression (@def-logistic-regression). A classifier is *calibrated* if, among the predictions made with confidence about $p$, a fraction about $p$ is correct; naive Bayes tends to be overconfident, because it counts correlated features as independent evidence. When errors occur, inspecting them usually suggests better features, which help more than tuning.

:::
