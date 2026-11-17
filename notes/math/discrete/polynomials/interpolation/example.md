<!-- Adapted (own wording) from UC Berkeley CS 70, Fall 2020, Notes 8 and 9 (source keys cs70-8, cs70-9, in note.md). -->

::: {#exm-lagrange-three-points .example name="A parabola through three points" level="easy"}
Find the polynomial of degree at most $2$ through $(1,1)$, $(2,2)$, $(3,4)$. The basis polynomials are
$$\Delta_1=\frac{(x-2)(x-3)}{2},\qquad \Delta_2=-(x-1)(x-3),\qquad \Delta_3=\frac{(x-1)(x-2)}{2},$$
so $p=1\cdot\Delta_1+2\cdot\Delta_2+4\cdot\Delta_3=\frac12x^2-\frac12x+1$. Check: $p(1)=1$, $p(2)=2$, $p(3)=4$.
:::

::: {#fig-interpolation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.4cm,y=0.7cm]
\draw[->, muted] (0,0) -- (4.1,0) node[lab, right] {$x$};
\draw[->, muted] (0,-1.6) -- (0,5.2);
\foreach \x in {1,2,3} \node[tick, below] at (\x,0) {$\x$};
\draw[primary, dashed, domain=0.3:3.6, samples=60] plot (\x,{(\x-2)*(\x-3)/2}) node[lab, right] {$\Delta_1$};
\draw[secondary, dashed, domain=0.6:3.4, samples=60] plot (\x,{-(\x-1)*(\x-3)}) node[lab, right] {$\Delta_2$};
\draw[muted, dashed, domain=0.4:3.6, samples=60] plot (\x,{(\x-1)*(\x-2)/2}) node[lab, right] {$\Delta_3$};
\draw[emph, accent, domain=0.2:3.7, samples=60] plot (\x,{0.5*\x*\x-0.5*\x+1}) node[lab, above] {$p$};
\foreach \x/\y in {1/1,2/2,3/4} \fill[ink] (\x,\y) circle[pt];
\end{tikzpicture}
\end{center}
```

The basis polynomials of @exm-lagrange-three-points (dashed): $\Delta_i$ is $1$ at $x=i$ and $0$ at the other two points. The combination $p=\Delta_1+2\Delta_2+4\Delta_3$ passes through all three points.

:::

::: {#exm-interpolation-by-equations .example name="The same task by linear equations" level="easy"}
For $(-1,2)$, $(0,1)$, $(2,5)$ and $p(x)=a_2x^2+a_1x+a_0$: the conditions are $a_2-a_1+a_0=2$, $a_0=1$ and $4a_2+2a_1+a_0=5$. Then $a_2-a_1=1$ and $2a_2+a_1=2$, so $a_2=1$, $a_1=0$, and $p(x)=x^2+1$.
:::
