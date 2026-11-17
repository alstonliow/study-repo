::: {.problem #prob-cs70hw-6-q2 origin="external" source="cs70hw-6-q2"}
**Message is too noisy.** In this problem, we are going to discuss the decoding procedure even when the codeword is corrupted more than they could be. For all parts, work in mod 17.

(a) Encode the message $(0, 1, 4)$ into a polynomial, where $P(0) = 0$, $P(1) = 1$, $P(2) = 4$, what is $P$?

(b) Suppose you send the message $(P(0), P(1), P(2), P(3), P(4))$ to the receiver and last packet is corrupted to 0. Run the decoding process and calulate the $Q$, $E$ as defined in the lecture. You should also confirm that $Q(x)/E(x) = P(x)$.

(c) After corrupting the 4-th packet to 6 and 5-th packet to 8, decode again, by computing $Q$, $E$, $Q(x)/E(x)$, and outputting the first 3 packets. Explain why the decoded message is not the original message, but rather $(1, 1, 4)$.

(d) Define the Hamming distance between two messages to be the number of packets that differ. For example, the distance between $(0, 1, 2, 3, 4)$ and $(0, 1, 1, 4, 4)$ is 2 since they differ at the third and forth position.

Let $RS[5, 3]$ be all Reed-Solomon codewords with codeword length 5, message length 3. Show that the Hamming distance between any two codewords in $RS[5, 3]$ is at least 3. Also show that the codeword $(1, 1, 3, 7, 13)$ (which the decoder finds) has the smallest Hamming distance from the non-codeword $(1, 1, 4, 7, 13)$ compared to all other codeword in $RS[5, 3]$.

(e) We generalize $RS[m, n]$ to be all Reed-Solomon codewords with length $m$, message length $n$. (Note: min Hamming distance between any pair of valid codewords is $m - n + 1$). Let $C_0$ be the corrupted codeword, $\mathit{msg} = \mathrm{Decode}(C_0)$, $E = \mathrm{Encode}(\mathit{msg})$. $\mathrm{Hamming}(x, y)$ is the hamming distance between $x$ and $y$. Show
$$\mathrm{Hamming}(C_0, E) = \min_{E' \in RS[m,n]} \bigl(\mathrm{Hamming}(C_0, E')\bigr)$$
Hint: if there are too many corruptions, clearly it will decode to a wrong message.

*Note (these notes):* In (c) the decoder actually returns $(0,2,4)$, not $(1,1,4)$, and the words in (d) do not come from (c); the solution treats (d) as a separate example. The official solution also gives $(0,2,4)$ in substance ($P(x)=2x$).
:::

::: {.problem #prob-cs70hw-6-q3 origin="external" source="cs70hw-6-q3"}
**Linearity.** Prove that Reed Solomon codes are linear; that is, the element-wise sum of two Reed Solomon codewords is also a Reed Solomon codeword. To do this, use the coefficient encoding rather than interpolation encoding: If you have a message of length $n$ and you want to send $m$ packets, create a degree $n - 1$ polynomial $p(x)$ where your message $(c_0, c_1, \ldots, c_{n-1})$ are the coefficients of $p(x)$, and the codeword is the evaluation of $p(x)$ at $\{0, 1, \ldots, m - 1\}$. (Assume we are working on $\mathrm{GF}(p)$ for large enough $p$.)
:::

::: {.problem #prob-cs70hw-6-q4 origin="external" source="cs70hw-6-q4"}
**Multiplicative.** Recall $RS[m, n]$ to be all Reed-Solomon codewords with length $m$, message length $n$. Given two codewords $a, b \in RS[m, n]$. Let $c = a * b$ be the element-wise product of $a$ and $b$. Show that $c \in RS[m, 2n - 1]$. (Assume we are working over $\mathrm{GF}(p)$, where $p$ is large enough)
:::
