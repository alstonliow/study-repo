<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-functions-16 origin="external" source="fit1058-cn-2.19-q16"}
If $f$ is an injection and $f^{-1}$ is its inverse relation, what can you say
about $f\circ f^{-1}$ and $f^{-1}\circ f$? What kinds of functions or
relations are they, and what are their domains and codomains?
:::

::: {.problem #prob-cs70hw-1-q7 origin="external" source="cs70hw-1-q7"}
**Preserving Set Operations.** For a function $f$, define the image of a set $X$ to be the set $f(X) = \{y \mid y = f(x) \text{ for some } x \in X\}$. Define the inverse image or preimage of a set $Y$ to be the set $f^{-1}(Y) = \{x \mid f(x) \in Y\}$. Prove the following statements, in which $A$ and $B$ are sets. By doing so, you will show that inverse images preserve set operations, but images typically do not.

Hint: For sets $X$ and $Y$, $X = Y$ if and only if $X \subseteq Y$ and $Y \subseteq X$. To prove that $X \subseteq Y$, it is sufficient to show that $(\forall x)\ ((x \in X) \implies (x \in Y))$.

(a) $f^{-1}(A \cup B) = f^{-1}(A) \cup f^{-1}(B)$.

(b) $f^{-1}(A \cap B) = f^{-1}(A) \cap f^{-1}(B)$.

(c) $f^{-1}(A \setminus B) = f^{-1}(A) \setminus f^{-1}(B)$.

(d) $f(A \cup B) = f(A) \cup f(B)$.

(e) $f(A \cap B) \subseteq f(A) \cap f(B)$, and give an example where equality does not hold.

(f) $f(A \setminus B) \supseteq f(A) \setminus f(B)$, and give an example where equality does not hold.
:::
