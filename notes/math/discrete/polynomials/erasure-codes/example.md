<!-- Adapted (own wording) from UC Berkeley CS 70, Fall 2020, Note 9 (source key cs70-9, in note.md). -->

::: {#exm-erasure-code-gf7 .example name="Losing two packets" level="medium"}
Send $n=4$ packets $3,1,5,0$ so that any $k=2$ may be lost; work in $\mathrm{GF}(7)$. The interpolating polynomial is $P(x)=x^3+4x^2+5$, and the codeword is $P(1),\dots,P(6)=3,1,5,0,6,1$.

If packets $2$ and $6$ are lost, the receiver has $(1,3)$, $(3,5)$, $(4,0)$, $(5,6)$. Interpolating modulo $7$ recovers $x^3+4x^2+5$, and the lost message packet is $P(2)=1$.
:::

::: {#fig-erasure-codes-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (q0) at (0.0,0) {$3$};
\node[tick] at (0.0,-0.75) {$P(1)$};
\node[box] (q1) at (1.35,0) {$1$};
\node[tick] at (1.35,-0.75) {$P(2)$};
\draw[hl] (q1.south west) -- (q1.north east) (q1.north west) -- (q1.south east);
\node[box] (q2) at (2.7,0) {$5$};
\node[tick] at (2.7,-0.75) {$P(3)$};
\node[box] (q3) at (4.050000000000001,0) {$0$};
\node[tick] at (4.050000000000001,-0.75) {$P(4)$};
\node[box] (q4) at (5.4,0) {$6$};
\node[tick] at (5.4,-0.75) {$P(5)$};
\node[box] (q5) at (6.75,0) {$1$};
\node[tick] at (6.75,-0.75) {$P(6)$};
\draw[hl] (q5.south west) -- (q5.north east) (q5.north west) -- (q5.south east);
\draw[decorate, decoration={brace, amplitude=5pt}] (-0.55,0.55) -- (4.6,0.55) node[lab, midway, above=5pt] {message: $n=4$};
\draw[decorate, decoration={brace, amplitude=5pt}] (4.85,0.55) -- (7.3,0.55) node[lab, midway, above=5pt] {extra: $k=2$};
\end{tikzpicture}
\end{center}
```

The codeword of @exm-erasure-code-gf7 with packets $2$ and $6$ lost. Any $4$ surviving values determine $P$, and with it the lost ones.

:::
