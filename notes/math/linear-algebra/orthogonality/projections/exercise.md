::: {.problem #prob-mit1806s10-5-q6 origin="external" source="mit1806s10-5-q6"}
Suppose $A$ is the $4\times4$ identity matrix with its last column removed. $A$ is $4\times3$. Project $\mathbf{b}=(1,2,3,4)$ onto the column space of $A$. What shape is the projection matrix $P$ and what is $P$?
:::

::: {.problem #prob-mit1806s10-5-q7 origin="external" source="mit1806s10-5-q7"}
What linear combination of $(1,2,-1)$ and $(1,0,1)$ is closest to $\mathbf{b}=(2,1,1)$?
:::

::: {.problem #prob-mit1806s10-5-q8 origin="external" source="mit1806s10-5-q8"}
If $P^2=P$ show that $(I-P)^2=I-P$. When $P$ projects onto the column space of $A$, $I-P$ projects onto the \_\_\_\_\_.
:::

::: {.problem #prob-mit1806s10-5-q9 origin="external" source="mit1806s10-5-q9"}
a. Find the projection matrix $P_C$ ontot he column space of $A$.
$$A=\begin{bmatrix}3&6&6\\4&8&8\end{bmatrix}.$$

b. Find the $3\times3$ projection matrix $P_R$ onto the row space of $A$. Multiply $B=P_CAP_R$. Your answer $B$ should be a little suprising — can you explain it?
:::

::: {.problem #prob-mit1806s10-5-q10 origin="external" source="mit1806s10-5-q10"}
In $\mathbb{R}^m$, suppose I give you $\mathbf{b}$ and $\mathbf{p}$, and $n$ linearly independent vectors $\mathbf{a}_1,\dots,\mathbf{a}_n$. How would you test to see if $\mathbf{p}$ is the projection of $\mathbf{b}$ onto the subspace spanned by the $\mathbf{a}$'s?
:::

::: {.problem #prob-mit18065ps-10-q17 origin="external" source="mit18065ps-10-q17"}
Problems 12 and 17 use four data points $\mathbf{b}=(0,8,8,20)$ to bring out the key ideas.


Project $\mathbf{b}=(0,8,8,20)$ onto the line through $\mathbf{a}=(1,1,1,1)$. Find $\widehat{x}=\mathbf{a}^{\mathsf T}\mathbf{b}/\mathbf{a}^{\mathsf T}\mathbf{a}$ and the projection $\mathbf{p}=\widehat{x}\mathbf{a}$. Check that $\mathbf{e}=\mathbf{b}-\mathbf{p}$ is perpendicular to $\mathbf{a}$, and find the shortest distance $\lVert\mathbf{e}\rVert$ from $\mathbf{b}$ to the line through $\mathbf{a}$.
:::
