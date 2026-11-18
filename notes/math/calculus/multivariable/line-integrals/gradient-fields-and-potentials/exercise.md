::: {.problem #prob-mit1802f07-8-q2 origin="external" source="mit1802f07-8-q2"}
Consider the vector field $\vec F(x,y)=\dfrac{-y\,\hat{\imath}+x\,\hat{\jmath}}{x^2+y^2}$.

a) Show that $\vec F$ is the gradient of the polar angle function $\theta(x,y)=\tan^{-1}(y/x)$ defined over the right half-plane $x>0$. (Note: this formula for $\theta$ does not make sense for $x=0$!)

b) Suppose that $C$ is a smooth curve in the right half-plane $x>0$ joining two points $A:(x_1,y_1)$ and $B:(x_2,y_2)$. Express $\int_C\vec F\cdot d\vec r$ in terms of the polar coordinates $(r_1,\theta_1)$ and $(r_2,\theta_2)$ of $A$ and $B$.

c) Compute directly from the definition the line integrals $\int_{C_1}\vec F\cdot d\vec r$ and $\int_{C_2}\vec F\cdot d\vec r$, where $C_1$ is the upper half of the unit circle running from $(1,0)$ to $(-1,0)$, and $C_2$ is the lower half of the unit circle, also going from $(1,0)$ to $(-1,0)$.

d) Show that the curl of $\vec F$ is zero at any point of the plane where $\vec F$ is defined (not just in the right half-plane $x>0$).

e) Using the results of parts (a)-(d), is $\vec F$ conservative (path-independent) over its entire domain of definition? Is it conservative over the right half-plane $x>0$? Justify your answers.

Note: in fact it is true that $\vec F=\nabla\theta$ everywhere. However, the polar angle $\theta$ cannot be defined as a single-valued differentiable function everywhere (if you try, you will find that it is only well-deﬁned up to adding multiples of $2\pi$). This is why in parts (a) and (b) we only consider the right half-plane; any other region over which $\theta$ can be defined unambiguously in a continuous manner would be equally suitable.
:::

::: {.problem #prob-mit1802f07-8-q3 origin="external" source="mit1802f07-8-q3"}
a) Calculate the curl of $\vec F=r^n(x\,\hat{\imath}+y\,\hat{\jmath})$ (where $r=\sqrt{x^2+y^2}$; start by finding formulas for $r_x$ and $r_y$).

b) Whenever possible, find a potential $g$ such that $\vec F=\nabla g$. (Hint: look for a potential of the form $g=g(r)$, with $r=\sqrt{x^2+y^2}$. Watch out for a certain negative value of $n$ for which the general formula doesn't work.)
:::

::: {.problem #prob-mit1802n-4c-q5 origin="external" source="mit1802n-4c-q5"}
For each of the following, tell for what value of the constants the field will be a gradient field, and for this value, find the corresponding (mathematical) potential function.

a) $\mathbf{F}=(y^2+2x)\mathbf{i}+axy\mathbf{j}$  b) $\mathbf{F}=e^{x+y}\big((x+a)\mathbf{i}+x\mathbf{j}\big)$

*Note (these notes):* Part (a) by method 1 and part (b) by method 2 of Notes V2 (Problem Set 8).
:::

::: {.problem #prob-mit1802n-4c-q6 origin="external" source="mit1802n-4c-q6"}
Decide which of the following differentials is exact. For each one that is exact, express it in the form $df$.

a) $y\,dx-x\,dy$  b) $y(2x+y)\,dx+x(2y+x)\,dy$

*Note (these notes):* Parts (a) and (b) were assigned, by both methods of Notes V2.
:::
