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

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-4-q5" status="draft"}
1. *For every prime $p$ and every integer $n$, $n^p\equiv n\pmod p$.* If $p\mid n$, both sides are $0$. Otherwise $n\bmod p\in\{1,\dots,p-1\}$, so $n^{p-1}\equiv1$; multiply by $n$.

2. *Modulo $7$:* $n^7\equiv n$ by step 1.

3. *Modulo $3$:* $n^3\equiv n$, so $n^7=n^3\cdot n^3\cdot n\equiv n\cdot n\cdot n=n^3\equiv n$.

4. *Modulo $2$:* $n^2\equiv n$, so $n^7\equiv n$ (apply $n^2\equiv n$ repeatedly).

5. So $2$, $3$ and $7$ divide $n^7-n$. They are pairwise coprime, so their product $42$ divides it (@prp-coprimedivides).
:::
