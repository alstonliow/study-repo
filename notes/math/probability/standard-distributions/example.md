<!-- Adapted (own wording) from UC Berkeley CS 70, Fall 2020, Note 13, §3.1 "Coin Tosses" (source key cs70-13.3.1, in note.md). -->

::: {#exm-biased-coin-tosses .example name="Biased coin tosses" level="easy"}
A coin shows Heads with probability $p$ and Tails with probability $1-p$, and
it is tossed $4$ times. The tosses are independent
(@def-mutual-independence-events).

**Outcomes are not equally likely.** The sample space has the $2^4=16$
sequences of H and T. When $p=\frac12$ each has probability $\frac1{16}$, but
for $p=\frac23$ they differ. A sequence with $k$ Heads has probability
$p^k(1-p)^{4-k}$, so
$$
\Pr(\mathrm{HHHH}) = \left(\tfrac23\right)^4 = \tfrac{16}{81},
\qquad
\Pr(\mathrm{TTHH}) = \left(\tfrac13\right)^2\left(\tfrac23\right)^2 = \tfrac{4}{81}.
$$

**All four tosses the same.** This event is $\{\mathrm{HHHH},\mathrm{TTTT}\}$,
so its probability is
$$
\tfrac{16}{81}+\tfrac{1}{81} = \tfrac{17}{81}.
$$

**Exactly two Heads.** Each such sequence has probability
$\left(\frac23\right)^2\left(\frac13\right)^2=\frac{4}{81}$. A sequence is fixed
by choosing which $2$ of the $4$ tosses are Heads, which can be done in
$\binom42=6$ ways. So the probability is $6\cdot\frac{4}{81}=\frac{8}{27}$.

**In general.** For $n$ tosses, each sequence with exactly $r$ Heads has
probability $p^r(1-p)^{n-r}$, and there are $\binom nr$ of them. So
$$
\Pr(\text{exactly } r \text{ Heads}) = \binom nr p^r(1-p)^{n-r},
$$
which is the binomial distribution $\mathrm{Bin}(n,p)$ (@def-binomial-distribution).
:::
