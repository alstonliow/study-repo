<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-functions-21 origin="external" source="fit1058-cn-2.19-q21"}
What can you say about the transitive closure of an equivalence relation?
:::

::: {.problem #prob-functions-22 origin="external" source="fit1058-cn-2.19-q22"}
The *anagram* relation on English words: $(x_1\cdots x_m,\,y_1\cdots
    y_n)$ belongs to it iff there exists a bijection
$f:\{1,\dots,m\}\to\{1,\dots,n\}$ such that $x_i=y_{f(i)}$ for all $i$.

(a) Find the largest set of three-letter words you can that are all
    related to each other by anagram.

(b) For each $k=1,2,3,4$, find an English word of length $k$ that is
    not related to any other word by anagram.

(c) Prove that anagram is an equivalence relation.

(d) (Programming challenge) Using a standard open-access list of
    English words, determine the number of equivalence classes of
    anagram on that list.
:::

::: {.problem #prob-mit6042f10-6-q1 origin="external" source="mit6042f10-6-q1"}
For each of the following, either prove that it is an equivalence relation and state its equivalence classes, or give an example of why it is not an equivalence relation.

(a) $R_n := \{(x, y) \in \mathbb{Z} \times \mathbb{Z} \text{ s.t. } x \equiv y \pmod n\}$

(b) $R := \{(x, y) \in P \times P \text{ s.t. } x \text{ is taller than } y\}$ where $P$ is the set of all people in the world today.

(c) $R := \{(x, y) \in \mathbb{Z} \times \mathbb{Z} \text{ s.t. } \gcd(x, y) = 1\}$

(d) $R_G :=$ the set of $(x, y) \in V \times V$ such that $V$ is the set of vertices of a graph $G$, and there is a path $x, v_1, \ldots, v_k, y$ from $x$ to $y$ along the edges of $G$.
:::
