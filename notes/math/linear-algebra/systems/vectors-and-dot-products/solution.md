<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-1-q1" status="draft"}
1. In the same way as for $\mathbf{v}$: $\cos\beta=w_1/\lVert\mathbf{w}\rVert$ and $\sin\beta=w_2/\lVert\mathbf{w}\rVert$.

2. Substituting,
   $$\cos\theta=\cos(\beta-\alpha)=\frac{v_1}{\lVert\mathbf{v}\rVert}\frac{w_1}{\lVert\mathbf{w}\rVert}+\frac{w_2}{\lVert\mathbf{w}\rVert}\frac{v_2}{\lVert\mathbf{v}\rVert}=\frac{v_1w_1+v_2w_2}{\lVert\mathbf{v}\rVert\lVert\mathbf{w}\rVert}=\frac{\mathbf{v}\cdot\mathbf{w}}{\lVert\mathbf{v}\rVert\lVert\mathbf{w}\rVert}.$$
:::

::: {.solution for="prob-mit1806s10-1-q2" status="draft"}
Yes. Take three unit vectors $120^\circ$ apart:
$$\mathbf{u}=(1,0),\qquad \mathbf{v}=\big(-\tfrac12,\tfrac{\sqrt3}2\big),\qquad \mathbf{w}=\big(-\tfrac12,-\tfrac{\sqrt3}2\big).$$
Each pair makes an angle of $120^\circ$, so each dot product is $\cos120^\circ=-\frac12<0$. (Four such vectors in the plane are impossible, but three are fine.)
:::

<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-1-q2" status="draft"}
a) $\overrightarrow{P_2P_3}=\overrightarrow{P_2P}-\overrightarrow{P_3P}=\mathbf{v}_2-\mathbf{v}_3$. $P$ is on the altitude from $P_1$ exactly when $\overrightarrow{P_1P}=\mathbf{v}_1$ is perpendicular to the side $P_2P_3$ (or $P=P_1$, which also satisfies this):
$$\mathbf{v}_1\cdot(\mathbf{v}_2-\mathbf{v}_3)=0,\qquad\text{i.e.}\qquad\mathbf{v}_1\cdot\mathbf{v}_2=\mathbf{v}_1\cdot\mathbf{v}_3 .$$

b) In the same way, $P$ on the altitude from $P_2$ means $\mathbf{v}_2\cdot(\mathbf{v}_1-\mathbf{v}_3)=0$, i.e. $\mathbf{v}_2\cdot\mathbf{v}_1=\mathbf{v}_2\cdot\mathbf{v}_3$. Together with (a), $\mathbf{v}_1\cdot\mathbf{v}_2=\mathbf{v}_1\cdot\mathbf{v}_3=\mathbf{v}_2\cdot\mathbf{v}_3$.

c) The condition for the altitude from $P_3$ is $\mathbf{v}_3\cdot(\mathbf{v}_1-\mathbf{v}_2)=0$, i.e. $\mathbf{v}_3\cdot\mathbf{v}_1=\mathbf{v}_3\cdot\mathbf{v}_2$, which follows from (b).
:::

::: {.solution for="prob-mit1802n-1a-q1" status="draft"}
a) $|\mathbf{A}|=\sqrt3$, $\operatorname{dir}\mathbf{A}=\frac1{\sqrt3}(\mathbf{i}+\mathbf{j}+\mathbf{k})$.

b) $|\mathbf{A}|=3$, $\operatorname{dir}\mathbf{A}=\frac13(2\mathbf{i}-\mathbf{j}+2\mathbf{k})$.

c) $|\mathbf{A}|=\sqrt{9+36+4}=7$, $\operatorname{dir}\mathbf{A}=\frac17(3\mathbf{i}-6\mathbf{j}-2\mathbf{k})$.
:::

::: {.solution for="prob-mit1802n-1a-q5" status="draft"}
$\mathbf{A}=3\cos30^\circ\,\mathbf{i}+3\sin30^\circ\,\mathbf{j}=\frac{3\sqrt3}2\mathbf{i}+\frac32\mathbf{j}$. The second condition is not redundant: the plane vectors of length $3$ at $30^\circ$ to $\mathbf{i}$ are $\frac{3\sqrt3}2\mathbf{i}\pm\frac32\mathbf{j}$, and only the one with $+$ makes $60^\circ$ with $\mathbf{j}$ (the other makes $120^\circ$).
:::

