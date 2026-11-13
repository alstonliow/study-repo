<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-proofs-02 origin="external" source="fit1058-cn-3.15-q2"}
A set of strings $L$ is *hereditary* if: for every nonempty string $x$
in $L$, there is a character in $x$ which can be deleted from $x$ to give
another string in $L$. Prove by contradiction that every nonempty hereditary
set of strings contains the empty string.
:::

::: {.problem #prob-proofs-04 origin="external" source="fit1058-cn-3.15-q4"}
Review the proofs of all the theorems in the previous chapters.

(a) Which ones use proof by construction?

(b) Which ones prove an implication by proving its contrapositive?

(c) Which ones use proof by cases?
:::

::: {.problem #prob-proofs-05 origin="external" source="fit1058-cn-3.15-q5"}
Let $E$ be a finite set and $\mathcal{I}$ a collection of subsets of $E$ satisfying:

- (I1) $\emptyset\in\mathcal{I}$.

- (I2) (hereditary) Whenever $X\subseteq Y$ and $Y\in\mathcal{I}$, we also
  have $X\in\mathcal{I}$.

- (I3) (independence augmentation) Whenever $X,Y\in\mathcal{I}$ and
  $|X|<|Y|$, there exists $y\in Y\setminus X$ such that
  $X\cup\{y\}\in\mathcal{I}$.

The sets in $\mathcal{I}$ are called *independent*. E.g. for $E=\{a,b,c\}$, each
of the following satisfies (I1)–(I3):
$\{\emptyset,\{a\},\{b\},\{a,b\}\}$;
$\{\emptyset,\{a\},\{b\},\{c\}\}$;
$\{\emptyset,\{a\},\{b\},\{c\},\{a,c\},\{b,c\}\}$;
$\{\emptyset,\{a\},\{b\},\{c\},\{a,b\},\{a,c\},\{b,c\}\}$;
$\{\emptyset\}$.
Counterexamples:
$\{\{a\},\{b\},\{a,b\}\}$ fails (I1), (I2);
$\{\emptyset,\{a\},\{a,b\}\}$ fails (I2);
$\{\emptyset,\{a\},\{b\},\{c\},\{a,b\}\}$ fails (I3);
$\emptyset$ fails (I1).

(a) For each counterexample above that fails (I2) and/or (I3), give
    specific sets $X$ and $Y$ for which the property fails.

(b) Prove that, for a social network, the set of cliques satisfies (I1)
    and (I2) but not, in general, (I3).

(c) Prove by contradiction that all maximal independent sets have the
    same size.

Now give each $e\in E$ a weight $w(e)\ge0$, and define
$w(X):=\sum_{e\in X}w(e)$. We seek an independent set of maximum weight
using the *greedy algorithm*:

> $X:=\emptyset$, $i:=1$.\
> Repeat: if there exists $y\in E\setminus X$ with $X\cup\{y\}\in\mathcal{I}$, choose
> such a $y$ with largest weight, call it $e_i$, add it to $X$ and increase
> $i$; else stop and output $X$.

(d) Construct a simple social network with nonnegative weights on the
    people such that the greedy algorithm, with $\mathcal{I}$ being the set of
    all cliques, does not find the maximum weight clique.

Now suppose $\mathcal{I}$ satisfies (I1)–(I3), and the greedy algorithm chooses
$e_1,e_2,\dots,e_r$ in that order.

(e) Prove by contradiction that
    $w(e_1)\ge w(e_2)\ge\cdots\ge w(e_r)$.

(f) Prove that the greedy algorithm finds a maximum weight independent
    set.
:::

::: {.problem #prob-proofs-12 origin="external" source="fit1058-cn-3.15-q12"}
(Challenge) Let $E$ be a finite set and $\mathcal S$ a set of subsets of $E$.

- $\mathcal S$ is *linear under $\triangle$* if
  $X\triangle Y\in\mathcal S$ for all $X,Y\in\mathcal S$.

- $\mathrm{span}(\mathcal S) := \{X_1\triangle\cdots\triangle X_k :
                X_1,\dots,X_k\in\mathcal S,\ k\in\mathbb{N}\}$ (the symmetric difference of
  zero sets is $\emptyset$).

- $\mathcal S$ is *dependent under $\triangle$* if for some
  distinct $X_1,\dots,X_k\in\mathcal S$,
  $X_1\triangle\cdots\triangle X_k=\emptyset$; otherwise
  *independent*.

- A *circuit* is a minimal dependent set; a *base* is a
  maximal independent set.

(a) Let $\mathcal S$ be linear under $\triangle$. Prove by induction on
    $k$ that for all $X_1,\dots,X_k\in\mathcal S$,
    $X_1\triangle\cdots\triangle X_k\in\mathcal S$.

(b) Prove that $\mathcal S$ is linear under $\triangle$ iff
    $\mathcal S=\mathrm{span}(\mathcal S)$.

(c) Prove by induction on $k$ that for all $X_1,\dots,X_k\in\mathcal
                  S$, either $X_1\triangle\cdots\triangle X_k=\emptyset$, or there
    exist distinct $Y_1,\dots,Y_n\in\mathcal S$ with $n\le k$ and
    $X_1\triangle\cdots\triangle X_k=Y_1\triangle\cdots\triangle Y_n$.

(d) Prove that $\mathcal S$ is dependent iff there exists
    $X\in\mathcal S$ with $X\in\mathrm{span}(\mathcal S\setminus\{X\})$.

(e) Prove that if $\mathcal S$ is minimal dependent, then for every
    $X\in\mathcal S$, $X\in\mathrm{span}(\mathcal S\setminus\{X\})$.

(f) Prove that every minimal spanning set is independent.

(g) Prove that every minimal spanning set is a maximal independent set.

(h) Prove that every maximal independent set is a spanning set.

(i) Prove that every maximal independent set is a minimal spanning set.

(j) Prove that $\mathcal S$ is a minimal spanning set iff it is a
    maximal independent set.

(k) Prove that if $\mathcal S$ is independent then
    $|\mathrm{span}(\mathcal S)|=2^{|\mathcal S|}$.

(l) Prove the independence augmentation property: if $\mathcal S$ and
    $\mathcal T$ are independent and $|\mathcal T|=|\mathcal S|+1$,
    then there exists $X\in\mathcal T\setminus\mathcal S$ such that
    $\mathcal S\cup\{X\}$ is independent.

(m) Prove that all bases have the same size.

(n) Do all minimal dependent sets have the same size? Prove your claim.

(o) Prove that for every base $\mathcal B$ of $\mathcal S$ and every
    $X\in\mathcal S$, there is a unique way to write $X$ as a symmetric
    difference of members of $\mathcal B$, each used at most once.

(p) For each of (a)–(o), state what type of proof you used.

(q) Design a simple algorithm: INPUT a collection $\mathcal S$ of
    subsets of $E$ with nonnegative weights; OUTPUT an independent
    $\mathcal X\subseteq\mathcal S$ of maximum total weight. Does it
    always find the best solution? Justify using a previous exercise.
:::

::: {.problem #prob-proofs-15 origin="external" source="fit1058-cn-3.15-q15"}
Let $G$ be the cryptosystem obtained from Caesar slide (Exercise 2.15) by
restricting the keyspace to $K_G=\{\mathtt a,\mathtt b,\dots,\mathtt m\}$.
Prove that $G$ is not idempotent.
:::
