::: {.problem #prob-mit18s096ps-1-q2 origin="external" source="mit18s096ps-1-q2"}
Calculate derivatives of each of the following functions in the requested forms---as a linear operator $f'(x)[dx]$, a Jacobian matrix, or a gradient $\nabla f$ ---as specified in each part.

(a) $f(x) = x^T (A + \operatorname{diagm}(x))^2 x$, where the inputs $x \in \mathbb{R}^n$ are vectors, the outputs are scalars, $A = A^T$ is a constant *symmetric* $n\times n$ matrix $\in \mathbb{R}^{n\times n}$, and $\operatorname{diagm}(x)$ denotes the $n\times n$ diagonal matrix $\begin{pmatrix} x_1 & & \\ & x_2 & \\ & & \ddots \end{pmatrix}$. Give the **gradient** $\nabla f$, such that $f'(x)dx = (\nabla f)^T dx$.

(b) $f(x) = (A + yx^T)^{-1} b$, where the inputs $x$ and outputs $f(x)$ are $n$-component (column) vectors in $\mathbb{R}^n$, $y$ and $b$ are constant vectors $\in \mathbb{R}^n$, and $A$ is a constant $n\times n$ matrix $\in \mathbb{R}^{n\times n}$.

  (i) Give $f'(x)$ as a **Jacobian** matrix.

  (ii) If you are given $A^{-1}$, then you can compute $(A + yx^T)^{-1}$ and hence $f(x)$ for any $x$ in $\sim n^2$ scalar-arithmetic operations (i.e., roughly proportional to $n^2$, or in computer-science terms $\Theta(n^2)$ "complexity"), using the "Sherman--Morrison" formula (Google it). **Explain** how your Jacobian matrix can therefore also be computed in $\sim n^2$ operations for any $x$ given $A^{-1}$ (i.e. give a sequence of computational steps, each of which costs no more than $\sim n^2$ arithmetic).

(c) $f(x) = \frac{xx^T}{x^T x}$, with vector inputs $x \in \mathbb{R}^n$ and matrix outputs $f\in \mathbb{R}^{n\times n}$. Give $f'(x)$ as a linear operator, i.e. a linear formula for $f'(x)[dx]$.

(d) $g(x) = \frac{xx^T}{x^T x} b$, with vector inputs $x \in \mathbb{R}^n$ and vector outputs $f\in \mathbb{R}^n$, where $b \in \mathbb{R}^n$ is a constant vector. Give $g'(x)$ as a **Jacobian** matrix.
:::

::: {.problem #prob-mit18s096ps-2-q2 origin="external" source="mit18s096ps-2-q2"}
Suppose that we have a two-argument function $f(x,y)$, where $x,y$ and $f$ may belong to arbitrary vector (Banach) spaces. Let's define "partial" derivatives $f_{x}$ and $f_{y}$ (also denoted $\frac{\partial f}{\partial x}$ and $\frac{\partial f}{\partial y}$) by the linearization:
$$
df=f(x+dx,y+dy)-f(x,y)=f_{x}(x,y)[dx]+f_{y}(x,y)[dy],
$$
implicitly dropping higher-order terms as usual. Compute the partial derivatives of the following functions:

(a) $f(A,x)=A^{-1}x$ for $n\times n$ matrices $A\in\mathbb{R}^{n\times n}$ and vectors $x\in\mathbb{R}^{n}$: give $f_{A}$ as a linear operator, and $f_{x}$ as a Jacobian matrix.

(b) $f(A,B)=\operatorname{tr}(A^{T}BA)$, for matrices $A,B\in\mathbb{R}^{n\times n}$: give the gradients $\nabla_{A}f$ and $\nabla_{B}f$ such that $f_{A}[dA]=\nabla_{A}f\cdot dA$ and $f_{B}[dB]=\nabla_{B}f\cdot dB$ under the Frobenius inner product $X\cdot Y=\operatorname{tr}(X^{T}Y)=\operatorname{tr}(Y^{T}X)$.
:::
