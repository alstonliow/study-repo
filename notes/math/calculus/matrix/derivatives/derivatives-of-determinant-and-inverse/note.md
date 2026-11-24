---
title: "Derivatives of the Determinant and the Inverse"
sources: [mit18s096-7, cs229-1]
requires: [math/calculus/matrix/derivatives/gradients-in-inner-product-spaces]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.S096 Matrix Calculus (IAP 2023), course notes Chapter 7 (two derivations of the derivative of the determinant, the characteristic polynomial, the logarithmic derivative, the Jacobian of the inverse), in our own wording; the examples are ours, checked in Python against finite differences; proofs written out in steps. Merged 2026-11-24 (owner): @cor-log-det-differential keeps its id and absorbs the log-determinant gradient of CS229 (lecture notes Chapter 4, formerly part 3 of @prp-matrix-gradient-rules, stated there for det A > 0); the statement for log|det A| and the differential form are from 18.S096, the cofactor argument (step 1 of @thm-jacobi-formula) is the CS229 proof. -->

Two matrix functions appear everywhere: the inverse, in every linear solve, and the determinant, in volumes, likelihoods and characteristic polynomials. Both have short derivatives once they are written as differentials.

::: {#thm-differential-inverse .theorem name="Derivative of the inverse"}

On invertible $n\times n$ matrices,

$$
d(A^{-1})=-A^{-1}\,dA\,A^{-1}.
$$

Its Jacobian matrix (@def-vec) is $-(A^{-\mathsf T})\otimes A^{-1}$.

:::

::: {.proof}

1. Differentiate $AA^{-1}=I$ with the product rule (@thm-differential-product-rule): $dA\,A^{-1}+A\,d(A^{-1})=0$, since $I$ is constant.

2. Multiply on the left by $A^{-1}$: $d(A^{-1})=-A^{-1}dA\,A^{-1}$.

3. By @thm-vec-kronecker-identity with the outer factors $-A^{-1}$ and $A^{-1}$, the Jacobian is $-(A^{-1})^{\mathsf T}\otimes A^{-1}$.

:::

For $1\times1$ matrices this is $d(1/a)=-da/a^2$; for matrices the two factors of $A^{-1}$ sit on either side of $dA$.

::: {#thm-jacobi-formula .theorem name="Jacobi's formula"}

For an $n\times n$ matrix $A$,

$$
d(\det A)=\operatorname{tr}\bigl(\operatorname{adj}(A)\,dA\bigr),
$$

where $\operatorname{adj}(A)$ is the adjugate (transposed cofactor matrix). If $A$ is invertible, $d(\det A)=\det A\,\operatorname{tr}(A^{-1}dA)$, and the Frobenius gradient (@def-gradient-inner-product) is $\nabla\det A=\operatorname{cof}A=\det A\,A^{-\mathsf T}$.

:::

::: {.proof}

1. *Cofactor derivation.* Expanding along row $i$, $\det A=\sum_ja_{ij}C_{ij}$, where the cofactors $C_{ij}$ do not involve row $i$. So $\partial\det A/\partial a_{ij}=C_{ij}$.

2. Hence $d(\det A)=\sum_{i,j}C_{ij}\,da_{ij}=\operatorname{tr}(C^{\mathsf T}dA)$, and $C^{\mathsf T}=\operatorname{adj}(A)$. The gradient is $C=\operatorname{cof}A$.

3. *Second derivation, for invertible $A$.* Write $\det(A+dA)=\det A\,\det(I+A^{-1}dA)$.

4. For a small matrix $E$, $\det(I+E)=\prod_i(1+\mu_i)$ over the eigenvalues $\mu_i$ of $E$, which is $1+\sum_i\mu_i$ to first order, that is $1+\operatorname{tr}E$.

5. So $d(\det A)=\det A\,\operatorname{tr}(A^{-1}dA)$. Since $\operatorname{adj}A=\det A\,A^{-1}$ (@sec-math-linear-algebra-determinants-cramers-rule-and-volume), the two forms agree.

:::

::: {#fig-derivatives-of-determinant-and-inverse-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.2cm, y=1.2cm]
\draw[regionA] (0,0) -- (2,1) -- (3,4) -- (1,3) -- cycle;
\node[lab] at (1.5,2) {$\det A$};
\draw[map] (0,0) -- (2,1) node[lab, below right] {$a_1$};
\draw[map] (0,0) -- (1,3) node[lab, above left] {$a_2$};
\draw[hl, dashed] (0,0) -- (2.4,1) -- (3.4,4) -- (1,3);
\draw[map, hl] (2,1) -- (2.4,1) node[lab, right] {$da_1$};
\end{tikzpicture}
\end{center}
```

The determinant is an area. Moving one column $a_1$ by $da_1$ changes the area to first order by a strip whose size is linear in $da_1$, with coefficients given by the cofactors of that column: this is step 1 of the proof.

:::

::: {#cor-log-det-differential .corollary name="The logarithmic derivative"}

For invertible $A$,

$$
d\bigl(\log\lvert\det A\rvert\bigr)=\operatorname{tr}(A^{-1}dA),\qquad \nabla\log\lvert\det A\rvert=A^{-\mathsf T}.
$$

In particular $\nabla_A\log\det A=(A^{-1})^{\mathsf T}$ on the open set where $\det A>0$; entrywise, $\partial\log\lvert\det A\rvert/\partial A_{ij}=(A^{-1})_{ji}$.

:::

::: {.proof}

1. By the chain rule, $d\log\lvert u\rvert=du/u$ for a nonzero scalar $u$.

2. With $u=\det A$ and @thm-jacobi-formula, $d\log\lvert\det A\rvert=\operatorname{tr}(A^{-1}dA)=\operatorname{tr}\bigl((A^{-\mathsf T})^{\mathsf T}dA\bigr)$.

:::

::: {#exm-derivatives-of-determinant-and-inverse-1 .example name="A two by two check"}

Let $A=\begin{bmatrix}2&1\\1&3\end{bmatrix}$, so $\det A=5$ and $A^{-1}=\frac15\begin{bmatrix}3&-1\\-1&2\end{bmatrix}$. Change only the corner, $dA=\varepsilon E_{11}$.

1. Jacobi's formula: $d(\det A)=5\operatorname{tr}(A^{-1}dA)=5\cdot\tfrac35\varepsilon=3\varepsilon$. Directly, $\det(A+\varepsilon E_{11})=(2+\varepsilon)3-1=5+3\varepsilon$.

2. Inverse: $d(A^{-1})=-A^{-1}E_{11}A^{-1}\varepsilon=-\varepsilon\begin{bmatrix}0.36&-0.12\\-0.12&0.04\end{bmatrix}$. A finite difference with $\varepsilon=10^{-7}$ in Python gives the same entries to seven digits.

:::

::: {#prp-characteristic-polynomial-derivative .proposition name="Derivative of the characteristic polynomial"}

Let $p(x)=\det(xI-A)$ and let $x$ not be an eigenvalue of $A$. Then

$$
\frac{p'(x)}{p(x)}=\operatorname{tr}\bigl((xI-A)^{-1}\bigr)=\sum_{i=1}^n\frac{1}{x-\lambda_i},
$$

where $\lambda_1,\dots,\lambda_n$ are the eigenvalues of $A$ with multiplicity.

:::

::: {.proof}

1. Put $M(x)=xI-A$, so $dM=I\,dx$.

2. By @cor-log-det-differential, $d\log\lvert p\rvert=\operatorname{tr}(M^{-1}I)\,dx$, so $p'/p=\operatorname{tr}\bigl((xI-A)^{-1}\bigr)$.

3. The eigenvalues of $(xI-A)^{-1}$ are $1/(x-\lambda_i)$, and the trace is their sum.

4. Alternatively, $p(x)=\prod_i(x-\lambda_i)$, and the logarithmic derivative of a product is the sum of the logarithmic derivatives of its factors.

:::

::: {#fig-derivatives-of-determinant-and-inverse-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\node[box] (A) at (0,0) {$dA$};
\node[box] (i1) at (2.4,0) {$A^{-1}dA$};
\node[hl box] (t) at (5.2,0.8) {$\operatorname{tr}(A^{-1}dA)$};
\node[hl box] (inv) at (5.2,-0.8) {$-A^{-1}dA\,A^{-1}$};
\draw[map] (A) -- (i1);
\draw[map] (i1) -- (t) node[lab, right, xshift=14mm] {$=d\log\lvert\det A\rvert$};
\draw[map] (i1) -- (inv) node[lab, right, xshift=16mm] {$=d(A^{-1})$};
\end{tikzpicture}
\end{center}
```

Both derivatives start from the same matrix $A^{-1}dA$, the relative change of $A$: its trace is the change of $\log\lvert\det A\rvert$, and multiplying it by $-A^{-1}$ on the right gives the change of $A^{-1}$.

:::
