::: {.problem #prob-eecs126hw-13-q1 origin="external" source="eecs126hw-13-q1"}
**Projections.** The following exercises are from the note on the Hilbert space of random variables. See the notes for some hints.

(a) Let $\mathcal H:=\{X:X\text{ is a real-valued random variable with }E[X^2]<\infty\}$. Prove that $\langle X,Y\rangle:=E[XY]$ makes $\mathcal H$ into a real inner product space.[^1]

(b) Let $U$ be a subspace of a real inner product space $V$ and let $P$ be the projection map onto $U$. Prove that $P$ is a linear transformation.

(c) Suppose that $U$ is finite-dimensional, $n:=\dim U$, with basis $\{v_i\}_{i=1}^{n}$. Suppose that the basis is orthonormal. Show that $Py=\sum_{i=1}^{n}\langle y,v_i\rangle v_i$. (Note: If we take $U=\mathbb R^n$ with the standard inner product, then $P$ can be represented as a matrix in the form $P=\sum_{i=1}^{n}v_iv_i^T$.)

[^1]: To be perfectly correct, it is possible for $X\ne0$ but $E[X^2]=0$; this occurs if $X=0$ with probability 1. To fix this, we need to define two random variables $X$ and $Y$ to be equal if $P(X=Y)=1$. In other words, we consider equivalence classes of random variables, defined by the relation $\overset{\text{a.s.}}{=}$. With this definition, then if $X\ne0$ we do indeed have $E[X^2]>0$.
:::

::: {.problem #prob-eecs126hw-13-q2 origin="external" source="eecs126hw-13-q2"}
**Exam Difficulties.** The difficulty of an EECS 126 exam, $\Theta$, is uniformly distributed on $[0,100]$ (i.e. continuous distribution, not discrete), and Alice gets a score $X$ that is uniformly distributed on $[0,\Theta]$. Alice gets her score back and wants to estimate the difficulty of the exam.

(a) What is the MLE of $\Theta$? What is the MAP of $\Theta$?

(b) What is the LLSE for $\Theta$?
:::

::: {.problem #prob-eecs126hw-13-q4 origin="external" source="eecs126hw-13-q4"}
**Photodetector LLSE.** Consider a photodetector in an optical communications system that counts the number of photons arriving during a certain interval. A user conveys information by switching a photon transmitter on or off. Assume that the probability of the transmitter being on is $p$. If the transmitter is on, the number of photons transmitted over the interval of interest is a Poisson random variable $\Theta$ with mean $\lambda$, and if it is off, the number of photons transmitted is $0$.

Unfortunately, regardless of whether or not the transmitter is on or off, photons may be detected due to "shot noise". The number $N$ of detected shot noise photons is a Poisson random variable $N$ with mean $\mu$, independent of the transmitted photons. Let $T$ be the number of transmitted photons and $D$ be the number of detected photons. Find $L[T\mid D]$.
:::

::: {.problem #prob-eecs126hw-14-q1 origin="external" source="eecs126hw-14-q1"}
**Balls in Bins Estimation.** We throw $n\ge1$ balls into $m\ge2$ bins. Let $X$ and $Y$ represent the number of balls that land in bin 1 and 2 respectively.

(a) Calculate $E[Y\mid X]$.

(b) What are $L[Y\mid X]$ and $Q[Y\mid X]$ (where $Q[Y\mid X]$ is the best quadratic estimator of $Y$ given $X$)?

Hint: Your justification should be no more than two or three sentences, no calculations necessary! Think carefully about the meaning of the MMSE.

(c) Unfortunately, your friend is not convinced by your answer to the previous part. Compute $E[X]$ and $E[Y]$.

(d) Compute $\operatorname{var}(X)$.

(e) Compute $\operatorname{cov}(X,Y)$.

(f) Compute $L[Y\mid X]$ using the formula. Ensure that your answer is the same as your answer to part (b).
:::

::: {.problem #prob-eecs126hw-14-q2 origin="external" source="eecs126hw-14-q2"}
**MMSE and Conditional Expectation.** Let $X,Y_1,\dots,Y_n$ be square integrable random variables. The MMSE of $X$ given $(Y_1,\dots,Y_n)$ is defined as the function $\phi(Y_1,\dots,Y_n)$ which minimizes the mean square error
$$E[(X-\phi(Y_1,\dots,Y_n))^2].$$

(a) For this part, assume $n=1$. Show that the MMSE is precisely the conditional expectation $E[X|Y]$. Hint: expand the difference as $(X-E[X|Y]+E[X|Y]-\phi(Y))$.

(b) Argue that
$$E\bigl[(X-E[X\mid Y_1,\dots,Y_n])^2\bigr]\le E\Bigl[\Bigl(X-\frac1n\sum_{i=1}^{n}E[X\mid Y_i]\Bigr)^2\Bigr].$$
That is, the MMSE does better than the average of the individual estimates given each $Y_i$.
:::

::: {.problem #prob-eecs126hw-14-q3 origin="external" source="eecs126hw-14-q3"}
**Geometric MMSE.** Let $N$ be a geometric random variable with parameter $1-p$, and $(X_i)_{i\in\mathbb N}$ be i.i.d. exponential random variables with parameter $\lambda$. Let $T=X_1+\dots+X_N$. Compute the LLSE and MMSE of $N$ given $T$.

Hint: Compute the MMSE first.
:::
