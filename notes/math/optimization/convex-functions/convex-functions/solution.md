<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-ee364ahw-2-q2" status="draft"}
1. *Halfspace.* $\mathbf{epi}\,f$ is a halfspace iff $f$ is affine (with $\mathbf{dom}\,f=\mathbf{R}^n$). If $f(x)=a^Tx+b$, then $\mathbf{epi}\,f=\{(x,t)\mid a^Tx-t\le-b\}$. Conversely, a halfspace $\{(x,t)\mid c^Tx+\gamma t\le d\}$ that is an epigraph must contain $(x,t')$ for all $t'\ge t$ whenever it contains $(x,t)$, so $\gamma<0$ ($\gamma=0$ would make it a vertical halfspace, not an epigraph of a real-valued function); then $(x,t)\in\mathbf{epi}\,f$ iff $t\ge(c^Tx-d)/(-\gamma)$, an affine function.

2. *Convex cone.* $\mathbf{epi}\,f$ is a convex cone iff $f$ is convex and positively homogeneous: $f(\alpha x)=\alpha f(x)$ for $\alpha\ge0$. Convexity of the set is convexity of $f$ (@prp-epigraph-convex). The cone property says $(x,t)\in\mathbf{epi}\,f\Rightarrow(\alpha x,\alpha t)\in\mathbf{epi}\,f$, that is, $f(\alpha x)\le\alpha f(x)$ for all $\alpha\ge0$; applying it with $1/\alpha$ to $\alpha x$ gives the reverse inequality for $\alpha>0$. (At $\alpha=0$ it says $f(0)\le0$, and $f(0)=0$ follows from $f(0)=f(2\cdot0)=2f(0)$.)

3. *Polyhedron.* $\mathbf{epi}\,f$ is a polyhedron iff $f$ is convex and piecewise affine: $f(x)=\max_{i=1,\ldots,m}(a_i^Tx+b_i)$ on a polyhedral domain $\{x\mid Cx\preceq d\}$. Such an epigraph is $\{(x,t)\mid a_i^Tx+b_i\le t,\ Cx\preceq d\}$. Conversely, a polyhedral epigraph is described by finitely many inequalities; those involving $t$ must have negative coefficient on $t$ (as in part 1), and solving each for $t$ shows $f$ is the maximum of the resulting affine functions on the set cut out by the others.
:::
