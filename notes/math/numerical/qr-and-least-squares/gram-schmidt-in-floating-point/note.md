---
title: "Gram–Schmidt in Floating Point"
sources: [mit18335-9, mit18335-10]
requires: [math/numerical/qr-and-least-squares/householder-qr]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lectures 9 and 10 and the reading on Gram–Schmidt as projections, in our own wording; the loss-of-orthogonality experiments were run in Python with numpy (double precision). -->

Classical Gram–Schmidt (@thm-qr-factorization) subtracts from each column its projections onto the previous $\mathbf{q}$'s, all computed from the *original* column. Rearranging the same arithmetic so that each projection is removed from the *current* vector gives modified Gram–Schmidt. The two agree in exact arithmetic but behave very differently in floating point.

::: {#def-classical-modified-gram-schmidt .definition name="Classical and modified Gram–Schmidt"}

Let $\mathbf{a}_1,\dots,\mathbf{a}_n$ be the columns of a full-rank $m\times n$ matrix $A$. Both methods produce $\hat Q=[\mathbf{q}_1\cdots\mathbf{q}_n]$ and upper triangular $\hat R$ with $A=\hat Q\hat R$.

1. *Classical (CGS):* for $j=1,\dots,n$, set $r_{ij}=\mathbf{q}_i^{\mathsf H}\mathbf{a}_j$ for $i<j$, $\mathbf{v}_j=\mathbf{a}_j-\sum_{i<j}r_{ij}\mathbf{q}_i$, $r_{jj}=\lVert\mathbf{v}_j\rVert$, $\mathbf{q}_j=\mathbf{v}_j/r_{jj}$.

2. *Modified (MGS):* set $\mathbf{v}_j=\mathbf{a}_j$ for all $j$. For $i=1,\dots,n$: $r_{ii}=\lVert\mathbf{v}_i\rVert$, $\mathbf{q}_i=\mathbf{v}_i/r_{ii}$, and for every $j>i$, $r_{ij}=\mathbf{q}_i^{\mathsf H}\mathbf{v}_j$ and $\mathbf{v}_j\gets\mathbf{v}_j-r_{ij}\mathbf{q}_i$.

:::

```{=latex}
\begin{algorithm}
\caption{Modified Gram--Schmidt}
\begin{algorithmic}
\INPUT columns $\mathbf{a}_1,\dots,\mathbf{a}_n$ of $A$
\STATE $\mathbf{v}_j\gets\mathbf{a}_j$ for $j=1,\dots,n$
\FOR{$i=1,\dots,n$}
    \STATE $r_{ii}\gets\lVert\mathbf{v}_i\rVert$; \quad $\mathbf{q}_i\gets\mathbf{v}_i/r_{ii}$
    \FOR{$j=i+1,\dots,n$}
        \STATE $r_{ij}\gets\mathbf{q}_i^{\mathsf H}\mathbf{v}_j$ \COMMENT{CGS would use $\mathbf{a}_j$ here}
        \STATE $\mathbf{v}_j\gets\mathbf{v}_j-r_{ij}\mathbf{q}_i$
    \ENDFOR
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

::: {#prp-cgs-mgs-equivalent .proposition name="CGS and MGS agree in exact arithmetic"}

In exact arithmetic CGS and MGS compute the same $\hat Q$ and $\hat R$. Both cost $\sim2mn^2$ flops.

:::

::: {.proof}

1. Let $P_i=I-\mathbf{q}_i\mathbf{q}_i^{\mathsf H}$. In MGS, when $\mathbf{q}_j$ is formed, $\mathbf{v}_j=P_{j-1}\cdots P_1\mathbf{a}_j$; in CGS, $\mathbf{v}_j=(I-\sum_{i<j}\mathbf{q}_i\mathbf{q}_i^{\mathsf H})\mathbf{a}_j$.

2. Since the $\mathbf{q}_i$ are orthonormal, $\mathbf{q}_i^{\mathsf H}\mathbf{q}_k=0$ for $i\ne k$, so expanding the product $P_{j-1}\cdots P_1$ every cross term $\mathbf{q}_i\mathbf{q}_i^{\mathsf H}\mathbf{q}_k\mathbf{q}_k^{\mathsf H}$ vanishes and the product equals $I-\sum_{i<j}\mathbf{q}_i\mathbf{q}_i^{\mathsf H}$. So the $\mathbf{v}_j$, hence the $\mathbf{q}_j$ and $r_{jj}$, agree.

3. For $i<j$, MGS computes $r_{ij}=\mathbf{q}_i^{\mathsf H}P_{i-1}\cdots P_1\mathbf{a}_j=\mathbf{q}_i^{\mathsf H}\mathbf{a}_j$, because $\mathbf{q}_i^{\mathsf H}\mathbf{q}_k=0$ for $k<i$.

4. *Cost.* In both, the pair $(i,j)$ with $i<j$ costs an inner product and an update, about $4m$ flops; there are $\sim n^2/2$ pairs, giving $\sim2mn^2$.

:::

::: {#rmk-gram-schmidt-in-floating-point-1 .remark name="MGS is triangular orthogonalization"}

Step $i$ of MGS replaces $[\mathbf{v}_i\ \mathbf{v}_{i+1}\cdots\mathbf{v}_n]$ by $[\mathbf{q}_i\ \mathbf{v}_{i+1}'\cdots\mathbf{v}_n']$, which is right multiplication by an upper triangular matrix $R_i$ (identity except in row $i$). So $AR_1R_2\cdots R_n=\hat Q$ and $\hat R=(R_1\cdots R_n)^{-1}$. Householder's method is the mirror image, $Q_n\cdots Q_1A=R$ with unitary factors on the left, and only it multiplies by perfectly conditioned matrices; the triangular $R_i$ can be ill-conditioned when $A$ is.

:::

::: {#exm-lauchli-gram-schmidt .example name="Three nearly parallel columns"}

Take $\varepsilon=10^{-8}$, so $\varepsilon^2<\varepsilon_{\text{mach}}$ in double precision, and
$$A=\begin{bmatrix}1&1&1\\\varepsilon&0&0\\0&\varepsilon&0\\0&0&\varepsilon\end{bmatrix}.$$
Then $\operatorname{fl}(1+\varepsilon^2)=1$, so $\mathbf{q}_1=(1,\varepsilon,0,0)$. Both methods give $\mathbf{q}_2=(0,-1,1,0)/\sqrt2$. For the third column CGS subtracts the projections of the original $\mathbf{a}_3$, getting $\mathbf{v}_3=(0,-\varepsilon,0,\varepsilon)$ and $\mathbf{q}_3=(0,-1,0,1)/\sqrt2$, so $\mathbf{q}_2^{\mathsf T}\mathbf{q}_3=\tfrac12$: the two vectors are $60^\circ$ apart instead of $90^\circ$. MGS subtracts the $\mathbf{q}_2$ component from the already reduced vector and gets $\mathbf{q}_3=(0,-1,-1,2)/\sqrt6$, orthogonal to $\mathbf{q}_2$ to working precision. (Checked numerically: $\mathbf{q}_2^{\mathsf T}\mathbf{q}_3=0.5$ for CGS and $0$ for MGS.)

:::

::: {#fig-gram-schmidt-in-floating-point-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.5]
\draw[emph, ->] (0,0) -- (1.6,0) node[lab, right] {$\mathbf{q}_2$};
\draw[hl, ->] (0,0) -- (60:1.6) node[lab, above] {$\mathbf{q}_3$};
\draw[faint] (0.4,0) arc (0:60:0.4); \node[lab] at (30:0.62) {$60^\circ$};
\node[lab] at (0.8,-0.4) {classical};
\begin{scope}[xshift=3cm]
\draw[emph, ->] (0,0) -- (1.6,0) node[lab, right] {$\mathbf{q}_2$};
\draw[hl, ->] (0,0) -- (90:1.6) node[lab, above] {$\mathbf{q}_3$};
\draw[faint] (0.25,0) -- (0.25,0.25) -- (0,0.25);
\node[lab] at (0.8,-0.4) {modified};
\end{scope}
\end{tikzpicture}
\end{center}
```

The vectors $\mathbf{q}_2,\mathbf{q}_3$ computed for the matrix of @exm-lauchli-gram-schmidt, drawn in the plane they span. Classical Gram–Schmidt loses orthogonality completely; modified Gram–Schmidt keeps it.

:::

::: {#rmk-gram-schmidt-in-floating-point-2 .remark name="How much orthogonality is lost"}

Error analyses (Björck for MGS, later work for CGS) and experiments agree on the typical behaviour for a full-rank $A$ with condition number $\kappa(A)$:
$$\lVert I-\tilde Q^{\mathsf H}\tilde Q\rVert\approx\begin{cases}\kappa(A)^2\,\varepsilon_{\text{mach}}&\text{CGS},\\ \kappa(A)\,\varepsilon_{\text{mach}}&\text{MGS},\\ \varepsilon_{\text{mach}}&\text{Householder},\end{cases}$$
as long as $\kappa(A)^2\varepsilon_{\text{mach}}$ (respectively $\kappa(A)\varepsilon_{\text{mach}}$) is below $1$. Even so, the *product* $\tilde Q\tilde R$ is close to $A$ for both Gram–Schmidt variants; what fails is the orthogonality of $\tilde Q$. Running CGS a second time on its own output ("twice is enough") restores orthogonality to $O(\varepsilon_{\text{mach}})$ when $\kappa(A)\varepsilon_{\text{mach}}\ll1$, and is used in Krylov methods (@sec-math-numerical-krylov-methods-arnoldi-iteration) because CGS uses matrix–vector products, which run faster than the vector updates of MGS.

:::

::: {#fig-gram-schmidt-in-floating-point-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.42cm, y=0.3cm]
\draw[->, faint] (0,-16) -- (17.5,-16) node[lab, right] {$\log_{10}\kappa(A)$};
\draw[->, faint] (0,-16) -- (0,2.5) node[lab, above] {$\log_{10}\lVert I-\tilde Q^{\mathsf T}\tilde Q\rVert_2$};
\foreach \x in {0,4,8,12,16} {\draw[faint] (\x,-16.3) -- (\x,-15.7); \node[tick, below] at (\x,-16.3) {$\x$};}
\foreach \y in {-16,-12,-8,-4,0} {\draw[faint] (-0.2,\y) -- (0.2,\y); \node[tick, left] at (-0.2,\y) {$\y$};}
\draw[hl] plot coordinates {(0,-15.32) (2,-13.16) (4,-7.84) (6,-3.91) (8,0.2) (10,0.61) (12,0.8) (14,0.92) (16,1.0)};
\draw[emph] plot coordinates {(0,-15.31) (2,-14.14) (4,-12.26) (6,-10.57) (8,-8.44) (10,-6.29) (12,-4.29) (14,-2.82) (16,-1.11)};
\draw[emph, dashed] plot coordinates {(0,-14.91) (2,-15.08) (4,-15.14) (6,-14.98) (8,-15.08) (10,-14.95) (12,-15.06) (14,-15.05) (16,-15.12)};
\foreach \p in {(0,-15.32),(2,-13.16),(4,-7.84),(6,-3.91),(8,0.2),(10,0.61),(12,0.8),(14,0.92),(16,1.0)} {\fill[accent] \p circle (2pt);}
\foreach \p in {(0,-15.31),(2,-14.14),(4,-12.26),(6,-10.57),(8,-8.44),(10,-6.29),(12,-4.29),(14,-2.82),(16,-1.11)} {\fill \p circle (2pt);}
\node[lab] at (6.3,-1.6) {CGS};
\node[lab] at (12.3,-7.2) {MGS};
\node[lab] at (12,-13.7) {Householder};
\end{tikzpicture}
\end{center}
```

Loss of orthogonality for $60\times20$ matrices $A=U\Sigma V^{\mathsf T}$ with random orthogonal $U,V$ and singular values spaced geometrically from $1$ to $1/\kappa$. Classical Gram–Schmidt loses orthogonality like $\kappa^2\varepsilon_{\text{mach}}$ (slope $2$) and has none left at $\kappa=10^8$; modified Gram–Schmidt like $\kappa\varepsilon_{\text{mach}}$ (slope $1$); Householder stays at $\varepsilon_{\text{mach}}$.

:::
