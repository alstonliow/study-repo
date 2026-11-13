<!-- Migrated from 1058note exercises/chapters (owner's solutions). -->

::: {.solution for="prob-functions-01"}
An indicator function is defined by
$$\chi_A(x) = \begin{cases} 1 & \text{if } x\in A \\
            0 & \text{if } x\notin A \end{cases}$$

Let $|A|=n$. The number of functions $\chi: A\to\{0,1\}$ equals
the number of ways to independently assign each of the $n$
elements of $A$ a value in $\{0,1\}$, which is $2^n$.

Equivalently, each such function corresponds to exactly one
subset $X\subseteq A$ (namely $X=\{x\in A : \chi(x)=1\}$), so the
number of indicator functions equals $|\mathcal P(A)| = 2^n$.
:::

::: {.solution for="prob-functions-02"}
**(a)**
$$\chi_{\overline A}(x) = 1-\chi_A(x).$$

**(b)** $x\in A\cap B \iff x\in A \wedge x\in B$, so
$$\chi_{A\cap B} = \chi_A\cdot\chi_B.$$

**(c)** $x\in A\setminus B \iff x\in A \wedge x\notin B$, so
$$\chi_{A\setminus B} = \chi_A\cdot\chi_{\overline B}
        = \chi_A\cdot(1-\chi_B) = \chi_A - \chi_A\chi_B.$$

**(d)** Since $A\triangle B = (A\setminus B)\cup(B\setminus
    A)$ is a disjoint union,
$$\chi_{A\triangle B} = \chi_{A\setminus B}+\chi_{B\setminus A}
        = (\chi_A-\chi_A\chi_B)+(\chi_B-\chi_A\chi_B)
        = \chi_A+\chi_B-2\chi_A\chi_B.$$
:::

::: {.solution for="prob-functions-03"}
::: {.proof}

Let $A$ be a finite set with $|A|=n$. Since function addition is
defined pointwise, for any $x_i\in A$,
$$\left(\sum_{X\subseteq A}\chi_X\right)(x_i)
        = \sum_{X\subseteq A}\chi_X(x_i).$$

Since $\chi_X(x_i)=1$ if $x_i\in X$ and $0$ otherwise, this sum
counts the number of subsets $X\subseteq A$ containing $x_i$.

**Method 1 (direct count).** A subset containing $x_i$ is
formed by fixing $x_i$ to be included, and choosing freely,
independently, whether each of the remaining $n-1$ elements is
included. This gives $2^{n-1}$ such subsets.

**Method 2 (summing over subset sizes).** For each size
$k=1,\dots,n$, the number of size-$k$ subsets containing $x_i$ is
obtained by fixing $x_i$ as one member and choosing the
remaining $k-1$ members from the other $n-1$ elements:
$\binom{n-1}{k-1}$. Summing over all sizes,
$$\sum_{X\subseteq A}\chi_X(x_i)
        = \sum_{k=1}^{n}\binom{n-1}{k-1}
        = \sum_{j=0}^{n-1}\binom{n-1}{j} = 2^{n-1},$$
using the binomial identity $\sum_{j=0}^{m}\binom{m}{j}=2^m$
with $m=n-1$.

Both methods agree: $\left(\sum_{X\subseteq A}\chi_X\right)(x_i)
    = 2^{n-1}$ for every $x_i\in A$, independent of which $x_i$ is
chosen. So $\sum_{X\subseteq A}\chi_X$ is the constant function
on $A$ with value $2^{n-1}$.

:::
:::
