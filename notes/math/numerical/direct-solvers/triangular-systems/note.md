---
title: "Triangular Systems and Back Substitution"
sources: [mit18335-13]
requires: [math/numerical/floating-point/stability-and-backward-error]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 13 (with the back-substitution analysis used in the course's QR and LU lectures), in our own wording; proofs written out in steps, condition numbers computed with numpy. -->

Every direct method for $A\mathbf{x}=\mathbf{b}$ (LU, Cholesky, QR) ends by solving triangular systems. Back substitution is cheap and backward stable in a strong, entry-by-entry sense; any inaccuracy in its answer comes from the conditioning of the triangular matrix.

::: {#def-back-substitution .definition name="Back substitution"}

For an invertible upper triangular $R\in\mathbb{C}^{m\times m}$, solve $R\mathbf{x}=\mathbf{b}$ from the last equation upwards:
$$x_m=\frac{b_m}{r_{mm}},\qquad x_j=\frac{b_j-\sum_{k=j+1}^mr_{jk}x_k}{r_{jj}}\quad(j=m-1,\dots,1).$$
*Forward substitution* solves a lower triangular system $L\mathbf{y}=\mathbf{b}$ from the top down in the same way.

:::

```{=latex}
\begin{algorithm}
\caption{Back substitution}
\begin{algorithmic}
\INPUT upper triangular $R$ with $r_{jj}\ne0$, right side $\mathbf{b}$
\FOR{$j=m,m-1,\dots,1$}
    \STATE $s\gets b_j$
    \FOR{$k=j+1,\dots,m$}
        \STATE $s\gets s-r_{jk}x_k$
    \ENDFOR
    \STATE $x_j\gets s/r_{jj}$
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

::: {#fig-triangular-systems-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.55]
\foreach \i in {1,...,5} {\foreach \j in {\i,...,5} {\draw[cell frame] ({\j-1},{-\i}) rectangle ++(1,1);}}
\foreach \j in {4,5} {\draw[hl cell] ({\j-1},-3) rectangle ++(1,1);}
\draw[hl cell] (2,-3) rectangle ++(1,1);
\node[lab] at (2.5,0.6) {$R$};
\foreach \i in {1,...,5} {\draw[cell frame] (6.2,{-\i}) rectangle ++(1,1);}
\foreach \i in {4,5} {\draw[hl cell] (6.2,{-\i}) rectangle ++(1,1); \node[tick] at (6.7,{-\i+0.5}) {done};}
\draw[hl] (6.2,-3) rectangle ++(1,1); \node[tick] at (6.7,-2.5) {$x_3$};
\node[lab] at (6.7,0.6) {$\mathbf{x}$};
\node[lab] at (8.2,-2.5) {$=$};
\foreach \i in {1,...,5} {\draw[cell frame] (9.2,{-\i}) rectangle ++(1,1);}
\draw[hl cell] (9.2,-3) rectangle ++(1,1);
\node[lab] at (9.7,0.6) {$\mathbf{b}$};
\end{tikzpicture}
\end{center}
```

Back substitution on a $5\times5$ system, computing $x_3$: it uses row $3$ of $R$ (shaded), the already known $x_4,x_5$, and $b_3$. Row $j$ costs about $2(m-j)$ flops, $m^2$ in total.

:::

::: {#thm-back-substitution-backward-stable .theorem name="Back substitution is backward stable"}

The solution $\tilde{\mathbf{x}}$ computed by back substitution in floating point satisfies
$$(R+\delta R)\,\tilde{\mathbf{x}}=\mathbf{b}\qquad\text{with}\qquad\lvert\delta r_{jk}\rvert\le m\,\varepsilon_{\text{mach}}\lvert r_{jk}\rvert+O(\varepsilon_{\text{mach}}^2)\ \text{ for all }j,k.$$
In particular $\lVert\delta R\rVert/\lVert R\rVert=O(\varepsilon_{\text{mach}})$, and by @thm-backward-stable-accuracy and @thm-condition-linear-system the forward error is $O(\kappa(R)\,\varepsilon_{\text{mach}})$.

:::

::: {.proof}

1. Fix a row $j$. The computed $\tilde x_j$ results from forming the products $r_{jk}\tilde x_k$ for $k>j$, subtracting them one by one from $b_j$, and dividing by $r_{jj}$. Each operation has a factor $(1+\varepsilon)$, $\lvert\varepsilon\rvert\le\varepsilon_{\text{mach}}$ (@def-floating-point-operations).

2. Following the analysis of recursive summation (@thm-naive-summation-backward), the computed value satisfies
$$\tilde x_j\,r_{jj}(1+\eta_{jj})=b_j-\sum_{k>j}r_{jk}\tilde x_k(1+\eta_{jk}),$$
where each $1+\eta$ is a product of at most $m$ factors $(1+\varepsilon)^{\pm1}$: one for the product $r_{jk}\tilde x_k$, the subtractions it passes through, and the division moved to the left side. The factors from the subtractions that also touch $b_j$ are divided out and moved onto the other terms, so $b_j$ itself is unperturbed.

3. Hence $\lvert\eta_{jk}\rvert\le m\varepsilon_{\text{mach}}+O(\varepsilon_{\text{mach}}^2)$. Setting $\delta r_{jk}=r_{jk}\eta_{jk}$ for all $k\ge j$ turns the last display into row $j$ of $(R+\delta R)\tilde{\mathbf{x}}=\mathbf{b}$.

4. This holds for every row with the same $\tilde{\mathbf{x}}$, because each row equation involves only the computed values $\tilde x_k$, which are fixed once computed.

:::

::: {#exm-ill-conditioned-triangular .example name="A triangular matrix with exponential condition number"}

Let $R_m$ have ones on the diagonal and $-1$ everywhere above it. Its inverse is upper triangular with entries $(R_m^{-1})_{jk}=2^{k-j-1}$ for $k>j$, so the last column of $R_m^{-1}$ sums to $2^{m-1}$ and
$$\kappa_1(R_m)=\lVert R_m\rVert_1\lVert R_m^{-1}\rVert_1=m\cdot2^{m-1}.$$
For $m=30$ this is $1.6\times10^{10}$ (and $\kappa_2\approx6.5\times10^9$), although every entry of $R_m$ is $0$ or $\pm1$ and its determinant is $1$. Back substitution with $R_{30}$ is still backward stable, but the answer may lose ten digits; small diagonal entries or a determinant near zero are not needed for ill-conditioning.

:::

::: {#fig-triangular-systems-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.2cm, y=0.4cm]
\draw[->, faint] (0,0) -- (32,0) node[lab, right] {$m$};
\draw[->, faint] (0,0) -- (0,11) node[lab, above] {$\log_{10}\kappa(R_m)$};
\foreach \x in {5,10,...,30} {\draw[faint] (\x,-0.15) -- (\x,0.15); \node[tick, below] at (\x,-0.15) {$\x$};}
\foreach \y in {2,4,...,10} {\draw[faint] (-0.3,\y) -- (0.3,\y); \node[tick, left] at (-0.3,\y) {$\y$};}
\draw[hl] plot coordinates {(5,1.90) (10,3.71) (15,5.39) (20,7.02) (25,8.62) (30,10.21)};
\draw[emph] plot coordinates {(5,1.47) (10,3.28) (15,4.98) (20,6.62) (25,8.23) (30,9.81)};
\node[lab] at (22,8.9) {$\kappa_1$};
\node[lab] at (26,7.6) {$\kappa_2$};
\end{tikzpicture}
\end{center}
```

Condition numbers of the $\pm1$ triangular matrices of @exm-ill-conditioned-triangular grow like $2^m$: about $0.3$ decimal digits are lost per extra row.

:::
