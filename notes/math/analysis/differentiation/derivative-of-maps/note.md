---
title: "The Derivative of a Map between Euclidean Spaces"
sources: [camib-at-a6, mit1802-8, mit1802-9, mit1802n-TA]
requires: [math/analysis/metric-spaces/continuous-maps, math/analysis/real/differentiability/differentiability-and-inverses, math/calculus/multivariable/differentiation/partial-derivatives]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Analysis II (Michaelmas 2015 lecture notes), Section 6.1, in our own wording; the examples are ours (checked symbolically); proofs written out in steps. The calculus notes state linear approximation for two variables with an informal proof; the rigorous versions here carry related= and merged 2026-11-20 (owner): thm-continuous-partials-differentiable replaces the calculus block thm-linear-approximation-two-variables (MIT 18.02, Lectures 8-9 and Supplementary Notes TA); its proof is the calculus two-step mean value argument extended to n coordinates. -->

In one variable, $f$ is differentiable at $a$ when $f(a+h)=f(a)+\lambda h+o(h)$ (@prp-derivative-little-o). In several variables the number $\lambda$ becomes a linear map, and this is the definition.

Throughout, $U\subseteq\mathbb R^n$ is open, so that $a+h\in U$ for all small $h$, and $\|\cdot\|$ is any norm; by @thm-norms-equivalent-finite-dimension the choice does not affect the definitions. $L(\mathbb R^n;\mathbb R^m)$ is the space of linear maps $\mathbb R^n\to\mathbb R^m$, identified with $m\times n$ matrices.

