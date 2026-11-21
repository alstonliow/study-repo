---
title: "Measure Zero and Lebesgue's Criterion"
sources: [camib-at-a3]
requires: [math/analysis/real/integration/integrable-functions, math/analysis/real/continuity/compactness-of-closed-intervals]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Analysis II (Michaelmas 2015 lecture notes), Section 3.3 (non-examinable). The source states Lebesgue's theorem without proof; the proof here, via oscillation, is our own write-up of the standard argument, in steps. Kept because it prepares measure theory. -->

Continuous and monotone functions are integrable (@sec-math-analysis-real-integration-integrable-functions), and so are bounded functions with finitely many discontinuities. Lebesgue's criterion says exactly how large the set of discontinuities may be: it must be negligible in the following sense.

::: {#def-measure-zero .definition name="Set of measure zero"}

A set $A\subseteq\mathbb R$ has *measure zero* if for every $\varepsilon>0$ there are countably many (or finitely many) open intervals $I_1,I_2,\dots$ with
$$A\subseteq\bigcup_jI_j\qquad\text{and}\qquad\sum_j|I_j|<\varepsilon,$$
where $|I|$ is the length of the interval $I$.

:::

::: {#fig-lebesgue-criterion-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.2,0) -- (6.4,0);
\draw[hl] (2.200,0.15) -- (3.800,0.15); \node[dot] at (3.000,0) {};
\draw[hl] (1.600,0.3) -- (2.400,0.3); \node[dot] at (2.000,0) {};
\draw[hl] (3.800,0.45) -- (4.200,0.45); \node[dot] at (4.000,0) {};
\draw[hl] (1.400,0.6) -- (1.600,0.6); \node[dot] at (1.500,0) {};
\draw[hl] (4.450,0.75) -- (4.550,0.75); \node[dot] at (4.500,0) {};
\draw[hl] (1.175,0.9) -- (1.225,0.9); \node[dot] at (1.200,0) {};
\draw[hl] (2.388,1.05) -- (2.413,1.05); \node[dot] at (2.400,0) {};
\draw[hl] (3.594,1.2) -- (3.606,1.2); \node[dot] at (3.600,0) {};
\draw[hl] (4.797,1.35) -- (4.803,1.35); \node[dot] at (4.800,0) {};
\node[lab, below] at (3,-0.1) {$q_1,q_2,\dots$ (the rationals in $[0,1]$)};
\end{tikzpicture}
\end{center}
```

Countable sets have measure zero: cover the $n$-th point by an interval of length $\varepsilon/2^n$; the lengths add up to at most $\varepsilon$.

:::

::: {#prp-measure-zero-examples .proposition name="Sets of measure zero"}

1. Every countable set has measure zero.
2. A countable union of sets of measure zero has measure zero.
3. An interval $[a,b]$ with $a<b$ does not have measure zero.

:::

::: {.proof}

1. Let $A=\{a_1,a_2,\dots\}$ and $\varepsilon>0$. The intervals $I_j=\bigl(a_j-\frac{\varepsilon}{2^{j+2}},a_j+\frac{\varepsilon}{2^{j+2}}\bigr)$ cover $A$ and have total length $\sum_j\frac\varepsilon{2^{j+1}}=\frac\varepsilon2<\varepsilon$.

2. Let $A=\bigcup_kA_k$ with each $A_k$ of measure zero. Cover $A_k$ by intervals of total length less than $\frac\varepsilon{2^k}$. All these intervals together are countably many, cover $A$, and have total length less than $\sum_k\frac\varepsilon{2^k}=\varepsilon$.

3. Suppose $[a,b]$ is covered by open intervals $I_j$ with $\sum|I_j|<b-a$. By @thm-heine-borel-interval finitely many, $I_1,\dots,I_n$ say, already cover $[a,b]$. A finite union of intervals covering $[a,b]$ has total length at least $b-a$ (induct on $n$: the interval containing $a$ reaches some point $c>a$, and the others must cover $[c,b]$ if $c\le b$). This contradicts $\sum_{j\le n}|I_j|<b-a$.

:::

::: {#exm-cantor-set-measure-zero .example name="The Cantor set"}

Start from $C_0=[0,1]$ and obtain $C_{n+1}$ by removing the open middle third of each interval of $C_n$. Then $C_n$ is a union of $2^n$ closed intervals of length $3^{-n}$, of total length $(\frac23)^n\to0$. The Cantor set $C=\bigcap_nC_n$ lies in every $C_n$; slightly enlarging the intervals of $C_n$ to open ones shows that $C$ has measure zero. Yet $C$ is uncountable (its points are the numbers with a ternary expansion using only the digits $0$ and $2$), so part 1 of @prp-measure-zero-examples does not cover all measure-zero sets.

:::

::: {#fig-lebesgue-criterion-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[shade] (0.000,-0.06) rectangle (6.000,0.06);
\fill[shade] (0.000,-0.46) rectangle (2.000,-0.34);
\fill[shade] (4.000,-0.46) rectangle (6.000,-0.34);
\fill[shade] (0.000,-0.86) rectangle (0.667,-0.74);
\fill[shade] (1.333,-0.86) rectangle (2.000,-0.74);
\fill[shade] (4.000,-0.86) rectangle (4.667,-0.74);
\fill[shade] (5.333,-0.86) rectangle (6.000,-0.74);
\fill[shade] (0.000,-1.26) rectangle (0.222,-1.14);
\fill[shade] (0.444,-1.26) rectangle (0.667,-1.14);
\fill[shade] (1.333,-1.26) rectangle (1.556,-1.14);
\fill[shade] (1.778,-1.26) rectangle (2.000,-1.14);
\fill[shade] (4.000,-1.26) rectangle (4.222,-1.14);
\fill[shade] (4.444,-1.26) rectangle (4.667,-1.14);
\fill[shade] (5.333,-1.26) rectangle (5.556,-1.14);
\fill[shade] (5.778,-1.26) rectangle (6.000,-1.14);
\fill[hl cell] (0.000,-1.66) rectangle (0.074,-1.54);
\fill[hl cell] (0.148,-1.66) rectangle (0.222,-1.54);
\fill[hl cell] (0.444,-1.66) rectangle (0.519,-1.54);
\fill[hl cell] (0.593,-1.66) rectangle (0.667,-1.54);
\fill[hl cell] (1.333,-1.66) rectangle (1.407,-1.54);
\fill[hl cell] (1.481,-1.66) rectangle (1.556,-1.54);
\fill[hl cell] (1.778,-1.66) rectangle (1.852,-1.54);
\fill[hl cell] (1.926,-1.66) rectangle (2.000,-1.54);
\fill[hl cell] (4.000,-1.66) rectangle (4.074,-1.54);
\fill[hl cell] (4.148,-1.66) rectangle (4.222,-1.54);
\fill[hl cell] (4.444,-1.66) rectangle (4.519,-1.54);
\fill[hl cell] (4.593,-1.66) rectangle (4.667,-1.54);
\fill[hl cell] (5.333,-1.66) rectangle (5.407,-1.54);
\fill[hl cell] (5.481,-1.66) rectangle (5.556,-1.54);
\fill[hl cell] (5.778,-1.66) rectangle (5.852,-1.54);
\fill[hl cell] (5.926,-1.66) rectangle (6.000,-1.54);
\node[lab, left] at (-0.1,0) {$C_0$}; \node[lab, left] at (-0.1,-1.6) {$C_4$};
\end{tikzpicture}
\end{center}
```

The first steps of the Cantor set: each step removes the open middle third of every interval. $C_k$ is $2^k$ intervals of total length $(2/3)^k\to0$, so the Cantor set has measure zero.

:::

## Oscillation

::: {#def-oscillation .definition name="Oscillation"}

Let $f:[a,b]\to\mathbb R$ be bounded. The *oscillation* of $f$ on a set $S\subseteq[a,b]$ is $\omega_f(S)=\sup_Sf-\inf_Sf$, and the oscillation of $f$ at a point $x$ is
$$\omega_f(x)=\inf_{\delta>0}\omega_f\bigl((x-\delta,x+\delta)\cap[a,b]\bigr).$$

:::

::: {#fig-lebesgue-criterion-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (4.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,2.6) node[lab, above] {$y$};
\draw[emph] (0.200,0.540) -- (0.225,0.545) -- (0.250,0.550) -- (0.275,0.555) -- (0.300,0.560) -- (0.325,0.565) -- (0.350,0.570) -- (0.375,0.575) -- (0.400,0.580) -- (0.425,0.585) -- (0.450,0.590) -- (0.475,0.595) -- (0.500,0.600) -- (0.525,0.605) -- (0.550,0.610) -- (0.575,0.615) -- (0.600,0.620) -- (0.625,0.625) -- (0.650,0.630) -- (0.675,0.635) -- (0.700,0.640) -- (0.725,0.645) -- (0.750,0.650) -- (0.775,0.655) -- (0.800,0.660) -- (0.825,0.665) -- (0.850,0.670) -- (0.875,0.675) -- (0.900,0.680) -- (0.925,0.685) -- (0.950,0.690) -- (0.975,0.695) -- (1.000,0.700) -- (1.025,0.705) -- (1.050,0.710) -- (1.075,0.715) -- (1.100,0.720) -- (1.125,0.725) -- (1.150,0.730) -- (1.175,0.735) -- (1.200,0.740) -- (1.225,0.745) -- (1.250,0.750) -- (1.275,0.755) -- (1.300,0.760) -- (1.325,0.765) -- (1.350,0.770) -- (1.375,0.775) -- (1.400,0.780) -- (1.425,0.785) -- (1.450,0.790) -- (1.475,0.795) -- (1.500,0.800) -- (1.525,0.805) -- (1.550,0.810) -- (1.575,0.815) -- (1.600,0.820) -- (1.625,0.825) -- (1.650,0.830) -- (1.675,0.835) -- (1.700,0.840) -- (1.725,0.845) -- (1.750,0.850) -- (1.775,0.855) -- (1.800,0.860) -- (1.825,0.865) -- (1.850,0.870) -- (1.875,0.875) -- (1.900,0.880) -- (1.925,0.885) -- (1.950,0.890) -- (1.975,0.895) -- (2.000,0.900) -- (2.025,0.905) -- (2.050,0.910) -- (2.075,0.915) -- (2.100,0.920) -- (2.125,0.925) -- (2.150,0.930) -- (2.175,0.935) -- (2.200,0.940);
\draw[emph] (2.200,1.930) -- (2.226,1.934) -- (2.253,1.938) -- (2.279,1.942) -- (2.305,1.946) -- (2.331,1.950) -- (2.357,1.954) -- (2.384,1.958) -- (2.410,1.962) -- (2.436,1.965) -- (2.463,1.969) -- (2.489,1.973) -- (2.515,1.977) -- (2.541,1.981) -- (2.567,1.985) -- (2.594,1.989) -- (2.620,1.993) -- (2.646,1.997) -- (2.673,2.001) -- (2.699,2.005) -- (2.725,2.009) -- (2.751,2.013) -- (2.777,2.017) -- (2.804,2.021) -- (2.830,2.025) -- (2.856,2.028) -- (2.883,2.032) -- (2.909,2.036) -- (2.935,2.040) -- (2.961,2.044) -- (2.987,2.048) -- (3.014,2.052) -- (3.040,2.056) -- (3.066,2.060) -- (3.093,2.064) -- (3.119,2.068) -- (3.145,2.072) -- (3.171,2.076) -- (3.197,2.080) -- (3.224,2.084) -- (3.250,2.087) -- (3.276,2.091) -- (3.303,2.095) -- (3.329,2.099) -- (3.355,2.103) -- (3.381,2.107) -- (3.407,2.111) -- (3.434,2.115) -- (3.460,2.119) -- (3.486,2.123) -- (3.513,2.127) -- (3.539,2.131) -- (3.565,2.135) -- (3.591,2.139) -- (3.617,2.143) -- (3.644,2.147) -- (3.670,2.151) -- (3.696,2.154) -- (3.723,2.158) -- (3.749,2.162) -- (3.775,2.166) -- (3.801,2.170) -- (3.828,2.174) -- (3.854,2.178) -- (3.880,2.182) -- (3.906,2.186) -- (3.932,2.190) -- (3.959,2.194) -- (3.985,2.198) -- (4.011,2.202) -- (4.037,2.206) -- (4.064,2.210) -- (4.090,2.213) -- (4.116,2.217) -- (4.143,2.221) -- (4.169,2.225) -- (4.195,2.229) -- (4.221,2.233) -- (4.248,2.237) -- (4.274,2.241) -- (4.300,2.245);
\node[hollow dot] at (2.200,0.940) {};\node[dot] at (2.200,1.930) {};
\fill[tintA] (1.8,0) rectangle (2.6,2.4); \draw[decorate, decoration={brace, amplitude=3pt}] (2.75,1.99) -- node[lab, right=3pt] {$\omega_f(x)\approx$ jump} (2.75,0.86);\draw[faint] (2.200,-0.06) -- (2.200,0.06); \node[lab, tick, below] at (2.200,-0.05) {$x$};
\end{tikzpicture}
\end{center}
```

At a jump, every interval around $x$ (shaded) contains values near both levels, so the oscillation $\omega_f(x)$ is the height of the jump; $f$ is continuous at $x$ exactly when $\omega_f(x)=0$.

:::

Directly from the definitions, $f$ is continuous at $x$ if and only if $\omega_f(x)=0$. So the set $D_f$ of discontinuities of $f$ is $\bigcup_{m\ge1}D_{1/m}$, where $D_\eta=\{x:\omega_f(x)\ge\eta\}$.

::: {#lem-oscillation-set-closed .lemma name="Large oscillation is a closed condition"}

For every $\eta>0$, if $x\in[a,b]\setminus D_\eta$ then some open interval around $x$ misses $D_\eta$. Consequently every cover of $D_\eta$ by open intervals has a finite subcover.

:::

::: {.proof}

1. If $\omega_f(x)<\eta$, there is $\delta>0$ with $\omega_f(J)<\eta$ for $J=(x-\delta,x+\delta)\cap[a,b]$. Every $y\in(x-\delta,x+\delta)$ has a smaller interval around it inside $(x-\delta,x+\delta)$, on which the oscillation is at most $\omega_f(J)$. So $\omega_f(y)<\eta$.

2. Let $\mathcal I$ cover $D_\eta$ by open intervals. Add, for each $x\in[a,b]\setminus D_\eta$, an open interval around $x$ missing $D_\eta$ (step 1). Together they cover $[a,b]$, so by @thm-heine-borel-interval finitely many do. Discarding the added intervals, which contain no point of $D_\eta$, leaves finitely many members of $\mathcal I$ covering $D_\eta$.

:::

## Lebesgue's criterion

::: {#thm-lebesgue-criterion .theorem name="Lebesgue's criterion for Riemann integrability"}

A bounded function $f:[a,b]\to\mathbb R$ is Riemann integrable if and only if its set of discontinuities
$$D_f=\{x\in[a,b]:f\text{ is not continuous at }x\}$$
has measure zero.

:::

::: {.proof}

Let $|f|\le M$ with $M>0$, and use @thm-riemann-criterion throughout.

1. *Integrable implies $D_{\eta}$ has measure zero.* Fix $\eta>0$ and $\varepsilon>0$, and take a dissection $a=x_0<\dots<x_n=b$ with $U-L<\frac{\eta\varepsilon}2$. If $x\in D_\eta$ lies in the open interval $(x_{i-1},x_i)$, then $M_i-m_i\ge\omega_f(x)\ge\eta$. The total length of such subintervals is therefore at most $\frac{U-L}\eta<\frac\varepsilon2$. Every other point of $D_\eta$ is one of the finitely many $x_i$. Enlarging each of these subintervals slightly to an open interval and covering each $x_i$ by a short open interval gives a cover of $D_\eta$ of total length less than $\varepsilon$.

2. *Integrable implies $D_f$ has measure zero.* $D_f=\bigcup_mD_{1/m}$, a countable union of sets of measure zero by step 1, so part 2 of @prp-measure-zero-examples applies.

3. *Conversely, cover the bad set.* Suppose $D_f$ has measure zero and let $\varepsilon>0$. Put $\eta=\frac\varepsilon{2(b-a)}$. Since $D_\eta\subseteq D_f$, cover $D_\eta$ by open intervals of total length less than $\frac\varepsilon{4M}$; by @lem-oscillation-set-closed finitely many, $I_1,\dots,I_k$, suffice.

4. *Cover the good set.* Let $K=[a,b]\setminus(I_1\cup\dots\cup I_k)$. Each $x\in K$ has $\omega_f(x)<\eta$, so there is an open interval $J_x\ni x$ whose closure $\overline{J_x}$ satisfies $\omega_f(\overline{J_x}\cap[a,b])<\eta$ (take half of a suitable $\delta$). The $I_j$ and the $J_x$ cover $[a,b]$; by @thm-heine-borel-interval finitely many $J_{x_1},\dots,J_{x_l}$ together with $I_1,\dots,I_k$ do.

5. *The dissection.* Let $D$ consist of $a$, $b$ and all endpoints of $I_1,\dots,I_k,J_{x_1},\dots,J_{x_l}$ lying in $[a,b]$. Take a subinterval $[u,v]$ of $D$. Its interior contains no endpoint, so for each of the finitely many intervals it lies either inside or outside it. If $(u,v)$ lies inside some $I_j$, call $[u,v]$ *bad*; otherwise $(u,v)\subseteq K$, so it lies inside some $J_{x_i}$ and $\omega_f([u,v])<\eta$; call it *good*.

6. *Estimate.* Assign each bad subinterval to one $I_j$ containing its interior; those assigned to $I_j$ do not overlap, so their total length is at most $|I_j|$. Hence
$$U_D(f)-L_D(f)\le\sum_{\text{bad}}2M(v-u)+\sum_{\text{good}}\eta(v-u)<2M\cdot\frac\varepsilon{4M}+\eta(b-a)=\varepsilon.$$
By @thm-riemann-criterion, $f$ is integrable.

:::

::: {#cor-lebesgue-criterion-consequences .corollary name="Consequences"}

Let $f,g:[a,b]\to\mathbb R$ be Riemann integrable.

1. If $\varphi:[A,B]\to\mathbb R$ is continuous and $f([a,b])\subseteq[A,B]$, then $\varphi\circ f$ is integrable.
2. $fg$, $|f|$, $\max(f,g)$ and $\min(f,g)$ are integrable.
3. A uniform limit of integrable functions is integrable.

:::

::: {.proof}

1. $\varphi\circ f$ is bounded, and it is continuous wherever $f$ is, so $D_{\varphi\circ f}\subseteq D_f$. A subset of a measure-zero set has measure zero.

2. Each of these is bounded and continuous wherever both $f$ and $g$ are, so its discontinuities lie in $D_f\cup D_g$, of measure zero by @prp-measure-zero-examples.

3. If $f_n\to f$ uniformly, $f$ is continuous wherever all $f_n$ are (@thm-uniform-limit-continuous), so $D_f\subseteq\bigcup_nD_{f_n}$; $f$ is bounded as in @thm-uniform-limit-integral, which proves this part directly.

:::

::: {#rmk-lebesgue-criterion-1 .remark name="Towards measure theory"}

The definition of measure zero is the first step of Lebesgue measure: the outer measure of $A$ is the infimum of $\sum|I_j|$ over all countable covers of $A$ by open intervals, and measure zero means outer measure $0$. @exm-dirichlet-function is discontinuous everywhere, so @thm-lebesgue-criterion confirms it is not Riemann integrable; the Lebesgue integral will integrate it (to $0$), because $\mathbb Q\cap[0,1]$ has measure zero.

:::
