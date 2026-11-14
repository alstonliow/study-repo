<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-functions-21" status="draft"}
It is the relation itself. An equivalence relation is already transitive, and
the transitive closure of a transitive relation $R$ is $R$: every
$R^{(k)}\subseteq R$, so their union adds nothing.
:::

::: {.solution for="prob-functions-22" status="draft"}
(a) $\{\text{ate},\ \text{eat},\ \text{eta},\ \text{tea}\}$, and some
    dictionaries also list "tae".

(b) Many examples work, e.g. "I" ($k=1$), "ox" ($k=2$), "why" ($k=3$),
    "jump" ($k=4$).

(c) Write $w\sim v$ for the anagram relation.

    1. *Reflexive.* $w\sim w$ using the identity bijection.

    2. *Symmetric.* If $w\sim v$ via $f$, so $x_i = y_{f(i)}$, then
       $y_j = x_{f^{-1}(j)}$, so $v\sim w$ via $f^{-1}$.

    3. *Transitive.* If $w\sim v$ via $f$ and $v\sim u$ via $g$, then
       $x_i = y_{f(i)} = z_{g(f(i))}$, so $w\sim u$ via the bijection
       $g\circ f$.

(d) Two words are anagrams exactly when they have the same sorted letters, so
    count the distinct sorted forms. For example, in Python:

    ```python
    words = {w.strip().lower() for w in open("/usr/share/dict/words")}
    print(len({"".join(sorted(w)) for w in words}))
    ```

    The answer depends on the word list used.
:::
