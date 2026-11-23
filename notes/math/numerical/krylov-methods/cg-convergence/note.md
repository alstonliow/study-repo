---
title: "Convergence of Conjugate Gradients"
sources: [mit18335-22]
requires: [math/numerical/krylov-methods/conjugate-gradient]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 22 (convergence of conjugate gradient), in our own wording; proofs written out in steps; the CG run was done with numpy on a 400 by 400 matrix with eigenvalues spread uniformly in [1,100]. -->

Like GMRES, CG is optimal over the Krylov space, so its convergence is a question about polynomials: how small can a polynomial with $p(0)=1$ be on the spectrum of $A$? For a positive definite matrix the spectrum lies in an interval $[\lambda_{\min},\lambda_{\max}]$, and the answer is given by Chebyshev polynomials. The result, convergence like $\bigl((\sqrt\kappa-1)/(\sqrt\kappa+1)\bigr)^n$, explains why CG needs about $\sqrt\kappa$ iterations where steepest descent needs $\kappa$.

::: {#thm-cg-polynomial .theorem name="CG as polynomial approximation"}

Let $A$ be symmetric positive definite with eigenvalues $\Lambda(A)$, and let $P_n$ be the polynomials of degree $\le n$ with $p(0)=1$. The CG errors satisfy $\mathbf{e}_n=p_n(A)\mathbf{e}_0$ where $p_n$ minimises $\lVert p(A)\mathbf{e}_0\rVert_A$ over $P_n$, and
$$\frac{\lVert\mathbf{e}_n\rVert_A}{\lVert\mathbf{e}_0\rVert_A}\le\min_{p\in P_n}\ \max_{\lambda\in\Lambda(A)}\lvert p(\lambda)\rvert .$$

:::

::: {.proof}

1. $\mathbf{x}\in\mathcal K_n$ means $\mathbf{x}=q(A)\mathbf{b}=q(A)A\mathbf{e}_0$ with $\deg q<n$ (here $\mathbf{x}_0=\mathbf{0}$, so $\mathbf{e}_0=\mathbf{x}_*$ and $\mathbf{b}=A\mathbf{e}_0$). Then $\mathbf{x}_*-\mathbf{x}=(I-Aq(A))\mathbf{e}_0=p(A)\mathbf{e}_0$ with $p\in P_n$, and every $p\in P_n$ arises.

2. By @thm-cg-properties, $\mathbf{x}_n$ minimises the $A$-norm of the error over $\mathcal K_n$, i.e. $p_n$ minimises $\lVert p(A)\mathbf{e}_0\rVert_A$.

3. Expand $\mathbf{e}_0=\sum_ja_j\mathbf{v}_j$ in orthonormal eigenvectors. Then $\lVert p(A)\mathbf{e}_0\rVert_A^2=\sum_ja_j^2\lambda_jp(\lambda_j)^2\le\max_j p(\lambda_j)^2\sum_ja_j^2\lambda_j=\max_jp(\lambda_j)^2\,\lVert\mathbf{e}_0\rVert_A^2$.

4. Combine 2 and 3 and minimise over $p$.

:::

::: {#cor-cg-distinct-eigenvalues .corollary name="Few distinct eigenvalues"}

If $A$ has only $k$ distinct eigenvalues, CG converges in at most $k$ steps (in exact arithmetic).

:::

::: {.proof}

1. Take $p(z)=\prod_{i=1}^k(1-z/\lambda_i)$ over the distinct eigenvalues. It has degree $k$, $p(0)=1$, and vanishes on $\Lambda(A)$.

2. By @thm-cg-polynomial, $\lVert\mathbf{e}_k\rVert_A=0$.

:::

::: {#thm-cg-chebyshev-bound .theorem name="The condition-number bound"}

If $\kappa=\lambda_{\max}/\lambda_{\min}$ is the 2-norm condition number of $A$, then
$$\frac{\lVert\mathbf{e}_n\rVert_A}{\lVert\mathbf{e}_0\rVert_A}\le2\Bigl(\frac{\sqrt\kappa-1}{\sqrt\kappa+1}\Bigr)^n .$$

:::

::: {.proof}

1. *Chebyshev polynomials.* $T_n(x)=\cos(n\arccos x)$ for $\lvert x\rvert\le1$ is a polynomial of degree $n$ (by $T_{n+1}=2xT_n-T_{n-1}$) with $\lvert T_n\rvert\le1$ there. For $x\ge1$, writing $x=\tfrac12(w+w^{-1})$ with $w\ge1$, one checks $T_n(x)=\tfrac12(w^n+w^{-n})\ge\tfrac12w^n$, where $w=x+\sqrt{x^2-1}$.

2. *The polynomial.* Map $[\lambda_{\min},\lambda_{\max}]$ to $[-1,1]$ by $x(\lambda)=\dfrac{\lambda_{\max}+\lambda_{\min}-2\lambda}{\lambda_{\max}-\lambda_{\min}}$, and put $p(\lambda)=T_n(x(\lambda))/T_n(x(0))$. Then $p(0)=1$, and on the spectrum $\lvert p\rvert\le1/T_n(\gamma)$ with $\gamma=x(0)=\dfrac{\kappa+1}{\kappa-1}>1$.

3. *Evaluate.* $\gamma+\sqrt{\gamma^2-1}=\dfrac{\kappa+1+2\sqrt\kappa}{\kappa-1}=\dfrac{(\sqrt\kappa+1)^2}{(\sqrt\kappa+1)(\sqrt\kappa-1)}=\dfrac{\sqrt\kappa+1}{\sqrt\kappa-1}$.

4. By step 1, $1/T_n(\gamma)\le2\bigl((\sqrt\kappa-1)/(\sqrt\kappa+1)\bigr)^n$, and @thm-cg-polynomial gives the result.

:::

Since $(\sqrt\kappa-1)/(\sqrt\kappa+1)\approx1-2/\sqrt\kappa$ for large $\kappa$, reducing the error by a factor $\epsilon$ takes about $\tfrac12\sqrt\kappa\ln(2/\epsilon)$ iterations. Steepest descent on the same problem contracts by $(\kappa-1)/(\kappa+1)\approx1-2/\kappa$ per step and needs about $\tfrac12\kappa\ln(1/\epsilon)$.

::: {#fig-cg-convergence-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.85cm, y=1.6cm]
\draw[->, faint] (0,0) -- (10.6,0) node[lab, right] {$\lambda$};
\draw[->, faint] (0,-0.25) -- (0,1.2) node[lab, above] {$p(\lambda)$};
\fill[tintA] (1,-0.1449) rectangle (10,0.1449);
\draw[emph, domain=0:10.2, samples=150] plot (\x,{(8*((11-2*\x)/9)^4-8*((11-2*\x)/9)^2+1)/6.9015});
\fill[accent] (0,1) circle (2pt) node[lab, left] {$1$};
\draw[faint] (1,-0.05) -- (1,0.05) node[tick, below=4pt] {$\lambda_{\min}$};
\draw[faint] (10,-0.05) -- (10,0.05) node[tick, below=4pt] {$\lambda_{\max}$};
\node[note, anchor=west] at (10.15,0.145) {$\pm1/T_4(\gamma)=\pm0.145$};
\end{tikzpicture}
\end{center}
```

The scaled Chebyshev polynomial of degree $4$ for $\kappa=10$ ($\lambda\in[1,10]$): it equals $1$ at the origin and stays within $\pm0.145$ on the whole interval (shaded band), smaller than any other degree-$4$ polynomial with $p(0)=1$ can manage. CG does at least this well after four steps.

:::

::: {#exm-cg-uniform-spectrum .example name="CG beats its bound"}

For a $400\times400$ symmetric positive definite matrix with eigenvalues spread uniformly over $[1,100]$ ($\kappa=100$) and a random right-hand side, the bound of @thm-cg-chebyshev-bound promises a reduction of the $A$-norm error by $0.82$ per step, about $10^{-3.2}$ after $40$ steps. The measured error after $40$ steps is $10^{-4.65}$: CG adapts to the actual eigenvalues. As the extreme eigenvalues are resolved by the Ritz values (@exm-ritz-values), the effective condition number of the remaining spectrum shrinks, and convergence accelerates (*superlinear convergence*).

:::

::: {#fig-cg-convergence-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.25cm, y=1.0cm]
\draw[->, faint] (0,0.5) -- (42,0.5) node[lab, right] {$n$};
\draw[->, faint] (0,0.5) -- (0,-5) node[lab, below] {$\log_{10}\lVert\mathbf{e}_n\rVert_A/\lVert\mathbf{e}_0\rVert_A$};
\foreach \x in {10,20,30,40} {\draw[faint] (\x,0.42) -- (\x,0.58); \node[tick, above] at (\x,0.58) {$\x$};}
\foreach \y in {-1,-2,-3,-4} {\draw[faint] (-0.3,\y) -- (0.3,\y); \node[tick, left] at (-0.3,\y) {$\y$};}
\draw[emph, dashed] plot coordinates {(0,0.3) (4,-0.05) (8,-0.4) (12,-0.74) (16,-1.09) (20,-1.44) (24,-1.79) (28,-2.14) (32,-2.49) (36,-2.84) (40,-3.18)};
\draw[hl] plot coordinates {(0,0) (4,-1.2) (8,-1.76) (12,-2.19) (16,-2.55) (20,-2.86) (24,-3.16) (28,-3.49) (32,-3.84) (36,-4.17) (40,-4.65)};
\node[lab] at (31,-1.9) {bound};
\node[lab] at (24,-3.6) {CG};
\end{tikzpicture}
\end{center}
```

Measured CG error for @exm-cg-uniform-spectrum against the Chebyshev bound $2(9/11)^n$ ($\kappa=100$). The actual curve is steeper than the bound and keeps getting steeper.

:::
