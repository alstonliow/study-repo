::: {.problem #prob-cs70hw-13-q1 origin="external" source="cs70hw-13-q1"}
**Random Cuckoo Hashing.** Cuckoo birds are parasitic beasts. They are known for hijacking the nests of other bird species and evicting the eggs already inside. Cuckoo hashing is inspired by this behavior. In cuckoo hashing, when we get a collision, the element that was already there gets evicted and rehashed.

We study a simple (but ineffective, as we'll see) version of cuckoo hashing, where all hashes are random. Let's say we want to hash $n$ pieces of data $d_1, d_2, \ldots, d_n$ into $n$ possible hash buckets labeled $1, \ldots, n$. We hash the $d_1, \ldots, d_n$ in that order. When hashing $d_i$, we assign it a random bucket chosen uniformly from $1, \ldots, n$. If there is no collision, then we place $d_i$ into that bucket. If there is a collision with some other $d_j$, we evict $d_j$ and assign it another random bucket uniformly from $1, \ldots, n$. (It is possible that $d_j$ gets assigned back to the bucket it was just evicted from!) We again perform the eviction step if we get another collision. We keep doing this until there is no more collision, and we then introduce the next piece of data, $d_{i+1}$ to the hash table.

(a) What is the probability that there are no collisions over the entire process of hashing $d_1, \ldots, d_n$ to buckets $1, \ldots, n$? What value does the probability tend towards as $n$ grows very large?

(b) Assume we have already hashed $d_1, \ldots, d_{n-1}$, and they each occupy their own bucket. We now introduce $d_n$ into our hash table. What is the expected number of collisions that we'll see while hashing $d_n$? (Hint: What happens when we hash $d_n$ and get a collision, so we evict some other $d_i$ and have to hash $d_i$? Are we at a situation that we've seen before?)

(c) Generalize the previous part: Assume we have already hashed $d_1, \ldots, d_{k-1}$ successully, where $1 \le k \le n$. Let $C_k$ be the number of collisions that we'll see while hashing $d_k$. What is $E[C_k]$?

(d) Let $C$ be the total number of collisions over the entire process of hashing $d_1, \ldots, d_n$. What is $E[C]$? You may leave your answer as a summation.
:::
