<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-probability-1-08"}
1. By De Morgan's law, $\overline{A\cup B} = \overline A\cap\overline B$.

2. For any event $E$, $\Pr(E) = 1 - \Pr(\overline E)$, because $E$ and
   $\overline E$ are disjoint and their union is the whole sample space.

3. Apply step 2 with $E = A\cup B$, then step 1:
   $$\Pr(A\cup B) = 1 - \Pr(\overline{A\cup B}) = 1 - \Pr(\overline A\cap\overline B).$$
:::

::: {.solution for="prob-probability-1-09"}
Let $P(n)$ be the statement for $n$ sets.

1. *Base case $n=0$.* The union of no sets is $\emptyset$, and
   $\Pr(\emptyset) = 0$, which is the empty sum. (For $n = 1$ both sides
   are $\Pr(A_1)$.)

2. *Inductive step.* Assume $P(n)$, and let $A_1,\dots,A_{n+1}$ be mutually
   disjoint. Put $B = A_1\sqcup\cdots\sqcup A_n$.

3. $B$ and $A_{n+1}$ are disjoint: an element of both would lie in some
   $A_k$ with $k\le n$ and in $A_{n+1}$, which are disjoint.

4. By the additivity axiom for two disjoint events and then $P(n)$:
   $$\Pr(B\sqcup A_{n+1}) = \Pr(B) + \Pr(A_{n+1}) = \sum_{k=1}^n\Pr(A_k) + \Pr(A_{n+1}) = \sum_{k=1}^{n+1}\Pr(A_k).$$

5. This is $P(n+1)$. By induction, $P(n)$ holds for all $n\in\mathbb N$.
:::

::: {.solution for="prob-probability-1-12"}
A fixed-point-free permutation is a *derangement*. Let $D_n$ be the number of
derangements of an $n$-set, so the probability is $D_n/n!$.

- $n = 2$: only the swap, so $D_2 = 1$ and the probability is $\frac12$.
- $n = 3$: the two $3$-cycles, so $D_3 = 2$ and the probability is $\frac26 = \frac13$.
- $n = 5$: by inclusion–exclusion,
  $$D_5 = 5!\Bigl(1 - \frac1{1!} + \frac1{2!} - \frac1{3!} + \frac1{4!} - \frac1{5!}\Bigr) = 120 - 120 + 60 - 20 + 5 - 1 = 44,$$
  so the probability is $\frac{44}{120} = \frac{11}{30}\approx 0.367$.

The probabilities approach $1/e\approx 0.368$ as $n$ grows.
:::

::: {.solution for="prob-cs70-14-q6"}
<!-- TODO: solution -->
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-10-q5" status="draft"}
(a) The arrangement is a uniformly random permutation. Let $A_i$ be "friend $i$ gets their own card". For any $k$ friends, $\Pr(A_{i_1}\cap\dots\cap A_{i_k})=\frac{(n-k)!}{n!}$. By inclusion–exclusion (@thm-general-case),
$$\Pr\Bigl(\bigcup_iA_i\Bigr)=\sum_{k=1}^n(-1)^{k+1}\binom nk\frac{(n-k)!}{n!}=\sum_{k=1}^n\frac{(-1)^{k+1}}{k!},$$
so $\Pr(\text{no one gets their own card})=\sum_{k=0}^n\frac{(-1)^k}{k!}$.

(b) These are the partial sums of $e^x$ at $x=-1$, so the limit is $e^{-1}\approx0.368$.
:::

::: {.solution for="prob-cs70hw-10-q6" status="draft"}
(a) Each ball lands in bin $1$ independently with probability $\frac1n$: $\binom nk\bigl(\frac1n\bigr)^k\bigl(1-\frac1n\bigr)^{n-k}$.

(b) $p=\sum_{k=n/2}^n\binom nk\bigl(\frac1n\bigr)^k\bigl(1-\frac1n\bigr)^{n-k}$.

(c) Each bin has at least half the balls with probability $p$, so by the union bound (@thm-union-bound) the probability is at most $np$.

