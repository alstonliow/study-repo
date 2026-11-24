<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit18s096ps-1-q0" status="draft"}
Write $v=(x,y)^{\mathsf T}$ and $R(\phi)=\begin{bmatrix}\cos\phi&\sin\phi\\-\sin\phi&\cos\phi\end{bmatrix}$, so rotate$(\theta)$ is $v\mapsto R(\theta)v$.

(a) The map is linear, $v\mapsto R(\theta)v$, so its Jacobian is the matrix itself: $J=\begin{bmatrix}\cos\theta&\sin\theta\\-\sin\theta&\cos\theta\end{bmatrix}$.

(b) Again linear: $J=\begin{bmatrix}\cosh\theta&\sinh\theta\\\sinh\theta&\cosh\theta\end{bmatrix}$.

(c) The first output is $x$, the second $y+\theta x^2$, so $J=\begin{bmatrix}1&0\\2\theta x&1\end{bmatrix}$.

(d) Here $w(v)=R(\phi)v$ with $\phi=\theta r$, $r=\sqrt{x^2+y^2}$.

1. By the product rule, $dw=R(\phi)\,dv+R'(\phi)\,v\,d\phi$, with $R'(\phi)=\begin{bmatrix}-\sin\phi&\cos\phi\\-\cos\phi&-\sin\phi\end{bmatrix}$.

2. From $r^2=v^{\mathsf T}v$, $2r\,dr=2v^{\mathsf T}dv$, so $d\phi=\theta\,dr=\dfrac{\theta}{r}v^{\mathsf T}dv$ (for $r\neq0$).

3. Hence $dw=\Bigl(R(\phi)+\dfrac{\theta}{r}\,R'(\phi)\,v\,v^{\mathsf T}\Bigr)dv$, and the Jacobian is $J=R(\theta r)+\dfrac{\theta}{r}\,R'(\theta r)\,v\,v^{\mathsf T}$: a rotation plus a rank-one correction. A centred-difference check in Python at $\theta=0.7$, $v=(0.3,-1.1)$ agrees to seven digits.
:::

::: {.solution for="prob-mit18s096ps-1-q1" status="draft"}
(a) $f(x+dx)-f(x)=L[x+dx]+y-L[x]-y=L[dx]$ exactly, with no higher-order term. So $f'(x)=L$ for every $x$: the derivative of an affine map is its linear part, and the constant $y$ drops out.

(b) Transposition is linear with $y=0$, so $f'(A)[dA]=dA^{\mathsf T}$. The trace is linear and $1$ is a constant, so $g'(A)[dA]=\operatorname{tr}(dA)$; under the Frobenius inner product $\operatorname{tr}(dA)=\operatorname{tr}(I^{\mathsf T}dA)$, so $\nabla g=I$.
:::
