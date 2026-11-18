<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit1801f06-4-q5" status="draft"}
Divide $[0,1]$ into $n$ pieces of width $\frac1n$. Since $e^x$ is increasing, its smallest value on $[\frac{i}n,\frac{i+1}n]$ is at the left end, so the lower sum is
$$\sum_{i=0}^{n-1}e^{i/n}\cdot\frac1n=\frac1n\sum_{i=0}^{n-1}\big(e^{1/n}\big)^i=\frac1n\cdot\frac{e-1}{e^{1/n}-1}=\frac{e-1}{n(e^{1/n}-1)},$$
by the geometric sum with ratio $e^{1/n}$ (and $(e^{1/n})^n=e$).

With $h=1/n$, $n(e^{1/n}-1)=\frac{e^h-1}h\to1$ as $h\to0$ (this is $e^h\approx1+h$, or the definition of $e$, @def-number-e). So the lower sums tend to $e-1$, and $\int_0^1e^x\,dx=e-1$.
:::
