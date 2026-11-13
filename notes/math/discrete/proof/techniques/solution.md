<!-- Migrated from 1058note exercises/chapters (owner's solutions). -->

::: {.solution for="prob-proofs-01"}
::: {.proof name="Proof (by cases)"}

Let $\operatorname{Collatz}(x) = C(x)$.

**Case 1: $x$ is odd, $x=2n+1$.**
$$\begin{aligned}
        C(x) &= 3(2n+1)+1 = 6n+4 = 2(3n+2) \quad \text{(even)} \\
        C^{(2)}(x) &= 3n+2 = 3\left(\frac{x-1}{2}\right)+2
            = \frac{3x-3}{2}+2 = \frac{3}{2}x+\frac12
    \end{aligned}$$
$$\implies C^{(2)}(x) < \frac32 x+1. \tag{1}$$

**Case 2: $x$ is even, $x=2m$.** Then $C(x)=m$.

**Case 2a: $m$ is odd.**
$$C^{(2)}(x) = 3m+1 = \frac32 x+1. \tag{2}$$

**Case 2b: $m$ is even.**
$$C^{(2)}(x) = \frac{m}{2} = \frac{x}{4}
            < \frac32 x < \frac32 x+1. \tag{3}$$

By (1), (2), (3), in all cases,
$$C^{(2)}(x) \le \frac32 x+1.$$

:::
:::
