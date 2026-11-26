<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18433-2-q1" status="draft"}
1. Let $B$ be the triangle $v,x,y$ with three pendant vertices: $r$ joined to $v$, $p$ to $x$, $q$ to $y$. Let $M=\{xy\}$. Then $v$ is exposed and $B$ is a blossom with empty stem.

2. $G/B$ is a star with centre $b$ and leaves $r,p,q$, so a maximum matching $M^*$ of $G/B$ has one edge, say $bp$, coming from $xp$. Adding $\frac12(|B|-1)=1$ edge of $B$ to cover the rest of $B$ gives $\{xp,vy\}$, with $2$ edges. But $\{vr,xp,yq\}$ is a matching of $G$ with $3$ edges.

3. This does not contradict @thm-blossom-shrinking. The theorem compares one matching $M$ with *its own* shrinking $M/B$: here $M/B=\varnothing$ is not maximum in $G/B$, and correspondingly $M$ is not maximum in $G$. It does not claim that $\nu(G)=\nu(G/B)+\frac12(|B|-1)$ in general; after augmenting, $B$ need not be a blossom any more, and a maximum matching of $G$ may use several edges leaving $B$, which no matching of $G/B$ can represent.
:::
