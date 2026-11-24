<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18335-38-q2" status="draft"}
**(a)**

1. *Key identity.* For real $a$ with $|a|\le2$ put $b=\sqrt{2-a}$, which is real with $0\le b\le2$. Then
$$(z^{2M}+bz^M+1)(z^{2M}-bz^M+1)=(z^{2M}+1)^2-b^2z^{2M}=z^{4M}+(2-b^2)z^{2M}+1=z^{4M}+az^{2M}+1.$$
Both factors have the required form, with real coefficients $\pm b$, $|\pm b|\le2$, and $M$ halved.

2. *Start.* $z^N-1=(z^{N/2}-1)(z^{N/2}+1)$, and $z^{N/2}+1=z^{2M}+0\cdot z^M+1$ with $M=N/4$ (for $N\ge4$).

3. *Recursion.* Factor $z^{N/2}-1$ by step 2 again, down to $z^2-1=(z-1)(z+1)$. Split each $z^{2M}+az^M+1$ with $M\ge2$ by step 1 into two such factors with $M/2$. The degrees halve each time, so this ends with quadratics $z^2+az+1$ ($M=1$, $|a|\le2$) and the linear factors $z\mp1$.

4. *Last step.* For $|a|\le2$ write $a=-2\cos\theta$. Then $z^2+az+1=(z-e^{i\theta})(z-e^{-i\theta})$, a conjugate pair on the unit circle. These are $N$-th roots of unity because the quadratic divides $z^N-1$. All constants before this step are real.

**(b)** With $N=8$, $y_k=x(\omega^k)$, $\omega=e^{-2\pi i/8}$, inputs complex. A complex addition costs $2$ real additions, and a complex number times a real constant costs $2$ real multiplications.

1. *Mod $z^4\mp1$.* Since $z^4\equiv\pm1$: $r_n=x_n+x_{n+4}$ and $c_n=x_n-x_{n+4}$ for $n=0,\dots,3$. This is $8$ complex additions.

2. *Mod $z^2\mp1$ of $r$.* $s_n=r_n+r_{n+2}$ and $t_n=r_n-r_{n+2}$ for $n=0,1$. This is $4$ complex additions.

3. *Mod $z^2\pm\sqrt2z+1$ of $c=c_0+c_1z+c_2z^2+c_3z^3$.* Modulo $z^2+\sqrt2z+1$ we have $z^2\equiv-\sqrt2z-1$ and $z^3\equiv z+\sqrt2$; modulo $z^2-\sqrt2z+1$, $z^2\equiv\sqrt2z-1$ and $z^3\equiv z-\sqrt2$. With $A=c_0-c_2$, $C=c_1+c_3$, $B=\sqrt2c_3$, $D=\sqrt2c_2$, the remainders are $u=(A+B)+(C-D)z$ and $v=(A-B)+(C+D)z$. This is $2$ real-constant products and $6$ complex additions.

4. *Evaluate the linear and quadratic remainders.*
   - $y_0=s_0+s_1$ and $y_4=s_0-s_1$: $2$ complex additions.
   - $y_2=t_0-it_1$ ($\omega^2=-i$) and $y_6=t_0+it_1$: $2$ complex additions; multiplying by $\pm i$ is free.
   - $\omega^{3},\omega^{5}=\frac{-1\mp i}{\sqrt2}$ are the roots of $z^2+\sqrt2z+1$. With $w=u_1/\sqrt2$ and $p=u_0-w$: $y_3=p-iw$, $y_5=p+iw$. This is $1$ real-constant product and $3$ complex additions.
   - $\omega^{1},\omega^{7}=\frac{1\mp i}{\sqrt2}$ are the roots of $z^2-\sqrt2z+1$. With $w'=v_1/\sqrt2$ and $q=v_0+w'$: $y_1=q-iw'$, $y_7=q+iw'$. Again $1$ product and $3$ complex additions.

5. *Count.* Complex additions: $8+4+6+2+2+3+3=28$, that is, $56$ real additions. Real-constant products: $2+1+1=4$, that is, $8$ real multiplications. Total: $64$ real operations.

6. *Comparison.* Bruun's algorithm with this straightforward schedule needs $64$ operations against split-radix's $56$, all of the excess being the $8$ multiplications by $\sqrt2$ and $1/\sqrt2$. Its additions already match split-radix's count. Its advantage is that the arithmetic stays real until the last step, not a lower operation count.
:::
