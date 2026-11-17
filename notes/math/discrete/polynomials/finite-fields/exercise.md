::: {.problem #prob-cs70hw-5-q4 origin="external" source="cs70hw-5-q4"}
**Polynomials in Fields.** Define the sequence of polynomials by $P_0(x) = x + 12$, $P_1(x) = x^2 - 5x + 5$ and $P_n(x) = xP_{n-2}(x) - P_{n-1}(x)$.

(For instance, $P_2(x) = 17x - 5$ and $P_3(x) = x^3 - 5x^2 - 12x + 5$.)

(a) Show that $P_n(7) \equiv 0 \pmod{19}$ for every $n \in \mathbb{N}$.

(b) Show that, for every prime $q$, if $P_{2017}(x) \not\equiv 0 \pmod q$, then $P_{2017}(x)$ has at most 2017 roots modulo $q$.
:::
