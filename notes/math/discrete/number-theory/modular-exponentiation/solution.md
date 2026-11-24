<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-number-theory-16"}
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

::: {.solution for="prob-mit6042f10-3-q1" status="draft"}
(a) Euclid's algorithm: $135=2\cdot59+17$, $59=3\cdot17+8$, $17=2\cdot8+1$, so $\gcd=1$. Back-substituting,
$$1=17-2\cdot8=17-2(59-3\cdot17)=7\cdot17-2\cdot59=7(135-2\cdot59)-2\cdot59=7\cdot135-16\cdot59,$$
so $s=7$, $t=-16$.

(b) Modulo $135$, $-16\cdot59\equiv1$, so $59^{-1}\equiv-16\equiv119$. Check: $59\cdot119=7021=52\cdot135+1$.

(c) $31$ is prime, so $\varphi(31)=30$ and $17^{30}\equiv1$; hence $17^{-1}\equiv17^{29}\pmod{31}$. By repeated squaring, $17^2\equiv10$, $17^4\equiv7$, $17^8\equiv18$, $17^{16}\equiv14$, and $17^{29}=17^{16}17^817^417\equiv14\cdot18\cdot7\cdot17\equiv11$. Check: $17\cdot11=187=6\cdot31+1$.

(d) $83$ is prime and does not divide $3$, so $3^{82}\equiv1\pmod{83}$. Since $482248=82\cdot5881+6$, $3^{482248}\equiv3^6=729\equiv729-8\cdot83=65$. The remainder is $65$.
:::

::: {.solution for="prob-mit6042f10-3-q3" status="draft"}
Here $p$ is an odd prime and, in (b) and (c), $p\nmid n$ (the criterion is about such $n$).

(a) $x^2\equiv y^2$ means $p\mid x^2-y^2=(x+y)(x-y)$. Since $p$ is prime, this holds if and only if $p\mid x+y$ or $p\mid x-y$ (Euclid's lemma), i.e. $x\equiv-y$ or $x\equiv y\pmod p$.

(b) Let $n\equiv x^2$. Since $p\nmid n$, also $p\nmid x$, so by Fermat's little theorem $n^{\frac{p-1}2}\equiv x^{p-1}\equiv1\pmod p$.

(c) Take $x=n^{k+1}$. Then $x^2=n^{2k+2}=n^{\frac{p+1}2}=n^{\frac{p-1}2}\cdot n\equiv n\pmod p$, by (b). The other square root is $-n^{k+1}$, by (a).
:::
