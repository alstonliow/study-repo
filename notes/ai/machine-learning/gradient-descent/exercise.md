::: {.problem #prob-cs221hw-1-q3 origin="external" source="cs221hw-1-q3"}
(a) Let $x_1, \dots, x_n$ be real numbers representing positions on a number line. Let $w_1, \dots, w_n$ be positive real numbers representing the importance of each of these positions. Consider the quadratic function: $f(\theta) = \sum_{i=1}^n w_i (\theta - x_i)^2$. Note that $\theta$ here is a scalar. What value of $\theta$ minimizes $f(\theta)$? Show that the optimum you find is indeed a minimum. What problematic issues could arise if some of the $w_i$'s are negative?

Note: You can think about this problem as trying to find the point $\theta$ that's not too far away from the $x_i$'s. Over time, hopefully you'll appreciate how nice quadratic functions are to minimize.

*Expected:* An expression for the value of $\theta$ that minimizes $f(\theta)$ and how you got it. A short calculation/argument to show that it is a minimum. 1-2 sentences describing a problem that could arise if some of the $w_i$'s are negative. Show your work.

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::
