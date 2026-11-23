<!-- Sipser problems assigned in MIT 18.404J (Fall 2020) problem sets, which cite them by number only.
     Statements verbatim from the 3rd edition (owner decision 2026-11-23, meta/SPEC.md §10). -->

<!-- Sipser 5.26; 18.404J PS3 Q3 -->
::: {.problem #prob-sipser3e-5-q26 origin="external" source="sipser3e-5-q26"}
Define a *two-headed finite automaton* (2DFA) to be a deterministic finite automaton that has two read-only, bidirectional heads that start at the left-hand end of the input tape and can be independently controlled to move in either direction. The tape of a 2DFA is finite and is just large enough to contain the input plus two additional blank tape cells, one on the left-hand end and one on the right-hand end, that serve as delimiters. A 2DFA accepts its input by entering a special accept state. For example, a 2DFA can recognize the language $\{\mathtt a^n\mathtt b^n\mathtt c^n\mid n\ge0\}$.

a. Let $A_{\mathsf{2DFA}}=\{\langle M,x\rangle\mid M \text{ is a 2DFA and } M \text{ accepts } x\}$. Show that $A_{\mathsf{2DFA}}$ is decidable.

b. Let $E_{\mathsf{2DFA}}=\{\langle M\rangle\mid M \text{ is a 2DFA and } L(M)=\emptyset\}$. Show that $E_{\mathsf{2DFA}}$ is not decidable.
:::

<!-- Sipser 5.21; 18.404J PS3 Q4 -->
::: {.problem #prob-sipser3e-5-q21 origin="external" source="sipser3e-5-q21"}
Let $\mathit{AMBIG}_{\mathsf{CFG}}=\{\langle G\rangle\mid G \text{ is an ambiguous CFG}\}$. Show that $\mathit{AMBIG}_{\mathsf{CFG}}$ is undecidable. (Hint: Use a reduction from PCP. Given an instance
$$P=\left\{\left[\frac{t_1}{b_1}\right],\left[\frac{t_2}{b_2}\right],\dots,\left[\frac{t_k}{b_k}\right]\right\}$$
of the Post Correspondence Problem, construct a CFG $G$ with the rules
$$\begin{aligned}
S&\to T\mid B\\
T&\to t_1T\mathtt a_1\mid\cdots\mid t_kT\mathtt a_k\mid t_1\mathtt a_1\mid\cdots\mid t_k\mathtt a_k\\
B&\to b_1B\mathtt a_1\mid\cdots\mid b_kB\mathtt a_k\mid b_1\mathtt a_1\mid\cdots\mid b_k\mathtt a_k,
\end{aligned}$$
where $\mathtt a_1,\dots,\mathtt a_k$ are new terminal symbols. Prove that this reduction works.)
:::
