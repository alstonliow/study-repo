<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit1801f06-7-q5" status="draft"}
The first hump is $-\pi/2\le x\le\pi/2$, which is symmetric about the $y$-axis; rotating it around the $y$-axis gives the same solid as rotating its right half $0\le x\le\pi/2$. By shells (@def-disks-and-shells),
$$V=\int_0^{\pi/2}2\pi x\cos x\,dx .$$
By @thm-integration-by-parts with $u=x$, $v=\sin x$: $\int x\cos x\,dx=x\sin x-\int\sin x\,dx=x\sin x+\cos x$. Hence
$$V=2\pi\big[x\sin x+\cos x\big]_0^{\pi/2}=2\pi\Big(\frac\pi2-1\Big)=\pi^2-2\pi\approx3.59 .$$
:::
