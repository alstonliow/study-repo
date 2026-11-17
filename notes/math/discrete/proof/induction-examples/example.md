<!-- Adapted (own wording) from UC Berkeley CS 70, Fall 2020, Note 3, §1-5 (source keys cs70-3.1 to cs70-3.5). -->

::: {#exm-checking-cases-is-not-proof .example name="Checking cases is not a proof" level="easy"}
$n^2-n+41$ is prime for $n=0,1,\dots,40$, but for $n=41$ it equals $41^2$. However many cases are checked, only a proof covers all $n$; induction does this with a base case and an inductive step.
:::

::: {#exm-two-colourable-maps .example name="Maps cut by straight lines are two-colourable" level="medium"}
A rectangle is cut into regions by $n$ straight lines across it. Claim: the regions can be coloured red and blue so that regions sharing a border have different colours.

1. Base case $n=0$: one region, one colour.

2. Inductive step: given $k+1$ lines, remove the last one and colour the map of $k$ lines by the induction hypothesis. Put the line back and swap red and blue on one side of it.

3. Two regions sharing a border along the new line now differ, because exactly one of them was swapped. Two regions sharing a border along an old line are on the same side of the new line, so they were swapped together or not at all, and still differ.
:::

::: {#exm-strengthen-odd-squares .example name="Strengthening the hypothesis: sums of odd numbers" level="medium"}
To prove "the sum of the first $n$ odd numbers is a perfect square", the hypothesis "the sum of the first $k$ is some square $m^2$" is too weak: why should $m^2+(2k+1)$ be a square? Computing $1,4,9,16$ suggests the stronger claim that the sum is $n^2$. That one goes through: $k^2+(2k+1)=(k+1)^2$. A stronger statement can be easier to prove, because the induction hypothesis gives more.
:::

::: {#exm-strengthen-reciprocal-squares .example name="Strengthening the hypothesis: a bounded sum" level="medium"}
Claim: $\sum_{i=1}^{n}\frac1{i^2}\le2$ for all $n\ge1$. The hypothesis "$\sum_{i=1}^{k}\frac1{i^2}\le2$" does not give the bound for $k+1$, since adding a positive term could push the sum past $2$. Prove instead $\sum_{i=1}^{n}\frac1{i^2}\le2-\frac1n$.

1. Base case $n=1$: $1\le2-1$.

2. Inductive step: $\sum_{i=1}^{k+1}\frac1{i^2}\le2-\frac1k+\frac1{(k+1)^2}$, and this is at most $2-\frac1{k+1}$ because
   $$\frac1k-\frac1{k+1}=\frac1{k(k+1)}\ge\frac1{(k+1)^2}.$$
:::

::: {#exm-postage-four-five .example name="Strong induction with several base cases: postage" level="medium"}
Claim: every $n\ge12$ can be written $n=4x+5y$ with $x,y\in\mathbb N$ (postage with $4$- and $5$-cent stamps).

1. Base cases: $12=4\cdot3$, $13=4\cdot2+5$, $14=4+5\cdot2$, $15=5\cdot3$.

2. Inductive step for $n=k+1\ge16$: $k+1-4\ge12$, so by the strong induction hypothesis $k+1-4=4x'+5y'$, and $k+1=4(x'+1)+5y'$.

Simple induction would only give the case $k$, not $k-3$; the four base cases are needed because the step goes back $4$.
:::

::: {#exm-binary-search-correct .example name="Proving a recursive program correct" level="medium"}
Binary search looks for a word in a dictionary of $n$ pages: if $n=1$, search the page directly; otherwise compare with the first word of the middle page and search the half that could contain the word. Claim: it returns the word's entry if it is there, and "not found" otherwise.

By strong induction on $n$. For $n=1$ the direct search is correct. For $n=k+1$, the comparison picks the only half that can contain the word, and that half has at most $k$ pages, so the recursive call is correct by the strong induction hypothesis. Strong induction is needed because the half has about $\frac n2$ pages, not $n-1$.
:::

::: {#exm-all-horses-same-colour .example name="A false proof: all horses have the same colour" level="medium"}
"By induction on the number $n$ of horses. One horse has one colour. Given $n+1$ horses, the first $n$ have the same colour and so do the last $n$; the horses in both groups link the two, so all $n+1$ have the same colour."

The inductive step fails from $n=1$ to $n=2$: the first horse and the last horse share no common horse, so nothing links them. One false case of $P(n)\implies P(n+1)$ is enough to break the chain.
:::
