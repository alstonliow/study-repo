<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-ats-3-q5" status="draft"}
(a) Let $(y_1,y_2) \notin \Delta$, so $y_1 \ne y_2$. Choose disjoint open $U \ni y_1$, $V \ni y_2$. Then $U \times V$ is open in the product and contains $(y_1,y_2)$. It misses $\Delta$: $(y,y) \in U \times V$ would give $y \in U \cap V$. So $(Y\times Y) \setminus \Delta$ is open.

(b) $h = (f,g) : X \to Y \times Y$ is continuous, because its components are. The set is $h^{-1}(\Delta)$, which is closed by (a).
:::

::: {.solution for="prob-camib-ats-3-q8" status="draft"}
$f$ is well defined because $g = h$ on $A \cap B$.

(a)

1. Let $C \subset Y$ be closed. Then $f^{-1}(C) = g^{-1}(C) \cup h^{-1}(C)$.

2. $g^{-1}(C)$ is closed in $A$, so $g^{-1}(C) = A \cap F$ with $F$ closed in $X$; since $A$ is closed in $X$, $g^{-1}(C)$ is closed in $X$. Likewise $h^{-1}(C)$ is closed in $X$.

3. A union of two closed sets is closed, so $f^{-1}(C)$ is closed and $f$ is continuous.

(b) No. Take $X = \mathbb{R}$, $A = (-\infty,0)$ (not closed), $B = [0,\infty)$, $g = 0$ and $h = 1$. They agree on $A \cap B = \emptyset$ and are continuous, but $f$ jumps at $0$ and is not continuous.
:::

::: {.solution for="prob-camib-ats-3-q9" status="draft"}
1. Let $X_1, \dots, X_n$ be metrizable, with metrics $d_1, \dots, d_n$ inducing their topologies. On $X = X_1 \times \cdots \times X_n$ let $D(x,y) = \max_i d_i(x_i,y_i)$, clearly a metric.

2. The open $D$-ball of radius $r$ about $x$ is $B_r(x_1) \times \cdots \times B_r(x_n)$.

3. *Product-open implies $D$-open.* Let $x \in U_1 \times \cdots \times U_n$ with each $U_i$ open. Choose $r_i > 0$ with $B_{r_i}(x_i) \subset U_i$ and $r = \min r_i$; then the $D$-ball of radius $r$ about $x$ lies in $U_1 \times \cdots \times U_n$. So basic product-open sets, and hence their unions, are $D$-open.

4. *$D$-open implies product-open.* If $W$ is $D$-open, each $x \in W$ has a $D$-ball about it inside $W$, which by step 2 is a product of open sets. So $W$ is a union of basic product-open sets.

5. So $D$ induces the product topology, which is therefore metrizable.
:::

::: {.solution for="prob-camib-ats-3-q10" status="draft"}
1. Define $\varphi : X \to [0,2]$ by $\varphi(x) = x$ on $[0,1]$ and $\varphi(x) = x - 1$ on $[2,3]$. Its restrictions to the closed pieces are continuous, so $\varphi$ is continuous (gluing lemma, question 8). It is surjective, and $\varphi(x) = \varphi(y)$ iff $x \sim y$ (only $1$ and $2$ share an image).

2. So $\varphi$ induces a bijection $\bar\varphi : X/\sim \to [0,2]$ with $\bar\varphi \circ q = \varphi$, where $q$ is the quotient map. By the universal property of the quotient topology, $\bar\varphi$ is continuous.

3. $X$ is closed and bounded in $\mathbb{R}$, hence compact, so $X/\sim = q(X)$ is compact. $[0,2]$ is Hausdorff.

4. A continuous bijection from a compact space to a Hausdorff space is a homeomorphism. So $X/\sim \cong [0,2]$.
:::

