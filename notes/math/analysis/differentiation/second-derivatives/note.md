---
title: "Second Derivatives and Taylor's Theorem in Several Variables"
sources: [camib-at-a6, mit1802-8, mit1802-9, mit1802-10, mit1802n-TA, mit1802n-SD, mit1806-27]
requires: [math/analysis/differentiation/chain-rule-and-mean-value, math/analysis/real/differentiability/taylors-theorem, math/linear-algebra/positive-definite/positive-definite-matrices]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Analysis II (Michaelmas 2015 lecture notes), Section 6.5, in our own wording; the counterexample to symmetry was checked symbolically; the second derivative test is our own addition from the second-order Taylor theorem; proofs written out in steps. The calculus notes state the equality of mixed partials and the second derivative test for two variables with informal proofs; the rigorous versions here carry related= and merged 2026-11-20 (owner): thm-symmetry-mixed-partials replaces the calculus block thm-mixed-partials (MIT 18.02, Lecture 8-9, Supplementary Notes TA); thm-second-derivative-test-several replaces the calculus block thm-second-derivative-test-two-variables (MIT 18.02, Lectures 9-10, Supplementary Notes SD: part 4, the AC-B^2 form) and the linear-algebra block thm-second-derivative-test (MIT 18.06, Lecture 27: the smallest-eigenvalue bound in step 1). -->

The derivative $Df$ of a map is again a map, from $U$ to the space of linear maps. Differentiating it once more gives a symmetric bilinear form, the Hessian, which controls the second-order behaviour of $f$ and decides the nature of critical points.

Throughout, $U\subseteq\mathbb R^n$ is open, and $D_iD_jf=D_i(D_jf)$ means: first the partial derivative in direction $e_j$, then in direction $e_i$.

