<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801n-4a-q1" status="draft"}
The curves meet where $x^3=ax$: $x=0,\pm\sqrt a$. On $(0,\sqrt a)$, $ax>x^3$, and the region is symmetric about the origin, so
$$A=2\int_0^{\sqrt a}(ax-x^3)\,dx=2\Big(\frac{a^2}2-\frac{a^2}4\Big)=\frac{a^2}2 .$$
:::

::: {.solution for="prob-mit1801n-4a-q2" status="draft"}
The region above the $x$-axis is $-1\le x\le1$, $0\le y\le1-x^2$.

- Vertical strips: $\int_{-1}^1(1-x^2)\,dx=2-\frac23=\frac43$.
- Horizontal strips: at height $y$ the region runs from $-\sqrt{1-y}$ to $\sqrt{1-y}$, so $\int_0^12\sqrt{1-y}\,dy=-\frac43(1-y)^{3/2}\Big|_0^1=\frac43$.
:::

::: {.solution for="prob-mit1801n-4a-q4" status="draft"}
Consecutive crossings are at $x=\frac\pi4$ and $x=\frac{5\pi}4$, with $\sin x\ge\cos x$ between them:
$$\int_{\pi/4}^{5\pi/4}(\sin x-\cos x)\,dx=\big[-\cos x-\sin x\big]_{\pi/4}^{5\pi/4}=\sqrt2-(-\sqrt2)=2\sqrt2 .$$
:::
