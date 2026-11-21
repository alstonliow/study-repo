---
title: "Generative Classifiers: Gaussian Discriminant Analysis"
sources: [cs229-4]
requires: [ai/machine-learning/logistic-regression, math/probability/estimation/jointly-gaussian, math/linear-algebra/matrix-methods/matrix-derivatives]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS229 lecture notes (version of 23 August 2026), Chapter 4.1 (generative and discriminative models, the GDA model, its maximum likelihood estimates, GDA versus logistic regression), in our own wording. The derivations of the estimates and of the logistic posterior are written out in steps; the one-dimensional example is our own. -->

Logistic regression models $p(y\mid\mathbf{x})$ directly. A *generative* classifier instead models how each class produces its inputs, and then uses Bayes' rule to classify.

::: {#def-generative-classifier .definition name="Discriminative and generative models"}

A *discriminative* model specifies $p(y\mid\mathbf{x})$ (or a direct map from $\mathbf{x}$ to labels). A *generative* model specifies the class prior $p(y)$ and the class-conditional distributions $p(\mathbf{x}\mid y)$. It classifies by Bayes' rule,

$$
\hat y(\mathbf{x})=\operatorname*{arg\,max}_yp(y\mid\mathbf{x})=\operatorname*{arg\,max}_y\frac{p(\mathbf{x}\mid y)\,p(y)}{p(\mathbf{x})}=\operatorname*{arg\,max}_yp(\mathbf{x}\mid y)\,p(y),
$$

since $p(\mathbf{x})$ does not depend on $y$. Naive Bayes (@def-naive-bayes) is a generative model with discrete features.

:::

::: {#def-gda .definition name="Gaussian discriminant analysis"}

The *Gaussian discriminant analysis* (GDA) model for inputs $\mathbf{x}\in\mathbb{R}^d$ and labels $y\in\{0,1\}$ has parameters $\phi\in(0,1)$, $\boldsymbol\mu_0,\boldsymbol\mu_1\in\mathbb{R}^d$ and a positive definite $\Sigma$, and assumes

$$
y\sim\operatorname{Bernoulli}(\phi),\qquad \mathbf{x}\mid y=0\sim N(\boldsymbol\mu_0,\Sigma),\qquad \mathbf{x}\mid y=1\sim N(\boldsymbol\mu_1,\Sigma),
$$

with the Gaussian density of @thm-jointly-gaussian-properties. The two classes share one covariance matrix.

:::

::: {#fig-gaussian-discriminant-analysis-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-0.4,0) -- (5.2,0) node[lab, right] {$x_1$};
\draw[->] (0,-0.4) -- (0,3.6) node[lab, above] {$x_2$};
\draw[faint, rotate around={25:(1.5,1.2)}] (1.5,1.2) ellipse (0.40 and 0.22);
\draw[faint, rotate around={25:(1.5,1.2)}] (1.5,1.2) ellipse (0.80 and 0.44);
\draw[faint, rotate around={25:(1.5,1.2)}] (1.5,1.2) ellipse (1.20 and 0.66);
\draw[emph, rotate around={25:(3.4,2.4)}] (3.4,2.4) ellipse (0.40 and 0.22);
\draw[emph, rotate around={25:(3.4,2.4)}] (3.4,2.4) ellipse (0.80 and 0.44);
\draw[emph, rotate around={25:(3.4,2.4)}] (3.4,2.4) ellipse (1.20 and 0.66);
\draw[hl] (1.2,3.4) -- (3.9,0.2);
\node[tick] at (0.8,0.3) {$y=0$};
\node[tick] at (4.6,3.2) {$y=1$};
\end{tikzpicture}
\end{center}
```

GDA in two dimensions: each class is a Gaussian with its own mean and a shared covariance (equal contour shapes), which makes the decision boundary a straight line

:::

::: {#thm-gda-mle .theorem name="Maximum likelihood estimates for GDA"}

Given examples $(\mathbf{x}^{(i)},y^{(i)})$, $i=1,\dots,N$, containing both classes, let $N_k$ be the number with $y^{(i)}=k$. The joint log-likelihood $\ell=\sum_i\log p(\mathbf{x}^{(i)},y^{(i)})$ is maximized by

$$
\phi=\frac{N_1}{N},\qquad \boldsymbol\mu_k=\frac1{N_k}\sum_{i:\,y^{(i)}=k}\mathbf{x}^{(i)},\qquad \Sigma=\frac1N\sum_{i=1}^N\bigl(\mathbf{x}^{(i)}-\boldsymbol\mu_{y^{(i)}}\bigr)\bigl(\mathbf{x}^{(i)}-\boldsymbol\mu_{y^{(i)}}\bigr)^{\mathsf T},
$$

provided this $\Sigma$ is invertible: the class frequency, the class means and the pooled covariance about the class means.

:::

::: {.proof}

1. Since $p(\mathbf{x},y)=p(y)\,p(\mathbf{x}\mid y)$,

   $$
   \ell=\sum_i\bigl(y^{(i)}\log\phi+(1-y^{(i)})\log(1-\phi)\bigr)-\frac N2\log\det\Sigma-\frac12\sum_i\bigl(\mathbf{x}^{(i)}-\boldsymbol\mu_{y^{(i)}}\bigr)^{\mathsf T}\Sigma^{-1}\bigl(\mathbf{x}^{(i)}-\boldsymbol\mu_{y^{(i)}}\bigr)+\text{const}.
   $$

   The first sum involves only $\phi$, so $\phi$ can be maximized separately.

2. *$\phi$.* The first sum is $N_1\log\phi+N_0\log(1-\phi)$. Its derivative $N_1/\phi-N_0/(1-\phi)$ is zero only at $\phi=N_1/N$, and the function tends to $-\infty$ at both ends of $(0,1)$, so this is the maximum.

3. *$\boldsymbol\mu_k$ for fixed $\Sigma$.* Only the examples of class $k$ involve $\boldsymbol\mu_k$. By @prp-matrix-gradient-rules, the gradient of $-\tfrac12(\mathbf{x}-\boldsymbol\mu)^{\mathsf T}\Sigma^{-1}(\mathbf{x}-\boldsymbol\mu)$ in $\boldsymbol\mu$ is $\Sigma^{-1}(\mathbf{x}-\boldsymbol\mu)$, so the gradient in $\boldsymbol\mu_k$ is $\Sigma^{-1}\sum_{i:\,y^{(i)}=k}(\mathbf{x}^{(i)}-\boldsymbol\mu_k)$. It vanishes exactly at the class mean, and $\ell$ is a concave quadratic in $\boldsymbol\mu_k$, so the class mean is the maximum for every $\Sigma$.

4. *$\Sigma$ with the means at their optimum.* Put $P=\Sigma^{-1}$ and $S=\sum_i(\mathbf{x}^{(i)}-\boldsymbol\mu_{y^{(i)}})(\mathbf{x}^{(i)}-\boldsymbol\mu_{y^{(i)}})^{\mathsf T}$. Writing each quadratic form as a trace (the trace trick of @sec-math-linear-algebra-matrix-methods-matrix-derivatives), the terms of $\ell$ that involve $\Sigma$ are

   $$
   g(P)=\frac N2\log\det P-\frac12\operatorname{tr}(PS).
   $$

5. By @prp-matrix-gradient-rules, $\nabla_Pg=\tfrac N2P^{-1}-\tfrac12S$ (both $P$ and $S$ are symmetric). This vanishes when $P^{-1}=S/N$, that is, $\Sigma=S/N$.

6. $g$ is concave on positive definite $P$: $\log\det$ is concave (@exm-log-det-concave) and $\operatorname{tr}(PS)$ is linear. A stationary point of a concave function is a maximum, which completes the proof.

:::

::: {#thm-gda-logistic-posterior .theorem name="The GDA posterior is logistic"}

Under the GDA model,

$$
p(y=1\mid\mathbf{x})=\sigma\bigl(\boldsymbol\theta^{\mathsf T}\mathbf{x}+\theta_0\bigr),\qquad \boldsymbol\theta=\Sigma^{-1}(\boldsymbol\mu_1-\boldsymbol\mu_0),\qquad \theta_0=-\tfrac12\bigl(\boldsymbol\mu_1^{\mathsf T}\Sigma^{-1}\boldsymbol\mu_1-\boldsymbol\mu_0^{\mathsf T}\Sigma^{-1}\boldsymbol\mu_0\bigr)+\log\frac{\phi}{1-\phi},
$$

where $\sigma$ is the logistic function. So GDA classifies with a linear decision boundary $\boldsymbol\theta^{\mathsf T}\mathbf{x}+\theta_0=0$.

:::

::: {.proof}

1. By Bayes' rule, $p(y=1\mid\mathbf{x})=\dfrac{1}{1+e^{-r(\mathbf{x})}}$ with the log odds $r(\mathbf{x})=\log\dfrac{p(\mathbf{x}\mid y=1)\,\phi}{p(\mathbf{x}\mid y=0)\,(1-\phi)}$.

2. The normalizing constants of the two Gaussians are equal because $\Sigma$ is shared, so they cancel and

   $$
   r(\mathbf{x})=-\tfrac12(\mathbf{x}-\boldsymbol\mu_1)^{\mathsf T}\Sigma^{-1}(\mathbf{x}-\boldsymbol\mu_1)+\tfrac12(\mathbf{x}-\boldsymbol\mu_0)^{\mathsf T}\Sigma^{-1}(\mathbf{x}-\boldsymbol\mu_0)+\log\frac{\phi}{1-\phi}.
   $$

3. Expanding, the terms $\mathbf{x}^{\mathsf T}\Sigma^{-1}\mathbf{x}$ cancel. Since $\Sigma^{-1}$ is symmetric, the cross terms give $(\boldsymbol\mu_1-\boldsymbol\mu_0)^{\mathsf T}\Sigma^{-1}\mathbf{x}=\boldsymbol\theta^{\mathsf T}\mathbf{x}$, and the remaining constants are $\theta_0$.

:::

::: {#fig-gaussian-discriminant-analysis-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (7.4,0) node[lab, right] {$x$};
\draw[faint, domain=0:7, samples=80, smooth, variable=\x] plot ({\x}, {2.4*exp(-((\x-2.5)^2)/(2*0.9^2))/(0.9*sqrt(2*pi))});
\draw[faint, domain=0:7, samples=80, smooth, variable=\x] plot ({\x}, {2.4*exp(-((\x-4.6)^2)/(2*0.9^2))/(0.9*sqrt(2*pi))});
\draw[hl, domain=0:7, samples=80, smooth, variable=\x] plot ({\x}, {2.2/(1+exp(-(\x-3.55)*2.6))});
\draw[faint, dashed] (3.55,0) -- (3.55,2.3);
\node[tick, text=accent] at (6.5,2.4) {$\Pr(y=1\mid x)$};
\end{tikzpicture}
\end{center}
```

With shared variance the GDA posterior $\Pr(y=1\mid x)$ is a logistic function of $x$: it crosses $\tfrac12$ midway between the class means when the priors are equal

:::

::: {#exm-gda-one-dimension .example name="Two classes on a line"}

Class $0$ has inputs $0,1,2$ and class $1$ has inputs $3,4,5$. By @thm-gda-mle, $\phi=\tfrac12$, $\mu_0=1$, $\mu_1=4$ and $\sigma^2=\tfrac16(1+0+1+1+0+1)=\tfrac23$. By @thm-gda-logistic-posterior,

$$
\theta=\frac{\mu_1-\mu_0}{\sigma^2}=4.5,\qquad \theta_0=-\frac{\mu_1^2-\mu_0^2}{2\sigma^2}=-11.25,
$$

so $p(y=1\mid x)=\sigma(4.5x-11.25)$ and the boundary is $x=2.5$, halfway between the means, as equal priors and a shared variance require. At $x=3$ the model gives $\sigma(2.25)\approx0.905$.

:::

::: {#fig-gaussian-discriminant-analysis-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm,y=1cm]
\draw[->] (-1.5,0) -- (6.8,0) node[lab,anchor=west] {$x$};
\draw[faint] (-1.50,0.013) -- (-1.40,0.019) -- (-1.30,0.028) -- (-1.20,0.039) -- (-1.10,0.054) -- (-1.00,0.073) -- (-0.90,0.098) -- (-0.80,0.129) -- (-0.70,0.168) -- (-0.60,0.215) -- (-0.50,0.271) -- (-0.40,0.337) -- (-0.30,0.413) -- (-0.20,0.498) -- (-0.10,0.591) -- (0.00,0.692) -- (0.10,0.798) -- (0.20,0.907) -- (0.30,1.015) -- (0.40,1.119) -- (0.50,1.215) -- (0.60,1.300) -- (0.70,1.370) -- (0.80,1.422) -- (0.90,1.455) -- (1.00,1.466) -- (1.10,1.455) -- (1.20,1.422) -- (1.30,1.370) -- (1.40,1.300) -- (1.50,1.215) -- (1.60,1.119) -- (1.70,1.015) -- (1.80,0.907) -- (1.90,0.798) -- (2.00,0.692) -- (2.10,0.591) -- (2.20,0.498) -- (2.30,0.413) -- (2.40,0.337) -- (2.50,0.271) -- (2.60,0.215) -- (2.70,0.168) -- (2.80,0.129) -- (2.90,0.098) -- (3.00,0.073) -- (3.10,0.054) -- (3.20,0.039) -- (3.30,0.028) -- (3.40,0.019) -- (3.50,0.013) -- (3.60,0.009) -- (3.70,0.006) -- (3.80,0.004) -- (3.90,0.003) -- (4.00,0.002) -- (4.10,0.001) -- (4.20,0.001) -- (4.30,0.000) -- (4.40,0.000) -- (4.50,0.000) -- (4.60,0.000) -- (4.70,0.000) -- (4.80,0.000) -- (4.90,0.000) -- (5.00,0.000) -- (5.10,0.000) -- (5.20,0.000) -- (5.30,0.000) -- (5.40,0.000) -- (5.50,0.000) -- (5.60,0.000) -- (5.70,0.000) -- (5.80,0.000) -- (5.90,0.000) -- (6.00,0.000) -- (6.10,0.000) -- (6.20,0.000) -- (6.30,0.000) -- (6.40,0.000) -- (6.50,0.000) -- (6.60,0.000) -- (6.70,0.000);
\draw (-1.50,0.000) -- (-1.40,0.000) -- (-1.30,0.000) -- (-1.20,0.000) -- (-1.10,0.000) -- (-1.00,0.000) -- (-0.90,0.000) -- (-0.80,0.000) -- (-0.70,0.000) -- (-0.60,0.000) -- (-0.50,0.000) -- (-0.40,0.000) -- (-0.30,0.000) -- (-0.20,0.000) -- (-0.10,0.000) -- (0.00,0.000) -- (0.10,0.000) -- (0.20,0.000) -- (0.30,0.000) -- (0.40,0.000) -- (0.50,0.000) -- (0.60,0.000) -- (0.70,0.000) -- (0.80,0.001) -- (0.90,0.001) -- (1.00,0.002) -- (1.10,0.003) -- (1.20,0.004) -- (1.30,0.006) -- (1.40,0.009) -- (1.50,0.013) -- (1.60,0.019) -- (1.70,0.028) -- (1.80,0.039) -- (1.90,0.054) -- (2.00,0.073) -- (2.10,0.098) -- (2.20,0.129) -- (2.30,0.168) -- (2.40,0.215) -- (2.50,0.271) -- (2.60,0.337) -- (2.70,0.413) -- (2.80,0.498) -- (2.90,0.591) -- (3.00,0.692) -- (3.10,0.798) -- (3.20,0.907) -- (3.30,1.015) -- (3.40,1.119) -- (3.50,1.215) -- (3.60,1.300) -- (3.70,1.370) -- (3.80,1.422) -- (3.90,1.455) -- (4.00,1.466) -- (4.10,1.455) -- (4.20,1.422) -- (4.30,1.370) -- (4.40,1.300) -- (4.50,1.215) -- (4.60,1.119) -- (4.70,1.015) -- (4.80,0.907) -- (4.90,0.798) -- (5.00,0.692) -- (5.10,0.591) -- (5.20,0.498) -- (5.30,0.413) -- (5.40,0.337) -- (5.50,0.271) -- (5.60,0.215) -- (5.70,0.168) -- (5.80,0.129) -- (5.90,0.098) -- (6.00,0.073) -- (6.10,0.054) -- (6.20,0.039) -- (6.30,0.028) -- (6.40,0.019) -- (6.50,0.013) -- (6.60,0.009) -- (6.70,0.006);
\draw[hl] (-1.50,0.000) -- (-1.40,0.000) -- (-1.30,0.000) -- (-1.20,0.000) -- (-1.10,0.000) -- (-1.00,0.000) -- (-0.90,0.000) -- (-0.80,0.000) -- (-0.70,0.000) -- (-0.60,0.000) -- (-0.50,0.000) -- (-0.40,0.000) -- (-0.30,0.000) -- (-0.20,0.000) -- (-0.10,0.000) -- (0.00,0.000) -- (0.10,0.000) -- (0.20,0.000) -- (0.30,0.000) -- (0.40,0.000) -- (0.50,0.000) -- (0.60,0.000) -- (0.70,0.001) -- (0.80,0.001) -- (0.90,0.002) -- (1.00,0.003) -- (1.10,0.004) -- (1.20,0.006) -- (1.30,0.010) -- (1.40,0.015) -- (1.50,0.024) -- (1.60,0.038) -- (1.70,0.059) -- (1.80,0.090) -- (1.90,0.139) -- (2.00,0.210) -- (2.10,0.312) -- (2.20,0.453) -- (2.30,0.636) -- (2.40,0.857) -- (2.50,1.100) -- (2.60,1.343) -- (2.70,1.564) -- (2.80,1.747) -- (2.90,1.888) -- (3.00,1.990) -- (3.10,2.061) -- (3.20,2.110) -- (3.30,2.141) -- (3.40,2.162) -- (3.50,2.176) -- (3.60,2.185) -- (3.70,2.190) -- (3.80,2.194) -- (3.90,2.196) -- (4.00,2.197) -- (4.10,2.198) -- (4.20,2.199) -- (4.30,2.199) -- (4.40,2.200) -- (4.50,2.200) -- (4.60,2.200) -- (4.70,2.200) -- (4.80,2.200) -- (4.90,2.200) -- (5.00,2.200) -- (5.10,2.200) -- (5.20,2.200) -- (5.30,2.200) -- (5.40,2.200) -- (5.50,2.200) -- (5.60,2.200) -- (5.70,2.200) -- (5.80,2.200) -- (5.90,2.200) -- (6.00,2.200) -- (6.10,2.200) -- (6.20,2.200) -- (6.30,2.200) -- (6.40,2.200) -- (6.50,2.200) -- (6.60,2.200) -- (6.70,2.200) node[lab,emph,anchor=west] {$p(y=1\mid x)$};
\node[hollow dot] at (0,0) {};
\node[hollow dot] at (1,0) {};
\node[hollow dot] at (2,0) {};
\node[hl dot] at (3,0) {};
\node[hl dot] at (4,0) {};
\node[hl dot] at (5,0) {};
\draw[tick] (2.5,0) -- (2.5,-0.12) node[lab,anchor=north] {$2.5$};
\end{tikzpicture}
\end{center}
```

@exm-gda-one-dimension: the fitted class densities (class $0$ faint, class $1$ plain), each weighted by $\phi=\tfrac12$, and the logistic posterior $p(y=1\mid x)=\sigma(4.5x-11.25)$ (scaled), which crosses $\tfrac12$ at $x=2.5$.

:::

::: {#rmk-gda-vs-logistic .remark name="GDA or logistic regression?"}

@thm-gda-logistic-posterior shows that GDA's assumptions imply a logistic posterior, but not conversely: Poisson class conditionals, for example, also give a logistic posterior. So GDA makes the stronger assumption. When the inputs really are Gaussian with a shared covariance, GDA uses the data more efficiently (it is asymptotically the best classifier and needs fewer examples). When they are not, logistic regression, which assumes only the form of $p(y\mid\mathbf{x})$, is more robust and is usually preferred with plenty of data. Giving each class its own covariance $\Sigma_k$ makes the boundary quadratic.

:::
