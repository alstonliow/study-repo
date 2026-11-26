<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18433-5-q11" status="draft"}
1. *$\dim\ge|S|$.* The points $0$ and $\chi_{\{e\}}$, $e\in S$, belong to $X$ and are affinely independent ($|S|+1$ points).

2. *$\dim\le|S|$.* An element $e\notin S$ (a *loop*) lies in no independent set, so every point of $X$, hence of $\operatorname{conv}(X)$, has $x_e=0$. These $|E\setminus S|$ equations are linearly independent, so $\operatorname{conv}(X)$ lies in an affine space of dimension $|S|$.

3. *Equalities in the description.* For a loop $e$, $r(\{e\})=0$, so $P$ contains the rows $x_e\le0$ and $x_e\ge0$: the implicit equalities $x_e=0$. These are $|E|-|S|=|E|-\dim P$ linearly independent equalities (by @thm-matroid-polytope, $P=\operatorname{conv}(X)$ has dimension $|S|$), exactly as many as a minimal description needs (@thm-facets-describe-polyhedra).
:::

::: {.solution for="prob-mit18433-5-q12" status="draft"}
The vertices of $P$ are the $\chi_I$, $I\in\mathcal I$. We use: $I_1,I_2$ are adjacent iff some weight $c$ is maximised over $\mathcal I$ exactly by $I_1$ and $I_2$ (exercise 3-9 with $-c$).

*If.* (i) Let $I_2=I_1+e$; put $c_f=1$ on $I_1$, $c_e=0$ and $c_f=-1$ elsewhere. The maximum $|I_1|$ is attained exactly by the independent $I$ with $I_1\subseteq I\subseteq I_1+e$, i.e. by $I_1$ and $I_2$. (ii) is symmetric. (iii) Let $I_1=J+a$, $I_2=J+b$ with $J+a+b\notin\mathcal I$; put $c=2$ on $J$, $c=1$ on $a,b$, $c=-1$ elsewhere. An $I$ with $|I\cap J|\le|J|-1$ has $c(I)\le2|J|-2+2=2|J|$. An $I\supseteq J$ can contain at most one of $a,b$; the value $2|J|+1$ needs exactly one and nothing else. So $J+a$, $J+b$ are the only maximisers.

*Only if.* Let $I_1,I_2$ be the only maximisers of $c$.

1. If $I_1\subsetneq I_2$: $c(I_2\setminus I_1)=0$, and each $a\in I_2\setminus I_1$ has $c_a\le0$ (else $I_1+a$ beats $I_1$), so all $c_a=0$ and every $I_1+a$ is a maximiser. Uniqueness forces $|I_2\setminus I_1|=1$: case (i). Similarly for (ii).

2. Otherwise $D_1=I_1\setminus I_2$ and $D_2=I_2\setminus I_1$ are non-empty. Every $e\in I_1\cup I_2$ has $c_e>0$: $c_e<0$ would let us drop $e$, and $c_e=0$ with $e\in I_1$ would make $I_1-e$ a third maximiser (it is not $I_2$, as $D_2\ne\varnothing$). So $I_1$ and $I_2$ are bases of $M$ restricted to $E^+=\{c>0\}$ (otherwise they could be extended), and $|D_1|=|D_2|=m$.

3. If $m=1$, $I_1\cup I_2$ has more elements than a base of $M|E^+$, so it is dependent: case (iii).

4. If $m\ge2$: by the exchange lemma for equal-size independent sets (stated with @def-exchange-graph) there is a bijection $\sigma:D_2\to D_1$ with $J_b=I_1-\sigma(b)+b\in\mathcal I$ for all $b\in D_2$. Then $c(J_b)\le c(I_1)$ gives $c_b\le c_{\sigma(b)}$; summing, $c(D_2)\le c(D_1)$, with equality since $c(I_1)=c(I_2)$. So every $c_b=c_{\sigma(b)}$ and each $J_b$ is a maximiser. But $J_b\ne I_1$ and $J_b\ne I_2$ (it misses $m-1\ge1$ elements of $D_2$): a contradiction.
:::

::: {.solution for="prob-mit18433ps-6-q5" status="draft"}
Assume $x\ge0$ (otherwise a violated $x_e\ge0$ is returned) and $x(E)=|V|-1$; write $n=|V|$.

(a) $u(\{s\})=\sum_vx(\delta(v))=2x(E)=2(n-1)$, and $u(\{s\}\cup V)=\sum_v2=2n$.

(b) For $\varnothing\ne S\subseteq V$, the arcs leaving $\{s\}\cup S$ are $s\to v$ for $v\notin S$, $v\to t$ for $v\in S$, and the arcs from $S$ to $V\setminus S$. So
$$u(\{s\}\cup S)=\sum_{v\notin S}x(\delta(v))+2|S|+x(\delta(S)).$$
Since $\sum_{v\notin S}x(\delta(v))=2x(E(V\setminus S))+x(\delta(S))$ and $x(E)=x(E(S))+x(\delta(S))+x(E(V\setminus S))$, this equals $2x(E)-2x(E(S))+2|S|=2n-2+2|S|-2x(E(S))$. It is less than $2n$ iff $x(E(S))>|S|-1$. For $S=V$ the value is exactly $2n$, so the minimum is below $2n$ iff some proper $S\subset V$ violates its inequality, and the minimising $S$ gives the violated inequality.

(c) For each $v\in V$, raise the capacity of $s\to v$ to $\infty$ and compute a minimum $s$–$t$ cut (one maximum flow). This is the minimum of $u(\{s\}\cup S)$ over $S\ni v$. The smallest of the $n$ answers is $\min_{S\ne\varnothing}u(\{s\}\cup S)$, which decides membership by (b).
:::
