---
title: "Primal–Dual Interior-Point Methods for Conic Programs"
sources: [mit6854-14, mit6854-15]
requires: [math/optimization/algorithms/barrier-method, math/optimization/convex-problems/semidefinite-programs]
status: draft
---

<!-- Added 2026-11-26 from MIT 6.854J (Fall 2008, Goemans), Lectures 14 and 15, in our own wording; proofs written out in steps; the path-following theorem and the distance lemma are stated without proof, as in the course. -->

Interior-point methods (Karmarkar, 1984) solve linear programs in polynomial time by moving through the interior of the feasible region instead of along its edges, and since the 1990s they solve semidefinite programs as well. Both are cases of *conic programming*, which lets one treat them together. The barrier method of @def-barrier-method is the primal side of the same idea; here the primal and the dual are followed together.

## Conic programs and their duals

::: {#def-conic-program .definition name="Conic program and its dual" related="def-dual-generalized-inequalities"}

Let $K$ be a closed convex cone in a space with inner product $\langle\cdot,\cdot\rangle$, and $K^*=\{s:\langle s,x\rangle\ge0\text{ for all }x\in K\}$ its *dual cone*. For a linear map $A$ with adjoint $A^*$ ($\langle A^*y,x\rangle=\langle y,Ax\rangle$), the *primal* and *dual* conic programs are
$$\text{(P)}\ \ \min\{\langle c,x\rangle:Ax=b,\ x\in K\},\qquad\text{(D)}\ \ \max\{\langle b,y\rangle:A^*y+s=c,\ s\in K^*\}.$$

:::

1. *Linear programming:* $K=K^*=\mathbb R^n_+$ with the dot product, $A^*=A^{\mathsf T}$.
2. *Semidefinite programming:* $K=K^*=\mathbb S^p_+$, the positive semidefinite $p\times p$ matrices, with $\langle X,Y\rangle=X\bullet Y=\operatorname{tr}(XY)$; then $AX=(A_1\bullet X,\dots,A_m\bullet X)$ and $A^*y=\sum_iy_iA_i$. Writing the lower triangle of $X$ as a vector with off-diagonal entries multiplied by $\sqrt2$ turns $X\bullet Y$ into a dot product.

Both cones are *self-dual*. For $\mathbb S^p_+$ this rests on the following fact.

::: {#lem-psd-inner-product .lemma name="Positive semidefinite matrices have non-negative inner products"}

If $X,Y\succeq0$ then $X\bullet Y\ge0$.

:::

::: {.proof}

1. Write $X=V^{\mathsf T}V$ (for instance $V=X^{1/2}$).

2. $X\bullet Y=\operatorname{tr}(V^{\mathsf T}VY)=\operatorname{tr}(VYV^{\mathsf T})$, using $\operatorname{tr}(CD)=\operatorname{tr}(DC)$.

3. $VYV^{\mathsf T}\succeq0$ since $z^{\mathsf T}VYV^{\mathsf T}z=(V^{\mathsf T}z)^{\mathsf T}Y(V^{\mathsf T}z)\ge0$, so its trace, the sum of its eigenvalues, is non-negative.

:::

::: {#thm-conic-duality .theorem name="Conic duality"}

1. *Weak duality:* for feasible $x$ and $(y,s)$, $\langle c,x\rangle-\langle b,y\rangle=\langle s,x\rangle\ge0$.
2. *Strong duality:* if (P) has a feasible $x$ in the interior of $K$ and (D) a feasible $s$ in the interior of $K^*$, both optima are attained and equal.

:::

::: {.proof}

1. $\langle c,x\rangle=\langle A^*y+s,x\rangle=\langle y,Ax\rangle+\langle s,x\rangle=\langle b,y\rangle+\langle s,x\rangle$, and $\langle s,x\rangle\ge0$ by the definition of $K^*$.

2. Strong duality is stated without proof (it follows from Slater's condition, @thm-weak-strong-duality).

:::

For linear programs strict feasibility is not needed. For semidefinite programs it is: without it the optimum may be an unattained infimum, one side may be infeasible while the other is finite, or both may be finite with different values.

## Barriers and the central path

::: {#def-conic-barrier .definition name="Barrier, barrier problems, central path"}

A *barrier* for $K$ is a strictly convex function $F$ on the interior of $K$ with $F(x)\to\infty$ as $x$ approaches the boundary. The canonical barriers are
$$F(x)=-\sum_j\ln x_j\ \ (K=\mathbb R^n_+),\qquad F(X)=-\ln\det X\ \ (K=\mathbb S^p_+).$$
For $\mu>0$ the *barrier problems* are
$$\text{(BP}_\mu)\ \ \min\{\langle c,x\rangle+\mu F(x):Ax=b\},\qquad\text{(BD}_\mu)\ \ \max\{\langle b,y\rangle-\mu F_*(s):A^*y+s=c\},$$
with $F_*$ the canonical barrier of $K^*$. Their unique optima $x(\mu)$ and $(y(\mu),s(\mu))$ form the *central path*.

:::

::: {#thm-central-path-conditions .theorem name="Central path conditions" related="thm-central-path-duality-gap"}

$x$ is optimal for (BP$_\mu$) if and only if there are $y,s$ with $Ax=b$, $A^*y+s=c$ and
$$x_js_j=\mu\ \text{for all }j\ \ (\text{LP}),\qquad XS=\mu I\ \ (\text{SDP}).$$
The same conditions characterise the optimum of (BD$_\mu$), so $\big(x(\mu),y(\mu),s(\mu)\big)$ solves both, and the duality gap on the central path is
$$\langle x(\mu),s(\mu)\rangle=n\mu\ \ (\text{LP}),\qquad p\mu\ \ (\text{SDP}).$$

:::

::: {.proof}

1. (BP$_\mu$) minimises a strictly convex function over an affine set, so $x$ is optimal exactly when the gradient $c+\mu\nabla F(x)$ is orthogonal to $\{h:Ah=0\}$, that is, equals $A^*y$ for some $y$. Put $s=-\mu\nabla F(x)$; then $A^*y+s=c$.

2. For $F(x)=-\sum\ln x_j$, $\nabla F(x)=-(1/x_1,\dots,1/x_n)$, so $s_j=\mu/x_j$, i.e. $x_js_j=\mu$, and $s>0$ lies in $K^*$.

3. For $F(X)=-\ln\det X$, $\partial\det X/\partial x_{ij}$ is the cofactor of $(i,j)$, so $\nabla F(X)=-X^{-1}$ and $S=\mu X^{-1}$, i.e. $XS=\mu I$, with $S\succ0$.

4. The dual barrier problem gives, in the same way, $Ax=b$ with $x=-\mu\nabla F_*(s)$, which is the same condition.

5. The gap is $\langle x,s\rangle=\sum_jx_j\mu/x_j=n\mu$, respectively $\operatorname{tr}(X\cdot\mu X^{-1})=p\mu$.

:::

So as $\mu\to0$ the central path converges to optimal solutions of (P) and (D). In general the barrier is *$\nu$-logarithmically homogeneous*, $F(\tau x)=F(x)-\nu\ln\tau$ for $\tau>0$, with $\nu=n$ for $\mathbb R^n_+$ and $\nu=p$ for $\mathbb S^p_+$; the gap on the path is $\nu\mu$. Both canonical barriers are also self-concordant (@def-self-concordant).

## Following the path

Measure the distance of a pair $(x,s)$ from the central point for $\mu$ by the local norm $\lVert v\rVert_x=\sqrt{v^{\mathsf T}\nabla^2F(x)^{-1}v}$:
$$d_\mu(x,s)=\Big\lVert\frac s\mu+\nabla F(x)\Big\rVert_x,$$
which is $0$ exactly on the central path. For LP, $\nabla^2F(x)=\operatorname{diag}(1/x_j^2)$, so
$$d_\mu(x,s)=\sqrt{\sum_j\Big(\frac{x_js_j}{\mu}-1\Big)^2},$$
and for SDP, $d_\mu(X,S)=\big\lVert\mu^{-1}X^{1/2}SX^{1/2}-I\big\rVert_F$.

::: {#lem-near-path-gap .lemma name="Near the path the gap is small"}

If $d_\mu(x,s)\le1$ then $\langle x,s\rangle\le2\nu\mu$.

:::

For LP this is immediate: $|x_js_j/\mu-1|\le1$ gives $x_js_j\le2\mu$ for every $j$.

::: {#def-primal-dual-ipm .definition name="Primal–dual path following"}

Start with strictly feasible $x_0$, $(y_0,s_0)$ and $\mu_0$ with $d_{\mu_0}(x_0,s_0)\le0.1$. At step $k$:

1. set $\mu_{k+1}=\mu_k/(1+0.1/\sqrt\nu)$;
2. compute the next point by one Newton step on the central path equations $Ax=b$, $A^*y+s=c$, $s+\mu_{k+1}\nabla F(x)=0$, linearising $\nabla F(x_k+\Delta x)\approx\nabla F(x_k)+\nabla^2F(x_k)\Delta x$ and solving the linear system for $(\Delta x,\Delta y,\Delta s)$.

Stop when $\langle x_k,s_k\rangle\le\varepsilon$.

:::

::: {#fig-primal-dual-interior-point-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.4]
\fill[tintA] (0,0)--(2,0)--(1.6,1.2)--(0,2)--cycle;
\draw[emph] (0,0)--(2,0)--(1.6,1.2)--(0,2)--cycle;
\draw[hl] (0.685,0.727) -- (0.686,0.728) -- (0.687,0.729) -- (0.688,0.730) -- (0.689,0.731) -- (0.691,0.733) -- (0.694,0.736) -- (0.697,0.739) -- (0.701,0.744) -- (0.706,0.749) -- (0.713,0.756) -- (0.722,0.765) -- (0.733,0.777) -- (0.747,0.792) -- (0.766,0.810) -- (0.789,0.833) -- (0.819,0.861) -- (0.855,0.894) -- (0.901,0.931) -- (0.955,0.971) -- (1.018,1.010) -- (1.087,1.046) -- (1.160,1.076) -- (1.232,1.100) -- (1.299,1.119) -- (1.358,1.134) -- (1.407,1.146) -- (1.448,1.156) -- (1.481,1.165) -- (1.507,1.172) -- (1.527,1.178) -- (1.543,1.182) -- (1.556,1.186) -- (1.566,1.189) -- (1.573,1.191) -- (1.579,1.193) -- (1.584,1.195) -- (1.588,1.196) -- (1.590,1.197) -- (1.593,1.198);
\node[dot] at (0.685,0.727) {};
\node[hl dot] at (1.6,1.2) {};
\node[lab, below] at (0.685,0.677) {$\mu\to\infty$};
\node[lab, above right] at (1.6,1.2) {$\mu\to0$};
\end{tikzpicture}
\end{center}
```

The central path of the program of @exm-simplex-small ($\min -x_1-x_2$ over the shaded polygon): it starts at the analytic centre ($\mu\to\infty$) and runs through the interior to the optimal vertex $(\tfrac85,\tfrac65)$; path following stays close to it.

:::

```{=latex}
\begin{algorithm}
\caption{Short-step primal--dual path following}
\begin{algorithmic}
\INPUT strictly feasible $x_0$, $(y_0,s_0)$, $\mu_0$ with $d_{\mu_0}(x_0,s_0)\le0.1$; accuracy $\varepsilon$
\OUTPUT feasible $x$, $(y,s)$ with duality gap at most $\varepsilon$
\STATE $k\gets0$
\WHILE{$\langle x_k,s_k\rangle>\varepsilon$}
\STATE $\mu_{k+1}\gets\mu_k/(1+0.1/\sqrt\nu)$
\STATE solve $A\Delta x=0$, $A^*\Delta y+\Delta s=0$, $s_k+\Delta s+\mu_{k+1}\big(\nabla F(x_k)+\nabla^2F(x_k)\Delta x\big)=0$
\STATE $(x_{k+1},y_{k+1},s_{k+1})\gets(x_k,y_k,s_k)+(\Delta x,\Delta y,\Delta s)$; $k\gets k+1$
\ENDWHILE
\RETURN $x_k$, $(y_k,s_k)$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-path-following .theorem name="Short-step path following"}

If $d_{\mu_k}(x_k,s_k)\le0.1$, then $d_{\mu_{k+1}}(x_{k+1},s_{k+1})\le0.1$. Consequently the gap falls below $\varepsilon$ after $O\big(\sqrt\nu\log(\langle x_0,s_0\rangle/\varepsilon)\big)$ iterations.

:::

::: {.proof}

1. The first statement is stated without proof; it rests on the self-concordance of the barrier.

2. Every iteration divides $\mu$ by $1+0.1/\sqrt\nu$, so $O(\sqrt\nu)$ iterations halve it.

3. By @lem-near-path-gap the gap stays at most $2\nu\mu_k$, and $\mu_0$ is within a constant factor of $\langle x_0,s_0\rangle/\nu$ when $d_{\mu_0}\le0.1$. So $O(\sqrt\nu\log(\langle x_0,s_0\rangle/\varepsilon))$ iterations suffice.

:::

An SDP with $p\times p$ matrices needs as many iterations as an LP with $p$ variables, but each Newton system has about $p^2$ unknowns instead of $p$.

::: {#rmk-primal-dual-interior-point-1 .remark name="Rounding and starting"}

For a linear program with integer data, once the gap is below $2^{-2L}$ one can move from the current point to a vertex at least as good (as in the proof of @thm-optimal-vertex), and that vertex is optimal; this gives a polynomial algorithm in $L$. For semidefinite programs there is no such exact rounding, and one is content with an $\varepsilon$-optimal solution. To *start*, note that as $\mu\to\infty$ the central point no longer depends on $c$: all central paths, for all objectives, start from the same analytic centre. So from any strictly feasible point one follows the central path of a suitable auxiliary objective backwards to large $\mu$, then switches to the true objective and follows its path forwards.

:::
