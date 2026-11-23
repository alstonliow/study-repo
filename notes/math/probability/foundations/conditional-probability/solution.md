<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-probability-1-10" status="draft"}
Yes, if "independent" means mutually independent (the definition for $n$
events).

1. Mutual independence of $A,B,C$ gives
   $\Pr(A\cap B\cap C) = \Pr(A)\Pr(B)\Pr(C)$ and $\Pr(B\cap C) = \Pr(B)\Pr(C)$.

2. Hence
   $$\Pr\bigl(A\cap(B\cap C)\bigr) = \Pr(A)\Pr(B)\Pr(C) = \Pr(A)\Pr(B\cap C),$$
   so $A$ and $B\cap C$ are independent. (This argument does not divide by
   $\Pr(B\cap C)$, so it also works when that probability is $0$.)

3. Pairwise independence is not enough. Toss two fair coins, and let
   $A$ = "first is H", $B$ = "second is H", $C$ = "both show the same". Each
   pair of these is independent, but
   $$\Pr(A\cap B\cap C) = \Pr(\mathrm{HH}) = \tfrac14 \ne \tfrac12\cdot\tfrac14 = \Pr(A)\Pr(B\cap C).$$
:::

::: {.solution for="prob-probability-1-11" status="draft"}
(a) The two paths $S\text{–}M\text{–}T$ and $S\text{–}N\text{–}T$ share no
    links, and each survives with probability $p^2$. At least one survives
    with probability
    $$1 - (1-p^2)^2 = 2p^2 - p^4.$$

(b) In Exercise 4.8(b), the circuit with two pairs of switches in series,
    placed in parallel, conducts exactly when $(v\wedge y)\vee(w\wedge z)$ is
    true. The network is the same circuit, with a link surviving playing the
    role of a switch being closed.

    So the reliability is the probability that this Boolean expression is
    true when each variable is independently true with probability $p$. The
    structure of the expression (an OR of two ANDs) matches the calculation
    in (a).

(c) Condition on the link $MN$.

    1. If $MN$ survives (probability $p$), $M$ and $N$ act as one node. $S$
       reaches it with probability $1-(1-p)^2 = 2p-p^2$, and so does $T$.
       So the probability of a path is $(2p-p^2)^2$.

    2. If $MN$ fails (probability $1-p$), we have the network of (a):
       $2p^2-p^4$.

    3. By the law of total probability,
       $$p(2p-p^2)^2 + (1-p)(2p^2-p^4) = 2p^2 + 2p^3 - 5p^4 + 2p^5.$$

(d) This network is the bridge circuit of Exercise 4.8(c), whose Boolean
    expression is
    $$(v\wedge y)\vee(w\wedge z)\vee(v\wedge x\wedge z)\vee(w\wedge x\wedge y),$$
    one term for each path. The reliability in (c) is the probability that
    this expression is true. The extra link adds two paths, so (c) is at
    least (a); indeed (c) minus (a) is $2p^3(1-p)^2\ge 0$.
:::

::: {.solution for="prob-probability-1-13" status="draft"}
Choose a random tile from the standard English Scrabble set of $100$ tiles.
The letters in the first half of the alphabet, A–M, account for
$$9+2+2+4+12+2+3+2+9+1+1+4+2 = 53$$
tiles (A, B, C, D, E, F, G, H, I, J, K, L, M). Of these, the vowels A, E, I
account for $9+12+9 = 30$. So
$$\Pr(\text{vowel}\mid\text{A–M}) = \frac{\Pr(\{\mathrm A,\mathrm E,\mathrm I\})}{\Pr(\{\mathrm A,\dots,\mathrm M\})} = \frac{30}{53}\approx 0.566.$$
:::

::: {.solution for="prob-probability-1-14" status="draft"}
Assume $\Pr(A)>0$ and $\Pr(B)>0$, so that both conditional probabilities are
defined, and also $\Pr(A\cap B)>0$.

1. By definition,
   $$\Pr(A\mid B) = \frac{\Pr(A\cap B)}{\Pr(B)},\qquad \Pr(B\mid A) = \frac{\Pr(A\cap B)}{\Pr(A)}.$$

