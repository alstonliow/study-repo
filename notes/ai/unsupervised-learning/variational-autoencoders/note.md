---
title: "Variational Inference and Variational Autoencoders"
sources: [cs229-11]
requires: [ai/unsupervised-learning/em-algorithm, ai/deep-learning/neural-networks]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS229 lecture notes (version of 23 August 2026), Chapter 11.5 (variational inference, mean-field and Gaussian families, amortized encoders, the variational autoencoder, the reparameterization trick), in our own wording. The closed-form KL term, its proof and the numerical check are our own additions; proofs written out in steps. -->

The E-step of EM needs the exact posterior $p(z\mid\mathbf{x};\boldsymbol\theta)$. When the model is a neural network this posterior has no closed form. *Variational inference* gives up exactness: it maximizes the ELBO (@def-elbo) over a manageable family of distributions $Q$ instead.

::: {#def-variational-inference .definition name="Variational inference"}

Fix a family $\mathcal Q$ of distributions on the latent space. *Variational inference* maximizes

$$
\sum_{i=1}^N\operatorname{ELBO}(\mathbf{x}^{(i)};Q_i,\boldsymbol\theta)\qquad\text{over }\boldsymbol\theta\text{ and }Q_1,\dots,Q_N\in\mathcal Q.
$$

By @thm-elbo this maximizes a lower bound on $\ell(\boldsymbol\theta)$ whose gap is $\sum_iD\bigl(Q_i\,\|\,p(z\mid\mathbf{x}^{(i)};\boldsymbol\theta)\bigr)$; if $\mathcal Q$ contains the exact posteriors, it is EM. A common family is the *mean-field* one, in which $Q(z)=\prod_kQ^{(k)}(z_k)$ makes the coordinates of $z$ independent, for instance Gaussians with diagonal covariance.

:::

::: {#def-vae .definition name="Variational autoencoder"}

A *variational autoencoder* (VAE) has latent variables $z\in\mathbb{R}^k$ and:

1. a *generative model* (decoder) $z\sim N(\mathbf{0},I_k)$ and $\mathbf{x}\mid z\sim N\bigl(g(z;\boldsymbol\theta),\sigma^2I_d\bigr)$, where $g$ is a neural network;
2. an *amortized* variational family (encoder): instead of a separate $Q_i$ per example, two networks $q(\mathbf{x};\boldsymbol\phi)\in\mathbb{R}^k$ and $v(\mathbf{x};\boldsymbol\psi)\in\mathbb{R}^k_{>0}$ give $Q_i=N\bigl(q(\mathbf{x}^{(i)};\boldsymbol\phi),\operatorname{diag}(v(\mathbf{x}^{(i)};\boldsymbol\psi))^2\bigr)$.

It is trained by maximizing $\sum_i\operatorname{ELBO}(\mathbf{x}^{(i)};Q_i,\boldsymbol\theta)$ over $\boldsymbol\theta,\boldsymbol\phi,\boldsymbol\psi$ by stochastic gradient ascent.

:::

::: {#prp-elbo-reconstruction-kl .proposition name="Reconstruction and regularization terms"}

For any $Q$, with $p(z)$ the prior,

$$
\operatorname{ELBO}(\mathbf{x};Q,\boldsymbol\theta)=E_{z\sim Q}\bigl[\log p(\mathbf{x}\mid z;\boldsymbol\theta)\bigr]-D\bigl(Q\,\|\,p(z)\bigr).
$$

For the VAE the first term is $-\dfrac1{2\sigma^2}E_{z\sim Q}\lVert\mathbf{x}-g(z;\boldsymbol\theta)\rVert^2$ plus a constant: a reconstruction error.

:::

::: {.proof}

1. Write $p(\mathbf{x},z;\boldsymbol\theta)=p(z)\,p(\mathbf{x}\mid z;\boldsymbol\theta)$ in @def-elbo:

   $$
   \operatorname{ELBO}=E_{z\sim Q}\bigl[\log p(\mathbf{x}\mid z;\boldsymbol\theta)\bigr]+E_{z\sim Q}\Bigl[\log\frac{p(z)}{Q(z)}\Bigr],
   $$

   and the second term is $-D(Q\,\|\,p(z))$.

2. For the VAE, $\log p(\mathbf{x}\mid z;\boldsymbol\theta)=-\frac d2\log(2\pi\sigma^2)-\frac1{2\sigma^2}\lVert\mathbf{x}-g(z;\boldsymbol\theta)\rVert^2$.

:::

::: {#prp-gaussian-kl .proposition name="KL divergence of a diagonal Gaussian from the standard one"}

With natural logarithms, for $Q=N(\boldsymbol\mu,\operatorname{diag}(s_1^2,\dots,s_k^2))$,

$$
D\bigl(Q\,\|\,N(\mathbf{0},I_k)\bigr)=\frac12\sum_{j=1}^k\bigl(s_j^2+\mu_j^2-1-\log s_j^2\bigr).
$$

:::

::: {.proof}

1. Both densities are products over the coordinates, so the divergence is the sum of the one-dimensional divergences.

2. In one dimension, with $z\sim N(\mu,s^2)$,

   $$
   \log\frac{Q(z)}{p(z)}=-\tfrac12\log s^2-\frac{(z-\mu)^2}{2s^2}+\frac{z^2}2.
   $$

3. Taking expectations, $E[(z-\mu)^2]=s^2$ and $E[z^2]=s^2+\mu^2$, so the divergence is $-\tfrac12\log s^2-\tfrac12+\tfrac12(s^2+\mu^2)$, which is the stated term.

:::

For example, $\boldsymbol\mu=(1,0)$ and $s^2=(1,\tfrac14)$ give $\tfrac12\bigl(1+(\tfrac14-1+\log4)\bigr)\approx0.818$. The divergence is $0$ exactly when $\boldsymbol\mu=\mathbf{0}$ and every $s_j=1$, so this term pulls the encoder towards the prior.

::: {#prp-reparameterization .proposition name="The reparameterization trick"}

If $z=\boldsymbol\mu+\mathbf{s}\odot\boldsymbol\xi$ with $\boldsymbol\xi\sim N(\mathbf{0},I_k)$ ($\odot$ the entrywise product), then $z\sim N(\boldsymbol\mu,\operatorname{diag}(\mathbf{s})^2)$, and for a differentiable $f$ (with enough integrability to differentiate under the expectation)

$$
\nabla_{\boldsymbol\mu}E_z[f(z)]=E_{\boldsymbol\xi}\bigl[\nabla f(\boldsymbol\mu+\mathbf{s}\odot\boldsymbol\xi)\bigr],\qquad \nabla_{\mathbf{s}}E_z[f(z)]=E_{\boldsymbol\xi}\bigl[\nabla f(\boldsymbol\mu+\mathbf{s}\odot\boldsymbol\xi)\odot\boldsymbol\xi\bigr].
$$

:::

::: {.proof}

1. Each $z_j=\mu_j+s_j\xi_j$ is an affine function of a standard normal, hence $N(\mu_j,s_j^2)$, and the coordinates are independent (@thm-jointly-gaussian-properties).

2. So $E_z[f(z)]=E_{\boldsymbol\xi}[f(\boldsymbol\mu+\mathbf{s}\odot\boldsymbol\xi)]$, where the distribution of $\boldsymbol\xi$ does not depend on $\boldsymbol\mu$ or $\mathbf{s}$.

3. Differentiating under the expectation with the chain rule, $\partial z_j/\partial\mu_j=1$ and $\partial z_j/\partial s_j=\xi_j$, which gives both formulas.

:::

::: {#rmk-vae-training .remark name="Training a VAE" editor="No figure: a VAE needs trained networks on real data; no small example is faithful."}

For each example, sample one $\boldsymbol\xi$, set $z=q(\mathbf{x};\boldsymbol\phi)+v(\mathbf{x};\boldsymbol\psi)\odot\boldsymbol\xi$, and use

$$
-\frac1{2\sigma^2}\lVert\mathbf{x}-g(z;\boldsymbol\theta)\rVert^2-\frac12\sum_j\bigl(v_j^2+q_j^2-1-\log v_j^2\bigr)
$$

as an unbiased estimate of the ELBO up to a constant (@prp-elbo-reconstruction-kl and @prp-gaussian-kl). By @prp-reparameterization its gradient in $\boldsymbol\theta,\boldsymbol\phi,\boldsymbol\psi$ is an unbiased estimate of the ELBO's gradient, computed by backpropagation through $z$ (@def-backpropagation). After training, new data are generated by sampling $z\sim N(\mathbf{0},I)$ and outputting $g(z;\boldsymbol\theta)$. The name comes from the shape: the encoder compresses $\mathbf{x}$ to a code $z$, and the decoder reconstructs $\mathbf{x}$ from it.

:::
