---
title: "The EM Algorithm and the Evidence Lower Bound"
sources: [cs229-11]
requires: [ai/unsupervised-learning/gaussian-mixtures, math/optimization/convex-functions/convex-functions, math/probability/information-theory/entropy]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS229 lecture notes (version of 23 August 2026), Chapter 11.2-11.4 (Jensen's inequality, the evidence lower bound, the general EM algorithm and its monotonicity, the ELBO as likelihood minus a KL divergence, the mixture of Gaussians M-step derived), in our own wording; proofs written out in steps. The count-and-normalize form of EM for Bayesian networks is @def-expectation-maximization (CS221); this note gives the general derivation it rests on. -->

EM works for any model with latent variables $z$ and parameters $\boldsymbol\theta$: the joint $p(\mathbf{x},z;\boldsymbol\theta)$ is easy to maximize, but the *marginal likelihood* $p(\mathbf{x};\boldsymbol\theta)=\sum_zp(\mathbf{x},z;\boldsymbol\theta)$ is not. (For continuous $z$ replace sums by integrals.) The key is a lower bound on $\log p(\mathbf{x};\boldsymbol\theta)$ from Jensen's inequality (@thm-jensen-inequality).

::: {#def-elbo .definition name="Evidence lower bound"}

For an observation $\mathbf{x}$ and any distribution $Q$ on the values of $z$ with $Q(z)>0$ wherever $p(\mathbf{x},z;\boldsymbol\theta)>0$, the *evidence lower bound* (ELBO) is

$$
\operatorname{ELBO}(\mathbf{x};Q,\boldsymbol\theta)=\sum_zQ(z)\log\frac{p(\mathbf{x},z;\boldsymbol\theta)}{Q(z)}=E_{z\sim Q}\Bigl[\log\frac{p(\mathbf{x},z;\boldsymbol\theta)}{Q(z)}\Bigr].
$$

:::

::: {#thm-elbo .theorem name="The ELBO bounds the log-likelihood"}

For every such $Q$,

$$
\log p(\mathbf{x};\boldsymbol\theta)=\operatorname{ELBO}(\mathbf{x};Q,\boldsymbol\theta)+D\bigl(Q\,\big\|\,p(z\mid\mathbf{x};\boldsymbol\theta)\bigr)\ge\operatorname{ELBO}(\mathbf{x};Q,\boldsymbol\theta),
$$

with equality if and only if $Q(z)=p(z\mid\mathbf{x};\boldsymbol\theta)$ for all $z$. Here $D$ is the relative entropy of @def-relative-entropy.

:::

::: {.proof}

1. *The bound.* $\log p(\mathbf{x};\boldsymbol\theta)=\log\sum_zQ(z)\dfrac{p(\mathbf{x},z;\boldsymbol\theta)}{Q(z)}=\log E_{z\sim Q}\Bigl[\dfrac{p(\mathbf{x},z;\boldsymbol\theta)}{Q(z)}\Bigr]$. Since $\log$ is concave, Jensen's inequality gives $\log E[\,\cdot\,]\ge E[\log\,\cdot\,]$, which is the ELBO.

2. *The identity.* Write $p(\mathbf{x},z;\boldsymbol\theta)=p(\mathbf{x};\boldsymbol\theta)\,p(z\mid\mathbf{x};\boldsymbol\theta)$. Then

   $$
   \operatorname{ELBO}=\sum_zQ(z)\log p(\mathbf{x};\boldsymbol\theta)+\sum_zQ(z)\log\frac{p(z\mid\mathbf{x};\boldsymbol\theta)}{Q(z)}=\log p(\mathbf{x};\boldsymbol\theta)-D\bigl(Q\,\|\,p(z\mid\mathbf{x};\boldsymbol\theta)\bigr).
   $$

3. *Equality.* The relative entropy is $\ge0$, with equality exactly when the two distributions agree (Gibbs' inequality, @thm-gibbs-inequality).

:::

::: {#def-em-general .definition name="The EM algorithm" related="def-expectation-maximization"}

For independent observations $\mathbf{x}^{(1)},\dots,\mathbf{x}^{(N)}$ with latent $z^{(i)}$, the log-likelihood is $\ell(\boldsymbol\theta)=\sum_i\log p(\mathbf{x}^{(i)};\boldsymbol\theta)$. *EM* starts from $\boldsymbol\theta^{(0)}$ and for $t=0,1,2,\dots$ repeats:

1. *E-step*: $Q_i(z)=p(z\mid\mathbf{x}^{(i)};\boldsymbol\theta^{(t)})$ for each $i$;
2. *M-step*: $\boldsymbol\theta^{(t+1)}=\operatorname{arg\,max}_{\boldsymbol\theta}\sum_i\operatorname{ELBO}(\mathbf{x}^{(i)};Q_i,\boldsymbol\theta)=\operatorname{arg\,max}_{\boldsymbol\theta}\sum_i\sum_zQ_i(z)\log p(\mathbf{x}^{(i)},z;\boldsymbol\theta)$.

(The term $-\sum_zQ_i(z)\log Q_i(z)$ of the ELBO does not depend on $\boldsymbol\theta$.) The M-step maximizes a *weighted complete-data* log-likelihood, which is usually as easy as fully observed maximum likelihood.

:::

```{=latex}
\begin{algorithm}
\caption{EM}
\begin{algorithmic}
\INPUT Observations $\mathbf{x}^{(1)},\dots,\mathbf{x}^{(N)}$, a model $p(\mathbf{x},z;\boldsymbol\theta)$, initial $\boldsymbol\theta$
\REPEAT
    \FOR{$i=1,\dots,N$}
        \STATE $Q_i(z)\gets p(z\mid\mathbf{x}^{(i)};\boldsymbol\theta)$ for all $z$ \COMMENT{E-step}
    \ENDFOR
    \STATE $\boldsymbol\theta\gets\operatorname{arg\,max}_{\boldsymbol\theta'}\sum_i\sum_zQ_i(z)\log p(\mathbf{x}^{(i)},z;\boldsymbol\theta')$ \COMMENT{M-step}
\UNTIL{$\ell(\boldsymbol\theta)$ changes by less than a tolerance}
\end{algorithmic}
\end{algorithm}
```

::: {#thm-em-monotone .theorem name="EM never decreases the likelihood"}

The iterates of EM satisfy $\ell(\boldsymbol\theta^{(t+1)})\ge\ell(\boldsymbol\theta^{(t)})$ for every $t$.

:::

::: {.proof}

1. By @thm-elbo, the E-step choice $Q_i=p(z\mid\mathbf{x}^{(i)};\boldsymbol\theta^{(t)})$ makes the bound tight at $\boldsymbol\theta^{(t)}$: $\ell(\boldsymbol\theta^{(t)})=\sum_i\operatorname{ELBO}(\mathbf{x}^{(i)};Q_i,\boldsymbol\theta^{(t)})$.

2. The M-step maximizes $\sum_i\operatorname{ELBO}(\mathbf{x}^{(i)};Q_i,\boldsymbol\theta)$ over $\boldsymbol\theta$, so its value at $\boldsymbol\theta^{(t+1)}$ is at least its value at $\boldsymbol\theta^{(t)}$.

3. By @thm-elbo again, for these same $Q_i$, $\ell(\boldsymbol\theta^{(t+1)})\ge\sum_i\operatorname{ELBO}(\mathbf{x}^{(i)};Q_i,\boldsymbol\theta^{(t+1)})$.

4. Chaining: $\ell(\boldsymbol\theta^{(t+1)})\ge\sum_i\operatorname{ELBO}(\mathbf{x}^{(i)};Q_i,\boldsymbol\theta^{(t+1)})\ge\sum_i\operatorname{ELBO}(\mathbf{x}^{(i)};Q_i,\boldsymbol\theta^{(t)})=\ell(\boldsymbol\theta^{(t)})$.

:::

::: {#rmk-em-coordinate-ascent .remark name="EM as coordinate ascent" editor="No figure: the general algorithm is drawn through its mixture-of-Gaussians instance in fig-gaussian-mixtures-1."}

Write $F(Q,\boldsymbol\theta)=\sum_i\operatorname{ELBO}(\mathbf{x}^{(i)};Q_i,\boldsymbol\theta)$. By @thm-elbo the E-step maximizes $F$ over $Q$ with $\boldsymbol\theta$ fixed, and the M-step maximizes it over $\boldsymbol\theta$ with $Q$ fixed: EM is coordinate ascent on $F$, like $k$-means on the distortion. Since $\ell$ is bounded above in many models, the increasing sequence $\ell(\boldsymbol\theta^{(t)})$ then converges, though only to a stationary value, not necessarily the global maximum. When the exact posterior is intractable, one can maximize $F$ over a restricted family of $Q$ instead (@sec-ai-deep-unsupervised-learning-variational-autoencoders).

:::

::: {#thm-gmm-m-step .theorem name="The mixture of Gaussians M-step"}

For the mixture of Gaussians (@def-gaussian-mixture), with responsibilities $w_j^{(i)}=Q_i(j)$ from the E-step, the M-step of @def-em-general gives exactly the updates of @def-em-gmm (assuming each $N_j>0$ and each resulting $\Sigma_j$ invertible).

:::

::: {.proof}

1. The M-step objective is

   $$
   \sum_i\sum_jw_j^{(i)}\Bigl(\log\phi_j-\tfrac12\log\det\Sigma_j-\tfrac12(\mathbf{x}^{(i)}-\boldsymbol\mu_j)^{\mathsf T}\Sigma_j^{-1}(\mathbf{x}^{(i)}-\boldsymbol\mu_j)\Bigr)+\text{const}.
   $$

   The $\phi$ terms, and the terms of each component $j$, can be maximized separately.

2. *Means.* The gradient in $\boldsymbol\mu_j$ is $\Sigma_j^{-1}\sum_iw_j^{(i)}(\mathbf{x}^{(i)}-\boldsymbol\mu_j)$ (@prp-matrix-gradient-rules), zero at the weighted mean; the objective is a concave quadratic in $\boldsymbol\mu_j$, so this is the maximum.

3. *Covariances.* With $P_j=\Sigma_j^{-1}$ the terms in $\Sigma_j$ are $\tfrac{N_j}2\log\det P_j-\tfrac12\operatorname{tr}(P_jS_j)$ with $S_j=\sum_iw_j^{(i)}(\mathbf{x}^{(i)}-\boldsymbol\mu_j)(\mathbf{x}^{(i)}-\boldsymbol\mu_j)^{\mathsf T}$. Exactly as in steps 4–6 of the proof of @thm-gda-mle, the maximum is $\Sigma_j=S_j/N_j$.

4. *Weights.* Maximize $\sum_jN_j\log\phi_j$ subject to $\sum_j\phi_j=1$. The Lagrange condition $N_j/\phi_j=\beta$ gives $\phi_j=N_j/\beta$, and the constraint gives $\beta=\sum_jN_j=N$, since the responsibilities of each point sum to $1$. The objective is concave in $\boldsymbol\phi$ and tends to $-\infty$ at the boundary of the simplex wherever some $N_j>0$ has $\phi_j\to0$, so this stationary point is the maximum.

:::
