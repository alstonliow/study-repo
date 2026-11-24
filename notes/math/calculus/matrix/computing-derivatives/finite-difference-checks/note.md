---
title: "Finite-Difference Checks"
sources: [mit18s096-4, cs231n-3]
requires: [math/calculus/matrix/derivatives/gradients-in-inner-product-spaces]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.S096 Matrix Calculus (IAP 2023), course notes Chapter 4 (why approximate derivatives, forward differences, the matrix-square example, accuracy, order of accuracy, roundoff, other methods), in our own wording; the error table and plot were computed by us in Python (4 by 4 Gaussian matrices, seed 1); proofs written out in steps. Merged 2026-11-24 (owner): @thm-finite-difference-error keeps the id of the CS231n block (Optimization notes, numerical gradients); the statement for general spaces and relative errors and step 2 of the proof are from 18.S096, the explicit Taylor remainders of steps 1 and 3 and the scalar formulas from CS231n; the separate 18.S096 block prp-finite-difference-order was removed. -->

Every hand-derived or hand-coded derivative should be checked against an independent computation. The cheapest check compares the derivative in one random direction with a *finite difference*, the change of $f$ for a small but finite step.

::: {#def-finite-difference-check .definition name="Finite-difference check" related="def-numerical-gradient"}

Let $f:V\to W$ between normed spaces, with a claimed derivative $L=f'(x)$. For a small step $\delta x$, the *forward difference* is $\delta f=f(x+\delta x)-f(x)$, and the check computes the *relative error*

$$
\frac{\lVert\delta f-L[\delta x]\rVert}{\lVert L[\delta x]\rVert}.
$$

The *centred difference* uses $\tfrac12\bigl(f(x+\delta x)-f(x-\delta x)\bigr)$ in place of $\delta f$. A correct $L$ gives a small relative error; a wrong $L$ gives an error of order $1$.

:::

The check works directly with $f'(x)[\delta x]$, so it needs no division by $\delta x$ and applies to matrix inputs and outputs. A random direction $\delta x$ is used because a wrong derivative is almost never right in a random direction.

::: {#thm-finite-difference-error .theorem name="Error of finite differences"}

Let $f$ be three times continuously differentiable near $x$, fix a direction $u$ and put $\delta x=su$. As $s\to0$,

$$
f(x+su)-f(x)=s\,f'(x)[u]+O(s^2),\qquad \tfrac12\bigl(f(x+su)-f(x-su)\bigr)=s\,f'(x)[u]+O(s^3).
$$

So the forward difference is *first order*: its relative error (@def-finite-difference-check) is proportional to $s$ when $f''(x)[u,u]\neq0$. The centred difference is *second order*: its relative error is $O(s^2)$. For a scalar function and $u=e_i$, dividing by $s=h$ gives the familiar $\frac{g(h)-g(0)}{h}=g'(0)+O(h)$ and $\frac{g(h)-g(-h)}{2h}=g'(0)+O(h^2)$ for $g(t)=f(x+te_i)$.

:::

::: {.proof}

1. Put $g(t)=f(x+tu)$, so $g'(0)=f'(x)[u]$, $g''(0)=f''(x)[u,u]$ (@def-second-derivative-bilinear). By Taylor's theorem (componentwise for vector outputs), $g(\pm s)=g(0)\pm s\,g'(0)+\tfrac{s^2}2g''(0)\pm\tfrac{s^3}6g'''(\xi_\pm)$ with $\xi_\pm$ between $0$ and $\pm s$.

2. *Forward.* $g(s)-g(0)-s\,g'(0)=\tfrac{s^2}2g''(0)+O(s^3)$. Dividing by $\lVert s\,g'(0)\rVert$ gives a relative error $\tfrac s2\lVert f''(x)[u,u]\rVert/\lVert f'(x)[u]\rVert+O(s^2)$, proportional to $s$.

3. *Centred.* In $g(s)-g(-s)$ the even-order terms cancel, leaving $2s\,g'(0)+\tfrac{s^3}6\bigl(g'''(\xi_+)+g'''(\xi_-)\bigr)$. Since $g'''$ is bounded near $0$, half of this is $s\,g'(0)+O(s^3)$, and the relative error is $O(s^2)$.

:::

::: {#prp-finite-difference-roundoff .proposition name="Roundoff limits the step size"}

In floating-point arithmetic with machine epsilon $\varepsilon$ (@def-floating-point-system), computing $\delta f$ adds an error of roughly $\varepsilon\lVert f(x)\rVert$. For the forward difference the relative error then behaves like

$$
c_1\,\frac{\lVert\delta x\rVert}{\lVert x\rVert}+c_2\,\frac{\varepsilon\lVert x\rVert}{\lVert\delta x\rVert},
$$

which is smallest when $\lVert\delta x\rVert\approx\sqrt{\varepsilon}\,\lVert x\rVert$, giving about half the significant digits.

:::

::: {.proof}

1. Each of $f(x+\delta x)$ and $f(x)$ is rounded with relative error at most about $\varepsilon$, so their difference carries an absolute error of order $\varepsilon\lVert f(x)\rVert$, however small the true difference is (*cancellation*).

2. Divided by $\lVert f'(x)[\delta x]\rVert\approx\lVert\delta x\rVert\,\lVert f(x)\rVert/\lVert x\rVert$ (for a typical well-scaled $f$), this is a relative error of order $\varepsilon\lVert x\rVert/\lVert\delta x\rVert$.

3. Adding the truncation error of @thm-finite-difference-error gives the sum. Writing $t=\lVert\delta x\rVert/\lVert x\rVert$, $c_1t+c_2\varepsilon/t$ is minimized at $t=\sqrt{c_2\varepsilon/c_1}$, of order $\sqrt\varepsilon$, with minimum value of order $\sqrt\varepsilon$.

:::

::: {#exm-finite-difference-checks-1 .example name="Checking the derivative of the matrix square"}

Take $f(A)=A^2$ with a random $4\times4$ Gaussian $A$ and $\delta A=s\,D$ for a random Gaussian $D$, in double precision ($\varepsilon\approx2.2\times10^{-16}$). We compared $\delta f$ with the correct $A\,\delta A+\delta A\,A$ and with the wrong guess $2A\,\delta A$:

| $s$ | $10^{-2}$ | $10^{-4}$ | $10^{-6}$ | $10^{-8}$ | $10^{-10}$ | $10^{-12}$ | $10^{-14}$ |
|---|---|---|---|---|---|---|---|
| correct, forward | $1.3\cdot10^{-2}$ | $1.3\cdot10^{-4}$ | $1.3\cdot10^{-6}$ | $1.6\cdot10^{-8}$ | $5.0\cdot10^{-7}$ | $5.0\cdot10^{-5}$ | $5.4\cdot10^{-3}$ |
| wrong $2A\,\delta A$ | $0.93$ | $0.93$ | $0.93$ | $0.93$ | $0.93$ | $0.93$ | $0.93$ |

The correct derivative's error falls in proportion to $s$ until $s\approx10^{-8}\approx\sqrt\varepsilon$, then rises again because of roundoff; the wrong guess is off by about $93\%$ at every scale. For this quadratic $f$ the centred difference has no truncation error at all: $\tfrac12\bigl((A+\delta A)^2-(A-\delta A)^2\bigr)=A\,\delta A+\delta A\,A$ exactly, so only roundoff remains.

:::

::: {#fig-finite-difference-checks-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.42cm, y=0.32cm]
\draw[->] (0,-9) -- (17,-9) node[lab, right] {$-\log_{10}s$};
\draw[->] (0,-9) -- (0,1.5) node[lab, above] {$\log_{10}$ rel.\ error};
\foreach \k in {0,4,8,12,16}{\draw (\k,-9) -- (\k,-9.3) node[lab, below] {$\k$};}
\foreach \e in {-8,-4,0}{\draw (0,\e) -- (-0.3,\e) node[lab, left] {$\e$};}
\draw[hl] plot coordinates {(0,0.11) (2,-1.89) (4,-3.89) (6,-5.89) (8,-7.80) (10,-6.30) (12,-4.30) (14,-2.27) (16,-0.47)};
\foreach \p in {(0,0.11),(2,-1.89),(4,-3.89),(6,-5.89),(8,-7.80),(10,-6.30),(12,-4.30),(14,-2.27),(16,-0.47)}{\fill[hl] \p circle (2pt);}
\draw[faint] (0,-0.03) -- (16,-0.03) node[lab, above left] {wrong $2A\,\delta A$};
\node[lab] at (4.2,-6.5) {truncation};
\node[lab] at (13.2,-6.5) {roundoff};
\end{tikzpicture}
\end{center}
```

Relative error of the forward-difference check for $f(A)=A^2$ on a log–log scale (data of @exm-finite-difference-checks-1). The slope $1$ on the left is first-order truncation error; the slope $-1$ on the right is roundoff; the minimum sits near $s=\sqrt\varepsilon\approx10^{-8}$.

:::

::: {#rmk-finite-difference-checks-1 .remark name="Finite differences are a check, not a method"}

Computing a whole gradient of $f:\mathbb{R}^n\to\mathbb{R}$ by finite differences needs $n$ extra evaluations of $f$ and gives only about half the digits, which is hopeless for large $n$ such as the weights of a neural network. As a *check*, a few random directions are enough. Better estimates exist (Richardson extrapolation over a sequence of steps, higher-order formulas), but exact derivatives come from analysis by hand or from automatic differentiation (@sec-math-calculus-matrix-computing-derivatives-forward-mode-automatic-differentiation). Note that forward and backward *differences* are unrelated to forward and reverse *mode* differentiation.

:::
