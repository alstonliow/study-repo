<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit1801f06-7-q3" status="draft"}
a) $\int\tan^{n+2}x\,dx=\int\tan^nx\,(\sec^2x-1)\,dx=\int\tan^nx\sec^2x\,dx-\int\tan^nx\,dx$. In the first integral put $u=\tan x$, $du=\sec^2x\,dx$: it is $\int u^n\,du=\frac{\tan^{n+1}x}{n+1}+c$.

b) With $n=2$ and then $n=0$: $\int\tan^4x\,dx=\frac{\tan^3x}3-\int\tan^2x\,dx=\frac{\tan^3x}3-\Big(\tan x-\int dx\Big)=\frac{\tan^3x}3-\tan x+x+c$.
:::
