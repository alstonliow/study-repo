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

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-1-q7" status="draft"}
(a)–(c) For every $x$, by the definition of the preimage,
$$x\in f^{-1}(A\cup B)\iff f(x)\in A\cup B\iff f(x)\in A\lor f(x)\in B\iff x\in f^{-1}(A)\cup f^{-1}(B).$$
Replacing $\lor$ by $\land$ gives (b), and by "$f(x)\in A$ and $f(x)\notin B$" gives (c). A chain of equivalences proves both inclusions at once.

(d)

1. If $y\in f(A\cup B)$, then $y=f(x)$ with $x\in A$ or $x\in B$, so $y\in f(A)$ or $y\in f(B)$.

2. If $y\in f(A)$, then $y=f(x)$ with $x\in A\subseteq A\cup B$, so $y\in f(A\cup B)$; the same for $f(B)$.

(e) If $y=f(x)$ with $x\in A\cap B$, then $y\in f(A)$ and $y\in f(B)$. For strict inclusion, let $f:\{1,2\}\to\{0\}$, $A=\{1\}$, $B=\{2\}$: then $f(A\cap B)=f(\emptyset)=\emptyset$ but $f(A)\cap f(B)=\{0\}$.

(f) Let $y\in f(A)\setminus f(B)$, so $y=f(x)$ for some $x\in A$. If $x\in B$, then $y\in f(B)$, which is false; so $x\in A\setminus B$ and $y\in f(A\setminus B)$. For strict inclusion, take the same $f$ with $A=\{1,2\}$, $B=\{2\}$: $f(A\setminus B)=\{0\}$ but $f(A)\setminus f(B)=\emptyset$.
:::
