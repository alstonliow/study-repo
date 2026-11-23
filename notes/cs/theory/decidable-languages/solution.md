<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-4-q24" status="draft"}
1. *The language.* $\mathit{USELESS}_{\mathsf{PDA}}=\{\langle P\rangle\mid P \text{ is a PDA with at least one useless state}\}$.

2. *One state at a time.* For a state $q$ of $P$, let $P_q$ be $P$ with $q$ as its only accept state. A PDA accepts $w$ when some branch has read all of $w$ and is in an accept state, so $L(P_q)\ne\emptyset$ iff some branch on some input enters $q$. In other words, $q$ is useless iff $L(P_q)=\emptyset$.

3. *Decider.* On input $\langle P\rangle$: for each state $q$, build $P_q$, convert it to an equivalent CFG $G_q$ (the PDA-to-CFG construction is effective), and run the decider for $E_{\mathsf{CFG}}$ on $\langle G_q\rangle$. Accept if some $G_q$ has an empty language; otherwise reject.

4. Each step halts, so this decides $\mathit{USELESS}_{\mathsf{PDA}}$.
:::

::: {.solution for="prob-sipser3e-4-q27" status="draft"}
1. Let $K=\{w\in\{0,1\}^*\mid w \text{ has more 1s than 0s}\}$. $K$ is context free: a PDA pushes a symbol for each unmatched $0$ or $1$, cancels opposite symbols, and accepts when the stack holds at least one $1$ at the end of the input.

2. $\langle M\rangle\in E$ iff $L(M)\cap K\ne\emptyset$.

3. *Decider.* On input $\langle M\rangle$: build a PDA for $L(M)\cap K$ with the product construction (a CFL intersected with a regular language, Problem 2.18), convert it to a CFG $G$, and run the decider for $E_{\mathsf{CFG}}$ on $\langle G\rangle$. Accept iff $L(G)\ne\emptyset$.

4. All constructions are effective and the $E_{\mathsf{CFG}}$ decider halts, so $E$ is decidable.
:::

::: {.solution for="prob-sipser3e-4-q14" status="draft"}
1. *Remove the rules that produce $0$.* Given a CFG $G$ over $\{0,1\}$, let $G'$ be $G$ with every rule deleted whose right-hand side contains the terminal $0$.

2. *Claim: $L(G')=L(G)\cap1^*$.* Every derivation in $G'$ is a derivation in $G$ that produces no $0$, so $L(G')\subseteq L(G)\cap1^*$. Conversely, a derivation in $G$ of a string in $1^*$ never uses a rule that writes a $0$, because terminals are never erased, so it is a derivation in $G'$.

3. *Decider.* On input $\langle G\rangle$, build $G'$, run the decider for $E_{\mathsf{CFG}}$ on $\langle G'\rangle$, and accept iff $L(G')\ne\emptyset$.

4. This always halts and accepts exactly when $1^*\cap L(G)\ne\emptyset$, so the language is decidable.
:::
