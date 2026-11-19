::: {.problem #prob-cs70hw-14-q7 origin="external" source="cs70hw-14-q7"}
**Sampling a Gaussian With Uniform.** In this question, we will see one way to generate a normal random variable if we have access to a random number generator that outputs numbers between 0 and 1 uniformly at random.

As a general comment, remember that showing two random variables have the same CDF or PDF is sufficient for showing that they have the same distribution.

(a) First, let us see how to generate an exponential random variable with a uniform random variable. Let $U_1 \sim \mathrm{Uniform}(0, 1)$. Prove that $-\ln U_1 \sim \mathrm{Expo}(1)$.

(b) Let $N_1, N_2 \sim \mathcal{N}(0, 1)$, where $N_1$ and $N_2$ are independent. Prove that $N_1^2 + N_2^2 \sim \mathrm{Expo}(1/2)$.

Hint: You may use the fact that over a region $R$, if we convert to polar coordinates $(x, y) \to (r, \theta)$, then the double integral over the region $R$ will be
$$\iint_R f(x, y)\, dx\, dy = \iint_R f(r\cos\theta, r\sin\theta) \cdot r\, dr\, d\theta.$$

(c) Suppose we have two uniform random variables, $U_1$ and $U_2$. How would you transform these two random variables into a normal random variable with mean 0 and variance 1?

Hint: What part (b) tells us is that the point $(N_1, N_2)$ will have a distance from the origin that is distributed as the square root of an exponential distribution. Try to use $U_1$ to sample the radius, and then use $U_2$ to sample the angle.
:::

::: {.problem #prob-eecs126hw-3-q4 origin="external" source="eecs126hw-3-q4"}
**Gaussian Densities.**

(a) Let $X_1\sim N(0,1)$, $X_2\sim N(0,1)$, where $X_1$ and $X_2$ are independent. Convolve the densities of $X_1$ and $X_2$ to show that $X_1+X_2\sim N(0,2)$. Remark. Note that this property is similar to the one shared by independent Poisson random variables.

(b) Let $X\sim N(0,1)$. Compute $E[X^n]$ for all integers $n\ge1$.
:::

::: {.problem #prob-eecs126hw-6-q5 origin="external" source="eecs126hw-6-q5"}
**Matrix Sketching.** Matrix sketching is an important technique in randomized linear algebra to do large computations efficiently. For example, to compute the multiplication $A^T\times B$ of two large matrices $A$ and $B$, we can use a random sketch matrix $S$ to compute a "sketch" $SA$ of $A$ and a "sketch" $SB$ of $B$. Such a sketching matrix has the property that $S^TS\approx I$ so that the approximate multiplication $A^TS^TSB$ is close to $A^TB$.

In this problem, we will discuss two popular sketching schemes and understand how they help in approximate computation. Let $\hat I=S^TS$ and the dimension of sketch matrix $S$ be $d\times n$ (typically $d\ll n$).

(a) (Gaussian-sketch) Define
$$S=\frac{1}{\sqrt d}\begin{pmatrix}S_{11}&\cdots&\cdots&S_{1n}\\\vdots&\ddots&&\vdots\\S_{d1}&\cdots&\cdots&S_{dn}\end{pmatrix}$$
such that $S_{ij}$'s are chosen i.i.d. from $N(0,1)$ for all $i\in[1,d]$ and $j\in[1,n]$. Find the element-wise mean and variance (as a function of $d$) of the matrix $\hat I=S^TS$, that is, find $E[\hat I_{ij}]$ and $\operatorname{Var}[\hat I_{ij}]$ for all $i\in[1,n]$ and $j\in[1,n]$.

(b) (Count-sketch) For each column $j\in[1,n]$ of $S$, choose a row $i$ uniformly randomly from $[1,d]$ such that
$$S_{ij}=\begin{cases}1,&\text{with probability }0.5\\-1,&\text{with probability }0.5\end{cases}$$
and assign $S_{kj}=0$ for all $k\ne i$. An example of a $3\times8$ count-sketch is
$$S=\begin{pmatrix}0&-1&1&0&0&-1&0&0\\1&0&0&0&-1&0&-1&0\\0&0&0&1&0&0&0&-1\end{pmatrix}$$
Again, find the element-wise mean and variance (as a function of $d$) of the matrix $\hat I=S^TS$.

Note that for sufficiently large $d$, the matrix $\hat I$ is close to the identity matrix for both cases. We will use this fact in the lab to do an approximate matrix multiplication.

Note: You can use the fact that the fourth moment of a standard Gaussian is 3 without proof.
:::