::: {#def-second-derivative-several .definition name="Second derivative" related="def-higher-partial-derivatives"}

Let $f:U\to\mathbb R^m$ be differentiable. $f$ is *twice differentiable* at $a$ if $Df:U\to L(\mathbb R^n;\mathbb R^m)$ is differentiable at $a$. Its derivative $D^2f(a)$ is a linear map $\mathbb R^n\to L(\mathbb R^n;\mathbb R^m)$, which we identify with the bilinear map
$$D^2f(a)(u,v)=\bigl(D^2f(a)u\bigr)v=\sum_{i,j=1}^nu_iv_j\,D_iD_jf(a).$$
$f$ is $C^2$ on $U$ if all second partial derivatives $D_iD_jf$ exist and are continuous on $U$.

:::

The formula holds because $D^2f(a)u$ is the derivative of $Df$ in the direction $u$ (@prp-derivative-partials-jacobian, applied to $Df$ entry by entry). The $j$-th column of $Df$ is $D_jf$, and its derivative in the direction $u$ is $\sum_iu_iD_iD_jf(a)$; applying the resulting linear map to $v=\sum_jv_je_j$ gives the double sum. By @thm-continuous-partials-differentiable applied to the partial derivatives $D_jf$, a $C^2$ map is twice differentiable at every point.

## Symmetry of mixed partial derivatives

::: {#exm-mixed-partials-differ .example name="Mixed partial derivatives can differ"}

Let $f(x,y)=\frac{xy(x^2-y^2)}{x^2+y^2}$ for $(x,y)\ne0$ and $f(0)=0$. One computes $D_1f(0,y)=-y$ and $D_2f(x,0)=x$ for all $x,y$. Hence $D_2D_1f(0)=-1$ but $D_1D_2f(0)=1$. The second partial derivatives exist everywhere but are not continuous at $0$.

:::

::: {#fig-second-derivatives-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) -- (1.500,0.000) arc (0:45:1.5) -- cycle;
\node[lab] at (0.924,0.383) {$+$};
\fill[tintB] (0,0) -- (1.061,1.061) arc (45:90:1.5) -- cycle;
\node[lab] at (0.383,0.924) {$-$};
\fill[tintA] (0,0) -- (0.000,1.500) arc (90:135:1.5) -- cycle;
\node[lab] at (-0.383,0.924) {$+$};
\fill[tintB] (0,0) -- (-1.061,1.061) arc (135:180:1.5) -- cycle;
\node[lab] at (-0.924,0.383) {$-$};
\fill[tintA] (0,0) -- (-1.500,0.000) arc (180:225:1.5) -- cycle;
\node[lab] at (-0.924,-0.383) {$+$};
\fill[tintB] (0,0) -- (-1.061,-1.061) arc (225:270:1.5) -- cycle;
\node[lab] at (-0.383,-0.924) {$-$};
\fill[tintA] (0,0) -- (-0.000,-1.500) arc (270:315:1.5) -- cycle;
\node[lab] at (0.383,-0.924) {$+$};
\fill[tintB] (0,0) -- (1.061,-1.061) arc (315:360:1.5) -- cycle;
\node[lab] at (0.924,-0.383) {$-$};
\draw[->, faint] (-1.8,0) -- (1.9,0) node[lab, right] {$x$}; \draw[->, faint] (0,-1.8) -- (0,1.9) node[lab, above] {$y$};
\end{tikzpicture}
\end{center}
```

Signs of $f=\frac{xy(x^2-y^2)}{x^2+y^2}=\frac{r^2}4\sin4\theta$ in the eight sectors. The second derivatives exist but are not continuous at $0$, and $D_1D_2f(0)\ne D_2D_1f(0)$.

:::

::: {#thm-symmetry-mixed-partials .theorem name="Symmetry of mixed partial derivatives"}

Let $f:U\to\mathbb R^m$, $a\in U$ and $i\ne j$. If $D_iD_jf$ and $D_jD_if$ exist on a neighbourhood of $a$ and are continuous at $a$, then $D_iD_jf(a)=D_jD_if(a)$. In particular, if $f$ is $C^2$ then $D^2f(a)$ is a symmetric bilinear form.

:::

::: {.proof}

1. *Reduce to two real variables.* Working component by component we may take $m=1$, and only the coordinates $i,j$ vary, so we may take $n=2$, $i=1$, $j=2$, $a=0$. The hypotheses include that $D_1f$ and $D_2f$ exist near $0$.

2. *A second difference.* For small $h,k\ne0$ let
$$\Delta(h,k)=f(h,k)-f(h,0)-f(0,k)+f(0,0).$$

3. *First way.* Let $\alpha(s)=f(s,k)-f(s,0)$, so $\Delta=\alpha(h)-\alpha(0)$. By @thm-mean-value, $\Delta=h\,\alpha'(s)=h\bigl(D_1f(s,k)-D_1f(s,0)\bigr)$ for some $s$ between $0$ and $h$. Applying the mean value theorem to $t\mapsto D_1f(s,t)$ gives $\Delta=hk\,D_2D_1f(s,t)$ for some $t$ between $0$ and $k$.

4. *Second way.* Starting from $\beta(t)=f(h,t)-f(0,t)$ in the same way gives $\Delta=hk\,D_1D_2f(s',t')$ for some $s'$ between $0$ and $h$ and $t'$ between $0$ and $k$.

5. *Let $h,k\to0$.* So $D_2D_1f(s,t)=D_1D_2f(s',t')$, where both points tend to $0$ as $(h,k)\to0$. By continuity at $0$, $D_2D_1f(0)=D_1D_2f(0)$.

6. If $f$ is $C^2$, all mixed partials are equal in pairs, so $D^2f(a)(u,v)=D^2f(a)(v,u)$ by the formula in @def-second-derivative-several.

:::

For $f:U\to\mathbb R$ of class $C^2$, the symmetric matrix $H_f(a)=\bigl(D_iD_jf(a)\bigr)_{i,j}$ is the *Hessian*; $D^2f(a)(u,v)=u^{\mathsf T}H_f(a)v$.

## Taylor's theorem and critical points

::: {#thm-taylor-second-order .theorem name="Second-order Taylor theorem"}

Let $f:U\to\mathbb R$ be $C^2$, $a\in U$ and $B_r(a)\subseteq U$. Then for $\|h\|<r$,
$$f(a+h)=f(a)+Df(a)h+\tfrac12D^2f(a)(h,h)+E(h),\qquad\frac{E(h)}{\|h\|^2}\to0\text{ as }h\to0.$$

:::

::: {.proof}

1. *Restrict to a line.* Fix $h$ with $0<\|h\|<r$ and let $g(t)=f(a+th)$ for $t$ in an open interval containing $[0,1]$. By the chain rule (@thm-chain-rule-several-variables), $g'(t)=Df(a+th)h=\sum_jh_jD_jf(a+th)$.

2. *Differentiate again.* Each $D_jf$ has continuous partial derivatives, hence is differentiable (@thm-continuous-partials-differentiable), so by the chain rule $g''(t)=\sum_{i,j}h_ih_jD_iD_jf(a+th)=D^2f(a+th)(h,h)$.

3. *One-variable Taylor.* By @thm-taylor-lagrange with $n=2$, $g(1)=g(0)+g'(0)+\frac12g''(s)$ for some $s\in(0,1)$. That is, the formula holds with
$$E(h)=\tfrac12\sum_{i,j}h_ih_j\bigl(D_iD_jf(a+sh)-D_iD_jf(a)\bigr).$$

4. *Estimate.* Since $|h_ih_j|\le\|h\|^2$, $\frac{|E(h)|}{\|h\|^2}\le\frac12\sum_{i,j}|D_iD_jf(a+sh)-D_iD_jf(a)|$, which tends to $0$ as $h\to0$ by continuity of the second partial derivatives at $a$.

:::

::: {#fig-second-derivatives-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (4.6,0) node[lab, right] {$t$};
\draw[->, faint] (0,-0.2) -- (0,2.0) node[lab, above] {};
\draw[emph] (0.000,0.800) -- (0.054,0.833) -- (0.107,0.866) -- (0.161,0.899) -- (0.215,0.932) -- (0.269,0.964) -- (0.322,0.995) -- (0.376,1.026) -- (0.430,1.055) -- (0.484,1.084) -- (0.537,1.111) -- (0.591,1.137) -- (0.645,1.162) -- (0.699,1.185) -- (0.752,1.207) -- (0.806,1.227) -- (0.860,1.246) -- (0.914,1.262) -- (0.967,1.277) -- (1.021,1.290) -- (1.075,1.302) -- (1.129,1.311) -- (1.182,1.318) -- (1.236,1.323) -- (1.290,1.327) -- (1.344,1.328) -- (1.397,1.328) -- (1.451,1.325) -- (1.505,1.321) -- (1.559,1.315) -- (1.613,1.307) -- (1.666,1.298) -- (1.720,1.287) -- (1.774,1.274) -- (1.827,1.260) -- (1.881,1.245) -- (1.935,1.228) -- (1.989,1.210) -- (2.042,1.191) -- (2.096,1.171) -- (2.150,1.151) -- (2.204,1.130) -- (2.257,1.108) -- (2.311,1.086) -- (2.365,1.063) -- (2.419,1.041) -- (2.472,1.018) -- (2.526,0.996) -- (2.580,0.974) -- (2.634,0.952) -- (2.688,0.931) -- (2.741,0.910) -- (2.795,0.891) -- (2.849,0.872) -- (2.902,0.854) -- (2.956,0.837) -- (3.010,0.822) -- (3.064,0.808) -- (3.117,0.796) -- (3.171,0.785) -- (3.225,0.775) -- (3.279,0.768) -- (3.332,0.762) -- (3.386,0.758) -- (3.440,0.756) -- (3.494,0.755) -- (3.548,0.757) -- (3.601,0.760) -- (3.655,0.766) -- (3.709,0.773) -- (3.763,0.783) -- (3.816,0.794) -- (3.870,0.807) -- (3.924,0.822) -- (3.978,0.839) -- (4.031,0.858) -- (4.085,0.878) -- (4.139,0.900) -- (4.192,0.923) -- (4.246,0.948) -- (4.300,0.974);
\draw[hl] (0.000,0.799) -- (0.036,0.827) -- (0.072,0.854) -- (0.107,0.881) -- (0.143,0.907) -- (0.179,0.932) -- (0.215,0.956) -- (0.251,0.979) -- (0.287,1.002) -- (0.322,1.024) -- (0.358,1.045) -- (0.394,1.065) -- (0.430,1.085) -- (0.466,1.104) -- (0.502,1.122) -- (0.537,1.139) -- (0.573,1.156) -- (0.609,1.172) -- (0.645,1.187) -- (0.681,1.201) -- (0.717,1.215) -- (0.752,1.227) -- (0.788,1.239) -- (0.824,1.251) -- (0.860,1.261) -- (0.896,1.271) -- (0.932,1.280) -- (0.967,1.288) -- (1.003,1.296) -- (1.039,1.303) -- (1.075,1.308) -- (1.111,1.314) -- (1.147,1.318) -- (1.183,1.322) -- (1.218,1.325) -- (1.254,1.327) -- (1.290,1.328) -- (1.326,1.329) -- (1.362,1.329) -- (1.397,1.328) -- (1.433,1.327) -- (1.469,1.324) -- (1.505,1.321) -- (1.541,1.317) -- (1.577,1.313) -- (1.613,1.307) -- (1.648,1.301) -- (1.684,1.294) -- (1.720,1.287) -- (1.756,1.278) -- (1.792,1.269) -- (1.827,1.259) -- (1.863,1.248) -- (1.899,1.237) -- (1.935,1.225) -- (1.971,1.212) -- (2.007,1.198) -- (2.042,1.184) -- (2.078,1.168) -- (2.114,1.152) -- (2.150,1.136) -- (2.186,1.118) -- (2.222,1.100) -- (2.257,1.081) -- (2.293,1.061) -- (2.329,1.040) -- (2.365,1.019) -- (2.401,0.997) -- (2.437,0.974) -- (2.472,0.951) -- (2.508,0.926) -- (2.544,0.901) -- (2.580,0.875) -- (2.616,0.849) -- (2.652,0.821) -- (2.688,0.793) -- (2.723,0.764) -- (2.759,0.735) -- (2.795,0.704) -- (2.831,0.673) -- (2.867,0.641) -- (2.903,0.609) -- (2.938,0.575) -- (2.974,0.541) -- (3.010,0.506) -- (3.046,0.470) -- (3.082,0.434) -- (3.117,0.397) -- (3.153,0.359) -- (3.189,0.320) -- (3.225,0.281) -- (3.261,0.240) -- (3.297,0.199) -- (3.333,0.158) -- (3.368,0.115) -- (3.404,0.072) -- (3.440,0.028) -- (3.476,-0.017) -- (3.512,-0.063);
\node[dot] at (1.600,1.309) {};\draw[faint] (1.600,-0.06) -- (1.600,0.06); \node[lab, tick, below] at (1.600,-0.05) {$0$};
\end{tikzpicture}
\end{center}
```

Second-order Taylor along a line: $t\mapsto f(a+th)$ (dark) and its quadratic approximation $f(a)+tDf(a)h+\frac{t^2}2D^2f(a)(h,h)$ (orange) agree up to $o(t^2)$.

:::

::: {#thm-second-derivative-test-several .theorem name="Second derivative test"}

Let $f:U\to\mathbb R$ be $C^2$ and $Df(a)=0$.

1. If $H_f(a)$ is positive definite (@def-positive-definite), $f$ has a strict local minimum at $a$.
2. If $H_f(a)$ is negative definite, $f$ has a strict local maximum at $a$.
3. If $u^{\mathsf T}H_f(a)u>0>v^{\mathsf T}H_f(a)v$ for some $u,v$ (indefinite), $f$ has neither at $a$.
4. For $n=2$, with $A=D_1D_1f(a)$, $B=D_1D_2f(a)$, $C=D_2D_2f(a)$: if $AC-B^2>0$ and $A>0$ there is a strict local minimum, if $AC-B^2>0$ and $A<0$ a strict local maximum, and if $AC-B^2<0$ neither (a saddle point). If $AC-B^2=0$ the test gives no conclusion.

:::

::: {.proof}

1. *A uniform lower bound.* The unit sphere $S=\{\|u\|=1\}$ is closed and bounded, hence sequentially compact (@thm-heine-borel-rn), and $u\mapsto u^{\mathsf T}H_f(a)u$ is continuous and positive on it. By @cor-extreme-value-compact it attains a minimum $\mu>0$. By homogeneity, $h^{\mathsf T}H_f(a)h\ge\mu\|h\|^2$ for all $h$. (Alternatively, $\mu$ is the smallest eigenvalue of $H_f(a)$, positive by @thm-positive-definite-tests.)

2. *Positive definite.* By @thm-taylor-second-order with $Df(a)=0$,
$$f(a+h)-f(a)=\tfrac12h^{\mathsf T}H_f(a)h+E(h)\ge\Bigl(\frac\mu2-\frac{|E(h)|}{\|h\|^2}\Bigr)\|h\|^2.$$
Choose $\rho>0$ with $\frac{|E(h)|}{\|h\|^2}<\frac\mu2$ for $0<\|h\|<\rho$. Then $f(a+h)>f(a)$ for those $h$.

3. *Negative definite:* apply part 1 to $-f$.

4. *Indefinite.* For small $t\ne0$, $f(a+tu)-f(a)=t^2\bigl(\frac12u^{\mathsf T}H_f(a)u+\frac{E(tu)}{t^2}\bigr)$, and $\frac{E(tu)}{t^2}=\frac{E(tu)}{\|tu\|^2}\|u\|^2\to0$, so this is positive for small $t$. In the same way $f(a+tv)<f(a)$ for small $t\ne0$. So every neighbourhood of $a$ contains points with larger and with smaller values.

5. *Two variables.* $H_f(a)=\begin{pmatrix}A&B\\B&C\end{pmatrix}$ has determinant $AC-B^2$, the product of its two eigenvalues. If $AC-B^2>0$ the eigenvalues have the same sign, which is the sign of $A$ (the trace $A+C$ has the sign of $A$, since $AC>B^2\ge0$ forces $A$ and $C$ to have the same sign): positive definite if $A>0$, negative definite if $A<0$, so parts 1 and 2 apply. If $AC-B^2<0$ the eigenvalues have opposite signs and part 3 applies with eigenvectors as $u,v$.

6. *No conclusion when $AC-B^2=0$*: see the examples after the proof.

:::

::: {#fig-second-derivatives-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl] (0,0) ellipse (0.50 and 0.30);
\draw[faint] (0,0) ellipse (1.00 and 0.60);
\draw[faint] (0,0) ellipse (1.50 and 0.90);
\node[dot] at (0,0) {}; \node[lab, below] at (0,-1.0) {Hessian positive definite: minimum};
\draw[hl] (4.586,-0.389) -- (4.557,-0.343) -- (4.531,-0.300) -- (4.509,-0.258) -- (4.490,-0.218) -- (4.474,-0.180) -- (4.461,-0.143) -- (4.451,-0.106) -- (4.444,-0.070) -- (4.440,-0.035) -- (4.438,0.000) -- (4.440,0.035) -- (4.444,0.070) -- (4.451,0.106) -- (4.461,0.143) -- (4.474,0.180) -- (4.490,0.218) -- (4.509,0.258) -- (4.531,0.300) -- (4.557,0.343) -- (4.586,0.389);
\draw[faint] (3.611,0.586) -- (3.657,0.557) -- (3.700,0.531) -- (3.742,0.509) -- (3.782,0.490) -- (3.820,0.474) -- (3.857,0.461) -- (3.894,0.451) -- (3.930,0.444) -- (3.965,0.440) -- (4.000,0.438) -- (4.035,0.440) -- (4.070,0.444) -- (4.106,0.451) -- (4.143,0.461) -- (4.180,0.474) -- (4.218,0.490) -- (4.258,0.509) -- (4.300,0.531) -- (4.343,0.557) -- (4.389,0.586);
\draw[hl] (3.414,-0.389) -- (3.443,-0.343) -- (3.469,-0.300) -- (3.491,-0.258) -- (3.510,-0.218) -- (3.526,-0.180) -- (3.539,-0.143) -- (3.549,-0.106) -- (3.556,-0.070) -- (3.560,-0.035) -- (3.562,0.000) -- (3.560,0.035) -- (3.556,0.070) -- (3.549,0.106) -- (3.539,0.143) -- (3.526,0.180) -- (3.510,0.218) -- (3.491,0.258) -- (3.469,0.300) -- (3.443,0.343) -- (3.414,0.389);
\draw[faint] (3.611,-0.586) -- (3.657,-0.557) -- (3.700,-0.531) -- (3.742,-0.509) -- (3.782,-0.490) -- (3.820,-0.474) -- (3.857,-0.461) -- (3.894,-0.451) -- (3.930,-0.444) -- (3.965,-0.440) -- (4.000,-0.438) -- (4.035,-0.440) -- (4.070,-0.444) -- (4.106,-0.451) -- (4.143,-0.461) -- (4.180,-0.474) -- (4.218,-0.490) -- (4.258,-0.509) -- (4.300,-0.531) -- (4.343,-0.557) -- (4.389,-0.586);
\draw[hl] (4.957,-0.635) -- (4.909,-0.561) -- (4.867,-0.490) -- (4.831,-0.422) -- (4.800,-0.357) -- (4.774,-0.294) -- (4.752,-0.233) -- (4.736,-0.173) -- (4.725,-0.115) -- (4.718,-0.057) -- (4.716,0.000) -- (4.718,0.057) -- (4.725,0.115) -- (4.736,0.173) -- (4.752,0.233) -- (4.774,0.294) -- (4.800,0.357) -- (4.831,0.422) -- (4.867,0.490) -- (4.909,0.561) -- (4.957,0.635);
\draw[faint] (3.365,0.957) -- (3.439,0.909) -- (3.510,0.867) -- (3.578,0.831) -- (3.643,0.800) -- (3.706,0.774) -- (3.767,0.752) -- (3.827,0.736) -- (3.885,0.725) -- (3.943,0.718) -- (4.000,0.716) -- (4.057,0.718) -- (4.115,0.725) -- (4.173,0.736) -- (4.233,0.752) -- (4.294,0.774) -- (4.357,0.800) -- (4.422,0.831) -- (4.490,0.867) -- (4.561,0.909) -- (4.635,0.957);
\draw[hl] (3.043,-0.635) -- (3.091,-0.561) -- (3.133,-0.490) -- (3.169,-0.422) -- (3.200,-0.357) -- (3.226,-0.294) -- (3.248,-0.233) -- (3.264,-0.173) -- (3.275,-0.115) -- (3.282,-0.057) -- (3.284,0.000) -- (3.282,0.057) -- (3.275,0.115) -- (3.264,0.173) -- (3.248,0.233) -- (3.226,0.294) -- (3.200,0.357) -- (3.169,0.422) -- (3.133,0.490) -- (3.091,0.561) -- (3.043,0.635);
\draw[faint] (3.365,-0.957) -- (3.439,-0.909) -- (3.510,-0.867) -- (3.578,-0.831) -- (3.643,-0.800) -- (3.706,-0.774) -- (3.767,-0.752) -- (3.827,-0.736) -- (3.885,-0.725) -- (3.943,-0.718) -- (4.000,-0.716) -- (4.057,-0.718) -- (4.115,-0.725) -- (4.173,-0.736) -- (4.233,-0.752) -- (4.294,-0.774) -- (4.357,-0.800) -- (4.422,-0.831) -- (4.490,-0.867) -- (4.561,-0.909) -- (4.635,-0.957);
\node[dot] at (4,0) {}; \node[lab, below] at (4,-1.0) {indefinite: saddle};
\end{tikzpicture}
\end{center}
```

Level curves near a critical point: closed ovals around a minimum when the Hessian is positive definite, and hyperbolas around a saddle when it is indefinite (orange: values above $f(a)$, grey: below).

:::

When $H_f(a)$ is only semidefinite the test is silent: $x^4+y^4$, $-x^4-y^4$ and $x^4-y^4$ all have $Df(0)=0$ and $H_f(0)=0$, with a minimum, a maximum and neither at $0$.
