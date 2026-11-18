<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801n-5d-q1" status="draft"}
$x=a\sin\theta$: $\int\frac{a\cos\theta\,d\theta}{a^3\cos^3\theta}=\frac1{a^2}\tan\theta+c=\frac{x}{a^2\sqrt{a^2-x^2}}+c$.
:::

::: {.solution for="prob-mit1801n-5d-q2" status="draft"}
$x=a\sin\theta$: $a^3\int\sin^3\theta\,d\theta=a^3\big(-\cos\theta+\frac13\cos^3\theta\big)$. With $a\cos\theta=\sqrt{a^2-x^2}$ this is $-a^2\sqrt{a^2-x^2}+\frac13(a^2-x^2)^{3/2}+c=-\frac13\sqrt{a^2-x^2}\,(2a^2+x^2)+c$.
:::

::: {.solution for="prob-mit1801n-5d-q7" status="draft"}
$x=a\sec\theta$, $dx=a\sec\theta\tan\theta\,d\theta$: $\int\frac{a\tan\theta\cdot a\sec\theta\tan\theta}{a^2\sec^2\theta}d\theta=\int\frac{\tan^2\theta}{\sec\theta}d\theta=\int(\sec\theta-\cos\theta)\,d\theta=\ln\lvert\sec\theta+\tan\theta\rvert-\sin\theta$. Back in $x$: $\ln\big\lvert x+\sqrt{x^2-a^2}\big\rvert-\frac{\sqrt{x^2-a^2}}x+c$.
:::

::: {.solution for="prob-mit1801n-5d-q10" status="draft"}
$x^2+4x+13=(x+2)^2+9$ (@prp-completing-the-square). With $x+2=3\tan\theta$: $\int\frac{3\sec^2\theta\,d\theta}{27\sec^3\theta}=\frac19\sin\theta+c=\frac{x+2}{9\sqrt{x^2+4x+13}}+c$.
:::
