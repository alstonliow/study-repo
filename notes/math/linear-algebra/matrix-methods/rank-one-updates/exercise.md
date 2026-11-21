::: {.problem #prob-mit18065ps-14-q1 origin="external" source="mit18065ps-14-q1"}
Another approach to $(I-\mathbf{u}\mathbf{v}^{\mathsf T})^{-1}$ starts with the formula for a geometric series : $(1-x)^{-1}=1+x+x^2+x^3+\cdots$ Apply that formula when $x=\mathbf{u}\mathbf{v}^{\mathsf T}=$ matrix :
$$\begin{aligned}(I-\mathbf{u}\mathbf{v}^{\mathsf T})^{-1}&=I+\mathbf{u}\mathbf{v}^{\mathsf T}+\mathbf{u}\mathbf{v}^{\mathsf T}\mathbf{u}\mathbf{v}^{\mathsf T}+\mathbf{u}\mathbf{v}^{\mathsf T}\mathbf{u}\mathbf{v}^{\mathsf T}\mathbf{u}\mathbf{v}^{\mathsf T}+\cdots\\&=I+\mathbf{u}\,[1+\mathbf{v}^{\mathsf T}\mathbf{u}+\mathbf{v}^{\mathsf T}\mathbf{u}\mathbf{v}^{\mathsf T}\mathbf{u}+\cdots]\,\mathbf{v}^{\mathsf T}.\end{aligned}$$
Take $x=\mathbf{v}^{\mathsf T}\mathbf{u}$ to see $I+\dfrac{\mathbf{u}\mathbf{v}^{\mathsf T}}{1-\mathbf{v}^{\mathsf T}\mathbf{u}}$. This is exactly equation (1) for $(I-\mathbf{u}\mathbf{v}^{\mathsf T})^{-1}$.
:::

::: {.problem #prob-mit18065ps-14-q4 origin="external" source="mit18065ps-14-q4"}
Problem 3 found the inverse matrix $M^{-1}=(A-\mathbf{u}\mathbf{v}^{\mathsf T})^{-1}$. In solving the equation $M\mathbf{y}=\mathbf{b}$, we compute only the solution $\mathbf{y}$ and not the whole inverse matrix $M^{-1}$. You can find $\mathbf{y}$ in two easy steps :

Step 1  Solve $A\mathbf{x}=\mathbf{b}$ and $A\mathbf{z}=\mathbf{u}$. Compute $D=1-\mathbf{v}^{\mathsf T}\mathbf{z}$.

Step 2  Then $\mathbf{y}=\mathbf{x}+\dfrac{\mathbf{v}^{\mathsf T}\mathbf{x}}{D}\mathbf{z}$ is the solution to $M\mathbf{y}=(A-\mathbf{u}\mathbf{v}^{\mathsf T})\mathbf{y}=\mathbf{b}$.

Verify $(A-\mathbf{u}\mathbf{v}^{\mathsf T})\mathbf{y}=\mathbf{b}$. We solved two equations using $A$, no equations using $M$.
:::
