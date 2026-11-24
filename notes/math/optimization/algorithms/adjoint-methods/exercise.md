::: {.problem #prob-mit18s096ps-2-q1 origin="external" source="mit18s096ps-2-q1"}
Suppose that $A(p)$ takes a vector $p\in\mathbb{R}^{n-1}$ and returns the $n\times n$ tridiagonal real-symmetric matrix
$$
A(p)=\left(\begin{array}{ccccc}
a_{1} & p_{1}\\
p_{1} & a_{2} & p_{2}\\
 & p_{2} & \ddots & \ddots\\
 &  & \ddots & a_{n-1} & p_{n-1}\\
 &  &  & p_{n-1} & a_{n}
\end{array}\right),
$$
where $a\in\mathbb{R}^{n-1}$ is some constant vector. Now, define a scalar-valued function $f(p)$ by
$$
f(p)=\left(c^{T}A(p)^{-1}b\right)^{2}
$$
for some constant vectors $b,c\in\mathbb{R}^{n}$ (assuming we choose $p$ and $a$ so that $A$ is invertible). Note that, in practice $A(p)^{-1}b$ is *not* computed by explicitly inverting the matrix $A$---instead, it can be computed in $\Theta(n)$ (i.e., roughly proportional to $n$) arithmetic operations using Gaussian elimination that takes advantage of the "sparsity" of $A$ (the pattern of zero entries), a "tridiagonal solve".

(a) Write down a formula for computing $\partial f/\partial p_{1}$ (in terms of matrix--vector products and matrix inverses). (Hint: once you know $df$ in terms of $dA$, you can get $\partial f/\partial p_{1}$ by "dividing" both sides by $\partial p_{1}$, so that $dA$ becomes $\partial A/\partial p_{1}$.)

(b) Outline a sequence of steps to compute both $f$ and $\nabla f$ (with respect to $p$) using only *two* tridiagonal solves $x=A^{-1}b$ and an "adjoint" solve $v=A^{-1}\text{(something)}$, plus $\Theta(n)$ (i.e., roughly proportional to $n$) additional arithmetic operations.

(c) Write a program implementing your $\nabla f$ procedure (in Julia, Python, Matlab, or any language you want) from the previous part. (You don't need to use a fancy tridiagonal solve if you don't know how to do this in your language; you can solve $A^{-1}\text{(vector)}$ inefficiently if needed using your favorite matrix libraries.) Implement a finite-difference test: Choose $a,b,c,p$ at random, and check that $\nabla f\cdot\delta p\approx f(p+\delta p)-f(p)$ (to a few digits) for a randomly chosen small $\delta p$.

*Note (these notes):* The diagonal $a$ has $n$ entries $a_1,\dots,a_n$, as the matrix shows; the statement's $a\in\mathbb{R}^{n-1}$ is a slip in the handout.
:::
