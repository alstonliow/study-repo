---
title: "Data Preprocessing: Centring, Scaling, PCA and Whitening"
sources: [cs231n-6]
requires: [ai/deep-learning/neural-networks, math/linear-algebra/matrix-methods/low-rank-approximation, math/probability/discrete/covariance-and-correlation]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS231n course notes (Neural networks part 2: data preprocessing), in our own wording; the example was computed with NumPy; the covariance proposition and its proof are our own. -->

Gradient-based training behaves best when the input features are centred at zero and of comparable size. Let $X\in\mathbb{R}^{N\times D}$ hold the $N$ training inputs as rows.

::: {#def-centring-scaling .definition name="Mean subtraction and normalization"}

*Mean subtraction* replaces every row $\mathbf{x}_i$ by $\mathbf{x}_i-\boldsymbol\mu$, where $\boldsymbol\mu=\frac1N\sum_i\mathbf{x}_i$ is the mean of the training inputs. *Normalization* then divides each coordinate $j$ by its standard deviation $\sigma_j$ over the training inputs, so that every feature has mean $0$ and variance $1$.

:::

For images all pixels already share one scale ($0$ to $255$), so mean subtraction alone is usual: either the mean image ($D$ numbers) or one mean per colour channel is subtracted.

::: {#def-pca-whitening .definition name="PCA and whitening"}

Let $X$ be centred and let its covariance $\Sigma=\frac1NX^{\mathsf T}X$ have the spectral decomposition $\Sigma=U\Lambda U^{\mathsf T}$, with $U$ orthogonal and $\Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_D)$, $\lambda_1\ge\dots\ge\lambda_D\ge0$. Then

1. $X_{\text{rot}}=XU$ expresses the data in the basis of eigenvectors (the principal components, @def-principal-components);
2. *PCA dimensionality reduction* keeps the first $k$ columns of $X_{\text{rot}}$, the directions of largest variance;
3. *whitening* divides column $j$ of $X_{\text{rot}}$ by $\sqrt{\lambda_j+\varepsilon}$ for a small $\varepsilon>0$: $X_{\text{white}}=XU(\Lambda+\varepsilon I)^{-1/2}$.

:::

::: {#prp-whitening-covariance .proposition name="Covariance after rotation and whitening"}

With the notation of @def-pca-whitening, $X_{\text{rot}}$ has covariance $\Lambda$, and with $\varepsilon=0$ and all $\lambda_j>0$, $X_{\text{white}}$ has covariance $I$.

:::

::: {.proof}

1. The columns of $XU$ have mean zero, because those of $X$ do and $U$ is a fixed linear map.
2. $\frac1N(XU)^{\mathsf T}(XU)=U^{\mathsf T}\Sigma U=U^{\mathsf T}U\Lambda U^{\mathsf T}U=\Lambda$, since $U^{\mathsf T}U=I$.
3. For $X_{\text{white}}=XU\Lambda^{-1/2}$, the covariance is $\Lambda^{-1/2}\,\Lambda\,\Lambda^{-1/2}=I$.

:::

So the rotated features are uncorrelated, and the whitened ones also have unit variance in every direction.

::: {#exm-whitening-four-points .example name="Whitening four points"}

The points $(2,1),(0,1),(-2,-1),(0,-1)$ have mean zero and covariance $\Sigma=\begin{pmatrix}2&1\\1&1\end{pmatrix}$, with eigenvalues $(3\pm\sqrt5)/2\approx2.618,\ 0.382$. In the eigenvector basis the point $(2,1)$ has coordinates $(\mp2.227,\ \pm0.201)$ (signs depend on the chosen eigenvectors), with variances $2.618$ and $0.382$; after whitening the coordinates are divided by $\sqrt{2.618}$ and $\sqrt{0.382}$, and both variances become $1$.

:::

::: {#fig-data-preprocessing-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.55cm,y=0.55cm]
\draw[faint] (-2.4,0) -- (2.4,0);
\draw[faint] (0.0,-2.4) -- (0.0,2.4);
\node[dot] at (2.000,1.000) {};
\node[dot] at (0.000,1.000) {};
\node[dot] at (-2.000,-1.000) {};
\node[dot] at (0.000,-1.000) {};
\node[lab] at (0.0,2.75) {centred};
\draw[faint] (2.80,0) -- (7.6,0);
\draw[faint] (5.2,-2.4) -- (5.2,2.4);
\node[dot] at (7.427,0.201) {};
\node[dot] at (5.726,-0.851) {};
\node[dot] at (2.973,-0.201) {};
\node[dot] at (4.674,0.851) {};
\node[lab] at (5.2,2.75) {rotated};
\draw[faint] (8.0,0) -- (12.8,0);
\draw[faint] (10.4,-2.4) -- (10.4,2.4);
\node[dot] at (11.776,0.325) {};
\node[dot] at (10.725,-1.376) {};
\node[dot] at (9.024,-0.325) {};
\node[dot] at (10.075,1.376) {};
\node[lab] at (10.4,2.75) {whitened};
\draw[hl,->] (0,0) -- (1.376,0.851);
\draw[hl,->] (0,0) -- (0.325,-0.526);
\draw[hl] (5.2,0) ellipse (1.618 and 0.618);
\draw[hl] (10.4,0) circle (1);
\end{tikzpicture}
\end{center}
```

The four points of @exm-whitening-four-points: centred data with the principal directions scaled by $\sqrt{\lambda_j}$ (left), in the eigenvector basis with standard deviations $1.618$ and $0.618$ (middle), and whitened, with unit variance in every direction (right).

:::

```{=latex}
\begin{algorithm}
\caption{PCA whitening}
\begin{algorithmic}
\INPUT training inputs $X\in\mathbb{R}^{N\times D}$, number $k$ of components, $\varepsilon>0$
\OUTPUT whitened training inputs, and $(\boldsymbol\mu,U_k,\Lambda_k)$ to apply to new inputs
\STATE $\boldsymbol\mu\gets\frac1N\sum_i\mathbf{x}_i$; $X\gets X-\mathbf{1}\boldsymbol\mu^{\mathsf T}$
\STATE $\Sigma\gets\frac1NX^{\mathsf T}X$; $U\Lambda U^{\mathsf T}\gets$ spectral decomposition of $\Sigma$ (eigenvalues decreasing)
\STATE $U_k,\Lambda_k\gets$ first $k$ eigenvectors and eigenvalues
\RETURN $XU_k(\Lambda_k+\varepsilon I)^{-1/2}$
\end{algorithmic}
\end{algorithm}
```

::: {#rmk-data-preprocessing-1 .remark name="Statistics come from the training data only"}

The mean, the scales and the PCA basis are computed on the training data, then applied unchanged to validation and test inputs. Computing them on all the data first and splitting afterwards leaks information from the test set into training.

:::

::: {#rmk-data-preprocessing-2 .remark name="Whitening in practice"}

Whitening amplifies the directions of smallest variance, which in images are mostly noise; $\varepsilon$ limits this. For convolutional networks on images, PCA and whitening are rarely used: centring (and sometimes per-channel scaling) is enough, and batch normalization (@sec-ai-deep-learning-batch-normalization) standardizes the inputs of later layers inside the network.

:::
