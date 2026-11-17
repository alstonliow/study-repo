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
