---
title: "The Definite Integral and Riemann Sums"
sources: [mit1801-18, mit1801n-PI]
requires: [math/calculus/limits/continuity, math/discrete/sequences/sums-and-series]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 18 and Supplementary Notes PI, in our own wording. Numbers checked in Python. -->

::: {#def-riemann-sum .definition name="Riemann sum, definite integral"}

Divide $[a,b]$ into $n$ pieces of width $\Delta x=(b-a)/n$ with points $x_i=a+i\Delta x$, and pick $c_i\in[x_{i-1},x_i]$. The Riemann sum is
$$\sum_{i=1}^n f(c_i)\,\Delta x .$$
If these sums tend to the same limit as $n\to\infty$ for every choice of the $c_i$, the limit is the definite integral
$$\int_a^b f(x)\,dx=\lim_{n\to\infty}\sum_{i=1}^n f(c_i)\,\Delta x .$$

:::

::: {#fig-definite-integral-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (2.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,3.2) node[lab, above] {$y$};
\draw[shade] (0.0,0) rectangle (0.33,0.0);
\draw[shade] (0.33,0) rectangle (0.67,0.08);
\draw[shade] (0.67,0) rectangle (1.0,0.31);
\draw[shade] (1.0,0) rectangle (1.33,0.7);
\draw[shade] (1.33,0) rectangle (1.67,1.24);
\draw[shade] (1.67,0) rectangle (2.00,1.94);
\draw[emph, domain=0:2.15, samples=50] plot (\x,{0.7*\x*\x});
\node[lab, below] at (2,0) {$b$};
\end{tikzpicture}
\end{center}
```

The lower Riemann sum of $x^2$ on $[0,b]$ with $n=6$: the rectangles lie under the graph, and their total area tends to $b^3/3$ as $n\to\infty$.

:::

Choosing $c_i$ to be where $f$ is smallest (largest) on each piece gives the lower (upper) sum; for $f\ge0$ these are areas of rectangles below (above) the graph. Every continuous function on $[a,b]$ is integrable (we use this without proof). For $f\ge0$ the integral is the area under the graph; in general it counts area below the axis as negative.

::: {#exm-integral-of-square .example name="Area under $x^2$"}

On $[0,b]$ with right endpoints $c_i=ib/n$:
$$\sum_{i=1}^n\Big(\frac{ib}{n}\Big)^2\frac bn=\frac{b^3}{n^3}\sum_{i=1}^n i^2=\frac{b^3}{n^3}\cdot\frac{n(n+1)(2n+1)}6\to\frac{b^3}3 .$$
So $\int_0^bx^2\,dx=b^3/3$, a third of the enclosing rectangle $b\times b^2$.

:::

::: {#exm-integral-of-identity-riemann .example name="Area under $x$"}

On $[0,b]$ with right endpoints, $\sum_{i=1}^n\frac{ib}{n}\cdot\frac bn=\frac{b^2}{n^2}\cdot\frac{n(n+1)}2\to\frac{b^2}2$, the area of the triangle under $y=x$.

:::

::: {#prp-integral-properties .proposition name="Properties of the integral"}

For integrable $f,g$ and constants $c$:

1. $\int_a^b(f+g)=\int_a^bf+\int_a^bg$ and $\int_a^bcf=c\int_a^bf$;
2. $\int_a^bf+\int_b^cf=\int_a^cf$, with the convention $\int_b^af=-\int_a^bf$ and $\int_a^af=0$;
3. if $f\le g$ on $[a,b]$ ($a<b$), then $\int_a^bf\le\int_a^bg$.

:::

Each holds for the Riemann sums and so for their limits.

::: {#exm-integral-accumulation .example name="Integrals beyond area"}

Money borrowed continuously at a rate $f(t)$ dollars per year, for $0\le t\le T$, adds up to $\int_0^Tf(t)\,dt$; if interest is charged continuously at rate $r$, the amount owed at $T$ is $\int_0^Tf(t)e^{r(T-t)}dt$. Any quantity built up from small pieces $f(c_i)\Delta x$ is an integral.

:::