2. Both have the same nonzero numerator. So they are equal if and only if
   the denominators are equal, that is, $\Pr(A) = \Pr(B)$.

The assumption $\Pr(A\cap B) > 0$ is needed. If $A$ and $B$ are disjoint,
both conditional probabilities are $0$ even when $\Pr(A)\ne\Pr(B)$. For
example, roll a die with $A = \{1\}$ and $B = \{2,3\}$.
:::

::: {.solution for="prob-probability-1-15" status="draft"}
1. By Exercise 11(c) with $p = \frac12$:
   $$2\cdot\tfrac14 + 2\cdot\tfrac18 - 5\cdot\tfrac1{16} + 2\cdot\tfrac1{32} = \tfrac{16+8-10+2}{32} = \tfrac12.$$

2. From $M$ to $N$ there are three link-disjoint routes: the direct link
   $MN$, the path $M\text{–}S\text{–}N$, and the path $M\text{–}T\text{–}N$.
   All three fail with probability
   $(1-p)(1-p^2)^2 = \frac12\cdot\bigl(\frac34\bigr)^2 = \frac9{32}$. So
   $$\Pr(\text{path from }M\text{ to }N) = 1 - \tfrac9{32} = \tfrac{23}{32}\approx 0.72.$$
   This is higher than in part 1, because $M$ and $N$ are joined directly.
:::

::: {.solution for="prob-cs70-14-q1"}
<!-- TODO: solution -->
:::

::: {.solution for="prob-cs70-14-q3"}
<!-- TODO: solution -->
:::

::: {.solution for="prob-cs70-14-q4"}
<!-- TODO: solution -->
:::

::: {.solution for="prob-cs70-14-q5"}
<!-- TODO: solution -->
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-9-q6" status="draft"}
"Switching" means moving to a uniformly random unopened door other than your first pick. Staying wins with the probability that the first pick hides a car.

(a) Staying wins with probability $\frac1n$. Switching wins only if the first pick was a goat (probability $\frac{n-1}n$); then the car is among the $n-2$ remaining closed doors, and you pick it with probability $\frac1{n-2}$. So switching wins with probability $\frac{n-1}{n(n-2)}$, larger than $\frac1n$ by the factor $\frac{n-1}{n-2}$.

(b) Now only one other door stays closed, and it hides the car exactly when your first pick was a goat: switching wins with probability $\frac{n-1}n$, staying with $\frac1n$.

(c) There are $n-1-j$ doors to switch to. By the law of total probability (@thm-law-of-total-probability), conditioning on the first pick,
$$\Pr(\text{win by switching})=\frac kn\cdot\frac{k-1}{n-1-j}+\frac{n-k}n\cdot\frac k{n-1-j}=\frac kn\cdot\frac{n-1}{n-1-j},$$
while staying wins with probability $\frac kn$. The ratio $\frac{n-1}{n-1-j}$ grows with $j$, so $j$ should be as large as allowed, $j=n-k-1$, giving the ratio $\frac{n-1}k$; this is largest for $k=1$. So $k=1$ and $j=n-2$, as in (b), with ratio $n-1$.
:::

::: {.solution for="prob-cs70hw-10-q1" status="draft"}
(b) True. $A$ is the disjoint union of $A\cap B$ and $A\cap\overline B$, so
$$\Pr(A\cap\overline B)=\Pr(A)-\Pr(A)\Pr(B)=\Pr(A)\bigl(1-\Pr(B)\bigr)=\Pr(A)\Pr(\overline B).$$

(a) True. By (b), $A$ and $\overline B$ are independent; applying (b) again to the independent pair $\overline B,A$ shows that $\overline B$ and $\overline A$ are independent.

(c) False in general. $\Pr(A\cap\overline A)=\Pr(\emptyset)=0$, while $\Pr(A)\Pr(\overline A)>0$ when $0<\Pr(A)<1$; for example a fair coin and $A=$ "heads". They are independent only when $\Pr(A)\in\{0,1\}$.

(d) True. $A$ is independent of itself when $\Pr(A)=\Pr(A)^2$, i.e. $\Pr(A)\in\{0,1\}$; for example $A=B=\Omega$.
:::

