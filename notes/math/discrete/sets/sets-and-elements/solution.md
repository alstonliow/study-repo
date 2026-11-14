<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-sets-02" status="draft"}
(a) A value of `aNewType` is an int together with a string, in that order.
    So the set of values is the Cartesian product
    $$\texttt{Int}\times\texttt{String}.$$

(b) A value of `anotherNewType` is either an int or a string. So the set of
    values is the union
    $$\texttt{Int}\cup\texttt{String}.$$

    Strictly, a C `union` does not record which member it holds, so if the two
    types shared a value we could not tell them apart. A type that does record
    this corresponds to the *disjoint* union
    $(\{0\}\times\texttt{Int})\cup(\{1\}\times\texttt{String})$.
:::
