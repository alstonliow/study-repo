---
title: "The Mean Value Theorem and Inequalities"
sources: [mit1801-14, mit1801n-MVT]
requires: [math/calculus/single-variable/applications-of-derivatives/optimization]
aliases: [math/calculus/applications-of-derivatives/mean-value-theorem]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 14 and Supplementary Notes MVT, in our own wording; proofs written out in steps. -->

::: {#thm-rolle .theorem name="Rolle's theorem"}

If $f$ is continuous on $[a,b]$, differentiable on $(a,b)$, and $f(a)=f(b)$, then $f'(c)=0$ for some $c\in(a,b)$.

:::

::: {.proof}

1. By @thm-extreme-value, $f$ has a maximum and a minimum on $[a,b]$.

2. If both occur at endpoints, they are equal (since $f(a)=f(b)$), so $f$ is constant and $f'=0$ everywhere.

3. Otherwise one of them occurs at an interior point $c$, and $f'(c)=0$ by @thm-closed-interval-method.

:::

::: {#thm-mean-value .theorem name="Mean value theorem"}

If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, then for some $c\in(a,b)$
$$\frac{f(b)-f(a)}{b-a}=f'(c).$$

:::

::: {.proof}

1. Subtract the secant line: $g(x)=f(x)-\Big(f(a)+\dfrac{f(b)-f(a)}{b-a}(x-a)\Big)$.

2. $g$ is continuous on $[a,b]$, differentiable on $(a,b)$, and $g(a)=g(b)=0$.

3. By @thm-rolle, $g'(c)=0$ for some $c$, i.e. $f'(c)=\dfrac{f(b)-f(a)}{b-a}$.

:::

::: {#fig-mean-value-theorem-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (3.7,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,3.0) node[lab, above] {$y$};
\draw[emph, domain=0:3.5, samples=60] plot (\x,{1.4*sqrt(\x)});
\draw[faint] (0.25,0.7) -- (3.25,2.52);
\fill (0.25,0.7) circle (1.3pt) node[lab, above left] {$a$};
\fill (3.25,2.52) circle (1.3pt) node[lab, below right] {$b$};
\draw[hl] (0.13,0.88) -- (2.53,2.34);
\fill (1.33,1.61) circle (1.5pt) node[lab, above left] {$c$};
\draw[faint, dashed] (1.33,0) -- (1.33,1.61);
\end{tikzpicture}
\end{center}
```

Mean value theorem: at some $c$ between $a$ and $b$ the tangent is parallel to the secant through the endpoints.

:::

In words: at some moment the instantaneous speed equals the average speed. Another form: $f(b)=f(a)+f'(c)(b-a)$, an exact version of the linear approximation.

::: {#cor-sign-of-derivative .corollary name="Consequences"}

On an interval:

1. if $f'>0$ then $f$ is increasing; if $f'<0$ it is decreasing; if $f'\ge0$ it is non-decreasing;
2. if $f'=0$ then $f$ is constant;
3. if $f'=g'$ then $f-g$ is constant.

:::

::: {.proof}

1. For $x_1<x_2$ in the interval, $f(x_2)-f(x_1)=f'(c)(x_2-x_1)$ for some $c$ between them; the sign of the right side is the sign of $f'(c)$.

2. If $f'=0$ the right side is $0$, so $f(x_2)=f(x_1)$.

3. Apply part 2 to $f-g$.

:::

::: {#exm-inequalities-by-mvt .example name="Proving inequalities"}

$e^x\ge1+x$ for all $x$: let $f(x)=e^x-(1+x)$, so $f(0)=0$ and $f'(x)=e^x-1$, which is $\ge0$ for $x\ge0$ and $\le0$ for $x\le0$. By @cor-sign-of-derivative $f$ decreases to $0$ and then increases, so $f\ge0$. Applying the same idea to $f(x)-(1+x+x^2/2)$ for $x\ge0$ gives $e^x\ge1+x+\tfrac{x^2}2$ there, and so on.

:::
