---
title: "The Fourier Transform, Convolution and the Gaussian"
sources: [camii-pm-5]
requires: [math/analysis/measure-theory/product-measures, math/analysis/measure-theory/lp-spaces]
status: draft
---

<!-- Added 2026-11-21 from Cambridge Part II Probability and Measure (Michaelmas 2016 lecture notes), Sections 5.1–5.3, in our own wording; proofs written out in steps. The computation of the Gaussian transform by a differential equation is our own route. -->

In this note $L^p=L^p(\mathbb R^d)$ consists of complex-valued Borel functions with $\int|f|^p\,dx<\infty$; integrals of complex functions are taken on real and imaginary parts, and $\big|\int f\big|\le\int|f|$. We write $\langle u,x\rangle=u_1x_1+\dots+u_dx_d$ and $|x|^2=\langle x,x\rangle$.

::: {#def-fourier-transform .definition name="Fourier transform of a function and of a measure"}

The *Fourier transform* of $f\in L^1(\mathbb R^d)$ and of a finite Borel measure $\mu$ on $\mathbb R^d$ are

$$
\hat f(u)=\int_{\mathbb R^d}f(x)\,e^{i\langle u,x\rangle}\,dx,\qquad\hat\mu(u)=\int_{\mathbb R^d}e^{i\langle u,x\rangle}\,\mu(dx),\qquad u\in\mathbb R^d .
$$

For a random variable $X$ in $\mathbb R^d$ with law $\mu_X$, $\varphi_X(u)=\hat\mu_X(u)=E\big[e^{i\langle u,X\rangle}\big]$ is its *characteristic function*.

:::

If $\mu$ has density $f$ then $\hat\mu=\hat f$, and for $d=1$ the characteristic function is the one of @sec-math-probability-joint-distributions-transforms.

::: {#prp-fourier-bounded-continuous .proposition name="Fourier transforms are bounded and continuous"}

$|\hat f(u)|\le\|f\|_1$ and $|\hat\mu(u)|\le\mu(\mathbb R^d)$, and both $\hat f$ and $\hat\mu$ are continuous.

:::

::: {.proof}

1. $|e^{i\langle u,x\rangle}|=1$, so the bounds follow from $\big|\int g\big|\le\int|g|$.

2. If $u_n\to u$, then $e^{i\langle u_n,x\rangle}\to e^{i\langle u,x\rangle}$ for each $x$, and the integrands are dominated by $|f|$ (respectively the constant $1$, integrable for the finite measure $\mu$). Dominated convergence gives $\hat f(u_n)\to\hat f(u)$.

:::

## Convolution

::: {#def-convolution .definition name="Convolution"}

For probability measures $\mu,\nu$ on $\mathbb R^d$, the *convolution* $\mu*\nu$ is the image of $\mu\otimes\nu$ under $(x,y)\mapsto x+y$: the law of $X+Y$ for independent $X\sim\mu$, $Y\sim\nu$. For $f\in L^p$ and a probability measure $\nu$,

$$
(f*\nu)(x)=\int_{\mathbb R^d}f(x-y)\,\nu(dy),
$$

and for $f\in L^p$, $g\in L^1$, $f*g=f*\nu$ where $\nu$ has density $g\ge0$ (by linearity for general $g$).

:::

::: {#prp-convolution-properties .proposition name="Convolution and the Fourier transform"}

1. For $f\in L^p$ ($1\le p<\infty$) and a probability measure $\nu$, $f*\nu$ is defined a.e. and $\|f*\nu\|_p\le\|f\|_p$.
2. For $f\in L^1$, $\widehat{f*\nu}=\hat f\,\hat\nu$.
3. For probability measures, $\widehat{\mu*\nu}=\hat\mu\,\hat\nu$; so $\varphi_{X+Y}=\varphi_X\varphi_Y$ for independent $X,Y$.

:::

::: {.proof}

1. By Jensen's inequality for the probability measure $\nu$ and the convex function $t\mapsto t^p$ (@thm-jensen-integrable), $\big(\int|f(x-y)|\,\nu(dy)\big)^p\le\int|f(x-y)|^p\,\nu(dy)$. Integrate in $x$ and use Tonelli (@thm-fubini) and translation invariance of Lebesgue measure: $\int\!\!\int|f(x-y)|^p\,dx\,\nu(dy)=\|f\|_p^p$. In particular the inner integral is finite for a.e. $x$.

2. $\int\!\!\int|f(x-y)|\,\nu(dy)\,dx=\|f\|_1<\infty$, so Fubini allows
$$\widehat{f*\nu}(u)=\int\!\!\int f(x-y)e^{i\langle u,x\rangle}dx\,\nu(dy)=\int\!\!\int f(z)e^{i\langle u,z\rangle}dz\;e^{i\langle u,y\rangle}\nu(dy)=\hat f(u)\hat\nu(u),$$
substituting $x=z+y$.

3. By the image-measure formula and Fubini, $\widehat{\mu*\nu}(u)=\int\!\!\int e^{i\langle u,x+y\rangle}\mu(dx)\nu(dy)=\hat\mu(u)\hat\nu(u)$.

:::

## The Gaussian

::: {#def-gaussian-heat-kernel .definition name="Gaussian density with variance $t$"}

For $t>0$ let

$$
g_t(x)=(2\pi t)^{-d/2}\,e^{-|x|^2/(2t)},\qquad x\in\mathbb R^d ,
$$

the density of $\sqrt t\,Z$ where $Z=(Z_1,\dots,Z_d)$ has independent $N(0,1)$ coordinates.

:::

::: {#fig-fourier-transform-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-3.3,0) -- (3.5,0) node[lab, right] {$x$};
\draw[->] (0,-0.1) -- (0,3.3) node[lab, above] {};
\draw[hl] (-3.000,0.000) -- (-2.900,0.000) -- (-2.800,0.000) -- (-2.700,0.000) -- (-2.600,0.000) -- (-2.500,0.000) -- (-2.400,0.000) -- (-2.300,0.000) -- (-2.200,0.000) -- (-2.100,0.000) -- (-2.000,0.001) -- (-1.900,0.002) -- (-1.800,0.004) -- (-1.700,0.008) -- (-1.600,0.015) -- (-1.500,0.028) -- (-1.400,0.051) -- (-1.300,0.087) -- (-1.200,0.143) -- (-1.100,0.227) -- (-1.000,0.346) -- (-0.900,0.505) -- (-0.800,0.710) -- (-0.700,0.958) -- (-0.600,1.243) -- (-0.500,1.549) -- (-0.400,1.854) -- (-0.300,2.133) -- (-0.200,2.357) -- (-0.100,2.503) -- (0.000,2.553) -- (0.100,2.503) -- (0.200,2.357) -- (0.300,2.133) -- (0.400,1.854) -- (0.500,1.549) -- (0.600,1.243) -- (0.700,0.958) -- (0.800,0.710) -- (0.900,0.505) -- (1.000,0.346) -- (1.100,0.227) -- (1.200,0.143) -- (1.300,0.087) -- (1.400,0.051) -- (1.500,0.028) -- (1.600,0.015) -- (1.700,0.008) -- (1.800,0.004) -- (1.900,0.002) -- (2.000,0.001) -- (2.100,0.000) -- (2.200,0.000) -- (2.300,0.000) -- (2.400,0.000) -- (2.500,0.000) -- (2.600,0.000) -- (2.700,0.000) -- (2.800,0.000) -- (2.900,0.000) -- (3.000,0.000);
\draw[emph] (-3.000,0.014) -- (-2.900,0.019) -- (-2.800,0.025) -- (-2.700,0.033) -- (-2.600,0.043) -- (-2.500,0.056) -- (-2.400,0.072) -- (-2.300,0.091) -- (-2.200,0.114) -- (-2.100,0.141) -- (-2.000,0.173) -- (-1.900,0.210) -- (-1.800,0.253) -- (-1.700,0.301) -- (-1.600,0.355) -- (-1.500,0.414) -- (-1.400,0.479) -- (-1.300,0.548) -- (-1.200,0.621) -- (-1.100,0.697) -- (-1.000,0.774) -- (-0.900,0.851) -- (-0.800,0.927) -- (-0.700,0.999) -- (-0.600,1.066) -- (-0.500,1.127) -- (-0.400,1.178) -- (-0.300,1.220) -- (-0.200,1.251) -- (-0.100,1.270) -- (0.000,1.277) -- (0.100,1.270) -- (0.200,1.251) -- (0.300,1.220) -- (0.400,1.178) -- (0.500,1.127) -- (0.600,1.066) -- (0.700,0.999) -- (0.800,0.927) -- (0.900,0.851) -- (1.000,0.774) -- (1.100,0.697) -- (1.200,0.621) -- (1.300,0.548) -- (1.400,0.479) -- (1.500,0.414) -- (1.600,0.355) -- (1.700,0.301) -- (1.800,0.253) -- (1.900,0.210) -- (2.000,0.173) -- (2.100,0.141) -- (2.200,0.114) -- (2.300,0.091) -- (2.400,0.072) -- (2.500,0.056) -- (2.600,0.043) -- (2.700,0.033) -- (2.800,0.025) -- (2.900,0.019) -- (3.000,0.014);
\draw[faint] (-3.000,0.207) -- (-2.900,0.223) -- (-2.800,0.240) -- (-2.700,0.257) -- (-2.600,0.274) -- (-2.500,0.292) -- (-2.400,0.311) -- (-2.300,0.329) -- (-2.200,0.349) -- (-2.100,0.368) -- (-2.000,0.387) -- (-1.900,0.406) -- (-1.800,0.426) -- (-1.700,0.445) -- (-1.600,0.464) -- (-1.500,0.482) -- (-1.400,0.500) -- (-1.300,0.517) -- (-1.200,0.533) -- (-1.100,0.549) -- (-1.000,0.563) -- (-0.900,0.577) -- (-0.800,0.589) -- (-0.700,0.600) -- (-0.600,0.610) -- (-0.500,0.619) -- (-0.400,0.626) -- (-0.300,0.631) -- (-0.200,0.635) -- (-0.100,0.638) -- (0.000,0.638) -- (0.100,0.638) -- (0.200,0.635) -- (0.300,0.631) -- (0.400,0.626) -- (0.500,0.619) -- (0.600,0.610) -- (0.700,0.600) -- (0.800,0.589) -- (0.900,0.577) -- (1.000,0.563) -- (1.100,0.549) -- (1.200,0.533) -- (1.300,0.517) -- (1.400,0.500) -- (1.500,0.482) -- (1.600,0.464) -- (1.700,0.445) -- (1.800,0.426) -- (1.900,0.406) -- (2.000,0.387) -- (2.100,0.368) -- (2.200,0.349) -- (2.300,0.329) -- (2.400,0.311) -- (2.500,0.292) -- (2.600,0.274) -- (2.700,0.257) -- (2.800,0.240) -- (2.900,0.223) -- (3.000,0.207);
\node[lab, text=accent] at (0.75,2.4) {$g_{1/4}$};
\node[lab] at (1.35,1.0) {$g_1$};
\node[lab] at (2.8,0.75) {$g_4$};
\end{tikzpicture}
\end{center}
```

Gaussian densities $g_t$ for $t=\frac14,1,4$. Their transforms are $e^{-tu^2/2}$: the narrower the density, the wider its transform.

:::

::: {#prp-gaussian-fourier .proposition name="The Fourier transform of a Gaussian"}

$\hat g_t(u)=e^{-t|u|^2/2}$. Equivalently $E\big[e^{i\langle u,Z\rangle}\big]=e^{-|u|^2/2}$.

:::

::: {.proof}

1. By independence of the coordinates and Fubini, $E[e^{i\langle u,Z\rangle}]=\prod_jE[e^{iu_jZ_j}]$, and scaling by $\sqrt t$ replaces $u$ by $\sqrt tu$. So it suffices to show $\phi(u)=\int_{\mathbb R}e^{iux}g_1(x)\,dx$ equals $e^{-u^2/2}$.

2. The $u$-derivative of the integrand, $ixe^{iux}g_1(x)$, is bounded by the integrable $|x|g_1(x)$. By @thm-differentiation-under-integral (on real and imaginary parts),
$$\phi'(u)=\int ixe^{iux}g_1(x)\,dx=-i\int e^{iux}g_1'(x)\,dx,$$
using $xg_1(x)=-g_1'(x)$.

3. Integrate by parts on $[-R,R]$ and let $R\to\infty$ (the boundary terms $e^{iuR}g_1(R)$ vanish): $\int e^{iux}g_1'(x)\,dx=-iu\int e^{iux}g_1(x)\,dx=-iu\,\phi(u)$. Hence $\phi'(u)=-u\phi(u)$.

4. So $\frac{d}{du}\big(e^{u^2/2}\phi(u)\big)=0$, and $\phi(0)=1$ gives $\phi(u)=e^{-u^2/2}$.

:::

::: {#cor-gaussian-inversion .corollary name="Inversion for the Gaussian"}

For all $x\in\mathbb R^d$,

$$
g_t(x)=(2\pi)^{-d}\int_{\mathbb R^d}\hat g_t(u)\,e^{-i\langle u,x\rangle}\,du .
$$

:::

::: {.proof}

1. $\hat g_t(u)=e^{-t|u|^2/2}=(2\pi/t)^{d/2}\,g_{1/t}(u)$.

2. So the right side is $(2\pi)^{-d}(2\pi/t)^{d/2}\,\hat g_{1/t}(-x)=(2\pi t)^{-d/2}e^{-|x|^2/(2t)}=g_t(x)$, by @prp-gaussian-fourier with $1/t$ in place of $t$.

:::
