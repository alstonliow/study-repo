<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-2-q4" status="draft"}
(a) Expand $S_n^4=\sum_{i,j,k,l}X_iX_jX_kX_l$. A term with some index appearing exactly once has expectation $0$ (independence and $E[X_i]=0$). The surviving terms are $i=j=k=l$ ($n$ terms) and two distinct indices each appearing twice ($\binom42=6$ placements times $\binom n2$ pairs). So
$$E[S_n^4]=nE[X_1^4]+3n(n-1)\bigl(E[X_1^2]\bigr)^2;$$
the third moment does not appear.

(b) By Markov's inequality applied to $S_n^4$ (@thm-generalised-markov),
$$P(|S_n|>n\epsilon)\le\frac{E[S_n^4]}{n^4\epsilon^4}\le\frac{E[X_1^4]+3(E[X_1^2])^2}{\epsilon^4n^2}=O(n^{-2}).$$

(c) $\sum_nn^{-2}<\infty$, so by Borel–Cantelli (@lem-borel-cantelli) with probability $1$ only finitely many $|S_n/n|>\epsilon$, i.e. $\limsup|S_n/n|\le\epsilon$. Apply this to $\epsilon=1/k$ for every $k\ge1$; the intersection of countably many probability-one events has probability one, and on it $S_n/n\to0$.
:::

::: {.solution for="prob-eecs126hw-4-q3" status="draft"}
(a) $Y_n\to0$. By independence $E|Y_n|=\prod_iE|X_i|=2^{-n}$, so by Markov's inequality $P(|Y_n|>\epsilon)\le2^{-n}/\epsilon\to0$.

(b) $Y_n\to1$. $Y_n\le1$, and $P(Y_n<1-\epsilon)=P(X_1<1-\epsilon)^n=(1-\epsilon/2)^n\to0$ for $0<\epsilon<2$.

(c) $Y_n\to\frac13$. The $X_i^2$ are i.i.d. with mean $E[X_1^2]=\int_{-1}^{1}\frac{x^2}{2}\,dx=\frac13$ and finite variance, so the weak law of large numbers (@thm-law-of-large-numbers) applies.
:::

::: {.solution for="prob-eecs126hw-4-q4" status="draft"}
(a) $W_n=4^nw_0$ if the first $n$ tosses are all heads (probability $2^{-n}$) and $0$ otherwise, so $E[W_n]=2^nw_0\to\infty$.

(b) $W_n\to0$ almost surely. Once a tail occurs the wealth stays $0$ forever, and the probability of never seeing a tail is $\lim_n2^{-n}=0$. So with probability $1$, $W_n=0$ for all large $n$. Almost sure convergence does not carry the expectations along.
:::

::: {.solution for="prob-eecs126hw-6-q1" status="draft"}
(a) The CDF of the constant $c$ is continuous everywhere except at $c$. For $\epsilon>0$,
$$P(|X_n-c|>\epsilon)\le P(X_n\le c-\epsilon)+1-P(X_n\le c+\epsilon/2)\to0+1-1=0.$$

(b) Let $Z_n=\frac{1}{\sigma\sqrt n}\sum_i(X_i-\mu)$, so $\bar X_n-\mu=\frac{\sigma}{\sqrt n}Z_n$. Fix $\epsilon>0$ and $K>0$. For $n\ge(\sigma K/\epsilon)^2$,
$$P(|\bar X_n-\mu|>\epsilon)=P\Bigl(|Z_n|>\frac{\epsilon\sqrt n}{\sigma}\Bigr)\le P(|Z_n|>K)\to P(|N(0,1)|>K).$$
So $\limsup_nP(|\bar X_n-\mu|>\epsilon)\le P(|N(0,1)|>K)$ for every $K$, and letting $K\to\infty$ the limit is $0$.
:::

::: {.solution for="prob-eecs126d-4-q3" status="draft"}
(a) Yes. On the probability-one event, $X_n=a$ and $X_n=b$ both happen for infinitely many $n$; a convergent sequence would have a limit equal to both $a$ and $b$. So $X_n$ converges with probability $0$.

(b) Yes, to $1/Y$. $P(Y=0)=0$. If $Y>0$, $Y+\frac1n\to Y$ and $X_n\to\frac1Y$. If $Y<0$, then $Y+\frac1n<0$ for large $n$ and again $X_n\to\frac1Y$.

(c) No. For every outcome, each block $\{2^k,\dots,2^{k+1}-1\}$ contains one $n$ with $X_n=2^k$ and others with $X_n=0$, so the sequence takes the value $0$ and arbitrarily large values infinitely often.

(d) Yes, to $X=0$: for $n$ in block $k$, $P(X_n\ne0)=2^{-k}\to0$. But $E[X_n]=2^k\cdot2^{-k}=1$ for every $n$, while $E[X]=0$ (compare the remark on expectations after @thm-continuous-mapping).
:::

::: {.solution for="prob-eecs126d-5-q1" status="draft"}
The fraction of volume of $[-1,1]^n$ in a set is the probability that $X=(X_1,\dots,X_n)$ lies in it.

(a) $n=1$: $A$ is $\{0.9/\sqrt3<|x|<1.1/\sqrt3\}$, total length $0.4/\sqrt3$, fraction $\frac{0.2}{\sqrt3}\approx0.115$. $n=2$: an annulus with radii $0.9\sqrt{2/3}$ and $1.1\sqrt{2/3}$, both less than $1$, so it lies inside the square; its area is $\pi\cdot\frac23(1.21-0.81)$, fraction $\frac{\pi}{15}\approx0.209$.

(b) $\frac{\|X\|_2^2}{n}=\frac1n\sum_iX_i^2$ and $E[X_i^2]=\frac13$, so by the weak law of large numbers $\frac{\|X\|_2^2}{n}\to\frac13$ in probability, and by continuous mapping (@thm-continuous-mapping) $\|X\|_2/\sqrt{n/3}\to1$. Hence $P(X\in A_{n,\epsilon})\to1$ for every $\epsilon>0$.

In low dimension the thin shell is a small part of the cube, so one expects "most points to be spread out". In high dimension almost all the volume sits in a thin shell at radius $\sqrt{n/3}$: near the corners relative to the inscribed ball of radius $1$, and far from the centre. Random points are then all at nearly the same distance from the origin (and from each other), which is what makes distance-based methods hard in high dimension.
:::

::: {.solution for="prob-eecs126d-6-q1" status="draft"}
1. If $T>n$, the walk is still inside at time $n$, so $P(T>n)\le P(|S_n|\le a)$.
2. Fix $K>0$. For $n\ge(a/K)^2$, $P(|S_n|\le a)\le P(|S_n/\sqrt n|\le K)$, and by the central limit theorem (@thm-central-limit-theorem) this tends to $P(|Z|\le K)$ with $Z\sim N(0,1)$.
3. So $\limsup_nP(T>n)\le P(|Z|\le K)$ for every $K$, and letting $K\to0$ gives $\lim_nP(T>n)=0$.
4. $\{T=\infty\}\subseteq\{T>n\}$ for every $n$, so $P(T=\infty)=0$.
:::
