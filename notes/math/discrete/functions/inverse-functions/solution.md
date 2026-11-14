<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-functions-16" status="draft"}
Let $f : A\to B$ be an injection, and let
$f^{-1} = \{(f(a),a) : a\in A\}$ be its inverse relation, from $B$ to $A$.
Since $f$ is injective, $f^{-1}$ relates each element of $\operatorname{im}f$
to exactly one element of $A$, and relates elements of
$B\setminus\operatorname{im}f$ to nothing.

- $f^{-1}\circ f$ (first $f$, then $f^{-1}$) sends each $a$ to $f(a)$ and
  back to $a$. It is the identity function $i_A : A\to A$.

- $f\circ f^{-1}$ (first $f^{-1}$, then $f$) relates each $b\in\operatorname{im}f$
  to itself and relates nothing else. It is the identity relation on
  $\operatorname{im}f$, viewed as a relation from $B$ to $B$. It is a
  function on $B$ (namely $i_B$) only if $f$ is also surjective; otherwise it
  is only a partial function.
:::
