::: {.problem #prob-camib-ats-3-q5 origin="external" source="camib-ats-3-q5"}
Let $(X,\tau)$ and $(Y,\rho)$ be topological spaces with $(Y,\rho)$ Hausdorff.

(a) Show that $\Delta = \{(y,y) : y \in Y\}$ is a closed subset of $Y \times Y$ with the product topology.

(b) Let $f$, $g : X \to Y$ be continuous. Show that $\{x \in X : f(x) = g(x)\}$ is a closed subset of $X$.
:::

::: {.problem #prob-camib-ats-3-q8 origin="external" source="camib-ats-3-q8"}
Let $(X,\tau)$ be a topological space, $X = A \cup B$ for $A, B \subset X$. Let $(Y,\rho)$ be another topological space. Take $g : A \to Y$ and $h : B \to Y$ be continuous functions, with respect to the subspace topology, which agree on $A \cap B$. Define a function $f : X \to Y$ by
$$f(x) = \begin{cases} g(x), & x \in A \\ h(x), & x \in B \end{cases},$$
which "glues" together $g$ and $h$.

(a) Show that, if $A$ and $B$ are both closed in $X$, then $f$ is continuous.

(b) Is this still true if $A$ is not closed in $X$?
:::

::: {.problem #prob-camib-ats-3-q9 origin="external" source="camib-ats-3-q9"}
Show that a finite product of metrizable topological spaces is metrizable. Hint: start by considering the product of two metric spaces $(X,d)$ and $(Y,e)$, and defining an appropriate metric on $X \times Y$.
:::

::: {.problem #prob-camib-ats-3-q10 origin="external" source="camib-ats-3-q10"}
Let $X = [0,1] \cup [2,3]$ with the usual topology and define an equivalence relation $\sim$ on $X$ by $x \sim y$ iff $x = y$ or $\{x,y\} = \{1,2\}$. Show that $X/\sim$ is homeomorphic to $[0,2]$ with the usual topology.
:::

::: {.problem #prob-camib-ats-3-q11 origin="external" source="camib-ats-3-q11"}
Let $X$, $Y$ be topological spaces and endow $X \times Y$ with the product topology.

(a) Show for each $y \in Y$ that $X \times \{y\}$, as a subspace of $X \times Y$, is homeomorphic to $X$.

(b) Define an equivalence relation $\sim$ on $X \times Y$ by $(x,y) \sim (x',y')$ iff $x = x'$. Assuming $Y$ is non-empty, show that $X \times Y/\sim$ is homeomorphic to $X$.
:::

::: {.problem #prob-camib-ats-3-q12 origin="external" source="camib-ats-3-q12"}
Let $\sim$ be the equivalence relation on $\mathbb{R}^2$ defined by $(x,y) \sim (z,w)$ iff $x - z \in \mathbb{Z}$ and $y - w \in \mathbb{Z}$. Show that $\mathbb{R}^2/\sim$ is homeomorphic to the torus.
$$T = \big\{\big((2 + \cos\theta)\cos\varphi, (2 + \cos\theta)\sin\varphi, \sin\theta\big) \,\big|\, \theta, \varphi \in [0,2\pi]\big\}.$$
:::

::: {.problem #prob-camib-ats-3-q13 origin="external" source="camib-ats-3-q13"}
Let $X = \{(x,y) \in \mathbb{R}^2 : y = \pm1\}$ and $\sim$ be the equivalence relation on $X$ defined by $(x,y) \sim (x',y') \Leftrightarrow x' = x \neq 0, y' = -y$. Define $Q = X/\sim$.

(a) Show that every point in $Q$ has a neighborhood homeomorphic to $\mathbb{R}$. Hint: it helps to sketch $Q$.

(b) Show that $Q$ is, however, not Hausdorff.
:::