::: {#def-derivative-several-variables .definition name="Derivative of a map" related="prp-derivative-little-o"}

A map $f:U\to\mathbb R^m$ is *differentiable* at $a\in U$ if there is a linear map $A\in L(\mathbb R^n;\mathbb R^m)$ with
$$\lim_{h\to0}\frac{\|f(a+h)-f(a)-Ah\|}{\|h\|}=0,$$
that is, $f(a+h)=f(a)+Ah+o(\|h\|)$. Then $A$ is the *derivative* $Df(a)$. $f$ is differentiable on $U$ if it is differentiable at every point of $U$.

:::

::: {#fig-derivative-of-maps-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0.0,0) -- (0.0,1.2); \draw[faint] (0,0.0) -- (1.2,0.0);
\draw[faint] (0.4,0) -- (0.4,1.2); \draw[faint] (0,0.4) -- (1.2,0.4);
\draw[faint] (0.8,0) -- (0.8,1.2); \draw[faint] (0,0.8) -- (1.2,0.8);
\draw[faint] (1.20,0) -- (1.20,1.2); \draw[faint] (0,1.20) -- (1.2,1.20);
\draw[emph] (3.600,0.100) -- (3.615,0.160) -- (3.632,0.220) -- (3.649,0.280) -- (3.667,0.340) -- (3.686,0.400) -- (3.706,0.460) -- (3.726,0.520) -- (3.748,0.580) -- (3.770,0.640) -- (3.793,0.700) -- (3.817,0.760) -- (3.842,0.820) -- (3.868,0.880) -- (3.895,0.940) -- (3.922,1.000) -- (3.951,1.060) -- (3.980,1.120) -- (4.010,1.180) -- (4.041,1.240) -- (4.073,1.300);
\draw[emph] (3.600,0.100) -- (3.660,0.121) -- (3.720,0.144) -- (3.780,0.167) -- (3.840,0.191) -- (3.900,0.216) -- (3.960,0.242) -- (4.020,0.268) -- (4.080,0.296) -- (4.140,0.324) -- (4.200,0.353) -- (4.260,0.383) -- (4.320,0.414) -- (4.380,0.446) -- (4.440,0.479) -- (4.500,0.512) -- (4.560,0.547) -- (4.620,0.582) -- (4.680,0.618) -- (4.740,0.655) -- (4.800,0.693);
\draw[emph] (4.000,0.259) -- (4.015,0.319) -- (4.032,0.379) -- (4.049,0.439) -- (4.067,0.499) -- (4.086,0.559) -- (4.106,0.619) -- (4.126,0.679) -- (4.148,0.739) -- (4.170,0.799) -- (4.193,0.859) -- (4.217,0.919) -- (4.242,0.979) -- (4.268,1.039) -- (4.295,1.099) -- (4.322,1.159) -- (4.351,1.219) -- (4.380,1.279) -- (4.410,1.339) -- (4.441,1.399) -- (4.473,1.459);
\draw[emph] (3.719,0.500) -- (3.779,0.521) -- (3.839,0.544) -- (3.899,0.567) -- (3.959,0.591) -- (4.019,0.616) -- (4.079,0.642) -- (4.139,0.668) -- (4.199,0.696) -- (4.259,0.724) -- (4.319,0.753) -- (4.379,0.783) -- (4.439,0.814) -- (4.499,0.846) -- (4.559,0.879) -- (4.619,0.912) -- (4.679,0.947) -- (4.739,0.982) -- (4.799,1.018) -- (4.859,1.055) -- (4.919,1.093);
\draw[emph] (4.400,0.457) -- (4.415,0.517) -- (4.432,0.577) -- (4.449,0.637) -- (4.467,0.697) -- (4.486,0.757) -- (4.506,0.817) -- (4.526,0.877) -- (4.548,0.937) -- (4.570,0.997) -- (4.593,1.057) -- (4.617,1.117) -- (4.642,1.177) -- (4.668,1.237) -- (4.695,1.297) -- (4.722,1.357) -- (4.751,1.417) -- (4.780,1.477) -- (4.810,1.537) -- (4.841,1.597) -- (4.873,1.657);
\draw[emph] (3.877,0.900) -- (3.937,0.921) -- (3.997,0.944) -- (4.057,0.967) -- (4.117,0.991) -- (4.177,1.016) -- (4.237,1.042) -- (4.297,1.068) -- (4.357,1.096) -- (4.417,1.124) -- (4.477,1.153) -- (4.537,1.183) -- (4.597,1.214) -- (4.657,1.246) -- (4.717,1.279) -- (4.777,1.312) -- (4.837,1.347) -- (4.897,1.382) -- (4.957,1.418) -- (5.017,1.455) -- (5.077,1.493);
\draw[emph] (4.800,0.693) -- (4.815,0.753) -- (4.832,0.813) -- (4.849,0.873) -- (4.867,0.933) -- (4.886,0.993) -- (4.906,1.053) -- (4.926,1.113) -- (4.948,1.173) -- (4.970,1.233) -- (4.993,1.293) -- (5.017,1.353) -- (5.042,1.413) -- (5.068,1.473) -- (5.095,1.533) -- (5.122,1.593) -- (5.151,1.653) -- (5.180,1.713) -- (5.210,1.773) -- (5.241,1.833) -- (5.273,1.893);
\draw[emph] (4.073,1.300) -- (4.133,1.321) -- (4.193,1.344) -- (4.253,1.367) -- (4.313,1.391) -- (4.373,1.416) -- (4.433,1.442) -- (4.493,1.468) -- (4.553,1.496) -- (4.613,1.524) -- (4.673,1.553) -- (4.733,1.583) -- (4.793,1.614) -- (4.853,1.646) -- (4.913,1.679) -- (4.973,1.712) -- (5.033,1.747) -- (5.093,1.782) -- (5.153,1.818) -- (5.213,1.855) -- (5.273,1.893);
\draw[hl, dashed] (3.600,0.100) -- (4.800,0.520) -- (5.100,1.720) -- (3.900,1.300) -- cycle;
\node[dot] at (0,0) {}; \node[lab, below left] at (0,0) {$a$}; \node[dot] at (3.6,0.1) {}; \node[lab, below left] at (3.6,0.1) {$f(a)$};
\draw[map] (1.5,0.6) -- node[lab, above] {$f$} (3.2,0.6);
\end{tikzpicture}
\end{center}
```

Near $a$, $f$ bends a small grid (dark); the affine map $h\mapsto f(a)+Df(a)h$ sends it to the parallelogram (orange), and the error is $o(\lVert h\rVert)$.

:::

::: {#prp-derivative-several-variables-basic .proposition name="Basic properties of the derivative"}

Let $f,g:U\to\mathbb R^m$ and $a\in U$.

1. The derivative, if it exists, is unique.
2. If $f$ is differentiable at $a$, it is continuous at $a$.
3. $f=(f_1,\dots,f_m)$ is differentiable at $a$ if and only if every component $f_i$ is, and then the $i$-th row of $Df(a)$ is $Df_i(a)$.
4. If $f,g$ are differentiable at $a$, so is $\lambda f+\mu g$, with $D(\lambda f+\mu g)(a)=\lambda Df(a)+\mu Dg(a)$.
5. A linear map $A$ is differentiable everywhere with $DA(a)=A$; a constant map has derivative $0$.

:::

::: {.proof}

1. If $A$ and $B$ both qualify, then $\frac{\|(A-B)h\|}{\|h\|}\le\frac{\|f(a+h)-f(a)-Ah\|}{\|h\|}+\frac{\|f(a+h)-f(a)-Bh\|}{\|h\|}\to0$. Put $h=tv$ for a fixed $v\ne0$ and $t\to0^+$: the left side is the constant $\frac{\|(A-B)v\|}{\|v\|}$, so $(A-B)v=0$ for all $v$.

2. $\|f(a+h)-f(a)\|\le\|f(a+h)-f(a)-Df(a)h\|+\|Df(a)h\|$. The first term is $o(\|h\|)$, and the second tends to $0$ because linear maps are continuous (@thm-linear-maps-continuous).

3. Use $\|\cdot\|_\infty$ on $\mathbb R^m$: a vector tends to $0$ if and only if each component does.

4. The error term of $\lambda f+\mu g$ is $\lambda$ times that of $f$ plus $\mu$ times that of $g$.

5. For linear $A$ the error $A(a+h)-Aa-Ah$ is identically $0$.

:::

## Partial derivatives

::: {#def-directional-derivative-several .definition name="Directional and partial derivatives" related="def-directional-derivative def-partial-derivative"}

For $f:U\to\mathbb R^m$, $a\in U$ and $v\in\mathbb R^n$, the *directional derivative* is
$$D_vf(a)=\lim_{t\to0}\frac{f(a+tv)-f(a)}t$$
when the limit exists. With $e_1,\dots,e_n$ the standard basis, $D_jf(a)=D_{e_j}f(a)=\frac{\partial f}{\partial x_j}(a)$ is the $j$-th *partial derivative*.

:::

::: {#fig-derivative-of-maps-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-2.2,0) -- (2.4,0) node[lab, right] {$x$}; \draw[->, faint] (0,-1.6) -- (0,1.8) node[lab, above] {$y$};
\draw[faint] (0,0) ellipse (0.60 and 0.42);
\draw[faint] (0,0) ellipse (1.20 and 0.84);
\draw[faint] (0,0) ellipse (1.80 and 1.26);
\node[dot] at (0.9,0.5) {}; \node[lab, below right] at (0.9,0.5) {$a$};
\draw[hl] (0.2,0.15) -- (2.0,1.05); \draw[->, emph] (0.9,0.5) -- (1.6,0.85) node[lab, above] {$v$};
\node[lab, left] at (0.25,0.2) {$a+tv$};
\end{tikzpicture}
\end{center}
```

The directional derivative $D_vf(a)$ is the rate of change of $f$ along the line $a+tv$ (orange) through $a$; the partial derivatives are the cases $v=e_1$, $v=e_2$. Ellipses: level curves of $f$.

:::

::: {#prp-derivative-partials-jacobian .proposition name="The derivative determines the partial derivatives"}

If $f:U\to\mathbb R^m$ is differentiable at $a$, then every directional derivative exists and $D_vf(a)=Df(a)v$. In particular $Df(a)$ is the matrix of partial derivatives (the *Jacobian matrix*)
$$Df(a)=\Bigl(\frac{\partial f_i}{\partial x_j}(a)\Bigr)_{1\le i\le m,\ 1\le j\le n},$$
and for $m=1$, $Df(a)v=\nabla f(a)\cdot v$ with $\nabla f(a)$ the gradient (@def-gradient).

:::

::: {.proof}

1. For $v\ne0$ put $h=tv$: $\Bigl\|\frac{f(a+tv)-f(a)}t-Df(a)v\Bigr\|=\frac{\|f(a+tv)-f(a)-Df(a)(tv)\|}{\|tv\|}\|v\|\to0$ as $t\to0$. For $v=0$ both sides are $0$.

2. The $j$-th column of a matrix is its value on $e_j$, which is $D_jf(a)$; its $i$-th entry is $D_jf_i(a)$.

:::

The converse fails badly: partial derivatives, even all directional derivatives, may exist without $f$ being differentiable.

::: {#exm-partials-without-derivative .example name="Partial derivatives are not enough"}

1. Let $f(x,y)=\frac{xy}{x^2+y^2}$ for $(x,y)\ne0$ and $f(0)=0$. Since $f=0$ on both axes, $D_1f(0)=D_2f(0)=0$. But $f(t,t)=\frac12$ for $t\ne0$, so $f$ is not even continuous at $0$, hence not differentiable there.
2. Let $g(x,y)=\frac{x^2y}{x^2+y^2}$ for $(x,y)\ne0$ and $g(0)=0$. It is continuous ($|g|\le|y|$), and for $v=(v_1,v_2)\ne0$, $\frac{g(tv)}t=\frac{v_1^2v_2}{v_1^2+v_2^2}$, so every $D_vg(0)$ exists. But $v\mapsto D_vg(0)$ is not linear ($D_{e_1}g(0)=D_{e_2}g(0)=0$ while $D_{(1,1)}g(0)=\frac12$), so by @prp-derivative-partials-jacobian $g$ is not differentiable at $0$.

:::

::: {#fig-derivative-of-maps-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,0) -- (1.600,0.000); \node[lab, tick] at (1.850,0.000) {$0$};
\draw[hl] (0,0) -- (1.131,1.131); \node[lab, tick] at (1.308,1.308) {$\tfrac12$};
\draw[faint] (0,0) -- (0.000,1.600); \node[lab, tick] at (0.000,1.850) {$0$};
\draw[hl] (0,0) -- (-1.131,1.131); \node[lab, tick] at (-1.308,1.308) {$-\tfrac12$};
\draw[faint] (0,0) -- (-1.600,0.000); \node[lab, tick] at (-1.850,0.000) {$0$};
\draw[hl] (0,0) -- (-1.131,-1.131); \node[lab, tick] at (-1.308,-1.308) {$\tfrac12$};
\draw[faint] (0,0) -- (-0.000,-1.600); \node[lab, tick] at (-0.000,-1.850) {$0$};
\draw[hl] (0,0) -- (1.131,-1.131); \node[lab, tick] at (1.308,-1.308) {$-\tfrac12$};\node[hollow dot] at (0,0) {};
\end{tikzpicture}
\end{center}
```

Part 1: $f=\frac{xy}{x^2+y^2}$ is constant along each line through $0$, with the values shown. It is $0$ on the axes, so both partial derivatives at $0$ exist, but it takes the values $\pm\frac12$ arbitrarily close to $0$, so $f$ is not even continuous there.

:::

::: {#thm-continuous-partials-differentiable .theorem name="Continuous partial derivatives imply differentiability"}

Let $f:U\to\mathbb R^m$ and $a\in U$. If all partial derivatives $D_jf$ exist on a neighbourhood of $a$ and are continuous at $a$, then $f$ is differentiable at $a$.

:::

::: {.proof}

1. By @prp-derivative-several-variables-basic we may assume $m=1$. Let $A$ be the linear map with matrix $(D_1f(a),\dots,D_nf(a))$; we show $f(a+h)-f(a)-Ah=o(\|h\|)$, using $\|\cdot\|_2$.

2. *Move along the axes.* For small $h$, put $p_0=a$ and $p_j=a+h_1e_1+\dots+h_je_j$, so $p_n=a+h$ and all $p_j$ lie in a ball around $a$ on which the partial derivatives exist. Then
$$f(a+h)-f(a)=\sum_{j=1}^n\bigl(f(p_j)-f(p_{j-1})\bigr).$$

3. *Mean value theorem on each segment.* $p_j$ and $p_{j-1}$ differ only in coordinate $j$, so $t\mapsto f(p_{j-1}+te_j)$ is differentiable on $[0,h_j]$ with derivative $D_jf(p_{j-1}+te_j)$. By @thm-mean-value there is $q_j$ on the segment from $p_{j-1}$ to $p_j$ with $f(p_j)-f(p_{j-1})=h_jD_jf(q_j)$.

4. *Estimate.* Hence
$$|f(a+h)-f(a)-Ah|=\Bigl|\sum_jh_j\bigl(D_jf(q_j)-D_jf(a)\bigr)\Bigr|\le\|h\|_2\sum_j|D_jf(q_j)-D_jf(a)|.$$
As $h\to0$, every $q_j\to a$ (it lies within $\|h\|_2$ of $a$), so by continuity of $D_jf$ at $a$ the sum tends to $0$. So the error is $o(\|h\|_2)$.

:::

For example, $f(x,y)=(e^x\cos y,\ e^x\sin y)$ has continuous partial derivatives everywhere, so it is differentiable with
$$Df(x,y)=\begin{pmatrix}e^x\cos y&-e^x\sin y\\e^x\sin y&e^x\cos y\end{pmatrix}.$$
