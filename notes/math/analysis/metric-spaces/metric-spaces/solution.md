<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-ats-1-q6" status="draft"}
(a) Not a metric for $n \ge 2$: $d((0,0,\dots),(0,1,0,\dots)) = 0$ for distinct points. (For $n = 1$ it is the usual metric.)

(b) A metric.

1. $d \ge |z - w|$ always, since $|z| + |w| \ge |z - w|$; so $d(z,w) = 0$ iff $z = w$. Symmetry is clear.

2. Triangle inequality $d(z,w) \le d(z,u) + d(u,w)$. If $z, w$ lie on one line through $0$: $d(z,w) = |z - w| \le |z - u| + |u - w| \le d(z,u) + d(u,w)$ by step 1.

3. Otherwise $d(z,w) = |z| + |w|$. Then $u$ cannot lie on the lines of both $z$ and $w$ unless $u = 0$, and $d(z,0) + d(0,w) = |z| + |w|$. If $u \ne 0$ is on the line of $z$ only: $d(z,u) + d(u,w) = |z - u| + |u| + |w| \ge |z| + |w|$. The case of the line of $w$ is symmetric. If $u$ is on neither line: $d(z,u) + d(u,w) = |z| + 2|u| + |w| \ge |z| + |w|$.

(c) A metric, even an ultrametric. Write $N(x,y)$ for the first index where $x$ and $y$ differ. $d \ge 0$, $d = 0$ iff $x = y$, and $d$ is symmetric. Given $x, y, z$ with $x \ne y$, let $N = N(x,y)$. At index $N$, $z$ differs from $x$ or from $y$, so $N(x,z) \le N$ or $N(z,y) \le N$. Hence $\max\{d(x,z), d(z,y)\} \ge 2^{-N} = d(x,y)$, which is stronger than the triangle inequality.

(d) A metric (the Hausdorff distance). Write $d_0(a,B) = \inf_{b\in B}d_0(a,b)$.

1. $d(A,B)$ is finite: fix $a_0 \in A$, $b_0 \in B$; for $a \in A$, $d_0(a,B) \le d_0(a,a_0) + d_0(a_0,b_0) < r_A + d_0(a_0,b_0)$. Symmetry and $d \ge 0$ are clear.

2. If $d(A,B) = 0$, then $d_0(a,B) = 0$ for every $a \in A$, so $a$ is a limit of points of $B$; as $B$ is closed, $a \in B$. So $A \subset B$, and symmetrically $B \subset A$.

3. Triangle inequality. For $a \in A$, $b \in B$: $d_0(a,C) \le d_0(a,b) + d_0(b,C) \le d_0(a,b) + d(B,C)$. Taking the infimum over $b$: $d_0(a,C) \le d_0(a,B) + d(B,C) \le d(A,B) + d(B,C)$. So $\sup_{a}d_0(a,C) \le d(A,B) + d(B,C)$, and the same argument with the roles of $A$ and $C$ exchanged bounds $\sup_c d_0(c,A)$. Hence $d(A,C) \le d(A,B) + d(B,C)$.
:::

::: {.solution for="prob-camib-ats-1-q7" status="draft"}
1. $d_1$ (Hamming distance): $d_1 = 0$ iff $s = s'$, and it is symmetric. If $s[i] \ne s''[i]$ then $s[i] \ne s'[i]$ or $s'[i] \ne s''[i]$, so $\{i : s[i] \ne s''[i]\} \subset \{i : s[i] \ne s'[i]\} \cup \{i : s'[i] \ne s''[i]\}$, which gives the triangle inequality.

2. $d_2$ (edit distance; intermediate strings may have any length): $d_2$ is a non-negative integer and $0$ iff $s = s'$. Each operation can be undone by one operation (insertion by deletion, deletion by insertion, substitution by substitution), so reversing a sequence of edits shows symmetry. Doing an optimal edit sequence from $s$ to $s'$ followed by one from $s'$ to $s''$ changes $s$ into $s''$, so $d_2(s,s'') \le d_2(s,s') + d_2(s',s'')$.

3. They are equivalent for every $L$. Substitutions alone turn $s$ into $s'$, so $d_2 \le d_1$. For $s \ne s'$, $d_2 \ge 1$ and $d_1 \le L$, so $d_1 \le Ld_2$. Thus $d_2 \le d_1 \le Ld_2$: they are Lipschitz equivalent, and in particular induce the same (discrete) topology on the finite set $X_L$.

4. The constant $L$ cannot be improved in general: for $s = abab\ldots$ and $s' = baba\ldots$ of even length $L$, $d_1 = L$ while $d_2 \le 2$ (delete the first letter, then append one at the end). So the metrics are not uniformly equivalent as $L$ varies.
:::
