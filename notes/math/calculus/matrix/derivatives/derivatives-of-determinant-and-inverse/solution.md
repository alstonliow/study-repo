<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit18s096ps-1-q2" status="draft"}
(a) Put $M=A+\operatorname{diagm}(x)$, which is symmetric, and $D=\operatorname{diagm}(dx)$, so $dM=D$.

1. By the product rule, $df=dx^{\mathsf T}M^2x+x^{\mathsf T}M^2dx+x^{\mathsf T}(D\,M+M\,D)\,x$.

2. The first two terms are equal scalars ($M^2$ is symmetric): together $2(M^2x)^{\mathsf T}dx$.

3. $x^{\mathsf T}DMx$ and $x^{\mathsf T}MDx$ both equal $\sum_ix_i(Mx)_i\,dx_i$, since $D$ is diagonal. Together $2\bigl(x\circ Mx\bigr)^{\mathsf T}dx$, where $\circ$ is the elementwise product, and $x\circ Mx=\operatorname{diagm}(x)Mx$.

4. Hence $\nabla f=2M^2x+2\operatorname{diagm}(x)Mx=2\bigl(A+2\operatorname{diagm}(x)\bigr)\bigl(A+\operatorname{diagm}(x)\bigr)x$.

(b)(i) Put $B=A+yx^{\mathsf T}$. By @thm-differential-inverse, $df=-B^{-1}(dB)B^{-1}b=-B^{-1}y\,(dx^{\mathsf T}f)$. The factor $dx^{\mathsf T}f=f^{\mathsf T}dx$ is a scalar, so

$$f'(x)=-\bigl(B^{-1}y\bigr)\,f(x)^{\mathsf T},$$

a rank-one $n\times n$ Jacobian.

(ii) Sherman–Morrison (@sec-math-linear-algebra-matrix-methods-rank-one-updates) gives $B^{-1}=A^{-1}-\dfrac{A^{-1}yx^{\mathsf T}A^{-1}}{1+x^{\mathsf T}A^{-1}y}$. Steps:

1. $u=A^{-1}y$ and $w=A^{-1}b$: two matrix–vector products, $\sim n^2$.
2. $f=w-u\,\dfrac{x^{\mathsf T}w}{1+x^{\mathsf T}u}$ and $B^{-1}y=\dfrac{u}{1+x^{\mathsf T}u}$: dot products and vector updates, $\sim n$.
3. $J=-\bigl(B^{-1}y\bigr)f^{\mathsf T}$: an outer product, $n^2$ multiplications.

No step multiplies two matrices, so the total is $\sim n^2$. (A Python check with $n=4$ confirms both formulas.)

(c) By the quotient rule, with $d(x^{\mathsf T}x)=2x^{\mathsf T}dx$,

$$f'(x)[dx]=\frac{dx\,x^{\mathsf T}+x\,dx^{\mathsf T}}{x^{\mathsf T}x}-\frac{2\,(x^{\mathsf T}dx)}{(x^{\mathsf T}x)^2}\,xx^{\mathsf T}.$$

(d) Apply (c) to $b$: $dg=f'(x)[dx]\,b=\dfrac{(x^{\mathsf T}b)\,dx+x\,(b^{\mathsf T}dx)}{x^{\mathsf T}x}-\dfrac{2(x^{\mathsf T}b)}{(x^{\mathsf T}x)^2}x\,(x^{\mathsf T}dx)$, using $dx^{\mathsf T}b=b^{\mathsf T}dx$. Collecting the coefficient of $dx$,

$$g'(x)=\frac{(x^{\mathsf T}b)\,I+x\,b^{\mathsf T}}{x^{\mathsf T}x}-\frac{2\,(x^{\mathsf T}b)}{(x^{\mathsf T}x)^2}\,xx^{\mathsf T}.$$

All four answers were checked against centred differences in Python.
:::

::: {.solution for="prob-mit18s096ps-2-q2" status="draft"}
(a) By the product rule and @thm-differential-inverse, $df=d(A^{-1})\,x+A^{-1}dx=-A^{-1}dA\,A^{-1}x+A^{-1}dx$. So $f_A[dA]=-A^{-1}\,dA\,A^{-1}x$ (a linear map from matrices to vectors) and $f_x=A^{-1}$.

(b) 1. Changing $A$: $df=\operatorname{tr}(dA^{\mathsf T}BA)+\operatorname{tr}(A^{\mathsf T}B\,dA)$. The first trace equals its transpose $\operatorname{tr}(A^{\mathsf T}B^{\mathsf T}dA)$, so $df=\operatorname{tr}\bigl(A^{\mathsf T}(B+B^{\mathsf T})dA\bigr)=\operatorname{tr}\bigl(((B+B^{\mathsf T})A)^{\mathsf T}dA\bigr)$, and $\nabla_Af=(B+B^{\mathsf T})A$.

2. Changing $B$: $df=\operatorname{tr}(A^{\mathsf T}dB\,A)=\operatorname{tr}(AA^{\mathsf T}dB)$ by the cyclic property, and $AA^{\mathsf T}$ is symmetric, so $\nabla_Bf=AA^{\mathsf T}$.

Both gradients agree with centred differences in Python for random $4\times4$ matrices.
:::
