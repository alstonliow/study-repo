::: {.problem #prob-eecs126hw-10-q2 origin="external" source="eecs126hw-10-q2"}
**Introduction to Information Theory.** Recall that the entropy of a discrete random variable $X$ is defined as
$$H(X)\overset{\Delta}{=}-\sum_xp(x)\log p(x)=-E[\log p(X)],$$
where $p(\cdot)$ is the PMF of $X$. Here, the logarithm is taken with base $2$, and entropy is measured in bits.

(a) Prove that $H(X)\ge0$.

(b) Entropy is often described as the average information content of a random variable. If $H(X)=0$, then no new information is given by observing $X$. On the other hand, if $H(X)=m$, then observing the value of $X$ gives you $m$ bits of information on average. Let $X$ be a Bernoulli random variable with $P(X=1)=p$. Would you expect $H(X)$ to be greater when $p=1/2$ or when $p=1/3$? Calculate $H(X)$ in both of these cases and verify your answer.

(c) We now consider a binary erasure channel (BEC).

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab] (x0) at (0,1) {$0$};
\node[lab] (x1) at (0,-1) {$1$};
\node[lab] (y0) at (3,1) {$0$};
\node[lab] (ye) at (3,0) {$?$};
\node[lab] (y1) at (3,-1) {$1$};
\node[lab] at (0,1.6) {$X$};
\node[lab] at (3,1.6) {$Y$};
\draw[->] (x0)--node[lab,tick,above]{$1-p_e$}(y0);
\draw[->] (x0)--node[lab,tick,above,pos=.7]{$p_e$}(ye);
\draw[->] (x1)--node[lab,tick,below,pos=.7]{$p_e$}(ye);
\draw[->] (x1)--node[lab,tick,below]{$1-p_e$}(y1);
\end{tikzpicture}
\end{center}
```

The input $X$ is a Bernoulli random variable with $P(X=0)=P(X=1)=1/2$. Each time that we use the channel the input $X$ will either get get erased with probability $p_e$, or it will get transmitted correctly with probability $1-p_e$. Using the character "?" to denote erasures, the output $Y$ of the channel can be written as
$$Y=\begin{cases}X,&\text{with probability }1-p_e\\?,&\text{with probability }p_e.\end{cases}$$
Compute $H(Y)$.

(d) We defined the entropy of a single random variable as a measure of the uncertainty inherent in the distribution of the random variable. We now extend this definition for a pair of random variables $(X,Y)$, but there is nothing really new in this definition because the pair $(X,Y)$ can be considered to be a single vector-valued random variable. Define the joint entropy of a pair of discrete random variables $(X,Y)$ to be
$$H(X,Y)\overset{\Delta}{=}-E[\log p(X,Y)],$$
where $p(\cdot,\cdot)$ is the joint PMF and the expectation is also taken over the joint distribution of $X$ and $Y$.

Compute $H(X,Y)$, for the BEC.

:::

::: {.problem #prob-eecs126hw-10-q3 origin="external" source="eecs126hw-10-q3"}
**Info Theory Bounds.** In this problem we explore some intuitive results which can be formalized using information theory.

(a) (optional) Prove Jensen's inequality: if $f$ is a convex function and $Z$ is random variable, then $f(E[Z])\le E[f(Z)]$. Hint: You can use fact that every convex function can be represented by the pointwise supremum of affine functions that are bounded above by $f$, i.e.
$$f(x)=\sup\{l(x)=ax+b:l(x)\le f(x)\ \forall x\}.$$

(b) It turns out that there is actually a limit to how much "randomness" there is in a random variable $X$ which takes on $|\mathcal X|$ distinct values. Show that for any distribution $p_X$, $H(X)\le\log|\mathcal X|$. Use this to conclude that if a random variable $X$ takes values in $[n]:=\{1,2,\dots,n\}$, then the distribution which maximizes $H(X)$ is $X\sim\text{Uniform}([n])$.

(c) For two random variable $X,Y$ we define the mutual information (this should have also been covered in discussion) to be
$$I(X;Y)=\sum_x\sum_yp(x,y)\log\frac{p(x,y)}{p(x)p(y)},$$
where the sums are taken over all outcomes of $X$ and $Y$. Show that $I(X;Y)\ge0$. In discussion, you have seen that $I(X;Y)=H(X)-H(X|Y)$. Therefore the fact that mutual information is nonnegative means intuitively that conditioning will only ever reduce our uncertainty.
:::

::: {.problem #prob-eecs126hw-10-q4 origin="external" source="eecs126hw-10-q4"}
**Relative Entropy and Stationary Distributions.** We define the relative entropy, also known as Kullback-Leibler divergence, between two distributions $p$ and $q$ as
$$D(p\|q)=E_{X\sim p}\Bigl[\log\Bigl(\frac{p(X)}{q(X)}\Bigr)\Bigr]=\sum_xp(x)\log\frac{p(x)}{q(x)}$$

(a) Show that $D(p\|q)\ge0$, with equality if and only if $p(x)=q(x)$ for all $x$. Thus, it is useful to think about $D(\cdot\|\cdot)$ as a sort of distance function. Hint: For strictly concave functions $f$, Jensen's inequality states that $f(E[Z])\ge E[f(Z)]$ with equality if and only if $Z$ is constant.

(b) Show that for any irreducible Markov chain with stationary distribution $\pi$, any other stationary distribution $\mu$ must be equal to $\pi$. Hint: Consider $D(\pi\|\mu P)$.
:::
