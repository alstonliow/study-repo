<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

<!-- Migrated from 1058note exercises/chapters (owner's solutions). -->

::: {.solution for="prob-functions-08"}
**(a)**

#### Setup: grouping by length.

For each $n\ge0$, there are $2^n$
bitstrings of length $n$. We assign each bitstring a natural number
(“index”) as follows:

|  length  |   bitstring   | number of bitstrings | index $\in \mathbb{N}$ |
|:--------:|:-------------:|:--------------------:|:----------------------:|
|   $0$    | $\varepsilon$ |         $1$          |          $0$           |
|   $1$    |     $0,1$     |       $2=2^1$        |         $1,2$          |
|   $2$    | $00,01,10,11$ |        $2^2$         |       $3,4,5,6$        |
| $\vdots$ |   $\vdots$    |       $\vdots$       |        $\vdots$        |
|   $n$    |   $\cdots$    |        $2^n$         |        $\cdots$        |

#### Defining $f_n$.

For $\{0,1\}^n$, the value of a string is a
member of $\{0,1,\dots,2^n-1\}$. Define $f_n$ to be the value of
$\{0,1\}^n$:
$$f_n : \{0,1\}^n \longrightarrow \{0,1,\dots,2^n-1\}, \qquad
    f_n(s) = f_n(s_1 s_2 \cdots s_n) = \sum_{i=1}^n s_i\cdot 2^{n-i}.$$

::: {.claim}

For every $n$, $f_n$ is a bijection.

:::

::: {.proof}

When $n=0$: $f_0:\{\varepsilon\}\to\{0\}$, $f_0(\varepsilon)=0$, is a
bijection.

Assume $f_{n-1}:\{0,1\}^{n-1}\to\{0,\dots,2^{n-1}-1\}$ is a bijection.

For $f_n$,
$$f_n(s_1\cdots s_n) = s_1\cdot 2^{n-1} + \sum_{i=2}^n s_i\cdot 2^{n-i}
        = s_1\cdot 2^{n-1} + f_{n-1}(s_2\cdots s_n).$$

When $s_1=0$: $f_n(s_1\cdots s_n)\in\{0,\dots,2^{n-1}-1\}$.

When $s_1=1$: $f_n(s_1\cdots s_n) \in \{2^{n-1},\dots,2^{n-1}-1+2^{n-1}\}
    = \{2^{n-1},\dots,2^n-1\}$.

We know that $f_n(s_1\cdots s_n)\in\{0,\dots,2^n-1\}$.

By induction, we know that $f_n$ is a bijection.

:::

#### Starting index of each length group.

Observe that, for
length $=n$, the starting index is equal to the number of bitstrings of
length $=0$ to length $=n-1$:
$$\text{starting index} = \sum_{k=0}^{n-1} |\{0,1\}^k| = \sum_{k=0}^{n-1} 2^k
    = \frac{2^n-1}{2-1} = 2^n-1.$$

So, $f : \{0,1\}^* \to \mathbb{N}$ is equal to $(2^n-1) +$ (position of bitstring
in the group of the length):
$$f(s) = (2^n-1) + f_n(s), \qquad n = |s|.$$

::: {.claim}

$f$ is a bijection.

:::

::: {.proof}

We know $f(s) \in \big[\,2^{|s|}-1,\ 2^{|s|+1}-2\,\big]$.

**First, we prove $f$ is injective.**

*Case 1: $s\ne t$ and $|s|\ne|t|$.* Let $|s|<|t|$. Then
$$f(s) \in \big[2^{|s|}-1,\ 2^{|s|+1}-2\big], \qquad
        f(t) \in \big[2^{|t|}-1,\ 2^{|t|+1}-2\big].$$
Since $|s|<|t|$ are integers, $|s|+1\le|t|$, so
$$2^{|s|+1}-2 \le 2^{|t|}-2 < 2^{|t|}-1.$$
So $\big[2^{|s|}-1,\ 2^{|s|+1}-2\big] \cap \big[2^{|t|}-1,\ 2^{|t|+1}-2\big]
    = \varnothing$. Hence $f(t)\ne f(s)$.

*Case 2: $s\ne t$ and $|s|=|t|$.*
$$f_{|s|}(s) \ne f_{|t|}(t) \implies f(s) \ne f(t).$$

By Case 1 and 2, $f$ is injective.

**Now we prove $f$ is surjective**, i.e. need to prove
$\forall m\in\mathbb{N},\ \exists\, s\in\{0,1\}^*,\ f(s)=m$.

We know $f(s) \in \big[2^{|s|}-1,\ 2^{|s|+1}-2\big]$, so we need
$$2^{|s|}-1 \le m \le 2^{|s|+1}-2
        \iff
        2^{|s|} \le m+1 \le 2^{|s|+1}-1
        \iff
        2^{|s|} \le m+1 < 2^{|s|+1}
        \iff
        |s| \le \log_2(m+1) < |s|+1.$$

So let $n = \lfloor \log_2(m+1) \rfloor$. Then
$$2^n \le m+1 < 2^{n+1}
        \implies
        0 \le m - 2^n + 1 < 2^n.$$

So $m-2^n+1 \in [0,2^n) \subseteq [0,2^n-1]$, which is the domain of
$f_n^{-1}$ (i.e., $m-2^n+1$ is in the range of $f_n$).

$f_n$ is surjective, so $\exists\, s\in\{0,1\}^n$ such that
$f_n(s) = m-2^n+1$. Then
$$f(s) = (2^n-1) + f_n(s) = (2^n-1) + (m-2^n+1) = m.$$

We proved that $\forall m\in\mathbb{N}$, $\exists\, s\in\{0,1\}^*$, $f(s)=m$.
So, $f$ is surjective.

Hence, $f$ is a bijection.

:::
:::

::: {.solution for="prob-functions-04" status="draft"}
Every function is a binary relation, and binary and ternary relations are
disjoint kinds of relation. Bijections are the functions that are both
injections and surjections, and identity functions are bijections:

```{=latex}
\begin{tikzpicture}[every node/.style={font=\small}]
  \draw (0,0) rectangle (11,6.4);
  \node[anchor=north west] at (0.1,6.35) {Relations};
  \draw (0.4,0.3) rectangle (2.6,5.6);
  \node[align=center] at (1.5,3) {Ternary\\relations};
  \draw (3,0.3) rectangle (10.7,5.6);
  \node[anchor=north west] at (3.05,5.55) {Binary relations};
  \draw (3.4,0.6) rectangle (10.4,4.9);
  \node[anchor=north west] at (3.45,4.85) {Functions};
  \draw (6.0,2.6) ellipse (2.0 and 1.6);
  \draw (7.8,2.6) ellipse (2.0 and 1.6);
  \node at (4.95,2.6) {Injections};
  \node at (8.85,2.6) {Surjections};
  \node at (6.9,3.15) {Bijections};
  \draw (6.9,2.3) ellipse (0.62 and 0.55);
  \node[align=center, font=\scriptsize] at (6.9,2.3) {Identity\\functions};
\end{tikzpicture}
```

(Other $n$-ary relations, $n\ne2,3$, lie inside "Relations" but outside both
boxes.)
:::

::: {.solution for="prob-functions-07" status="draft"}
Here $\mathbb N = \{0,1,2,\dots\}$.

**Injection.** $f(m,n) = 2^m3^n$. By unique prime factorisation,
$2^m3^n = 2^{m'}3^{n'}$ forces $m = m'$ and $n = n'$.

**Bijection.**
$$g(m,n) = 2^m(2n+1) - 1.$$

1. *Injective.* $g(m,n)+1 = 2^m(2n+1)$. The exponent $m$ is the number of
   factors $2$ in $g(m,n)+1$, and $2n+1$ is its odd part, so both are
   determined by the value.

2. *Surjective.* Let $N\in\mathbb N$. Then $N+1\ge1$ can be written as
   $2^m\cdot q$ with $q$ odd, say $q = 2n+1$. Then $g(m,n) = N$.
:::

::: {.solution for="prob-functions-12" status="draft"}
$f\sqcup g : A\cup C\to B\cup D$ is defined by
$$(f\sqcup g)(x) = \begin{cases} f(x), & x\in A,\\ g(x), & x\in C.\end{cases}$$
This is well defined because $A\cap C = \emptyset$.

1. *Injective.* Let $(f\sqcup g)(x) = (f\sqcup g)(y)$. If $x,y\in A$, then
   $f(x) = f(y)$, so $x = y$. Likewise if $x,y\in C$. If $x\in A$ and $y\in C$,
   the value would lie in $B\cap D = \emptyset$, which is impossible.

2. *Surjective.* Each $b\in B$ is $f(a)$ for some $a\in A$, and each $d\in D$
   is $g(c)$ for some $c\in C$.

3. *Inverse.* By the same construction with the inverses,
   $$(f\sqcup g)^{-1} = f^{-1}\sqcup g^{-1},$$
   which sends $y\in B$ to $f^{-1}(y)$ and $y\in D$ to $g^{-1}(y)$. Checking
   on $A$ and $C$ separately shows both compositions are identities.
:::
