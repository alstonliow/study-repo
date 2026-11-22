---
title: "Generative Adversarial Networks"
sources: [cs231n-15]
requires: [ai/deep-unsupervised-learning/autoregressive-image-models]
aliases: [ai/unsupervised-learning/generative-adversarial-networks]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-21 from Stanford CS231n course notes (Generative modeling: generative adversarial networks, the minimax objective, training, evaluation by inception score and nearest neighbours, mode collapse, DCGAN, CycleGAN, StyleGAN), in our own wording; the optimal-discriminator theorem and the Jensen–Shannon corollary are proved in our own steps; the loss derivatives were checked in Python. -->

Autoregressive models and VAEs (@sec-ai-deep-unsupervised-learning-variational-autoencoders) write down a density. A *generative adversarial network* (GAN) gives up the density and learns only to sample: a *generator* turns random noise into data, and a *discriminator* is trained at the same time to tell its outputs from real data.

::: {#def-gan .definition name="Generative adversarial network"}

Let $p_{\text{data}}$ be the data distribution on $\mathbb{R}^D$ and $p_z$ a simple noise distribution on $\mathbb{R}^k$ (say $\mathcal N(\mathbf 0,I)$). A *GAN* has a *generator* $G_\theta:\mathbb{R}^k\to\mathbb{R}^D$ and a *discriminator* $D_\phi:\mathbb{R}^D\to(0,1)$, the probability that its input is real. They play the minimax game

$$
\min_\theta\max_\phi\ V(\theta,\phi),\qquad V=\mathbb E_{\mathbf{x}\sim p_{\text{data}}}\bigl[\log D_\phi(\mathbf{x})\bigr]+\mathbb E_{\mathbf{z}\sim p_z}\bigl[\log\bigl(1-D_\phi(G_\theta(\mathbf{z}))\bigr)\bigr].
$$

Write $p_g$ for the distribution of $G_\theta(\mathbf{z})$. To sample, draw $\mathbf{z}\sim p_z$ and output $G_\theta(\mathbf{z})$.

:::

The discriminator maximizes $V$, the log-likelihood of a binary classifier with labels real $=1$ and generated $=0$ (@def-logistic-regression); the generator minimizes it, that is, tries to make the discriminator wrong on its samples.

::: {#thm-gan-optimal-discriminator .theorem name="The optimal discriminator"}

Suppose $p_{\text{data}}$ and $p_g$ have densities. For fixed $G$, the discriminator maximizing $V$ is

$$
D^*(\mathbf{x})=\frac{p_{\text{data}}(\mathbf{x})}{p_{\text{data}}(\mathbf{x})+p_g(\mathbf{x})},
$$

and then $V=2\operatorname{JS}(p_{\text{data}}\,\|\,p_g)-\log4$, where $\operatorname{JS}(p\,\|\,q)=\tfrac12D(p\,\|\,m)+\tfrac12D(q\,\|\,m)$ with $m=\tfrac12(p+q)$ is the *Jensen–Shannon divergence* and $D$ the relative entropy (@def-relative-entropy).

:::

::: {.proof}

1. Changing variables in the second expectation, $V=\int\bigl(p_{\text{data}}(\mathbf{x})\log D(\mathbf{x})+p_g(\mathbf{x})\log(1-D(\mathbf{x}))\bigr)\,d\mathbf{x}$.
2. For $a,b\ge0$ not both $0$, the function $y\mapsto a\log y+b\log(1-y)$ on $(0,1)$ has derivative $a/y-b/(1-y)$, which is zero at $y=a/(a+b)$; it is concave, so this is its maximum. Maximizing the integrand pointwise gives $D^*$.
3. Substituting, with $m=\frac12(p_{\text{data}}+p_g)$: $D^*=p_{\text{data}}/(2m)$ and $1-D^*=p_g/(2m)$, so $V=\int p_{\text{data}}\log\frac{p_{\text{data}}}{m}+\int p_g\log\frac{p_g}{m}-2\log2$.
4. The two integrals are $D(p_{\text{data}}\|m)$ and $D(p_g\|m)$, which sum to $2\operatorname{JS}$; and $2\log2=\log4$.

:::

::: {#cor-gan-global-optimum .corollary name="The generator's optimum"}

With an optimal discriminator, the generator's objective $2\operatorname{JS}(p_{\text{data}}\|p_g)-\log4$ is minimized exactly when $p_g=p_{\text{data}}$, where $D^*\equiv\frac12$ and $V=-\log4$.

:::

::: {.proof}

1. The relative entropy is non-negative and zero only for equal distributions (@thm-gibbs-inequality), so $\operatorname{JS}\ge0$, with equality iff $p_{\text{data}}=m=p_g$.
2. Then $D^*=p_{\text{data}}/(2p_{\text{data}})=\frac12$.

:::

The theorem idealizes: the networks have limited capacity, and the game is played by alternating gradient steps, not exact maximization, so convergence is not guaranteed.

::: {#def-gan-training .definition name="Alternating training and the non-saturating loss"}

GAN training alternates, for each minibatch, a gradient *ascent* step on $V$ in $\phi$ with real examples $\mathbf{x}_i$ and fresh noise $\mathbf{z}_i$, and a step for $G$. In the *non-saturating* form the generator, instead of minimizing $\mathbb E\log(1-D(G(\mathbf{z})))$, maximizes

$$
\mathbb E_{\mathbf{z}\sim p_z}\bigl[\log D_\phi(G_\theta(\mathbf{z}))\bigr].
$$

:::

```{=latex}
\begin{algorithm}
\caption{GAN training}
\begin{algorithmic}
\INPUT data, noise distribution $p_z$, networks $G_\theta$, $D_\phi$, number $k$ of discriminator steps
\OUTPUT trained generator $G_\theta$
\REPEAT
    \FOR{$k$ steps}
        \STATE draw real $\mathbf{x}_{1..m}$ and noise $\mathbf{z}_{1..m}$
        \STATE ascend $\frac1m\sum_i\bigl[\log D_\phi(\mathbf{x}_i)+\log(1-D_\phi(G_\theta(\mathbf{z}_i)))\bigr]$ in $\phi$
    \ENDFOR
    \STATE draw noise $\mathbf{z}_{1..m}$
    \STATE ascend $\frac1m\sum_i\log D_\phi(G_\theta(\mathbf{z}_i))$ in $\theta$ \COMMENT{non-saturating generator loss}
\UNTIL{the samples are good enough}
\end{algorithmic}
\end{algorithm}
```

::: {#prp-gan-non-saturating .proposition name="Why the non-saturating loss"}

Let $D=\sigma(s)$ for the discriminator's logit $s$ on a generated sample. Then

$$
\frac{\partial}{\partial s}\log(1-\sigma(s))=-\sigma(s),\qquad \frac{\partial}{\partial s}\log\sigma(s)=1-\sigma(s).
$$

Early in training, when the discriminator rejects the samples ($\sigma(s)\approx0$), the original generator loss has gradient near $0$ in $s$, while the non-saturating one has gradient near $1$.

:::

::: {.proof}

1. $\log(1-\sigma(s))=\log\sigma(-s)$, and $\frac{d}{ds}\log\sigma(s)=\sigma'(s)/\sigma(s)=1-\sigma(s)$ (@prp-sigmoid-saturation).
2. So $\frac{d}{ds}\log\sigma(-s)=-(1-\sigma(-s))=-\sigma(s)$.
3. At $\sigma(s)\approx0$ the first derivative is about $0$ and the second about $1$.

:::

::: {#fig-generative-adversarial-networks-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[->] (0,0) -- (3.24,0) node[lab,anchor=west] {$D(G(\mathbf z))$};
\draw[->] (0,-2.5) -- (0,2.6) node[lab,anchor=south] {generator loss};
\draw[faint] (0.015,-0.003) -- (0.030,-0.005) -- (0.044,-0.007) -- (0.059,-0.010) -- (0.074,-0.012) -- (0.089,-0.015) -- (0.103,-0.018) -- (0.118,-0.020) -- (0.133,-0.023) -- (0.147,-0.025) -- (0.162,-0.028) -- (0.177,-0.030) -- (0.191,-0.033) -- (0.206,-0.036) -- (0.221,-0.038) -- (0.235,-0.041) -- (0.250,-0.044) -- (0.265,-0.046) -- (0.280,-0.049) -- (0.294,-0.052) -- (0.309,-0.054) -- (0.324,-0.057) -- (0.338,-0.060) -- (0.353,-0.063) -- (0.368,-0.065) -- (0.383,-0.068) -- (0.397,-0.071) -- (0.412,-0.074) -- (0.427,-0.077) -- (0.441,-0.080) -- (0.456,-0.082) -- (0.471,-0.085) -- (0.485,-0.088) -- (0.500,-0.091) -- (0.515,-0.094) -- (0.529,-0.097) -- (0.544,-0.100) -- (0.559,-0.103) -- (0.574,-0.106) -- (0.588,-0.109) -- (0.603,-0.112) -- (0.618,-0.115) -- (0.632,-0.118) -- (0.647,-0.121) -- (0.662,-0.125) -- (0.676,-0.128) -- (0.691,-0.131) -- (0.706,-0.134) -- (0.721,-0.137) -- (0.735,-0.141) -- (0.750,-0.144) -- (0.765,-0.147) -- (0.779,-0.150) -- (0.794,-0.154) -- (0.809,-0.157) -- (0.824,-0.160) -- (0.838,-0.164) -- (0.853,-0.167) -- (0.868,-0.171) -- (0.882,-0.174) -- (0.897,-0.178) -- (0.912,-0.181) -- (0.926,-0.185) -- (0.941,-0.188) -- (0.956,-0.192) -- (0.971,-0.195) -- (0.985,-0.199) -- (1.000,-0.203) -- (1.015,-0.206) -- (1.029,-0.210) -- (1.044,-0.214) -- (1.059,-0.218) -- (1.073,-0.221) -- (1.088,-0.225) -- (1.103,-0.229) -- (1.117,-0.233) -- (1.132,-0.237) -- (1.147,-0.241) -- (1.162,-0.245) -- (1.176,-0.249) -- (1.191,-0.253) -- (1.206,-0.257) -- (1.220,-0.261) -- (1.235,-0.265) -- (1.250,-0.269) -- (1.264,-0.274) -- (1.279,-0.278) -- (1.294,-0.282) -- (1.309,-0.287) -- (1.323,-0.291) -- (1.338,-0.295) -- (1.353,-0.300) -- (1.367,-0.304) -- (1.382,-0.309) -- (1.397,-0.313) -- (1.411,-0.318) -- (1.426,-0.323) -- (1.441,-0.327) -- (1.456,-0.332) -- (1.470,-0.337) -- (1.485,-0.342) -- (1.500,-0.346) -- (1.514,-0.351) -- (1.529,-0.356) -- (1.544,-0.361) -- (1.558,-0.366) -- (1.573,-0.372) -- (1.588,-0.377) -- (1.603,-0.382) -- (1.617,-0.387) -- (1.632,-0.393) -- (1.647,-0.398) -- (1.661,-0.403) -- (1.676,-0.409) -- (1.691,-0.415) -- (1.706,-0.420) -- (1.720,-0.426) -- (1.735,-0.432) -- (1.750,-0.438) -- (1.764,-0.443) -- (1.779,-0.449) -- (1.794,-0.456) -- (1.808,-0.462) -- (1.823,-0.468) -- (1.838,-0.474) -- (1.852,-0.481) -- (1.867,-0.487) -- (1.882,-0.493) -- (1.897,-0.500) -- (1.911,-0.507) -- (1.926,-0.514) -- (1.941,-0.521) -- (1.955,-0.527) -- (1.970,-0.535) -- (1.985,-0.542) -- (1.999,-0.549) -- (2.014,-0.556) -- (2.029,-0.564) -- (2.044,-0.572) -- (2.058,-0.579) -- (2.073,-0.587) -- (2.088,-0.595) -- (2.102,-0.603) -- (2.117,-0.612) -- (2.132,-0.620) -- (2.147,-0.629) -- (2.161,-0.637) -- (2.176,-0.646) -- (2.191,-0.655) -- (2.205,-0.664) -- (2.220,-0.674) -- (2.235,-0.683) -- (2.249,-0.693) -- (2.264,-0.703) -- (2.279,-0.713) -- (2.293,-0.723) -- (2.308,-0.734) -- (2.323,-0.744) -- (2.338,-0.755) -- (2.352,-0.766) -- (2.367,-0.778) -- (2.382,-0.790) -- (2.396,-0.802) -- (2.411,-0.814) -- (2.426,-0.827) -- (2.441,-0.840) -- (2.455,-0.853) -- (2.470,-0.867) -- (2.485,-0.881) -- (2.499,-0.895) -- (2.514,-0.910) -- (2.529,-0.925) -- (2.543,-0.941) -- (2.558,-0.958) -- (2.573,-0.975) -- (2.587,-0.992) -- (2.602,-1.010) -- (2.617,-1.029) -- (2.632,-1.049) -- (2.646,-1.069) -- (2.661,-1.090) -- (2.676,-1.112) -- (2.690,-1.136) -- (2.705,-1.160) -- (2.720,-1.185) -- (2.734,-1.212) -- (2.749,-1.241) -- (2.764,-1.271) -- (2.779,-1.303) -- (2.793,-1.338) -- (2.808,-1.374) -- (2.823,-1.414) -- (2.837,-1.458) -- (2.852,-1.505) -- (2.867,-1.557) -- (2.881,-1.616) -- (2.896,-1.682) -- (2.911,-1.758) -- (2.926,-1.848) -- (2.940,-1.959) -- (2.955,-2.100);
\draw[hl] (0.030,2.308) -- (0.044,2.107) -- (0.059,1.964) -- (0.074,1.853) -- (0.089,1.762) -- (0.103,1.685) -- (0.118,1.618) -- (0.133,1.560) -- (0.147,1.507) -- (0.162,1.459) -- (0.177,1.416) -- (0.191,1.376) -- (0.206,1.339) -- (0.221,1.305) -- (0.235,1.272) -- (0.250,1.242) -- (0.265,1.214) -- (0.280,1.187) -- (0.294,1.161) -- (0.309,1.137) -- (0.324,1.113) -- (0.338,1.091) -- (0.353,1.070) -- (0.368,1.049) -- (0.383,1.030) -- (0.397,1.011) -- (0.412,0.993) -- (0.427,0.975) -- (0.441,0.958) -- (0.456,0.942) -- (0.471,0.926) -- (0.485,0.911) -- (0.500,0.896) -- (0.515,0.881) -- (0.529,0.867) -- (0.544,0.854) -- (0.559,0.840) -- (0.574,0.827) -- (0.588,0.815) -- (0.603,0.802) -- (0.618,0.790) -- (0.632,0.778) -- (0.647,0.767) -- (0.662,0.756) -- (0.676,0.745) -- (0.691,0.734) -- (0.706,0.723) -- (0.721,0.713) -- (0.735,0.703) -- (0.750,0.693) -- (0.765,0.683) -- (0.779,0.674) -- (0.794,0.665) -- (0.809,0.655) -- (0.824,0.646) -- (0.838,0.638) -- (0.853,0.629) -- (0.868,0.620) -- (0.882,0.612) -- (0.897,0.604) -- (0.912,0.596) -- (0.926,0.588) -- (0.941,0.580) -- (0.956,0.572) -- (0.971,0.564) -- (0.985,0.557) -- (1.000,0.549) -- (1.015,0.542) -- (1.029,0.535) -- (1.044,0.528) -- (1.059,0.521) -- (1.073,0.514) -- (1.088,0.507) -- (1.103,0.500) -- (1.117,0.494) -- (1.132,0.487) -- (1.147,0.481) -- (1.162,0.474) -- (1.176,0.468) -- (1.191,0.462) -- (1.206,0.456) -- (1.220,0.450) -- (1.235,0.444) -- (1.250,0.438) -- (1.264,0.432) -- (1.279,0.426) -- (1.294,0.420) -- (1.309,0.415) -- (1.323,0.409) -- (1.338,0.404) -- (1.353,0.398) -- (1.367,0.393) -- (1.382,0.388) -- (1.397,0.382) -- (1.411,0.377) -- (1.426,0.372) -- (1.441,0.367) -- (1.456,0.362) -- (1.470,0.357) -- (1.485,0.352) -- (1.500,0.347) -- (1.514,0.342) -- (1.529,0.337) -- (1.544,0.332) -- (1.558,0.327) -- (1.573,0.323) -- (1.588,0.318) -- (1.603,0.313) -- (1.617,0.309) -- (1.632,0.304) -- (1.647,0.300) -- (1.661,0.295) -- (1.676,0.291) -- (1.691,0.287) -- (1.706,0.282) -- (1.720,0.278) -- (1.735,0.274) -- (1.750,0.270) -- (1.764,0.265) -- (1.779,0.261) -- (1.794,0.257) -- (1.808,0.253) -- (1.823,0.249) -- (1.838,0.245) -- (1.852,0.241) -- (1.867,0.237) -- (1.882,0.233) -- (1.897,0.229) -- (1.911,0.225) -- (1.926,0.222) -- (1.941,0.218) -- (1.955,0.214) -- (1.970,0.210) -- (1.985,0.207) -- (1.999,0.203) -- (2.014,0.199) -- (2.029,0.196) -- (2.044,0.192) -- (2.058,0.188) -- (2.073,0.185) -- (2.088,0.181) -- (2.102,0.178) -- (2.117,0.174) -- (2.132,0.171) -- (2.147,0.167) -- (2.161,0.164) -- (2.176,0.161) -- (2.191,0.157) -- (2.205,0.154) -- (2.220,0.151) -- (2.235,0.147) -- (2.249,0.144) -- (2.264,0.141) -- (2.279,0.137) -- (2.293,0.134) -- (2.308,0.131) -- (2.323,0.128) -- (2.338,0.125) -- (2.352,0.122) -- (2.367,0.118) -- (2.382,0.115) -- (2.396,0.112) -- (2.411,0.109) -- (2.426,0.106) -- (2.441,0.103) -- (2.455,0.100) -- (2.470,0.097) -- (2.485,0.094) -- (2.499,0.091) -- (2.514,0.088) -- (2.529,0.085) -- (2.543,0.083) -- (2.558,0.080) -- (2.573,0.077) -- (2.587,0.074) -- (2.602,0.071) -- (2.617,0.068) -- (2.632,0.066) -- (2.646,0.063) -- (2.661,0.060) -- (2.676,0.057) -- (2.690,0.054) -- (2.705,0.052) -- (2.720,0.049) -- (2.734,0.046) -- (2.749,0.044) -- (2.764,0.041) -- (2.779,0.038) -- (2.793,0.036) -- (2.808,0.033) -- (2.823,0.030) -- (2.837,0.028) -- (2.852,0.025) -- (2.867,0.023) -- (2.881,0.020) -- (2.896,0.018) -- (2.911,0.015) -- (2.926,0.013) -- (2.940,0.010) -- (2.955,0.008);
\node[lab,anchor=west] at (1.65,-0.65) {$\log(1-D)$, minimized};
\node[lab,anchor=west] at (0.36,1.8) {$-\log D$, non-saturating};
\draw[tick] (3.0,0) -- (3.0,-0.08) node[lab,anchor=north] {$1$};
\end{tikzpicture}
\end{center}
```

The two generator losses as functions of the discriminator output on a generated sample. When the discriminator rejects the samples ($D$ near $0$, early in training) the original loss $\log(1-D)$ is flat, while $-\log D$ is steep (@prp-gan-non-saturating).

:::

Both losses push $D(G(\mathbf{z}))$ in the same direction and have the same fixed points, but only the non-saturating one gives the generator a usable signal when it is still bad.

::: {#rmk-gan-challenges .remark name="Difficulties and evaluation" editor="No figure of a GAN training run: it needs two trained networks and a dataset; the figure after the non-saturating proposition shows the part of the algorithm that can be drawn exactly."}

1. *Instability*: the two players can oscillate instead of converging; architecture choices such as those of DCGAN (strided and transposed convolutions instead of pooling, batch normalization, ReLU in the generator and leaky ReLU in the discriminator) made training reliable.
2. *Mode collapse*: the generator may cover only a few modes of $p_{\text{data}}$, producing a few kinds of output that fool the current discriminator.
3. *Evaluation*: with no likelihood, samples are judged indirectly. The *inception score* passes samples through a pretrained classifier and rewards confident predictions per sample and diverse predictions overall; showing each sample's *nearest neighbours* in the training set checks that the generator does not just copy training images; human studies (such as HYPE) measure how often people mistake samples for real images.
4. Later variants learn image-to-image maps without paired data (CycleGAN, with a cycle-consistency loss) or control the style of each resolution level (StyleGAN).

:::
