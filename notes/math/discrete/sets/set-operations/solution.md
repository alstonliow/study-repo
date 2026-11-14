<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-sets-01" status="draft"}
The formula $|B\setminus A| = |B|-|A|$ assumes that every element of $A$ is
removed from $B$. That is only true when every element of $A$ is in $B$, that
is, when $A\subseteq B$.

For example, take $A=\{1,5\}$ and $B=\{1,2,3\}$. Then
$|B\setminus A| = |\{2,3\}| = 2$, but $|B|-|A| = 3-2 = 1$. The element $5$ was
subtracted although it was never in $B$.

The elements actually removed from $B$ are those in $A\cap B$. So in general
$$|B\setminus A| = |B| - |A\cap B|.$$

To find $|B\setminus A|$ we therefore need $|B|$ and $|A\cap B|$ (or any data
from which $|A\cap B|$ can be found, such as $|A|$ and $|A\cup B|$).
When $A\subseteq B$ we have $A\cap B = A$, and the formula reduces to the
original one.
:::

::: {.solution for="prob-sets-03" status="draft"}
(a) $A\cup B = B$. Every element of $A$ is already in $B$.

(b) $A\cup B \ne B$: some element of $A$ is not in $B$, and it is in
    $A\cup B$. So $B$ is a proper subset of $A\cup B$.

(c) $A\subseteq B$ if and only if $A\cup B = B$.
    This follows from (a) and (b).

(d) $A\subseteq B$ if and only if $A\cap B = A$.

    If $A\subseteq B$, every element of $A$ is in both sets, so $A\cap B = A$.
    If $A\not\subseteq B$, some element of $A$ is missing from $A\cap B$, so
    $A\cap B\ne A$.

(e) $A\subseteq B$ if and only if $A\setminus B = \emptyset$.

    $A\setminus B$ consists exactly of the elements of $A$ that are not in
    $B$, and $A\subseteq B$ says there are none.
:::

::: {.solution for="prob-sets-06" status="draft"}
(a) Each region is an intersection of $A$ or $\overline A$, $B$ or
    $\overline B$, and $C$ or $\overline C$:

```{=latex}
\begin{tikzpicture}[scale=1.5, every node/.style={font=\scriptsize}]
  \draw (0,0) circle (1.3);
  \draw (1.5,0) circle (1.3);
  \draw (0.75,-1.3) circle (1.3);
  \draw (-1.6,-2.9) rectangle (3.1,1.75);
  \node at (-0.65,1.45) {$A$};
  \node at (2.15,1.45) {$B$};
  \node at (0.75,-2.75) {$C$};
  \node at (-0.45,0.25) {$A\cap\overline B\cap\overline C$};
  \node at (1.95,0.25) {$\overline A\cap B\cap\overline C$};
  \node at (0.75,-1.85) {$\overline A\cap\overline B\cap C$};
  \node at (0.75,0.65) {$A\cap B\cap\overline C$};
  \node[align=center] at (-0.15,-0.95) {$A\cap\overline B$\\$\cap\, C$};
  \node[align=center] at (1.65,-0.95) {$\overline A\cap B$\\$\cap\, C$};
  \node at (0.75,-0.45) {$A\cap B\cap C$};
  \node at (2.3,-2.6) {$\overline A\cap\overline B\cap\overline C$};
\end{tikzpicture}
```

(b) Three. The usual diagram of three equal circles is a general Venn diagram.

    For four circles: two circles meet in at most two points, so four circles
    have at most $2\binom42 = 12$ crossing points. Each circle is cut into at
    most $6$ arcs, giving at most $24$ edges. By Euler's formula the number of
    regions (including the outside) is at most $24 - 12 + 2 = 14 < 16 = 2^4$.
    So no four circles, of any sizes, give a general Venn diagram.

(c) Use four congruent ellipses. Two are tilted one way and two the other, and
    each pair overlaps so that all $16$ regions appear:

```{=latex}
\begin{tikzpicture}[scale=0.85]
  \draw[rotate around={45:(-0.6,0)}]   (-0.6,0)   ellipse (2.4 and 1.1);
  \draw[rotate around={45:(-0.6,1.5)}] (-0.6,1.5) ellipse (2.4 and 1.1);
  \draw[rotate around={-45:(0.6,1.5)}] (0.6,1.5)  ellipse (2.4 and 1.1);
  \draw[rotate around={-45:(0.6,0)}]   (0.6,0)    ellipse (2.4 and 1.1);
  \node at (-2.75,-2.05) {$A_1$};
  \node at (-2.75,-0.15) {$A_2$};
  \node at (2.75,-0.15) {$A_3$};
  \node at (2.75,-2.05) {$A_4$};
\end{tikzpicture}
```

(d) Place the centres of four equal spheres at the vertices of a regular
    tetrahedron, with the radius a little larger than the edge length of the
    tetrahedron. This is the three-dimensional analogue of three circles
    centred at the vertices of an equilateral triangle. Every one of the $16$
    combinations "inside or outside each sphere" then occurs in some region of
    space.
