<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit1801f06-1-q1" status="draft"}
Let $f(x)=\frac{x-1}{x+1}$, so $f(-x)=\frac{-x-1}{-x+1}=\frac{x+1}{x-1}$. By @thm-even-odd-decomposition the even and odd parts are
$$E(x)=\frac12\Big(\frac{x-1}{x+1}+\frac{x+1}{x-1}\Big)=\frac{(x-1)^2+(x+1)^2}{2(x^2-1)}=\frac{x^2+1}{x^2-1},$$
$$O(x)=\frac12\Big(\frac{x-1}{x+1}-\frac{x+1}{x-1}\Big)=\frac{(x-1)^2-(x+1)^2}{2(x^2-1)}=\frac{-2x}{x^2-1}.$$
Check: $E+O=\frac{x^2-2x+1}{x^2-1}=\frac{(x-1)^2}{(x-1)(x+1)}=\frac{x-1}{x+1}$. Both parts are defined for $x\neq\pm1$ (the decomposition needs a domain symmetric about $0$).
:::
