---
title: "Numerical Gradients and Gradient Checking"
sources: [cs231n-3, cs231n-7]
requires: [ai/deep-learning/backpropagation]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS231n course notes (Optimization: numerical and analytic gradients; Neural networks part 3: gradient checks), in our own wording; the error theorem is proved by Taylor expansion as our own proof; the example was computed in Python. -->

Backpropagation (@def-backpropagation) computes exact gradients fast, but its code is easy to get wrong. Finite differences compute gradients slowly from loss values alone, so comparing the two catches most bugs. The exercise @prob-backpropagation-gradient-check-code implements the numerical side.

::: {#def-numerical-gradient .definition name="Numerical gradient"}

For $f:\mathbb{R}^p\to\mathbb{R}$, a point $\boldsymbol\theta$, a step $h>0$ and the unit vectors $\mathbf{e}_i$, the *forward difference* and the *centred difference* approximations of $\partial f/\partial\theta_i$ are

$$
\frac{f(\boldsymbol\theta+h\mathbf{e}_i)-f(\boldsymbol\theta)}{h},\qquad \frac{f(\boldsymbol\theta+h\mathbf{e}_i)-f(\boldsymbol\theta-h\mathbf{e}_i)}{2h}.
$$

The *numerical gradient* collects one of them for $i=1,\dots,p$; it costs $p+1$ or $2p$ evaluations of $f$.

:::

::: {#thm-finite-difference-error .theorem name="Error of finite differences"}

Let $g(t)=f(\boldsymbol\theta+t\mathbf{e}_i)$ be three times continuously differentiable near $0$. Then, as $h\to0$,

$$
\frac{g(h)-g(0)}{h}=g'(0)+O(h),\qquad \frac{g(h)-g(-h)}{2h}=g'(0)+O(h^2).
$$

:::

::: {.proof}

1. By Taylor's theorem, $g(\pm h)=g(0)\pm hg'(0)+\tfrac{h^2}{2}g''(0)\pm\tfrac{h^3}{6}g'''(\xi_\pm)$ for some $\xi_\pm$ between $0$ and $\pm h$.
2. Forward difference: $\dfrac{g(h)-g(0)}{h}=g'(0)+\tfrac h2g''(0)+\tfrac{h^2}{6}g'''(\xi_+)$, so the error is $O(h)$, with leading term $\tfrac h2g''(0)$.
3. Centred difference: in $g(h)-g(-h)$ the even terms cancel, leaving $2hg'(0)+\tfrac{h^3}{6}\bigl(g'''(\xi_+)+g'''(\xi_-)\bigr)$. Dividing by $2h$ gives $g'(0)+O(h^2)$, since $g'''$ is bounded near $0$.

:::

::: {#exm-finite-difference-cube .example name="The derivative of a cube"}

For $g(t)=t^3$ at $t=1$, where $g'(1)=3$: with $h=10^{-2}$ the forward difference is $3.0301$ and the centred difference $3.0001$; with $h=10^{-4}$ they are $3.0003$ and $3.00000001$. The forward error falls by $100$ when $h$ does, the centred error by $10^4$.

:::

::: {#fig-gradient-checking-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[->] (0,0) -- (6.2,0) node[lab,anchor=west] {$-\log_{10}h$};
\draw[->] (0,0) -- (0,4.25) node[lab,anchor=south] {$\log_{10}$ error};
\draw[tick] (0,0.0) -- (-0.08,0.0) node[lab,anchor=east] {$-16$};
\draw[tick] (0,1.0) -- (-0.08,1.0) node[lab,anchor=east] {$-12$};
\draw[tick] (0,2.0) -- (-0.08,2.0) node[lab,anchor=east] {$-8$};
\draw[tick] (0,3.0) -- (-0.08,3.0) node[lab,anchor=east] {$-4$};
\draw[tick] (0,4.0) -- (-0.08,4.0) node[lab,anchor=east] {$0$};
\draw[tick] (0.4,0) -- (0.4,-0.08) node[lab,anchor=north] {$1$};
\draw[tick] (2.0,0) -- (2.0,-0.08) node[lab,anchor=north] {$5$};
\draw[tick] (4.0,0) -- (4.0,-0.08) node[lab,anchor=north] {$10$};
\draw[tick] (6.0,0) -- (6.0,-0.08) node[lab,anchor=north] {$15$};
\draw[faint] (0.400,3.873) -- (0.500,3.809) -- (0.600,3.745) -- (0.700,3.682) -- (0.800,3.620) -- (0.900,3.557) -- (1.000,3.494) -- (1.100,3.432) -- (1.200,3.369) -- (1.300,3.307) -- (1.400,3.244) -- (1.500,3.182) -- (1.600,3.119) -- (1.700,3.057) -- (1.800,2.994) -- (1.900,2.932) -- (2.000,2.869) -- (2.100,2.807) -- (2.200,2.744) -- (2.300,2.682) -- (2.400,2.619) -- (2.500,2.557) -- (2.600,2.494) -- (2.700,2.432) -- (2.800,2.370) -- (2.900,2.306) -- (3.000,2.250) -- (3.100,2.184) -- (3.200,1.900) -- (3.300,2.079) -- (3.400,2.254) -- (3.500,2.316) -- (3.600,2.349) -- (3.700,2.334) -- (3.800,2.430) -- (3.900,2.438) -- (4.000,2.349) -- (4.100,2.334) -- (4.200,2.709) -- (4.300,2.798) -- (4.400,2.349) -- (4.500,2.918) -- (4.600,2.972) -- (4.700,3.027) -- (4.800,3.107) -- (4.900,3.179) -- (5.000,3.134) -- (5.100,3.175) -- (5.200,3.345) -- (5.300,3.370) -- (5.400,3.486) -- (5.500,3.378) -- (5.600,3.345) -- (5.700,3.647) -- (5.800,3.677) -- (5.900,3.378) -- (6.000,3.880);
\draw[hl] (0.400,3.500) -- (0.500,3.375) -- (0.600,3.250) -- (0.700,3.125) -- (0.800,3.000) -- (0.900,2.875) -- (1.000,2.750) -- (1.100,2.625) -- (1.200,2.500) -- (1.300,2.375) -- (1.400,2.250) -- (1.500,2.125) -- (1.600,2.000) -- (1.700,1.875) -- (1.800,1.750) -- (1.900,1.623) -- (2.000,1.497) -- (2.100,1.445) -- (2.200,1.174) -- (2.300,1.446) -- (2.400,1.476) -- (2.500,1.500) -- (2.600,1.655) -- (2.700,1.694) -- (2.800,1.484) -- (2.900,1.737) -- (3.000,1.884) -- (3.100,1.772) -- (3.200,1.963) -- (3.300,2.008) -- (3.400,2.177) -- (3.500,2.238) -- (3.600,2.228) -- (3.700,2.334) -- (3.800,2.430) -- (3.900,2.438) -- (4.000,2.349) -- (4.100,2.334) -- (4.200,2.550) -- (4.300,2.698) -- (4.400,2.349) -- (4.500,2.811) -- (4.600,2.848) -- (4.700,2.884) -- (4.800,3.000) -- (4.900,3.088) -- (5.000,3.134) -- (5.100,3.175) -- (5.200,3.216) -- (5.300,2.963) -- (5.400,3.386) -- (5.500,3.378) -- (5.600,3.345) -- (5.700,3.488) -- (5.800,3.677) -- (5.900,3.378) -- (6.000,3.804);
\node[lab,anchor=west] at (1.20,3.57) {forward};
\node[lab,anchor=west] at (2.12,1.20) {centred};
\end{tikzpicture}
\end{center}
```

Error of the forward and centred differences for $g(t)=t^3$ at $t=1$ in double precision, against the step $h$. The truncation errors fall like $h$ and $h^2$ (slopes $1$ and $2$) until rounding error, which grows like $1/h$, takes over: near $h=10^{-8}$ for the forward and $h=10^{-5}$ for the centred difference.

:::

In floating point, $h$ cannot be taken arbitrarily small: the difference $f(\boldsymbol\theta+h\mathbf{e}_i)-f(\boldsymbol\theta-h\mathbf{e}_i)$ loses relative precision as $h$ shrinks. In double precision $h\approx10^{-5}$ is a common choice.

::: {#def-relative-error .definition name="Relative error of a gradient check"}

For an analytic gradient entry $a$ and a numerical one $n$, not both zero, the *relative error* is

$$
\frac{\lvert a-n\rvert}{\max(\lvert a\rvert,\lvert n\rvert)} .
$$

:::

An absolute difference means nothing without the scale of the gradient: $10^{-4}$ is excellent if the entries are about $1$ and useless if they are about $10^{-5}$. As rough guides in double precision with centred differences, relative errors below $10^{-7}$ indicate a correct gradient, around $10^{-4}$ call for a closer look unless the loss has kinks, and above $10^{-2}$ indicate a bug. Errors grow with depth, so a ten-layer network may legitimately show $10^{-2}$ in its first layers.

```{=latex}
\begin{algorithm}
\caption{Gradient check}
\begin{algorithmic}
\INPUT loss $f$, analytic gradient routine $\nabla f$, point $\boldsymbol\theta$, step $h$, number $m$ of coordinates
\OUTPUT largest relative error found
\STATE $\mathbf{a}\gets\nabla f(\boldsymbol\theta)$; $r\gets0$
\FOR{$m$ coordinates $i$ chosen at random}
    \STATE $n\gets\bigl(f(\boldsymbol\theta+h\mathbf{e}_i)-f(\boldsymbol\theta-h\mathbf{e}_i)\bigr)/(2h)$
    \STATE $r\gets\max\bigl(r,\ \lvert a_i-n\rvert/\max(\lvert a_i\rvert,\lvert n\rvert)\bigr)$
\ENDFOR
\RETURN $r$
\end{algorithmic}
\end{algorithm}
```

::: {#rmk-gradient-checking-1 .remark name="Practical rules for gradient checks"}

1. Use double precision and the centred formula.
2. *Kinks.* ReLU, max and the hinge loss (@def-multiclass-svm-loss) are not differentiable everywhere. If $\boldsymbol\theta\pm h\mathbf{e}_i$ straddles a kink, the numerical gradient mixes the two one-sided slopes and disagrees with the analytic one, without any bug. Using few data points makes crossing a kink less likely; one can also record whether any $\max$ changed its winner between the two evaluations.
3. Check with only a few examples and a few random coordinates per parameter tensor, which is cheap; make sure every tensor is checked.
4. Turn off randomness in the forward pass (dropout, data augmentation), or fix its seed, so that both evaluations compute the same function.
5. Check the data loss without regularization as well: a correct penalty term can hide a wrong data gradient that is small beside it.
6. Check after a short period of training too, not only at initialization, where special values (zero biases, symmetric weights) can hide errors.

:::

::: {#rmk-gradient-checking-2 .remark name="Sanity checks before training"}

Before a long run: with small random weights and $K$ classes, the cross entropy loss should start near $\log K$, since every class gets probability about $1/K$ ($\log10\approx2.303$ for ten classes); increasing the regularization strength should increase the loss; and the model should reach nearly zero loss on a tiny subset of the training data (say 20 examples) with regularization off. A model that cannot overfit a tiny subset has a bug.

:::
