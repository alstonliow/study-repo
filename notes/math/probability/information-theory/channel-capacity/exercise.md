::: {.problem #prob-eecs126hw-4-q5 origin="external" source="eecs126hw-4-q5"}
**Soliton Distribution.** This question pertains to the fountain codes introduced in Lab 2.

Say that you wish to send $n$ chunks of a message, $X_1,\dots,X_n$, across a channel, but alas the channel is a packet erasure channel: each of the packets you send is erased with probability $p_e>0$. Instead of sending the $n$ chunks directly through the channel, we will instead send $n$ packets through the channel, call them $Y_1,\dots,Y_n$. How do we choose the packets $Y_1,\dots,Y_n$?

Let $p(\cdot)$ be a probability distribution on $\{1,\dots,n\}$; this represents the degree distribution of the packets.

(i) For $i=1,\dots,n$, pick $D_i$ (a random variable) according to the distribution $p(\cdot)$. Then, choose $D_i$ random chunks among $X_1,\dots,X_n$, and "assign" $Y_i$ to the $D_i$ chosen chunks.

(ii) For $i=1,\dots,n$, let $Y_i$ be the XOR of all of the chunks assigned for $Y_i$ (the number of chunks assigned for $Y_i$ is called the degree of $Y_i$).

(iii) Send each $Y_i$ across the channel, along with metadata which describes which chunks were assigned to $Y_i$.

The receiver on the other side of the channel receives the packets $Y_1,\dots,Y_n$ (for simplicity, assume that no packets are erased by the channel; in this problem, we are just trying to understand what we should do in the ideal situation of no channel noise), and decoding proceeds as follows:

(i) If there is a received packet $Y$ with only one assigned chunk $X_j$, then set $X_j=Y$. Then, "peel off" $X_j$: for all packets $Y_i$ that $X_j$ is assigned to, replace $Y_i$ with $Y_i\operatorname{XOR}X_j$. Remove $Y$ and $X_j$ (notice that this may create new degree-one packets, which allows decoding to continue).

(ii) Repeat the above step until all chunks have been decoded, or there are no remaining degree-one packets (in which case we declare failure).

In the lab, you will play around with the algorithm and watch it in action. Here, our goal is to work out what a good degree distribution $p(\cdot)$ is.

Intuitively, a good degree distribution needs to occasionally have prolific packets that have high degree; this is to ensure that all packets are connected to at least one chunk. However, we need "most" of the packets to have low degree to make decoding easier. Ideally, we would like to choose $p(\cdot)$ such that at each step of the algorithm, there is exactly one degree-one packet.

(a) Suppose that when $k$ chunks have been recovered ($k=0,1,\dots,N-1$), then the expected number of packets of degree $d$ (for $d>1$) is $f_k(d)$. Assuming we are in the ideal situation where there is exactly one degree-one packet for any $k$: What is the probability that a given degree $d$ packet is connected to the chunk we are about to peel off? Based on that, what is the expected number of packets of degree $d$ whose degrees are reduced by one after the $(k+1)$st chunk is peeled off?

(b) We want $f_k(1)=1$ for all $k=0,1,\dots,n-1$. Show that in order for this to hold, then for all $d=2,\dots,n$ we have $f_k(d)=(n-k)/[d(d-1)]$. From this, deduce what $p(d)$ must be, for $d=1,\dots,n$. (This is called the ideal soliton distribution.)

[Hint: You should get two different recursion equations since the only degree 1 node at peeling $k+1$ is going to come from the peeling of degree 2 nodes at peeling $k$, however, for other higher degree $d$ nodes, there will be some probability that some degree $d$ ones will remain from the previous iteration and some probability that they will come from $d+1$ one that will be peeled off]

(c) Find the expectation of the distribution $p(\cdot)$.

In practice, the ideal soliton distribution does not perform very well because it is not enough to design the distribution to work well in expectation.
:::