::: {.solution for="prob-cs70hw-10-q3" status="draft"}
The coin is fair, so each sequence of $m$ flips has probability $2^{-m}$.

(a) The game ends at flip $5$ exactly when flips $3,4,5$ are THH (flip $3$ must be T, or it would have ended at flip $4$) and flips $1,2$ are not HH. That leaves TT, TH, HT: probability $\frac3{32}$.

(b) Of the three equally likely sequences TTTHH, THTHH, HTTHH, two have three heads: $\frac23$.

(c) Count sequences of $6$ flips with no run of three equal flips. Such a sequence is determined by its first flip and by its runs of length $1$ or $2$ summing to $6$; the number of such compositions of $6$ is the Fibonacci number $13$. So there are $2\cdot13=26$ sequences without a run of three, and the game stops within $6$ flips with probability $1-\frac{26}{64}=\frac{38}{64}=\frac{19}{32}$.
:::

::: {.solution for="prob-cs70hw-10-q4" status="draft"}
Toss the coin twice. Output "heads" on HT, "tails" on TH, and on HH or TT discard the pair and start again. With $\Pr(\text{heads})=p$ and independent tosses, $\Pr(\text{HT})=p(1-p)=\Pr(\text{TH})$, so in each round where we stop, the two outputs are equally likely. A round stops with probability $2p(1-p)>0$ (for $0<p<1$), so with probability $1$ we stop after finitely many rounds, after $\frac1{2p(1-p)}$ rounds on average.
:::

::: {.solution for="prob-mit6042f10-10-q1" status="draft"}
(a) Every value is non-negative, and
$$\sum_{w\in S}\Pr_B\{w\}=\sum_{w\in B}\frac{\Pr\{w\}}{\Pr\{B\}}=\frac{\Pr\{B\}}{\Pr\{B\}}=1.$$
So $\Pr_B$ is a probability function on outcomes (@def-probability-general-case), and events get the sum over their outcomes.

(b) $\Pr_B\{A\}=\sum_{w\in A}\Pr_B\{w\}=\sum_{w\in A\cap B}\frac{\Pr\{w\}}{\Pr\{B\}}=\frac{\Pr\{A\cap B\}}{\Pr\{B\}}$, since outcomes outside $B$ contribute $0$. So $\Pr_B\{A\}=\Pr(A\mid B)$ (@def-conditional-probability).
:::

::: {.solution for="prob-mit6042f10-10-q6" status="draft"}
(a) By symmetry the top card is black with probability $\frac{26}{52}=\frac12$.

(b) Given that the first card was red, the remaining $51$ cards contain $26$ black ones in uniformly random order, so the next card is black with probability $\frac{26}{51}>\frac12$.

(c) Given what has been seen, the remaining $r+b$ cards are in uniformly random order, so each of them, in particular the next one, is black with probability $\frac b{r+b}$.

(d) No strategy wins with probability more than $\frac12$.

1. A strategy decides to stop using only the cards seen so far. Given those cards, the remaining cards are in uniformly random order, so the next card and the *last* card of the deck have the same conditional probability $\frac b{r+b}$ of being black.

2. So, conditioning on the moment the strategy stops and on the cards seen (@thm-law-of-total-probability), the probability of winning equals the probability that the last card of the deck is black.

3. The strategy cannot influence the last card, which is black with probability $\frac12$. Every strategy wins with probability exactly $\frac12$.
:::

::: {.solution for="prob-mit6042f10-11-q1" status="draft"}
All $8$ outcomes have probability $\frac18$.

(a) $T=\{(G,G,E),(G,G,Y)\}$ and $O=\{(G,G,E),(G,G,Y),(G,B,E),(B,G,Y)\}$.

(b) $T\subseteq O$, so $\Pr(T\mid O)=\frac{\Pr(T)}{\Pr(O)}=\frac{2/8}{4/8}=\frac12$.

(c) The argument conditions on the wrong event. "A girl opened the door" is the event $O$, not "there is at least one girl" (which has $6$ outcomes, probability $\frac34$). Two-girl households always produce a girl at the door, while mixed households do so only half the time, so $O$ favours two-girl households more than "at least one girl" does.
:::

