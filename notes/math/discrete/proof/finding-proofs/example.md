<!-- Adapted (own wording) from UC Berkeley CS 70, Fall 2020, Note 2, §3 (source key cs70-2.3). -->

::: {#exm-digit-sum-nine .example name="Proving an equivalence: digit sums and 9" level="medium"}
Claim: for an integer $0<n<1000$, the sum of the digits of $n$ is divisible by $9$ if and only if $n$ is divisible by $9$. To prove $P\iff Q$, prove $P\implies Q$ and $Q\implies P$ separately.

Write $n=100a+10b+c$ with digits $a,b,c$, so that $n=99a+9b+(a+b+c)$.

1. ($\Leftarrow$) If $a+b+c=9k$, then $n=9(11a+b+k)$, so $9\mid n$.

2. ($\Rightarrow$) If $n=9l$, then $a+b+c=n-99a-9b=9(l-11a-b)$, so $9\mid a+b+c$.

Compare the shorter argument with congruences in @sec-math-discrete-number-theory-modular-arithmetic.
:::
