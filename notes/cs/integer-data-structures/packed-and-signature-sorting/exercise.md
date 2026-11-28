::: {.problem #prob-mit6851ps-8-q1 origin="external" source="mit6851ps-8-q1"}
**Signature compression.** Recall that the first step in Signature Sort was to reduce each $w=\lg^{2+\varepsilon}n$ bit input word to a $O(\lg^{1+\varepsilon}n)$-bit signature. We achieved this by dividing each word into $k=\lg^\varepsilon n$ chunks of $w/k=\lg^2n$ bits each and applying a hash function to each chunk, reducing it to $\lg n$ bits. After hashing, our word was of the form

$$0^{w/k-\lg n}h_1\,0^{w/k-\lg n}h_2\cdots0^{w/k-\lg n}h_k,$$

where each chunk hash $h_i$ is $\lg n$ bits long. Describe how to compress this word so that all of the hashed chunks are adjacent in the least significant bits of the word, so that it has the form needed by the algorithm:

$$0^{w-k\lg n}h_1h_2\cdots h_k.$$

Your algorithm should take $O(1)$ time using the word-RAM operations ($+$, $-$, $*$, $/$, $\%$, $\&$, $|$, $\sim$, $\wedge$, $\ll$, $\gg$). You may assume that $\varepsilon<1$.
:::
