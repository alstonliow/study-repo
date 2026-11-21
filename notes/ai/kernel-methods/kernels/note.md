---
title: "Feature Maps and Kernels"
sources: [cs229-5]
requires: [ai/deep-learning/neural-networks]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS229 lecture notes (version of 23 August 2026), Chapter 5 (feature maps, LMS with features, the kernel trick, properties of kernels and the positive semidefinite characterization), in our own wording. The proof of the characterization (the feature space spanned by the functions K(., x)) and the closure proof are our own; proofs written out in steps. -->

A linear model on a feature map $\phi(\mathbf{x})$ (@def-feature-map) can fit curved patterns, but $\phi(\mathbf{x})$ may be huge or infinite-dimensional. Often the learning algorithm needs only the inner products $\langle\phi(\mathbf{x}),\phi(\mathbf{z})\rangle$, and these can be cheap to compute directly.

::: {#def-kernel-function .definition name="Kernel"}

A function $K:\mathcal X\times\mathcal X\to\mathbb{R}$ on an input set $\mathcal X$ is a *kernel* if there are a real inner product space $\mathcal H$ (possibly infinite-dimensional) and a map $\phi:\mathcal X\to\mathcal H$ with

$$
K(\mathbf{x},\mathbf{z})=\langle\phi(\mathbf{x}),\phi(\mathbf{z})\rangle\qquad\text{for all }\mathbf{x},\mathbf{z}\in\mathcal X.
$$

For points $\mathbf{x}^{(1)},\dots,\mathbf{x}^{(N)}$, the $N\times N$ matrix with entries $K_{ij}=K(\mathbf{x}^{(i)},\mathbf{x}^{(j)})$ is their *kernel matrix* (Gram matrix).

:::

::: {#exm-kernel-polynomial .example name="Polynomial and Gaussian kernels"}

1. On $\mathbb{R}^d$, $K(\mathbf{x},\mathbf{z})=(\mathbf{x}^{\mathsf T}\mathbf{z})^2=\sum_{i,j}(x_ix_j)(z_iz_j)$, so $K$ is a kernel with $\phi(\mathbf{x})=(x_ix_j)_{i,j=1}^d\in\mathbb{R}^{d^2}$. For $\mathbf{x}=(1,2)$ and $\mathbf{z}=(3,1)$: $\phi(\mathbf{x})=(1,2,2,4)$, $\phi(\mathbf{z})=(9,3,3,1)$ and $\langle\phi(\mathbf{x}),\phi(\mathbf{z})\rangle=9+6+6+4=25=(3+2)^2$. The kernel costs $O(d)$ operations, the feature map $O(d^2)$.

2. More generally $K(\mathbf{x},\mathbf{z})=(\mathbf{x}^{\mathsf T}\mathbf{z}+c)^k$ with $c\ge0$ is a kernel whose features are all monomials of degree at most $k$, about $\binom{d+k}{k}$ of them, but it still costs $O(d)$.

3. The *Gaussian kernel* $K(\mathbf{x},\mathbf{z})=\exp\bigl(-\lVert\mathbf{x}-\mathbf{z}\rVert^2/(2\tau^2)\bigr)$ is a kernel (@prp-kernel-closure) with an infinite-dimensional feature space.

:::

::: {#thm-kernel-psd .theorem name="Kernels are exactly the positive semidefinite functions"}

A function $K:\mathcal X\times\mathcal X\to\mathbb{R}$ is a kernel if and only if, for every finite set of points $\mathbf{x}^{(1)},\dots,\mathbf{x}^{(N)}\in\mathcal X$, the kernel matrix is symmetric and positive semidefinite.

:::

::: {.proof}

*Only if.*

1. $K_{ij}=\langle\phi(\mathbf{x}^{(i)}),\phi(\mathbf{x}^{(j)})\rangle=K_{ji}$, so the matrix is symmetric.

2. For $\mathbf{c}\in\mathbb{R}^N$, $\mathbf{c}^{\mathsf T}K\mathbf{c}=\sum_{i,j}c_ic_j\langle\phi(\mathbf{x}^{(i)}),\phi(\mathbf{x}^{(j)})\rangle=\bigl\lVert\sum_ic_i\phi(\mathbf{x}^{(i)})\bigr\rVert^2\ge0$.

*If.*

3. For $\mathbf{x}\in\mathcal X$ let $k_{\mathbf{x}}$ be the function $k_{\mathbf{x}}(\mathbf{z})=K(\mathbf{z},\mathbf{x})$, and let $\mathcal H$ be the vector space of finite combinations $f=\sum_ia_ik_{\mathbf{x}^{(i)}}$. For $f$ as above and $g=\sum_jb_jk_{\mathbf{z}^{(j)}}$ define

   $$
   \langle f,g\rangle=\sum_{i,j}a_ib_jK(\mathbf{x}^{(i)},\mathbf{z}^{(j)}).
   $$

4. This does not depend on how $f$ and $g$ are written. Using the symmetry of $K$, $f(\mathbf{z})=\sum_ia_iK(\mathbf{x}^{(i)},\mathbf{z})$, so

   $$
   \langle f,g\rangle=\sum_jb_j\sum_ia_iK(\mathbf{x}^{(i)},\mathbf{z}^{(j)})=\sum_jb_jf(\mathbf{z}^{(j)}),
   $$

   which depends on $f$ only as a function; in the same way $\langle f,g\rangle=\sum_ia_ig(\mathbf{x}^{(i)})$ depends on $g$ only as a function. In particular $\langle f,k_{\mathbf{z}}\rangle=f(\mathbf{z})$.

5. The form is bilinear and symmetric, and $\langle f,f\rangle=\mathbf{a}^{\mathsf T}K\mathbf{a}\ge0$ by the hypothesis. So it is a positive semidefinite symmetric bilinear form, and the Cauchy–Schwarz inequality holds for it.

6. If $\langle f,f\rangle=0$ then for every $\mathbf{z}$, $f(\mathbf{z})^2=\langle f,k_{\mathbf{z}}\rangle^2\le\langle f,f\rangle\langle k_{\mathbf{z}},k_{\mathbf{z}}\rangle=0$, so $f=0$. Hence $\langle\cdot,\cdot\rangle$ is an inner product on $\mathcal H$.

7. With $\phi(\mathbf{x})=k_{\mathbf{x}}$, $\langle\phi(\mathbf{x}),\phi(\mathbf{z})\rangle=K(\mathbf{x},\mathbf{z})$ by the definition in step 3, so $K$ is a kernel.

:::

::: {#prp-kernel-closure .proposition name="Building kernels"}

Let $K_1,K_2$ be kernels on $\mathcal X$ and $c>0$. Then $cK_1$, $K_1+K_2$, $K_1K_2$ and $\exp(K_1)$ are kernels, and so is $f(\mathbf{x})K_1(\mathbf{x},\mathbf{z})f(\mathbf{z})$ for any function $f:\mathcal X\to\mathbb{R}$. Consequently the polynomial and Gaussian kernels of @exm-kernel-polynomial are kernels.

:::

::: {.proof}

By @thm-kernel-psd it is enough to check that every kernel matrix is positive semidefinite. Fix points and let $A,B$ be the kernel matrices of $K_1,K_2$ on them.

1. $cA$ and $A+B$ are positive semidefinite, since $\mathbf{c}^{\mathsf T}(A+B)\mathbf{c}=\mathbf{c}^{\mathsf T}A\mathbf{c}+\mathbf{c}^{\mathsf T}B\mathbf{c}$.

2. *Product.* Write $B=\sum_k\lambda_k\mathbf{u}_k\mathbf{u}_k^{\mathsf T}$ with $\lambda_k\ge0$ (spectral theorem). The kernel matrix of $K_1K_2$ has entries $A_{ij}B_{ij}$, so for $\mathbf{c}\in\mathbb{R}^N$,

   $$
   \sum_{i,j}c_ic_jA_{ij}B_{ij}=\sum_k\lambda_k\sum_{i,j}(c_iu_{k,i})A_{ij}(c_ju_{k,j})\ge0,
   $$

   since each inner sum is $\mathbf{v}^{\mathsf T}A\mathbf{v}$ with $v_i=c_iu_{k,i}$.

3. *Exponential.* By steps 1 and 2 and induction, each partial sum $\sum_{m=0}^M K_1^m/m!$ is a kernel (the constant $1$ is the kernel with $\phi(\mathbf{x})=1$). Its kernel matrices converge entrywise to those of $\exp(K_1)$, and a limit of positive semidefinite matrices is positive semidefinite.

4. *Rescaling.* The kernel matrix of $f(\mathbf{x})K_1(\mathbf{x},\mathbf{z})f(\mathbf{z})$ is $DAD$ with $D=\operatorname{diag}(f(\mathbf{x}^{(i)}))$, and $\mathbf{c}^{\mathsf T}DAD\mathbf{c}=(D\mathbf{c})^{\mathsf T}A(D\mathbf{c})\ge0$.

5. *Consequences.* $\mathbf{x}^{\mathsf T}\mathbf{z}$ is a kernel ($\phi=\mathrm{id}$) and so is the constant $c\ge0$, so $(\mathbf{x}^{\mathsf T}\mathbf{z}+c)^k$ is a kernel by steps 1 and 2. For the Gaussian kernel,

   $$
   e^{-\lVert\mathbf{x}-\mathbf{z}\rVert^2/(2\tau^2)}=e^{-\lVert\mathbf{x}\rVert^2/(2\tau^2)}\,e^{\mathbf{x}^{\mathsf T}\mathbf{z}/\tau^2}\,e^{-\lVert\mathbf{z}\rVert^2/(2\tau^2)},
   $$

   which is step 4 applied to the kernel $\exp(\mathbf{x}^{\mathsf T}\mathbf{z}/\tau^2)$ of step 3.

:::

::: {#def-kernel-trick .definition name="The kernel trick for least squares"}

Gradient descent on the squared loss with features $\phi$ (batch version, step size $\alpha$) updates

$$
\boldsymbol\theta\leftarrow\boldsymbol\theta+\alpha\sum_{i=1}^N\bigl(y^{(i)}-\langle\boldsymbol\theta,\phi(\mathbf{x}^{(i)})\rangle\bigr)\phi(\mathbf{x}^{(i)}).
$$

The *kernelized* version keeps coefficients $\boldsymbol\beta\in\mathbb{R}^N$ instead, starting from $\boldsymbol\beta=\mathbf{0}$, and updates

$$
\beta_i\leftarrow\beta_i+\alpha\Bigl(y^{(i)}-\sum_{j=1}^N\beta_jK(\mathbf{x}^{(i)},\mathbf{x}^{(j)})\Bigr)\quad(i=1,\dots,N),\qquad\text{that is,}\quad\boldsymbol\beta\leftarrow\boldsymbol\beta+\alpha(\mathbf{y}-K\boldsymbol\beta),
$$

and predicts $\sum_i\beta_iK(\mathbf{x}^{(i)},\mathbf{x})$ at a new input $\mathbf{x}$.

:::

::: {#prp-kernel-trick .proposition name="The kernelized updates are the same algorithm"}

If gradient descent of @def-kernel-trick starts at $\boldsymbol\theta=\mathbf{0}$, then after every step $\boldsymbol\theta=\sum_i\beta_i\phi(\mathbf{x}^{(i)})$, where $\boldsymbol\beta$ follows the kernelized updates, and the two versions make the same predictions. Each kernelized step costs $O(N^2)$ kernel-matrix operations (after computing $K$ once), independent of the dimension of $\phi$.

:::

::: {.proof}

1. At the start both $\boldsymbol\theta$ and $\sum_i\beta_i\phi(\mathbf{x}^{(i)})$ are $\mathbf{0}$.

2. Suppose $\boldsymbol\theta=\sum_j\beta_j\phi(\mathbf{x}^{(j)})$ before a step. Then $\langle\boldsymbol\theta,\phi(\mathbf{x}^{(i)})\rangle=\sum_j\beta_jK(\mathbf{x}^{(j)},\mathbf{x}^{(i)})$, so the update adds $\sum_i\alpha\bigl(y^{(i)}-\sum_j\beta_jK_{ij}\bigr)\phi(\mathbf{x}^{(i)})$ to $\boldsymbol\theta$: exactly $\sum_i(\text{change in }\beta_i)\,\phi(\mathbf{x}^{(i)})$. By induction the relation holds after every step.

3. The prediction $\langle\boldsymbol\theta,\phi(\mathbf{x})\rangle=\sum_i\beta_iK(\mathbf{x}^{(i)},\mathbf{x})$ needs only kernel values.

:::

::: {#rmk-kernels-1 .remark name="Kernels as similarity" editor="No figure: kernelized least squares on a small example draws the same fitted curve as least squares on the explicit features, so a picture would not show the trick, which is about cost."}

$K(\mathbf{x},\mathbf{z})$ is large when $\phi(\mathbf{x})$ and $\phi(\mathbf{z})$ point the same way, so a kernel can be designed as a measure of similarity (between strings, graphs or images) without writing $\phi$ down; @thm-kernel-psd says which similarity measures are allowed. Any algorithm that touches the inputs only through inner products can be kernelized this way, the support vector machine (@sec-ai-kernel-methods-support-vector-machines) being the main example. The price is that predictions cost $O(N)$ kernel evaluations each, like the non-parametric method of @def-locally-weighted-regression.

:::
