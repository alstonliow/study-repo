<!-- Adapted (own wording) from UC Berkeley CS 70, Fall 2020, Note 9 (source key cs70-9, in note.md). -->

::: {#exm-berlekamp-welch-gf7 .example name="Decoding one error" level="hard"}
Work in $\mathrm{GF}(7)$ and send the $n=3$ characters $3,0,6$, guarding against $k=1$ error. The polynomial is $P(x)=x^2+x+1$ and the codeword is $P(1),\dots,P(5)=3,0,6,0,3$. Suppose the first character arrives as $2$, so $r=(2,0,6,0,3)$.

With $Q(x)=a_3x^3+a_2x^2+a_1x+a_0$ and $E(x)=x+b_0$, the conditions $Q(i)=r_iE(i)$ for $i=1,\dots,5$ become, modulo $7$,
$$\begin{aligned}
a_3+a_2+a_1+a_0+5b_0&=2,\\
a_3+4a_2+2a_1+a_0&=0,\\
6a_3+2a_2+3a_1+a_0+b_0&=4,\\
a_3+2a_2+4a_1+a_0&=0,\\
6a_3+4a_2+5a_1+a_0+4b_0&=1.
\end{aligned}$$
Their solution is $a_3=1$, $a_2=a_1=0$, $a_0=6$, $b_0=6$. So $E(x)=x+6=x-1$, which locates the error at position $1$, and $Q(x)=x^3+6=x^3-1$. Dividing, $P(x)=Q(x)/E(x)=x^2+x+1$, and the correct first character is $P(1)=3$.
:::

::: {#fig-reed-solomon-codes-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[hl box] (q0) at (0.0,0) {$2$};
\node[tick] at (0.0,-0.75) {$P(1)$};
\node[box] (q1) at (1.35,0) {$0$};
\node[tick] at (1.35,-0.75) {$P(2)$};
\node[box] (q2) at (2.7,0) {$6$};
\node[tick] at (2.7,-0.75) {$P(3)$};
\node[box] (q3) at (4.050000000000001,0) {$0$};
\node[tick] at (4.050000000000001,-0.75) {$P(4)$};
\node[box] (q4) at (5.4,0) {$3$};
\node[tick] at (5.4,-0.75) {$P(5)$};
\node[lab, accent, above=4pt] at (q0.north) {sent $3$};
\draw[decorate, decoration={brace, amplitude=5pt, mirror}] (-0.55,-1.1) -- (5.95,-1.1) node[lab, midway, below=5pt] {$n+2k=5$ characters received; at most $k=1$ changed};
\end{tikzpicture}
\end{center}
```

The received string of @exm-berlekamp-welch-gf7: one character was changed, and the receiver does not know which.

:::