::: {.solution for="prob-mit6042f10-11-q4" status="draft"}
Let $q=p^2+(1-p)^2$ be the probability that a round is discarded ($HH$ or $TT$).

(a) The game ends with your win in round $j$ exactly when rounds $1,\dots,j-1$ are discarded and round $j$ is $TH$. By independence this has probability $q^{j-1}(1-p)p$, and the same holds for $HT$ with $p(1-p)$. Summing over $j=1,\dots,N$, $\Pr\{W\}=\Pr\{L\}=p(1-p)\frac{1-q^N}{1-q}$.

(b) A tie means all $N$ rounds are discarded: $\Pr\{\text{tie}\}=q^N$. For $\frac12<p<1$, $q=1-2p(1-p)<1$, so $q^N\to0$. (Compare @prob-cs70hw-10-q4.)
:::

::: {.solution for="prob-mit6042f10-11-q5" status="draft"}
(a) $\Pr(A\cap B)=\Pr(\emptyset)=0$, so independence $\Pr(A\cap B)=\Pr(A)\Pr(B)$ forces $\Pr(A)=0$ or $\Pr(B)=0$.

(b) $\Pr(A\cap\overline B)=\Pr(A)-\Pr(A)\Pr(B)=\Pr(A)\Pr(\overline B)$. (This is @prob-cs70hw-10-q1 (b).)

(c) Toss two fair coins. Let $A$ = "both tosses agree", $B$ = "first toss is H", $C$ = "second toss is H". Then $\Pr(A\cap B)=\Pr(HH)=\frac14=\Pr(A)\Pr(B)$, and likewise for $C$. But $B\cup C$ = "at least one H" has probability $\frac34$, and $\Pr(A\cap(B\cup C))=\Pr(HH)=\frac14\ne\frac12\cdot\frac34$.

(d) Assume $\Pr(C)>0$ (if $\Pr(C)=0$, $C$ is independent of every event). By inclusion–exclusion for the conditional probability and the three independences,
$$\Pr(A\cup B\mid C)=\Pr(A\mid C)+\Pr(B\mid C)-\Pr(A\cap B\mid C)=\Pr(A)+\Pr(B)-\Pr(A\cap B)=\Pr(A\cup B),$$
which says that $C$ and $A\cup B$ are independent.
:::

::: {.solution for="prob-mit6042f10-11-q6" status="draft"}
(a) That the three markers occur *mutually* independently, so that the probability of all three is the product.

(b) Pairwise independence does not determine $\Pr(A\cap B\cap C)$; it only gives the upper bound $\Pr(A\cap B\cap C)\le\Pr(B\cap C)=\frac1{3000}\cdot\frac1{5000}=\frac1{15\,000\,000}$. In a world of several billion people, up to several hundred could have all three markers, so the markers alone cannot single out Joe.

(c) Only $\Pr(A\cap B\cap C)\le\min(\Pr(A),\Pr(B),\Pr(C))=\frac1{5000}$, and it may be as small as $0$.

(d) The product rule gives $\Pr(A\cap B\cap C)=\Pr(A)\Pr(B\mid A)\Pr(C\mid A\cap B)$ (@thm-chain-rule). The attorney replaced $\Pr(C\mid A\cap B)$ by $\Pr(C\mid A)$, which assumes that $B$ and $C$ are independent *given* $A$. The researcher only found that $B$ and $C$ are independent unconditionally, which does not imply conditional independence given $A$. So the probability is not determined by the data.
:::

::: {.solution for="prob-eecs126hw-1-q1" status="draft"}
Let $B$ and $A$ be the numbers of heads of Bob and Alice.

1. Bob has more tails than Alice iff $n+1-B>n-A$, iff $B\le A$. So exactly one of "Bob has more heads" ($B\ge A+1$) and "Bob has more tails" happens.
2. Swapping heads and tails on every coin is a bijection of outcomes that preserves probabilities (the coins are fair) and maps the first event onto the second, so they have equal probability.
3. Two complementary events of equal probability each have probability $\tfrac12$.
:::

::: {.solution for="prob-eecs126hw-1-q5" status="draft"}
The answer is $\frac{n-m}{n+m}$ (the ballot theorem).

