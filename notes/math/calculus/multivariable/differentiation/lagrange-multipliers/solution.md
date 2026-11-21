<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-5-q3" status="draft"}
a) Minimise $f=(x-2)^2+(y+1)^2+(z-1)^2$ subject to $g=x^2+yz=2$. $\nabla f=\lambda\nabla g$ gives
$$2(x-2)=2\lambda x,\qquad 2(y+1)=\lambda z,\qquad 2(z-1)=\lambda y,\qquad x^2+yz=2 .$$

b) Adding the second and third equations: $2(y+z)=\lambda(y+z)$, so $z=-y$ or $\lambda=2$.

- $z=-y$: then $x=\frac2{1-\lambda}$ and $2(y+1)=-\lambda y$ gives $y=-\frac2{2+\lambda}$. The constraint $x^2-y^2=2$ becomes $\frac4{(1-\lambda)^2}-\frac4{(2+\lambda)^2}=2$, i.e. $(1-\lambda)^2(2+\lambda)^2-6(1+2\lambda)=0$, or $\lambda^4+2\lambda^3-3\lambda^2-16\lambda-2=0$. Its real roots are $\lambda\approx-0.1283$ and $\lambda\approx2.3448$. The first gives $(1.7725,-1.0686,1.0686)$ at distance $0.2473$, the second $(-1.4872,-0.4603,0.4603)$ at distance $3.570$. The closest point is $(1.7725,-1.0686,1.0686)$.
- $\lambda=2$: the first equation gives $x=-2$, the other two both say $z=y+1$, and the constraint becomes $4+y(y+1)=2$, i.e. $y^2+y+2=0$, which has no real solution. So this case gives no point at all.

The estimate $(\frac{16}9,-\frac{19}{18},\frac{19}{18})\approx(1.7778,-1.0556,1.0556)$ has $x$ within $\frac1{100}$ (error $0.0053$), but $y$ and $z$ are off by $0.013$, slightly more than $\frac1{100}$.
:::

::: {.solution for="prob-mit1802n-2i-q1" status="draft"}
Maximise $V=xyz$ with $x,y,z\ge0$ on the surface.

a) $\nabla V=\lambda\nabla f$: $yz=\lambda$, $xz=2\lambda$, $xy=3\lambda$. Then $xyz=\lambda x=2\lambda y=3\lambda z$, so $x=2y=3z$, and $x+2y+3z=3x=18$: $P=(6,3,2)$, $V=36$. The part of the plane in the first octant is a closed triangle on whose edges $V=0$; $V$ is continuous and positive inside, so its maximum is at an interior critical point, and this is the only one.

b) $yz=2\lambda x$, $xz=4\lambda y$, $xy=8\lambda z$. Multiplying by $x,y,z$: $xyz=2\lambda x^2=4\lambda y^2=8\lambda z^2$, so $x^2=2y^2=4z^2$, and each of the three terms of the constraint equals $4$: $P=(2,\sqrt2,1)$, $V=2\sqrt2$. It is the maximum by the same argument ($V=0$ on the edges of the closed piece of ellipsoid in the first octant).
:::

::: {.solution for="prob-mit1802n-2i-q3" status="draft"}
Minimise $A=2xz+4yz+3xy$ subject to $xyz=1$ (length $x$, width $y$, height $z$). $\nabla A=\lambda\nabla(xyz)$:
$$2z+3y=\lambda yz,\qquad4z+3x=\lambda xz,\qquad2x+4y=\lambda xy .$$
Multiplying by $x$, $y$, $z$ respectively: $2xz+3xy=4yz+3xy=2xz+4yz\ (=\lambda)$. The first equality gives $x=2y$, the second $3xy=2xz$, i.e. $z=\frac32y$. Proportions $4:2:3$, as in 2F-2.
:::

::: {.solution for="prob-mit18065ps-24-q1" status="draft"}
1. (a) With the sign that makes (e) come out as stated: $L(\mathbf{x},\lambda)=\frac12x_1^2+2x_2^2+\lambda(x_1+3x_2-b)$.

2. (b) $\partial L/\partial x_1=x_1+\lambda=0$, $\;\partial L/\partial x_2=4x_2+3\lambda=0$, $\;\partial L/\partial\lambda=x_1+3x_2-b=0$.

3. (c) $x_1=-\lambda$, $x_2=-\frac34\lambda$; then $-\lambda-\frac94\lambda=b$ gives $\lambda^*=-\frac{4b}{13}$ and $\mathbf{x}^*=\big(\frac{4b}{13},\frac{3b}{13}\big)$.

4. (d) The level sets $\frac12x_1^2+2x_2^2=c$ are ellipses (circles only after rescaling $x_2$), centred at the origin. The minimiser is where the line $x_1+3x_2=b$ touches the smallest such ellipse; there the gradient $(x_1,4x_2)$ is parallel to the normal $(1,3)$ of the line: $(4b/13,12b/13)=\frac{4b}{13}(1,3)$.

5. (e) $F^*=\frac12\big(\frac{4b}{13}\big)^2+2\big(\frac{3b}{13}\big)^2=\frac{26b^2}{169}=\frac{2b^2}{13}$, so $\partial F^*/\partial b=\frac{4b}{13}=-\lambda^*$.
:::
