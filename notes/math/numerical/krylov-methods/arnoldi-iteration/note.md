---
title: "Krylov Subspaces and the Arnoldi Iteration"
sources: [mit18335-18]
requires: [math/numerical/eigenvalue-algorithms/hessenberg-reduction, math/numerical/qr-and-least-squares/gram-schmidt-in-floating-point]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 18 (Krylov methods and the Arnoldi algorithm), in our own wording; proofs written out in steps; Ritz values computed with numpy. -->

For a large sparse matrix we can afford matrix–vector products but not $O(m^3)$ factorizations. Krylov methods build approximations from the vectors $\mathbf{b},A\mathbf{b},A^2\mathbf{b},\dots$, which cost one product each. The Arnoldi iteration orthonormalises these vectors and, as a by-product, produces the first $n$ columns of a Hessenberg reduction of $A$: a small matrix that captures how $A$ acts on the Krylov space.

::: {#def-krylov-subspace .definition name="Krylov subspace"}

For $A\in\mathbb{C}^{m\times m}$ and $\mathbf{b}\in\mathbb{C}^m$, the $n$-th *Krylov subspace* is
$$\mathcal K_n=\mathcal K_n(A,\mathbf{b})=\operatorname{span}\{\mathbf{b},A\mathbf{b},\dots,A^{n-1}\mathbf{b}\}=\{p(A)\mathbf{b}:\ p\text{ a polynomial of degree}<n\}.$$

:::

The vectors $A^j\mathbf{b}$ themselves are a terrible basis: by power iteration they all turn towards the dominant eigenvector, so the Krylov matrix $[\mathbf{b}\ A\mathbf{b}\cdots A^{n-1}\mathbf{b}]$ is extremely ill-conditioned. An orthonormal basis is built one vector at a time instead.

::: {#def-arnoldi-iteration .definition name="Arnoldi iteration"}

Set $\mathbf{q}_1=\mathbf{b}/\lVert\mathbf{b}\rVert$. For $n=1,2,\dots$: compute $\mathbf{v}=A\mathbf{q}_n$, orthogonalise it against $\mathbf{q}_1,\dots,\mathbf{q}_n$ by modified Gram–Schmidt, recording $h_{jn}=\mathbf{q}_j^{\mathsf H}\mathbf{v}$, and set $h_{n+1,n}=\lVert\mathbf{v}\rVert$, $\mathbf{q}_{n+1}=\mathbf{v}/h_{n+1,n}$. Let $Q_n=[\mathbf{q}_1\cdots\mathbf{q}_n]$, let $\tilde H_n$ be the $(n+1)\times n$ upper Hessenberg matrix of the $h_{ij}$, and $H_n$ its first $n$ rows.

:::

```{=latex}
\begin{algorithm}
\caption{Arnoldi iteration}
\begin{algorithmic}
\INPUT $A$ (as a routine computing $A\mathbf{x}$), $\mathbf{b}\ne\mathbf{0}$
\STATE $\mathbf{q}_1\gets\mathbf{b}/\lVert\mathbf{b}\rVert$
\FOR{$n=1,2,\dots$}
    \STATE $\mathbf{v}\gets A\mathbf{q}_n$
    \FOR{$j=1,\dots,n$}
        \STATE $h_{jn}\gets\mathbf{q}_j^{\mathsf H}\mathbf{v}$; \quad $\mathbf{v}\gets\mathbf{v}-h_{jn}\mathbf{q}_j$
    \ENDFOR
    \STATE $h_{n+1,n}\gets\lVert\mathbf{v}\rVert$ \COMMENT{if $0$: $\mathcal K_n$ is invariant, stop}
    \STATE $\mathbf{q}_{n+1}\gets\mathbf{v}/h_{n+1,n}$
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

::: {#thm-arnoldi-relation .theorem name="The Arnoldi relation"}

As long as no $h_{k+1,k}$ vanishes for $k\le n$, the columns of $Q_n$ form an orthonormal basis of $\mathcal K_n$, and
$$AQ_n=Q_{n+1}\tilde H_n=Q_nH_n+h_{n+1,n}\mathbf{q}_{n+1}\mathbf{e}_n^{\mathsf T},\qquad H_n=Q_n^{\mathsf H}AQ_n .$$
If $h_{n+1,n}=0$, then $\mathcal K_n$ is invariant under $A$ and every eigenvalue of $H_n$ is an eigenvalue of $A$.

:::

::: {.proof}

1. Column $n$ of the recurrence reads $A\mathbf{q}_n=\sum_{j\le n+1}h_{jn}\mathbf{q}_j$, which is column $n$ of $AQ_n=Q_{n+1}\tilde H_n$. The second form splits off the last row of $\tilde H_n$.

2. The $\mathbf{q}_j$ are orthonormal by construction (Gram–Schmidt), so multiplying by $Q_n^{\mathsf H}$ and using $Q_n^{\mathsf H}\mathbf{q}_{n+1}=\mathbf{0}$ gives $H_n=Q_n^{\mathsf H}AQ_n$.

3. *Spans.* By induction, $\mathbf{q}_{k+1}$ is a combination of $A\mathbf{q}_k$ and $\mathbf{q}_1,\dots,\mathbf{q}_k$, all in $\mathcal K_{k+1}$ if $\mathbf{q}_1,\dots,\mathbf{q}_k\in\mathcal K_k$. Since $h_{k+1,k}\ne0$, $A\mathbf{q}_k$ (and hence $A^k\mathbf{b}$, up to lower terms) lies in the span of $\mathbf{q}_1,\dots,\mathbf{q}_{k+1}$, so the spans agree and have dimension $k+1$.

4. If $h_{n+1,n}=0$, then $AQ_n=Q_nH_n$: $\mathcal K_n=\operatorname{range}Q_n$ is invariant, and if $H_n\mathbf{y}=\theta\mathbf{y}$ then $A(Q_n\mathbf{y})=\theta Q_n\mathbf{y}$.

:::

::: {#fig-arnoldi-iteration-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.04,0.05) -- (-0.10,0.05) -- (-0.10,-2.09) -- (-0.04,-2.09);
\draw[faint] (2.08,0.05) -- (2.14,0.05) -- (2.14,-2.09) -- (2.08,-2.09);
\node[tick] at (0.17,-0.17) {$\times$};
\node[tick] at (0.51,-0.17) {$\times$};
\node[tick] at (0.85,-0.17) {$\times$};
\node[tick] at (1.19,-0.17) {$\times$};
\node[tick] at (1.53,-0.17) {$\times$};
\node[tick] at (1.87,-0.17) {$\times$};
\node[tick] at (0.17,-0.51) {$\times$};
\node[tick] at (0.51,-0.51) {$\times$};
\node[tick] at (0.85,-0.51) {$\times$};
\node[tick] at (1.19,-0.51) {$\times$};
\node[tick] at (1.53,-0.51) {$\times$};
\node[tick] at (1.87,-0.51) {$\times$};
\node[tick] at (0.17,-0.85) {$\times$};
\node[tick] at (0.51,-0.85) {$\times$};
\node[tick] at (0.85,-0.85) {$\times$};
\node[tick] at (1.19,-0.85) {$\times$};
\node[tick] at (1.53,-0.85) {$\times$};
\node[tick] at (1.87,-0.85) {$\times$};
\node[tick] at (0.17,-1.19) {$\times$};
\node[tick] at (0.51,-1.19) {$\times$};
\node[tick] at (0.85,-1.19) {$\times$};
\node[tick] at (1.19,-1.19) {$\times$};
\node[tick] at (1.53,-1.19) {$\times$};
\node[tick] at (1.87,-1.19) {$\times$};
\node[tick] at (0.17,-1.53) {$\times$};
\node[tick] at (0.51,-1.53) {$\times$};
\node[tick] at (0.85,-1.53) {$\times$};
\node[tick] at (1.19,-1.53) {$\times$};
\node[tick] at (1.53,-1.53) {$\times$};
\node[tick] at (1.87,-1.53) {$\times$};
\node[tick] at (0.17,-1.87) {$\times$};
\node[tick] at (0.51,-1.87) {$\times$};
\node[tick] at (0.85,-1.87) {$\times$};
\node[tick] at (1.19,-1.87) {$\times$};
\node[tick] at (1.53,-1.87) {$\times$};
\node[tick] at (1.87,-1.87) {$\times$};
\node[note] at (1.02,-2.39) {$A$};
\node[lbl] at (2.42,-1.02) {};
\draw[faint] (2.75,0.05) -- (2.69,0.05) -- (2.69,-2.09) -- (2.75,-2.09);
\draw[faint] (3.85,0.05) -- (3.91,0.05) -- (3.91,-2.09) -- (3.85,-2.09);
\node[tick] at (2.96,-0.17) {$\times$};
\node[tick] at (3.30,-0.17) {$\times$};
\node[tick] at (3.64,-0.17) {$\times$};
\node[tick] at (2.96,-0.51) {$\times$};
\node[tick] at (3.30,-0.51) {$\times$};
\node[tick] at (3.64,-0.51) {$\times$};
\node[tick] at (2.96,-0.85) {$\times$};
\node[tick] at (3.30,-0.85) {$\times$};
\node[tick] at (3.64,-0.85) {$\times$};
\node[tick] at (2.96,-1.19) {$\times$};
\node[tick] at (3.30,-1.19) {$\times$};
\node[tick] at (3.64,-1.19) {$\times$};
\node[tick] at (2.96,-1.53) {$\times$};
\node[tick] at (3.30,-1.53) {$\times$};
\node[tick] at (3.64,-1.53) {$\times$};
\node[tick] at (2.96,-1.87) {$\times$};
\node[tick] at (3.30,-1.87) {$\times$};
\node[tick] at (3.64,-1.87) {$\times$};
\node[note] at (3.30,-2.39) {$Q_3$};
\node[lbl] at (4.19,-1.02) {$=$};
\draw[faint] (4.52,0.05) -- (4.46,0.05) -- (4.46,-2.09) -- (4.52,-2.09);
\draw[faint] (5.96,0.05) -- (6.02,0.05) -- (6.02,-2.09) -- (5.96,-2.09);
\node[tick] at (4.73,-0.17) {$\times$};
\node[tick] at (5.07,-0.17) {$\times$};
\node[tick] at (5.41,-0.17) {$\times$};
\node[tick] at (5.75,-0.17) {$\times$};
\node[tick] at (4.73,-0.51) {$\times$};
\node[tick] at (5.07,-0.51) {$\times$};
\node[tick] at (5.41,-0.51) {$\times$};
\node[tick] at (5.75,-0.51) {$\times$};
\node[tick] at (4.73,-0.85) {$\times$};
\node[tick] at (5.07,-0.85) {$\times$};
\node[tick] at (5.41,-0.85) {$\times$};
\node[tick] at (5.75,-0.85) {$\times$};
\node[tick] at (4.73,-1.19) {$\times$};
\node[tick] at (5.07,-1.19) {$\times$};
\node[tick] at (5.41,-1.19) {$\times$};
\node[tick] at (5.75,-1.19) {$\times$};
\node[tick] at (4.73,-1.53) {$\times$};
\node[tick] at (5.07,-1.53) {$\times$};
\node[tick] at (5.41,-1.53) {$\times$};
\node[tick] at (5.75,-1.53) {$\times$};
\node[tick] at (4.73,-1.87) {$\times$};
\node[tick] at (5.07,-1.87) {$\times$};
\node[tick] at (5.41,-1.87) {$\times$};
\node[tick] at (5.75,-1.87) {$\times$};
\node[note] at (5.24,-2.39) {$Q_4$};
\node[lbl] at (6.30,-1.02) {};
\draw[faint] (6.63,0.05) -- (6.57,0.05) -- (6.57,-1.41) -- (6.63,-1.41);
\draw[faint] (7.73,0.05) -- (7.79,0.05) -- (7.79,-1.41) -- (7.73,-1.41);
\node[tick] at (6.84,-0.17) {$\times$};
\node[tick] at (7.18,-0.17) {$\times$};
\node[tick] at (7.52,-0.17) {$\times$};
\node[tick] at (6.84,-0.51) {$\times$};
\node[tick] at (7.18,-0.51) {$\times$};
\node[tick] at (7.52,-0.51) {$\times$};
\node[tick] at (7.18,-0.85) {$\times$};
\node[tick] at (7.52,-0.85) {$\times$};
\fill[accentLight] (7.37,-1.34) rectangle (7.67,-1.04);
\node[tick] at (7.52,-1.19) {$\times$};
\node[note] at (7.18,-1.71) {$\tilde H_3$};
\end{tikzpicture}
\end{center}
```

The Arnoldi relation $AQ_n=Q_{n+1}\tilde H_n$ for $n=3$: a tall $m\times m$ matrix times $m\times3$ equals $m\times4$ times a $4\times3$ Hessenberg matrix. The extra last row (shaded) holds $h_{4,3}$.

:::

::: {#def-ritz-values .definition name="Ritz values"}

The eigenvalues $\theta_1,\dots,\theta_n$ of $H_n$ are the *Ritz values* (or Arnoldi eigenvalue estimates) of $A$ at step $n$, and $Q_n\mathbf{y}$ for an eigenvector $\mathbf{y}$ of $H_n$ is a *Ritz vector*. They are the eigenvalues of the restriction of $A$ to $\mathcal K_n$ followed by orthogonal projection back onto $\mathcal K_n$.

:::

::: {#thm-arnoldi-polynomial .theorem name="Arnoldi as polynomial approximation"}

If $\dim\mathcal K_n=n$, the characteristic polynomial $p_n(z)=\det(zI-H_n)$ is the unique monic polynomial of degree $n$ that minimises $\lVert p(A)\mathbf{b}\rVert$ over all monic polynomials $p$ of degree $n$.

:::

::: {.proof}

1. For monic $p$ of degree $n$, $p(A)\mathbf{b}=A^n\mathbf{b}-\mathbf{y}$ with $\mathbf{y}\in\mathcal K_n$, and every $\mathbf{y}\in\mathcal K_n$ arises. So the minimum is attained exactly when $\mathbf{y}$ is the orthogonal projection of $A^n\mathbf{b}$ onto $\mathcal K_n$, i.e. when $p(A)\mathbf{b}\perp\mathcal K_n$, equivalently $Q_n^{\mathsf H}p(A)\mathbf{b}=\mathbf{0}$; this $p$ is unique.

2. *Claim:* $Q_n^{\mathsf H}A^k\mathbf{q}_1=H_n^k\mathbf{e}_1$ for $0\le k\le n$. For $k=0$ both sides are $\mathbf{e}_1$. If it holds for some $k<n$, then $A^k\mathbf{q}_1\in\mathcal K_n$, so $A^k\mathbf{q}_1=Q_nQ_n^{\mathsf H}A^k\mathbf{q}_1$ and $Q_n^{\mathsf H}A^{k+1}\mathbf{q}_1=(Q_n^{\mathsf H}AQ_n)(Q_n^{\mathsf H}A^k\mathbf{q}_1)=H_nH_n^k\mathbf{e}_1$.

3. Hence $Q_n^{\mathsf H}p_n(A)\mathbf{q}_1=p_n(H_n)\mathbf{e}_1=\mathbf{0}$ by the Cayley–Hamilton theorem (@thm-cayley-hamilton). By step 1, $p_n$ is the minimiser.

:::

Since $\lVert p(A)\mathbf{b}\rVert$ is small when $p$ has roots near eigenvalues of $A$ that $\mathbf{b}$ excites, the Ritz values approximate eigenvalues, the *extreme*, isolated ones first: a degree-$n$ polynomial can be small on most of the spectrum and still have a root next to an outlier.

::: {#exm-ritz-values .example name="Ritz values converge to outlying eigenvalues"}

Let $A$ be diagonal with $100$ eigenvalues equally spaced in $[0,2]$ and two outliers $2.5$ and $3$, and $\mathbf{b}=(1,\dots,1)$. The largest Ritz value is $2.431$ at $n=3$, $2.989$ at $n=6$ and $3.000$ to three decimals from $n=8$; the second outlier $2.5$ appears to three decimals at $n=10$. Meanwhile the Ritz values inside $[0,2]$ only gradually fill out the interval.

:::

::: {#fig-arnoldi-iteration-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=3.2cm, y=0.32cm]
\node[tick, anchor=east] at (-0.08,-1) {$n=1$};
\draw[faint] (0,-1) -- (3.1,-1);
\fill (1.034,-1) circle (1.7pt);
\node[tick, anchor=east] at (-0.08,-2) {$n=2$};
\draw[faint] (0,-2) -- (3.1,-2);
\fill (0.491,-2) circle (1.7pt); \fill (1.758,-2) circle (1.7pt);
\node[tick, anchor=east] at (-0.08,-3) {$n=3$};
\draw[faint] (0,-3) -- (3.1,-3);
\fill (0.295,-3) circle (1.7pt); \fill (1.328,-3) circle (1.7pt); \fill (2.431,-3) circle (1.7pt);
\node[tick, anchor=east] at (-0.08,-4) {$n=4$};
\draw[faint] (0,-4) -- (3.1,-4);
\fill (0.176,-4) circle (1.7pt); \fill (0.867,-4) circle (1.7pt); \fill (1.707,-4) circle (1.7pt); \fill (2.873,-4) circle (1.7pt);
\node[tick, anchor=east] at (-0.08,-5) {$n=5$};
\draw[faint] (0,-5) -- (3.1,-5);
\fill (0.118,-5) circle (1.7pt); \fill (0.615,-5) circle (1.7pt); \fill (1.327,-5) circle (1.7pt); \fill (1.926,-5) circle (1.7pt); \fill (2.963,-5) circle (1.7pt);
\node[tick, anchor=east] at (-0.08,-6) {$n=6$};
\draw[faint] (0,-6) -- (3.1,-6);
\fill (0.083,-6) circle (1.7pt); \fill (0.457,-6) circle (1.7pt); \fill (1.034,-6) circle (1.7pt); \fill (1.668,-6) circle (1.7pt); \fill (2.227,-6) circle (1.7pt); \fill (2.989,-6) circle (1.7pt);
\node[tick, anchor=east] at (-0.08,-7) {$n=7$};
\draw[faint] (0,-7) -- (3.1,-7);
\fill (0.059,-7) circle (1.7pt); \fill (0.337,-7) circle (1.7pt); \fill (0.785,-7) circle (1.7pt); \fill (1.318,-7) circle (1.7pt); \fill (1.815,-7) circle (1.7pt); \fill (2.44,-7) circle (1.7pt); \fill (2.998,-7) circle (1.7pt);
\node[tick, anchor=east] at (-0.08,-8) {$n=8$};
\draw[faint] (0,-8) -- (3.1,-8);
\fill (0.042,-8) circle (1.7pt); \fill (0.255,-8) circle (1.7pt); \fill (0.605,-8) circle (1.7pt); \fill (1.043,-8) circle (1.7pt); \fill (1.501,-8) circle (1.7pt); \fill (1.882,-8) circle (1.7pt); \fill (2.49,-8) circle (1.7pt); \fill (3.0,-8) circle (1.7pt);
\node[tick, anchor=east] at (-0.08,-9) {$n=9$};
\draw[faint] (0,-9) -- (3.1,-9);
\fill (0.031,-9) circle (1.7pt); \fill (0.198,-9) circle (1.7pt); \fill (0.479,-9) circle (1.7pt); \fill (0.84,-9) circle (1.7pt); \fill (1.24,-9) circle (1.7pt); \fill (1.625,-9) circle (1.7pt); \fill (1.92,-9) circle (1.7pt); \fill (2.498,-9) circle (1.7pt); \fill (3.0,-9) circle (1.7pt);
\node[tick, anchor=east] at (-0.08,-10) {$n=10$};
\draw[faint] (0,-10) -- (3.1,-10);
\fill (0.023,-10) circle (1.7pt); \fill (0.158,-10) circle (1.7pt); \fill (0.387,-10) circle (1.7pt); \fill (0.689,-10) circle (1.7pt); \fill (1.034,-10) circle (1.7pt); \fill (1.389,-10) circle (1.7pt); \fill (1.711,-10) circle (1.7pt); \fill (1.944,-10) circle (1.7pt); \fill (2.5,-10) circle (1.7pt); \fill (3.0,-10) circle (1.7pt);
\node[tick, anchor=east] at (-0.08,-11) {$n=11$};
\draw[faint] (0,-11) -- (3.1,-11);
\fill (0.018,-11) circle (1.7pt); \fill (0.129,-11) circle (1.7pt); \fill (0.319,-11) circle (1.7pt); \fill (0.573,-11) circle (1.7pt); \fill (0.872,-11) circle (1.7pt); \fill (1.192,-11) circle (1.7pt); \fill (1.503,-11) circle (1.7pt); \fill (1.773,-11) circle (1.7pt); \fill (1.959,-11) circle (1.7pt); \fill (2.5,-11) circle (1.7pt); \fill (3.0,-11) circle (1.7pt);
\node[tick, anchor=east] at (-0.08,-12) {$n=12$};
\draw[faint] (0,-12) -- (3.1,-12);
\fill (0.013,-12) circle (1.7pt); \fill (0.106,-12) circle (1.7pt); \fill (0.267,-12) circle (1.7pt); \fill (0.484,-12) circle (1.7pt); \fill (0.744,-12) circle (1.7pt); \fill (1.029,-12) circle (1.7pt); \fill (1.318,-12) circle (1.7pt); \fill (1.591,-12) circle (1.7pt); \fill (1.819,-12) circle (1.7pt); \fill (1.97,-12) circle (1.7pt); \fill (2.5,-12) circle (1.7pt); \fill (3.0,-12) circle (1.7pt);
\fill[accentLight] (0,-13.6) rectangle (2,-13.2); \draw[accent] (2.5,-13.7) -- (2.5,-13.1); \draw[accent] (3,-13.7) -- (3,-13.1);
\foreach \x in {0,1,2,2.5,3} {\node[tick, below] at (\x,-13.7) {$\x$};}
\end{tikzpicture}
\end{center}
```

Ritz values (dots) of @exm-ritz-values for $n=1,\dots,12$ (one row per $n$, top to bottom), above the spectrum (ticks: the interval $[0,2]$ and the outliers $2.5$, $3$). The outliers are captured within a few steps; the dense part of the spectrum converges slowly, from its ends inward.

:::

::: {#rmk-arnoldi-iteration-1 .remark name="Cost"}

Step $n$ costs one matrix–vector product plus $\sim4mn$ flops of orthogonalisation, and $Q_n$ must be stored: after $n$ steps the work is $O(n^2m)$ beyond the products and the storage $O(nm)$. This growth is what restarting addresses (@sec-math-numerical-krylov-methods-lanczos-and-restarting). Arnoldi is the basis of GMRES for linear systems and of the standard sparse eigensolvers.

:::
