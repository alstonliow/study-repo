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
