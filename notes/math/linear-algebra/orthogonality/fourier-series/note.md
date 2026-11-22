---
title: "Fourier Series as Orthogonal Expansion"
sources: [mit1806-24]
requires: [math/linear-algebra/orthogonality/orthonormal-bases-and-gram-schmidt]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 24 (second half), in our own wording; proofs written out in steps. -->

Projection onto orthogonal vectors works in any space with a dot product, including spaces of functions.

::: {#def-function-inner-product .definition name="Inner product of functions"}

For real functions on $[0,2\pi]$ define
$$\langle f,g\rangle=\int_0^{2\pi}f(x)\,g(x)\,dx,\qquad \lVert f\rVert^2=\langle f,f\rangle.$$
$f$ and $g$ are *orthogonal* when $\langle f,g\rangle=0$. This is the dot product of @def-dot-product with the sum replaced by an integral.

:::

::: {#prp-trigonometric-orthogonality .proposition name="Sines and cosines are orthogonal"}

The functions $1,\cos x,\sin x,\cos2x,\sin2x,\dots$ are pairwise orthogonal on $[0,2\pi]$, with
$$\lVert1\rVert^2=2\pi,\qquad \lVert\cos kx\rVert^2=\lVert\sin kx\rVert^2=\pi\quad(k\ge1).$$

:::

::: {.proof}

1. Product formulas turn every product into a sum, e.g. $\cos jx\cos kx=\frac12\big(\cos(j-k)x+\cos(j+k)x\big)$, and similarly for $\sin\cdot\sin$ and $\sin\cdot\cos$.

2. $\int_0^{2\pi}\cos mx\,dx=\int_0^{2\pi}\sin mx\,dx=0$ for every integer $m\neq0$, since the integral covers whole periods.

3. So every product of two different functions in the list integrates to $0$. For $j=k\ge1$ the term $\frac12\cos0=\frac12$ remains and integrates to $\pi$; for the constant, $\int_0^{2\pi}1\,dx=2\pi$.

:::

::: {#fig-fourier-series-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[y={(0,0.9cm)}]
\draw[->, muted] (0,0) -- (6.7,0) node[right, lab, tick] {$x$}; \draw[->, muted] (0,-1.3) -- (0,1.3);
\fill[tintA, domain=0:3.1416, samples=60] plot (\x, {sin(\x r)*sin(2*\x r)}) -- cycle;
\fill[tintB, domain=3.1416:6.2832, samples=60] (3.1416,0) -- plot (\x, {sin(\x r)*sin(2*\x r)}) -- cycle;
\draw[faint, domain=0:6.2832, samples=60] plot (\x, {sin(\x r)});
\draw[faint, dashed, domain=0:6.2832, samples=60] plot (\x, {sin(2*\x r)});
\draw[emph, ink, domain=0:6.2832, samples=100] plot (\x, {sin(\x r)*sin(2*\x r)});
\node[lab, tick] at (3.14,-0.25) {$\pi$}; \node[lab, tick] at (6.28,-0.25) {$2\pi$};
\node[lab, note, anchor=west] at (6.5,0.8) {$\sin x\,\sin2x$: the shaded areas cancel};
\end{tikzpicture}
\end{center}
```

Why $\sin x$ and $\sin 2x$ are orthogonal: their product (dark curve) has as much area above the axis as below over a full period, so $\int_0^{2\pi}\sin x\sin2x\,dx=0$. The faint curves are the two factors.

:::

::: {#thm-fourier-coefficients .theorem name="Fourier coefficients are projections"}

If $f(x)=a_0+\sum_{k\ge1}(a_k\cos kx+b_k\sin kx)$ (with the series converging suitably), then
$$a_0=\frac1{2\pi}\int_0^{2\pi}f(x)\,dx,\qquad a_k=\frac1\pi\int_0^{2\pi}f(x)\cos kx\,dx,\qquad b_k=\frac1\pi\int_0^{2\pi}f(x)\sin kx\,dx.$$

:::

::: {.proof}

1. Take the inner product of both sides with $\cos kx$ (integrate term by term).

2. By @prp-trigonometric-orthogonality every term on the right vanishes except $a_k\lVert\cos kx\rVert^2=\pi a_k$. This gives $a_k$.

3. The same argument with $\sin kx$ and with $1$ gives $b_k$ and $a_0$.

:::

::: {#fig-fourier-series-4}

```{=latex}
\begin{center}
\begin{tikzpicture}[y={(0,0.9cm)}]
\draw[->, muted] (0,0) -- (6.7,0) node[right, lab, tick] {$x$}; \draw[->, muted] (0,-1.5) -- (0,1.6);
\draw[bold, ink] (0,1) -- (3.1416,1); \draw[bold, ink] (3.1416,-1) -- (6.2832,-1); \draw[faint, dashed] (3.1416,1) -- (3.1416,-1);
\draw[emph, accent, domain=0:6.2832, samples=80] plot (\x, {4/pi*sin(\x r)});
\node[lab, note] at (1.2,1.3) {$f$}; \node[lab, note, accent, anchor=west] at (6.5,-0.9) {$b_1\sin x$, $b_1=\frac{\langle f,\sin x\rangle}{\langle\sin x,\sin x\rangle}=\frac4\pi$};
\end{tikzpicture}
\end{center}
```

The first Fourier term is the projection of the square wave $f$ onto the line through $\sin x$: the multiple $b_1\sin x$ closest to $f$ in the norm of @def-function-inner-product. The remaining error $f-b_1\sin x$ is orthogonal to $\sin x$.

:::

Each coefficient is the projection formula $\mathbf{a}^{\mathsf T}\mathbf{b}/\mathbf{a}^{\mathsf T}\mathbf{a}$ of @thm-projection-onto-line, with $\mathbf{a}$ a basis function and $\mathbf{b}=f$. Because the basis is orthogonal, the coefficients can be computed one at a time, as with $Q^{\mathsf T}\mathbf{b}$ in @prp-projection-with-orthonormal-columns.

::: {#exm-fourier-square-wave .example name="A square wave"}

Let $f(x)=1$ on $(0,\pi)$ and $f(x)=-1$ on $(\pi,2\pi)$. Then $a_0=0$ and $a_k=0$, and
$$b_k=\frac1\pi\Big(\int_0^\pi\sin kx\,dx-\int_\pi^{2\pi}\sin kx\,dx\Big)=\frac{2(1-\cos k\pi)}{k\pi}=\begin{cases}\frac4{k\pi}&k\text{ odd},\\0&k\text{ even}.\end{cases}$$
So $f(x)=\frac4\pi\big(\sin x+\frac13\sin3x+\frac15\sin5x+\cdots\big)$.

:::

::: {#fig-fourier-series-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[y={(0,1cm)}]
\draw[->, muted] (0,0) -- (5.3,0) node[right, lab, tick] {$k$}; \draw[->, muted] (0,0) -- (0,1.6) node[above, lab, tick] {$b_k$};
\draw[bar] (0.35,0) rectangle (0.65,1.273);
\node[lab, tick] at (0.50,-0.2) {1};
\node[lab, tick] at (1.00,-0.2) {2};
\draw[bar] (1.35,0) rectangle (1.65,0.424);
\node[lab, tick] at (1.50,-0.2) {3};
\node[lab, tick] at (2.00,-0.2) {4};
\draw[bar] (2.35,0) rectangle (2.65,0.255);
\node[lab, tick] at (2.50,-0.2) {5};
\node[lab, tick] at (3.00,-0.2) {6};
\draw[bar] (3.35,0) rectangle (3.65,0.182);
\node[lab, tick] at (3.50,-0.2) {7};
\node[lab, tick] at (4.00,-0.2) {8};
\draw[bar] (4.35,0) rectangle (4.65,0.141);
\node[lab, tick] at (4.50,-0.2) {9};
\node[lab, note, anchor=west] at (1.0,1.27) {$\frac{4}{\pi}\approx1.27$}; \node[lab, note, anchor=west] at (2.0,0.55) {$\frac4{3\pi}$};
\node[lab, note, anchor=west] at (5.4,0.8) {even $k$: $b_k=0$};
\end{tikzpicture}
\end{center}
```

The sine coefficients $b_k=\frac{4}{k\pi}$ ($k$ odd) of the square wave. They decay only like $1/k$, which is why the partial sums converge slowly near the jumps.

:::

::: {#fig-fourier-series-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.100,0) -- (3.856,0) node[lab, right] {$x$};
\draw[->, faint] (0,-1.260) -- (0,1.350) node[lab, above] {};
\draw[emph] (0,0.900) -- (1.728,0.900) -- (1.728,-0.900) -- (3.456,-0.900);
\draw[hl] (0.000,0.000) -- (0.029,0.179) -- (0.058,0.352) -- (0.086,0.515) -- (0.115,0.661) -- (0.144,0.788) -- (0.173,0.892) -- (0.202,0.972) -- (0.230,1.028) -- (0.259,1.060) -- (0.288,1.070) -- (0.317,1.061) -- (0.346,1.037) -- (0.374,1.002) -- (0.403,0.961) -- (0.432,0.918) -- (0.461,0.878) -- (0.490,0.843) -- (0.518,0.816) -- (0.547,0.799) -- (0.576,0.794) -- (0.605,0.799) -- (0.634,0.814) -- (0.662,0.837) -- (0.691,0.865) -- (0.720,0.896) -- (0.749,0.926) -- (0.778,0.954) -- (0.806,0.975) -- (0.835,0.988) -- (0.864,0.993) -- (0.893,0.988) -- (0.922,0.975) -- (0.950,0.954) -- (0.979,0.926) -- (1.008,0.896) -- (1.037,0.865) -- (1.066,0.837) -- (1.094,0.814) -- (1.123,0.799) -- (1.152,0.794) -- (1.181,0.799) -- (1.210,0.816) -- (1.238,0.843) -- (1.267,0.878) -- (1.296,0.918) -- (1.325,0.961) -- (1.354,1.002) -- (1.382,1.037) -- (1.411,1.061) -- (1.440,1.070) -- (1.469,1.060) -- (1.497,1.028) -- (1.526,0.972) -- (1.555,0.892) -- (1.584,0.788) -- (1.613,0.661) -- (1.641,0.515) -- (1.670,0.352) -- (1.699,0.179) -- (1.728,0.000) -- (1.757,-0.179) -- (1.785,-0.352) -- (1.814,-0.515) -- (1.843,-0.661) -- (1.872,-0.788) -- (1.901,-0.892) -- (1.929,-0.972) -- (1.958,-1.028) -- (1.987,-1.060) -- (2.016,-1.070) -- (2.045,-1.061) -- (2.073,-1.037) -- (2.102,-1.002) -- (2.131,-0.961) -- (2.160,-0.918) -- (2.189,-0.878) -- (2.217,-0.843) -- (2.246,-0.816) -- (2.275,-0.799) -- (2.304,-0.794) -- (2.333,-0.799) -- (2.361,-0.814) -- (2.390,-0.837) -- (2.419,-0.865) -- (2.448,-0.896) -- (2.477,-0.926) -- (2.505,-0.954) -- (2.534,-0.975) -- (2.563,-0.988) -- (2.592,-0.993) -- (2.621,-0.988) -- (2.649,-0.975) -- (2.678,-0.954) -- (2.707,-0.926) -- (2.736,-0.896) -- (2.765,-0.865) -- (2.793,-0.837) -- (2.822,-0.814) -- (2.851,-0.799) -- (2.880,-0.794) -- (2.909,-0.799) -- (2.937,-0.816) -- (2.966,-0.843) -- (2.995,-0.878) -- (3.024,-0.918) -- (3.053,-0.961) -- (3.081,-1.002) -- (3.110,-1.037) -- (3.139,-1.061) -- (3.168,-1.070) -- (3.197,-1.060) -- (3.225,-1.028) -- (3.254,-0.972) -- (3.283,-0.892) -- (3.312,-0.788) -- (3.341,-0.661) -- (3.369,-0.515) -- (3.398,-0.352) -- (3.427,-0.179) -- (3.456,-0.000);
\node[lab, tick, below] at (1.728,0) {$\pi$};
\node[lab, tick, below] at (3.456,0) {$2\pi$};
\end{tikzpicture}
\end{center}
```

The square wave and the sum of its first three nonzero Fourier terms, $\frac4\pi(\sin x+\frac13\sin3x+\frac15\sin5x)$.

:::

::: {#rmk-fourier-series-1 .remark name="Infinite-dimensional space"}

The space of functions with $\lVert f\rVert^2<\infty$ is infinite-dimensional; the Fourier basis plays the role of the orthonormal columns of $Q$. The discrete version, with sums over $n$ sample points, is the Fourier matrix of @sec-math-linear-algebra-eigenvalues-complex-matrices.

:::
