---
title: "Numerical Integration"
sources: [mit1801-24]
requires: [math/calculus/integrals/fundamental-theorem]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 24, in our own wording. Numbers checked in Python. -->

Split $[a,b]$ into $n$ pieces of width $\Delta x=(b-a)/n$ with $y_i=f(a+i\Delta x)$.

::: {#def-numerical-rules .definition name="Riemann, trapezoidal and Simpson's rules"}

$$\begin{aligned}
\text{left Riemann sum:}&\quad \Delta x\,(y_0+y_1+\dots+y_{n-1}),\\
\text{trapezoidal rule:}&\quad \Delta x\,\Big(\tfrac12y_0+y_1+\dots+y_{n-1}+\tfrac12y_n\Big),\\
\text{Simpson's rule ($n$ even):}&\quad \frac{\Delta x}3\,\big(y_0+4y_1+2y_2+4y_3+\dots+2y_{n-2}+4y_{n-1}+y_n\big).
\end{aligned}$$

:::

The trapezoidal rule replaces $f$ on each piece by the chord; Simpson's rule replaces it on each pair of pieces by the parabola through three points.

::: {#thm-simpson-parabola .theorem name="Area under a parabola"}

If $y=Ax^2+Bx+C$ passes through $(-h,y_0)$, $(0,y_1)$, $(h,y_2)$, then
$$\int_{-h}^hy\,dx=\frac h3\,(y_0+4y_1+y_2).$$

:::

::: {.proof}

1. $\int_{-h}^h(Ax^2+Bx+C)\,dx=\tfrac23Ah^3+2Ch$, since the odd term integrates to $0$.

2. $y_1=C$ and $y_0+y_2=2Ah^2+2C$, so $2Ah^2=y_0+y_2-2y_1$.

3. Then $\tfrac23Ah^3+2Ch=\tfrac h3\big(2Ah^2+6C\big)=\tfrac h3\big(y_0+y_2-2y_1+6y_1\big)=\tfrac h3(y_0+4y_1+y_2)$.

:::

::: {#fig-numerical-integration-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-2.1,0) -- (2.2,0) node[lab, right] {$x$};
\fill[shade, domain=-1.5:1.5, samples=40] (-1.5,0) -- plot (\x,{-0.36*\x*\x+0.13*\x+2.2}) -- (1.5,0) -- cycle;
\draw[emph, domain=-1.8:1.8, samples=50] plot (\x,{-0.36*\x*\x+0.13*\x+2.2});
\draw[faint, dashed] (-1.5,0) -- (-1.5,1.2);
\fill (-1.5,1.2) circle (1.5pt);
\node[lab, below] at (-1.5,0) {$-h$};
\draw[faint, dashed] (0.0,0) -- (0.0,2.2);
\fill (0.0,2.2) circle (1.5pt);
\node[lab, below] at (0.0,0) {$0$};
\draw[faint, dashed] (1.5,0) -- (1.5,1.6);
\fill (1.5,1.6) circle (1.5pt);
\node[lab, below] at (1.5,0) {$h$};
\node[lab, above] at (-1.5,1.25) {$y_0$};
\node[lab, above] at (0,2.25) {$y_1$};
\node[lab, above] at (1.5,1.65) {$y_2$};
\end{tikzpicture}
\end{center}
```

Simpson's rule replaces $f$ on $[-h,h]$ by the parabola through three points; the shaded area is exactly $\frac h3(y_0+4y_1+y_2)$.

:::

::: {#exm-numerical-ln2 .example name="Estimating $\ln2$"}

For $\int_1^2\frac{dx}x=\ln2=0.693147\ldots$ with $n=2$ ($\Delta x=\tfrac12$, $y=1,\tfrac23,\tfrac12$): the trapezoidal rule gives $\tfrac12\big(\tfrac12+\tfrac23+\tfrac14\big)=0.708333$, and Simpson's rule gives $\tfrac16\big(1+\tfrac83+\tfrac12\big)=0.694444$.

:::

::: {#rmk-numerical-integration-errors .remark name="How fast the errors shrink"}

For smooth $f$, halving $\Delta x$ roughly halves the error of a Riemann sum, divides that of the trapezoidal rule by $4$ (error about $C(\Delta x)^2$) and that of Simpson's rule by $16$ (about $C(\Delta x)^4$). Simpson's rule is exact for cubics.

:::
