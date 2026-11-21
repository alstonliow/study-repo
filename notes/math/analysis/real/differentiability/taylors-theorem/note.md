---
title: "Local Inverses and Taylor's Theorem"
sources: [cama1-5, mit1801-37]
requires: [math/analysis/real/differentiability/differentiability-and-inverses, math/calculus/single-variable/applications-of-derivatives/mean-value-theorem]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Section 5.3, in our own wording; proofs written out in steps. Rolle's theorem, the mean value theorem and its consequences are already proved in @sec-math-calculus-single-variable-applications-of-derivatives-mean-value-theorem; Merged 2026-11-20 (owner): Taylor's formula with remainder from MIT 18.01 Lecture 37 (former id thm-taylor-remainder, no proof) was removed; @thm-taylor-lagrange is the single version, with the 18.01 $R_n$ notation added after it. -->

The mean value theorem (@thm-mean-value) is the bridge from information about $f'$ to information about $f$: for instance $f'>0$ on an interval makes $f$ strictly increasing (@cor-sign-of-derivative). This note uses it twice more: to invert functions locally, and, through a higher-order Rolle's theorem, to prove Taylor's theorem.

## Local inverses

::: {#thm-local-inverse-function .theorem name="Inverse function theorem in one variable"}

Let $f$ have a continuous derivative on $(a,b)$, and let $x\in(a,b)$ with $f'(x)\ne0$. Then there is an open interval $I\ni x$ such that $f$ restricted to $I$ is injective, and its inverse $g:f(I)\to I$ is differentiable with
$$g'(f(z))=\frac1{f'(z)}\quad\text{for all }z\in I.$$

:::

::: {.proof}

1. Say $f'(x)>0$ (otherwise use $-f$). Since $f'$ is continuous, there is $\delta>0$ with $f'>0$ on $(x-\delta,x+\delta)$.

2. By @cor-sign-of-derivative, $f$ is strictly increasing on $(x-\delta,x+\delta)$; it is continuous there by @thm-differentiable-continuous.

3. Let $I=(x-\delta/2,x+\delta/2)$. On the closed interval $[x-\delta/2,x+\delta/2]$, $f$ is continuous, strictly increasing and has non-zero derivative inside, so @thm-inverse-differentiable gives the inverse and its derivative at every point of $f(I)$.

:::

