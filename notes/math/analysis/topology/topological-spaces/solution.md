<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-ats-3-q7" status="draft"}
(a) Let $x_n \to x$ and let $V$ be an open set containing $f(x)$. Then $f^{-1}(V)$ is open and contains $x$, so $x_n \in f^{-1}(V)$ for large $n$, that is, $f(x_n) \in V$. So $f(x_n) \to f(x)$.

(b) Let $X$ be an uncountable set with the co-countable topology, $Y$ the same set with the discrete topology, and $f$ the identity.

1. In $X$, convergent sequences are eventually constant (question 6(a)), so $f$ is sequentially continuous.

2. $\{p\}$ is open in $Y$, but $f^{-1}(\{p\}) = \{p\}$ is not open in $X$, as its complement is uncountable. So $f$ is not continuous.

(c)

1. Let $C \subset Y$ be closed. Then $f^{-1}(C)$ is sequentially closed: if $x_n \in f^{-1}(C)$ and $x_n \to x$, then $f(x_n) \to f(x)$ with $f(x_n) \in C$, and $C$ is sequentially closed (question 6(b), step 1), so $f(x) \in C$.

2. $X$ is second countable, so by question 6(b) $f^{-1}(C)$ is closed. Hence $f$ is continuous.
:::
