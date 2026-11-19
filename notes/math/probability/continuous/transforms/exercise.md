::: {.problem #prob-eecs126hw-6-q3 origin="external" source="eecs126hw-6-q3"}
**Transform Practice.** Consider a random variable $Z$ with transform
$$M_Z(s)=\frac{a-3s}{s^2-6s+8},\quad\text{for }|s|<2.$$
Calculate the following quantities:

(a) The numerical value of the parameter $a$.

(b) $E[Z]$.

(c) $\operatorname{var}(Z)$.
:::

::: {.problem #prob-eecs126hw-6-q4 origin="external" source="eecs126hw-6-q4"}
**Rotationally Invariant Random Variables.** Suppose random variables $X$ and $Y$ are i.i.d., with zero mean, such that their joint density is rotation invariant, i.e. for any orthogonal matrix $U$ with orthonormal rows and orthonormal columns,
$$U\begin{pmatrix}X\\Y\end{pmatrix}\overset{d}{=}\begin{pmatrix}X\\Y\end{pmatrix}.$$

(a) Let $\phi(t)$ be the characteristic function of $X$. Show that $\phi(t)^n=\phi(\sqrt nt)$.

(b) Show that $\phi(t)=\exp(ct^2)$ for some constant $c$, and all $t$ such that $t^2\in\mathbb Q$. Hint: Let $t^2=a/b$, where $a,b$ are positive integers.

(c) Conclude that $X$ and $Y$ must be Gaussians.
:::