::: {.solution for="prob-camib-ats-3-q11" status="draft"}
(a) $i : X \to X \times \{y\}$, $i(x) = (x,y)$, is a bijection. It is continuous into $X \times Y$ (its components are the identity and a constant), hence into the subspace. Its inverse is the restriction of the projection $\pi_X$, which is continuous. So $i$ is a homeomorphism.

(b)

1. $\pi_X : X \times Y \to X$ is continuous, surjective (as $Y \ne \emptyset$), and $\pi_X(p) = \pi_X(p')$ iff $p \sim p'$. So it induces a continuous bijection $\bar\pi : (X \times Y)/\sim \to X$ with $\bar\pi \circ q = \pi_X$.

2. $\pi_X$ is an open map: it sends a basic open set $U \times V$ ($V \ne \emptyset$) to $U$, and images commute with unions. (For $V = \emptyset$ the image is $\emptyset$.)

3. Let $W$ be open in the quotient. Then $q^{-1}(W)$ is open, and $\bar\pi(W) = \pi_X(q^{-1}(W))$ is open by step 2. So $\bar\pi$ is open, hence a homeomorphism.
:::

::: {.solution for="prob-camib-ats-3-q12" status="draft"}
1. Define $\Phi : \mathbb{R}^2 \to T$ by $\Phi(x,y) = \big((2 + \cos2\pi x)\cos2\pi y, (2 + \cos2\pi x)\sin2\pi y, \sin2\pi x\big)$. It is continuous and surjective.

2. $\Phi(x,y) = \Phi(x',y')$ iff $(x,y) \sim (x',y')$. The "if" direction is periodicity. Conversely, the distance from the $z$-axis is $2 + \cos2\pi x > 0$, so equal images give $\cos2\pi x = \cos2\pi x'$, and the third coordinate gives $\sin2\pi x = \sin2\pi x'$; hence $x - x' \in \mathbb{Z}$. Dividing the first two coordinates by $2 + \cos2\pi x$ gives equal $(\cos2\pi y, \sin2\pi y)$, so $y - y' \in \mathbb{Z}$.

3. So $\Phi$ induces a continuous bijection $\bar\Phi : \mathbb{R}^2/\sim \to T$.

4. Every class meets $[0,1]^2$, so $\mathbb{R}^2/\sim = q([0,1]^2)$ is compact as a continuous image of a compact set. $T \subset \mathbb{R}^3$ is Hausdorff.

5. A continuous bijection from a compact space to a Hausdorff space is a homeomorphism.
:::

::: {.solution for="prob-camib-ats-3-q13" status="draft"}
$Q$ is the "line with two origins". Write $L_\pm = \{(x,\pm1)\}$, the quotient map $q$, and $o_\pm = q(0,\pm1)$. (The relation is taken reflexive, so each point is equivalent to itself.)

(a)

1. Let $U_+ = q(L_+)$. Then $q^{-1}(U_+) = L_+ \cup \{(x,-1) : x \ne 0\}$ is open in $X$, so $U_+$ is open in $Q$.

2. $q|_{L_+} : L_+ \to U_+$ is a continuous bijection. It is open: for $V$ open in $L_+$, $q^{-1}(q(V)) = V \cup \{(x,-1) : (x,1) \in V, x \ne 0\}$, a union of two open sets. So $U_+ \cong L_+ \cong \mathbb{R}$.

3. Likewise $U_- = q(L_-) \cong \mathbb{R}$. Every point of $Q$ lies in $U_+$ or $U_-$.

(b) Let $W_\pm$ be open sets containing $o_\pm$. Then $q^{-1}(W_+)$ is an open set containing $(0,1)$, so it contains $(x,1)$ for $|x| < \varepsilon$; similarly $q^{-1}(W_-)$ contains $(x,-1)$ for $|x| < \varepsilon'$. For $0 < |x| < \min(\varepsilon,\varepsilon')$, the point $q(x,1) = q(x,-1)$ lies in $W_+ \cap W_-$. So $o_+$ and $o_-$ cannot be separated.
:::
