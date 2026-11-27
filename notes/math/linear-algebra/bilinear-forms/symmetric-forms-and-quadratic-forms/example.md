<!-- Added 2026-11-27: the examples of Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 7.1, restated in our own words with our own checks. -->

::: {#exm-quadratic-form-two-variables .example name="Different forms, same quadratic form"}

A symmetric $S\in\operatorname{Mat}_n(F)$ gives the symmetric bilinear form $\varphi(x,y)=x^{\mathsf T}Sy$. For an arbitrary $A\in\operatorname{Mat}_2(\mathbb R)$, the form $x^{\mathsf T}Ay$ has quadratic form
$$q(x,y)=A_{11}x^2+(A_{12}+A_{21})xy+A_{22}y^2 .$$
Only $A_{12}+A_{21}$ enters, so $A$ and its symmetric part $\tfrac12(A+A^{\mathsf T})$ give different bilinear forms when $A\ne A^{\mathsf T}$ but the same $q$. Among all of them exactly one is symmetric, which is what the polarization identity recovers.

:::

::: {#exm-diagonalise-quadratic-form-two-ways .example name="Diagonalising a quadratic form in two ways"}

Let $q(x,y,z)=x^2+y^2+z^2+2xy+4yz+6xz$ on $\mathbb R^3$, with symmetric matrix $A=\begin{bmatrix}1&1&3\\1&1&2\\3&2&1\end{bmatrix}$.

*Following the proof of @thm-symmetric-form-diagonalizable.*

1. $q(e_1)=1\ne0$; take $f_1=e_1$. Then $\varphi(f_1,v)=v_1+v_2+3v_3$.

2. Choose $f_2$ with $\varphi(f_1,f_2)=0$ and $q(f_2)\ne0$: $f_2=(3,0,-1)^{\mathsf T}$ gives $q(f_2)=9+1-18=-8$, and $\varphi(f_2,v)=v_2+8v_3$.

3. Choose $f_3$ orthogonal to both: $v_1+v_2+3v_3=0$ and $v_2+8v_3=0$ give $f_3=(5,-8,1)^{\mathsf T}$, with $q(f_3)=8$.

4. So $q(af_1+bf_2+cf_3)=a^2-8b^2+8c^2$.

*Completing the square.*

1. $q=(x+y+3z)^2-2yz-8z^2$.

2. $-8z^2-2yz=-8\bigl(z+\tfrac y8\bigr)^2+\tfrac18y^2$.

3. So $q=(x+y+3z)^2+\tfrac18y^2-8\bigl(z+\tfrac y8\bigr)^2$.

The two diagonal forms differ, but both have two positive and one negative coefficient, as Sylvester's law of inertia requires.

:::
