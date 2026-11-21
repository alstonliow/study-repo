<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18065ps-14-q1" status="draft"}
1. Regroup each power: $(\mathbf{u}\mathbf{v}^{\mathsf T})^k=\mathbf{u}(\mathbf{v}^{\mathsf T}\mathbf{u})^{k-1}\mathbf{v}^{\mathsf T}$, because the inner products $\mathbf{v}^{\mathsf T}\mathbf{u}$ are numbers. This gives the second line.

2. The bracket is the scalar series $1+x+x^2+\cdots=1/(1-x)$ with $x=\mathbf{v}^{\mathsf T}\mathbf{u}$, valid for $\lvert x\rvert<1$. So $(I-\mathbf{u}\mathbf{v}^{\mathsf T})^{-1}=I+\mathbf{u}\mathbf{v}^{\mathsf T}/(1-\mathbf{v}^{\mathsf T}\mathbf{u})$.

3. The series argument needs $\lvert\mathbf{v}^{\mathsf T}\mathbf{u}\rvert<1$, but the final formula holds whenever $\mathbf{v}^{\mathsf T}\mathbf{u}\ne1$, as direct multiplication shows (@thm-sherman-morrison with $A=I$).
:::

::: {.solution for="prob-mit18065ps-14-q4" status="draft"}
1. Write $c=\mathbf{v}^{\mathsf T}\mathbf{x}/D$. Using $A\mathbf{x}=\mathbf{b}$ and $A\mathbf{z}=\mathbf{u}$:
$$(A-\mathbf{u}\mathbf{v}^{\mathsf T})(\mathbf{x}+c\mathbf{z})=\mathbf{b}+c\mathbf{u}-\mathbf{u}(\mathbf{v}^{\mathsf T}\mathbf{x})-c\,\mathbf{u}(\mathbf{v}^{\mathsf T}\mathbf{z}).$$

2. Collect the $\mathbf{u}$ terms: $\mathbf{u}\big[c(1-\mathbf{v}^{\mathsf T}\mathbf{z})-\mathbf{v}^{\mathsf T}\mathbf{x}\big]=\mathbf{u}\big[cD-\mathbf{v}^{\mathsf T}\mathbf{x}\big]=\mathbf{0}$.

3. So $M\mathbf{y}=\mathbf{b}$ (assuming $D\ne0$, the condition for $M$ to be invertible).
:::
