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

::: {#fig-binomial-distribution-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (8.6,0) node[lab, right] {$k$};
\draw[->] (0,0) -- (0,2.0) node[lab, above] {};
\node[dot] at (0.00,0.092) {};
\node[dot] at (0.40,0.461) {};
\node[dot] at (0.80,1.095) {};
\node[dot] at (1.20,1.643) {};
\node[dot] at (1.60,1.746) {};
\node[dot] at (2.00,1.396) {};
\node[dot] at (2.40,0.873) {};
\node[dot] at (2.80,0.436) {};
\node[dot] at (3.20,0.177) {};
\node[dot] at (3.60,0.059) {};
\node[dot] at (4.00,0.016) {};
\node[dot] at (4.40,0.004) {};
\node[dot] at (4.80,0.001) {};
\node[dot] at (5.20,0.000) {};
\node[dot] at (5.60,0.000) {};
\node[dot] at (6.00,0.000) {};
\node[dot] at (6.40,0.000) {};
\node[dot] at (6.80,0.000) {};
\node[dot] at (7.20,0.000) {};
\node[dot] at (7.60,0.000) {};
\node[dot] at (8.00,0.000) {};
\node[tick, above] at (1.60,1.85) {$p=0.2$};
\node[hl dot] at (0.00,0.000) {};
\node[hl dot] at (0.40,0.000) {};
\node[hl dot] at (0.80,0.001) {};
\node[hl dot] at (1.20,0.009) {};
\node[hl dot] at (1.60,0.037) {};
\node[hl dot] at (2.00,0.118) {};
\node[hl dot] at (2.40,0.296) {};
\node[hl dot] at (2.80,0.591) {};
\node[hl dot] at (3.20,0.961) {};
\node[hl dot] at (3.60,1.281) {};
\node[hl dot] at (4.00,1.410) {};
\node[hl dot] at (4.40,1.281) {};
\node[hl dot] at (4.80,0.961) {};
\node[hl dot] at (5.20,0.591) {};
\node[hl dot] at (5.60,0.296) {};
\node[hl dot] at (6.00,0.118) {};
\node[hl dot] at (6.40,0.037) {};
\node[hl dot] at (6.80,0.009) {};
\node[hl dot] at (7.20,0.001) {};
\node[hl dot] at (7.60,0.000) {};
\node[hl dot] at (8.00,0.000) {};
\node[tick, above] at (4.00,1.51) {$p=0.5$};
\node[hollow dot] at (0.00,0.000) {};
\node[hollow dot] at (0.40,0.000) {};
\node[hollow dot] at (0.80,0.000) {};
\node[hollow dot] at (1.20,0.000) {};
\node[hollow dot] at (1.60,0.000) {};
\node[hollow dot] at (2.00,0.000) {};
\node[hollow dot] at (2.40,0.000) {};
\node[hollow dot] at (2.80,0.000) {};
\node[hollow dot] at (3.20,0.001) {};
\node[hollow dot] at (3.60,0.004) {};
\node[hollow dot] at (4.00,0.016) {};
\node[hollow dot] at (4.40,0.059) {};
\node[hollow dot] at (4.80,0.177) {};
\node[hollow dot] at (5.20,0.436) {};
\node[hollow dot] at (5.60,0.873) {};
\node[hollow dot] at (6.00,1.396) {};
\node[hollow dot] at (6.40,1.746) {};
\node[hollow dot] at (6.80,1.643) {};
\node[hollow dot] at (7.20,1.095) {};
\node[hollow dot] at (7.60,0.461) {};
\node[hollow dot] at (8.00,0.092) {};
\node[tick, above] at (6.40,1.85) {$p=0.8$};
\draw (0.0,0) -- (0.0,-0.08) node[tick, below] {$0$};
\draw (2.0,0) -- (2.0,-0.08) node[tick, below] {$5$};
\draw (4.0,0) -- (4.0,-0.08) node[tick, below] {$10$};
\draw (6.0,0) -- (6.0,-0.08) node[tick, below] {$15$};
\draw (8.0,0) -- (8.0,-0.08) node[tick, below] {$20$};
\end{tikzpicture}
\end{center}
```

$\operatorname{Bin}(20,p)$ for $p=0.2,0.5,0.8$: each peaks near $np$, and $p$ and $1-p$ give mirror images

:::
