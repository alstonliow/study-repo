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

::: {.solution for="prob-proofs-12"}
**(a)**

**(b)**

**(c)**

**(d)**

**(e)**

**(f)**

**(g)**

**(h)**

**(i)**

**(j)**

**(k)**

**(l)**

**(m)**

**(n)**

**(o)**

**Algorithm & justification**
:::

::: {.solution for="prob-proofs-04" status="draft"}
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

::: {.solution for="prob-proofs-15" status="draft"}
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