::: {.solution for="prob-mit1802n-1a-q6" status="draft"}
Ground velocity $=$ air velocity $+$ wind. The wind blows from the northeast, i.e. towards the southwest: $\mathbf{w}=50\cdot\frac{-\mathbf{i}-\mathbf{j}}{\sqrt2}=-25\sqrt2\,(\mathbf{i}+\mathbf{j})$. We want ground velocity $200\,\mathbf{j}$, so the air velocity is
$$200\,\mathbf{j}-\mathbf{w}=25\sqrt2\,\mathbf{i}+(200+25\sqrt2)\,\mathbf{j}\approx35.4\,\mathbf{i}+235.4\,\mathbf{j}.$$
:::

::: {.solution for="prob-mit1802n-1a-q7" status="draft"}
The rectangle has sides $a\mathbf{i}$ and $b\mathbf{j}$. Turning by $90^\circ$ clockwise sends $\mathbf{i}\to-\mathbf{j}$ and $\mathbf{j}\to\mathbf{i}$; counterclockwise sends $\mathbf{i}\to\mathbf{j}$ and $\mathbf{j}\to-\mathbf{i}$.

a) $\mathbf{A}'=b\,\mathbf{i}-a\,\mathbf{j}$.  b) $\mathbf{A}''=-b\,\mathbf{i}+a\,\mathbf{j}$.

c) $|\mathbf{i}'|=\frac15\sqrt{9+16}=1$. $\mathbf{j}'$ must be $\mathbf{i}'$ turned $90^\circ$ counterclockwise: $\mathbf{j}'=(-4\mathbf{i}+3\mathbf{j})/5$.
:::

::: {.solution for="prob-mit1802n-1a-q8" status="draft"}
a) The $\mathbf{i}$-component of the unit vector $\mathbf{u}=\operatorname{dir}\mathbf{A}$ is $\mathbf{u}\cdot\mathbf{i}=|\mathbf{u}||\mathbf{i}|\cos\alpha=\cos\alpha$; likewise for $\mathbf{j}$ and $\mathbf{k}$.

b) $\cos\alpha=\dfrac a{\sqrt{a^2+b^2+c^2}}$, $\cos\beta=\dfrac b{\sqrt{a^2+b^2+c^2}}$, $\cos\gamma=\dfrac c{\sqrt{a^2+b^2+c^2}}$. For $-\mathbf{i}+2\mathbf{j}+2\mathbf{k}$ (length $3$): $-\frac13,\frac23,\frac23$.

c) If $t,u,v$ are the direction cosines of $\mathbf{A}$, then by (a) $t\mathbf{i}+u\mathbf{j}+v\mathbf{k}$ is the unit vector $\operatorname{dir}\mathbf{A}$, so $t^2+u^2+v^2=1$. Conversely, if $t^2+u^2+v^2=1$, then $\mathbf{A}=t\mathbf{i}+u\mathbf{j}+v\mathbf{k}$ is a unit vector, $\operatorname{dir}\mathbf{A}=\mathbf{A}$, and by (a) its direction cosines are $t,u,v$.
:::

::: {.solution for="prob-mit1802n-1a-q9" status="draft"}
Let the triangle be $PQR$ with $\mathbf{A}=PQ$ and $\mathbf{B}=PR$, and let $M,N$ be the midpoints of $PQ$ and $PR$. Then $PM=\frac12\mathbf{A}$, $PN=\frac12\mathbf{B}$, and
$$MN=PN-PM=\tfrac12(\mathbf{B}-\mathbf{A})=\tfrac12QR .$$
So $MN$ is parallel to $QR$ and half as long.
:::

