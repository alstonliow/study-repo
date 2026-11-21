---
title: "Support Vector Machines: Margins and the Dual"
sources: [cs229-6]
requires: [ai/kernel-methods/kernels, math/optimization/duality/kkt-conditions]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS229 lecture notes (version of 23 August 2026), Chapter 6.1-6.6 (functional and geometric margins, the optimal margin classifier, its dual, support vectors, kernelized prediction), in our own wording. The same problem appears in convex-optimization form in @sec-math-optimization-applications-linear-discrimination (EE364A), where its dual is derived for the robust separation problem; this note follows CS229's labels-and-margins view and links that note instead of repeating it. The numerical example is our own, solved exactly and checked in Python. Proofs written out in steps. -->

Logistic regression is confident about a point when its logit is far from $0$. A support vector machine (SVM) makes this the training goal: find the linear boundary that keeps every training point as far from it as possible.

::: {#def-svm-margins .definition name="Functional and geometric margins"}

Use labels $y\in\{-1,+1\}$ and a linear classifier $h(\mathbf{x})=\operatorname{sign}(\mathbf{w}^{\mathsf T}\mathbf{x}+b)$. For a training example $(\mathbf{x}^{(i)},y^{(i)})$,

- the *functional margin* is $\hat\gamma^{(i)}=y^{(i)}(\mathbf{w}^{\mathsf T}\mathbf{x}^{(i)}+b)$, the margin of @def-margin;
- the *geometric margin* is $\gamma^{(i)}=\hat\gamma^{(i)}/\lVert\mathbf{w}\rVert$.

The margins of a training set are the smallest ones, $\hat\gamma=\min_i\hat\gamma^{(i)}$ and $\gamma=\min_i\gamma^{(i)}$. Scaling $(\mathbf{w},b)$ by $c>0$ multiplies $\hat\gamma$ by $c$ but leaves $\gamma$ and the classifier unchanged.

:::

::: {#prp-geometric-margin-distance .proposition name="The geometric margin is a distance"}

If $\mathbf{w}\ne\mathbf{0}$, the distance from $\mathbf{x}^{(i)}$ to the hyperplane $\{\mathbf{x}:\mathbf{w}^{\mathsf T}\mathbf{x}+b=0\}$ is $\lvert\mathbf{w}^{\mathsf T}\mathbf{x}^{(i)}+b\rvert/\lVert\mathbf{w}\rVert$. So $\gamma^{(i)}$ is this distance when the point is classified correctly and minus it otherwise.

:::

::: {.proof}

1. The closest point of the hyperplane to $\mathbf{x}^{(i)}$ is $\mathbf{x}^{(i)}-t\,\mathbf{w}/\lVert\mathbf{w}\rVert$ for the $t$ that puts it on the hyperplane, because the hyperplane's normal direction is $\mathbf{w}$.

2. Solving $\mathbf{w}^{\mathsf T}\bigl(\mathbf{x}^{(i)}-t\,\mathbf{w}/\lVert\mathbf{w}\rVert\bigr)+b=0$ gives $t=(\mathbf{w}^{\mathsf T}\mathbf{x}^{(i)}+b)/\lVert\mathbf{w}\rVert$, and the distance is $\lvert t\rvert$.

3. Multiplying $t$ by $y^{(i)}$ gives $\gamma^{(i)}$, which is positive exactly when the sign of $\mathbf{w}^{\mathsf T}\mathbf{x}^{(i)}+b$ matches the label.

:::

::: {#def-optimal-margin-classifier .definition name="Optimal margin classifier" related="def-max-margin-separation"}

For a linearly separable training set (@def-separable), the *optimal margin classifier* maximizes the geometric margin $\gamma$. Because the scale of $(\mathbf{w},b)$ is free, we may fix $\hat\gamma=1$; maximizing $\gamma=1/\lVert\mathbf{w}\rVert$ is then the convex quadratic program

$$
\begin{aligned}
\min_{\mathbf{w},b}\quad&\tfrac12\lVert\mathbf{w}\rVert^2\\
\text{subject to}\quad&y^{(i)}(\mathbf{w}^{\mathsf T}\mathbf{x}^{(i)}+b)\ge1,\quad i=1,\dots,N.
\end{aligned}
$$

:::

::: {#thm-svm-dual .theorem name="The SVM dual"}

The dual of the problem in @def-optimal-margin-classifier is

$$
\begin{aligned}
\max_{\boldsymbol\alpha}\quad&W(\boldsymbol\alpha)=\sum_{i=1}^N\alpha_i-\frac12\sum_{i,j=1}^Ny^{(i)}y^{(j)}\alpha_i\alpha_j\langle\mathbf{x}^{(i)},\mathbf{x}^{(j)}\rangle\\
\text{subject to}\quad&\alpha_i\ge0,\quad\sum_{i=1}^N\alpha_iy^{(i)}=0.
\end{aligned}
$$

Strong duality holds for separable data, and if $\boldsymbol\alpha^\star$ solves the dual, the optimal primal weights are

$$
\mathbf{w}^\star=\sum_{i=1}^N\alpha_i^\star y^{(i)}\mathbf{x}^{(i)},
$$

with $\alpha_i^\star>0$ only for points on the margin, $y^{(i)}(\mathbf{w}^{\star\mathsf T}\mathbf{x}^{(i)}+b^\star)=1$. The intercept is $b^\star=y^{(i)}-\mathbf{w}^{\star\mathsf T}\mathbf{x}^{(i)}$ for any $i$ with $\alpha_i^\star>0$.

:::

::: {.proof}

1. The Lagrangian (@def-lagrangian), with a multiplier $\alpha_i\ge0$ for each constraint $1-y^{(i)}(\mathbf{w}^{\mathsf T}\mathbf{x}^{(i)}+b)\le0$, is

   $$
   L(\mathbf{w},b,\boldsymbol\alpha)=\tfrac12\lVert\mathbf{w}\rVert^2-\sum_i\alpha_i\bigl(y^{(i)}(\mathbf{w}^{\mathsf T}\mathbf{x}^{(i)}+b)-1\bigr).
   $$

2. The dual function is $\inf_{\mathbf{w},b}L$. $L$ is linear in $b$ with coefficient $-\sum_i\alpha_iy^{(i)}$, so the infimum is $-\infty$ unless $\sum_i\alpha_iy^{(i)}=0$.

3. When it is $0$, $L$ is a convex quadratic in $\mathbf{w}$ with gradient $\mathbf{w}-\sum_i\alpha_iy^{(i)}\mathbf{x}^{(i)}$, minimized at $\mathbf{w}=\sum_i\alpha_iy^{(i)}\mathbf{x}^{(i)}$.

4. Substituting, $\tfrac12\lVert\mathbf{w}\rVert^2-\mathbf{w}^{\mathsf T}\sum_i\alpha_iy^{(i)}\mathbf{x}^{(i)}=-\tfrac12\lVert\mathbf{w}\rVert^2=-\tfrac12\sum_{i,j}y^{(i)}y^{(j)}\alpha_i\alpha_j\langle\mathbf{x}^{(i)},\mathbf{x}^{(j)}\rangle$, so the dual function is $W(\boldsymbol\alpha)$, giving the dual problem.

5. For separable data, some $(\mathbf{w},b)$ has all functional margins positive; scaling it makes every constraint hold strictly. The constraints are affine, so Slater's condition holds (@thm-slater) and strong duality holds.

6. By the KKT conditions (@thm-kkt), a primal optimum $(\mathbf{w}^\star,b^\star)$ and dual optimum $\boldsymbol\alpha^\star$ satisfy stationarity, which is step 3, and complementary slackness (@prp-complementary-slackness): $\alpha_i^\star\bigl(y^{(i)}(\mathbf{w}^{\star\mathsf T}\mathbf{x}^{(i)}+b^\star)-1\bigr)=0$. So $\alpha_i^\star>0$ forces the constraint to be tight, and then $y^{(i)}\in\{\pm1\}$ gives $b^\star=y^{(i)}-\mathbf{w}^{\star\mathsf T}\mathbf{x}^{(i)}$.

7. Some $\alpha_i^\star$ is positive: otherwise $\mathbf{w}^\star=\mathbf{0}$, which violates the constraints of the two classes (with both classes present).

:::

::: {#def-support-vectors .definition name="Support vectors"}

The training points with $\alpha_i^\star>0$ are the *support vectors*. They lie on the margin, and by @thm-svm-dual the classifier depends only on them: moving or deleting any other point (without crossing the margin) does not change it.

:::

::: {#exm-svm-three-points .example name="Three points in the plane"}

Take positive points $\mathbf{x}^{(1)}=(2,2)$, $\mathbf{x}^{(2)}=(3,0)$ and a negative point $\mathbf{x}^{(3)}=(0,0)$. The dual solution is

$$
\alpha_1^\star=\tfrac16,\quad\alpha_2^\star=\tfrac19,\quad\alpha_3^\star=\tfrac5{18}
$$

(check: $\alpha_1+\alpha_2=\alpha_3$), so $\mathbf{w}^\star=\tfrac16(2,2)+\tfrac19(3,0)=\bigl(\tfrac23,\tfrac13\bigr)$ and, from the negative point, $b^\star=-1-0=-1$. All three functional margins equal $1$: $\tfrac43+\tfrac23-1$, $2-1$ and $-(0-1)$. All three points are support vectors, the boundary is $2x_1+x_2=3$, and the geometric margin is $1/\lVert\mathbf{w}^\star\rVert=3/\sqrt5\approx1.342$. The primal and dual values agree: $\tfrac12\lVert\mathbf{w}^\star\rVert^2=\tfrac5{18}=\sum_i\alpha_i^\star-\tfrac12\lVert\mathbf{w}^\star\rVert^2$.

:::

::: {#fig-support-vector-machines-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[->] (-0.5,0) -- (3.8,0) node[lab,anchor=west] {$x_1$};
\draw[->] (0,-0.5) -- (0,3.4) node[lab,anchor=south] {$x_2$};
\draw[hl] (-0.1,3.2) -- (1.75,-0.5);
\draw[faint] (-0.5,1.0) -- (0.25,-0.5);
\draw[faint] (1.4,3.2) -- (3.25,-0.5);
\node[hl dot] at (2,2) {};
\node[lab,tick,anchor=south west] at (2,2) {$(2,2)$};
\node[hl dot] at (3,0) {};
\node[lab,tick,anchor=south west] at (3,0) {$(3,0)$};
\node[hollow dot] at (0,0) {};
\node[lab,tick,anchor=south west] at (0,0) {$(0,0)$};
\node[lab,emph,anchor=west] at (1.0,1.2) {$2x_1+x_2=3$};
\end{tikzpicture}
\end{center}
```

The optimal margin classifier of @exm-svm-three-points (filled: $+1$, hollow: $-1$). The boundary $2x_1+x_2=3$ lies halfway between the margin lines $2x_1+x_2=0$ and $2x_1+x_2=6$, and all three points are support vectors.

:::

::: {#rmk-svm-kernelized .remark name="Kernelized SVMs"}

Both the dual objective and the prediction

$$
\mathbf{w}^{\star\mathsf T}\mathbf{x}+b^\star=\sum_{i=1}^N\alpha_i^\star y^{(i)}\langle\mathbf{x}^{(i)},\mathbf{x}\rangle+b^\star
$$

use the inputs only through inner products. Replacing every $\langle\mathbf{x},\mathbf{z}\rangle$ by a kernel $K(\mathbf{x},\mathbf{z})$ (@def-kernel-function) trains the optimal margin classifier in the feature space of $K$, which may be infinite-dimensional, while solving a problem with only $N$ variables; prediction sums over the support vectors only. With the Gaussian kernel the boundary in input space can be any smooth curve. Data that are not separable need the soft margin of @sec-ai-kernel-methods-soft-margin-svm.

:::
