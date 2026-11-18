---
title: "Gradient Descent"
sources: [cs221-2, cs221-3]
requires: [ai/machine-learning/linear-regression]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lectures 2 and 3 (gradient descent), in our own wording. The descent lemma and its corollary are our own addition, to make the remark "converges for small enough learning rates" precise; proofs written out in steps. -->

The gradient $\nabla\text{TrainLoss}(\theta)$ points in the direction in which the training loss increases fastest (@sec-math-calculus-multivariable-differentiation-gradient). Gradient descent repeatedly takes a small step the other way.

::: {#def-gradient-descent .definition name="Gradient descent"}

Given a differentiable function $F:\mathbb{R}^p\to\mathbb{R}$ (here $F=\text{TrainLoss}$), an initial point $\theta_0$ and a *learning rate* (step size) $\eta>0$, *gradient descent* produces

$$
\theta_{t+1}=\theta_t-\eta\,\nabla F(\theta_t),\qquad t=0,1,2,\dots
$$

and stops after a fixed number $T$ of steps, or when the gradient is small.

:::

```{=latex}
\begin{algorithm}
\caption{Gradient descent}
\begin{algorithmic}
\INPUT Training data $\mathcal D$, initial parameters $\theta$, learning rate $\eta$, number of steps $T$
\OUTPUT Parameters $\theta$
\FOR{$t=1$ \TO $T$}
    \STATE $\mathbf{g}\gets\frac{1}{\lvert\mathcal D\rvert}\sum_{(x,y)\in\mathcal D}\nabla_\theta\text{Loss}(x,y,\theta)$
    \STATE $\theta\gets\theta-\eta\,\mathbf{g}$
\ENDFOR
\RETURN $\theta$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-gradient-descent-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (5,0) node[lab,anchor=north east] {step $t$};
\draw[->] (0,0) -- (0,3.1) node[lab,anchor=north west] {$\text{TrainLoss}(\theta_t)$};
\foreach \t in {0,2,4,6,8,10} { \node[lab,tick] at ({\t*0.45},-0.25) {\t}; }
\foreach \y in {5,10,15,20} { \node[lab,tick] at (-0.3,{\y*0.12}) {\y}; }
\draw[hl] plot coordinates {(0.00,2.80) (0.45,2.03) (0.90,1.48) (1.35,1.09) (1.80,0.81) (2.25,0.61) (2.70,0.47) (3.15,0.37) (3.60,0.30) (4.05,0.25) (4.50,0.21)};
\node[dot] at (0.00,2.80) {}; \node[dot] at (0.45,2.03) {}; \node[dot] at (0.90,1.48) {}; \node[dot] at (1.35,1.09) {}; \node[dot] at (1.80,0.81) {}; \node[dot] at (2.25,0.61) {}; \node[dot] at (2.70,0.47) {}; \node[dot] at (3.15,0.37) {}; \node[dot] at (3.60,0.30) {}; \node[dot] at (4.05,0.25) {}; \node[dot] at (4.50,0.21) {};
\end{tikzpicture}
\end{center}
```

Learning curve of gradient descent on the data of @exm-linear-regression-1, from $(w,b)=(0,1)$ with $\eta=0.01$: the training loss falls from $23.33$ to $1.75$ in ten steps (the minimum is $0.21$).

:::

The learning rate trades speed against stability: a small $\eta$ makes slow progress, and a large one overshoots, so that the loss oscillates or diverges. The next theorem says how small is small enough.

::: {#thm-descent-lemma .theorem name="Descent lemma"}

Suppose $\nabla F$ is $L$-Lipschitz: $\lVert\nabla F(\mathbf{u})-\nabla F(\mathbf{v})\rVert\le L\lVert\mathbf{u}-\mathbf{v}\rVert$ for all $\mathbf{u},\mathbf{v}$. If $0<\eta\le1/L$, then one step of gradient descent satisfies

$$
F(\theta-\eta\nabla F(\theta))\ \le\ F(\theta)-\frac{\eta}{2}\,\lVert\nabla F(\theta)\rVert^2 .
$$

:::

::: {.proof}

1. Write $\mathbf{g}=\nabla F(\theta)$ and $\mathbf{d}=-\eta\mathbf{g}$. The function $\phi(s)=F(\theta+s\mathbf{d})$ has $\phi'(s)=\nabla F(\theta+s\mathbf{d})\cdot\mathbf{d}$, so
$$
F(\theta+\mathbf{d})-F(\theta)=\int_0^1\nabla F(\theta+s\mathbf{d})\cdot\mathbf{d}\,ds .
$$

2. Split the integrand as $\mathbf{g}\cdot\mathbf{d}+\bigl(\nabla F(\theta+s\mathbf{d})-\mathbf{g}\bigr)\cdot\mathbf{d}$. By the Cauchy–Schwarz inequality and the Lipschitz condition, the second term is at most $Ls\lVert\mathbf{d}\rVert^2$.

3. Integrating over $s\in[0,1]$,
$$
F(\theta+\mathbf{d})-F(\theta)\le\mathbf{g}\cdot\mathbf{d}+\frac{L}{2}\lVert\mathbf{d}\rVert^2=-\eta\lVert\mathbf{g}\rVert^2+\frac{L\eta^2}{2}\lVert\mathbf{g}\rVert^2 .
$$

4. Since $L\eta\le1$, the right side is at most $-\eta\lVert\mathbf{g}\rVert^2+\frac{\eta}{2}\lVert\mathbf{g}\rVert^2=-\frac{\eta}{2}\lVert\mathbf{g}\rVert^2$.

:::

::: {#cor-gradient-descent-stationary .corollary name="Gradient descent finds small gradients"}

Under the hypotheses of @thm-descent-lemma, if $F$ is bounded below by $F^*$, then the iterates of gradient descent satisfy

$$
\min_{0\le t<T}\lVert\nabla F(\theta_t)\rVert^2\ \le\ \frac{2\,\bigl(F(\theta_0)-F^*\bigr)}{\eta\,T}.
$$

:::

::: {.proof}

1. By @thm-descent-lemma, $\frac{\eta}{2}\lVert\nabla F(\theta_t)\rVert^2\le F(\theta_t)-F(\theta_{t+1})$ for every $t$.

2. Summing over $t=0,\dots,T-1$, the right sides telescope to $F(\theta_0)-F(\theta_T)\le F(\theta_0)-F^*$.

3. The left side is at least $T\cdot\frac{\eta}{2}\min_t\lVert\nabla F(\theta_t)\rVert^2$; dividing by $T\eta/2$ gives the bound.

:::

::: {#rmk-gradient-descent-1 .remark name="Convex and non-convex losses"}

The corollary only promises a point where the gradient is nearly zero. For a convex training loss, such as the squared loss of linear regression or the logistic loss, every such point is nearly a global minimum, so gradient descent with a small enough learning rate converges to the minimum value. For neural networks the training loss is not convex and there is no such guarantee, although gradient descent works well in practice. On the data of @exm-linear-regression-1 the gradient of the training loss is Lipschitz with $L\approx15.6$ (the largest eigenvalue of its constant Hessian), so any $\eta\le0.064$ is safe.

:::

::: {#def-stochastic-gradient-descent .definition name="Stochastic gradient descent"}

*Stochastic gradient descent* (SGD) replaces the full gradient in each step by the average gradient over a *minibatch* $B\subseteq\mathcal D$ drawn at random (in the extreme, a single example):

$$
\theta\gets\theta-\eta\,\frac{1}{\lvert B\rvert}\sum_{(x,y)\in B}\nabla_\theta\text{Loss}(x,y,\theta).
$$

The minibatch gradient is an unbiased estimate of $\nabla\text{TrainLoss}(\theta)$ and costs $\lvert B\rvert$ instead of $\lvert\mathcal D\rvert$ gradient evaluations.

:::

```{=latex}
\begin{algorithm}
\caption{Stochastic gradient descent}
\begin{algorithmic}
\INPUT Training data $\mathcal D$, initial parameters $\theta$, learning rate $\eta$, batch size $m$, number of steps $T$
\OUTPUT Parameters $\theta$
\FOR{$t=1$ \TO $T$}
    \STATE $B\gets$ $m$ examples drawn at random from $\mathcal D$
    \STATE $\theta\gets\theta-\eta\,\frac{1}{m}\sum_{(x,y)\in B}\nabla_\theta\text{Loss}(x,y,\theta)$
\ENDFOR
\RETURN $\theta$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-gradient-descent-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0.5) -- (4.3,0.5) node[lab,anchor=north east] {$w$};
\draw[->] (0,0.5) -- (0,4.0) node[lab,anchor=north west] {$b$};
\foreach \w in {1,2} { \node[lab,tick] at ({\w*1.6},0.25) {\w}; }
\foreach \b in {1,2,3} { \node[lab,tick] at (-0.25,{\b*1.0}) {\b}; }
\draw[faint] (0.00,1.00) -- (3.84,1.60) -- (3.71,1.56) -- (3.65,1.54) -- (3.68,1.56) -- (3.70,1.57) -- (3.72,1.58) -- (3.73,1.59) -- (3.74,1.60) -- (3.75,1.61) -- (1.20,1.21) -- (2.25,1.54) -- (2.14,1.52) -- (2.72,1.70) -- (3.01,1.79) -- (1.53,1.56) -- (2.56,1.72) -- (2.91,1.83) -- (3.08,1.88) -- (3.17,1.91) -- (1.36,1.63) -- (1.60,1.78) -- (2.38,1.90) -- (1.84,1.81) -- (2.00,1.92) -- (2.51,2.08) -- (1.65,1.94) -- (2.29,2.14) -- (2.36,2.18) -- (1.67,2.08) -- (2.15,2.15);
\draw[hl] (0.00,1.00) -- (1.97,1.47) -- (2.39,1.60) -- (2.47,1.66) -- (2.47,1.70) -- (2.45,1.74) -- (2.43,1.77) -- (2.42,1.81) -- (2.40,1.84) -- (2.38,1.87) -- (2.36,1.90) -- (2.34,1.94) -- (2.33,1.97) -- (2.31,2.00) -- (2.29,2.03) -- (2.28,2.06) -- (2.26,2.09) -- (2.25,2.11) -- (2.23,2.14) -- (2.22,2.17) -- (2.20,2.20) -- (2.19,2.22) -- (2.17,2.25) -- (2.16,2.27) -- (2.15,2.30) -- (2.13,2.32) -- (2.12,2.34) -- (2.11,2.37) -- (2.10,2.39) -- (2.08,2.41) -- (2.07,2.43);
\node[dot] at (0,1) {};
\node[hl dot] at (1.49,3.50) {};
\node[lab,anchor=west] at (1.59,3.50) {minimizer};
\node[lab,anchor=west] at (2.6,1.2) {GD (solid), SGD (faint)};
\end{tikzpicture}
\end{center}
```

Thirty steps in parameter space on the data of @exm-linear-regression-1 from $(w,b)=(0,1)$: gradient descent with $\eta=0.05$ (solid) and stochastic gradient descent with one random example per step and $\eta=0.05$ (faint), which zigzags around the same path. Both head towards the minimizer $(\frac{13}{14},\frac72)$ along a long, flat valley of the loss.

:::

::: {#rmk-gradient-descent-2 .remark name="Other optimizers"}

Deep learning mostly uses refinements of SGD that adapt the step for each parameter, such as Adam, or that orthogonalize the update of each weight matrix, such as Muon. They share the outline above: estimate a gradient on a minibatch, then step against it.

:::
