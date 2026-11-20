::: {.problem #prob-camib-ats-2-q12 origin="external" source="camib-ats-2-q12"}
The goal of this question is to guide you through the proof of the Stone–Weierstrass theorem, which asserts that a continuous function $f : K \to \mathbb{R}$, where $K = [a_1,b_1] \times \cdots \times [a_n,b_n] \subset \mathbb{R}^n$, can be approximated uniformly by a sequence of polynomials. (Compare with Taylor series: we don't require analyticity here for the convergence to occur.) We take $n = 1$ in what follows.

(a) Argue that, without loss of generality, it is enough to show the statement with $[a_1,b_1] = [0,1]$.

(b) Letting $p_{n,k}(x) = \binom nk x^k(1 - x)^{n-k}$, show that one has
$$\sum_{k=0}^n p_{n,k}(x) = 1, \qquad \sum_{k=0}^n\Big(x - \frac kn\Big)^2p_{n,k}(x) = \frac1n x(1 - x).$$

(c) Now let $p_n(x) = \sum_{k=0}^n f\big(\frac kn\big)p_{n,k}(x)$. Use the first identity to show
$$|p_n(x) - f(x)| \leq \sum_{|x - \frac kn| < \delta}|f(k/n) - f(x)|\,p_{k,n}(x) + \sum_{|x - \frac kn| \geq \delta}|f(k/n) - f(x)|\,p_{k,n}(x),$$
for any $\delta > 0$.

(d) Choose an appropriate $\delta$, and use the second identity for $p_{n,k}$, to conclude that $p_n \rightrightarrows f$ in $[0,1]$.
:::
