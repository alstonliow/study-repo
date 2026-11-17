<!-- Adapted (own wording) from UC Berkeley CS 70, Fall 2020, Note 17, §1-3 (source keys cs70-17.1 to cs70-17.3, in note.md). -->

::: {#exm-markov-vs-chebyshev .example name="Many heads: Markov against Chebyshev" level="medium"}
Toss a fair coin $n$ times and let $X$ be the number of heads, so $E[X]=\frac n2$ and $\mathrm{Var}(X)=\frac n4$. How likely is $X\ge\frac34n$?

1. Markov (@thm-markov-inequality): $\Pr(X\ge\frac34n)\le\dfrac{n/2}{3n/4}=\dfrac23$, whatever $n$ is.

2. Chebyshev (@thm-chebyshev-s-inequality): $X\ge\frac34n$ implies $|X-\frac n2|\ge\frac n4$, so
   $$\Pr\bigl(X\ge\tfrac34n\bigr)\le\frac{n/4}{(n/4)^2}=\frac4n.$$

3. The exact values are about $0.055$ for $n=10$ and $2.8\times10^{-7}$ for $n=100$. Both are bounds, not estimates, but Chebyshev's improves as $n$ grows and Markov's does not.
:::

::: {#exm-polling .example name="How large a poll?" level="easy"}
To estimate the proportion $p$ of voters for a party to within $\varepsilon=0.1$ with confidence $95\%$ ($\delta=0.05$), @thm-coin-bias-sample-size asks for
$$n\ge\frac1{4\cdot0.01\cdot0.05}=500$$
people, chosen independently at random. The answer does not depend on the size of the population.
:::
