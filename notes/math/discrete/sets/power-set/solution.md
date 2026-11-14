<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-sets-04" status="draft"}
(a) and (b) Each arrow is labelled by the element it adds:

```{=latex}
\begin{tikzpicture}[x=1.9cm, y=1.5cm, every node/.style={font=\small},
    lab/.style={font=\scriptsize, fill=white, inner sep=1pt}]
  \node (e)   at (0,0) {$\emptyset$};
  \node (a)   at (-1,1) {$\{a\}$};
  \node (b)   at (0,1)  {$\{b\}$};
  \node (c)   at (1,1)  {$\{c\}$};
  \node (ab)  at (-1,2) {$\{a,b\}$};
  \node (ac)  at (0,2)  {$\{a,c\}$};
  \node (bc)  at (1,2)  {$\{b,c\}$};
  \node (abc) at (0,3)  {$\{a,b,c\}$};
  \foreach \s/\t/\l/\p in {e/a/a/0.5, e/b/b/0.5, e/c/c/0.5,
      a/ab/b/0.5, a/ac/c/0.3, b/ab/a/0.3, b/bc/c/0.3, c/ac/a/0.3, c/bc/b/0.5,
      ab/abc/c/0.5, ac/abc/b/0.5, bc/abc/a/0.5}
    \draw[-{Stealth[length=4pt]}] (\s) -- node[lab, pos=\p] {$\l$} (\t);
\end{tikzpicture}
```

(c) As a cube. Put $\emptyset$ at one corner and $\{a,b,c\}$ at the opposite
    corner. Each of the three directions of the edges corresponds to adding
    one of $a$, $b$, $c$. The corner $(x_a,x_b,x_c)\in\{0,1\}^3$ is the set of
    elements whose coordinate is $1$.

(d) There are $2^n$ sets, one for each subset.

    Each set $X$ with $|X| = k$ has $n-k$ arrows leaving it, one for each
    element not in $X$. Counting the arrows by the element they add instead:
    an arrow labelled $x$ goes from a set $X$ with $x\notin X$ to
    $X\cup\{x\}$, and there are $2^{n-1}$ such $X$. So there are
    $$n\cdot 2^{n-1}$$
    arrows.

(e) $2^{n-1}$ arrows for each element, as shown in (d).

(f) Let $k = |Y\setminus X|$. A directed path from $X$ to $Y$ adds the
    elements of $Y\setminus X$ one at a time, and every order gives a
    different path. So there are $k!$ paths.

(g) Let $k = |Y\setminus X|$. If $k=0$ the only path is $X$ itself. If
    $k\ge 1$ the maximum is $k$.

    1. *At most $k$.* Each path starts with an arrow from $X$ to
       $X\cup\{x\}$ for some $x\in Y\setminus X$. If $k\ge 2$ the set
       $X\cup\{x\}$ is internal, so two internally disjoint paths must start
       with different elements. There are only $k$ choices.

    2. *At least $k$.* Write $Y\setminus X = \{x_1,\dots,x_k\}$. For each
       $j$, let path $P_j$ add the elements in the cyclic order
       $x_j, x_{j+1}, \dots, x_k, x_1, \dots, x_{j-1}$.

    3. After $t$ steps (with $1\le t\le k-1$), path $P_j$ has added a block
       of $t$ cyclically consecutive elements starting at $x_j$. Different
       starting points give different blocks, because $t < k$. So no internal
       set is shared by two paths.

(h) The union $X\cup Y$ is the lowest set that can be reached from both $X$
    and $Y$ by going up along arrows. The intersection $X\cap Y$ is the
    highest set from which both $X$ and $Y$ can be reached by going up.
:::

::: {.solution for="prob-sets-05" status="draft"}
For a three-element set, the following list changes one bit at a time:
$$000,\ 001,\ 011,\ 010,\ 110,\ 111,\ 101,\ 100.$$

This is a *Gray code*. It extends to any $n$ by reflection:

1. For $n=1$ the list is $0,\ 1$.

2. Given a list $L$ for $n-1$ bits, form the list for $n$ bits by writing
   $L$ with a $0$ in front, followed by $L$ in reverse order with a $1$ in
   front.

3. Within each half, consecutive strings differ in one bit because $L$ does.
   At the join, the two strings are the last string of $L$ with $0$ and then
   $1$ in front, so they differ only in the first bit.

The list for $n=3$ above is obtained this way from $00,\ 01,\ 11,\ 10$.
:::

::: {.solution for="prob-sets-07" status="draft"}
1. Assume $A\subseteq B$, and let $X\in\mathcal{P}(A)$. We show
   $X\in\mathcal{P}(B)$.

2. By definition of the power set, $X\subseteq A$.

3. Let $x\in X$. Then $x\in A$ by step 2, and $x\in B$ since $A\subseteq B$.
   So $X\subseteq B$.

4. Hence $X\in\mathcal{P}(B)$. Since $X$ was arbitrary,
   $\mathcal{P}(A)\subseteq\mathcal{P}(B)$.
:::

::: {.solution for="prob-sets-08" status="draft"}
(a) Compare consecutive terms using $\binom nr = \frac{n!}{r!\,(n-r)!}$:
    $$\frac{\binom n{r+1}}{\binom nr} = \frac{n-r}{r+1}.$$

    1. This ratio is greater than $1$ exactly when $n-r > r+1$, that is,
       when $r < \frac{n-1}{2}$. So the terms increase while $r$ goes up to
       $\lfloor n/2\rfloor$.

    2. The ratio is less than $1$ exactly when $r > \frac{n-1}{2}$, so the
       terms decrease from $\lceil n/2\rceil$ on.

    3. If $n$ is odd and $r = \frac{n-1}{2}$, the ratio is exactly $1$. The
       two middle terms $\binom n{(n-1)/2}$ and $\binom n{(n+1)/2}$ are
       equal.

(b) Let $1\le r\le n-1$, so all three coefficients are positive. Using the
    ratio from (a) twice:
    $$\frac{\binom nr^2}{\binom n{r-1}\binom n{r+1}}
      = \frac{\binom nr}{\binom n{r-1}}\cdot\frac{\binom nr}{\binom n{r+1}}
      = \frac{n-r+1}{r}\cdot\frac{r+1}{n-r}.$$

    Both factors are greater than the corresponding factors of
    $\frac{n-r}{r}\cdot\frac{r}{n-r} = 1$, since $n-r+1 > n-r$ and
    $r+1 > r$. So the ratio is greater than $1$, which proves the
    inequality.

(c) You have $\binom nr^2$ options and your friend has
    $\binom n{r-1}\binom n{r+1}$. For $1\le r\le n-1$, part (b) shows that you
    always have strictly more, whatever $n$ and $r$ are, so the numbers are
    never equal.

    For $r=0$ or $r=n$, your friend has no options at all, since there is no
    subset of size $-1$ or $n+1$, while you have exactly one.
:::
