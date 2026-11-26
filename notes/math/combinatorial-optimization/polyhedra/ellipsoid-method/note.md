---
title: "The Ellipsoid Method"
sources: [mit18433-7]
requires: [math/combinatorial-optimization/polyhedra/combinatorial-polytopes]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on the ellipsoid algorithm (Section 7), in our own wording; example our own (checked by computation); proofs written out in steps. The bounds for 0-1 polytopes are given with proofs; rounding to an optimal vertex is only sketched, as in the course. Applications to arborescences and matchings are in @sec-math-combinatorial-optimization-matroids-arborescences and @sec-cs-graph-optimization-minimum-t-odd-cut. -->

The ellipsoid method (Shor 1977, Yudin–Nemirovski 1976, applied to linear programming by Khachiyan in 1979) was the first polynomial-time algorithm for linear programming. It is slow in practice, but it needs very little access to the polyhedron: only a way to answer "is this point inside, and if not, which inequality does it violate?". This makes it a powerful theoretical tool in combinatorial optimisation.

We write $E(a,A)=\{x\in\mathbb R^n:(x-a)^{\mathsf T}A^{-1}(x-a)\le1\}$ for the ellipsoid with centre $a$ and positive definite matrix $A$ (@def-ball-ellipsoid). If $A=B^{\mathsf T}B$, the affine map $x\mapsto(B^{-1})^{\mathsf T}(x-a)$ sends $E(a,A)$ onto the unit ball $E(0,I)$; affine maps multiply all volumes by the same factor.

