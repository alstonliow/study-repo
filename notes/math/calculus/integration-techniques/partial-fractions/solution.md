<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit1801f06-7-q4" status="draft"}
a) $\frac{\cos x}{1-\sin^2x}=\frac{\cos x}{\cos^2x}=\frac1{\cos x}=\sec x$. With $u=\sin x$, $du=\cos x\,dx$:
$$\int\sec x\,dx=\int\frac{du}{1-u^2}=\int\frac12\Big(\frac1{1+u}+\frac1{1-u}\Big)du=\frac12\ln\Big|\frac{1+u}{1-u}\Big|+c=\frac12\ln\frac{1+\sin x}{1-\sin x}+c,$$
using cover-up (@prp-cover-up): $\frac1{(1-u)(1+u)}$ has coefficient $\frac12$ at both factors. (The fraction is positive since $\lvert\sin x\rvert<1$ where $\sec x$ is defined.)

b) $\frac{1+\sin x}{1-\sin x}=\frac{(1+\sin x)^2}{1-\sin^2x}=\frac{(1+\sin x)^2}{\cos^2x}$, so
$$\frac12\ln\frac{(1+\sin x)^2}{\cos^2x}=\ln\Big|\frac{1+\sin x}{\cos x}\Big|=\ln\lvert\sec x+\tan x\rvert,$$
the formula of @prp-tan-sec-integrals.
:::
