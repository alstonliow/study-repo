::: {.problem #prob-mit18065ps-7-q10 origin="external" source="mit18065ps-7-q10"}
If $A$ is a 2 by 2 matrix with $\sigma_1\ge\sigma_2>0$, find $\lVert A^{-1}\rVert_2$ and $\lVert A^{-1}\rVert_F^2$.
:::

::: {.problem #prob-mit18065ps-8-q1 origin="external" source="mit18065ps-8-q1"}
Show directly this fact about $\ell^1$ and $\ell^2$ and $\ell^\infty$ vector norms : $\lVert\mathbf{v}\rVert_2^2\le\lVert\mathbf{v}\rVert_1\lVert\mathbf{v}\rVert_\infty$.
:::

::: {.problem #prob-mit18065ps-8-q7 origin="external" source="mit18065ps-8-q7"}
A short proof of $\lVert AB\rVert_F\le\lVert A\rVert_F\lVert B\rVert_F$ starts from multiplying rows times columns :

$\lvert(AB)_{ij}\rvert^2\le\lVert\text{row } i \text{ of } A\rVert^2\,\lVert\text{column } j \text{ of } B\rVert^2$ is the Cauchy-Schwarz inequality

Add up both sides over all $i$ and $j$ to show that $\lVert AB\rVert_F^2\le\lVert A\rVert_F^2\lVert B\rVert_F^2$.
:::

::: {.problem #prob-mit18065ps-11-q6 origin="external" source="mit18065ps-11-q6"}
The first page of I.11 shows unit balls for the $\ell^1$ and $\ell^2$ and $\ell^\infty$ norms. Those are the three sets of vectors $\mathbf{v}=(v_1,v_2)$ with $\lVert\mathbf{v}\rVert_1\le1$, $\lVert\mathbf{v}\rVert_2\le1$, $\lVert\mathbf{v}\rVert_\infty\le1$. Unit balls are always convex because of the triangle inequality for vector norms :
$$\text{If }\lVert\mathbf{v}\rVert\le1\text{ and }\lVert\mathbf{w}\rVert\le1\text{ show that }\Big\lVert\frac{\mathbf{v}}2+\frac{\mathbf{w}}2\Big\rVert\le1 .$$
:::
