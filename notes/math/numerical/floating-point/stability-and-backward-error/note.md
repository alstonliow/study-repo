---
title: "Stability and Backward Error"
sources: [mit18335-3, mit18335-5]
requires: [math/numerical/floating-point/floating-point-arithmetic, math/numerical/floating-point/conditioning]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lectures 3 and 5 (backwards stability; condition numbers), in our own wording; proofs written out in steps. -->

An algorithm computes $\tilde f(x)$ in floating point instead of the exact $f(x)$. We cannot ask for $\tilde f(x)=f(x)$, and asking for a small relative error is too much when the problem is ill-conditioned. The right demand is that the algorithm add no more error than the problem's own sensitivity forces: it should give the exact answer to a nearby question.

::: {#def-big-o-machine-epsilon .definition name="O(ε_mach)"}

A quantity $\varphi(x,\varepsilon_{\text{mach}})$ is $O(\varepsilon_{\text{mach}})$ if there is a constant $C$ with $\lvert\varphi\rvert\le C\varepsilon_{\text{mach}}$ for all data $x$ in the domain and all sufficiently small $\varepsilon_{\text{mach}}$. We imagine a family of floating-point systems with $\varepsilon_{\text{mach}}\to0$; $C$ may depend on the dimensions of the problem (such as $n$) but not on $x$.

:::

::: {#def-stability .definition name="Accurate, stable and backward stable algorithms"}

An algorithm $\tilde f$ for a problem $f$ is

1. *accurate* if $\dfrac{\lVert\tilde f(x)-f(x)\rVert}{\lVert f(x)\rVert}=O(\varepsilon_{\text{mach}})$ for all $x$;

2. *stable* if for each $x$ there is $\tilde x$ with $\dfrac{\lVert\tilde x-x\rVert}{\lVert x\rVert}=O(\varepsilon_{\text{mach}})$ and $\dfrac{\lVert\tilde f(x)-f(\tilde x)\rVert}{\lVert f(\tilde x)\rVert}=O(\varepsilon_{\text{mach}})$: a nearly right answer to a nearly right question;

3. *backward stable* if for each $x$ there is $\tilde x$ with $\dfrac{\lVert\tilde x-x\rVert}{\lVert x\rVert}=O(\varepsilon_{\text{mach}})$ and $\tilde f(x)=f(\tilde x)$: exactly the right answer to a nearly right question.

The smallest such relative distance $\lVert\tilde x-x\rVert/\lVert x\rVert$ is the *backward error*; the relative error of $\tilde f(x)$ itself is the *forward error*.

:::

::: {#fig-stability-and-backward-error-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.0]
\draw[regionA] (0,0) ellipse (1.6 and 1.2);
\node[lab] at (0,1.45) {data $X$};
\fill (-0.5,-0.2) circle (1.6pt) node[lab, below] {$x$};
\fill (0.3,0.35) circle (1.6pt) node[lab, right] {$\tilde x$};
\draw[faint, dashed] (-0.5,-0.2) -- (0.3,0.35);
\node[note] at (-0.2,-0.75) {backward error};
\draw[regionB] (6,0) ellipse (1.6 and 1.2);
\node[lab] at (6,1.45) {answers $Y$};
\fill (5.4,-0.35) circle (1.6pt) node[lab, below] {$f(x)$};
\fill (6.6,0.45) circle (1.6pt) node[lab, right] {$\tilde f(x)=f(\tilde x)$};
\draw[faint, dashed] (5.4,-0.35) -- (6.6,0.45);
\node[note] at (6.2,-0.85) {forward error};
\draw[map] (-0.4,-0.1) to[bend right=12] node[lab, below] {$f$} (5.3,-0.35);
\draw[map, hl] (-0.4,-0.1) to[bend left=25] node[lab, above] {$\tilde f$} (6.5,0.5);
\draw[map, faint] (0.4,0.4) to[bend left=6] (6.45,0.45);
\end{tikzpicture}
\end{center}
```

Backward stability: the computed answer $\tilde f(x)$ is the exact answer for a perturbed input $\tilde x$ within $O(\varepsilon_{\text{mach}})$ of $x$. The forward error is then at most the condition number times the backward error (@thm-backward-stable-accuracy).

:::

::: {#thm-backward-stable-accuracy .theorem name="Accuracy of a backward stable algorithm"}

If $\tilde f$ is a backward stable algorithm for a problem $f$ with relative condition number $\kappa(x)$, then
$$\frac{\lVert\tilde f(x)-f(x)\rVert}{\lVert f(x)\rVert}=O\bigl(\kappa(x)\,\varepsilon_{\text{mach}}\bigr).$$

:::

::: {.proof}

1. By backward stability, $\tilde f(x)=f(\tilde x)$ with $\lVert\tilde x-x\rVert/\lVert x\rVert=O(\varepsilon_{\text{mach}})$.

2. By the definition of the condition number (@def-relative-condition-number), for perturbations this small
$$\frac{\lVert f(\tilde x)-f(x)\rVert}{\lVert f(x)\rVert}\le\bigl(\kappa(x)+o(1)\bigr)\frac{\lVert\tilde x-x\rVert}{\lVert x\rVert},$$
where $o(1)\to0$ as $\varepsilon_{\text{mach}}\to0$.

3. Combine the two lines: the right-hand side is $O(\kappa(x)\varepsilon_{\text{mach}})$.

:::

The same conclusion holds for a stable algorithm (the extra forward perturbation contributes another $O(\varepsilon_{\text{mach}})$). This splits error analysis into two independent questions: the conditioning of the problem, and the backward error of the algorithm.

::: {#prp-arithmetic-backward-stable .proposition name="Floating-point arithmetic is backward stable"}

For data $x=(x_1,x_2)$ the algorithm $\tilde f(x)=\operatorname{fl}(x_1)\ominus\operatorname{fl}(x_2)$ for $f(x)=x_1-x_2$ is backward stable; so are the analogous algorithms for $+,\times,\div$. The inner product $\mathbf{x}^{\mathsf T}\mathbf{y}$ computed by summing the products in order is backward stable as well.

:::

::: {.proof}

1. By @thm-rounding-relative-error, $\operatorname{fl}(x_i)=x_i(1+\varepsilon_i)$ with $\lvert\varepsilon_i\rvert\le\varepsilon_{\text{mach}}$, and by @def-floating-point-operations the subtraction adds a factor $1+\varepsilon_3$.

2. So $\tilde f(x)=\bigl(x_1(1+\varepsilon_1)-x_2(1+\varepsilon_2)\bigr)(1+\varepsilon_3)=\tilde x_1-\tilde x_2$ with $\tilde x_i=x_i(1+\varepsilon_i)(1+\varepsilon_3)$.

3. $\lvert\tilde x_i-x_i\rvert/\lvert x_i\rvert\le2\varepsilon_{\text{mach}}+\varepsilon_{\text{mach}}^2=O(\varepsilon_{\text{mach}})$, so $\tilde f(x)=f(\tilde x)$ with a backward error $O(\varepsilon_{\text{mach}})$.

4. For the inner product, each product $x_iy_i$ and each partial sum gets a factor $(1+\varepsilon)$. Attaching every factor that multiplies the $i$-th term to $x_i$ gives $\tilde x_i=x_i(1+\eta_i)$ with $\lvert\eta_i\rvert\le n\varepsilon_{\text{mach}}+O(\varepsilon_{\text{mach}}^2)$, and the computed result equals $\tilde{\mathbf{x}}^{\mathsf T}\mathbf{y}$ exactly. The detailed count is the summation analysis of @thm-naive-summation-backward.

:::

::: {#exm-stable-not-backward-stable .example name="Stable but not backward stable"}

1. *Adding one.* Computing $f(x)=x+1$ as $\tilde f(x)=\operatorname{fl}(x)\oplus1$ gives $(x(1+\varepsilon_1)+1)(1+\varepsilon_2)$, a relative error $O(\varepsilon_{\text{mach}})$ in the answer, so the algorithm is accurate and hence stable. But for $\lvert x\rvert\ll\varepsilon_{\text{mach}}$ the result is exactly $1$, and the only $\tilde x$ with $\tilde x+1=1$ is $\tilde x=0$: a relative backward error of $100\%$. It is not backward stable.

2. *Outer product.* $A=\mathbf{x}\mathbf{y}^{\mathsf T}$ computed entry by entry as $x_i\otimes y_j$ has every entry correct to relative error $\varepsilon_{\text{mach}}$, so it is stable. But the computed matrix is generally not of rank one, while every exact outer product $\tilde{\mathbf{x}}\tilde{\mathbf{y}}^{\mathsf T}$ is; so it is not the exact outer product of any nearby data.

:::

::: {#exm-unstable-algorithm .example name="An unstable algorithm for a well-conditioned problem"}

The eigenvalues of a symmetric matrix are well-conditioned (perturbing $A$ by $\delta A$ moves each eigenvalue by at most $\lVert\delta A\rVert_2$, @thm-weyl-inequality). Computing them as roots of the characteristic polynomial is unstable: the map from coefficients to roots can be extremely ill-conditioned. For $A=\operatorname{diag}(1,2,\dots,20)$ the coefficients of $\det(\lambda I-A)=\prod_k(\lambda-k)$ reach $20!\approx2.4\times10^{18}$, and merely rounding them to double precision moves the roots near $12$ and $14$ by about $5\times10^{-4}$, an error some $10^{12}$ times $\varepsilon_{\text{mach}}$. The algorithm has inserted an ill-conditioned intermediate problem between the data and the answer. See @sec-math-numerical-eigenvalue-algorithms-hessenberg-reduction.

:::

::: {#rmk-stability-and-backward-error-1 .remark name="Why backward error is the right measure"}

The data of a computation usually carry errors far larger than $\varepsilon_{\text{mach}}$ (measurements, earlier rounding, model errors). If the computed answer is exact for data within $O(\varepsilon_{\text{mach}})$ of the given ones, the algorithm is as good as the data allow: any remaining forward error is the problem's fault, not the algorithm's. Backward error is also easy to measure afterwards; for a linear system the residual $\mathbf{r}=\mathbf{b}-A\tilde{\mathbf{x}}$ gives the backward error $\lVert\mathbf{r}\rVert/(\lVert A\rVert\lVert\tilde{\mathbf{x}}\rVert)$ directly.

:::
