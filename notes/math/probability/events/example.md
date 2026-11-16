<!-- Adapted (own wording) from UC Berkeley CS 70, Fall 2020, Note 13, §3.5 "Balls and Bins" (source key cs70-13.3.5, in note.md). -->

::: {#exm-balls-and-bins .example name="Balls and bins" level="medium"}
Throw $20$ labelled balls into $10$ labelled bins. Each ball lands in each bin
with the same chance, whatever the other balls do. What is the probability
that bin $1$ ends up empty, and that it gets at least one ball?

**Sample space.** An outcome records the bin of each ball in order, so it is a
length-$20$ sequence over the $10$ bins. By @prp-ordered-with-replacement there
are
$$
|\Omega| = 10^{20}
$$
outcomes, all equally likely.

**Bin 1 empty.** Let $A$ be the event that bin $1$ is empty. Then every ball
lands in one of the other $9$ bins, so $|A| = 9^{20}$ and
$$
\Pr(A) = \frac{9^{20}}{10^{20}} = \left(\frac{9}{10}\right)^{20} \approx 0.12 .
$$

**Bin 1 not empty.** The event "bin $1$ gets at least one ball" is
$\overline{A}$, so by @prp-complement its probability is
$1-\Pr(A)\approx 0.88$.

**In general.** With $m$ balls and $n$ bins,
$$
\Pr(\text{bin } 1 \text{ is empty}) = \left(1-\frac{1}{n}\right)^{m}.
$$
The model fits many situations. Tossing a fair coin $3$ times is $m=3$ balls
in $n=2$ bins, and rolling two dice is $m=2$ balls in $n=6$ bins. In computing
it models load balancing, where each job goes to a processor chosen at
random.
:::