::: {.solution for="prob-mit1802n-1a-q11" status="draft"}
Let the parallelogram be $OPQR$ with $\mathbf{A}=OP$, $\mathbf{B}=OR$; then $OQ=\mathbf{A}+\mathbf{B}$. The midpoint $X$ of $OQ$ has $OX=\frac12(\mathbf{A}+\mathbf{B})$. The midpoint $Y$ of $PR$ has $OY=OP+\frac12PR=\mathbf{A}+\frac12(\mathbf{B}-\mathbf{A})=\frac12(\mathbf{A}+\mathbf{B})$. So $X=Y$.
:::

::: {.solution for="prob-mit1802n-1b-q1" status="draft"}
a) $\cos\theta=\dfrac{4+0+2}{\sqrt2\cdot6}=\dfrac1{\sqrt2}$, $\theta=\pi/4$.

b) $\cos\theta=\dfrac{2-1+2}{\sqrt6\sqrt6}=\dfrac12$, $\theta=\pi/3$.
:::

::: {.solution for="prob-mit1802n-1b-q2" status="draft"}
The dot product is $c-2-2=c-4$. a) Orthogonal for $c=4$. b) Acute when the dot product is positive: $c>4$.
:::

::: {.solution for="prob-mit1802n-1b-q5" status="draft"}
a) $\mathbf{F}\cdot\frac{\mathbf{i}+\mathbf{j}-\mathbf{k}}{\sqrt3}=\frac{2-2-1}{\sqrt3}=-\frac1{\sqrt3}$.

b) The direction is $\frac17(3\mathbf{i}+2\mathbf{j}-6\mathbf{k})$, and $\mathbf{F}\cdot\frac17(3,2,-6)=\frac{6-4-6}7=-\frac47$.
:::

::: {.solution for="prob-mit1802n-1b-q11" status="draft"}
Let the sides from one vertex be $\mathbf{A}$ and $\mathbf{B}$; the diagonals are $\mathbf{A}+\mathbf{B}$ and $\mathbf{A}-\mathbf{B}$. Then $(\mathbf{A}+\mathbf{B})\cdot(\mathbf{A}-\mathbf{B})=|\mathbf{A}|^2-|\mathbf{B}|^2$, which is $0$ if and only if $|\mathbf{A}|=|\mathbf{B}|$, i.e. all four sides are equal.
:::

::: {.solution for="prob-mit1802n-1b-q12" status="draft"}
Let $O$ be the centre, the diameter run from $-\mathbf{A}$ to $\mathbf{A}$ (as seen from $O$), and $P$ be on the circle with $OP=\mathbf{B}$, $|\mathbf{B}|=|\mathbf{A}|$. The sides of the inscribed angle at $P$ are $\mathbf{A}-\mathbf{B}$ and $-\mathbf{A}-\mathbf{B}$, and
$$(\mathbf{A}-\mathbf{B})\cdot(-\mathbf{A}-\mathbf{B})=-|\mathbf{A}|^2+|\mathbf{B}|^2=0 .$$
:::

::: {.solution for="prob-mit1802n-1b-q13" status="draft"}
$\mathbf{u}_1=\cos\theta_1\mathbf{i}+\sin\theta_1\mathbf{j}$ and $\mathbf{u}_2=\cos\theta_2\mathbf{i}+\sin\theta_2\mathbf{j}$ are unit vectors with angle $\theta_1-\theta_2$ between them (up to sign and multiples of $2\pi$, which do not change the cosine). So $\cos(\theta_1-\theta_2)=\mathbf{u}_1\cdot\mathbf{u}_2=\cos\theta_1\cos\theta_2+\sin\theta_1\sin\theta_2$.
:::

::: {.solution for="prob-mit1802n-1b-q14" status="draft"}
Let the sides from the vertex with angle $\theta$ be $\mathbf{A},\mathbf{B}$, with $|\mathbf{A}|=a$, $|\mathbf{B}|=b$; the third side is $\mathbf{A}-\mathbf{B}$, of length $c$. Then
$$c^2=(\mathbf{A}-\mathbf{B})\cdot(\mathbf{A}-\mathbf{B})=\mathbf{A}\cdot\mathbf{A}-2\mathbf{A}\cdot\mathbf{B}+\mathbf{B}\cdot\mathbf{B}=a^2+b^2-2ab\cos\theta .$$
:::