::: {#def-separation-oracle .definition name="Separation oracle"}

A *separation oracle* for a convex set $P\subseteq\mathbb R^n$ takes a point $x^*\in\mathbb R^n$ and either reports $x^*\in P$, or returns an inequality $c^{\mathsf T}x\le d$ that is valid for $P$ and violated by $x^*$ ($c^{\mathsf T}x^*>d$).

:::

For $P=\{x:Cx\le d\}$ given explicitly, checking the rows one by one is a separation oracle. The point of the definition is that an oracle may exist, and run fast, even when $P$ has exponentially many inequalities.

::: {#def-ellipsoid-method .definition name="Ellipsoid method"}

Given a separation oracle for $P$ and an ellipsoid $E_0=E(a_0,A_0)\supseteq P$, repeat for $k=0,1,2,\dots$:

1. Ask the oracle about the centre $a_k$. If $a_k\in P$, stop.
2. Otherwise it returns $c$ with $c^{\mathsf T}x\le c^{\mathsf T}a_k$ for all $x\in P$ (weaken the returned inequality by moving it through $a_k$). Set
$$b=\frac{A_kc}{\sqrt{c^{\mathsf T}A_kc}},\qquad a_{k+1}=a_k-\frac{1}{n+1}\,b,\qquad A_{k+1}=\frac{n^2}{n^2-1}\Big(A_k-\frac{2}{n+1}\,bb^{\mathsf T}\Big).$$

Stop with "$P$ is empty" once $\operatorname{Vol}(E_k)$ is smaller than a known lower bound on $\operatorname{Vol}(P)$.

:::

```{=latex}
\begin{algorithm}
\caption{Ellipsoid method}
\begin{algorithmic}
\INPUT separation oracle for $P\subseteq\mathbb R^n$, ellipsoid $E(a_0,A_0)\supseteq P$, volume bound $v$
\OUTPUT a point of $P$, or "empty"
\STATE $k\gets0$
\WHILE{$a_k\notin P$}
\IF{$\operatorname{Vol}(E(a_k,A_k))<v$} \RETURN "empty" \ENDIF
\STATE $c\gets$ oracle's violated inequality at $a_k$
\STATE $b\gets A_kc/\sqrt{c^{\mathsf T}A_kc}$
\STATE $a_{k+1}\gets a_k-b/(n+1)$; $A_{k+1}\gets\frac{n^2}{n^2-1}\big(A_k-\frac2{n+1}bb^{\mathsf T}\big)$
\STATE $k\gets k+1$
\ENDWHILE
\RETURN $a_k$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-ellipsoid-step .theorem name="One step of the ellipsoid method"}

With the notation of @def-ellipsoid-method, for $n\ge2$,
$$E(a_k,A_k)\cap\{x:c^{\mathsf T}x\le c^{\mathsf T}a_k\}\subseteq E(a_{k+1},A_{k+1})\qquad\text{and}\qquad\frac{\operatorname{Vol}(E_{k+1})}{\operatorname{Vol}(E_k)}<e^{-1/(2(n+1))}.$$

:::

::: {.proof}

1. *Reduction to the unit ball.* The affine map sending $E_k$ to $E(0,I)$ sends the half-ellipsoid to a half-ball and preserves volume ratios, and the formulas transform accordingly. After a rotation we may assume the half-ball is $H=E(0,I)\cap\{x:x_1\ge0\}$; the formulas then give the centre $\frac1{n+1}e_1$ and the ellipsoid
$$E'=\Big\{x:\Big(\tfrac{n+1}n\Big)^2\Big(x_1-\tfrac1{n+1}\Big)^2+\tfrac{n^2-1}{n^2}\sum_{i\ge2}x_i^2\le1\Big\}.$$

2. *Containment.* Expanding the square, the left side equals
$$\tfrac{n^2-1}{n^2}\lVert x\rVert^2+\tfrac{2n+2}{n^2}\,x_1(x_1-1)+\tfrac1{n^2}.$$
For $x\in H$ we have $\lVert x\rVert\le1$ and $0\le x_1\le1$, so this is at most $\frac{n^2-1}{n^2}+0+\frac1{n^2}=1$. Hence $H\subseteq E'$.

3. *Volume.* The volume of an ellipsoid is proportional to the product of its semi-axes. $E'$ has one semi-axis $\frac n{n+1}$ and $n-1$ semi-axes $\frac n{\sqrt{n^2-1}}$, the unit ball all semi-axes $1$, so the ratio is
$$\frac n{n+1}\Big(\frac{n^2}{n^2-1}\Big)^{(n-1)/2}=\Big(1-\frac1{n+1}\Big)\Big(1+\frac1{n^2-1}\Big)^{(n-1)/2}.$$

4. Using $1+t<e^t$ for $t\ne0$, this is less than $e^{-1/(n+1)}\,e^{(n-1)/(2(n^2-1))}=e^{-1/(n+1)+1/(2(n+1))}=e^{-1/(2(n+1))}$.

:::

So after $k$ steps $\operatorname{Vol}(E_k)<e^{-k/(2(n+1))}\operatorname{Vol}(E_0)$, and if $P$ is non-empty with volume at least $v$, the method finds a point of $P$ within $2(n+1)\ln(\operatorname{Vol}(E_0)/v)$ steps.

::: {#exm-ellipsoid-step-disk .example name="One step in the plane"}

Take $n=2$, the unit disk $E_0=E(0,I)$, and the cut $x_1\le0$ ($c=e_1$). Then $b=e_1$, the new centre is $(-\frac13,0)$ and $A_1=\frac43\big(I-\frac23e_1e_1^{\mathsf T}\big)=\operatorname{diag}(\frac49,\frac43)$. The new ellipse has semi-axes $\frac23$ and $\frac2{\sqrt3}$, area ratio $\sqrt{\det A_1}=\frac4{3\sqrt3}\approx0.770<e^{-1/6}\approx0.846$, and it contains the left half-disk.

:::

::: {#fig-ellipsoid-method-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,-1.5) arc (-90:-270:1.5) -- cycle;
\draw[emph] (0,0) circle (1.5);
\draw[hl] (-0.5,0) ellipse ({1.5*2/3} and {1.5*1.1547});
\draw[faint, dashed] (0,-2) -- (0,2);
\fill (0,0) circle (1.5pt); \node[lab, right] at (0,0) {$a_0$};
\fill (-0.5,0) circle (1.5pt); \node[lab, left] at (-0.5,0) {$a_1$};
\node[lab] at (1.9,1.2) {$E_0$}; \node[lab] at (-1.55,1.65) {$E_1$};
\node[lab] at (0.6,-1.9) {$c^{\mathsf T}x=c^{\mathsf T}a_0$};
\end{tikzpicture}
\end{center}
```

One step of the ellipsoid method in the plane: the centre $a_0$ of the unit disk $E_0$ violates the cut $x_1\le0$, and $E_1$ (thick) is the smallest ellipse containing the shaded half-disk, with centre $a_1=(-\frac13,0)$ and about $77\%$ of the area of $E_0$.

:::

The theorem below applies this to combinatorial problems: $S\subseteq\{0,1\}^n$ is given implicitly (say, the matchings of a graph) and $P=\operatorname{conv}(S)$.

::: {#thm-optimization-from-separation .theorem name="Optimisation from separation (Grötschel–Lovász–Schrijver)"}

Let $S\subseteq\{0,1\}^n$ with $P=\operatorname{conv}(S)$ full-dimensional, and suppose a separation oracle for $P$ is given. Then for $c\in\mathbb Z^n$, $\min\{c^{\mathsf T}x:x\in S\}$ can be computed with a number of arithmetic operations and oracle calls polynomial in $n$ and $\log c_{\max}$, where $c_{\max}=\max_i|c_i|$.

:::

::: {.proof}

1. *From optimisation to feasibility.* The optimum value is an integer $d^*$ in $[-nc_{\max},nc_{\max}]$. For an integer $d$, the polytope $P_d=P\cap\{x:c^{\mathsf T}x\le d+\frac12\}$ is non-empty exactly when $d\ge d^*$ (a minimiser over $P$ can be taken at a vertex, which is in $S$). Binary search over $d$ needs $O(\log(nc_{\max}))$ feasibility tests, and the oracle for $P$ plus one extra inequality is an oracle for $P_d$.

2. *Starting ellipsoid.* The ball with centre $(\frac12,\dots,\frac12)$ and radius $\frac{\sqrt n}2$ contains $\{0,1\}^n$ and hence $P_d$. Its volume is at most $(\frac{\sqrt n}2)^n$ times the volume $\le2^n$ of the unit ball, that is at most $(\sqrt n)^n$, so $\ln\operatorname{Vol}(E_0)=O(n\log n)$.

3. *Volume of a non-empty $P_d$.* Let $v_0\in S$ with $c^{\mathsf T}v_0\le d$. As $P$ is full-dimensional, there are $v_1,\dots,v_n\in S$ with $v_1-v_0,\dots,v_n-v_0$ linearly independent. Put $\alpha=\frac1{2nc_{\max}}$ and $w_i=v_i$ if $c^{\mathsf T}v_i\le d+\frac12$, otherwise $w_i=v_0+\alpha(v_i-v_0)$; in the second case $c^{\mathsf T}w_i\le d+\alpha\cdot nc_{\max}=d+\frac12$. So the simplex $\operatorname{conv}\{v_0,w_1,\dots,w_n\}$ lies in $P_d$.

4. Its volume is $\frac1{n!}|\det(w_1-v_0,\dots,w_n-v_0)|\ge\frac{\alpha^n}{n!}|\det(v_1-v_0,\dots,v_n-v_0)|\ge\frac{\alpha^n}{n!}$, because the last determinant is a non-zero integer. So $-\ln\operatorname{Vol}(P_d)=O(n\log n+n\log c_{\max})$.

5. By @thm-ellipsoid-step, each feasibility test needs $O(n\cdot(n\log n+n\log c_{\max}))$ steps, each with one oracle call and $O(n^2)$ arithmetic operations. With the binary search this is polynomial.

6. Finally a point of $P_{d^*}$ found this way can be rounded to a vertex of $P$ of no larger cost, that is, to an optimal element of $S$; we omit this step.

:::

::: {#rmk-ellipsoid-method-1 .remark name="Precision and full dimension"}

The proof ignores rounding: the square roots in the update must be computed to a polynomial number of bits, which needs a slightly larger ellipsoid at each step. If $P$ is not full-dimensional, one first finds its affine hull and works in fewer variables. Neither changes the polynomial bound.

:::
