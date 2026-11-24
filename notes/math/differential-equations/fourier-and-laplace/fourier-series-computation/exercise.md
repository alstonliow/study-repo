::: {.problem #prob-mit1803ps-21-q1 origin="external" source="mit1803ps-21-q1"}
[Fourier Series] This problem will use the Mathlet Fourier Coefficients.

When the applet opens you are presented with a series of sliders labeled $b_n$. By pressing the [Formula] radio button you can see that they are coefficients of sines in a Fourier series made up entirely of sine functions. If you press the [Cosine] radio button you'll see $a$'s, coefficients of cosines. Move one of the slider handles: a cosine or sine curve appears and changes amplitude. Release it at some value and move another one. The white curves shows the new sinusoid, and the yellow curve shows the sum of the two. By moving more sliders you can build up more complicated sums and more complicated functions.

Now select the Target [B]. Is it an even function or an odd function? Based on this, decide whether to appoximate it using sines or cosines. Select one or the other appropriately (using [All terms]) and do the best you can by eyeballing the result to get the best approximation you can to the green target curve. Does it appear that only even terms are needed? Only odd term? or both? The [Odd terms] and [Even terms] buttons allow you to choose just the even terms or the odd terms, and gives you more of the one you select. If it seems that just the even or odd terms will be useful, explain (in words) why.

(a) Write down these values of the coefficients.

(b) The target function [B] is the periodic function with period $2\pi$ which is given by $f(t) = \frac\pi4$ for $-\frac\pi2 < t < \frac\pi2$, $f(t) = -\frac\pi4$ for $\frac\pi2 < t < \frac{3\pi}2$, and $f(\pm\frac\pi2) = 0$. Compute the Fourier coefficients for this function, using the integral formulas for them, and compare with your answers from (a). Reset the sliders to the computed values and see if it looks like a better fit.

(c) Now set the sliders to some random set of values. Still with target function [B] displayed, select the [Distance] button. A number appears at the upper right corner of the screen. This is the "root mean square" distance from the target function to the selected finite Fourier sum. It is a measure of goodness of fit. Instead of eyeballing the fit as before, start from the bottom and successively adjust the sliders to minimize the distance. Write down the optimal values of the coefficients. Compare with the computed values.

Lessons: (1) The Fourier coefficients are the coefficients resulting in the best possible fit, and (2) the process of optimizing one coefficient is independent of the process of optimizing any of the others. (This is "orthogonality.")

*Note (these notes):* The Java Mathlets this problem uses no longer run in most browsers; the solution answers the analytic parts and describes what the applet would show.
:::

::: {.problem #prob-mit1803ps-22-q1 origin="external" source="mit1803ps-22-q1"}
[Fourier Series]

(a) Find the Fourier series for $2\sin(t - \frac\pi3)$ (Hint: A function of period $2\pi$ has just one expression as a linear combination of $\cos(mt)$'s and $\sin(nt)$'s.)

The square wave $\operatorname{sq}(t)$ is the odd function of period $2\pi$ such that $\operatorname{sq}(t) = 1$ for $0 < t < \pi$ and $\operatorname{sq}(\pi) = 0$. In class we calculated its Fourier series.

(b) $\operatorname{sq}(t)$ has minimal period $2\pi$, but it is also a function of period $4\pi$. Use the integral formulas for the Fourier coefficients to calculate its Fourier series, regarded as a function of period $4\pi$. Comment on the relationship between your answer and the Fourier series for $\operatorname{sq}(t)$.

Use the Fourier series for $\operatorname{sq}(t)$, along with calculus and algebraic manipulations, to compute the Fourier series of each of the following functions without evaluating any of the integrals for the Fourier coefficients. In each case, sketch a graph of the function, as well, and give the minimal period.

(c) $\operatorname{sq}(t - \frac\pi4)$.

(d) $1 + 2\operatorname{sq}(2\pi t)$.

(e) The $f(t)$ of [B] in the Fourier Coefficients Applet explored in this session.

(f) The periodic function $g(t)$ with period $2\pi$ such that $g(t) = t$ for $-\frac\pi2 \le t \le \frac\pi2$ and $g(t) = \pi - t$ for $\frac\pi2 \le t \le \frac{3\pi}2$. (Hint: what is $g'(t)$ in terms of $\operatorname{sq}(t)$?)
:::
