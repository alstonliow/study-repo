<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-counting-11" status="draft"}
Let
$$X = \{(x_1,\dots,x_n)\in\mathbb Z^n : x_i\ge 0,\ x_1+\cdots+x_n = r\},$$
$$Y = \{(y_1,\dots,y_n)\in\mathbb Z^n : y_i\ge 1,\ y_1+\cdots+y_n = r+n\}.$$

Define $f : X\to Y$ by
$$f(x_1,\dots,x_n) = (x_1+1,\dots,x_n+1).$$

1. *$f$ maps into $Y$.* Each $x_i+1\ge1$, and
   $\sum(x_i+1) = r+n$.

2. *Inverse.* Define $g : Y\to X$ by $g(y_1,\dots,y_n) = (y_1-1,\dots,y_n-1)$.
   Each $y_i-1\ge0$ and $\sum(y_i-1) = r$, so $g$ maps into $X$.

3. $g(f(x)) = x$ and $f(g(y)) = y$, so $f$ is a bijection with inverse $g$.
:::
