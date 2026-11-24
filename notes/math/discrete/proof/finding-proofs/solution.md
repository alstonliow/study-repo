<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

<!-- Migrated from 1058note exercises/chapters (owner's solutions). -->

::: {.solution for="prob-proofs-02"}
::: {.proof name="Proof (by contradiction)"}

Assume that $L$ is a nonempty hereditary set of strings that does
*not* contain the empty string.

Let $S = \{\,|x| : x \in L\,\}$ be the set of lengths of strings
in $L$. Since $L$ is nonempty, $S$ is a nonempty subset of $\mathbb{N}$.
By the Well-Ordering Principle, $S$ has a smallest element.

Let $x_0 \in L$ be a string of minimum length, i.e.
$$\forall x \in L,\ |x_0| \le |x|.$$
Since $x_0$ is a nonempty string, its length is
$|x_0| = n_0 \ge 1$.

Since $L$ is hereditary and $x_0 \in L$ is nonempty, there is a
character in $x_0$ which can be deleted to give another string
$x_1 \in L$, where
$$|x_1| = n_0 - 1.$$

Since $x_0$ is the smallest string in $L$, we have
$|x_0| \le |x|$ for every $x \in L$. But
$$|x_1| = n_0 - 1 < n_0 = |x_0|,$$
which contradicts the minimality of $x_0$.

This is a contradiction. Therefore, the assumption is false, and
$L$ must contain the empty string.

:::
:::

::: {.solution for="prob-proofs-05"}
**(a)**

**(b)**

::: {.proof name="Proof of (b)"}

Let $E$ = vertices of a social network, and let $\mathcal{I}$ = the set of
all cliques.

**(I1).** Let $X$ be a clique, and consider $X = \emptyset$.
Since $\emptyset$ contains no elements, there do not exist
$u,v\in\emptyset$ with $u\ne v$.
$$\text{So the implication ``}u\ne v \implies (u,v)\text{ is
        edge''}$$
holds vacuously for all $u,v\in\emptyset$. So $\emptyset$ is a
clique, i.e.
$$\emptyset\in\mathcal{I}.$$

**(I2).** Need to prove: if $X\subseteq Y$ and $Y$ is a
clique, then $X$ is a clique.

For all $u,v\in X$ with $u\ne v$: since $X\subseteq Y$,
$$u,v\in Y \quad \text{with } u\ne v.$$
Since $Y$ is a clique, $(u,v)$ is an edge. Hence $X$ is also a
clique.

**(I3) fails in general.** Consider the graph with vertices
$\{a,b,c,d\}$ and a single edge $(b,c)$. Let
$$X=\{a\}, \qquad Y=\{b,c\}.$$
$X$ and $Y$ are cliques, and $Y\setminus X = \{b,c\}$. Checking
each candidate:
$$X\cup\{b\} = \{a,b\} \text{ is not a clique, since } (a,b)
        \text{ is not an edge.}$$
$$X\cup\{c\} = \{a,c\} \text{ is not a clique, since } (a,c)
        \text{ is not an edge.}$$
So no valid $y\in Y\setminus X$ exists, and (I3) fails.

:::

::: {.remark}

This is the key place where the “clique matroid” fails to be a
genuine matroid: in the vector-space analogy, (I3) is the
exchange axiom that guarantees any linearly independent set can
be extended toward a larger independent set. Cliques do not have
this exchange property in general, which is exactly why the
greedy algorithm can fail on them (part (d)).

:::

**(c)**

::: {.proof name="Proof of (c)"}

An independent set $X\in\mathcal{I}$ is *maximal* if
$$\nexists\, Y\in\mathcal{I}\text{ such that } X\subsetneq Y.$$

We need to prove:
$$\forall X,Y\in\mathcal{I},\quad X \text{ maximal} \wedge Y \text{
        maximal} \implies |X|=|Y|.$$

Assume, for contradiction, there exist two maximal independent
sets $X,Y\in\mathcal{I}$ with $|X|\ne|Y|$. WLOG, assume
$$|X|<|Y|.$$

Since $X,Y\in\mathcal{I}$ and $|X|<|Y|$, by (I3) there exists
$y\in Y\setminus X$ such that
$$X\cup\{y\}\in\mathcal{I}.$$

Since $y\notin X$, we have
$$X\subsetneq X\cup\{y\}, \qquad X\cup\{y\}\in\mathcal{I}.$$
This contradicts the assumption that $X$ is maximal.

Therefore, the assumption is false: all maximal independent sets
have the same size.

:::

::: {.remark}

This is the exact analogue of the fact that any two bases of a
vector space have the same size (i.e. dimension is well
defined). There, the argument uses the Steinitz exchange lemma;
here (I3) plays precisely that role.

:::

**(d)**

**(e)**

::: {.proof name="Proof of (e)"}

When $\mathcal{I}$ satisfies (I1)–(I3), the greedy algorithm chooses
elements of $E$ in a specific order $e_1,e_2,\dots,e_r$. We prove
$$w(e_i) \ge w(e_{i+1}) \qquad \text{for all } 1\le i<r.$$

Recall $e_i$ is the maximum-weight element among all
$y\in E\setminus X_{i-1}$ satisfying $X_{i-1}\cup\{y\}\in\mathcal{I}$:
$$X_{i-1}\cup\{e_i\}\in\mathcal{I},$$
$$\forall y \text{ with } X_{i-1}\cup\{y\}\in\mathcal{I},\quad
        w(e_i)\ge w(y).$$

Assume, for contradiction, that
$$w(e_i) < w(e_{i+1}) \qquad \text{for some } 1\le i<r.$$

Since $e_{i+1}$ was chosen by the algorithm at round $i+1$,
$$X_i \cup \{e_{i+1}\} \in \mathcal{I}.$$
Since $X_{i-1}\subseteq X_i$,
$$X_{i-1}\cup\{e_{i+1}\} \subseteq X_i\cup\{e_{i+1}\}.$$
Since $X_i\cup\{e_{i+1}\}\in\mathcal{I}$, by (I2),
$$X_{i-1}\cup\{e_{i+1}\}\in\mathcal{I}.$$

This means $e_{i+1}$ is one of the candidates $y$ satisfying
$X_{i-1}\cup\{y\}\in\mathcal{I}$ at round $i$. Since $e_i$ was chosen at
round $i$ as the maximum-weight element among all such
candidates,
$$w(e_i) \ge w(e_{i+1}),$$
which contradicts the assumption $w(e_i) < w(e_{i+1})$.

Therefore the assumption is false, and
$$w(e_i)\ge w(e_{i+1}) \qquad \text{for all } 1\le i<r.$$

:::

::: {.remark}

This mirrors a standard fact from linear algebra: if you build up
an independent set greedily by always adding the “largest”
remaining valid candidate, the sequence of choices is
automatically monotone — the exchange property (I2) is what
lets you “pull” a later candidate back to an earlier round
without breaking independence.

:::

**(f)**

::: {.proof name="Proof of (f)"}

Let $Y$ be a maximum weight independent set. By the stopping
condition of the greedy algorithm, when $X=\{e_1,\dots,e_r\}$,
there is no $y\in E\setminus X$ such that
$$X\cup\{y\}\in\mathcal{I}.$$
So $X$ is a maximal independent set.

By part (c), we know
$$|X|=|Y|=r.$$
Write $Y=\{f_1,\dots,f_r\}$ with
$$w(f_1)\ge w(f_2) \ge \cdots \ge w(f_r).$$

**Main claim.** For each $i=1,\dots,r$,
$$w(e_i)\ge w(f_i).$$

By contradiction (minimal counterexample): assume there exists a
minimum $i$ such that $w(e_i) < w(f_i)$. By minimality of $i$,
$$w(e_k)\ge w(f_k) \qquad \text{for all } k<i.$$

Let
$$X_{i-1}=\{e_1,\dots,e_{i-1}\}, \qquad F_i=\{f_1,\dots,f_i\}.$$
Since $X_{i-1}\subseteq X\in\mathcal{I}$, by (I2), $X_{i-1}\in\mathcal{I}$. Since
$F_i\subseteq Y\in\mathcal{I}$, by (I2), $F_i\in\mathcal{I}$. Also
$$|X_{i-1}|=i-1 < i = |F_i|.$$

By (I3), there exists $y\in F_i\setminus X_{i-1}$ such that
$$X_{i-1}\cup\{y\}\in\mathcal{I}.$$

Since $y\in F_i = \{f_1,\dots,f_i\}$, and these are sorted in
decreasing order of weight, $f_i$ has the smallest weight among
them, so
$$w(y) \ge w(f_i).$$

Now, since $y\notin X_{i-1}$ and $X_{i-1}\cup\{y\}\in\mathcal{I}$, $y$ is a
valid candidate at round $i$ of the greedy algorithm. But $e_i$
was chosen at round $i$ as the element of maximum weight among
all such valid candidates, so
$$w(e_i) \ge w(y) \ge w(f_i).$$
This contradicts the assumption $w(e_i) < w(f_i)$. Hence no such
$i$ exists, and
$$w(e_i)\ge w(f_i) \qquad \text{for all } i=1,\dots,r.$$

Summing over $i$:
$$w(X) = \sum_{i=1}^r w(e_i) \ge \sum_{i=1}^r w(f_i) = w(Y).$$
Since $Y$ was assumed to be a maximum weight independent set,
$w(X)\ge w(Y)$ forces
$$w(X)=w(Y).$$
Therefore $X$ is also a maximum weight independent set.
$$\therefore \text{Greedy algorithm finds a maximum weight
        independent set.}$$

:::

::: {.remark}

This whole argument is the discrete, combinatorial analogue of
the Matroid Greedy Theorem, itself a generalisation of the fact
that Gaussian elimination / the Gram–Schmidt-style greedy basis
selection process finds an optimal basis with respect to any
linear weighting — the same “minimal counterexample +
exchange” technique (Steinitz exchange lemma) underlies both.

:::
:::

::: {.solution for="prob-proofs-12" status="draft"}
<!-- Written by Claude in our own words, then checked against the FIT1058 sample solutions
     (not copied). Differences: (b) adds the caveat S nonempty; (n) uses a different
     counterexample (the sample's 4-set family has symmetric difference {1,4}, not empty);
     (g), (h), (m) are proved directly rather than by contradiction. -->
**Conventions.** Throughout we use that $\triangle$ is commutative and associative,
$X \triangle X = \emptyset$ and $X \triangle \emptyset = X$; so a symmetric difference of
several sets does not depend on order or bracketing, and two equal terms cancel.
A dependence witness always has $k \ge 1$ (with $k = 0$ every family would be dependent).
For (f)–(o) fix a family $\mathcal{S}$; "spanning", "independent", "minimal" and "maximal"
refer to subfamilies $\mathcal{T} \subseteq \mathcal{S}$, and $\mathcal{T}$ is *spanning* if
$\mathrm{span}(\mathcal{T}) = \mathrm{span}(\mathcal{S})$. Two facts used repeatedly:

- **(L)** $\mathcal{T} \subseteq \mathrm{span}(\mathcal{T})$, and $\mathrm{span}(\mathcal{T})$ is linear
  under $\triangle$ (join the two lists of terms). Hence if $\mathcal{U} \subseteq \mathrm{span}(\mathcal{T})$,
  then $\mathrm{span}(\mathcal{U}) \subseteq \mathrm{span}(\mathcal{T})$: each term of a member of
  $\mathrm{span}(\mathcal{U})$ expands into members of $\mathcal{T}$. Also $\mathcal{U} \subseteq \mathcal{T}$
  implies $\mathrm{span}(\mathcal{U}) \subseteq \mathrm{span}(\mathcal{T})$.
- **(M)** If $\mathcal{U}$ is independent, $X \notin \mathcal{U}$ and $\mathcal{U} \cup \{X\}$ is dependent,
  then $X \in \mathrm{span}(\mathcal{U})$. Indeed, take distinct $X_1, \ldots, X_k \in \mathcal{U} \cup \{X\}$
  with $X_1 \triangle \cdots \triangle X_k = \emptyset$. If $X$ were not among them, $\mathcal{U}$ would be
  dependent; so $X = X_j$ for some $j$, and taking $\triangle X_j$ of both sides gives $X$ as the
  symmetric difference of the other $X_i$, all in $\mathcal{U}$.

**(a)** Induction on $k \ge 1$.

1. Base case $k = 1$: $X_1 \in \mathcal{S}$.

2. Inductive step: suppose the claim holds for $k$, and let $X_1, \ldots, X_{k+1} \in \mathcal{S}$.
   Then $Z := X_1 \triangle \cdots \triangle X_k \in \mathcal{S}$ by the inductive hypothesis, so
   $X_1 \triangle \cdots \triangle X_{k+1} = Z \triangle X_{k+1} \in \mathcal{S}$ by linearity.

3. The case $k = 0$ gives $\emptyset$. If $\mathcal{S} \neq \emptyset$, pick $X \in \mathcal{S}$; then
   $\emptyset = X \triangle X \in \mathcal{S}$. If $\mathcal{S} = \emptyset$ the case $k = 0$ fails, so the
   claim holds for all $k$ exactly when $\mathcal{S} \neq \emptyset$.

**(b)** This needs $\mathcal{S} \neq \emptyset$: the empty family is linear (vacuously), but
$\mathrm{span}(\emptyset) = \{\emptyset\} \neq \emptyset$. Assume $\mathcal{S} \neq \emptyset$.

1. ($\Rightarrow$) Every $X \in \mathcal{S}$ is a symmetric difference of one member, so
   $\mathcal{S} \subseteq \mathrm{span}(\mathcal{S})$. Conversely every member of the span is in
   $\mathcal{S}$ by (a), including the case $k = 0$ (step 3 of (a)).

2. ($\Leftarrow$) If $X, Y \in \mathcal{S}$, then $X \triangle Y \in \mathrm{span}(\mathcal{S}) = \mathcal{S}$.

**(c)** Induction on $k \ge 0$.

1. Base case $k = 0$: the empty symmetric difference is $\emptyset$.

2. Inductive step: let $Z := X_1 \triangle \cdots \triangle X_k$. By the inductive hypothesis $Z = \emptyset$,
   or $Z = Y_1 \triangle \cdots \triangle Y_n$ with distinct $Y_i \in \mathcal{S}$ and $n \le k$.
   Consider $Z \triangle X_{k+1}$.

3. If $Z = \emptyset$, then $Z \triangle X_{k+1} = X_{k+1}$, one set, and $1 \le k+1$.

4. If $X_{k+1} \notin \{Y_1, \ldots, Y_n\}$, then $Y_1, \ldots, Y_n, X_{k+1}$ are distinct, and $n + 1 \le k + 1$.

5. If $X_{k+1} = Y_j$, the two copies cancel, leaving the symmetric difference of the $n - 1$
   distinct sets $Y_i$, $i \ne j$. This is $\emptyset$ if $n = 1$; otherwise $n - 1 \le k + 1$.

**(d)**

1. ($\Rightarrow$) Take distinct $X_1, \ldots, X_k \in \mathcal{S}$, $k \ge 1$, with
   $X_1 \triangle \cdots \triangle X_k = \emptyset$, and let $X := X_1$. Taking $\triangle X_1$ of both sides gives
   $X = X_2 \triangle \cdots \triangle X_k$. By distinctness $X_2, \ldots, X_k \in \mathcal{S} \setminus \{X\}$,
   so $X \in \mathrm{span}(\mathcal{S} \setminus \{X\})$ (for $k = 1$ this says $X = \emptyset$, the empty
   symmetric difference).

2. ($\Leftarrow$) Suppose $X \in \mathrm{span}(\mathcal{S} \setminus \{X\})$. Apply (c) to the family
   $\mathcal{S} \setminus \{X\}$. Either $X = \emptyset$, and then the single set $X_1 := X$ witnesses
   dependence; or $X = Y_1 \triangle \cdots \triangle Y_n$ with distinct $Y_i \in \mathcal{S} \setminus \{X\}$, and then
   $X, Y_1, \ldots, Y_n$ are distinct members of $\mathcal{S}$ with $X \triangle Y_1 \triangle \cdots \triangle Y_n = \emptyset$.

**(e)**

1. Since $\mathcal{S}$ is dependent, there are distinct $X_1, \ldots, X_k \in \mathcal{S}$ with
   $X_1 \triangle \cdots \triangle X_k = \emptyset$. The subfamily $\{X_1, \ldots, X_k\}$ is then dependent, so by
   minimality it is all of $\mathcal{S}$.

2. Let $X \in \mathcal{S}$; then $X = X_j$ for some $j$, and as in (d) $X$ is the symmetric difference of the
   other $X_i$, which all lie in $\mathcal{S} \setminus \{X\}$.

**(f)** Let $\mathcal{T}$ be a minimal spanning subfamily, and suppose for contradiction that it is dependent.

1. By (d) there is $X \in \mathcal{T}$ with $X \in \mathrm{span}(\mathcal{T} \setminus \{X\})$.

2. Then $\mathcal{T} \subseteq \mathrm{span}(\mathcal{T} \setminus \{X\})$, so by (L)
   $\mathrm{span}(\mathcal{T}) \subseteq \mathrm{span}(\mathcal{T} \setminus \{X\}) \subseteq \mathrm{span}(\mathcal{T})$.

3. So $\mathcal{T} \setminus \{X\}$ is spanning, contradicting the minimality of $\mathcal{T}$.

**(g)** Let $\mathcal{T}$ be a minimal spanning subfamily. It is independent by (f).

1. Let $X \in \mathcal{S} \setminus \mathcal{T}$. Then
   $X \in \mathrm{span}(\mathcal{S}) = \mathrm{span}(\mathcal{T}) = \mathrm{span}((\mathcal{T} \cup \{X\}) \setminus \{X\})$,
   so $\mathcal{T} \cup \{X\}$ is dependent by (d).

2. Any subfamily of $\mathcal{S}$ properly containing $\mathcal{T}$ contains such a $\mathcal{T} \cup \{X\}$, and a
   family containing a dependent family is dependent (the same witness works). So $\mathcal{T}$ is maximal independent.

**(h)** Let $\mathcal{T}$ be a maximal independent subfamily.

1. Let $X \in \mathcal{S}$. If $X \in \mathcal{T}$ then $X \in \mathrm{span}(\mathcal{T})$. Otherwise
   $\mathcal{T} \cup \{X\}$ is dependent by maximality, so $X \in \mathrm{span}(\mathcal{T})$ by (M).

2. Hence $\mathcal{S} \subseteq \mathrm{span}(\mathcal{T})$, so $\mathrm{span}(\mathcal{S}) \subseteq \mathrm{span}(\mathcal{T})$ by (L);
   the reverse inclusion holds since $\mathcal{T} \subseteq \mathcal{S}$. So $\mathcal{T}$ is spanning.

**(i)** Let $\mathcal{T}$ be a maximal independent subfamily. It is spanning by (h). Suppose for
contradiction that some $\mathcal{T}' \subsetneq \mathcal{T}$ is spanning, and pick $X \in \mathcal{T} \setminus \mathcal{T}'$.

1. $X \in \mathrm{span}(\mathcal{S}) = \mathrm{span}(\mathcal{T}') \subseteq \mathrm{span}(\mathcal{T} \setminus \{X\})$ by (L).

2. By (d), $\mathcal{T}$ is dependent, a contradiction. So $\mathcal{T}$ is a minimal spanning subfamily.

**(j)** ($\Rightarrow$) is (g) and ($\Leftarrow$) is (i).

**(k)** Let $n := |\mathcal{S}|$. For $\mathcal{U} \subseteq \mathcal{S}$ let $\varphi(\mathcal{U})$ be the symmetric
difference of all members of $\mathcal{U}$ (with $\varphi(\emptyset) = \emptyset$). We show that
$\varphi : \mathcal{P}(\mathcal{S}) \to \mathrm{span}(\mathcal{S})$ is a bijection; then
$|\mathrm{span}(\mathcal{S})| = |\mathcal{P}(\mathcal{S})| = 2^n$.

1. Surjective: a member of the span is $X_1 \triangle \cdots \triangle X_k$; by (c) it is $\emptyset = \varphi(\emptyset)$
   or $Y_1 \triangle \cdots \triangle Y_m = \varphi(\{Y_1, \ldots, Y_m\})$ with the $Y_i$ distinct.

2. Injective: members in both $\mathcal{U}$ and $\mathcal{V}$ cancel in pairs, so
   $\varphi(\mathcal{U}) \triangle \varphi(\mathcal{V}) = \varphi(\mathcal{U} \triangle \mathcal{V})$. If
   $\varphi(\mathcal{U}) = \varphi(\mathcal{V})$ and $\mathcal{U} \neq \mathcal{V}$, then the members of the nonempty
   family $\mathcal{U} \triangle \mathcal{V} \subseteq \mathcal{S}$ are distinct with symmetric difference
   $\emptyset$, so $\mathcal{S}$ is dependent, a contradiction.

**(l)** Suppose for contradiction that $\mathcal{S} \cup \{X\}$ is dependent for every $X \in \mathcal{T} \setminus \mathcal{S}$.

1. By (M), every $X \in \mathcal{T} \setminus \mathcal{S}$ lies in $\mathrm{span}(\mathcal{S})$; so does every
   $X \in \mathcal{T} \cap \mathcal{S}$. Hence $\mathcal{T} \subseteq \mathrm{span}(\mathcal{S})$, and
   $\mathrm{span}(\mathcal{T}) \subseteq \mathrm{span}(\mathcal{S})$ by (L).

2. By (k), $2^{|\mathcal{S}| + 1} = |\mathrm{span}(\mathcal{T})| \le |\mathrm{span}(\mathcal{S})| = 2^{|\mathcal{S}|}$,
   a contradiction.

**(m)** Let $\mathcal{B}_1, \mathcal{B}_2$ be bases (maximal independent subfamilies) of $\mathcal{S}$.

1. By (h) both are spanning, so $\mathrm{span}(\mathcal{B}_1) = \mathrm{span}(\mathcal{S}) = \mathrm{span}(\mathcal{B}_2)$.

2. By (k), $2^{|\mathcal{B}_1|} = 2^{|\mathcal{B}_2|}$, so $|\mathcal{B}_1| = |\mathcal{B}_2|$.

(Alternatively: if $|\mathcal{B}_1| < |\mathcal{B}_2|$, apply (l) to $\mathcal{B}_1$ and $|\mathcal{B}_1| + 1$ members of
$\mathcal{B}_2$ to contradict the maximality of $\mathcal{B}_1$.)

**(n)** No. Let $E = \{1, 2\}$ and $\mathcal{S} = \{\emptyset, \{1\}, \{2\}, \{1, 2\}\}$.

1. $\{\emptyset\}$ is dependent ($k = 1$, $X_1 = \emptyset$), and its only proper subfamily, the empty family,
   is independent. So it is a minimal dependent subfamily of size $1$.

2. $\{\{1\}, \{2\}, \{1, 2\}\}$ is dependent, since $\{1\} \triangle \{2\} \triangle \{1, 2\} = \emptyset$. Its proper
   subfamilies are independent: each single member is nonempty, and two distinct sets have nonempty
   symmetric difference. So it is a minimal dependent subfamily of size $3$.

**(o)** Let $\mathcal{B}$ be a base of $\mathcal{S}$ and $X \in \mathcal{S}$. With $\varphi$ as in (k), a way of
writing $X$ using each member of $\mathcal{B}$ at most once is a subfamily $\mathcal{U} \subseteq \mathcal{B}$ with
$\varphi(\mathcal{U}) = X$.

1. Existence: $X \in \mathrm{span}(\mathcal{S}) = \mathrm{span}(\mathcal{B})$ by (h), and $\varphi$ maps onto
   $\mathrm{span}(\mathcal{B})$ by (k).

2. Uniqueness: $\mathcal{B}$ is independent, so $\varphi$ is injective on $\mathcal{P}(\mathcal{B})$ by (k).

**(p)** (a) induction; (b) direct proof of both directions; (c) induction with proof by cases;
(d) direct proof of both directions, by construction; (e) direct proof; (f) contradiction;
(g) direct proof; (h) direct proof by cases; (i) contradiction; (j) combining two earlier results;
(k) bijective proof (construction, with injectivity by contradiction); (l) contradiction;
(m) direct proof (the alternative is by contradiction); (n) counterexample; (o) existence and uniqueness.

**(q)** Greedy algorithm.

1. Sort the members of $\mathcal{S}$ by weight, largest first, and start with $\mathcal{X} := \emptyset$.

2. For each $X$ in this order, add $X$ to $\mathcal{X}$ if $\mathcal{X} \cup \{X\}$ is still independent.
   By (d) and (M) this holds exactly when $X \notin \mathrm{span}(\mathcal{X})$, which can be tested by
   Gaussian elimination over $\{0, 1\}$ on the characteristic vectors of the sets.

3. Output $\mathcal{X}$.

It always finds a best solution. Take the ground set to be $\mathcal{S}$ and the independent subfamilies
of $\mathcal{S}$ as $\mathcal{I}$ in @prob-proofs-05. Then (I1) holds since the empty family is independent;
(I2) holds since a subfamily of an independent family is independent (a witness in the subfamily
would be one in the family); and (I3) follows from (l), applied to $\mathcal{X}$ and any $|\mathcal{X}| + 1$
members of $\mathcal{Y}$ when $|\mathcal{X}| < |\mathcal{Y}|$. This greedy algorithm is the one in
@prob-proofs-05, so by its part (f) it finds an independent subfamily of maximum weight.
:::

::: {.solution for="prob-proofs-04"}
<!-- TODO: as in Exercise 3, this refers to the proofs in these notes rather
     than the Course Notes' numbering. Owner to check. -->
(a) **Construction.** The ($\Leftarrow$) direction of @thm-inverse-functions-1
    constructs $f^{-1}$, by defining $f^{-1}(y)$ as the unique preimage of
    $y$. Part (a) of the proof of @thm-equivalence-relations-1 constructs the
    class $[x]_R$ containing $x$.

(b) **Contrapositive.** The definition of injectivity is used in its
    contrapositive form ($x_1\ne x_2\Rightarrow f(x_1)\ne f(x_2)$ becomes
    $f(x_1) = f(x_2)\Rightarrow x_1 = x_2$). The ($\Rightarrow$) direction of
    @thm-inverse-functions-1 argues that two preimages of the same $y$ would
    contradict the definition of $f^{-1}$, which is close to a contrapositive
    argument.

(c) **Cases.** The inductive step for @thm-finite-equal-size-domain-codomain
    splits on whether $y = b$ or $y\in B'$. Part (b) of the proof of
    @thm-equivalence-relations-1 treats $Y\setminus X$ and $X\setminus Y$
    separately.

A proof with several parts is not automatically a proof by cases. For example,
parts (a) and (b) of the proof of @thm-equivalence-relations-1 prove two
statements that must *both* hold, not alternatives.
:::

::: {.solution for="prob-proofs-15"}
We show that $G\circ G$ is not embeddable in $G$ (definitions as in Exercise
2.15), so $G\circ G\not\equiv G$.

1. Take the key pair $(\mathtt m,\mathtt m)$ for $G\circ G$. Since
   $\mathtt m = 12$, encrypting with it adds $12 + 12 = 24$ to every letter
   (mod $26$).

2. A key $k$ of $G$ adds $k\in\{0,1,\dots,12\}$ to every letter. To match the
   pair on the message $\mathtt a$ (letter $0$), we would need
   $k\equiv 24\pmod{26}$, but $24\notin\{0,\dots,12\}$.

3. So no key of $G$ does the same job as $(\mathtt m,\mathtt m)$. Hence
   $G\circ G\not\le G$, and $G$ is not idempotent.

The full Caesar slide is idempotent (Exercise 2.15) because its keyspace is
closed under addition mod $26$. Restricting the keys breaks this closure.
:::

::: {.solution for="prob-cs70-2-q1"}
<!-- TODO: solution -->
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6042f10-1-q4" status="draft"}
1. Weigh $4$ coins against $4$ others. If one side is lighter, the fake is among its $4$ coins; if they balance, it is among the $4$ coins not weighed. Either way $4$ suspects remain.

2. Weigh two of the suspects against each other. If one is lighter, it is the fake.

3. Otherwise the fake is one of the other two suspects: weigh them against each other, and the lighter one is the fake.

(In fact $2$ weighings suffice for up to $9$ coins and $3$ for up to $27$: split into three groups and weigh two of them.)
:::
