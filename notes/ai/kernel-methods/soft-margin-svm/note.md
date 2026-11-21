---
title: "Soft Margins and the SMO Algorithm"
sources: [cs229-6]
requires: [ai/kernel-methods/support-vector-machines]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS229 lecture notes (version of 23 August 2026), Chapter 6.7-6.8 (regularization and the non-separable case, the KKT conditions of the soft-margin dual, coordinate ascent, SMO), in our own wording. The derivation of the SMO step through the errors E_i, the hinge-loss form and the worked SMO step are our own; proofs written out in steps. The support vector classifier of @def-support-vector-classifier (EE364A) is the same primal problem in another notation. -->

Real data are rarely separable, and one outlier can swing the optimal margin classifier a long way. The soft-margin SVM lets points violate the margin at a price.

::: {#def-soft-margin-svm .definition name="Soft-margin SVM" related="def-support-vector-classifier"}

For training examples $(\mathbf{x}^{(i)},y^{(i)})$ with $y^{(i)}\in\{-1,+1\}$ and a constant $C>0$, the *soft-margin SVM* solves

$$
\begin{aligned}
\min_{\mathbf{w},b,\boldsymbol\xi}\quad&\tfrac12\lVert\mathbf{w}\rVert^2+C\sum_{i=1}^N\xi_i\\
\text{subject to}\quad&y^{(i)}(\mathbf{w}^{\mathsf T}\mathbf{x}^{(i)}+b)\ge1-\xi_i,\quad\xi_i\ge0,\quad i=1,\dots,N.
\end{aligned}
$$

The *slack* $\xi_i$ is how far point $i$ falls short of functional margin $1$. A large $C$ makes violations expensive; as $C\to\infty$ the problem tends to the optimal margin classifier (@def-optimal-margin-classifier).

:::

::: {#prp-soft-margin-hinge .proposition name="Hinge loss form"}

The soft-margin SVM is equivalent to the unconstrained problem

$$
\min_{\mathbf{w},b}\ \tfrac12\lVert\mathbf{w}\rVert^2+C\sum_{i=1}^N\max\bigl(0,\,1-y^{(i)}(\mathbf{w}^{\mathsf T}\mathbf{x}^{(i)}+b)\bigr),
$$

that is, the *hinge loss* $\max(0,1-m)$ of the margin $m$ plus a squared-norm penalty.

:::

::: {.proof}

1. For fixed $(\mathbf{w},b)$, the constraints on $\xi_i$ are $\xi_i\ge1-m_i$ and $\xi_i\ge0$ with $m_i=y^{(i)}(\mathbf{w}^{\mathsf T}\mathbf{x}^{(i)}+b)$.

2. The objective increases with each $\xi_i$, so the best choice is the smallest allowed, $\xi_i=\max(0,1-m_i)$.

3. Substituting it leaves the stated problem in $(\mathbf{w},b)$ alone.

:::

::: {#fig-soft-margin-svm-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=0.8cm]
\draw[->] (-2.3,0) -- (3.3,0) node[lab,anchor=west] {$m$};
\draw[->] (0,-0.2) -- (0,3.4) node[lab,anchor=south] {loss};
\draw[hl] (-2.2,3.2) -- (1,0) -- (3.1,0);
\node[lab,emph,anchor=north east] at (0.6,0.4) {hinge};
\draw (-2.20,3.326) -- (-2.10,3.196) -- (-2.00,3.069) -- (-1.90,2.942) -- (-1.80,2.818) -- (-1.70,2.695) -- (-1.60,2.574) -- (-1.50,2.455) -- (-1.40,2.338) -- (-1.30,2.223) -- (-1.20,2.111) -- (-1.10,2.002) -- (-1.00,1.895) -- (-0.90,1.791) -- (-0.80,1.690) -- (-0.70,1.592) -- (-0.60,1.497) -- (-0.50,1.405) -- (-0.40,1.317) -- (-0.30,1.233) -- (-0.20,1.151) -- (-0.10,1.074) -- (0.00,1.000) -- (0.10,0.930) -- (0.20,0.863) -- (0.30,0.800) -- (0.40,0.740) -- (0.50,0.684) -- (0.60,0.631) -- (0.70,0.582) -- (0.80,0.535) -- (0.90,0.492) -- (1.00,0.452) -- (1.10,0.415) -- (1.20,0.380) -- (1.30,0.348) -- (1.40,0.318) -- (1.50,0.291) -- (1.60,0.265) -- (1.70,0.242) -- (1.80,0.221) -- (1.90,0.201) -- (2.00,0.183) -- (2.10,0.167) -- (2.20,0.152) -- (2.30,0.138) -- (2.40,0.125) -- (2.50,0.114) -- (2.60,0.103) -- (2.70,0.094) -- (2.80,0.085) -- (2.90,0.077) -- (3.00,0.070) -- (3.10,0.064) ;
\node[lab,anchor=south east] at (3.1,0.2) {logistic};
\draw[faint] (-2.2,1) -- (0,1) -- (0,0) -- (3.1,0);
\node[lab,anchor=south] at (-1.6,1) {zero-one};
\draw[tick] (1,0) -- (1,-0.1) node[lab,anchor=north] {$1$};
\end{tikzpicture}
\end{center}
```

The hinge loss $\max(0,1-m)$ of @prp-soft-margin-hinge, the logistic loss $\log_2(1+e^{-m})$ and the zero-one loss as functions of the margin $m$. The hinge loss is exactly $0$ once $m\ge1$, which is why only points on or inside the margin become support vectors.

:::

::: {#thm-soft-margin-dual .theorem name="The soft-margin dual and its KKT conditions"}

The dual of the soft-margin SVM is

$$
\max_{\boldsymbol\alpha}\ W(\boldsymbol\alpha)=\sum_i\alpha_i-\frac12\sum_{i,j}y^{(i)}y^{(j)}\alpha_i\alpha_jK_{ij}\quad\text{subject to}\quad0\le\alpha_i\le C,\quad\sum_i\alpha_iy^{(i)}=0,
$$

with $K_{ij}=\langle\mathbf{x}^{(i)},\mathbf{x}^{(j)}\rangle$ (or any kernel). Strong duality holds, $\mathbf{w}^\star=\sum_i\alpha_i^\star y^{(i)}\mathbf{x}^{(i)}$, and with $f(\mathbf{x})=\mathbf{w}^{\star\mathsf T}\mathbf{x}+b^\star$ the optimal $\boldsymbol\alpha^\star$ satisfies

$$
\alpha_i^\star=0\Rightarrow y^{(i)}f(\mathbf{x}^{(i)})\ge1,\qquad \alpha_i^\star=C\Rightarrow y^{(i)}f(\mathbf{x}^{(i)})\le1,\qquad 0<\alpha_i^\star<C\Rightarrow y^{(i)}f(\mathbf{x}^{(i)})=1.
$$

:::

::: {.proof}

1. Take multipliers $\alpha_i\ge0$ for the margin constraints and $r_i\ge0$ for $\xi_i\ge0$:

   $$
   L=\tfrac12\lVert\mathbf{w}\rVert^2+C\sum_i\xi_i-\sum_i\alpha_i\bigl(y^{(i)}(\mathbf{w}^{\mathsf T}\mathbf{x}^{(i)}+b)-1+\xi_i\bigr)-\sum_ir_i\xi_i.
   $$

2. $L$ is linear in each $\xi_i$ with coefficient $C-\alpha_i-r_i$ and linear in $b$ with coefficient $-\sum_i\alpha_iy^{(i)}$; the infimum is $-\infty$ unless both vanish. The condition $r_i=C-\alpha_i\ge0$ is $\alpha_i\le C$.

3. With those conditions the $\xi$ and $b$ terms disappear and the minimization in $\mathbf{w}$ is the one of @thm-svm-dual, giving $\mathbf{w}=\sum_i\alpha_iy^{(i)}\mathbf{x}^{(i)}$ and the dual objective $W(\boldsymbol\alpha)$.

4. The problem is a convex QP with affine constraints, always feasible (take $\mathbf{w}=\mathbf{0}$, $b=0$, $\xi_i=1$), so strong duality holds and the KKT conditions (@thm-kkt) hold at the optimum.

5. Complementary slackness gives $\alpha_i^\star\bigl(y^{(i)}f(\mathbf{x}^{(i)})-1+\xi_i^\star\bigr)=0$ and $r_i^\star\xi_i^\star=0$ with $r_i^\star=C-\alpha_i^\star$.

6. If $\alpha_i^\star=0$ then $r_i^\star=C>0$, so $\xi_i^\star=0$ and feasibility gives $y^{(i)}f(\mathbf{x}^{(i)})\ge1$.

7. If $\alpha_i^\star=C$ the first condition gives $y^{(i)}f(\mathbf{x}^{(i)})=1-\xi_i^\star\le1$.

8. If $0<\alpha_i^\star<C$ then $r_i^\star>0$ forces $\xi_i^\star=0$, and $\alpha_i^\star>0$ forces $y^{(i)}f(\mathbf{x}^{(i)})=1-\xi_i^\star=1$.

:::

The only change from the separable dual is the upper bound $\alpha_i\le C$: no single point can pull on the boundary with weight more than $C$. Points with $0<\alpha_i^\star<C$ lie exactly on the margin and give $b^\star=y^{(i)}-\mathbf{w}^{\star\mathsf T}\mathbf{x}^{(i)}$.

::: {#def-coordinate-ascent .definition name="Coordinate ascent"}

*Coordinate ascent* maximizes $W(\alpha_1,\dots,\alpha_N)$ by repeatedly choosing one index $i$ and setting $\alpha_i$ to the value that maximizes $W$ with all other coordinates held fixed. Each step cannot decrease $W$.

:::

Coordinate ascent cannot be applied to the SVM dual directly: the constraint $\sum_i\alpha_iy^{(i)}=0$ determines any one $\alpha_i$ from the others. The fix is to change two coordinates at a time.

::: {#def-smo .definition name="Sequential minimal optimization (SMO)"}

Write $f(\mathbf{x})=\sum_k\alpha_ky^{(k)}K(\mathbf{x}^{(k)},\mathbf{x})+b$ for the current classifier and $E_k=f(\mathbf{x}^{(k)})-y^{(k)}$ for its error on example $k$. Start from a feasible $\boldsymbol\alpha$ (for instance $\boldsymbol\alpha=\mathbf{0}$). Repeat until the conditions of @thm-soft-margin-dual hold to a tolerance:

1. Choose a pair $i\ne j$ (heuristically, one that violates the KKT conditions most). Put $s=y^{(i)}y^{(j)}$ and $\eta=K_{ii}+K_{jj}-2K_{ij}$, and assume $\eta>0$.
2. Compute the ends of the feasible segment: if $s=-1$, $L=\max(0,\alpha_j-\alpha_i)$ and $H=\min(C,C+\alpha_j-\alpha_i)$; if $s=1$, $L=\max(0,\alpha_i+\alpha_j-C)$ and $H=\min(C,\alpha_i+\alpha_j)$.
3. Set $\alpha_j^{\text{new}}=\alpha_j+y^{(j)}(E_i-E_j)/\eta$, clipped to $[L,H]$.
4. Set $\alpha_i^{\text{new}}=\alpha_i+s\,(\alpha_j-\alpha_j^{\text{new}})$, then update $b$ so that a point strictly inside $(0,C)$ has $y f=1$.

:::

```{=latex}
\begin{algorithm}
\caption{SMO for the soft-margin SVM dual}
\begin{algorithmic}
\INPUT Kernel matrix $K$, labels $y^{(1)},\dots,y^{(N)}\in\{\pm1\}$, constant $C>0$
\STATE $\boldsymbol\alpha\gets\mathbf{0}$, $b\gets0$
\WHILE{some $\alpha_k$ violates the KKT conditions}
    \STATE choose a pair $i\ne j$
    \STATE $s\gets y^{(i)}y^{(j)}$, $\eta\gets K_{ii}+K_{jj}-2K_{ij}$
    \STATE compute $L,H$ from $s$, $\alpha_i$, $\alpha_j$ and $C$
    \STATE $a\gets\operatorname{clip}\bigl(\alpha_j+y^{(j)}(E_i-E_j)/\eta,\ L,\ H\bigr)$
    \STATE $\alpha_i\gets\alpha_i+s\,(\alpha_j-a)$, $\alpha_j\gets a$
    \STATE update $b$ \COMMENT{so that a point with $0<\alpha_k<C$ has $y^{(k)}f(\mathbf{x}^{(k)})=1$}
\ENDWHILE
\RETURN $\boldsymbol\alpha$, $b$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-smo-step .theorem name="The SMO step is an exact pairwise maximization"}

With all coordinates except $\alpha_i,\alpha_j$ fixed, the SMO step of @def-smo returns the feasible pair that maximizes $W$. In particular SMO never decreases $W$.

:::

::: {.proof}

1. The equality constraint fixes $\alpha_iy^{(i)}+\alpha_jy^{(j)}$, so the feasible pairs lie on the line $\alpha_i=\text{const}-s\,\alpha_j$; intersecting it with the box $[0,C]^2$ gives exactly $\alpha_j\in[L,H]$ with the stated ends.

2. Along this line, $W$ is a quadratic function $w(\alpha_j)$. Its derivative is $\partial W/\partial\alpha_j-s\,\partial W/\partial\alpha_i$. Since $\partial W/\partial\alpha_k=1-y^{(k)}\sum_l\alpha_ly^{(l)}K_{kl}=1-y^{(k)}\bigl(f(\mathbf{x}^{(k)})-b\bigr)$ and $s\,y^{(i)}=y^{(j)}$, the derivative at the current point is

   $$
   1-s+y^{(j)}\bigl(f(\mathbf{x}^{(i)})-f(\mathbf{x}^{(j)})\bigr)=y^{(j)}(E_i-E_j),
   $$

   using $y^{(j)}\bigl(y^{(j)}-y^{(i)}\bigr)=1-s$.

3. The Hessian of $W$ is $-Q$ with $Q_{kl}=y^{(k)}y^{(l)}K_{kl}$. The direction of the line is $(-s,1)$ in $(\alpha_i,\alpha_j)$, so $w''=-(Q_{ii}-2sQ_{ij}+Q_{jj})=-(K_{ii}+K_{jj}-2K_{ij})=-\eta$.

4. A quadratic with $w'=y^{(j)}(E_i-E_j)$ at the current point and $w''=-\eta<0$ is maximized at $\alpha_j+y^{(j)}(E_i-E_j)/\eta$.

5. A concave function of one variable restricted to an interval is maximized at the unconstrained maximizer clipped to the interval. Step 4 of @def-smo then restores the equality constraint.

:::

::: {#exm-smo-one-step .example name="One SMO step"}

Take the three points of @exm-svm-three-points, the linear kernel, $C=1$ and the start $\boldsymbol\alpha=\mathbf{0}$, $b=0$. Then $f=0$, so $E_1=-1$, $E_2=-1$, $E_3=1$. Choose the pair $(i,j)=(1,3)$: $s=-1$, $\eta=K_{11}+K_{33}-2K_{13}=8$, $L=0$, $H=1$, and

$$
\alpha_3^{\text{new}}=0+(-1)\frac{-1-1}{8}=\tfrac14,\qquad \alpha_1^{\text{new}}=0+(-1)\bigl(0-\tfrac14\bigr)=\tfrac14.
$$

Now $\mathbf{w}=\tfrac14(2,2)=\bigl(\tfrac12,\tfrac12\bigr)$ and $W=\tfrac12-\tfrac12\cdot\tfrac12=\tfrac14$, up from $0$; the optimum is $\tfrac5{18}\approx0.278$, reached after further steps. Since every optimal $\alpha_i^\star$ there is below $C=1$, the soft-margin and hard-margin solutions coincide for this data.

:::

::: {#rmk-soft-margin-svm-1 .remark name="Why SMO is fast" editor="No figure for SMO: its iterates are dual coefficients, and the boundaries after the worked step and at the optimum are the picture of fig-support-vector-machines-1 with one more line."}

Each SMO step is solved in closed form and touches only two coordinates, so it costs $O(N)$ to update the errors $E_k$ afterwards (with a cached kernel matrix). No general-purpose QP solver is needed, and the memory is $O(N)$ beyond the kernel values. Most $\alpha_i$ end at $0$, so good pair-selection heuristics concentrate on the few candidates for support vectors.

:::
