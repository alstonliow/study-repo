<!-- Migrated from 1058note exercises/chapters (owner's solutions). -->

::: {.solution for="prob-functions-05"}
::: {.proof}

Recall that $R\subseteq A\times B$ is a function if and only if
$R$ satisfies both:

- **Existence**: $\{x\in A : (x,y)\in R \text{ for
              some } y\in B\} = A$;

- **Uniqueness (well-definedness)**: for every
  $x\in A$, the set $R(x)=\{y\in B : xRy\}$ contains
  exactly one element.

**(i) $f\cap g$.**
$$(f\cap g)(x) = \{f(x)\}\cap\{g(x)\}.$$
When $f(x)=g(x)$: $(f\cap g)(x) = \{f(x)\}$.
When $f(x)\ne g(x)$: $(f\cap g)(x) = \emptyset$ — does not
exist. So $f\cap g$ is *not necessarily* a function; it can
fail **existence**.

**(ii) $f\cup g$.**
$$(f\cup g)(x) = \{f(x)\}\cup\{g(x)\}.$$
When $f(x)=g(x)$: $|(f\cup g)(x)|=1$.
When $f(x)\ne g(x)$: $|(f\cup g)(x)|=2$. So $f\cup g$ is
*not necessarily* a function; it can fail
**uniqueness**.

**(iii) $f\setminus g$.**
$$(f\setminus g)(x) = \{f(x)\}\setminus\{g(x)\}.$$
When $f(x)=g(x)$: $|f\setminus g|=0$ — does not exist.
When $f(x)\ne g(x)$: $|f\setminus g|=1$. So $f\setminus g$ is
*not necessarily* a function; it can fail
**existence**.

**(iv) $g\setminus f$.**
By the same argument as (iii) with the roles of $f,g$
interchanged, $g\setminus f$ is *not necessarily* a
function.

**(v) $f\triangle g$.**
$$(f\triangle g)(x) = \{(f\setminus g)(x)\}
        \cup \{(g\setminus f)(x)\}.$$
When $f(x)=g(x)$: $|f\triangle g|=0$ — does not exist.
When $f(x)\ne g(x)$: $|f\triangle g|=2$. So $f\triangle g$ is
*not necessarily* a function; depending on $f,g$, it can
fail either **existence** or **uniqueness**.

**(vi) $f\times g$.**
$$f\times g = \{((a,b),(c,d)) : (a,b)\in f,\ (c,d)\in g\}.$$
This defines a function
$$f\times g : A\times C \to B\times D, \qquad
        (f\times g)(x,y) = (f(x), g(y)).$$
**Existence**: for all $(x,y)\in A\times C$, since $f$ and
$g$ are functions, $f(x)$ and $g(y)$ must exist, so
$(f(x),g(y))$ exists.
**Uniqueness**: since $f(x)$ and $g(y)$ are each unique,
the pair $(f(x),g(y))$ is unique.
So $f\times g$ is *always* a function.

:::
:::

::: {.solution for="prob-functions-06"}
By [5(ii)](#5ii) $f \cup g$ is always a function.
:::