(d) Both bins can have at least $\frac n2$ balls only if each has exactly $\frac n2$; this happens with probability $\binom n{n/2}\bigl(\frac1n\bigr)^n$ (choose the balls of bin $1$, the rest go to bin $2$). By inclusion–exclusion, the probability is $2p-\binom n{n/2}n^{-n}$.

(e) Let $K$ be the number of the other $n-1$ balls in the first ball's bin; $K\sim\mathrm{Bin}(n-1,\frac1n)$. Given $K=k$, we pick the first ball with probability $\frac1{k+1}$. By the law of total probability,
$$\Pr=\sum_{k=0}^{n-1}\binom{n-1}k\Bigl(\frac1n\Bigr)^k\Bigl(1-\frac1n\Bigr)^{n-1-k}\frac1{k+1}.$$
Using $\frac1{k+1}\binom{n-1}k=\frac1n\binom n{k+1}$, this sum equals $1-\bigl(1-\frac1n\bigr)^n$, which tends to $1-\frac1e$.
:::

::: {.solution for="prob-cs70hw-10-q7" status="draft"}
(a) One coin for each of the $\binom n2$ pairs: $|\Omega|=2^{\binom n2}$.

(b) All $\binom k2$ edges inside $S$ must be present: $\Pr(E_S)=2^{-\binom k2}$.

(c) They are independent if $V_1$ and $V_2$ share at most one vertex: then they share no edge, so the two events depend on disjoint sets of coins. If they share at least two vertices, they share at least one edge, so $|E(V_1)\cup E(V_2)|<\binom\ell2+\binom k2$ and $\Pr(E_{V_1}\cap E_{V_2})=2^{-|E(V_1)\cup E(V_2)|}>2^{-\binom\ell2-\binom k2}=\Pr(E_{V_1})\Pr(E_{V_2})$, so they are not independent.

(d) $\binom nk=\frac{n(n-1)\cdots(n-k+1)}{k!}\le n(n-1)\cdots(n-k+1)\le n^k$.

(e) By the union bound over the $\binom nk$ sets of size $k$, and (d),
$$\Pr(\text{some }k\text{-clique})\le\binom nk2^{-k(k-1)/2}\le\bigl(n\,2^{-(k-1)/2}\bigr)^k.$$
If $k-1\ge4\log_2n$, then $2^{-(k-1)/2}\le n^{-2}$, so the bound is at most $n^{-k}\le\frac1n$ (as $k\ge1$).
:::

::: {.solution for="prob-mit6042f10-10-q2" status="draft"}
(a) Each rule comes from splitting an event into disjoint pieces.

1. *Difference:* $A$ is the disjoint union of $A-B$ and $A\cap B$.
2. *Complement:* $S$ is the disjoint union of $A$ and $\overline A$, and $\Pr\{S\}=1$.
3. *Inclusion–exclusion:* $A\cup B$ is the disjoint union of $A$ and $B-A$, and $\Pr\{B-A\}=\Pr\{B\}-\Pr\{A\cap B\}$ by the difference rule.
4. *Union bound:* by 3, since $\Pr\{A\cap B\}\ge0$.
5. *Monotonicity:* if $A\subseteq B$, then $\Pr\{B\}=\Pr\{A\}+\Pr\{B-A\}\ge\Pr\{A\}$.

(b) Induction on $n$. For $n=1$ there is nothing to prove. If it holds for $n$, then by the 2-event union bound
$$\Pr\Bigl(\bigcup_{i=1}^{n+1}A_i\Bigr)\le\Pr\Bigl(\bigcup_{i=1}^nA_i\Bigr)+\Pr(A_{n+1})\le\sum_{i=1}^{n+1}\Pr(A_i).$$
(@thm-union-bound)
:::

::: {.solution for="prob-eecs126hw-1-q2" status="draft"}
Let $A_i$ be the event that passenger $i$ sits in their own seat.

