<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-functions-09" status="draft"}
For $x\in A$, $\mathrm{Fix}(\{x\})$ is the set of bijections that fix $x$, and
$$F = \bigcup_{x\in A}\mathrm{Fix}(\{x\}).$$
A bijection fixes every element of $X$ exactly when it is in all of the
$\mathrm{Fix}(\{x\})$ for $x\in X$, so
$$\bigcap_{x\in X}\mathrm{Fix}(\{x\}) = \mathrm{Fix}(X).$$
By inclusion–exclusion (Exercise 1.13),
$$|F| = \sum_{\emptyset\ne X\subseteq A}(-1)^{|X|-1}\,|\mathrm{Fix}(X)|.$$
:::

::: {.solution for="prob-functions-10" status="draft"}
(a) The number of bijections fixing $X$ depends only on $|X|$, not on which
    elements $X$ contains: relabelling the elements of $A$ turns the
    bijections fixing one $k$-set into those fixing any other.

(b) A bijection fixing $X$ is an arbitrary bijection on the other $n-k$
    elements: $f_k = (n-k)!$.

(c) There are $\binom nk$ sets $X$ of size $k$, so by Exercise 9
    $$|F| = \sum_{k=1}^n(-1)^{k-1}\binom nk f_k = \sum_{k=1}^n(-1)^{k-1}\binom nk(n-k)! = \sum_{k=1}^n(-1)^{k-1}\frac{n!}{k!}.$$

(d) $$n! - |F| = n! - \sum_{k=1}^n(-1)^{k-1}\binom nk f_k = n!\sum_{k=0}^n\frac{(-1)^k}{k!}.$$

(e) The proportion is $\sum_{k=0}^n(-1)^k/k!$:

    | set | $n$ | fixed-point-free | proportion |
    |---|---|---|---|
    | $\{0,1\}$ | 2 | 1 | $0.5$ |
    | suits | 4 | 9 | $0.375$ |
    | decimal digits | 10 | 1{,}334{,}961 | $\approx 0.3678795$ |
    | alphabet | 26 | $\approx 1.48\times10^{26}$ | $\approx 0.3678794412$ |

(f) The formula works for every finite set. As $n$ grows the proportion
    converges very quickly to
    $$\sum_{k=0}^\infty\frac{(-1)^k}{k!} = \frac1e\approx 0.367879,$$
    and the error is less than $1/(n+1)!$. For $n = 26$ it already agrees
    with $1/e$ to about $27$ decimal places.
:::

::: {.solution for="prob-functions-11" status="draft"}
(a) Write a function as the string $f(1)f(2)f(3)f(4)$. A surjection onto three
    values uses one value twice and the others once. There are $36$:

    aabc aacb abac abbc abca abcb abcc acab acba acbb acbc accb
    baac babc baca bacb bacc bbac bbca bcaa bcab bcac bcba bcca
    caab caba cabb cabc cacb cbaa cbab cbac cbba cbca ccab ccba

    In each, the sets $f^{-1}(a), f^{-1}(b), f^{-1}(c)$ form one of the $6$
    partitions of $\{1,2,3,4\}$ into three parts from Exercise 1.20, and each
    partition arises from $3! = 6$ surjections: $36 = 6\cdot6$.

(b) Send each surjection $f$ to the partition of its preimages:
    $$f\mapsto\bigl\{f^{-1}(a),\ f^{-1}(b),\ f^{-1}(c)\bigr\}.$$
    The three preimages are nonempty because $f$ is a surjection, disjoint,
    and their union is $\{1,2,3,4\}$, so this is a partition into three
    parts. Every such partition arises by assigning $a,b,c$ to its parts, so
    the map is a surjection.

(c) Every preimage has size $6$: the surjections giving a partition are the
    $3!$ ways to assign the labels $a,b,c$ to its three parts.
:::
