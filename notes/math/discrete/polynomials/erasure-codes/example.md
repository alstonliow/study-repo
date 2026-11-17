<!-- Adapted (own wording) from UC Berkeley CS 70, Fall 2020, Note 9 (source key cs70-9, in note.md). -->

::: {#exm-erasure-code-gf7 .example name="Losing two packets" level="medium"}
Send $n=4$ packets $3,1,5,0$ so that any $k=2$ may be lost; work in $\mathrm{GF}(7)$. The interpolating polynomial is $P(x)=x^3+4x^2+5$, and the codeword is $P(1),\dots,P(6)=3,1,5,0,6,1$.

If packets $2$ and $6$ are lost, the receiver has $(1,3)$, $(3,5)$, $(4,0)$, $(5,6)$. Interpolating modulo $7$ recovers $x^3+4x^2+5$, and the lost message packet is $P(2)=1$.
:::
