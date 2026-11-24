---
title: "Second Derivatives, Bilinear Maps and Hessians"
sources: [mit18s096-12]
requires: [math/calculus/matrix/derivatives/derivatives-of-determinant-and-inverse]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.S096 Matrix Calculus (IAP 2023), course notes Chapter 12 (Hessian matrices, second derivatives as bilinear maps, the generalized quadratic approximation, Hessians in optimization: Newton-like methods, computing Hessians, minima, maxima and saddle points), in our own wording; the examples are ours, checked in Python; proofs written out in steps. The rigorous treatment on Euclidean spaces (symmetry, Taylor's theorem) is @def-second-derivative-several and its note; this note works with differentials on any vector space. -->

The derivative $f'(x)$ is itself a function of $x$, with values in the linear operators. Differentiating it once more gives an operator that eats two directions, a *bilinear map*. For scalar functions of vectors this bilinear map is the Hessian matrix.

::: {#def-second-derivative-bilinear .definition name="Second derivative as a bilinear map" related="def-second-derivative-several"}

Let $f:V\to W$ be differentiable near $x$. The *second derivative* $f''(x)$ is the derivative of $x\mapsto f'(x)$. It is a linear map from $V$ to the linear maps $V\to W$, so it takes two vectors:

$$
f'(x+dx')[dx]-f'(x)[dx]=f''(x)[dx,dx']+\text{(higher order)} .
$$