:::

::: {.solution for="prob-sets-09" status="draft"}
$$|A\cup B| = |A| + |B| - |A\cap B|.$$

$|A|+|B|$ counts every element of $A\cap B$ twice, so we subtract it once.
:::

::: {.solution for="prob-sets-10" status="draft"}
Rearranging the answer to Exercise 9:
$$|A\cap B| = |A| + |B| - |A\cup B|.$$
:::

::: {.solution for="prob-sets-11" status="draft"}
$$|A\cup B\cup C| = |A|+|B|+|C| - |A\cap B| - |A\cap C| - |B\cap C| + |A\cap B\cap C|.$$

1. Write $A\cup B\cup C = (A\cup B)\cup C$ and apply Exercise 9:
   $$|A\cup B\cup C| = |A\cup B| + |C| - |(A\cup B)\cap C|.$$

2. By the distributive law, $(A\cup B)\cap C = (A\cap C)\cup(B\cap C)$, so by
   Exercise 9 again
   $$|(A\cup B)\cap C| = |A\cap C| + |B\cap C| - |A\cap B\cap C|.$$

3. Substitute this and $|A\cup B| = |A|+|B|-|A\cap B|$ into step 1.
:::

::: {.solution for="prob-sets-12" status="draft"}
$$|A\cap B\cap C| = |A|+|B|+|C| - |A\cup B| - |A\cup C| - |B\cup C| + |A\cup B\cup C|.$$

1. By Exercise 10, $|A\cap B| = |A|+|B|-|A\cup B|$, and similarly for the
   other two pairs. Adding the three equations:
   $$|A\cap B|+|A\cap C|+|B\cap C| = 2(|A|+|B|+|C|) - (|A\cup B|+|A\cup C|+|B\cup C|).$$

2. Rearrange Exercise 11 to isolate the triple intersection:
   $$|A\cap B\cap C| = |A\cup B\cup C| - (|A|+|B|+|C|) + (|A\cap B|+|A\cap C|+|B\cap C|).$$

3. Substitute step 1 into step 2 and collect terms.
:::

::: {.solution for="prob-sets-13" status="draft"}
For two and three sets, Exercises 9 and 11 become
$$|A\cup B| = i_1 - i_2,\qquad |A\cup B\cup C| = i_1 - i_2 + i_3.$$

In general (the inclusion–exclusion principle):
$$|A_1\cup\cdots\cup A_n| = i_1 - i_2 + i_3 - \cdots + (-1)^{n-1} i_n
  = \sum_{k=1}^{n} (-1)^{k-1} i_k.$$

The last term is $+i_n$ when $n$ is odd and $-i_n$ when $n$ is even.
:::

::: {.solution for="prob-sets-14" status="draft"}
For two and three sets, Exercises 10 and 12 become
$$|A\cap B| = u_1 - u_2,\qquad |A\cap B\cap C| = u_1 - u_2 + u_3.$$

In general:
$$|A_1\cap\cdots\cap A_n| = \sum_{k=1}^{n} (-1)^{k-1} u_k,$$
with last term $(-1)^{n-1}u_n$, exactly as in Exercise 13.

One way to prove it:

1. Let $U = A_1\cup\cdots\cup A_n$ and take complements inside $U$. By
   De Morgan's law,
   $$A_1\cap\cdots\cap A_n = U\setminus(\overline{A_1}\cup\cdots\cup\overline{A_n}).$$

2. An intersection of $k$ complements is the complement of a union of $k$ of
   the sets, so its size is $|U|$ minus the size of that union. Summing over
   all choices of $k$ sets gives $\binom nk|U| - u_k$.

3. Apply Exercise 13 to the complements:
   $$\Bigl|\bigcup_j \overline{A_j}\Bigr| = \sum_{k=1}^n (-1)^{k-1}\Bigl(\binom nk |U| - u_k\Bigr)
     = |U| - \sum_{k=1}^n (-1)^{k-1}u_k,$$
   since $\sum_{k=1}^n (-1)^{k-1}\binom nk = 1$.

4. Subtract this from $|U|$, using step 1.
:::

::: {.solution for="prob-sets-21" status="draft"}
The eight parts are the basic regions of the Venn diagram, one for each choice
of "in" or "out" for each of the three sets:

- $A\cap B\cap C$
- $A\cap B\cap\overline C$
- $A\cap\overline B\cap C$
- $\overline A\cap B\cap C$
- $A\cap\overline B\cap\overline C$
- $\overline A\cap B\cap\overline C$
- $\overline A\cap\overline B\cap C$
- $\overline A\cap\overline B\cap\overline C$

Every element of $U$ is in exactly one of these, because each element is
either in or out of each set. The assumption that all basic regions are
nonempty makes every part nonempty, as a partition requires.
:::
