<!-- Sipser problems assigned in MIT 18.404J (Fall 2020) problem sets, which cite them by number only.
     Statements verbatim from the 3rd edition (owner decision 2026-11-23, meta/SPEC.md §10). -->

<!-- Sipser 2.24; 18.404J PS1 Q6 -->
::: {.problem #prob-sipser3e-2-q24 origin="external" source="sipser3e-2-q24"}
Let $E=\{\mathtt a^i\mathtt b^j\mid i\ne j \text{ and } 2i\ne j\}$. Show that $E$ is a context-free language.
:::

<!-- Sipser 2.27; 18.404J PS1 Q7 -->
::: {.problem #prob-sipser3e-2-q27 origin="external" source="sipser3e-2-q27"}
Let $G=(V,\Sigma,R,\langle\mathrm{STMT}\rangle)$ be the following grammar.
$$\begin{aligned}
\langle\mathrm{STMT}\rangle&\to\langle\mathrm{ASSIGN}\rangle\mid\langle\mathrm{IF\text-THEN}\rangle\mid\langle\mathrm{IF\text-THEN\text-ELSE}\rangle\\
\langle\mathrm{IF\text-THEN}\rangle&\to\mathtt{if\ condition\ then}\ \langle\mathrm{STMT}\rangle\\
\langle\mathrm{IF\text-THEN\text-ELSE}\rangle&\to\mathtt{if\ condition\ then}\ \langle\mathrm{STMT}\rangle\ \mathtt{else}\ \langle\mathrm{STMT}\rangle\\
\langle\mathrm{ASSIGN}\rangle&\to\mathtt{a{:=}1}
\end{aligned}$$
$$\Sigma=\{\mathtt{if},\mathtt{condition},\mathtt{then},\mathtt{else},\mathtt{a{:=}1}\}$$
$$V=\{\langle\mathrm{STMT}\rangle,\langle\mathrm{IF\text-THEN}\rangle,\langle\mathrm{IF\text-THEN\text-ELSE}\rangle,\langle\mathrm{ASSIGN}\rangle\}$$
$G$ is a natural-looking grammar for a fragment of a programming language, but $G$ is ambiguous.

a. Show that $G$ is ambiguous.

b. Give a new unambiguous grammar for the same language.
:::

<!-- Sipser 2.26; 18.404J PS1, read-and-solve problem (not handed in) -->
::: {.problem #prob-sipser3e-2-q26 origin="external" source="sipser3e-2-q26"}
Show that if $G$ is a CFG in Chomsky normal form, then for any string $w\in L(G)$ of length $n\ge1$, exactly $2n-1$ steps are required for any derivation of $w$.
:::
