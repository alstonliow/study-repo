<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-25-q1" status="draft"}
**(a)** The roots of $2s^2+4s+4$ are $-1\pm i$. By @prp-impulse-response-second-order, $w$ is the homogeneous solution with $w(0)=0$, $\dot w(0)=\tfrac12$: $w=\tfrac12u(t)e^{-t}\sin t$.

**(b)** $2\ddot v+4\dot v+4v=1$ has the constant solution $\tfrac14$, so for $t>0$, $v=\tfrac14+e^{-t}(c_1\cos t+c_2\sin t)$ with $v(0)=\dot v(0)=0$: $c_1=-\tfrac14$, and $-c_1+c_2=0$ gives $c_2=-\tfrac14$. So $v=\tfrac14u(t)\bigl(1-e^{-t}(\cos t+\sin t)\bigr)$.

**(c)** For $t>0$, $\dot v=\tfrac14e^{-t}(\cos t+\sin t)-\tfrac14e^{-t}(-\sin t+\cos t)=\tfrac12e^{-t}\sin t=w$; and $v$ is continuous at $0$, so there is no delta term.

**(d)** For $p(D)=a_nD^n+\dots$, the impulse response is the homogeneous solution with $w(0)=\dots=w^{(n-2)}(0)=0$ and $w^{(n-1)}(0)=1/a_n$.

(i) $2u(t)$ is constant for $t>0$ with $w(0^+)=2$: first order with root $0$ and $1/a_1=2$, so $p(D)=\tfrac12D$.

(ii) $t$ has $w(0)=0$, $\dot w(0)=1$ and solves $\ddot w=0$: $p(D)=D^2$.

(iii) $t^2$ has $w(0)=\dot w(0)=0$, $\ddot w(0)=2$ and solves $D^3w=0$: $1/a_3=2$, so $p(D)=\tfrac12D^3$.
:::

::: {.solution for="prob-mit1803ps-26-q1" status="draft"}
**(a)** $w=e^{-kt}$ (for $t>0$). Then
$$x=\int_0^te^{-k(t-\tau)}\cos\omega\tau\,d\tau=\frac{k\cos\omega t+\omega\sin\omega t-ke^{-kt}}{k^2+\omega^2}.$$
Check: $x(0)=0$, and $\dot x+kx=\dfrac{-k\omega\sin\omega t+\omega^2\cos\omega t+k^2e^{-kt}+k^2\cos\omega t+k\omega\sin\omega t-k^2e^{-kt}}{k^2+\omega^2}=\cos\omega t$.

**(b)** $w=\dfrac{\sin\omega_0t}{\omega_0}$, so $x=\displaystyle\int_0^t\frac{\sin\omega_0(t-\tau)}{\omega_0}\,d\tau=\frac{1-\cos\omega_0t}{\omega_0^2}$. Check: $x(0)=\dot x(0)=0$ and $\ddot x+\omega_0^2x=\cos\omega_0t+1-\cos\omega_0t=1$.

**(c)** $t^2*t=\displaystyle\int_0^t\tau^2(t-\tau)\,d\tau=\frac{t^4}3-\frac{t^4}4=\frac{t^4}{12}$, and $t*t^2=\displaystyle\int_0^t\tau(t-\tau)^2\,d\tau=\frac{t^4}{12}$ as well: convolution is commutative.

**(d)** $t*t=\tfrac{t^3}6$, so both are $\dfrac16\,t^3*t=\dfrac16\cdot\dfrac{t^5}{20}=\dfrac{t^5}{120}$: equal, as associativity predicts (also $\mathcal L$ of each is $1/s^6$).
:::
