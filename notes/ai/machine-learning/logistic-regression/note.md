---
title: "Logistic Regression"
sources: [cs221-3]
requires: [ai/machine-learning/linear-classification, ai/machine-learning/gradient-descent]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 3 (logistic function, logistic loss, gradient descent), in our own wording. The convexity proposition is our own addition; proofs written out in steps. -->

To get useful gradients, the classifier outputs a probability for each label instead of a hard label, and the loss rewards giving the correct label high probability.

::: {#def-logistic-function .definition name="Logistic function"}

The *logistic* (sigmoid) function $\sigma:\mathbb{R}\to(0,1)$ is

$$
\sigma(z)=\frac{1}{1+e^{-z}}.
$$

:::

::: {#fig-logistic-regression-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-3.4,0) -- (3.4,0) node[lab, right] {$z$};
\draw[->] (0,0) -- (0,2.4) node[lab, above] {};
\draw[emph, domain=-3.2:3.2, samples=80, smooth, variable=\x] plot ({\x}, {2/(1+exp(-1.5*\x))});
\draw[faint, dashed] (-3.2,2) -- (3.2,2);
\draw (0,1) -- (-0.08,1) node[tick, left] {$\tfrac12$};
\draw (0,2) -- (-0.08,2) node[tick, left] {$1$};
\end{tikzpicture}
\end{center}
```

The logistic function $\sigma(z)=1/(1+e^{-z})$ squashes any real score into $(0,1)$; $\sigma(0)=\tfrac12$ and $\sigma(-z)=1-\sigma(z)$

:::

::: {#prp-logistic-function .proposition name="Properties of the logistic function"}

1. $\sigma$ is increasing, with $\sigma(z)\to0$ as $z\to-\infty$, $\sigma(0)=\tfrac12$ and $\sigma(z)\to1$ as $z\to\infty$.
2. $\sigma(z)+\sigma(-z)=1$.
3. If $p=\sigma(z)$ then $z=\log\dfrac{p}{1-p}$ (the *log odds* of $p$).
4. $\sigma'(z)=\sigma(z)\bigl(1-\sigma(z)\bigr)=\sigma(z)\,\sigma(-z)$, which tends to $0$ as $\lvert z\rvert\to\infty$.

:::

::: {.proof}

1. As $z$ increases, $e^{-z}$ decreases from $\infty$ to $0$, so $1+e^{-z}$ decreases from $\infty$ to $1$ and $\sigma(z)$ increases from $0$ to $1$; at $z=0$ it is $\tfrac1{1+1}$.

2. $\sigma(-z)=\dfrac{1}{1+e^{z}}=\dfrac{e^{-z}}{e^{-z}+1}$, and adding $\dfrac{1}{1+e^{-z}}$ gives $1$.

3. From $p(1+e^{-z})=1$ we get $e^{-z}=\dfrac{1-p}{p}$, so $z=\log\dfrac{p}{1-p}$.

4. By the chain rule $\sigma'(z)=\dfrac{e^{-z}}{(1+e^{-z})^2}=\sigma(z)\cdot\dfrac{e^{-z}}{1+e^{-z}}=\sigma(z)\,\sigma(-z)$, and $\sigma(-z)=1-\sigma(z)$ by part 2. One of the two factors tends to $0$ as $\lvert z\rvert\to\infty$ and the other stays below $1$.

:::

::: {#def-logistic-regression .definition name="Logistic model, logistic loss"}

The *logistic regression* model for labels $y\in\{-1,+1\}$ turns the logit into probabilities

$$
p_\theta(y=+1\mid\mathbf{x})=\sigma(\mathbf{w}\cdot\mathbf{x}+b),\qquad p_\theta(y=-1\mid\mathbf{x})=\sigma\bigl(-(\mathbf{w}\cdot\mathbf{x}+b)\bigr),
$$

that is, $p_\theta(y\mid\mathbf{x})=\sigma\bigl(y\,(\mathbf{w}\cdot\mathbf{x}+b)\bigr)$, a function of the margin $m=y\,(\mathbf{w}\cdot\mathbf{x}+b)$. Its loss is the *logistic loss*

$$
\text{Loss}(\mathbf{x},y,\theta)=-\log\sigma(m)=\log\bigl(1+e^{-m}\bigr).
$$

:::

::: {#rmk-logistic-regression-1 .remark name="Maximum likelihood"}

The loss comes from the *maximum likelihood* principle: choose $\theta$ so that the model gives the observed training labels the highest probability. Treating examples as independent, that probability is $\prod_{(\mathbf{x},y)\in\mathcal D}p_\theta(y\mid\mathbf{x})$. Maximizing it is the same as maximizing the sum of logarithms, and negating that sum (and dividing by $\lvert\mathcal D\rvert$) gives the training logistic loss. The logistic loss decreases smoothly in the margin and tends to $0$ as the margin grows, whereas the zero-one loss jumps at margin $0$ (@fig-logistic-regression-1).

:::

::: {#fig-logistic-regression-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-3.3,0) -- (3.4,0) node[lab,anchor=north east] {margin $m$};
\draw[->] (0,0) -- (0,2.7) node[lab,anchor=north west] {loss};
\foreach \m in {-3,-2,-1,1,2,3} { \node[lab,tick] at (\m,-0.25) {\m}; }
\node[lab,tick] at (-0.25,0.8) {1};
\draw[faint] (-3,0.8) -- (0,0.8);
\draw[faint] (0,0) -- (3,0);
\node[hollow dot] at (0,0) {}; \node[dot] at (0,0.8) {};
\draw[hl] plot coordinates {(-3.00,2.439) (-2.75,2.250) (-2.50,2.063) (-2.25,1.880) (-2.00,1.702) (-1.75,1.528) (-1.50,1.361) (-1.25,1.202) (-1.00,1.051) (-0.75,0.909) (-0.50,0.779) (-0.25,0.661) (0.00,0.555) (0.25,0.461) (0.50,0.379) (0.75,0.309) (1.00,0.251) (1.25,0.202) (1.50,0.161) (1.75,0.128) (2.00,0.102) (2.25,0.080) (2.50,0.063) (2.75,0.050) (3.00,0.039)};
\node[lab,anchor=west] at (-1.2,1.9) {logistic $\log(1+e^{-m})$};
\node[lab,anchor=south] at (-2.0,0.8) {zero-one};
\end{tikzpicture}
\end{center}
```

Zero-one loss and logistic loss as functions of the margin. The zero-one loss is flat except for a jump at $0$; the logistic loss decreases smoothly and is $\log2\approx0.69$ at $m=0$.

:::

::: {#thm-logistic-loss-gradient .theorem name="Gradient of the logistic loss"}

With margin $m=y\,(\mathbf{w}\cdot\mathbf{x}+b)$,

$$
\nabla_{\mathbf{w}}\text{Loss}(\mathbf{x},y,\theta)=-\sigma(-m)\,y\,\mathbf{x},\qquad
\frac{\partial}{\partial b}\text{Loss}(\mathbf{x},y,\theta)=-\sigma(-m)\,y .
$$

:::

::: {.proof}

1. As a function of $m$, $\text{Loss}=-\log\sigma(m)$, so by @prp-logistic-function (part 4)
$$
\frac{d\,\text{Loss}}{dm}=-\frac{\sigma'(m)}{\sigma(m)}=-\frac{\sigma(m)\sigma(-m)}{\sigma(m)}=-\sigma(-m).
$$

2. The margin is linear in the parameters, with $\nabla_{\mathbf{w}}m=y\,\mathbf{x}$ and $\partial m/\partial b=y$.

3. The chain rule multiplies the two.

:::

The factor $\sigma(-m)\in(0,1)$ is the probability the model gives to the wrong label: an example that is already classified correctly with confidence contributes almost nothing, and a wrongly classified one pulls $\mathbf{w}$ towards $y\,\mathbf{x}$.

::: {#prp-logistic-loss-convex .proposition name="The logistic loss is convex"}

For every example, $\theta\mapsto\text{Loss}(\mathbf{x},y,\theta)$ is convex, and so is the training logistic loss.

:::

::: {.proof}

1. Let $\ell(m)=\log(1+e^{-m})$. By step 1 of the previous proof $\ell'(m)=-\sigma(-m)$, so $\ell''(m)=\sigma'(-m)=\sigma(-m)\sigma(m)>0$, and $\ell$ is convex.

2. The margin $m$ is an affine function of $\theta=(\mathbf{w},b)$, and a convex function of an affine function is convex: for $\theta_\lambda=\lambda\theta_1+(1-\lambda)\theta_2$ the margin is $\lambda m_1+(1-\lambda)m_2$, so $\ell(m(\theta_\lambda))\le\lambda\ell(m_1)+(1-\lambda)\ell(m_2)$.

3. An average of convex functions is convex.

:::

```{=latex}
\begin{algorithm}
\caption{Logistic regression by gradient descent}
\begin{algorithmic}
\INPUT Training data $\mathcal D$ with labels $\pm1$, learning rate $\eta$, number of steps $T$
\OUTPUT Parameters $(\mathbf{w},b)$
\STATE $\mathbf{w}\gets\mathbf{0}$; $b\gets0$
\FOR{$t=1$ \TO $T$}
    \STATE $c(\mathbf{x},y)\gets-\sigma\bigl(-y(\mathbf{w}\cdot\mathbf{x}+b)\bigr)\,y$ for each $(\mathbf{x},y)\in\mathcal D$
    \STATE $\mathbf{w}\gets\mathbf{w}-\eta\,\frac{1}{\lvert\mathcal D\rvert}\sum_{(\mathbf{x},y)}c(\mathbf{x},y)\,\mathbf{x}$; \quad $b\gets b-\eta\,\frac{1}{\lvert\mathcal D\rvert}\sum_{(\mathbf{x},y)}c(\mathbf{x},y)$
\ENDFOR
\RETURN $(\mathbf{w},b)$
\end{algorithmic}
\end{algorithm}
```

::: {#exm-logistic-regression-1 .example name="Training on three points"}

On the data of @exm-linear-classification-1, gradient descent from $\mathbf{w}=\mathbf{0}$, $b=0$ with $\eta=1$ starts at training loss $\log2\approx0.693$ (every probability is $\tfrac12$). After one step $\mathbf{w}=(\tfrac16,-\tfrac13)$, $b=-\tfrac16$, and all three examples are already classified correctly. After $20$ steps $\mathbf{w}\approx(1.92,-1.78)$, $b\approx-1.51$ and the training loss is $0.111$. The training zero-one loss is $0$ but the logistic loss is not: it keeps decreasing as the margins grow, and it is $0$ only in the limit.

:::

::: {#fig-logistic-regression-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.9]
\draw[->] (-1,0) -- (3.5,0) node[lab,anchor=north east] {$x_1$};
\draw[->] (0,-1.5) -- (0,2.6) node[lab,anchor=north west] {$x_2$};
\draw[faint] (-1,-1.0) -- (3.5,1.25) node[lab,anchor=west] {step 1};
\draw[faint,dashed] (-0.7,-1.146) -- (3.5,2.323) node[lab,anchor=west] {step 5};
\draw[hl] (-0.5,-1.389) -- (3.2,2.601) node[lab,anchor=west] {step 20};
\node[hollow dot] at (1,2) {};
\node[hollow dot] at (0,0) {};
\node[dot] at (2,0) {};
\end{tikzpicture}
\end{center}
```

Decision boundaries during the run of @exm-logistic-regression-1 after $1$, $5$ and $20$ steps (filled point label $+1$, hollow points $-1$). The boundary settles between the classes as gradient descent increases the margins.

:::
