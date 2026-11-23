<!-- Adapted (own wording) from UC Berkeley CS 70, Fall 2020, Note 13, §3.3 and §3.4 (source keys cs70-13.3.3, cs70-13.3.4, in note.md). -->

::: {#exm-card-shuffling .example name="Shuffling a deck" level="easy"}
A perfect shuffle of $52$ cards is modelled by the sample space of all $52!$ orderings of the deck, each with probability $\frac1{52!}$. Real shuffles are slightly biased, but the model is close enough to be useful.
:::

::: {#exm-flush .example name="A flush" level="medium"}
Deal a $5$-card hand from a shuffled deck. The sample space is the set of all hands, $\binom{52}5=2\,598\,960$ of them (@exm-poker-hands), all equally likely.

1. A flush has all five cards in one suit. There are $\binom{13}5$ hands in a given suit and $4$ suits, so $4\binom{13}5$ flushes.

2. Hence
   $$\Pr(\text{flush})=\frac{4\binom{13}5}{\binom{52}5}=4\cdot\frac{13\cdot12\cdot11\cdot10\cdot9}{52\cdot51\cdot50\cdot49\cdot48}\approx0.002.$$
:::

<!-- Added 2026-11-17 from MIT 6.042J, Mathematics for Computer Science (2015), Section 16.3 (mcs-16.3); the dice are our own, checked by enumeration. -->

::: {#exm-nontransitive-dice .example name="Non-transitive dice" level="medium"}
Three fair dice have faces $A=\{2,2,4,4,9,9\}$, $B=\{1,1,6,6,8,8\}$ and $C=\{3,3,5,5,7,7\}$. Roll two of them; the higher number wins. Each pair of faces has probability $\frac1{36}$.

1. *$A$ against $B$.* $A$ shows $2$: beats $B$'s $1$s ($2$ faces). $A$ shows $4$: beats the $1$s. $A$ shows $9$: beats all $6$ faces. So $A$ wins in $2\cdot2+2\cdot2+2\cdot6=20$ of the $36$ pairs: probability $\frac59$.

2. *$B$ against $C$.* $B$'s $6$s beat $3,5$ ($4$ faces each), its $8$s beat all $6$: $2\cdot4+2\cdot6=20$ pairs, probability $\frac59$.

3. *$C$ against $A$.* $C$'s $3$s beat the $2$s, its $5$s and $7$s beat the $2$s and $4$s: $2\cdot2+2\cdot4+2\cdot4=20$ pairs, probability $\frac59$.

So $A$ beats $B$, $B$ beats $C$ and $C$ beats $A$, each with probability $\frac59$: "beats with probability more than $\frac12$" is not a transitive relation. Whoever picks a die second can always pick one that wins more often than not.
:::
