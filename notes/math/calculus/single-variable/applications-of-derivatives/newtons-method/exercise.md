::: {.problem #prob-mit1801f06-3-q5 origin="external" source="mit1801f06-3-q5"}
Newton's method.

a) Compute the cube root of 9 to 6 significant figures using Newton's method. Give the general formula, and list numerical values, starting with $x_0=2$. At what iteration $k$ does the method surpass the accuracy of your calculator or computer? (Display your answers to the accuracy of your calculator or computer.)

b) For each step $x_k$, $k=0,1,\ldots$, say whether the value is i) larger or smaller than $9^{1/3}$; ii) larger or smaller than the preceding value $x_{k-1}$. Illustrate on the graph of $x^3-9$ why this is so.

c) Find a quadratic approximation to $9^{1/3}$, and estimate the difference between the quadratic approximation and the exact answer. (Hint: To get a reasonable quadratic approximation, use $9=8(1+1/8)$.)
:::

::: {.problem #prob-mit18335ps-1-q3 origin="external" source="mit18335ps-1-q3"}
**Newtonish methods**

Newton's method for a root of $f(x)=0$ is to iterate $x_{n+1}=x_n-f(x_n)/f'(x_n)$ starting from some initial guess $x_1$ (which must be sufficiently close to the root to guarantee convergence in general). Suppose that you are also given $f''(x)$, the second derivative. In this problem, you will propose an iteration scheme that takes advantage of this second-derivative information.

(a) Propose a Newton-like iteration that takes advantage of $f$, $f'$, and $f''$ (assuming $f$ is analytic in the neighborhood of the root). (Hint: use a second-order Taylor approximation of $f$.) If you solve a quadratic equation $ax^2+bx+c=0$, you might want to compute the two roots as $\frac{-b-\sqrt{b^2-4ac}}{2a}$ and $\frac{2c}{-b-\sqrt{b^2-4ac}}$, assuming $b>0$, to avoid disastrous cancellation errors for $|ac|\ll b^2$. (Google "quadratic formula cancellation error." In the event of a disaster, your method can fall back to an ordinary Newton step.)

(b) Analyze its asymptotic convergence rate: if $x$ is an exact root, write $x_n=x(1+\delta_n)$ as in class, and solve for $\delta_{n+1}$ in terms of $\delta_n$ assuming you are close to the root ($\delta_n\ll1$).

(c) Modify the Julia Newton's-method notebook from class to implement your method to compute a root of $f(x)=x^3-1$. In particular start with $x_1=2$, so that your scheme should(!) converge to $x=1$, and look at the error $x_n-1$. Demonstrate that it agrees with your predicted convergence rate from the previous part. [You should use arbitrary precision as in the notebook from class, so that you can watch the convergence rate for many digits. An approximate number of accurate digits is given by $-\log_{10}(x_n-1)$.]
:::