1. For a set $S$ of $k$ passengers, $\Pr(\bigcap_{i\in S}A_i)=(N-k)!/N!$, and there are $\binom Nk$ such sets, so the $k$-th inclusion–exclusion term is $\binom Nk\frac{(N-k)!}{N!}=\frac1{k!}$.
2. Hence $\Pr(\bigcup_iA_i)=\sum_{k=1}^N(-1)^{k+1}/k!$ and
$$\Pr(\text{no one in their seat})=\sum_{k=0}^{N}\frac{(-1)^k}{k!}\xrightarrow[N\to\infty]{}e^{-1}\approx0.368.$$
:::

::: {.solution for="prob-mit6041f10-1-q1" status="draft"}
Write $E_1=A\cap B^c\cap C^c$, $E_2=A^c\cap B\cap C^c$, $E_3=A^c\cap B^c\cap C$ for "only $A$", "only $B$", "only $C$".

(a) $A\cup B\cup C$.
(b) At most one means none or exactly one: $E_1\cup E_2\cup E_3\cup(A^c\cap B^c\cap C^c)$.
(c) $A^c\cap B^c\cap C^c=(A\cup B\cup C)^c$.
(d) $A\cap B\cap C$.
(e) $E_1\cup E_2\cup E_3$.
(f) $A\cap B\cap C^c$.
(g) $A\cup(A^c\cap B^c)$, which simplifies to $A\cup B^c$.

In the Venn diagrams shade, respectively: everything inside the three circles; the region outside all circles together with the three "only one circle" regions; the region outside all circles; the central triple overlap; the three "only one circle" regions; the part of $A\cap B$ outside $C$; circle $A$ together with everything outside $B$.
:::

::: {.solution for="prob-mit6041f10-1-q6" status="draft"}
1. By De Morgan, $(A\cap B\cap C)^c=A^c\cup B^c\cup C^c$, so $\Pr(A\cap B\cap C)=1-\Pr(A^c\cup B^c\cup C^c)$.

2. By the union bound (@thm-union-bound), $\Pr(A^c\cup B^c\cup C^c)\le\Pr(A^c)+\Pr(B^c)+\Pr(C^c)=3-\Pr(A)-\Pr(B)-\Pr(C)$.

3. Combining, $\Pr(A\cap B\cap C)\ge1-3+\Pr(A)+\Pr(B)+\Pr(C)=\Pr(A)+\Pr(B)+\Pr(C)-2$.
:::

::: {.solution for="prob-mit1805s22-1-q3" status="draft"}
(a) $S=\{1,\dots,365\}^n$ has $365^n$ equally likely outcomes, so $P(E)=|E|/365^n$ for every $E\subseteq S$.

(b) Let $d$ be your birthday. $A=\{(b_1,\dots,b_n): b_i=d\text{ for some }i\}$; $B$ is the set of sequences with $b_i=b_j$ for some $i<j$; $C$ is the set of sequences with $b_i=b_j=b_k$ for some $i<j<k$.

(c) $A^c$ is the set of sequences avoiding $d$, of size $364^n$, so $P(A)=1-(364/365)^n$. This exceeds $\frac12$ when $n>\ln2/\ln(365/364)\approx252.65$, so the smallest $n$ is $253$.

(d) The $n$ birthdays can coincide with each other, so $n$ people cover fewer than $n$ distinct days; to cover half the year in expectation one needs more than $365/2$ people.

(e) Using the exact formula of (f): $P(B)\approx0.891$ for $n=40$ and $\approx0.903$ for $n=41$, so the answer is $n=41$; a simulation with $10000$ trials reproduces this to about $\pm0.006$. With only $30$ trials the estimate has standard deviation about $\sqrt{0.9\cdot0.1/30}\approx0.055$, so runs vary between roughly $0.8$ and $1$.

(f) $B^c$ consists of the sequences of $n$ distinct days, $365\cdot364\cdots(365-n+1)$ of them, so
$$P(B)=1-\frac{365\cdot364\cdots(365-n+1)}{365^n}\quad(n\le365),\qquad P(B)=1\quad(n>365).$$

(g) An exact computation (a recursion on the number of days used once and twice) gives $P(C)\approx0.4995$ for $n=87$ and $\approx0.5111$ for $n=88$, so the answer is $88$; simulations with $10000$ trials cannot reliably separate $87$ from $88$.
:::
