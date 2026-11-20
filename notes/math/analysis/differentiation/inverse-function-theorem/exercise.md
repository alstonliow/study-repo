::: {.problem #prob-camib-ats-4-q12 origin="external" source="camib-ats-4-q12"}
Define $f : M_n \to M_n$ by $f(A) = A^2$.

(a) Show that $f$ is continuously differentiable on the whole of $M_n$.

(b) Deduce that there is a continuous square root function on some neighbourhood of the identity $\mathrm{Id}$; that is, show that there is an open ball $B_\varepsilon(\mathrm{Id})$ for some $\varepsilon > 0$ and a continuous function $g : B_\varepsilon(\mathrm{Id}) \to M_n$ such that $g(A)^2 = A$ for all $A \in B_\varepsilon(\mathrm{Id})$.

(c) Is it possible to define a continuous square-root function on the whole of $M_n$?
:::

::: {.problem #prob-camib-ats-4-q16 origin="external" source="camib-ats-4-q16"}
Let $f : U \to \mathbb{R}^m$, where $U \subset \mathbb{R}^{n+m}$ open, be a continuously differentiable function. (By convention, we use the notation $x \in \mathbb{R}^n$ and $y \in \mathbb{R}^m$.) Let $x_0 \in \mathbb{R}^n$ and $y_0 \in \mathbb{R}^m$ be such that $(x_0,y_0) \in U$. Suppose $f(x_0,y_0) = 0$ and that
$$J_yf|_{(x_0,y_0)} := \det\left(\left[\frac{\partial f^j}{\partial y^i}\right]_{i,j=0}^m\right) \neq 0$$

(a) Let $F(x,y) = (x, f(x,y))$. Show that $F$ is locally invertible around the point $(x_0,0)$.

(b) Let $G = (G^1, \dots, G^{n+m})$ denote the local inverse of $f$. Show that, for points $(X,0)$, $X \in \mathbb{R}^n$, in the domain of $G$, one has $f(X, G^n(X,0), \dots G^{n+m}(X,0)) = 0$.

(c) Deduce that there exists an open neighborhood $W' \subset \mathbb{R}^n$ of $x_0$ and an open neighborhood $W'' \subset \mathbb{R}^m$ of $y_0$ satisfying $W' \times W'' \subset U$, and a unique map $g : W' \to W''$ such that
$$\begin{cases} g(x_0) = y_0 \\ f(x,g(x)) = 0 \end{cases}.$$
We call $g$ the *implicit* function defined by the zero set of $f$.

(d) Show that $g$ is differentiable and compute its derivative.

(e) As an application, show that the level set $C = \{(x,y) \in \mathbb{R}^2 : x^3 + y^3 - 3yx = 0\}$ is locally graphical, except in small neighborhoods of $(0,0)$ and $(2^{\frac23}, 2^{\frac13})$.

*Note (these notes):* The printed statement has small typos, read here as intended: the index range in $J_y f$ is $i,j = 1,\dots,m$; in (a), $F$ is inverted near $(x_0,y_0)$, with image near $(x_0,0)$; in (b), $G$ is the local inverse of $F$ and the last $m$ components are $G^{n+1},\dots,G^{n+m}$.
:::
