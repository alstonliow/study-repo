<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-sets-15" status="draft"}
$A\triangle B$ is the set of elements in exactly one of $A$ and $B$. Three ways:
$$|A\triangle B| = |A\cup B| - |A\cap B|,$$
$$|A\triangle B| = |A| + |B| - 2|A\cap B|,$$
$$|A\triangle B| = |A\setminus B| + |B\setminus A|.$$

The first holds because $A\triangle B = (A\cup B)\setminus(A\cap B)$ and
$A\cap B\subseteq A\cup B$. The second follows from the first using
$|A\cup B| = |A|+|B|-|A\cap B|$. The third holds because $A\setminus B$ and
$B\setminus A$ are disjoint and their union is $A\triangle B$.
:::

::: {.solution for="prob-sets-16" status="draft"}
An element is in $A\triangle B\triangle C$ exactly when it is in an odd number
of the three sets (see Exercise 18). So the shaded regions are the three
"only one set" regions and the centre:

```{=latex}
\begin{tikzpicture}[scale=1.1]
  \fill[gray!35, even odd rule] (0,0) circle (1.2) (1.4,0) circle (1.2) (0.7,-1.2) circle (1.2);
  \draw (0,0) circle (1.2);
  \draw (1.4,0) circle (1.2);
  \draw (0.7,-1.2) circle (1.2);
  \draw (-1.7,-2.7) rectangle (3.1,1.6);
  \node at (-0.85,1.25) {$A$};
  \node at (2.25,1.25) {$B$};
  \node at (0.7,-2.55) {$C$};
\end{tikzpicture}
```
:::

::: {.solution for="prob-sets-17" status="draft"}
1. Let $x$ be any element. By definition, $x\in(A\cup B)\triangle(A\cap B)$
   if and only if $x$ is in exactly one of $A\cup B$ and $A\cap B$.

2. Since $A\cap B\subseteq A\cup B$, $x$ cannot be in $A\cap B$ without
   being in $A\cup B$. So "exactly one of them" means $x\in A\cup B$ and
   $x\notin A\cap B$.

3. That says $x$ is in at least one of $A$, $B$ but not in both, that is,
   in exactly one of $A$ and $B$.

4. This is the definition of $x\in A\triangle B$. Both sets have the same
   elements, so they are equal.
:::

::: {.solution for="prob-sets-18" status="draft"}
$A_1\triangle A_2\triangle\cdots\triangle A_n$ consists of the elements that
belong to an **odd number** of the sets $A_1,\dots,A_n$.

Proof by induction on $n$.

1. *Base case $n=1$.* The expression is $A_1$, and an element belongs to an
   odd number of the sets $\{A_1\}$ exactly when it is in $A_1$.

2. *Inductive step.* Assume the claim for $n-1$ sets, and let
   $S = A_1\triangle\cdots\triangle A_{n-1}$. Then the expression for $n$
   sets is $S\triangle A_n$.

3. Let $m$ be the number of the sets $A_1,\dots,A_{n-1}$ containing $x$. By
   the assumption, $x\in S$ if and only if $m$ is odd.

4. $x\in S\triangle A_n$ if and only if exactly one of "$m$ is odd" and
   "$x\in A_n$" holds. In both cases this means the total count
   $m + [x\in A_n]$ is odd.
:::