::: {#fig-taylors-theorem-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (4.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,2.2) node[lab, above] {$y$};
\draw[emph] (0.000,0.500) -- (0.054,0.558) -- (0.107,0.616) -- (0.161,0.674) -- (0.215,0.731) -- (0.269,0.787) -- (0.322,0.843) -- (0.376,0.899) -- (0.430,0.953) -- (0.484,1.006) -- (0.537,1.058) -- (0.591,1.109) -- (0.645,1.158) -- (0.699,1.206) -- (0.752,1.252) -- (0.806,1.296) -- (0.860,1.339) -- (0.914,1.379) -- (0.967,1.418) -- (1.021,1.454) -- (1.075,1.488) -- (1.129,1.520) -- (1.182,1.549) -- (1.236,1.576) -- (1.290,1.601) -- (1.344,1.622) -- (1.397,1.642) -- (1.451,1.658) -- (1.505,1.672) -- (1.559,1.683) -- (1.613,1.691) -- (1.666,1.697) -- (1.720,1.700) -- (1.774,1.700) -- (1.827,1.697) -- (1.881,1.691) -- (1.935,1.683) -- (1.989,1.671) -- (2.042,1.657) -- (2.096,1.641) -- (2.150,1.621) -- (2.204,1.599) -- (2.257,1.575) -- (2.311,1.548) -- (2.365,1.518) -- (2.419,1.486) -- (2.472,1.452) -- (2.526,1.416) -- (2.580,1.377) -- (2.634,1.336) -- (2.688,1.294) -- (2.741,1.249) -- (2.795,1.203) -- (2.849,1.155) -- (2.902,1.106) -- (2.956,1.055) -- (3.010,1.003) -- (3.064,0.950) -- (3.117,0.895) -- (3.171,0.840) -- (3.225,0.784) -- (3.279,0.727) -- (3.332,0.670) -- (3.386,0.613) -- (3.440,0.555) -- (3.494,0.497) -- (3.548,0.439) -- (3.601,0.381) -- (3.655,0.323) -- (3.709,0.266) -- (3.763,0.209) -- (3.816,0.153) -- (3.870,0.098) -- (3.924,0.044) -- (3.978,-0.009) -- (4.031,-0.061) -- (4.085,-0.112) -- (4.139,-0.161) -- (4.192,-0.209) -- (4.246,-0.255) -- (4.300,-0.299);
\fill[tintA] (0.6,0) rectangle (1.6,2.0);
\draw[hl] (0.600,1.117) -- (0.612,1.129) -- (0.625,1.140) -- (0.637,1.151) -- (0.650,1.163) -- (0.662,1.174) -- (0.675,1.185) -- (0.688,1.196) -- (0.700,1.207) -- (0.713,1.218) -- (0.725,1.229) -- (0.738,1.239) -- (0.750,1.250) -- (0.762,1.260) -- (0.775,1.271) -- (0.787,1.281) -- (0.800,1.291) -- (0.812,1.301) -- (0.825,1.311) -- (0.837,1.321) -- (0.850,1.331) -- (0.863,1.341) -- (0.875,1.350) -- (0.887,1.360) -- (0.900,1.369) -- (0.912,1.378) -- (0.925,1.388) -- (0.938,1.397) -- (0.950,1.405) -- (0.962,1.414) -- (0.975,1.423) -- (0.988,1.432) -- (1.000,1.440) -- (1.012,1.448) -- (1.025,1.457) -- (1.038,1.465) -- (1.050,1.473) -- (1.062,1.480) -- (1.075,1.488) -- (1.087,1.496) -- (1.100,1.503) -- (1.112,1.511) -- (1.125,1.518) -- (1.137,1.525) -- (1.150,1.532) -- (1.163,1.539) -- (1.175,1.545) -- (1.188,1.552) -- (1.200,1.558) -- (1.212,1.565) -- (1.225,1.571) -- (1.237,1.577) -- (1.250,1.583) -- (1.262,1.588) -- (1.275,1.594) -- (1.288,1.600) -- (1.300,1.605) -- (1.312,1.610) -- (1.325,1.615) -- (1.337,1.620) -- (1.350,1.625) -- (1.362,1.629) -- (1.375,1.634) -- (1.387,1.638) -- (1.400,1.643) -- (1.413,1.647) -- (1.425,1.650) -- (1.438,1.654) -- (1.450,1.658) -- (1.462,1.661) -- (1.475,1.665) -- (1.487,1.668) -- (1.500,1.671) -- (1.512,1.674) -- (1.525,1.676) -- (1.538,1.679) -- (1.550,1.682) -- (1.562,1.684) -- (1.575,1.686) -- (1.587,1.688) -- (1.600,1.690);
\draw[faint] (1.100,-0.06) -- (1.100,0.06); \node[lab, tick, below] at (1.100,-0.05) {$a$};\node[dot] at (1.100,1.503) {};
\node[lab, above] at (1.1,2.0) {$f'>0$ here};
\draw[faint, dashed] (1.745,1.700) -- (1.745,0); \node[lab, tick, below] at (1.745,-0.05) {$f'=0$};
\end{tikzpicture}
\end{center}
```

If $f'(a)\ne0$ and $f'$ is continuous, $f'$ keeps its sign near $a$, so $f$ is strictly monotone there and has a differentiable inverse on that piece (orange). Where $f'=0$, $f$ turns round and has no inverse nearby.

:::

Continuity of $f'$ is needed. The function $f(x)=x+2x^2\sin(1/x)$, $f(0)=0$, has $f'(0)=1$, but $f'$ takes negative values in every interval around $0$, so $f$ is not injective near $0$.

## Taylor's theorem

::: {#thm-higher-order-rolle .theorem name="Higher-order Rolle's theorem"}

Let $f$ be $n$ times differentiable on an open interval containing $[a,b]$, with
$$f(a)=f'(a)=\cdots=f^{(n-1)}(a)=0\quad\text{and}\quad f(b)=0.$$
Then $f^{(n)}(x)=0$ for some $x\in(a,b)$.

:::

::: {.proof}

1. Let $x_0=b$. We find $b=x_0>x_1>\cdots>x_n>a$ with $f^{(k)}(x_k)=0$ for each $k$.

2. Given $x_k$ with $k<n$: $f^{(k)}(a)=0=f^{(k)}(x_k)$, and $f^{(k)}$ is differentiable (hence continuous) on $[a,x_k]$. Rolle's theorem (@thm-rolle) gives $x_{k+1}\in(a,x_k)$ with $f^{(k+1)}(x_{k+1})=0$.

3. After $n$ steps, $x=x_n$ works.

:::

::: {#fig-taylors-theorem-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,0) -- (6,0); \node[lab, left] at (0,0) {$f$};
\node[dot] at (0.500,0.000) {};
\node[dot] at (2.500,0.000) {};
\node[dot] at (4.000,0.000) {};
\node[dot] at (5.500,0.000) {};
\draw[faint] (0,-0.6) -- (6,-0.6); \node[lab, left] at (0,-0.6) {$f'$};
\node[hl dot] at (1.400,-0.600) {};
\node[hl dot] at (3.100,-0.600) {};
\node[hl dot] at (4.800,-0.600) {};
\draw[faint] (0,-1.2) -- (6,-1.2); \node[lab, left] at (0,-1.2) {$f''$};
\node[hl dot] at (2.300,-1.200) {};
\node[hl dot] at (4.000,-1.200) {};
\draw[faint] (0,-1.8) -- (6,-1.8); \node[lab, left] at (0,-1.8) {$f'''$};
\node[hl dot] at (3.200,-1.800) {};
\end{tikzpicture}
\end{center}
```

Higher-order Rolle: between two zeros of $f$ lies a zero of $f'$, so $n+1$ zeros of $f$ give $n$ zeros of $f'$, $n-1$ of $f''$, down to one zero of $f^{(n)}$.

:::

The polynomial $Q_k(x)=\frac{(x-a)^k}{k!}$ satisfies $Q_k^{(j)}(a)=1$ if $j=k$ and $0$ if $j\ne k$. Hence
$$P(x)=\sum_{k=0}^{n-1}f^{(k)}(a)\frac{(x-a)^k}{k!}$$
has the same first $n-1$ derivatives at $a$ as $f$, and the same value. It is the *Taylor polynomial* of degree $n-1$ of $f$ at $a$.

::: {#thm-taylor-lagrange .theorem name="Taylor's theorem with Lagrange remainder"}

Let $f$ be $n$ times differentiable on an open interval containing $a$ and $a+h$ ($h\ne0$). Then
$$f(a+h)=\sum_{k=0}^{n-1}\frac{f^{(k)}(a)}{k!}h^k+\frac{f^{(n)}(x)}{n!}h^n$$
for some $x$ strictly between $a$ and $a+h$.

:::

::: {.proof}

1. Take $h>0$ and write $b=a+h$. With $P$ the Taylor polynomial above, define
$$p(t)=P(t)+\frac{(t-a)^n}{(b-a)^n}\bigl(f(b)-P(b)\bigr).$$
The added term has derivatives of order $<n$ equal to $0$ at $a$, so $p^{(k)}(a)=f^{(k)}(a)$ for $k<n$, and $p(b)=f(b)$.

2. Apply @thm-higher-order-rolle to $f-p$: there is $x\in(a,b)$ with $f^{(n)}(x)=p^{(n)}(x)$.

3. $P$ has degree $n-1$, so $p^{(n)}$ is the constant $\frac{n!}{(b-a)^n}\bigl(f(b)-P(b)\bigr)$. Hence $f(b)=P(b)+\frac{(b-a)^n}{n!}f^{(n)}(x)$, which is the claim.

4. For $h<0$, apply steps 1–3 to $t\mapsto f(-t)$ at the point $-a$, whose $k$-th derivative is $(-1)^kf^{(k)}(-t)$.

:::

::: {#fig-taylors-theorem-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-3.2,0) -- (3.4,0) node[lab, right] {$x$};
\draw[->, faint] (0,-1.8) -- (0,1.9) node[lab, above] {$y$};
\draw[emph] (-2.880,0.443) -- (-2.808,0.360) -- (-2.736,0.275) -- (-2.664,0.187) -- (-2.592,0.098) -- (-2.520,0.008) -- (-2.448,-0.082) -- (-2.376,-0.171) -- (-2.304,-0.259) -- (-2.232,-0.344) -- (-2.160,-0.427) -- (-2.088,-0.507) -- (-2.016,-0.582) -- (-1.944,-0.653) -- (-1.872,-0.718) -- (-1.800,-0.778) -- (-1.728,-0.831) -- (-1.656,-0.878) -- (-1.584,-0.917) -- (-1.512,-0.949) -- (-1.440,-0.974) -- (-1.368,-0.990) -- (-1.296,-0.999) -- (-1.224,-0.999) -- (-1.152,-0.991) -- (-1.080,-0.976) -- (-1.008,-0.952) -- (-0.936,-0.921) -- (-0.864,-0.882) -- (-0.792,-0.836) -- (-0.720,-0.783) -- (-0.648,-0.724) -- (-0.576,-0.659) -- (-0.504,-0.589) -- (-0.432,-0.514) -- (-0.360,-0.435) -- (-0.288,-0.352) -- (-0.216,-0.267) -- (-0.144,-0.179) -- (-0.072,-0.090) -- (0.000,0.000) -- (0.072,0.090) -- (0.144,0.179) -- (0.216,0.267) -- (0.288,0.352) -- (0.360,0.435) -- (0.432,0.514) -- (0.504,0.589) -- (0.576,0.659) -- (0.648,0.724) -- (0.720,0.783) -- (0.792,0.836) -- (0.864,0.882) -- (0.936,0.921) -- (1.008,0.952) -- (1.080,0.976) -- (1.152,0.991) -- (1.224,0.999) -- (1.296,0.999) -- (1.368,0.990) -- (1.440,0.974) -- (1.512,0.949) -- (1.584,0.917) -- (1.656,0.878) -- (1.728,0.831) -- (1.800,0.778) -- (1.872,0.718) -- (1.944,0.653) -- (2.016,0.582) -- (2.088,0.507) -- (2.160,0.427) -- (2.232,0.344) -- (2.304,0.259) -- (2.376,0.171) -- (2.448,0.082) -- (2.520,-0.008) -- (2.592,-0.098) -- (2.664,-0.187) -- (2.736,-0.275) -- (2.808,-0.360) -- (2.880,-0.443);
\draw[faint] (-1.344,-1.680) -- (-1.296,-1.620) -- (-1.248,-1.560) -- (-1.200,-1.500) -- (-1.152,-1.440) -- (-1.104,-1.380) -- (-1.056,-1.320) -- (-1.008,-1.260) -- (-0.960,-1.200) -- (-0.912,-1.140) -- (-0.864,-1.080) -- (-0.816,-1.020) -- (-0.768,-0.960) -- (-0.720,-0.900) -- (-0.672,-0.840) -- (-0.624,-0.780) -- (-0.576,-0.720) -- (-0.528,-0.660) -- (-0.480,-0.600) -- (-0.432,-0.540) -- (-0.384,-0.480) -- (-0.336,-0.420) -- (-0.288,-0.360) -- (-0.240,-0.300) -- (-0.192,-0.240) -- (-0.144,-0.180) -- (-0.096,-0.120) -- (-0.048,-0.060) -- (0.000,0.000) -- (0.048,0.060) -- (0.096,0.120) -- (0.144,0.180) -- (0.192,0.240) -- (0.240,0.300) -- (0.288,0.360) -- (0.336,0.420) -- (0.384,0.480) -- (0.432,0.540) -- (0.480,0.600) -- (0.528,0.660) -- (0.576,0.720) -- (0.624,0.780) -- (0.672,0.840) -- (0.720,0.900) -- (0.768,0.960) -- (0.816,1.020) -- (0.864,1.080) -- (0.912,1.140) -- (0.960,1.200) -- (1.008,1.260) -- (1.056,1.320) -- (1.104,1.380) -- (1.152,1.440) -- (1.200,1.500) -- (1.248,1.560) -- (1.296,1.620) -- (1.344,1.680);
\draw[faint] (-2.400,1.500) -- (-2.352,1.295) -- (-2.304,1.101) -- (-2.256,0.918) -- (-2.208,0.744) -- (-2.160,0.581) -- (-2.112,0.427) -- (-2.064,0.282) -- (-2.016,0.147) -- (-1.968,0.021) -- (-1.920,-0.096) -- (-1.872,-0.205) -- (-1.824,-0.305) -- (-1.776,-0.396) -- (-1.728,-0.480) -- (-1.680,-0.556) -- (-1.632,-0.625) -- (-1.584,-0.686) -- (-1.536,-0.740) -- (-1.488,-0.788) -- (-1.440,-0.828) -- (-1.392,-0.862) -- (-1.344,-0.890) -- (-1.296,-0.911) -- (-1.248,-0.927) -- (-1.200,-0.938) -- (-1.152,-0.942) -- (-1.104,-0.942) -- (-1.056,-0.937) -- (-1.008,-0.927) -- (-0.960,-0.912) -- (-0.912,-0.893) -- (-0.864,-0.870) -- (-0.816,-0.843) -- (-0.768,-0.813) -- (-0.720,-0.778) -- (-0.672,-0.741) -- (-0.624,-0.701) -- (-0.576,-0.658) -- (-0.528,-0.612) -- (-0.480,-0.564) -- (-0.432,-0.514) -- (-0.384,-0.462) -- (-0.336,-0.408) -- (-0.288,-0.352) -- (-0.240,-0.296) -- (-0.192,-0.238) -- (-0.144,-0.179) -- (-0.096,-0.120) -- (-0.048,-0.060) -- (0.000,0.000) -- (0.048,0.060) -- (0.096,0.120) -- (0.144,0.179) -- (0.192,0.238) -- (0.240,0.295) -- (0.288,0.352) -- (0.336,0.408) -- (0.384,0.462) -- (0.432,0.514) -- (0.480,0.564) -- (0.528,0.612) -- (0.576,0.658) -- (0.624,0.701) -- (0.672,0.741) -- (0.720,0.778) -- (0.768,0.813) -- (0.816,0.843) -- (0.864,0.870) -- (0.912,0.893) -- (0.960,0.912) -- (1.008,0.927) -- (1.056,0.937) -- (1.104,0.942) -- (1.152,0.942) -- (1.200,0.938) -- (1.248,0.927) -- (1.296,0.911) -- (1.344,0.890) -- (1.392,0.862) -- (1.440,0.828) -- (1.488,0.788) -- (1.536,0.740) -- (1.584,0.686) -- (1.632,0.625) -- (1.680,0.556) -- (1.728,0.480) -- (1.776,0.396) -- (1.824,0.305) -- (1.872,0.205) -- (1.920,0.096) -- (1.968,-0.021) -- (2.016,-0.147) -- (2.064,-0.282) -- (2.112,-0.427) -- (2.160,-0.580) -- (2.208,-0.744) -- (2.256,-0.918) -- (2.304,-1.101) -- (2.352,-1.295) -- (2.400,-1.500);
\draw[hl] (-2.880,-0.863) -- (-2.832,-0.779) -- (-2.784,-0.709) -- (-2.736,-0.652) -- (-2.688,-0.607) -- (-2.640,-0.572) -- (-2.592,-0.547) -- (-2.544,-0.530) -- (-2.496,-0.522) -- (-2.448,-0.520) -- (-2.400,-0.525) -- (-2.352,-0.535) -- (-2.304,-0.550) -- (-2.256,-0.569) -- (-2.208,-0.591) -- (-2.160,-0.615) -- (-2.112,-0.642) -- (-2.064,-0.670) -- (-2.016,-0.700) -- (-1.968,-0.730) -- (-1.920,-0.760) -- (-1.872,-0.789) -- (-1.824,-0.818) -- (-1.776,-0.846) -- (-1.728,-0.872) -- (-1.680,-0.897) -- (-1.632,-0.919) -- (-1.584,-0.940) -- (-1.536,-0.958) -- (-1.488,-0.973) -- (-1.440,-0.985) -- (-1.392,-0.995) -- (-1.344,-1.001) -- (-1.296,-1.004) -- (-1.248,-1.004) -- (-1.200,-1.001) -- (-1.152,-0.994) -- (-1.104,-0.984) -- (-1.056,-0.970) -- (-1.008,-0.953) -- (-0.960,-0.933) -- (-0.912,-0.909) -- (-0.864,-0.882) -- (-0.816,-0.852) -- (-0.768,-0.819) -- (-0.720,-0.783) -- (-0.672,-0.745) -- (-0.624,-0.703) -- (-0.576,-0.659) -- (-0.528,-0.613) -- (-0.480,-0.565) -- (-0.432,-0.514) -- (-0.384,-0.462) -- (-0.336,-0.408) -- (-0.288,-0.352) -- (-0.240,-0.296) -- (-0.192,-0.238) -- (-0.144,-0.179) -- (-0.096,-0.120) -- (-0.048,-0.060) -- (0.000,0.000) -- (0.048,0.060) -- (0.096,0.120) -- (0.144,0.179) -- (0.192,0.238) -- (0.240,0.296) -- (0.288,0.352) -- (0.336,0.408) -- (0.384,0.462) -- (0.432,0.514) -- (0.480,0.565) -- (0.528,0.613) -- (0.576,0.659) -- (0.624,0.703) -- (0.672,0.745) -- (0.720,0.783) -- (0.768,0.819) -- (0.816,0.852) -- (0.864,0.882) -- (0.912,0.909) -- (0.960,0.933) -- (1.008,0.953) -- (1.056,0.970) -- (1.104,0.984) -- (1.152,0.994) -- (1.200,1.001) -- (1.248,1.004) -- (1.296,1.004) -- (1.344,1.001) -- (1.392,0.995) -- (1.440,0.985) -- (1.488,0.973) -- (1.536,0.958) -- (1.584,0.940) -- (1.632,0.919) -- (1.680,0.897) -- (1.728,0.872) -- (1.776,0.846) -- (1.824,0.818) -- (1.872,0.789) -- (1.920,0.760) -- (1.968,0.730) -- (2.016,0.700) -- (2.064,0.670) -- (2.112,0.642) -- (2.160,0.615) -- (2.208,0.591) -- (2.256,0.569) -- (2.304,0.550) -- (2.352,0.535) -- (2.400,0.525) -- (2.448,0.520) -- (2.496,0.522) -- (2.544,0.530) -- (2.592,0.547) -- (2.640,0.572) -- (2.688,0.607) -- (2.736,0.652) -- (2.784,0.709) -- (2.832,0.779) -- (2.880,0.863);
\node[lab, right] at (2.9,1.2) {$n=5$};
\end{tikzpicture}
\end{center}
```

Taylor polynomials of $\sin$ at $0$ of degree $1$, $3$, $5$ (orange). The Lagrange remainder $\frac{f^{(n+1)}(\xi)}{(n+1)!}x^{n+1}$ measures the gap; it is small near $0$ and grows with $\lvert x\rvert$.

:::

With $n+1$ in place of $n$ and $x=a+h$, this is the form used in single-variable calculus: $f(x)=\sum_{k=0}^n\frac{f^{(k)}(a)}{k!}(x-a)^k+R_n(x)$ with $R_n(x)=\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$ for some $c$ between $a$ and $x$.

If $|f^{(n)}|\le C$ near $a$, the remainder is at most $\frac{C}{n!}|h|^n$, which is $o(h^{n-1})$: the Taylor polynomial is then the best polynomial approximation of degree $n-1$ near $a$. Whether the full Taylor series converges to $f$ depends on how the remainder behaves as $n\to\infty$.

::: {#exm-taylors-theorem-1 .example name="A function equal to its derivative"}

Suppose $f:\mathbb R\to\mathbb R$ is differentiable with $f'=f$ and $f(0)=1$. Then for every $x$,
$$f(x)=\sum_{k=0}^\infty\frac{x^k}{k!}.$$
We cannot simply differentiate the series term by term: the sum rule covers finite sums only. Instead:

1. $f'=f$ is differentiable, so $f''=f'=f$, and inductively $f^{(n)}=f$ exists for all $n$, with $f^{(n)}(0)=1$.

2. By @thm-taylor-lagrange, $f(x)=\sum_{k=0}^{n-1}\frac{x^k}{k!}+\frac{f(u_n)}{n!}x^n$ for some $u_n$ between $0$ and $x$.

3. $f$ is continuous, hence bounded on the closed interval between $0$ and $x$, say by $C$ (@thm-extreme-value-proof). So the remainder is at most $\frac{C|x|^n}{n!}$.

4. $\frac{|x|^n}{n!}\to0$ for fixed $x$: once $n\ge2|x|$ each further factor $\frac{|x|}{n}$ is at most $\frac12$. So the partial sums converge to $f(x)$.

Whether such an $f$ exists is a separate question, answered in @sec-math-analysis-real-power-series-exponential-and-trigonometric-functions.

:::
