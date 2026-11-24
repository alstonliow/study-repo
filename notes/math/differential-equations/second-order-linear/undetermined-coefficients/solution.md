<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-16-q1" status="draft"}
1. $p(s)=s^3-s=s(s^2-1)$ has $p(0)=0$, so write the equation as $(D^2-1)w=t^2+1$ with $w=\dot x$ (as in the remark on $p(0)=0$ in @sec-math-differential-equations-second-order-linear-undetermined-coefficients).
2. Try $w=at^2+bt+c$: $\ddot w-w=-at^2-bt+(2a-c)=t^2+1$, so $a=-1$, $b=0$, $c=-3$: $w=-t^2-3$.
3. Integrating, $x_p=-\tfrac13t^3-3t$.
4. The characteristic roots are $0,1,-1$, so
$$x=-\tfrac13t^3-3t+c_1+c_2e^t+c_3e^{-t}.$$
:::
