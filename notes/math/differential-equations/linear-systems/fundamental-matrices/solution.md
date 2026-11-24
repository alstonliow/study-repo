<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-35-q1" status="draft"}
**(a)** Multiplication by $e^{zt}=e^{at}(\cos bt+i\sin bt)$ gives $A(e^{zt})=e^{at}\begin{pmatrix}\cos bt&-\sin bt\\\sin bt&\cos bt\end{pmatrix}$. The columns of this matrix solve $\dot{\mathbf u}=A(z)\mathbf u$: the first column corresponds to $e^{zt}\cdot1$ and the second to $e^{zt}\cdot i$, and $\frac{d}{dt}(e^{zt}w)=z\,e^{zt}w$ is multiplication by $z$, i.e. by $A(z)$. At $t=0$ it is $I$. By @prp-exponential-fundamental-matrix, $e^{A(z)t}=A(e^{zt})$: the two answers are the same matrix.

**(b)** The roots are $-1\pm i$, so solutions are $e^{-t}(c_1\cos t+c_2\sin t)$. Matching the conditions: $x_1=e^{-t}(\cos t+\sin t)$ and $x_2=e^{-t}\sin t$. For the companion matrix $\begin{pmatrix}0&1\\-2&-2\end{pmatrix}$, the columns of $e^{At}$ are $(x_1,\dot x_1)$ and $(x_2,\dot x_2)$ (they solve the system and equal $I$ at $0$):
$$e^{At}=e^{-t}\begin{pmatrix}\cos t+\sin t&\sin t\\-2\sin t&\cos t-\sin t\end{pmatrix}.$$

**(c)** Let $X=\begin{pmatrix}e^{3t}&e^{2t}\\e^{3t}&2e^{2t}\end{pmatrix}$, a fundamental matrix, with $X(0)^{-1}=\begin{pmatrix}2&-1\\-1&1\end{pmatrix}$.

(i)–(ii) $e^{At}=X(t)X(0)^{-1}=\begin{pmatrix}2e^{3t}-e^{2t}&-e^{3t}+e^{2t}\\2e^{3t}-2e^{2t}&-e^{3t}+2e^{2t}\end{pmatrix}$, and $u_1$, $u_2$ are its first and second columns.

(iii) $A=\frac{d}{dt}e^{At}\big|_{t=0}=\begin{pmatrix}4&-1\\2&1\end{pmatrix}$. Check: $A(1,1)=(3,3)$ and $A(1,2)=(2,4)$.
:::
