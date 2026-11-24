---
title: "Second-Order Linear Equations and Characteristic Roots"
sources: [mit1803-11, mit1803-12]
requires: [math/differential-equations/complex-and-sinusoids/sinusoidal-functions, math/differential-equations/first-order/first-order-linear-equations]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.03SC Differential Equations (Fall 2011), Sessions 11 (linear and nonlinear equations, superposition) and 12 (second-order physical systems, the characteristic polynomial, modes and roots), in our own wording; examples are ours, checked in Python; proofs written out in steps. The existence and uniqueness theorem is stated without proof, as in the course. -->

Second-order linear equations with constant coefficients model springs, pendulums at small amplitude and electric circuits. Their homogeneous solutions are built from exponentials whose rates are the roots of a polynomial.

::: {#def-linear-ode .definition name="Linear differential equation"}
A *linear differential equation* of order $n$ has the form
$$
a_n(t)\,y^{(n)} + \dots + a_1(t)\,y' + a_0(t)\,y = q(t),
$$
with $a_n\neq0$ on the interval considered. It is *homogeneous* if $q=0$ and has *constant coefficients* if all $a_k$ are constants.
:::

::: {#thm-superposition-linear .theorem name="Superposition"}
Write $L(y)=a_ny^{(n)}+\dots+a_0y$. Then $L(c_1y_1+c_2y_2)=c_1L(y_1)+c_2L(y_2)$. Consequently:

1. any linear combination of solutions of $L(y)=0$ is a solution;
2. if $L(y_1)=q_1$ and $L(y_2)=q_2$, then $L(c_1y_1+c_2y_2)=c_1q_1+c_2q_2$;
3. every solution of $L(y)=q$ is $y_p+y_h$, with $y_p$ one particular solution and $y_h$ a solution of $L(y)=0$.
:::

::: {.proof}
1. Differentiation is linear: $(c_1y_1+c_2y_2)^{(k)}=c_1y_1^{(k)}+c_2y_2^{(k)}$ for each $k$.

2. Multiplying by $a_k$ and summing over $k$ gives $L(c_1y_1+c_2y_2)=c_1L(y_1)+c_2L(y_2)$; statements 1 and 2 follow at once.

3. If $L(y)=q=L(y_p)$, then $L(y-y_p)=0$, so $y-y_p$ is a homogeneous solution.
:::

::: {#thm-existence-uniqueness-linear .theorem name="Existence and uniqueness for linear equations"}
If $a_0,\dots,a_n,q$ are continuous on an interval $I$ with $a_n\neq0$ there, then for each $t_0\in I$ and any numbers $b_0,\dots,b_{n-1}$ there is exactly one solution on all of $I$ with $y^{(k)}(t_0)=b_k$ for $k<n$. In particular, if $y_1,y_2$ solve a second-order homogeneous equation and neither is a constant multiple of the other, then $c_1y_1+c_2y_2$ is the general solution.
:::

::: {#exm-spring-mass-dashpot .example name="Mass, spring and dashpot"}
A mass $m$ on a spring of stiffness $k$, with a dashpot of damping constant $b$, moved by an external force $F(t)$, has displacement $x(t)$ satisfying
$$
m\,x''+b\,x'+k\,x = F(t),
$$
by Newton's second law with spring force $-kx$ and damping force $-bx'$. All three constants are positive (with $b=0$ for an undamped system).
:::

::: {#fig-second-order-linear-equations-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.25,-0.90) -- (0,-0.70); \draw[faint] (-0.25,-0.70) -- (0,-0.50); \draw[faint] (-0.25,-0.50) -- (0,-0.30); \draw[faint] (-0.25,-0.30) -- (0,-0.10); \draw[faint] (-0.25,-0.10) -- (0,0.10); \draw[faint] (-0.25,0.10) -- (0,0.30); \draw[faint] (-0.25,0.30) -- (0,0.50); \draw[faint] (-0.25,0.50) -- (0,0.70); \draw[faint] (-0.25,0.70) -- (0,0.90); \draw (0,-0.9) -- (0,0.9);
\draw (0,0.45) -- (0.30,0.33) -- (0.46,0.57) -- (0.62,0.33) -- (0.78,0.57) -- (0.94,0.33) -- (1.10,0.57) -- (1.26,0.33) -- (1.42,0.57) -- (1.58,0.33) -- (1.74,0.57) -- (1.9,0.45) -- (2.2,0.45); \node[lab, above] at (1.1,0.62) {spring $k$};
\draw (0,-0.45) -- (0.9,-0.45); \draw (0.9,-0.65) -- (0.9,-0.25); \draw (0.7,-0.7) -- (1.4,-0.7) -- (1.4,-0.2) -- (0.7,-0.2);
\draw (1.4,-0.45) -- (2.2,-0.45); \node[lab, below] at (1.05,-0.75) {dashpot $b$};
\node[box] (m) at (2.7,0) {$m$};
\draw[->, accent, emph] (3.2,0) -- (4.1,0) node[right, lab] {$F(t)$};
\draw[->] (2.7,-0.95) -- (3.4,-0.95) node[right, lab] {$x$};
\draw[faint] (2.7,-0.85) -- (2.7,-1.05);
\end{tikzpicture}
\end{center}
```

A mass on a spring with a dashpot, pushed by an external force. The spring pulls back with force $-kx$, the dashpot resists with $-bx'$.

:::

::: {#def-characteristic-polynomial .definition name="Characteristic polynomial"}
The *characteristic polynomial* of $a_ny^{(n)}+\dots+a_1y'+a_0y=0$ (constant coefficients) is
$$
p(s) = a_ns^n+\dots+a_1s+a_0 .
$$
Its roots are the *characteristic roots*. Since $(e^{rt})^{(k)}=r^ke^{rt}$, the function $e^{rt}$ is a solution exactly when $p(r)=0$; such exponential solutions are the *modes* of the system.
:::

::: {#thm-second-order-characteristic-roots .theorem name="Real solutions from characteristic roots"}
Let $p(s)=s^2+bs+c$ with real $b,c$. A basis of real solutions of $y''+by'+cy=0$ is:

1. $e^{r_1t},\ e^{r_2t}$ if $p$ has distinct real roots $r_1\neq r_2$;
2. $e^{rt},\ t\,e^{rt}$ if $p$ has a repeated root $r$;
3. $e^{at}\cos\omega t,\ e^{at}\sin\omega t$ if $p$ has complex roots $a\pm i\omega$, $\omega>0$.
:::

::: {.proof}
1. In case 1 both exponentials solve the equation (@def-characteristic-polynomial), and they are not multiples of each other since $r_1\neq r_2$.

2. In case 2, $p(s)=(s-r)^2$, so $b=-2r$ and $c=r^2$. For $y=te^{rt}$: $y'=(1+rt)e^{rt}$ and $y''=(2r+r^2t)e^{rt}$. Then $y''-2ry'+r^2y=e^{rt}\bigl(2r+r^2t-2r-2r^2t+r^2t\bigr)=0$.

3. In case 3, $z=e^{(a+i\omega)t}$ is a complex solution. Because the coefficients are real, the real and imaginary parts of $z$ are real solutions; they are $e^{at}\cos\omega t$ and $e^{at}\sin\omega t$ (@def-complex-exponential), and their ratio $\tan\omega t$ is not constant.

4. In each case @thm-existence-uniqueness-linear makes the two functions a basis.
:::

::: {#exm-characteristic-roots .example name="An initial value problem"}
Solve $y''+5y'+6y=0$, $y(0)=1$, $y'(0)=0$.

1. $p(s)=s^2+5s+6=(s+2)(s+3)$, so $y=c_1e^{-2t}+c_2e^{-3t}$.
2. The conditions give $c_1+c_2=1$ and $-2c_1-3c_2=0$, so $c_1=3$, $c_2=-2$.
3. Hence $y=3e^{-2t}-2e^{-3t}$.
:::

::: {#fig-second-order-linear-equations-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.4cm, y=0.65cm]
\draw[->] (0,0) -- (4.3,0) node[lab, right] {$t$};
\draw[->] (0,-2.2) -- (0,3.4) node[lab, above] {$y$};
\draw[muted, dashed] (0,3) -- (0.051,2.711) -- (0.101,2.45) -- (0.152,2.214) -- (0.203,2.001) -- (0.253,1.808) -- (0.304,1.634) -- (0.354,1.477) -- (0.405,1.334) -- (0.456,1.206) -- (0.506,1.09) -- (0.557,0.985) -- (0.608,0.89) -- (0.658,0.804) -- (0.709,0.727) -- (0.759,0.657) -- (0.81,0.594) -- (0.861,0.536) -- (0.911,0.485) -- (0.962,0.438) -- (1.013,0.396) -- (1.063,0.358) -- (1.114,0.323) -- (1.165,0.292) -- (1.215,0.264) -- (1.266,0.239) -- (1.316,0.216) -- (1.367,0.195) -- (1.418,0.176) -- (1.468,0.159) -- (1.519,0.144) -- (1.57,0.13) -- (1.62,0.117) -- (1.671,0.106) -- (1.722,0.096) -- (1.772,0.087) -- (1.823,0.078) -- (1.873,0.071) -- (1.924,0.064) -- (1.975,0.058) -- (2.025,0.052) -- (2.076,0.047) -- (2.127,0.043) -- (2.177,0.039) -- (2.228,0.035) -- (2.278,0.031) -- (2.329,0.028) -- (2.38,0.026) -- (2.43,0.023) -- (2.481,0.021) -- (2.532,0.019) -- (2.582,0.017) -- (2.633,0.015) -- (2.684,0.014) -- (2.734,0.013) -- (2.785,0.011) -- (2.835,0.01) -- (2.886,0.009) -- (2.937,0.008) -- (2.987,0.008) -- (3.038,0.007) -- (3.089,0.006) -- (3.139,0.006) -- (3.19,0.005) -- (3.241,0.005) -- (3.291,0.004) -- (3.342,0.004) -- (3.392,0.003) -- (3.443,0.003) -- (3.494,0.003) -- (3.544,0.003) -- (3.595,0.002) -- (3.646,0.002) -- (3.696,0.002) -- (3.747,0.002) -- (3.797,0.002) -- (3.848,0.001) -- (3.899,0.001) -- (3.949,0.001) -- (4,0.001);
\draw[muted, dashed] (0,-2) -- (0.051,-1.718) -- (0.101,-1.476) -- (0.152,-1.268) -- (0.203,-1.089) -- (0.253,-0.936) -- (0.304,-0.804) -- (0.354,-0.691) -- (0.405,-0.593) -- (0.456,-0.51) -- (0.506,-0.438) -- (0.557,-0.376) -- (0.608,-0.323) -- (0.658,-0.278) -- (0.709,-0.238) -- (0.759,-0.205) -- (0.81,-0.176) -- (0.861,-0.151) -- (0.911,-0.13) -- (0.962,-0.112) -- (1.013,-0.096) -- (1.063,-0.082) -- (1.114,-0.071) -- (1.165,-0.061) -- (1.215,-0.052) -- (1.266,-0.045) -- (1.316,-0.039) -- (1.367,-0.033) -- (1.418,-0.028) -- (1.468,-0.024) -- (1.519,-0.021) -- (1.57,-0.018) -- (1.62,-0.015) -- (1.671,-0.013) -- (1.722,-0.011) -- (1.772,-0.01) -- (1.823,-0.008) -- (1.873,-0.007) -- (1.924,-0.006) -- (1.975,-0.005) -- (2.025,-0.005) -- (2.076,-0.004) -- (2.127,-0.003) -- (2.177,-0.003) -- (2.228,-0.003) -- (2.278,-0.002) -- (2.329,-0.002) -- (2.38,-0.002) -- (2.43,-0.001) -- (2.481,-0.001) -- (2.532,-0.001) -- (2.582,-0.001) -- (2.633,-0.001) -- (2.684,-0.001) -- (2.734,-0.001) -- (2.785,0) -- (2.835,0) -- (2.886,0) -- (2.937,0) -- (2.987,0) -- (3.038,0) -- (3.089,0) -- (3.139,0) -- (3.19,0) -- (3.241,0) -- (3.291,0) -- (3.342,0) -- (3.392,0) -- (3.443,0) -- (3.494,0) -- (3.544,0) -- (3.595,0) -- (3.646,0) -- (3.696,0) -- (3.747,0) -- (3.797,0) -- (3.848,0) -- (3.899,0) -- (3.949,0) -- (4,0);
\draw[emph, primary] (0,1) -- (0.051,0.993) -- (0.101,0.974) -- (0.152,0.946) -- (0.203,0.911) -- (0.253,0.872) -- (0.304,0.83) -- (0.354,0.786) -- (0.405,0.741) -- (0.456,0.696) -- (0.506,0.652) -- (0.557,0.609) -- (0.608,0.567) -- (0.658,0.527) -- (0.709,0.488) -- (0.759,0.452) -- (0.81,0.418) -- (0.861,0.385) -- (0.911,0.355) -- (0.962,0.326) -- (1.013,0.3) -- (1.063,0.275) -- (1.114,0.253) -- (1.165,0.231) -- (1.215,0.212) -- (1.266,0.194) -- (1.316,0.177) -- (1.367,0.162) -- (1.418,0.148) -- (1.468,0.135) -- (1.519,0.123) -- (1.57,0.112) -- (1.62,0.102) -- (1.671,0.093) -- (1.722,0.084) -- (1.772,0.077) -- (1.823,0.07) -- (1.873,0.064) -- (1.924,0.058) -- (1.975,0.052) -- (2.025,0.048) -- (2.076,0.043) -- (2.127,0.039) -- (2.177,0.036) -- (2.228,0.032) -- (2.278,0.029) -- (2.329,0.027) -- (2.38,0.024) -- (2.43,0.022) -- (2.481,0.02) -- (2.532,0.018) -- (2.582,0.016) -- (2.633,0.015) -- (2.684,0.013) -- (2.734,0.012) -- (2.785,0.011) -- (2.835,0.01) -- (2.886,0.009) -- (2.937,0.008) -- (2.987,0.007) -- (3.038,0.007) -- (3.089,0.006) -- (3.139,0.005) -- (3.19,0.005) -- (3.241,0.004) -- (3.291,0.004) -- (3.342,0.004) -- (3.392,0.003) -- (3.443,0.003) -- (3.494,0.003) -- (3.544,0.002) -- (3.595,0.002) -- (3.646,0.002) -- (3.696,0.002) -- (3.747,0.002) -- (3.797,0.001) -- (3.848,0.001) -- (3.899,0.001) -- (3.949,0.001) -- (4,0.001);
\node[lab, note, muted, right] at (0.35,2.1) {$3e^{-2t}$}; \node[lab, note, muted, right] at (0.35,-1.2) {$-2e^{-3t}$};
\draw (0,1) -- (-0.08,1) node[left, lab, tick] {$1$};
\end{tikzpicture}
\end{center}
```

The solution $3e^{-2t}-2e^{-3t}$ (solid) of the initial value problem is a combination of the two modes (dashed); it starts at $1$ with slope $0$.

:::
