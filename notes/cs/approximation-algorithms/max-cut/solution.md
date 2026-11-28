<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6854ps-5-q3" status="draft"}
*(a)* A clause with one literal is satisfied with probability $\tfrac12$; with two literals on different variables, $\tfrac34$; $x\vee\bar x$ always; $x\vee x$ is a one-literal clause. So each clause is satisfied with probability at least $\tfrac12$, and the expected number is at least $k/2\ge\mathrm{OPT}/2$.

*(b) i.* An assignment gives the feasible point $y_i=[x_i\text{ true}]$, $z_j=[C_j\text{ satisfied}]$ with objective equal to its number of satisfied clauses, so $\mathrm{LP}\ge\mathrm{OPT}$.

*ii.* Let $p_1,p_2$ be the probabilities that the literals of $C_j$ are true ($y^*_i$ or $1-y^*_i$), so $p_1+p_2\ge z^*_j$. If $C_j$ has one literal, it is satisfied with probability $p_1\ge z^*_j$. With two literals on different variables, by the AM–GM inequality
$$1-(1-p_1)(1-p_2)\ge1-\Big(1-\frac{p_1+p_2}2\Big)^2\ge1-\Big(1-\frac{z^*_j}2\Big)^2=z^*_j-\frac{z_j^{*2}}4\ge\frac34z^*_j$$
for $z^*_j\in[0,1]$ (the bound $1-(1-z/2)^2$ is increasing in $z$). Clauses $x\vee\bar x$ are always satisfied. Summing, the expectation is at least $\tfrac34\mathrm{LP}\ge\tfrac34\mathrm{OPT}$.

*(c) i.* For an assignment take $v_i=v_0$ if $x_i$ is true and $v_i=-v_0$ otherwise. Then $v(\text{literal})$ is $1$ or $0$ as the literal is true or false, and for $C=x_1\vee x_2$ the value $(3+v_0\cdot v_1+v_0\cdot v_2-v_1\cdot v_2)/4$ is $1$, $1$, $0$ when two, one or no literal is true; negated literals are handled by replacing $v_i$ by $-v_i$. So the NLP value is at least $\mathrm{OPT}$.

*ii.* Let $s_i=\operatorname{sign}(r\cdot v_i)$ and $\theta_{ij}$ the angle between $v_i$ and $v_j$; $x_i$ is true iff $s_i=s_0$. By step 1 of the proof of @thm-goemans-williamson, $\Pr[s_i\ne s_j]=\theta_{ij}/\pi$.

1. *One literal* $x_i$: true with probability $1-\theta_{0i}/\pi$, while $v(x_i)=(1+\cos\theta_{0i})/2$. With $\theta'=\pi-\theta_{0i}$, the definition of $\gamma$ gives $\theta'/\pi\ge\gamma(1-\cos\theta')/2$, i.e. $\Pr\ge\gamma\,v(x_i)$.

2. *Two literals* $x_1\vee x_2$: the identity $[s_1=s_0]+[s_2=s_0]+[s_1\ne s_2]=2\cdot[\,s_1=s_0\text{ or }s_2=s_0\,]$ (check the three cases) gives
$$\Pr[C\text{ satisfied}]=\frac12\Big(\big(1-\tfrac{\theta_{01}}\pi\big)+\big(1-\tfrac{\theta_{02}}\pi\big)+\tfrac{\theta_{12}}\pi\Big),\qquad v(C)=\frac12\Big(\tfrac{1+\cos\theta_{01}}2+\tfrac{1+\cos\theta_{02}}2+\tfrac{1-\cos\theta_{12}}2\Big),$$
and each of the three terms is at least $\gamma$ times its counterpart, as in 1 and in @thm-goemans-williamson. Negations again replace $v_i$ by $-v_i$.

3. Summing, the expected number of satisfied clauses is at least $\gamma\,\mathrm{NLP}\ge\gamma\,\mathrm{OPT}\approx0.878\,\mathrm{OPT}$. The NLP is the semidefinite program in $Y_{ij}=v_i\cdot v_j$ with $Y_{ii}=1$, $Y\succeq0$, solvable to any accuracy.

*(d)* Yes. Adding triangle inequalities to the semidefinite program and rotating the vectors before rounding gives $0.931$ (Feige and Goemans), and refinements reach about $0.940$ (Lewin, Livnat and Zwick), which is best possible under the Unique Games Conjecture (Austrin).
:::
