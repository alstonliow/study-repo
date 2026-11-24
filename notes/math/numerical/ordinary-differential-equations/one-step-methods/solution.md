<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-3-q1" status="draft"}
**(a)** The solution is $y=x^2$, so $y(1)=1$. With step $h=1/n$ and $x_k=k/n$, Euler's method gives $y_{k+1} = y_k + h\cdot2x_k$, so
$$y_n = \sum_{k=0}^{n-1}\frac{2k}{n}\cdot\frac1n = \frac{2}{n^2}\cdot\frac{n(n-1)}{2} = \frac{n-1}{n}.$$
Two steps give $\tfrac12$, three steps $\tfrac23$. As $n\to\infty$, $(n-1)/n\to1=y(1)$: yes.

**(b)** $y(1) - y_n = 1-\dfrac{n-1}{n} = \dfrac1n = h$: the error is exactly proportional to $h$, as predicted for a first-order method (@prp-euler-midpoint-order).
:::
