<!-- Sipser problems assigned in MIT 18.404J (Fall 2020) problem sets, which cite them by number only.
     Statements verbatim from the 3rd edition (owner decision 2026-11-23, meta/SPEC.md §10). -->

<!-- Sipser 6.11; 18.404J PS3 Q6 -->
::: {.problem #prob-sipser3e-6-q11 origin="external" source="sipser3e-6-q11"}
Let $\phi_{\mathrm{eq}}$ be defined as in Problem 6.10. Give a model of the sentence
$$\begin{aligned}
\phi_{\mathrm{lt}}=\ &\phi_{\mathrm{eq}}\\
&\land\forall x,y\,\big[R_1(x,y)\to\neg R_2(x,y)\big]\\
&\land\forall x,y\,\big[\neg R_1(x,y)\to(R_2(x,y)\oplus R_2(y,x))\big]\\
&\land\forall x,y,z\,\big[(R_2(x,y)\land R_2(y,z))\to R_2(x,z)\big]\\
&\land\forall x\,\exists y\,\big[R_2(x,y)\big].
\end{aligned}$$
:::
