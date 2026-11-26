::: {.problem #prob-mit18433-5-q11 origin="external" source="mit18433-5-q11"}
Let $M=(E,\mathcal I)$ be a matroid and let $S=\{e\in E:\{e\}\in\mathcal I\}$. Show that $\dim(\operatorname{conv}(X))=|S|$ (where $X$ is the set of incidence vectors of independent sets) and show that the description for $P$ has the required number of linearly independent equalities.
:::

::: {.problem #prob-mit18433-5-q12 origin="external" source="mit18433-5-q12"}
Let $M=(E,\mathcal I)$ be a matroid and let $P$ be the corresponding matroid polytope, i.e. the convex hull of characteristic vectors of independent sets. Show that two independent sets $I_1$ and $I_2$ are adjacent on $P$ if and only if either (i) $I_1\subseteq I_2$ and $|I_1|+1=|I_2|$, or (ii) $I_2\subseteq I_1$ and $|I_2|+1=|I_1|$, or (iii) $|I_1\setminus I_2|=|I_2\setminus I_1|=1$ and $I_1\cup I_2\notin\mathcal I$.
:::

::: {.problem #prob-mit18433ps-6-q5 origin="external" source="mit18433ps-6-q5"}
While discussing the matroid polytope, we derived that the spanning tree polytope of a graph $G=(V,E)$ is given by (read again the notes on matroid optimization):
$$P=\{x\in\mathbb R^{|E|}:\ x(E)=|V|-1,\quad x(E(S))\le|S|-1\ \ S\subset V,\quad 0\le x_e\ \ e\in E\},$$
where as usual $x(F)=\sum_{e\in F}x_e$.

If we wanted to use the ellipsoid to optimize over $P$, we would need to solve the separation problem: Given $x$, is $x\in P$ and if not, provide a valid inequality for $P$ violated by $x$. We can easily check whether $x(E)=|V|-1$ so in what follows we assume that the given $x$ already satisfies $x(E)=|V|-1$. We are now going to show that the separation problem can be solved by solving $|V|$ maximum flow problems.

Consider the following directed graph $D=(V\cup\{s,t\},A)$. $A$ has three types of arcs:

- For any $v\in V$, $D$ has an arc $(s,v)$ with capacity $u((s,v))=x(\delta(v))$,
- for any $v\in V$, $D$ has an arc $(v,t)$ with capacity $u((v,t))=2$,
- for any $(u,v)\in E$, $D$ has the arcs $(u,v)$ and $(v,u)$ both of capacity $x_{uv}$.

(a) In $D$, what is the capacity of the cut induced by $\{s\}$ and by $\{s\}\cup V$?

(b) Show that there exists a violated inequality for $x$ (satisfying $x(E)=|V|-1$) if and only if the value of the following cut problem is less than $2|V|$:
$$\min_{S\subseteq V,S\ne\emptyset}u(\{s\}\cup S).$$
(Notice that we are not allowing the cut to be induced by $\{s\}$.)

(c) Show that the separation problem can be solved by $|V|$ maximum flow problems (in $|V|$ networks obtained by slightly modifying $D$).

*Note (these notes):* the original adds in a footnote that optimising over $P$ alone is easier with the greedy algorithm; separation matters when further constraints are added.
:::
