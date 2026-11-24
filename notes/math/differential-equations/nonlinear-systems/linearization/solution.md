<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-37-q1" status="draft"}
**(a)**

1. From $x'=0$: $y=\tfrac x2+\tfrac{x^2}8$.
2. Substituting in $5x-y-y^2=0$ and multiplying by $64$: $-x(x-4)(x^2+12x+72)=0$.
3. The roots are $0$, $4$ and $-6\pm6i$; the last two are not real, so give no critical points.
4. $x=0$ gives $y=0$, and $x=4$ gives $y=2+2=4$. The critical points are $(0,0)$ and $(4,4)$.

**(b)** The Jacobian is $J=\begin{pmatrix}1+\frac x2&-2\\5&-1-2y\end{pmatrix}$.

- At $(0,0)$: $J=\begin{pmatrix}1&-2\\5&-1\end{pmatrix}$, $T=0$, $\Delta=9$: eigenvalues $\pm3i$, a center, turning counterclockwise (lower-left entry positive).
- At $(4,4)$: $J=\begin{pmatrix}3&-2\\5&-9\end{pmatrix}$, $\Delta=-17$: a saddle with eigenvalues $-3\pm\sqrt{26}\approx2.10,\,-8.10$; eigenvectors from the first row $(3-\lambda)u=2v$: about $(1,0.45)$ (outgoing) and $(1,5.55)$ (incoming).

Guess: near the origin trajectories circle counterclockwise; near $(4,4)$ they follow the saddle's four separatrices; some of the separatrices of the saddle bound the region of circling orbits around the origin.
:::

::: {.solution for="prob-mit1803ps-37-q2" status="draft"}
- $(4,4)$ is a saddle, which is structurally stable (@def-structural-stability). By @thm-linearization the nonlinear system has a saddle there too: near $(4,4)$ the picture is certainly the linear one, with two incoming and two outgoing trajectories tangent to the eigenvectors.
- $(0,0)$ is a center, a borderline type, so it is not structurally stable. The theorem only says that the nonlinear trajectories near it turn counterclockwise around it; they may close up (a nonlinear center) or spiral slowly in or out.

So the saddle part of the guess-sketch is guaranteed, while the closed orbits drawn around the origin are only a guess.
:::
