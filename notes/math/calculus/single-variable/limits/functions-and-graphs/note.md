---
title: "Functions and Their Graphs"
sources: [mit1801n-G, mit1801-5]
requires: [math/discrete/functions/inverse-functions]
aliases: [math/calculus/limits/functions-and-graphs]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Supplementary Notes G (Recitation 0) and Lecture 5 (graphs of inverse functions), in our own wording; proofs written out in steps. -->

## Even and odd functions

::: {#def-even-odd-function .definition name="Even and odd functions"}

A function $f$ defined on a set symmetric about $0$ is
$$\text{even if } f(-x)=f(x),\qquad \text{odd if } f(-x)=-f(x)\qquad\text{for all } x .$$

:::

The graph of an even function is symmetric about the $y$-axis; the graph of an odd function is symmetric about the origin. Examples: $x^2$, $\cos x$, $\lvert x\rvert$ are even; $x^3$, $\sin x$, $\tan x$ are odd.

::: {#thm-even-odd-decomposition .theorem name="Even–odd decomposition"}

Every function $f$ on a symmetric domain is, in exactly one way, the sum of an even and an odd function:
$$f(x)=\underbrace{\frac{f(x)+f(-x)}{2}}_{E(x)}+\underbrace{\frac{f(x)-f(-x)}{2}}_{O(x)} .$$

:::

::: {.proof}

1. Replacing $x$ by $-x$ swaps the two terms in $E$, so $E(-x)=E(x)$; it swaps and negates the terms in $O$, so $O(-x)=-O(x)$. Clearly $E+O=f$.

2. Uniqueness: if $f=E_1+O_1=E_2+O_2$, then $g=E_1-E_2=O_2-O_1$ is both even and odd, so $g(x)=g(-x)=-g(x)$ and $g=0$.

:::

::: {#exm-even-odd-exponential .example name="Splitting $e^x$"}

For $f(x)=e^x$ the even part is $\frac{e^x+e^{-x}}2=\cosh x$ and the odd part is $\frac{e^x-e^{-x}}2=\sinh x$; these are the hyperbolic functions of the note on exponentials and logarithms.

:::

## Moving and stretching graphs

::: {#prp-graph-transformations .proposition name="Translations and rescalings"}

Let $a>0$ and $c\neq 0$. Compared with the graph of $y=f(x)$:
$$\begin{aligned}
y&=f(x-a) &&\text{is shifted right by } a, & y&=f(x)+a &&\text{is shifted up by } a,\\
y&=f(x/c) &&\text{is stretched horizontally by } c, & y&=c\,f(x) &&\text{is stretched vertically by } c,
\end{aligned}$$
where a negative $c$ also reflects the graph in the $y$-axis (horizontal case) or the $x$-axis (vertical case).

:::

::: {.proof}

1. The point $(x_0,y_0)$ lies on $y=f(x)$ exactly when $(x_0+a,y_0)$ lies on $y=f(x-a)$, since $f((x_0+a)-a)=y_0$. So every point moves right by $a$.

2. Likewise $(x_0,y_0)$ is on $y=f(x)$ exactly when $(cx_0,y_0)$ is on $y=f(x/c)$; the vertical cases are the same argument applied to $y$.

:::

## Graph of an inverse function

::: {#prp-graph-of-inverse .proposition name="Graph of an inverse"}

If $f$ is one-to-one with inverse $g=f^{-1}$, the graph of $g$ is the reflection of the graph of $f$ in the line $y=x$.

:::

::: {.proof}

1. $(a,b)$ lies on the graph of $f$ $\iff$ $b=f(a)$ $\iff$ $a=g(b)$ $\iff$ $(b,a)$ lies on the graph of $g$.

2. The map $(a,b)\mapsto(b,a)$ is the reflection in $y=x$.

:::

::: {#exm-inverse-of-square .example name="Square root as an inverse"}

On $x\ge0$, $f(x)=x^2$ is increasing and its inverse is $g(y)=\sqrt y$. Reflecting the right half of the parabola in $y=x$ gives the graph of $\sqrt x$. On all of $\mathbb R$, $x^2$ has no inverse, since $f(-1)=f(1)$: the domain must be restricted first.

:::
