<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs221hw-6-q3" status="draft"}
**(a)** $Y\rightarrow A_0$, $Y\rightarrow A_1$, $Y\rightarrow A_2$. Each label depends only on the true label, and the annotators are conditionally independent given $Y$, so there are no edges between the $A_i$.

**(b)** A perfect annotator copies $Y$:

| $y$ | $p(A_0=\text{good}\mid Y=y)$ | $p(A_0=\text{bad}\mid Y=y)$ |
|---|---|---|
| good | $1$ | $0$ |
| bad | $0$ | $1$ |

**(c)** A uniform guesser ignores $Y$:

| $y$ | $p(A_0=\text{good}\mid Y=y)$ | $p(A_0=\text{bad}\mid Y=y)$ |
|---|---|---|
| good | $0.5$ | $0.5$ |
| bad | $0.5$ | $0.5$ |
:::
