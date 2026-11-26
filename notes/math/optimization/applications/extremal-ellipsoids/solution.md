<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-ee364ahw-6-q4" status="draft"}
1. Write $a_i^T$ for the rows of $A$, and split each into positive and negative parts, $a_i=a_i^+-a_i^-$ with $(a_i^+)_j=\max\{a_{ij},0\}$ and $(a_i^-)_j=\max\{-a_{ij},0\}$.

2. $\mathcal R\subseteq\mathcal P$ iff $\max_{x\in\mathcal R}a_i^Tx\le b_i$ for every $i$. The maximum of a linear function over a box is taken coordinate by coordinate: $x_j=u_j$ where $a_{ij}>0$ and $x_j=l_j$ where $a_{ij}<0$. So
$$\max_{l\preceq x\preceq u}a_i^Tx=(a_i^+)^Tu-(a_i^-)^Tl,$$
and the containment is the $m$ linear inequalities $A^+u-A^-l\preceq b$, with $A^\pm$ the matrices of rows $(a_i^\pm)^T$. This avoids the $2^n$ vertex constraints.

3. The volume is $\prod_j(u_j-l_j)$; maximizing its logarithm gives the convex problem
$$\begin{array}{ll}\text{maximize}&\sum_{j=1}^n\log(u_j-l_j)\\ \text{subject to}&A^+u-A^-l\preceq b,\end{array}$$
with implicit constraint $l\prec u$. The objective is concave (a sum of $\log$ of affine functions) and the constraints are linear, in the same spirit as the inscribed ellipsoid of @def-max-inscribed-ellipsoid.
:::

::: {.solution for="prob-mit6854ps-4-q4" status="draft"}
Here $nE(a,A)=E(a,n^2A)$, the ellipsoid scaled by $n$ about its centre.

*1. Reduction.* An affine bijection maps ellipsoids to ellipsoids, convex hulls to convex hulls, and multiplies all volumes by the same factor. So assume $E$ is the unit ball $B$ and, after a rotation, $b=(\beta,0,\dots,0)$ with $\beta>n$.

*Candidate.* For small $\varepsilon>0$ let $E'$ have centre $(\varepsilon,0,\dots,0)$, semi-axis $1+\varepsilon$ along $e_1$ and $r=\sqrt{1-\eta}$ in the other directions, with $\eta=2\kappa\varepsilon$ for a constant $\kappa$ with $\frac1{\beta-1}<\kappa<\frac1{n-1}$ (possible since $\beta>n$).

*Volume.* $\operatorname{vol}E'/\operatorname{vol}B=(1+\varepsilon)(1-\eta)^{(n-1)/2}=1+\varepsilon\big(1-(n-1)\kappa\big)+O(\varepsilon^2)>1$ for small $\varepsilon$.

*Containment.* Compare support functions in a unit direction $u$ with $u_1=c$: $h_{\operatorname{conv}(B\cup\{b\})}(u)=\max(1,\beta c)$ and
$$h_{E'}(u)=\varepsilon c+\sqrt{(1+\varepsilon)^2c^2+(1-\eta)(1-c^2)}=1+\varepsilon g(c)+O(\varepsilon^2),\quad g(c)=(1+c)\big(c-\kappa(1-c)\big),$$
uniformly in $c$. Now $g(c)<0$ for $-1<c\le\frac1\beta$ (as $c<\kappa(1-c)$ there, using $\kappa>\frac1{\beta-1}$), $g(-1)=0$ with $h_{E'}=1$ exactly at $c=-1$, and for $c>\frac1\beta$ the right side $\beta c-1$ is positive. A compactness argument (split $[-1,1]$ into a neighbourhood of $-1$, where one expands to second order, a middle part where $g<0$, and the part $c\ge\frac1\beta+\delta$ where $\beta c-1\ge\beta\delta$) shows $h_{E'}\le\max(1,\beta c)$ for all $u$ once $\varepsilon$ is small. So $E'\subseteq\operatorname{conv}(B\cup\{b\})$ and $E'$ has larger volume.

*2.* Assume $K$ has non-empty interior (otherwise work in its affine hull). The ellipsoids inside $\bar K$ form a compact family with continuous volume, so one of maximum volume, $E$, exists. If some $b\in K$ were outside $nE$, then by 1 the set $\operatorname{conv}(E\cup\{b\})\subseteq K$ would contain an ellipsoid of larger volume: a contradiction. Hence $K\subseteq nE$. This proves the second half of @thm-ellipsoid-efficiency in the form stated here.

*3.* Write $E=\{Bu+a:\lVert u\rVert\le1\}$ with $B\succ0$. Then $E\subseteq K$ iff $\sup_{\lVert u\rVert\le1}c_i^T(Bu+a)=\lVert Bc_i\rVert+c_i^Ta\le d_i$ for every row $c_i$ of $C$, and $\operatorname{vol}E$ is proportional to $\det B$. So maximise the concave function $\log\det B$ over $B\succ0$, $a$, subject to the convex constraints $\lVert Bc_i\rVert+c_i^Ta\le d_i$ (@def-max-inscribed-ellipsoid).
:::
