<!-- Added 2026-11-27: the examples of Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 6.3, restated in our own words with our own checks. -->

::: {#exm-rotation-not-triangulable .example name="A rotation is triangulable only over C"}

Let $R_\theta=\begin{bmatrix}\cos\theta&\sin\theta\\-\sin\theta&\cos\theta\end{bmatrix}$ with $\theta\notin\pi\mathbb Z$. Its characteristic polynomial $t^2-2t\cos\theta+1$ has roots $e^{\pm i\theta}$, which are not real. A real upper triangular matrix similar to $R_\theta$ would have its real diagonal entries as eigenvalues, so none exists. Over $\mathbb C$ the two eigenvalues are distinct, so $R_\theta$ is even diagonalisable. This is why the triangular-form arguments work over $\mathbb C$ (compare @exm-endomorphism-not-diagonalisable).

:::
