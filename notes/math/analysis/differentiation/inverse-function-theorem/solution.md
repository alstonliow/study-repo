<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-ats-4-q12" status="draft"}
Use the operator norm on $M_n$, so $\|AB\| \le \|A\|\|B\|$.

(a) $f(A + H) = A^2 + AH + HA + H^2$. The map $H \mapsto AH + HA$ is linear and $\|H^2\| \le \|H\|^2 = o(\|H\|)$, so $Df|_A(H) = AH + HA$. Moreover $\|(Df|_A - Df|_B)(H)\| = \|(A - B)H + H(A - B)\| \le 2\|A - B\|\|H\|$, so $A \mapsto Df|_A$ is continuous (indeed Lipschitz): $f$ is $C^1$.

(b) $Df|_{\mathrm{Id}}(H) = 2H$ is invertible. By the inverse function theorem there are open sets $U \ni \mathrm{Id}$ and $V \ni f(\mathrm{Id}) = \mathrm{Id}$ such that $f : U \to V$ is a bijection with continuous (indeed $C^1$) inverse. Choose $\varepsilon > 0$ with $B_\varepsilon(\mathrm{Id}) \subset V$ and let $g = f^{-1}$ restricted to it. Then $g(A)^2 = A$.

(c) No: some matrices have no real square root at all. For $n = 1$ take $-1$. In general take $E = \mathrm{diag}(-1, 0, \dots, 0)$. If $B^2 = E$, the eigenvalues of $B^2$ (with algebraic multiplicity) are the squares of those of $B$. To get $-1$, $B$ needs an eigenvalue $\pm i$; non-real eigenvalues of a real matrix come in conjugate pairs with equal multiplicity, and both $i$ and $-i$ square to $-1$. So $-1$ would have multiplicity at least $2$ in $B^2 = E$, but it has multiplicity $1$.
:::

::: {.solution for="prob-camib-ats-4-q16" status="draft"}
Write $D_xf$ ($m\times n$) and $D_yf$ ($m\times m$) for the blocks of $Df$; the hypothesis says $D_yf(x_0,y_0)$ is invertible. Write $G = (G_x, G_y)$ with $G_x \in \mathbb{R}^n$, $G_y \in \mathbb{R}^m$.

(a) $F : U \to \mathbb{R}^{n+m}$ is $C^1$ with
$$DF = \begin{pmatrix} I_n & 0 \\ D_xf & D_yf\end{pmatrix}, \qquad \det DF|_{(x_0,y_0)} = \det D_yf(x_0,y_0) \ne 0.$$
By the inverse function theorem there are open $W \ni (x_0,y_0)$ and $V \ni F(x_0,y_0) = (x_0,0)$ such that $F : W \to V$ is a bijection with $C^1$ inverse $G : V \to W$.

(b) For $(X,Z) \in V$, $F(G(X,Z)) = (X,Z)$. The first block says $G_x(X,Z) = X$, and the second then says $f(X, G_y(X,Z)) = Z$. With $Z = 0$: $f(X, G_y(X,0)) = 0$.

(c)

1. Shrinking $W$, we may take $W = W_1 \times W''$, a product of open sets inside $U$, and $V = F(W)$ (open, as $G$ is continuous).

2. Let $W' = \{x \in W_1 : (x,0) \in V\}$, open and containing $x_0$, and $g(x) = G_y(x,0)$ for $x \in W'$. Then $g(x) \in W''$, $g(x_0) = y_0$ (as $G(x_0,0) = (x_0,y_0)$), and $f(x,g(x)) = 0$ by (b).

3. Uniqueness: if $x \in W'$, $y \in W''$ and $f(x,y) = 0$, then $(x,y), (x,g(x)) \in W$ and $F(x,y) = (x,0) = F(x,g(x))$. As $F$ is injective on $W$, $y = g(x)$.

(d) $g = G_y(\cdot,0)$ is $C^1$ because $G$ is. Differentiating $f(x,g(x)) = 0$ by the chain rule gives $D_xf + D_yf\cdot Dg = 0$, and $D_yf$ is invertible near $(x_0,y_0)$ (its determinant is continuous), so
$$Dg(x) = -\big(D_yf(x,g(x))\big)^{-1}D_xf(x,g(x)).$$

(e)

1. Let $\Phi(x,y) = x^3 + y^3 - 3xy$, so $\partial_y\Phi = 3(y^2 - x)$. By (c) with $n = m = 1$, near every point of $C$ where $\partial_y\Phi \ne 0$, $C$ is the graph of a $C^1$ function $y = g(x)$.

2. On $C$, $\partial_y\Phi = 0$ means $x = y^2$, and then $\Phi = y^6 - 2y^3 = 0$, so $y = 0$ or $y^3 = 2$. These are the points $(0,0)$ and $(2^{2/3}, 2^{1/3})$.

3. So $C$ is locally graphical away from small neighbourhoods of these two points. (At $(2^{2/3},2^{1/3})$, $\partial_x\Phi = 3(x^2 - y) = 3\cdot2^{1/3} \ne 0$, so there $C$ is instead locally a graph $x = h(y)$, with a vertical tangent.)
:::
