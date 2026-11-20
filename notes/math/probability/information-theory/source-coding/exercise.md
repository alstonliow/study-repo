::: {.problem #prob-eecs126hw-11-q2 origin="external" source="eecs126hw-11-q2"}
**Compression of a Random Source.** Suppose I'm trying to send a text message to my friend. In general, I know I need $\log_2(26)$ bits for every letter I want to send because there are 26 letters in the alphabet. However, it turns out if I have some information on the distribution of the letters, I can do better. For example, I might give the letter e a shorter bit representation because I know it's the most common. Actually, it turns out the number of bits I need on average is the entropy, and in this problem, we try to show why this is true in general.

Let $(X_i)_{i=1}^{\infty}\overset{\text{i.i.d.}}{\sim}p(\cdot)$, where $p$ is a discrete PMF on a finite set $\mathcal X$. We know the entropy of a random variable $X$ is
$$H(X)=-\sum_{x\in\mathcal X}p(x)\log_2p(x)$$
Since entropy is really a function of the distribution, we could write the entropy as $H(p)$.

(a) Show that
$$-\frac1n\log_2p(X_1,\dots,X_n)\xrightarrow[n\to\infty]{}H(X_1)\text{ almost surely.}$$
(Here, we are extending the notation $p(\cdot)$ to denote the joint PMF of $(X_1,\dots,X_n)$: $p(x_1,\dots,x_n):=p(x_1)\cdots p(x_n)$.)

(b) Fix $\epsilon>0$ and define $A_\epsilon^{(n)}$ as the set of all sequences $(x_1,\dots,x_n)\in\mathcal X^n$ such that:
$$2^{-n(H(X_1)+\epsilon)}\le p(x_1,\dots,x_n)\le2^{-n(H(X_1)-\epsilon)}.$$
Show that $P((X_1,\dots,X_n)\in A_\epsilon^{(n)})>1-\epsilon$ for all $n$ sufficiently large. Consequently, $A_\epsilon^{(n)}$ is called the typical set because the observed sequences lie within $A_\epsilon^{(n)}$ with high probability.

(c) Show that $(1-\epsilon)2^{n(H(X_1)-\epsilon)}\le|A_\epsilon^{(n)}|\le2^{n(H(X_1)+\epsilon)}$, for $n$ sufficiently large. Use the union bound.

Parts (b) and (c) are called the asymptotic equipartition property (AEP) because they say that there are $\approx2^{nH(X_1)}$ observed sequences which each have probability $\approx2^{-nH(X_1)}$. Thus, by discarding the sequences outside of $A_\epsilon^{(n)}$, we need only keep track of $2^{nH(X_1)}$ sequences, which means that a length-$n$ sequence can be compressed into $\approx nH(X_1)$ bits, requiring $H(X_1)$ bits per symbol.

(d) Now show that for any $\delta>0$ and any positive integer $n$, if $B_n\subseteq\mathcal X^n$ is a set with $|B_n|\le2^{n(H(X_1)-\delta)}$, then $P((X_1,\dots,X_n)\in B_n)\to0$ as $n\to\infty$.

This says that we cannot compress the observed sequences of length $n$ into any set smaller than size $2^{nH(X_1)}$.

[Hint: Consider the intersection of $B_n$ and $A_\epsilon^{(n)}$.]

(e) Next we turn towards using the AEP for compression. Recall that in order to encode a set of size $n$ in binary, it requires $\lceil\log_2n\rceil$ bits. Therefore, a naïve encoding requires $\lceil\log_2|\mathcal X|\rceil$ bits per symbol.

From (b) and (d), if we use $\log_2|A_\epsilon^{(n)}|\approx nH(X_1)$ bits to encode the sequences in $A_\epsilon^{(n)}$, ignoring all other sequences, then the probability of error with this encoding will tend to $0$ as $n\to\infty$, and thus an asymptotically error-free encoding can be achieved using $H(X_1)$ bits per symbol.

Alternatively, we can create an error-free code by using $1+\lceil\log_2|A_\epsilon^{(n)}|\rceil$ bits to encode the sequences in $A_\epsilon^{(n)}$ and $1+n\lceil\log_2|\mathcal X|\rceil$ bits to encode other sequences, where the first bit is used to indicate whether the sequence belongs in $A_\epsilon^{(n)}$ or not. Let $L_n$ be the length of the encoding of $X_1,\dots,X_n$ using this code; show that $\lim_{n\to\infty}E[L_n]/n\le H(X_1)+\epsilon$. In other words, asymptotically, we can compress the sequence so that the number of bits per symbol is arbitrary close to the entropy.
:::

::: {#prob-guessing-tree-code .problem .coding origin="adapted" source="res-ucb-eecs126-labs-guess-my-word"}
A secret word is drawn from a list in alphabetical order, the $i$-th word with probability proportional to a weight $w_i>0$. We may only ask whether the secret comes after a given word, so every strategy is a binary search tree that keeps the words in order: unlike a Huffman tree (@def-huffman-code), it may not reorder the leaves. A greedy tree imitates Huffman's algorithm while keeping the order. Repeatedly merge the *adjacent* pair of nodes whose total weight is smallest (the leftmost such pair on ties) into one node of their total weight, until one node is left.

Write `guess_counts(freqs)` that builds this tree and returns each word's depth in it, which is the number of questions needed to find that word. The tests check that the depths come from a full binary tree ($\sum_i2^{-d_i}=1$) and that the mean depth is at least the entropy.

```{.python .starter}
def guess_counts(freqs):
    """freqs[i] > 0 is the weight of the i-th word in alphabetical order. Build the
    search tree by repeatedly merging the adjacent pair of nodes with the smallest
    total weight (the leftmost such pair on ties). Return, for each word, its depth
    in the tree: the number of questions needed to identify it."""
    ...
```

```{.python .tests}
import math
import random


def test_uniform_weights():
    assert guess_counts([1, 1, 1, 1]) == [2, 2, 2, 2]


def test_one_heavy_word():
    assert guess_counts([8, 1, 1, 1, 1]) == [1, 3, 3, 3, 3]


def test_leftmost_pair_on_ties():
    # merges: (1,1) -> [2,6,1,1]; (1,1) -> [2,6,2]; tie 8 = 8, take (2,6) -> [8,2]
    assert guess_counts([1, 1, 6, 1, 1]) == [3, 3, 2, 2, 2]


def test_smallest_sum_not_smallest_word():
    # sums 5, 4, 6: merge (3, 1) -> [2, 4, 5]; sums 6, 9: merge (2, 4) -> [6, 5]
    assert guess_counts([2, 3, 1, 5]) == [2, 3, 3, 1]


def test_single_word_needs_no_question():
    assert guess_counts([5]) == [0]


def test_kraft_and_entropy():
    rng = random.Random(7)
    for _ in range(20):
        f = [rng.randint(1, 50) for _ in range(rng.randint(2, 30))]
        d = guess_counts(f)
        assert abs(sum(2.0 ** -x for x in d) - 1) < 1e-12, "a full binary tree"
        total = sum(f)
        H = -sum(x / total * math.log2(x / total) for x in f)
        mean = sum(x * dx for x, dx in zip(f, d)) / total
        assert mean >= H - 1e-12
```
:::
