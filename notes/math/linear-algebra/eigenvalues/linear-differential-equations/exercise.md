::: {.problem #prob-mit1806s10-8-q1 origin="external" source="mit1806s10-8-q1"}
The matrix in this question is skew-symmetric ($A^{\mathsf T}=-A$):
$$\frac{d\mathbf{u}}{dt}=\begin{bmatrix}0&c&-b\\-c&0&a\\b&-a&0\end{bmatrix}\mathbf{u}\qquad\text{or}\qquad\begin{aligned}u_1'&=cu_2-bu_3\\u_2'&=au_3-cu_1\\u_3'&=bu_1-au_2\end{aligned}$$

(a) The derivative of $\lVert\mathbf{u}(t)\rVert^2=u_1^2+u_2^2+u_3^3$ is $2u_1u_1'+2u_2u_2'+2u_3u_3'$. Substitute $u_1',u_2',u_3'$ to get *zero*. Then $\lVert\mathbf{u}(t)\rVert^2$ stays equal to $\lVert\mathbf{u}(0)\rVert^2$.

(b) *When $A$ is skew-symmetric, $Q=e^{At}$ is orthogonal.* Prove $Q^{\mathsf T}=e^{-At}$ from the series for $Q=e^{At}$. Then $Q^{\mathsf T}Q=I$.

*Note (these notes):* $u_3^3$ is a misprint for $u_3^2$.
:::

::: {.problem #prob-mit1806s10-8-q2 origin="external" source="mit1806s10-8-q2"}
Write $A=\begin{bmatrix}1&3\\0&0\end{bmatrix}$ as $S\Lambda S^{-1}$. Multiply $Se^{\Lambda t}S^{-1}$ to find the matrix exponential $e^{At}$. Check $e^{At}$ and the derivative of $e^{At}$ when $t=0$.
:::

::: {.problem #prob-mit1806s10-8-q3 origin="external" source="mit1806s10-8-q3"}
Centering $y''=-y$ in Example 3 will produce $Y_{n+1}-2Y_n+Y_{n-1}=-(\Delta t)^2Y_n$. This can be written as a one-step difference equation for $U=(Y,Z)$:
$$\begin{aligned}Y_{n+1}&=Y_n+\Delta t\,Z_n\\Z_{n+1}&=Z_n-\Delta t\,Y_{n+1}\end{aligned}\qquad\begin{bmatrix}1&0\\\Delta t&1\end{bmatrix}\begin{bmatrix}Y_{n+1}\\Z_{n+1}\end{bmatrix}=\begin{bmatrix}1&\Delta t\\0&1\end{bmatrix}\begin{bmatrix}Y_n\\Z_n\end{bmatrix}.$$
Invert the matrix on the left side to write this as $U_{n+1}=AU_n$. Show that $\det A=1$. Choose the large time step $\Delta t=1$ and find the eigenvalues $\lambda_1$ and $\lambda_2=\bar\lambda_1$ of $A$:
$$A=\begin{bmatrix}1&1\\-1&0\end{bmatrix}\text{ has }\lvert\lambda_1\rvert=\lvert\lambda_2\rvert=1.\text{ Show that }A^6\text{ is exactly }I.$$
After 6 steps to $t=6$, $U_6$ equals $U_0$. The exact $y=\cos t$ returns to 1 at $t=2\pi$.
:::

::: {.problem #prob-mit1806s10-8-q4 origin="external" source="mit1806s10-8-q4"}
The centered choice (*leapfrog method*) in Problem 28 is very successful for small time steps $\Delta t$. But find the eigenvalues of $A$ for $\Delta t=\sqrt2$ and $2$:
$$A=\begin{bmatrix}1&\sqrt2\\-\sqrt2&-1\end{bmatrix}\qquad\text{and}\qquad A=\begin{bmatrix}1&2\\-2&-3\end{bmatrix}$$
Both matrices have $\lvert\lambda\rvert=1$. Compute $A^4$ in both cases and find the eigenvectors of $A$. That value $\Delta t=2$ is at the border of instability. Time steps $\Delta t>2$ will lead to $\lvert\lambda\rvert>1$, and the powers in $U_n=A^nU_0$ will explode.

*Note* You might say that nobody would compute with $\Delta t>2$. But if an atom vibrates with $y''=-1000000y$, then $\Delta t>.0002$ will give instability. Leapfrog has a very strict stability limit. $Y_{n+1}=Y_n+3Z_n$ and $Z_{n+1}=Z_n-3Y_{n+1}$ will explode because $\Delta t=3$ is too large.

*Note (these notes):* Problem 28 is @prob-mit1806s10-8-q3.
:::

::: {.problem #prob-mit1806s10-8-q5 origin="external" source="mit1806s10-8-q5"}
Another good idea for $y''=-y$ is the trapezoidal method (half forward/half back): This may be the best way to keep $(Y_n,Z_n)$ exactly on a circle.
$$\text{Trapezoidal}\qquad\begin{bmatrix}1&-\Delta t/2\\\Delta t/2&1\end{bmatrix}\begin{bmatrix}Y_{n+1}\\Z_{n+1}\end{bmatrix}=\begin{bmatrix}1&\Delta t/2\\-\Delta t/2&1\end{bmatrix}\begin{bmatrix}Y_n\\Z_n\end{bmatrix}$$

(a) Invert the left matrix to write this equation as $U_{n+1}=AU_n$. Show that $A$ is an orthogonal matrix: $A^{\mathsf T}A=I$. These points $U_n$ never leave the circle. $A=(I-B)^{-1}(I+B)$ is always an orthogonal matrix if $B^{\mathsf T}=-B$.

(b) (Optional MATHLAB) Take 32 steps from $U_0=(1,0)$ to $U_{32}$ with $\Delta t=2\pi/32$. Is $U_{32}=U_0$? I think there is a small error.
:::