$f''(x)[dx,dx']$ is linear in each of $dx$ and $dx'$ separately, and when $f''$ is continuous it is symmetric: $f''(x)[dx,dx']=f''(x)[dx',dx]$.

:::

::: {#def-hessian-matrix .definition name="Hessian matrix"}

For $f:\mathbb{R}^n\to\mathbb{R}$ twice differentiable, the *Hessian* $H(x)$ is the $n\times n$ matrix with

$$
f''(x)[dx,dx']=dx^{\mathsf T}H(x)\,dx',\qquad H_{ij}=\frac{\partial^2f}{\partial x_i\,\partial x_j}.
$$

Equivalently, $H$ is the Jacobian of the gradient: $d(\nabla f)=H\,dx$.

:::

::: {#prp-quadratic-approximation .proposition name="Quadratic approximation"}

If $f''$ is continuous near $x$, then

$$
f(x+\delta x)=f(x)+f'(x)[\delta x]+\tfrac12f''(x)[\delta x,\delta x]+o(\lVert\delta x\rVert^2).
$$

:::

::: {.proof}

1. Put $g(t)=f(x+t\,\delta x)$ for $t\in[0,1]$. By the chain rule, $g'(t)=f'(x+t\delta x)[\delta x]$ and $g''(t)=f''(x+t\delta x)[\delta x,\delta x]$.

2. Taylor's formula in one variable gives $g(1)=g(0)+g'(0)+\tfrac12g''(\tau)$ for some $\tau\in(0,1)$ (componentwise for vector outputs, or with the integral remainder).

3. Continuity of $f''$ makes $g''(\tau)-g''(0)$ smaller than any multiple of $\lVert\delta x\rVert^2$ for small $\delta x$, which gives the remainder. The full argument is @sec-math-analysis-differentiation-second-derivatives.

:::

::: {#fig-hessians-and-bilinear-maps-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.2cm, y=1.2cm]
\draw[->] (-0.2,0) -- (4,0) node[lab, right] {$x$};
\draw[domain=0.3:3.8, samples=50] plot (\x, {0.6+0.5*sin(deg(1.3*\x))+0.15*\x});
\draw[faint, domain=0.8:3.4] plot (\x, {1.1578-0.407*(\x-2)});
\draw[hl, domain=0.6:3.4, samples=40] plot (\x, {1.1578-0.407*(\x-2)-0.2178*(\x-2)*(\x-2)});
\fill (2,1.1578) circle (1.5pt);
\node[lab] at (3.6,1.9) {linear};
\node[lab] at (3.7,0.55) {quadratic};
\end{tikzpicture}
\end{center}
```

Near a point, the first derivative gives the tangent line; adding $\tfrac12f''[\delta x,\delta x]$ gives the parabola that also matches the curvature, which is what Newton-like methods minimize at each step.

:::

::: {#exm-hessians-and-bilinear-maps-1 .example name="Second derivative of the trace of a cube"}

Let $f(A)=\operatorname{tr}(A^3)$ on $n\times n$ matrices.

1. By the product rule and the cyclic property of the trace, $df=\operatorname{tr}(dA\,A^2+A\,dA\,A+A^2dA)=3\operatorname{tr}(A^2dA)$, so $\nabla f=3(A^2)^{\mathsf T}$.

2. Change $A$ by $dA'$ in this formula: $A^2$ changes by $dA'A+A\,dA'$, so

   $$f''(A)[dA,dA']=3\operatorname{tr}\bigl(A\,dA\,dA'+A\,dA'\,dA\bigr),$$

   which is visibly symmetric in $dA$ and $dA'$.

3. For a random $3\times3$ matrix $A$ and directions $U,V$, a second-order finite difference $\bigl(f(A+hU+hV)-f(A+hU)-f(A+hV)+f(A)\bigr)/h^2$ with $h=10^{-4}$ matches $3\operatorname{tr}(AUV+AVU)$ to three digits.

:::

::: {#prp-critical-point-classification .proposition name="Minima, maxima and saddle points" related="def-critical-point-two-variables"}

Let $f:\mathbb{R}^n\to\mathbb{R}$ have a continuous Hessian and $\nabla f(x)=0$.

1. If $H(x)$ is positive definite, $x$ is a strict local minimum.
2. If $H(x)$ is negative definite, $x$ is a strict local maximum.
3. If $H(x)$ has a positive and a negative eigenvalue, $x$ is a saddle point.

:::

::: {.proof}

1. With $\nabla f=0$, @prp-quadratic-approximation gives $f(x+\delta x)-f(x)=\tfrac12\delta x^{\mathsf T}H\delta x+o(\lVert\delta x\rVert^2)$.

2. If $H$ is positive definite with smallest eigenvalue $\mu>0$, then $\delta x^{\mathsf T}H\delta x\ge\mu\lVert\delta x\rVert^2$, which beats the remainder for small $\delta x$, so $f(x+\delta x)>f(x)$ for small $\delta x\ne0$.

3. Case 2 is case 1 for $-f$.

4. If $Hu=\mu u$ with $\mu>0$ and $Hv=\nu v$ with $\nu<0$, then $f$ increases along $tu$ and decreases along $tv$ for small $t\ne0$.

:::

::: {#fig-hessians-and-bilinear-maps-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm, y=0.9cm]
\begin{scope}
\foreach \r in {0.5,1,1.5}{\draw[set] (0,0) ellipse ({\r*1.2} and {\r*0.7});}
\fill (0,0) circle (1.5pt);
\node[lab] at (0,-1.7) {$H$ positive definite: minimum};
\end{scope}
\begin{scope}[xshift=5.5cm]
\foreach \c in {0.4,1.2}{
  \draw[set, domain=-1.6:1.6, samples=30] plot (\x, {sqrt(\x*\x/2+\c)});
  \draw[set, domain=-1.6:1.6, samples=30] plot (\x, {-sqrt(\x*\x/2+\c)});
  \draw[set, hl, domain=-1.5:1.5, samples=30] plot ({sqrt(\x*\x*2+\c)}, \x);
  \draw[set, hl, domain=-1.5:1.5, samples=30] plot ({-sqrt(\x*\x*2+\c)}, \x);}
\fill (0,0) circle (1.5pt);
\node[lab] at (0,-1.7) {eigenvalues of both signs: saddle};
\end{scope}
\end{tikzpicture}
\end{center}
```

Level curves of the quadratic part $\tfrac12\delta x^{\mathsf T}H\delta x$ near a critical point. A definite Hessian gives ellipses; an indefinite one gives hyperbolas, with $f$ above $f(x)$ on one pair (highlighted) and below on the other.

:::

::: {#rmk-hessians-and-bilinear-maps-1 .remark name="Hessians in optimization"}

Newton's method for minimization (@sec-math-optimization-algorithms-newtons-method-for-minimization) solves $H\,\delta x=-\nabla f$ at each step, and quasi-Newton methods such as BFGS build an approximation of $H$ from gradients. For large $n$ one rarely forms $H$: iterative solvers need only *Hessian–vector products* $Hv$, the directional derivative of $\nabla f$ along $v$, which automatic differentiation computes at the cost of a few gradients (@sec-math-calculus-matrix-computing-derivatives-reverse-mode-automatic-differentiation).

:::