1. Call a sequence bad if the score is tied at some time after the start. Captain America is always strictly ahead iff the sequence is good.
2. Every sequence starting with a Superman basket is bad: Superman leads first and Captain America leads at the end, so the difference passes through $0$.
3. Bad sequences starting with a Captain America basket are in bijection with sequences starting with a Superman basket: swap the scorers of every basket up to the first tie. This preserves the final score and the first tie.
4. So $\Pr(\text{bad})=2\Pr(\text{Superman scores first})=\frac{2m}{n+m}$, and $\Pr(\text{good})=1-\frac{2m}{n+m}=\frac{n-m}{n+m}$.
:::

::: {.solution for="prob-mit6041f10-2-q2" status="draft"}
There are $25$ equally likely ordered pairs.

(a) $A=\{(5,5)\}$, so $\Pr(A)=1/25$; $\Pr(B)=\Pr(C)=1-(4/5)^2=9/25$.
  i. $A\subseteq B$, so $\Pr(A\cap B)=1/25\ne\Pr(A)\Pr(B)=9/625$: not independent.
  ii. $A\cap C=\emptyset$, so $\Pr(A\cap C)=0\ne\Pr(A)\Pr(C)$: not independent.

(b) i. $E$ has the $8$ pairs $(i,i\pm1)$, so $\Pr(E)=8/25$; $F$ has $\binom52=10$ pairs, $\Pr(F)=10/25$; $E\cap F=\{(1,2),(2,3),(3,4),(4,5)\}$ has probability $4/25$. Since $\frac{8}{25}\cdot\frac{10}{25}=\frac{3.2}{25}\ne\frac4{25}$, they are not independent.
  ii. $D=\{(2,5),(3,4),(4,3),(5,2)\}$. Given $D$: $E\cap D=\{(3,4),(4,3)\}$, $F\cap D=\{(2,5),(3,4)\}$, $E\cap F\cap D=\{(3,4)\}$, so $\Pr(E\mid D)=\Pr(F\mid D)=\frac12$ and $\Pr(E\cap F\mid D)=\frac14=\frac12\cdot\frac12$. They are conditionally independent given $D$.
:::

::: {.solution for="prob-mit6041f10-2-q5" status="draft"}
(a)

1. By distributivity, $A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$, and the intersection of these two is $A\cap B\cap C$.

2. Inclusion-exclusion and independence give
$$\Pr(A\cap(B\cup C))=\Pr(A)\Pr(B)+\Pr(A)\Pr(C)-\Pr(A)\Pr(B)\Pr(C).$$

3. The right side is $\Pr(A)\bigl(\Pr(B)+\Pr(C)-\Pr(B)\Pr(C)\bigr)=\Pr(A)\Pr(B\cup C)$, again by inclusion-exclusion and independence of $B$ and $C$.

(b)

1. If $A_1,\dots,A_n$ are independent, so are $A_1^c,\dots,A_n^c$: for any subfamily, replacing one event by its complement keeps the product rule, since $\Pr(A^c\cap G)=\Pr(G)-\Pr(A\cap G)=(1-\Pr(A))\Pr(G)$ when $G$ is an intersection of the others; repeat one event at a time.

2. By De Morgan, $(A_1\cup\dots\cup A_n)^c=A_1^c\cap\dots\cap A_n^c$, whose probability is $\prod_i(1-\Pr(A_i))$ by step 1.

3. Taking complements gives the formula.
:::

::: {.solution for="prob-mit1805s22-2-q1" status="draft"}
Use the sample space $\{MM,MF,FM,FF\}$ (older first), all outcomes with probability $\frac14$.

(a) The condition "older is female" is $\{FM,FF\}$, of probability $\frac12$; both female is $\{FF\}$. So the answer is $\frac{1/4}{1/2}=\frac12$.

(b) The condition "at least one male" is $\{MM,MF,FM\}$, of probability $\frac34$, and both male is $\{MM\}$. The answer is $\frac{1/4}{3/4}=\frac13$. The two answers differ because the conditions remove different outcomes: in (b) the information does not say *which* kitten is male.
:::
