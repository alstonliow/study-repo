<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-sets-20" status="draft"}
Three parts with four elements in total means one part has two elements and
the other two parts are singletons. The partition is fixed by the pair, so
there are $\binom42 = 6$ partitions:

- $\{\{1,2\},\{3\},\{4\}\}$
- $\{\{1,3\},\{2\},\{4\}\}$
- $\{\{1,4\},\{2\},\{3\}\}$
- $\{\{2,3\},\{1\},\{4\}\}$
- $\{\{2,4\},\{1\},\{3\}\}$
- $\{\{3,4\},\{1\},\{2\}\}$
:::

::: {.solution for="prob-sets-22" status="draft"}
(a) Only the trivial partition $\{\mathbb R\}$, with
    $\mathbb R = (-\infty,\infty)$ as its single part.

    1. Suppose some part is an open interval $I\ne\mathbb R$. Then $I$ has
       an endpoint $a\in\mathbb R$, and $a\notin I$ because $I$ is open.

    2. Some other part $J$ contains $a$. Since $J$ is open, it contains an
       interval $(a-\varepsilon, a+\varepsilon)$.

    3. This interval contains points of $I$ that are close to $a$. So
       $I\cap J\ne\emptyset$, which is impossible in a partition.

(b) Yes. For example,
    $$\{[n, n+1) : n\in\mathbb Z\}.$$
    Every real $x$ lies in exactly one of these, namely the one with
    $n = \lfloor x\rfloor$.

(c) Yes, if one-point intervals $[a,a] = \{a\}$ are allowed:
    $\{\{a\} : a\in\mathbb R\}$ is a partition of $\mathbb R$ into closed
    intervals.

    If every part must be a closed interval $[a,b]$ with $a<b$, then the
    answer is no.

    1. Each such interval contains a rational number, and the parts are
       disjoint. So there are only countably many parts.

    2. There are at least two parts, because $\mathbb R$ is not a bounded
       interval.

    3. Sierpiński's theorem says that $\mathbb R$ cannot be written as a
       union of countably many (at least two) pairwise disjoint nonempty
       closed sets. So no such partition exists.
:::
