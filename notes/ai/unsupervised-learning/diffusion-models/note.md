---
title: "Denoising Diffusion Models"
sources: [cs231na-3]
requires: [ai/unsupervised-learning/variational-autoencoders, ai/deep-learning/convolutional-layers]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS231n Assignment 3 (denoising diffusion probabilistic models: forward noising, noise and image prediction, U-Net, denoising loss, reverse sampling, classifier-free guidance), in our own wording; the two propositions are proved in our own steps; the noise schedule numbers were computed in Python. The link between the simple loss and the evidence lower bound is stated, not proved. This note also fills the diffusion-model chapter that the CS229 integration left to the deep learning courses. -->

A *diffusion model* generates data by learning to undo a fixed process that slowly turns data into noise. Training only asks a network to predict the noise added to a training image, a plain regression problem; sampling starts from pure noise and removes it step by step.

::: {#def-diffusion-forward-process .definition name="Forward (noising) process"}

Fix a number of steps $T$ and a *noise schedule* $0<\beta_1<\dots<\beta_T<1$; let $\alpha_t=1-\beta_t$ and $\bar\alpha_t=\prod_{s=1}^{t}\alpha_s$. Starting from a data point $\mathbf{x}_0\in\mathbb{R}^D$, the *forward process* is the Markov chain

$$
\mathbf{x}_t=\sqrt{\alpha_t}\,\mathbf{x}_{t-1}+\sqrt{\beta_t}\,\boldsymbol\varepsilon_t,\qquad \boldsymbol\varepsilon_t\sim\mathcal N(\mathbf 0,I)\ \text{independent},\qquad t=1,\dots,T,
$$

that is $q(\mathbf{x}_t\mid\mathbf{x}_{t-1})=\mathcal N(\sqrt{\alpha_t}\mathbf{x}_{t-1},\beta_tI)$.

:::

::: {#prp-diffusion-marginal .proposition name="Jumping to any step"}

For every $t$, $q(\mathbf{x}_t\mid\mathbf{x}_0)=\mathcal N\bigl(\sqrt{\bar\alpha_t}\,\mathbf{x}_0,\ (1-\bar\alpha_t)I\bigr)$; equivalently $\mathbf{x}_t=\sqrt{\bar\alpha_t}\,\mathbf{x}_0+\sqrt{1-\bar\alpha_t}\,\boldsymbol\varepsilon$ with $\boldsymbol\varepsilon\sim\mathcal N(\mathbf 0,I)$.

:::

::: {.proof}

1. Induction on $t$. For $t=1$ it is the definition, since $\bar\alpha_1=\alpha_1$ and $1-\alpha_1=\beta_1$.
2. Suppose $\mathbf{x}_{t-1}=\sqrt{\bar\alpha_{t-1}}\mathbf{x}_0+\sqrt{1-\bar\alpha_{t-1}}\,\boldsymbol\eta$ with $\boldsymbol\eta\sim\mathcal N(\mathbf 0,I)$ independent of $\boldsymbol\varepsilon_t$. Then $\mathbf{x}_t=\sqrt{\bar\alpha_t}\mathbf{x}_0+\sqrt{\alpha_t(1-\bar\alpha_{t-1})}\,\boldsymbol\eta+\sqrt{\beta_t}\,\boldsymbol\varepsilon_t$.
3. The last two terms are independent centred normals in each coordinate, so their sum is normal (@cor-sum-of-normals) with variance $\alpha_t-\bar\alpha_t+1-\alpha_t=1-\bar\alpha_t$.

:::

With the common linear schedule $\beta_t$ from $10^{-4}$ to $0.02$ over $T=1000$ steps, $\bar\alpha_{500}\approx0.079$ and $\bar\alpha_{1000}\approx4\times10^{-5}$: by the last step the signal coefficient $\sqrt{\bar\alpha_T}\approx0.006$, and $\mathbf{x}_T$ is essentially standard normal whatever $\mathbf{x}_0$ was.

::: {#prp-diffusion-posterior .proposition name="The forward process reversed, given the data point"}

For $t\ge2$, $q(\mathbf{x}_{t-1}\mid\mathbf{x}_t,\mathbf{x}_0)=\mathcal N(\tilde{\boldsymbol\mu}_t,\tilde\beta_tI)$ with

$$
\tilde{\boldsymbol\mu}_t=\frac{\sqrt{\bar\alpha_{t-1}}\,\beta_t}{1-\bar\alpha_t}\,\mathbf{x}_0+\frac{\sqrt{\alpha_t}\,(1-\bar\alpha_{t-1})}{1-\bar\alpha_t}\,\mathbf{x}_t,\qquad \tilde\beta_t=\frac{1-\bar\alpha_{t-1}}{1-\bar\alpha_t}\,\beta_t .
$$

If $\mathbf{x}_t=\sqrt{\bar\alpha_t}\mathbf{x}_0+\sqrt{1-\bar\alpha_t}\,\boldsymbol\varepsilon$, then $\tilde{\boldsymbol\mu}_t=\dfrac{1}{\sqrt{\alpha_t}}\Bigl(\mathbf{x}_t-\dfrac{\beta_t}{\sqrt{1-\bar\alpha_t}}\,\boldsymbol\varepsilon\Bigr)$.

:::

::: {.proof}

1. Coordinates are independent, so work with one coordinate and $x_0$ fixed. By @prp-diffusion-marginal and @def-diffusion-forward-process, $x_{t-1}=\sqrt{\bar\alpha_{t-1}}x_0+\sqrt{1-\bar\alpha_{t-1}}\,\eta$ and $x_t=\sqrt{\alpha_t}x_{t-1}+\sqrt{\beta_t}\,\varepsilon_t$, so $(x_{t-1},x_t)$ is jointly Gaussian.
2. Its moments: $\operatorname{Var}(x_{t-1})=1-\bar\alpha_{t-1}$, $\operatorname{Var}(x_t)=1-\bar\alpha_t$, and $\operatorname{Cov}(x_{t-1},x_t)=\sqrt{\alpha_t}(1-\bar\alpha_{t-1})$.
3. By @thm-jointly-gaussian-conditional, the conditional mean is $\sqrt{\bar\alpha_{t-1}}x_0+\frac{\sqrt{\alpha_t}(1-\bar\alpha_{t-1})}{1-\bar\alpha_t}\bigl(x_t-\sqrt{\bar\alpha_t}x_0\bigr)$. The coefficient of $x_0$ is $\sqrt{\bar\alpha_{t-1}}\bigl(1-\frac{\alpha_t(1-\bar\alpha_{t-1})}{1-\bar\alpha_t}\bigr)=\sqrt{\bar\alpha_{t-1}}\frac{1-\alpha_t}{1-\bar\alpha_t}$, which is the claim since $1-\alpha_t=\beta_t$.
4. The conditional variance is $(1-\bar\alpha_{t-1})-\frac{\alpha_t(1-\bar\alpha_{t-1})^2}{1-\bar\alpha_t}=\frac{(1-\bar\alpha_{t-1})(1-\alpha_t)}{1-\bar\alpha_t}=\tilde\beta_t$.
5. Substituting $x_0=(x_t-\sqrt{1-\bar\alpha_t}\,\varepsilon)/\sqrt{\bar\alpha_t}$ and simplifying with $\bar\alpha_t=\alpha_t\bar\alpha_{t-1}$ gives the second form of $\tilde\mu_t$.

:::

::: {#def-ddpm .definition name="Denoising diffusion probabilistic model"}

A *DDPM* learns a network $\boldsymbol\varepsilon_\theta(\mathbf{x}_t,t)$ that predicts the noise in $\mathbf{x}_t$. It is trained to minimize the *simple loss*

$$
L(\theta)=\mathbb E_{\mathbf{x}_0,\,t,\,\boldsymbol\varepsilon}\Bigl[\bigl\lVert\boldsymbol\varepsilon-\boldsymbol\varepsilon_\theta\bigl(\sqrt{\bar\alpha_t}\mathbf{x}_0+\sqrt{1-\bar\alpha_t}\,\boldsymbol\varepsilon,\ t\bigr)\bigr\rVert^2\Bigr],
$$

with $\mathbf{x}_0$ from the training data, $t$ uniform on $\{1,\dots,T\}$ and $\boldsymbol\varepsilon\sim\mathcal N(\mathbf 0,I)$. Its *reverse process* samples $\mathbf{x}_T\sim\mathcal N(\mathbf 0,I)$ and then, for $t=T,\dots,1$,

$$
\mathbf{x}_{t-1}=\frac{1}{\sqrt{\alpha_t}}\Bigl(\mathbf{x}_t-\frac{\beta_t}{\sqrt{1-\bar\alpha_t}}\,\boldsymbol\varepsilon_\theta(\mathbf{x}_t,t)\Bigr)+\sqrt{\tilde\beta_t}\,\mathbf{z},\qquad \mathbf{z}\sim\mathcal N(\mathbf 0,I),
$$

with $\mathbf{z}=\mathbf 0$ at the last step $t=1$.

:::

::: {#fig-diffusion-models-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[->] (5.7,0) -- (-0.4,0) node[lab,anchor=east] {$t$};
\draw[->] (0,-2.08) -- (0,2.24) node[lab,anchor=south] {$x_t$};
\draw[tick] (0.0,0) -- (0.0,-0.08) node[lab,anchor=north] {$0$};
\draw[tick] (2.75,0) -- (2.75,-0.08) node[lab,anchor=north] {$25$};
\draw[tick] (5.5,0) -- (5.5,-0.08) node[lab,anchor=north] {$50$};
\draw[faint,dashed] (0,0.8) -- (5.5,0.8);
\draw[hl] (5.500,0.001) -- (5.390,0.120) -- (5.280,0.024) -- (5.170,-0.276) -- (5.060,-0.390) -- (4.950,-0.674) -- (4.840,-0.569) -- (4.730,-0.047) -- (4.620,-0.183) -- (4.510,-0.346) -- (4.400,-0.132) -- (4.290,0.020) -- (4.180,0.080) -- (4.070,-0.185) -- (3.960,-0.146) -- (3.850,0.110) -- (3.740,-0.261) -- (3.630,-0.334) -- (3.520,-0.811) -- (3.410,-1.063) -- (3.300,-1.439) -- (3.190,-1.334) -- (3.080,-1.508) -- (2.970,-1.255) -- (2.860,-1.050) -- (2.750,-0.946) -- (2.640,-1.416) -- (2.530,-1.350) -- (2.420,-1.165) -- (2.310,-0.954) -- (2.200,-1.121) -- (2.090,-1.026) -- (1.980,-1.034) -- (1.870,-0.990) -- (1.760,-0.569) -- (1.650,-0.548) -- (1.540,-0.373) -- (1.430,-0.051) -- (1.320,-0.016) -- (1.210,0.103) -- (1.100,0.246) -- (0.990,0.365) -- (0.880,0.304) -- (0.770,0.437) -- (0.660,0.686) -- (0.550,0.578) -- (0.440,0.735) -- (0.330,0.775) -- (0.220,0.764) -- (0.110,0.815) -- (0.000,0.800);
\draw[faint] (5.500,0.610) -- (5.390,0.128) -- (5.280,0.155) -- (5.170,0.355) -- (5.060,0.270) -- (4.950,0.494) -- (4.840,0.442) -- (4.730,0.644) -- (4.620,1.081) -- (4.510,0.784) -- (4.400,0.803) -- (4.290,0.611) -- (4.180,0.625) -- (4.070,0.234) -- (3.960,0.069) -- (3.850,0.039) -- (3.740,0.337) -- (3.630,0.681) -- (3.520,0.285) -- (3.410,0.080) -- (3.300,0.297) -- (3.190,-0.222) -- (3.080,-0.277) -- (2.970,-0.226) -- (2.860,0.171) -- (2.750,0.386) -- (2.640,0.332) -- (2.530,0.277) -- (2.420,0.259) -- (2.310,0.651) -- (2.200,0.565) -- (2.090,0.519) -- (1.980,0.619) -- (1.870,0.611) -- (1.760,0.592) -- (1.650,0.407) -- (1.540,0.456) -- (1.430,0.427) -- (1.320,0.676) -- (1.210,0.798) -- (1.100,0.794) -- (0.990,0.887) -- (0.880,0.824) -- (0.770,0.942) -- (0.660,0.901) -- (0.550,0.922) -- (0.440,0.770) -- (0.330,0.807) -- (0.220,0.731) -- (0.110,0.782) -- (0.000,0.800);
\draw[faint] (5.500,-0.244) -- (5.390,-0.527) -- (5.280,-0.401) -- (5.170,0.441) -- (5.060,0.124) -- (4.950,-0.084) -- (4.840,0.012) -- (4.730,0.196) -- (4.620,0.141) -- (4.510,0.084) -- (4.400,0.328) -- (4.290,0.490) -- (4.180,0.151) -- (4.070,0.144) -- (3.960,0.174) -- (3.850,-0.123) -- (3.740,0.000) -- (3.630,-0.211) -- (3.520,0.125) -- (3.410,0.212) -- (3.300,0.264) -- (3.190,0.128) -- (3.080,0.135) -- (2.970,-0.346) -- (2.860,-0.551) -- (2.750,-0.353) -- (2.640,-0.782) -- (2.530,-0.443) -- (2.420,-0.741) -- (2.310,-0.425) -- (2.200,-0.494) -- (2.090,-0.196) -- (1.980,-0.063) -- (1.870,-0.278) -- (1.760,0.093) -- (1.650,0.452) -- (1.540,0.485) -- (1.430,0.482) -- (1.320,0.503) -- (1.210,0.400) -- (1.100,0.635) -- (0.990,0.592) -- (0.880,0.631) -- (0.770,0.580) -- (0.660,0.576) -- (0.550,0.530) -- (0.440,0.738) -- (0.330,0.759) -- (0.220,0.827) -- (0.110,0.801) -- (0.000,0.800);
\draw[faint] (5.500,-0.556) -- (5.390,-0.601) -- (5.280,-0.723) -- (5.170,-0.631) -- (5.060,-0.682) -- (4.950,-0.700) -- (4.840,-1.080) -- (4.730,-1.227) -- (4.620,-0.544) -- (4.510,-0.690) -- (4.400,-0.942) -- (4.290,-0.724) -- (4.180,-0.191) -- (4.070,-0.594) -- (3.960,-0.574) -- (3.850,-0.681) -- (3.740,-1.108) -- (3.630,-0.763) -- (3.520,-0.665) -- (3.410,-0.546) -- (3.300,-0.664) -- (3.190,-0.437) -- (3.080,-0.494) -- (2.970,-0.436) -- (2.860,-0.627) -- (2.750,-0.818) -- (2.640,-0.356) -- (2.530,-0.380) -- (2.420,-0.208) -- (2.310,-0.125) -- (2.200,-0.135) -- (2.090,-0.151) -- (1.980,0.080) -- (1.870,0.098) -- (1.760,0.151) -- (1.650,0.235) -- (1.540,0.522) -- (1.430,0.678) -- (1.320,0.759) -- (1.210,0.677) -- (1.100,0.494) -- (0.990,0.687) -- (0.880,0.836) -- (0.770,0.810) -- (0.660,0.865) -- (0.550,0.917) -- (0.440,0.936) -- (0.330,0.927) -- (0.220,0.824) -- (0.110,0.813) -- (0.000,0.800);
\draw[faint] (5.500,-0.997) -- (5.390,-0.571) -- (5.280,-0.323) -- (5.170,0.031) -- (5.060,0.694) -- (4.950,1.151) -- (4.840,0.670) -- (4.730,0.062) -- (4.620,0.348) -- (4.510,0.008) -- (4.400,0.028) -- (4.290,0.319) -- (4.180,-0.197) -- (4.070,-0.802) -- (3.960,-0.622) -- (3.850,-0.521) -- (3.740,-0.514) -- (3.630,-0.421) -- (3.520,-0.592) -- (3.410,-0.926) -- (3.300,-0.849) -- (3.190,-0.994) -- (3.080,-1.298) -- (2.970,-1.002) -- (2.860,-0.875) -- (2.750,-0.638) -- (2.640,-0.761) -- (2.530,-0.784) -- (2.420,-0.875) -- (2.310,-0.920) -- (2.200,-0.709) -- (2.090,-0.723) -- (1.980,-0.486) -- (1.870,-0.273) -- (1.760,0.249) -- (1.650,0.055) -- (1.540,0.314) -- (1.430,0.368) -- (1.320,0.431) -- (1.210,0.265) -- (1.100,0.294) -- (0.990,0.498) -- (0.880,0.555) -- (0.770,0.625) -- (0.660,0.644) -- (0.550,0.804) -- (0.440,0.801) -- (0.330,0.661) -- (0.220,0.723) -- (0.110,0.783) -- (0.000,0.800);
\draw[faint] (5.500,-2.601) -- (5.390,-2.501) -- (5.280,-1.754) -- (5.170,-1.543) -- (5.060,-1.778) -- (4.950,-1.908) -- (4.840,-1.321) -- (4.730,-1.123) -- (4.620,-0.980) -- (4.510,-0.884) -- (4.400,-0.767) -- (4.290,-0.416) -- (4.180,-0.177) -- (4.070,-0.065) -- (3.960,-0.345) -- (3.850,-0.128) -- (3.740,-0.283) -- (3.630,0.097) -- (3.520,-0.235) -- (3.410,-0.211) -- (3.300,-0.150) -- (3.190,-0.450) -- (3.080,0.097) -- (2.970,0.523) -- (2.860,0.414) -- (2.750,0.628) -- (2.640,0.725) -- (2.530,0.096) -- (2.420,0.213) -- (2.310,0.249) -- (2.200,0.317) -- (2.090,0.130) -- (1.980,0.143) -- (1.870,0.179) -- (1.760,0.483) -- (1.650,0.583) -- (1.540,0.610) -- (1.430,0.900) -- (1.320,0.791) -- (1.210,0.731) -- (1.100,0.474) -- (0.990,0.756) -- (0.880,0.890) -- (0.770,0.975) -- (0.660,0.996) -- (0.550,0.941) -- (0.440,0.902) -- (0.330,0.835) -- (0.220,0.803) -- (0.110,0.801) -- (0.000,0.800);
\node[lab,anchor=east] at (-0.05,0.8) {$x_0=1$};
\end{tikzpicture}
\end{center}
```

The DDPM reverse process run on one-dimensional data that are always $x_0=1$, with $T=50$ steps, $\beta_t$ from $10^{-4}$ to $0.2$, and the exact noise prediction $\varepsilon=(x_t-\sqrt{\bar\alpha_t})/\sqrt{1-\bar\alpha_t}$ in place of a network. Six runs start from standard normal $x_{50}$ (right) and all end at $x_0=1$ (left).

:::

The reverse step is @prp-diffusion-posterior with the unknown noise replaced by its prediction. Equivalently the network predicts the clean image $\hat{\mathbf{x}}_0=(\mathbf{x}_t-\sqrt{1-\bar\alpha_t}\,\boldsymbol\varepsilon_\theta)/\sqrt{\bar\alpha_t}$, and the step samples from $q(\mathbf{x}_{t-1}\mid\mathbf{x}_t,\hat{\mathbf{x}}_0)$. The model is a hierarchical latent variable model like a VAE (@def-vae) with a fixed encoder, and the simple loss is a reweighting of its evidence lower bound (@def-elbo); this derivation is not reproduced here.

```{=latex}
\begin{algorithm}
\caption{DDPM training}
\begin{algorithmic}
\INPUT training data, schedule $\beta_{1..T}$, network $\boldsymbol\varepsilon_\theta$, learning rate
\OUTPUT trained parameters $\theta$
\REPEAT
    \STATE draw a minibatch of $\mathbf{x}_0$; for each, draw $t\sim\text{Uniform}\{1,\dots,T\}$ and $\boldsymbol\varepsilon\sim\mathcal N(\mathbf 0,I)$
    \STATE $\mathbf{x}_t\gets\sqrt{\bar\alpha_t}\mathbf{x}_0+\sqrt{1-\bar\alpha_t}\,\boldsymbol\varepsilon$
    \STATE take a gradient step on $\lVert\boldsymbol\varepsilon-\boldsymbol\varepsilon_\theta(\mathbf{x}_t,t)\rVert^2$, averaged over the minibatch
\UNTIL{converged}
\end{algorithmic}
\end{algorithm}
```

```{=latex}
\begin{algorithm}
\caption{DDPM sampling}
\begin{algorithmic}
\INPUT trained $\boldsymbol\varepsilon_\theta$, schedule $\beta_{1..T}$
\OUTPUT a sample $\mathbf{x}_0$
\STATE $\mathbf{x}_T\sim\mathcal N(\mathbf 0,I)$
\FOR{$t=T,T-1,\dots,1$}
    \STATE $\mathbf{z}\sim\mathcal N(\mathbf 0,I)$ if $t>1$, else $\mathbf{z}\gets\mathbf 0$
    \STATE $\mathbf{x}_{t-1}\gets\frac{1}{\sqrt{\alpha_t}}\bigl(\mathbf{x}_t-\frac{\beta_t}{\sqrt{1-\bar\alpha_t}}\boldsymbol\varepsilon_\theta(\mathbf{x}_t,t)\bigr)+\sqrt{\tilde\beta_t}\,\mathbf{z}$
\ENDFOR
\RETURN $\mathbf{x}_0$
\end{algorithmic}
\end{algorithm}
```

::: {#rmk-diffusion-unet .remark name="The denoising network" editor="The training algorithm has no figure of its own: one training step only adds noise to a data point and regresses on it; the figure after the DDPM definition runs the sampling algorithm with the exact noise predictor that training aims at."}

$\boldsymbol\varepsilon_\theta$ maps an image to an image of the same shape, so it is usually a *U-Net*: a convolutional encoder that halves the resolution and increases the channels a few times, a mirrored decoder that upsamples back, and skip connections that concatenate each encoder level's features to the decoder level of the same resolution, so fine detail need not pass through the bottleneck. The step $t$ enters through a sinusoidal embedding (@def-sinusoidal-positional-encoding) added inside every block; a condition such as a text embedding enters the same way or by cross-attention (@def-cross-attention).

:::

::: {#def-classifier-free-guidance .definition name="Classifier-free guidance"}

For a conditional model $\boldsymbol\varepsilon_\theta(\mathbf{x}_t,t,c)$ trained with the condition $c$ replaced by a null condition $\varnothing$ on a random 10–20% of the examples, *classifier-free guidance* with weight $w\ge0$ samples with

$$
\tilde{\boldsymbol\varepsilon}=(1+w)\,\boldsymbol\varepsilon_\theta(\mathbf{x}_t,t,c)-w\,\boldsymbol\varepsilon_\theta(\mathbf{x}_t,t,\varnothing)
$$

in place of $\boldsymbol\varepsilon_\theta$ in the reverse step.

:::

The guided prediction moves away from what the model would do without the condition, so the samples follow the condition more closely; larger $w$ gains fidelity to $c$ and loses diversity. $w=0$ is the plain conditional model.
