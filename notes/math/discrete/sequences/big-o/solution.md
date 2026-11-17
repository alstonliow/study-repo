<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-sequences-11" status="draft"}
(a) No. Once $n\ge 10^4$ we have $n^2 > 100\,n^{1.5}$, since this is
    equivalent to $n^{0.5} > 100$. Oh-No had many winning choices, and
    $n = 10^6$ is one of them.

(b) Nothing. Whatever $c$ and $N$ Oh-Yes picks, Oh-No can choose
    $n > \max(N, c^2)$. Then $n^{0.5} > c$, so $n^2 > c\,n^{1.5}$. Oh-Yes
    has no winning move, because $n^2$ is not $O(n^{1.5})$.

(c) (Play it.)

(d) Oh-Yes has a winning strategy exactly when $a_n = O(f(n))$: there exist
    $c>0$ and $N$ with $a_n\le c\,f(n)$ for all $n\ge N$. Oh-Yes simply
    plays those $c$ and $N$.

(e) Take $a_n = n$ and $f(n) = \log_2 n$. Given any $c$ and $N$, Oh-No picks
    a large $n\ge N$ with $n > c\log_2 n$, which exists because
    $n/\log_2 n\to\infty$; for example a large power of $2$, $n = 2^m$ with
    $2^m > cm$.

(f) Oh-No has a winning strategy exactly when $a_n$ is **not** $O(f(n))$:
    for every $c>0$ and every $N$ there is some $n\ge N$ with
    $a_n > c\,f(n)$. Exactly one of the two players has a winning strategy.
:::

::: {.solution for="prob-sequences-12" status="draft"}
(a) $O(n^4)$. It is $(n+1)^4$.

(b) $\binom n2 = \frac{n(n-1)}2 = O(n^2)$.

(c) $\binom n3 = \frac{n(n-1)(n-2)}6 = O(n^3)$.

(d) The sum is $n + d\,\frac{n(n-1)}2$, which is $O(n^2)$ (or $O(n)$ if
    $d = 0$).

(e) $2^{n+1} - 1 = O(2^n)$.

(f) $n!\le n^n$, so $(n!)^{1/n}\le n$, giving $O(n)$. This cannot be improved
    to a smaller power of $n$, since $(n!)^{1/n}$ is about $n/e$.

(g) $n^{1/n}\le e^{1/e} < 2$ for all $n\ge1$, so it is $O(1)$. (In fact
    $n^{1/n}\to1$.)
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6042f10-7-q5" status="draft"}
(a) $f=O(g)$, $f=\Omega(g)$, $f=\Theta(g)$: $\log_2n=(\log_210)\log_{10}n$, a constant multiple, but not $f\sim g$ (the ratio is $\log_210\approx3.32$).

(b) $f=o(g)$ and $f=O(g)$: $\frac{2^n}{10^n}=5^{-n}\to0$.

(c) $f=o(g)$ and $f=O(g)$: $\frac0{17}=0$.

(d) None. For integer $n$, the pairs $(f(n),g(n))$ cycle through $(2,1),(1,2),(0,1),(1,0)$. When $n\equiv3\pmod4$, $g(n)=0<f(n)=1$, so $f\ne O(g)$; when $n\equiv2\pmod4$, $f(n)=0<g(n)=1$, so $g\ne O(f)$, i.e. $f\ne\Omega(g)$. The others need one of these.

(e) $f=\omega(g)$ and $f=\Omega(g)$: every exponential $c^n$ with $c>1$ eventually exceeds every polynomial, since $\frac{\ln(c^n)}{\ln(n^k)}=\frac{n\ln c}{k\ln n}\to\infty$.
:::
