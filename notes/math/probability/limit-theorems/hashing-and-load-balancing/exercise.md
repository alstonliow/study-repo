::: {.problem #prob-cs70hw-13-q1 origin="external" source="cs70hw-13-q1"}
**Random Cuckoo Hashing.** Cuckoo birds are parasitic beasts. They are known for hijacking the nests of other bird species and evicting the eggs already inside. Cuckoo hashing is inspired by this behavior. In cuckoo hashing, when we get a collision, the element that was already there gets evicted and rehashed.

We study a simple (but ineffective, as we'll see) version of cuckoo hashing, where all hashes are random. Let's say we want to hash $n$ pieces of data $d_1, d_2, \ldots, d_n$ into $n$ possible hash buckets labeled $1, \ldots, n$. We hash the $d_1, \ldots, d_n$ in that order. When hashing $d_i$, we assign it a random bucket chosen uniformly from $1, \ldots, n$. If there is no collision, then we place $d_i$ into that bucket. If there is a collision with some other $d_j$, we evict $d_j$ and assign it another random bucket uniformly from $1, \ldots, n$. (It is possible that $d_j$ gets assigned back to the bucket it was just evicted from!) We again perform the eviction step if we get another collision. We keep doing this until there is no more collision, and we then introduce the next piece of data, $d_{i+1}$ to the hash table.

(a) What is the probability that there are no collisions over the entire process of hashing $d_1, \ldots, d_n$ to buckets $1, \ldots, n$? What value does the probability tend towards as $n$ grows very large?

(b) Assume we have already hashed $d_1, \ldots, d_{n-1}$, and they each occupy their own bucket. We now introduce $d_n$ into our hash table. What is the expected number of collisions that we'll see while hashing $d_n$? (Hint: What happens when we hash $d_n$ and get a collision, so we evict some other $d_i$ and have to hash $d_i$? Are we at a situation that we've seen before?)

(c) Generalize the previous part: Assume we have already hashed $d_1, \ldots, d_{k-1}$ successully, where $1 \le k \le n$. Let $C_k$ be the number of collisions that we'll see while hashing $d_k$. What is $E[C_k]$?

(d) Let $C$ be the total number of collisions over the entire process of hashing $d_1, \ldots, d_n$. What is $E[C]$? You may leave your answer as a summation.
:::

::: {.problem #prob-mit6042f10-11-q3 origin="external" source="mit6042f10-11-q3"}
In lecture we discussed the Birthday Paradox. Namely, we found that in a group of $m$ people with $N$ possible birthdays, if $m \ll N$, then:
$$\Pr\{\text{all } m \text{ birthdays are different}\} \sim e^{-\frac{m(m-1)}{2N}}$$
To find the number of people, $m$, necessary for a half chance of a match, we set the probability to 1/2 to get:
$$m \sim \sqrt{(2\ln 2)N} \approx 1.18\sqrt{N}$$
For $N = 365$ days we found $m$ to be 23.

We could also run a different experiment. As we put on the board the birthdays of the poeple surveyed, we could ask the class if anyone has the same birthday. In this case, before we reached a match amongst the surveyed people, we would already have found other people in the rest of the class who have the same birthday as someone already surveyed. Let's investigate why this is.

(a) Consider a group of $m$ people with $N$ possible birthdays amongst a larger class of $k$ people, such that $m \le k$. Define $\Pr\{A\}$ to be the probability that $m$ people all have different birthdays and none of the other $k - m$ people have the same birthday as one of the $m$.

Show that, if $m \ll N$, then $\Pr\{A\} \sim e^{\frac{m(m-2k)}{2N}}$. (Notice that the probability of no match is $e^{-\frac{m^2}{2N}}$ when $k$ is $m$, and it gets smaller as $k$ gets larger.)

Hints: For $m \ll N$: $\frac{N!}{(N-m)!N^m} \sim e^{-\frac{m^2}{2N}}$, and $\left(1 - \frac{m}{N}\right) \sim e^{-\frac{m}{N}}$.

(b) Find the approximate number of people in the group, $m$, necessary for a half chance of a match (your answer will be in the form of a quadratic). Then simplify your answer to show that, as $k$ gets large (such that $N \ll k$), then $m \sim \frac{N\ln 2}{k}$.

Hint: For $x \ll 1$: $\sqrt{1 - x} \sim \left(1 - \frac{x}{2}\right)$.

*Note (these notes):* The approximation $(1-\frac mN)^{k-m}\sim e^{-\frac{m(k-m)}N}$ in (a) also needs $m\ll N$; part (b) uses $N\ll k^2$.
:::

::: {.problem #prob-mit6042f10-12-q6 origin="external" source="mit6042f10-12-q6"}
Suppose $n$ balls are thrown randomly into $n$ boxes, so each ball lands in each box with uniform probability. Also, suppose the outcome of each throw is independent of all the other throws.

(a) Let $X_i$ be an indicator random variable whose value is 1 if box $i$ is empty and 0 otherwise. Write a simple closed form expression for the probability distribution of $X_i$. Are $X_1, X_2, \ldots, X_n$ independent random variables?

(b) Find a constant, $c$, such that the expected number of empty boxes is asymptotically equal ($\sim$) to $cn$.

(c) Show that
$$\Pr(\text{at least } k \text{ balls fall in the first box}) \le \binom{n}{k}\left(\frac{1}{n}\right)^k.$$

(d) Let $R$ be the maximum of the numbers of balls that land in each of the boxes. Conclude from the previous parts that
$$\Pr\{R \ge k\} \le \frac{n}{k!}.$$

(e) Conclude that
$$\lim_{n \to \infty} \Pr\{R \ge n^\epsilon\} = 0$$
for all $\epsilon > 0$.
:::
