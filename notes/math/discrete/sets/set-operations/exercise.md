<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-sets-01 origin="external" source="fit1058-cn-1.16-q1"}
Why does the set difference only satisfy (1.9) $\bigl(|B\setminus A| = |B|-|A|\bigr)$
when $A\subseteq B$? How would you modify (1.9) so that it covers any set
difference $B\setminus A$? What extra information about the sets would you
need, in order to determine $|B\setminus A|$?
:::

::: {.problem #prob-sets-03 origin="external" source="fit1058-cn-1.16-q3"}
Suppose $A$ and $B$ are subsets of some universal set $U$.

(a) If $A\subseteq B$, what is $A\cup B$?

(b) If $A\not\subseteq B$, what can you say about $A\cup B$?

(c) Complete the following: $A\subseteq B$ if and only if
    $A\cup B = \underline{\hspace{2cm}}$.

(d) Devise another equivalent condition for $A\subseteq B$ involving
    intersection instead of union.

(e) Devise another equivalent condition for $A\subseteq B$ involving
    set difference.
:::

::: {.problem #prob-sets-06 origin="external" source="fit1058-cn-1.16-q6"}
Two intersecting sets $A,B$ divide the plane into four basic regions:
$\overline{A\cup B}$, $A\cap B$, $A\setminus B$, $B\setminus A$. Three sets
can divide the plane into eight regions.

(a) Label each basic region of a Venn diagram for three sets $A,B,C$
    with appropriate intersections of sets.

A *general Venn diagram* for $n$ sets $A_1,\dots,A_n$ is one in which
every intersection of the form
$$(A_1 \text{ or } \overline{A_1})\cap(A_2\text{ or }\overline{A_2})\cap\cdots
        \cap(A_n\text{ or }\overline{A_n})$$
corresponds to one of the basic regions, so there are $2^n$ basic regions.

(b) What is the maximum number of sets for which a general Venn diagram
    can be drawn in which all the sets are circles of the same size?

(c) Draw a general Venn diagram in the plane for four sets. You can use
    closed curves other than circles.

(d) How could you draw a three-dimensional general Venn diagram using
    four sets, each represented as a sphere?
:::

::: {.problem #prob-sets-09 origin="external" source="fit1058-cn-1.16-q9"}
Express $|A\cup B|$ in terms of $|A|,|B|,|A\cap B|$.
:::

::: {.problem #prob-sets-10 origin="external" source="fit1058-cn-1.16-q10"}
Express $|A\cap B|$ in terms of $|A|,|B|,|A\cup B|$.
:::

::: {.problem #prob-sets-11 origin="external" source="fit1058-cn-1.16-q11"}
Express $|A\cup B\cup C|$ in terms of
$|A|,|B|,|C|,|A\cap B|,|A\cap C|,|B\cap C|,|A\cap B\cap C|$.
:::

::: {.problem #prob-sets-12 origin="external" source="fit1058-cn-1.16-q12"}
Express $|A\cap B\cap C|$ in terms of
$|A|,|B|,|C|,|A\cup B|,|A\cup C|,|B\cup C|,|A\cup B\cup C|$.
:::

::: {.problem #prob-sets-13 origin="external" source="fit1058-cn-1.16-q13"}
Suppose we have sets $A_1,\dots,A_n$. For each $k$, let
$$i_k := \text{sum of all sizes of intersections of $k$ of the sets.}$$
E.g. for $n=3$: $i_1=|A_1|+|A_2|+|A_3|$,
$i_2=|A_1\cap A_2|+|A_1\cap A_3|+|A_2\cap A_3|$, $i_3=|A_1\cap A_2\cap A_3|$.

Rewrite your expressions for $|A\cup B|$ and $|A\cup B\cup C|$ in terms of
$i_1,i_2,\dots$. Then write out a general expression for
$|A_1\cup\cdots\cup A_n|$. Pay careful attention to the sign of the last term.
:::

::: {.problem #prob-sets-14 origin="external" source="fit1058-cn-1.16-q14"}
Now let
$$u_k := \text{sum of all sizes of unions of $k$ of the sets.}$$
Rewrite your expressions for $|A\cap B|$ and $|A\cap B\cap C|$ in terms of
$u_1,u_2,\dots$. Then write out a general expression for
$|A_1\cap\cdots\cap A_n|$. Pay careful attention to the sign of the last term.
:::

::: {.problem #prob-sets-21 origin="external" source="fit1058-cn-1.16-q21"}
Suppose $A,B,C\subseteq U$ are nonempty sets such that all basic regions in
their general Venn diagram are nonempty (see Exercise 6). Then $A,B,C$ define
a partition of $U$ into eight parts. What are those parts? Express each part
in terms of one or more of $A,B,C$ using set operations.
:::
