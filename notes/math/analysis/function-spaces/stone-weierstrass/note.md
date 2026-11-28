---
title: "The Stone–Weierstrass Theorem"
sources: [camii-lan-3, camii-lans-3]
requires: [math/analysis/function-spaces/urysohn-tietze, math/analysis/real/uniform-convergence/weierstrass-approximation]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Linear Analysis (lecture notes), Section 3.4, and Example Sheet 3 (questions 3, 4, 5), in our own wording; proofs written out in steps. The lecture notes use the Weierstrass approximation theorem for $|x|$; here it is taken from the Bernstein-polynomial note. -->

Polynomials are dense in $C[0,1]$. The Stone–Weierstrass theorem says what makes this work: a subalgebra of $C(K)$ is dense as soon as it separates points and contains the constants.

::: {#def-subalgebra-separates .definition name="Subalgebra, separating points"}

A *subalgebra* $\mathcal A\subseteq C_{\mathbb R}(K)$ is a linear subspace closed under pointwise product. It *separates points* if for $x\ne y$ in $K$ there is $f\in\mathcal A$ with $f(x)\ne f(y)$. It *vanishes nowhere* if for each $x$ some $f\in\mathcal A$ has $f(x)\ne0$.

:::

::: {#lem-abs-uniform-limit .lemma name="Absolute values in a closed subalgebra"}

If $\mathcal A\subseteq C_{\mathbb R}(K)$ is a closed subalgebra and $f\in\mathcal A$, then $|f|\in\mathcal A$. Hence a closed subalgebra is a lattice: $\max(f,g)=\frac12(f+g+|f-g|)$ and $\min(f,g)$ are in $\mathcal A$.

:::

::: {.proof}

1. Let $M=\|f\|_\infty$ and assume $M>0$. By the Weierstrass approximation theorem (@thm-weierstrass-approximation) there are polynomials $p_n$ with $p_n\to|t|$ uniformly on $[-M,M]$.

2. Replacing $p_n$ by $p_n-p_n(0)$ we may assume $p_n(0)=0$, since $p_n(0)\to0$. Then $p_n\circ f$ is a polynomial in $f$ without constant term, so lies in $\mathcal A$ (no constant function is needed).

3. $\|p_n\circ f-|f|\|_\infty\le\sup_{|t|\le M}|p_n(t)-|t||\to0$, and $\mathcal A$ is closed, so $|f|\in\mathcal A$.

:::

::: {#thm-stone-weierstrass .theorem name="Stone–Weierstrass theorem (real case)"}

Let $K$ be a compact Hausdorff space and $\mathcal A\subseteq C_{\mathbb R}(K)$ a subalgebra that separates points and vanishes nowhere (e.g. contains the constants). Then $\mathcal A$ is dense in $C_{\mathbb R}(K)$ in the sup norm.

:::

::: {.proof}

1. It suffices to show the closure $\overline{\mathcal A}$ is all of $C_{\mathbb R}(K)$. The closure is again a closed subalgebra separating points and vanishing nowhere, so by @lem-abs-uniform-limit it is closed under $\max$ and $\min$.

2. *Interpolating at two points.* For $x\ne y$ the linear map $w\mapsto(w(x),w(y))$ from $\overline{\mathcal A}$ to $\mathbb R^2$ is onto, so any two values $a,b$ are attained at $x,y$ by some $h\in\overline{\mathcal A}$. Suppose the image $L$ were a proper subspace. It is a line spanned by some $(\alpha,\beta)$, and it is closed under coordinatewise products because $\overline{\mathcal A}$ is an algebra. Nowhere vanishing gives $L\ne0$ with a vector having first entry $\ne0$, so $\alpha\ne0$, and similarly a vector with second entry $\ne0$ forces $\beta\ne0$. Then $(\alpha^2,\beta^2)\in L$ forces $\alpha^2\beta=\alpha\beta^2$, so $\alpha=\beta$ and every $w\in\overline{\mathcal A}$ has $w(x)=w(y)$, contradicting that $\overline{\mathcal A}$ separates points.

3. *Fix $g\in C_{\mathbb R}(K)$ and $\varepsilon>0$.* For each $x,y$ choose $h_{xy}\in\overline{\mathcal A}$ with $h_{xy}(x)=g(x)$ and $h_{xy}(y)=g(y)$.

4. For fixed $x$, the sets $V_y=\{z:h_{xy}(z)<g(z)+\varepsilon\}$ are open and contain $y$. By compactness finitely many $V_{y_1},\dots,V_{y_m}$ cover $K$. Then $h_x=\min_ih_{xy_i}\in\overline{\mathcal A}$ satisfies $h_x<g+\varepsilon$ everywhere, and $h_x(x)=g(x)$ because each $h_{xy_i}(x)=g(x)$.

5. The sets $W_x=\{z:h_x(z)>g(z)-\varepsilon\}$ are open and contain $x$. Finitely many $W_{x_1},\dots,W_{x_k}$ cover $K$, and $h=\max_jh_{x_j}\in\overline{\mathcal A}$ satisfies $g-\varepsilon<h<g+\varepsilon$ everywhere.

6. So $\|g-h\|_\infty<\varepsilon$, i.e. $g\in\overline{\mathcal A}$.

:::

::: {#fig-stone-weierstrass-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (0,0) -- (5.2,0);
\draw[faint, domain=0:5, samples=40] plot (\x,{1.5+0.8*sin(\x*60)+0.25}); \draw[faint, domain=0:5, samples=40] plot (\x,{1.5+0.8*sin(\x*60)-0.25});
\draw[emph, domain=0:5, samples=40] plot (\x,{1.5+0.8*sin(\x*60)}); \node[lab, right] at (5,2.3) {$g$};
\draw[hl, domain=0:5, samples=40] plot (\x,{1.5+0.8*sin(\x*60)+0.12*sin(\x*300)}); \node[lab, right] at (5,0.9) {$h\in\mathcal A$};
\end{tikzpicture}
\end{center}
```

An element $h$ of the subalgebra stays within $\varepsilon$ of $g$ everywhere.

:::

::: {#thm-stone-weierstrass-complex .theorem name="Stone–Weierstrass theorem (complex case)"}

Let $K$ be compact Hausdorff and $\mathcal A\subseteq C(K)$ a complex subalgebra that separates points, vanishes nowhere and is closed under complex conjugation. Then $\mathcal A$ is dense in $C(K)$.

:::

::: {.proof}

1. The real parts $\operatorname{Re}f=\frac12(f+\bar f)$ and imaginary parts $\operatorname{Im}f=\frac1{2i}(f-\bar f)$ of elements of $\mathcal A$ lie in $\mathcal A$, so $\mathcal A_{\mathbb R}=\mathcal A\cap C_{\mathbb R}(K)$ is a real subalgebra.

2. It separates points: if $f(x)\ne f(y)$ then one of $\operatorname{Re}f,\operatorname{Im}f$ separates them. It vanishes nowhere similarly.

3. By @thm-stone-weierstrass it is dense in $C_{\mathbb R}(K)$; therefore $\mathcal A$ is dense in $C(K)$ (write $g=\operatorname{Re}g+i\operatorname{Im}g$).

:::

::: {#exm-stone-weierstrass-uses .example name="Applications"}

(i) *Polynomials.* The polynomials separate points and contain constants, so they are dense in $C[0,1]$ (the Weierstrass theorem again), and polynomials in several variables are dense in $C(K)$ for $K\subseteq\mathbb R^n$ compact.

(ii) *Even moments.* If $f\in C[0,1]$ and $\int_0^1f(x)x^{n}dx=0$ for every even $n\ge0$, then $f=0$. The even polynomials in $x$ form an algebra containing constants that separates points of $[0,1]$ (since $x\mapsto x^2$ is injective there), so they are dense. Taking $p_k\to f$ uniformly, $\int fp_k=0$ for each $k$ and $\int f^2=\lim\int fp_k=0$.

(iii) *Trigonometric polynomials* are dense in $C(S^1)$: they form a conjugation-closed algebra containing constants and separating points of the circle.

(iv) *Closure under conjugation cannot be dropped.* The polynomials in $z$ on the closed unit disc form an algebra separating points and containing constants, but every uniform limit of polynomials is holomorphic inside the disc, and $\bar z$ is not.

(v) *Separability.* For a compact metric space $K$, $C(K)$ is separable: pick a countable dense subset $\{x_n\}$ of $K$, and let $\mathcal A$ be the algebra generated by the constants and the functions $d(\cdot,x_n)$. It separates points, and the polynomials with rational coefficients in finitely many of these generators form a countable dense subset.

:::
