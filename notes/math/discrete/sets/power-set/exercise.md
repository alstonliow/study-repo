<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-sets-04 origin="external" source="fit1058-cn-1.16-q4"}
Consider diagrams of the following type (e.g. for $\{a,b\}$: $\emptyset$ at
the bottom, $\{a\},\{b\}$ in the middle, $\{a,b\}$ at the top). The
requirements are:

- Sets are written in their usual textual form (not Venn diagrams).

- Smaller sets are lower on the page than larger sets; sets of the
  same size are on the same horizontal level.

- If $X\subset Y$ and $|Y|=|X|+1$ then there is an arrow from $X$ to $Y$.

- The diagram is as neat and symmetric as possible.

(a) Draw a diagram of this type that shows all subsets of $\{a,b,c\}$
    and the subset relation among them.

(b) For every pair $X,Y$ with $X\subset Y$ and $|Y|=|X|+1$, label the
    corresponding arrow by the sole member of $Y\setminus X$.

(c) If you could draw in three dimensions, how could you draw this
    diagram in a natural way?

(d) For a set of $n$ elements, how many sets and how many arrows does a
    diagram of this type have?

(e) For each element of the $n$-element set in (d), how many arrows are
    labelled by that element?

(f) Suppose $X\subseteq Y$. How many directed paths (along arrows,
    forwards only) are there from $X$ to $Y$? Give an expression.

(g) With $X,Y$ as in (f), what is the maximum number of mutually
    internally disjoint paths from $X$ to $Y$? (Two paths are
    internally disjoint if no internal set on either path appears
    anywhere on the other path.)

(h) Explain how to use the diagram to find, for any two sets in it,
    their union and intersection.
:::

::: {.problem #prob-sets-05 origin="external" source="fit1058-cn-1.16-q5"}
Given $U=\{e_1,e_2,\dots,e_n\}$, the *characteristic string* of a subset
$A\subseteq U$ is the $n$-bit string $b_1b_2\cdots b_n$ where
$$b_i = \begin{cases} 1, & e_i\in A;\\ 0, & e_i\notin A.\end{cases}$$
Write down the characteristic string of each of the subsets of a set of three
elements. List them, one above the other, so that each differs from the one
above it in just one bit. See if you can extend this to subsets of a set of
$n$ elements.
:::

::: {.problem #prob-sets-07 origin="external" source="fit1058-cn-1.16-q7"}
Prove that if $A\subseteq B$ then $\mathcal{P}(A)\subseteq\mathcal{P}(B)$.
:::

::: {.problem #prob-sets-08 origin="external" source="fit1058-cn-1.16-q8"}
Consider the sequence of binomial coefficients
$\binom n0,\binom n1,\binom n2,\dots,\binom n{n-1},\binom nn$.

(a) Using one of the formulas for $\binom nr$, prove that these
    binomial coefficients increase as $r$ goes from $0$ to
    $\lfloor n/2\rfloor$ and then decrease as $r$ goes from
    $\lceil n/2\rceil$ to $n$. (In the odd case, what happens when $r$
    goes from $(n-1)/2$ to $(n+1)/2$?)

(b) Prove that, for every integer $r$ with $1\le r\le n-1$,
    $$\binom nr^2 > \binom n{r-1}\binom n{r+1}.$$
    (The sequence is *strictly log-concave*.)

(c) You choose an ordered pair of subsets of size $r$ of a set of size
    $n$ (no other restriction). Your friend chooses one subset of size
    $r-1$ and another of size $r+1$. Who has more options? Does the
    answer depend on $n$ and $r$? Is there any situation where the
    numbers of choices are the same?
:::
