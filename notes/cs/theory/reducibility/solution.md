<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-5-q22" status="draft"}
1. *($\Rightarrow$)* Let $M$ recognize $A$. The function $f(w)=\langle M,w\rangle$ is computable, and $w\in A$ iff $M$ accepts $w$ iff $\langle M,w\rangle\in A_{\mathsf{TM}}$. So $A\le_{\mathrm m}A_{\mathsf{TM}}$.

2. *($\Leftarrow$)* Let $f$ reduce $A$ to $A_{\mathsf{TM}}$, and let $U$ recognize $A_{\mathsf{TM}}$ (the universal TM). On input $w$, compute $f(w)$ and run $U$ on it. This accepts exactly when $f(w)\in A_{\mathsf{TM}}$, that is, when $w\in A$, so $A$ is Turing-recognizable.
:::

::: {.solution for="prob-sipser3e-5-q23" status="draft"}
1. *($\Rightarrow$)* Let $M$ decide $A$. Define $f(w)=01$ if $M$ accepts $w$ and $f(w)=10$ otherwise. Since $M$ always halts, $f$ is computable. As $01\in0^*1^*$ and $10\notin0^*1^*$, $w\in A$ iff $f(w)\in0^*1^*$.

2. *($\Leftarrow$)* $0^*1^*$ is regular, hence decidable. If $A\le_{\mathrm m}0^*1^*$ by $f$, then on input $w$ we compute $f(w)$ and run the decider for $0^*1^*$; this decides $A$.
:::

::: {.solution for="prob-sipser3e-5-q25" status="draft"}
1. *The example.* Let $B=\{0w\mid w\in A_{\mathsf{TM}}\}\cup\{1w\mid w\notin A_{\mathsf{TM}}\}$.

2. *Undecidable.* $w\mapsto0w$ reduces $A_{\mathsf{TM}}$ to $B$, and $A_{\mathsf{TM}}$ is undecidable.

3. *$B\le_{\mathrm m}\overline B$.* Let $f(0w)=1w$, $f(1w)=0w$ and $f(\varepsilon)=1$; $f$ is computable.
   - $0w\in B$ iff $w\in A_{\mathsf{TM}}$ iff $1w\notin B$ iff $f(0w)\in\overline B$.
   - $1w\in B$ iff $w\notin A_{\mathsf{TM}}$ iff $0w\notin B$ iff $f(1w)\in\overline B$.
   - $\varepsilon\notin B$, and $f(\varepsilon)=1\in B$ because $\varepsilon$ is not an encoding and so $\varepsilon\notin A_{\mathsf{TM}}$; so $f(\varepsilon)\notin\overline B$.

4. *Remark (the problem set's follow-up question).* Such a $B$ is never Turing-recognizable. The same $f$ also gives $\overline B\le_{\mathrm m}B$. So if $B$ were recognizable, $\overline B$ would be too, and $B$ would be decidable.
:::
