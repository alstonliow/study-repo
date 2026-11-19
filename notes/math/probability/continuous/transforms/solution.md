<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-6-q3" status="draft"}
(a) $M_Z(0)=E[e^0]=1$, so $a/8=1$ and $a=8$.

(b)–(c) Partial fractions: $\frac{8-3s}{(s-2)(s-4)}=\frac12\cdot\frac{2}{2-s}+\frac12\cdot\frac{4}{4-s}$, so $Z$ is an equal mixture of $\operatorname{Exp}(2)$ and $\operatorname{Exp}(4)$ (uniqueness, @thm-transform-properties). Hence
$$E[Z]=\tfrac12\cdot\tfrac12+\tfrac12\cdot\tfrac14=\tfrac38,\qquad E[Z^2]=\tfrac12\cdot\tfrac2{4}+\tfrac12\cdot\tfrac2{16}=\tfrac5{16},\qquad\operatorname{var}(Z)=\tfrac5{16}-\tfrac9{64}=\tfrac{11}{64}.$$
(Differentiating $M_Z$ at $0$ gives the same: $M_Z'(0)=\frac38$, $M_Z''(0)=\frac5{16}$.)
:::

::: {.solution for="prob-eecs126hw-6-q4" status="draft"}
(a) The first row of a rotation is any unit vector $(\alpha,\beta)$, so $\alpha X+\beta Y\overset d=X$, and by independence $\phi(\alpha t)\phi(\beta t)=\phi(t)$ whenever $\alpha^2+\beta^2=1$. By induction on $n$: the case $n=1$ is trivial, and with $\alpha=\sqrt{n/(n+1)}$, $\beta=\sqrt{1/(n+1)}$ applied at $\sqrt{n+1}\,t$,
$$\phi(\sqrt{n+1}\,t)=\phi(\sqrt n\,t)\,\phi(t)=\phi(t)^{n+1}.$$

(b) Rotation by $\pi$ gives $-X\overset d=X$, so $\phi$ is real; and $\phi(t)=\phi(t/\sqrt2)^2\ge0$. Using (a) twice, for $t^2=a/b$:
$$\phi(t)^b=\phi(\sqrt b\,t)=\phi(\sqrt a)=\phi(1)^a.$$
If $\phi(1)=0$ then $\phi(t)=0$ for every $t$ with $t^2$ rational, contradicting continuity at $\phi(0)=1$. So $\phi(1)=e^c$ for some $c\le0$, and taking the non-negative $b$-th root, $\phi(t)=e^{ca/b}=e^{ct^2}$.

(c) Characteristic functions are continuous and $\{t:t^2\in\mathbb Q\}$ is dense, so $\phi(t)=e^{ct^2}$ for all $t$. If $c=0$, $X=0$ (a degenerate Gaussian); otherwise $\phi$ is the characteristic function of $N(0,-2c)$, and by uniqueness $X$ and $Y$ are $N(0,-2c)$.
:::
