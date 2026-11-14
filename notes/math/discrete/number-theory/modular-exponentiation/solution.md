<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-number-theory-16" status="draft"}
Let $e$ be the given exponent.

1. Reduce the base: $1752 = 14\cdot 125 + 2$, so $1752\equiv 2\pmod{125}$.

2. $\gcd(2,125) = 1$ and $\varphi(125) = 125 - 25 = 100$, so by Euler's
   theorem $2^{100}\equiv 1\pmod{125}$. Hence only $e\bmod 100$ matters.

3. $e\bmod 100$ is given by the last two digits of $e$, which are $64$. So
   $$1752^e\equiv 2^{64}\pmod{125}.$$

4. Compute $2^{64}$ by repeated squaring mod $125$:
   $$\begin{aligned}
   2^{8} &= 256 \equiv 6,\\
   2^{16} &\equiv 6^2 = 36,\\
   2^{32} &\equiv 36^2 = 1296 \equiv 46,\\
   2^{64} &\equiv 46^2 = 2116 \equiv 116.
   \end{aligned}$$

5. Therefore
   $$1752^{e}\bmod 125 = 116.$$
:::
