---
title: "Least Squares Fitting by Calculus"
sources: [mit1802-9, mit1802n-LS]
requires: [math/calculus/multivariable/differentiation/critical-points]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 9 and Supplementary Notes LS, in our own wording. The same equations from the linear-algebra side are in math/linear-algebra/orthogonality/least-squares (related, not merged). -->

Given data points $(x_1,y_1),\dots,(x_n,y_n)$, we look for the line $y=ax+b$ that fits them best. The unknowns are $a$ and $b$, not $x$ and $y$.

::: {#thm-least-squares-line-calculus .theorem name="The least-squares line" related="thm-least-squares-normal-equations"}

The total square deviation
$$D(a,b)=\sum_{i=1}^n\big(y_i-(ax_i+b)\big)^2$$
is smallest when $a,b$ solve
$$\Big(\sum x_i^2\Big)a+\Big(\sum x_i\Big)b=\sum x_iy_i,\qquad\Big(\sum x_i\Big)a+nb=\sum y_i .$$
When the $x_i$ are not all equal this system has exactly one solution.

:::

::: {.proof}

1. At a minimum, $D_a=D_b=0$ (@prp-local-extremum-critical). Differentiating term by term,
$$D_a=-2\sum x_i\big(y_i-ax_i-b\big),\qquad D_b=-2\sum\big(y_i-ax_i-b\big).$$
Setting both to $0$ and rearranging gives the two equations.

2. The determinant of the system is $n\sum x_i^2-\big(\sum x_i\big)^2=\sum_{i<j}(x_i-x_j)^2$, which is positive unless all $x_i$ are equal; so there is exactly one critical point.

3. $D_{aa}=2\sum x_i^2$, $D_{ab}=2\sum x_i$, $D_{bb}=2n$, so $D_{aa}D_{bb}-D_{ab}^2=4\big(n\sum x_i^2-(\sum x_i)^2\big)>0$ and $D_{aa}>0$. As $D$ is a quadratic function of $(a,b)$, @thm-quadratic-form-two-variables shows that the critical point is the global minimum.

:::

::: {#exm-least-squares-line-calculus .example name="Three points"}

For $(0,1),(1,1),(2,3)$: $\sum x_i=3$, $\sum x_i^2=5$, $\sum y_i=5$, $\sum x_iy_i=7$. The equations $5a+3b=7$, $3a+3b=5$ give $a=1$, $b=\frac23$: the best line is $y=x+\frac23$.

:::

::: {#fig-least-squares-fitting-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.3]
\draw[->] (-0.4,0) -- (2.7,0) node[lab, right] {$x$};
\draw[->] (0,-0.2) -- (0,3.6) node[lab, above] {$y$};
\foreach \x in {1,2} \draw (\x,0.06) -- (\x,-0.06) node[tick, below] {$\x$};
\foreach \y in {1,2,3} \draw (0.06,\y) -- (-0.06,\y) node[tick, left] {$\y$};
\draw[emph, primary] (-0.3,0.367) -- (2.6,3.267) node[lab, right] {$y=x+\frac23$};
\draw[hl] (0,1) -- (0,0.667);
\draw[hl] (1,1) -- (1,1.667);
\draw[hl] (2,3) -- (2,2.667);
\foreach \p in {(0,1),(1,1),(2,3)} \fill[ink] \p circle[pt];
\end{tikzpicture}
\end{center}
```

The least-squares line of @exm-least-squares-line-calculus. $D(a,b)$ is the sum of the squares of the vertical deviations (highlighted) between the data points and the line $y=ax+b$; the line $y=x+\frac23$ makes it smallest.

:::

::: {#rmk-least-squares-fitting-1 .remark name="Other laws"}

- An exponential law $y=ce^{ax}$ becomes linear after taking logarithms: $\ln y=ax+b$ with $b=\ln c$. Fit a line to the points $(x_i,\ln y_i)$. (This minimises the deviations of $\ln y$, not of $y$.) Moore's law, the exponential growth of the number of transistors on a chip, is found this way, as a straight line on a log plot.
- A quadratic law $y=ax^2+bx+c$ is fitted in the same way; setting the three partial derivatives of $D(a,b,c)$ to zero gives a $3\times3$ linear system.

:::
