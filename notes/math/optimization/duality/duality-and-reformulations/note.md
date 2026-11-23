---
title: "Duality, Reformulations and Generalized Inequalities"
sources: [ee364a-5]
requires: [math/optimization/duality/lagrange-dual-problem, math/optimization/convex-problems/semidefinite-programs]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on duality, in our own wording; proofs written out in steps. -->

Equivalent problems can have very different duals. Introducing variables, making constraints explicit or implicit, and allowing generalized inequalities all change the dual, often making it more useful.

::: {#exm-dual-new-variables .example name="Introducing new variables"}

Unconstrained $\min_x f_0(Ax+b)$ has the trivial dual $g=p^\star$. Rewrite it as minimize $f_0(y)$ subject to $Ax+b-y=0$. Then
$$g(\nu)=\inf_{x,y}\big(f_0(y)-\nu^{\mathsf T}y+\nu^{\mathsf T}Ax+b^{\mathsf T}\nu\big)=\begin{cases}b^{\mathsf T}\nu-f_0^*(\nu)&\text{if }A^{\mathsf T}\nu=0,\\-\infty&\text{otherwise.}\end{cases}$$
For norm approximation, minimize $\lVert Ax-b\rVert$, this gives the dual: maximize $b^{\mathsf T}\nu$ subject to $A^{\mathsf T}\nu=0$, $\lVert\nu\rVert_*\le1$.

:::

::: {#fig-duality-and-reformulations-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (a) at (0,0) {$\min_x f_0(Ax+b)$};
\node[box] (b) at (4.6,0) {$\min f_0(y)$\\ s.t. $y=Ax+b$};
\node[hl box] (c) at (9.4,0) {$\max\ b^{\mathsf T}\nu-f_0^*(\nu)$\\ s.t. $A^{\mathsf T}\nu=0$};
\draw[map] (a) -- node[lab, above] {new variable} (b);
\draw[map] (b) -- node[lab, above] {dual} (c);
\draw[map, dashed] (a.south) .. controls (2,-1.3) and (7,-1.3) .. node[lab, below] {dual: trivial, $g=p^\star$} (c.south);
\end{tikzpicture}
\end{center}
```

Dualizing the unconstrained problem directly gives nothing useful; introducing $y=Ax+b$ as a variable with an equality constraint first gives a dual in terms of the conjugate $f_0^*$.

:::

::: {#exm-dual-implicit-constraints .example name="Implicit constraints"}

The LP with box constraints, minimize $c^{\mathsf T}x$ subject to $Ax=b$, $-\mathbf 1\preceq x\preceq\mathbf 1$, has dual maximize $-b^{\mathsf T}\nu-\mathbf 1^{\mathsf T}\lambda_1-\mathbf 1^{\mathsf T}\lambda_2$ subject to $c+A^{\mathsf T}\nu+\lambda_1-\lambda_2=0$, $\lambda_1,\lambda_2\succeq0$. Making the box implicit, $f_0(x)=c^{\mathsf T}x$ on $\operatorname{dom}f_0=\{-\mathbf 1\preceq x\preceq\mathbf 1\}$, gives
$$g(\nu)=\inf_{-\mathbf 1\preceq x\preceq\mathbf 1}(c^{\mathsf T}x+\nu^{\mathsf T}(Ax-b))=-b^{\mathsf T}\nu-\lVert A^{\mathsf T}\nu+c\rVert_1,$$
an unconstrained dual.

:::

::: {#fig-duality-and-reformulations-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-2.6,0) -- (2.4,0) node[lab, right] {$\nu$};
\draw[->, faint] (0,-2.6) -- (0,0.8) node[lab, above] {};
\draw[hl] (-2.4,-0.8) -- (-2.38,-0.79) -- (-2.36,-0.78) -- (-2.33,-0.77) -- (-2.31,-0.76) -- (-2.29,-0.75) -- (-2.27,-0.73) -- (-2.25,-0.72) -- (-2.22,-0.71) -- (-2.2,-0.7) -- (-2.18,-0.69) -- (-2.16,-0.68) -- (-2.14,-0.67) -- (-2.11,-0.66) -- (-2.09,-0.65) -- (-2.07,-0.64) -- (-2.05,-0.62) -- (-2.03,-0.61) -- (-2,-0.6) -- (-1.98,-0.59) -- (-1.96,-0.58) -- (-1.94,-0.57) -- (-1.92,-0.56) -- (-1.89,-0.55) -- (-1.87,-0.54) -- (-1.85,-0.52) -- (-1.83,-0.51) -- (-1.81,-0.5) -- (-1.78,-0.49) -- (-1.76,-0.48) -- (-1.74,-0.47) -- (-1.72,-0.46) -- (-1.7,-0.45) -- (-1.67,-0.44) -- (-1.65,-0.43) -- (-1.63,-0.42) -- (-1.61,-0.4) -- (-1.59,-0.39) -- (-1.56,-0.38) -- (-1.54,-0.37) -- (-1.52,-0.36) -- (-1.5,-0.35) -- (-1.48,-0.34) -- (-1.45,-0.33) -- (-1.43,-0.32) -- (-1.41,-0.3) -- (-1.39,-0.29) -- (-1.37,-0.28) -- (-1.34,-0.27) -- (-1.32,-0.26) -- (-1.3,-0.25) -- (-1.28,-0.24) -- (-1.26,-0.23) -- (-1.23,-0.22) -- (-1.21,-0.21) -- (-1.19,-0.19) -- (-1.17,-0.18) -- (-1.15,-0.17) -- (-1.12,-0.16) -- (-1.1,-0.15) -- (-1.08,-0.14) -- (-1.06,-0.13) -- (-1.04,-0.12) -- (-1.01,-0.11) -- (-0.99,-0.1) -- (-0.97,-0.08) -- (-0.95,-0.07) -- (-0.93,-0.06) -- (-0.9,-0.05) -- (-0.88,-0.04) -- (-0.86,-0.03) -- (-0.84,-0.02) -- (-0.82,-0.01) -- (-0.79,0) -- (-0.77,0.01) -- (-0.75,0.03) -- (-0.73,0.04) -- (-0.71,0.05) -- (-0.68,0.06) -- (-0.66,0.07) -- (-0.64,0.08) -- (-0.62,0.09) -- (-0.6,0.1) -- (-0.57,0.11) -- (-0.55,0.12) -- (-0.53,0.14) -- (-0.51,0.15) -- (-0.49,0.16) -- (-0.46,0.17) -- (-0.44,0.18) -- (-0.42,0.19) -- (-0.4,0.2) -- (-0.38,0.16) -- (-0.35,0.13) -- (-0.33,0.1) -- (-0.31,0.06) -- (-0.29,0.03) -- (-0.27,-0) -- (-0.24,-0.03) -- (-0.22,-0.07) -- (-0.2,-0.1) -- (-0.18,-0.13) -- (-0.16,-0.17) -- (-0.13,-0.2) -- (-0.11,-0.23) -- (-0.09,-0.27) -- (-0.07,-0.3) -- (-0.05,-0.33) -- (-0.02,-0.36) -- (-0,-0.4) -- (0.02,-0.43) -- (0.04,-0.46) -- (0.06,-0.5) -- (0.09,-0.53) -- (0.11,-0.56) -- (0.13,-0.6) -- (0.15,-0.63) -- (0.17,-0.66) -- (0.2,-0.69) -- (0.22,-0.73) -- (0.24,-0.76) -- (0.26,-0.79) -- (0.28,-0.83) -- (0.31,-0.86) -- (0.33,-0.89) -- (0.35,-0.93) -- (0.37,-0.96) -- (0.39,-0.99) -- (0.42,-1.02) -- (0.44,-1.06) -- (0.46,-1.09) -- (0.48,-1.12) -- (0.5,-1.16) -- (0.53,-1.19) -- (0.55,-1.22) -- (0.57,-1.26) -- (0.59,-1.29) -- (0.61,-1.32) -- (0.64,-1.35) -- (0.66,-1.39) -- (0.68,-1.42) -- (0.7,-1.45) -- (0.72,-1.49) -- (0.75,-1.52) -- (0.77,-1.55) -- (0.79,-1.58) -- (0.81,-1.62) -- (0.83,-1.65) -- (0.86,-1.68) -- (0.88,-1.72) -- (0.9,-1.75) -- (0.92,-1.78) -- (0.94,-1.82) -- (0.97,-1.85) -- (0.99,-1.88) -- (1.01,-1.92) -- (1.03,-1.95) -- (1.05,-1.98) -- (1.08,-2.01) -- (1.1,-2.05) -- (1.12,-2.08) -- (1.14,-2.11) -- (1.16,-2.15) -- (1.19,-2.18) -- (1.21,-2.21) -- (1.23,-2.25) -- (1.25,-2.28) -- (1.27,-2.31) -- (1.3,-2.34) -- (1.32,-2.38) -- (1.34,-2.41) -- (1.36,-2.44) -- (1.38,-2.48) -- (1.41,-2.51) -- (1.43,-2.54) -- (1.45,-2.58) -- (1.47,-2.61) -- (1.49,-2.64) -- (1.52,-2.67) -- (1.54,-2.71) -- (1.56,-2.74) -- (1.58,-2.77) -- (1.6,-2.81) -- (1.63,-2.84) -- (1.65,-2.87) -- (1.67,-2.91) -- (1.69,-2.94) -- (1.71,-2.97) -- (1.74,-3) -- (1.76,-3.04) -- (1.78,-3.07) -- (1.8,-3.1) -- (1.82,-3.14) -- (1.85,-3.17) -- (1.87,-3.2) -- (1.89,-3.24) -- (1.91,-3.27) -- (1.93,-3.3) -- (1.96,-3.33) -- (1.98,-3.37) -- (2,-3.4);
\fill[ink] (-0.4,0.2) circle[pt] node[lab, above] {$\nu=-c/a$};
\end{tikzpicture}
\end{center}
```

Keeping the box $-1\le x\le1$ implicit makes the dual function finite everywhere: in one dimension with $a=1$, $b=0.5$, $c=0.4$, $g(\nu)=-b\nu-\lvert a\nu+c\rvert$ is concave and piecewise linear, with its kink where $a\nu+c=0$.

:::

::: {#def-dual-generalized-inequalities .definition name="Duality for generalized inequalities"}

For minimize $f_0(x)$ subject to $f_i(x)\preceq_{K_i}0$, $h_i(x)=0$, the Lagrangian is
$$L(x,\lambda_1,\dots,\lambda_m,\nu)=f_0(x)+\sum_i\lambda_i^{\mathsf T}f_i(x)+\sum_i\nu_ih_i(x),$$
and the dual problem maximizes $g=\inf_xL$ subject to $\lambda_i\succeq_{K_i^*}0$ (@def-dual-cone). The lower bound property, weak duality and, for convex problems with a strictly feasible point ($f_i(x)\prec_{K_i}0$), strong duality hold as before.

:::

::: {.proof}

1. Lower bound: for feasible $\tilde x$, $-f_i(\tilde x)\in K_i$ and $\lambda_i\in K_i^*$, so $\lambda_i^{\mathsf T}f_i(\tilde x)\le0$. Then $g\le L(\tilde x,\dots)\le f_0(\tilde x)$ as in @thm-dual-lower-bound.

:::

::: {#fig-duality-and-reformulations-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) -- (-1.73,-1) -- (-1.7,-1.05) -- (-1.67,-1.1) -- (-1.63,-1.15) -- (-1.6,-1.2) -- (-1.56,-1.25) -- (-1.52,-1.3) -- (-1.48,-1.34) -- (-1.44,-1.39) -- (-1.4,-1.43) -- (-1.35,-1.47) -- (-1.31,-1.52) -- (-1.26,-1.55) -- (-1.21,-1.59) -- (-1.16,-1.63) -- (-1.11,-1.66) -- (-1.06,-1.7) -- (-1.01,-1.73) -- (-0.95,-1.76) -- (-0.9,-1.79) -- (-0.85,-1.81) -- cycle;
\fill[tintB] (0,0) -- (1.63,-0.76) -- (1.71,-0.55) -- (1.77,-0.33) -- (1.8,-0.1) -- (1.8,0.13) -- (1.77,0.35) -- (1.71,0.57) -- (1.62,0.78) -- (1.51,0.98) -- (1.37,1.16) -- (1.22,1.33) -- (1.04,1.47) -- (0.85,1.59) -- (0.64,1.68) -- (0.42,1.75) -- (0.2,1.79) -- (-0.03,1.8) -- (-0.26,1.78) -- (-0.48,1.73) -- (-0.7,1.66) -- (-0.9,1.56) -- cycle;
\draw[emph] (-1.73,-1) -- (0,0) -- (-0.85,-1.81);
\draw[faint] (1.63,-0.76) -- (0,0) -- (-0.9,1.56);
\draw[->, hl] (0,0) -- (-1,-1.11) node[lab, left] {$f_i(x)$};
\draw[->, hl] (0,0) -- (0.7,1.21) node[lab, right] {$\lambda_i$};
\node[lab] at (-1.47,-1.63) {$-K$};
\node[lab] at (1.41,0.51) {$K^*$};
\end{tikzpicture}
\end{center}
```

Why the multiplier must lie in the dual cone: if $f_i(x)\preceq_K0$, that is $f_i(x)\in-K$, and $\lambda_i\in K^*$, then $\lambda_i^{\mathsf T}f_i(x)\le0$ (the angle between them is at least $90^\circ$), which gives the lower-bound property.

:::

::: {#exm-sdp-dual .example name="Semidefinite program"}

The SDP minimize $c^{\mathsf T}x$ subject to $x_1F_1+\cdots+x_nF_n\preceq G$ has Lagrangian $c^{\mathsf T}x+\operatorname{tr}\big(Z(\sum_ix_iF_i-G)\big)$ with $Z\succeq0$ (the semidefinite cone is self-dual, @exm-dual-cones). It is affine in $x$, so the dual is
$$\text{maximize }-\operatorname{tr}(GZ)\quad\text{s.t. }Z\succeq0,\ \operatorname{tr}(F_iZ)+c_i=0,\ i=1,\dots,n.$$
Strong duality holds if the primal LMI is strictly feasible.

:::

::: {#rmk-duality-and-reformulations-1 .remark name="No rule for the best form"}

There is no general rule for which equivalent form has the most useful dual. Common tricks: introduce variables for arguments of functions, move simple constraints into the domain, and replace the objective by an increasing function of it (for example minimize $\frac12\lVert y\rVert_2^2$ instead of $\lVert y\rVert_2$).

:::
