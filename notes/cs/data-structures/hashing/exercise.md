::: {.problem #prob-mit6006s20-3-q1 origin="external" source="mit6006s20-3-q1"}
**Hash Practice**

(a) Insert integer keys `A = [47, 61, 36, 52, 56, 33, 92]` in order into a hash table of size $7$ using the hash function $h(k)=(10k+4)\bmod7$. Each slot of the hash table stores a linked list of the keys hashing to that slot, with later insertions being appended to the end of the list. Draw a picture of the hash table after all keys have been inserted.

(b) Suppose the hash function were instead $h(k)=((10k+4)\bmod c)\bmod7$ for some positive integer $c$. Find the smallest value of $c$ such that no collisions occur when inserting the keys from `A`.
:::

::: {.problem #prob-mit6006s20-3-q2 origin="external" source="mit6006s20-3-q2"}
**Dorm Hashing**

MIT wants to assign $2n$ new students to $n$ rooms, numbered $0$ to $n-1$, in Pseudorandom Hall. Each MIT student will have an ID: a postive integer less than $u$, with $u\gg2n$. No two students can have the same ID, but new students are allowed to choose their own IDs after the start of term.

MIT wants to find students quickly given their IDs, so will assign students to rooms by hashing their IDs to a room number. So as not to appear biased, MIT will publish a family $\mathcal H$ of hash functions online before the start of term (before new students choose their IDs), and then after students choose IDs, MIT will choose a rooming hash function uniformly at random from $\mathcal H$.

New MIT freshmen Rony Stark and Tiri Williams want to be roommates. For each hash family below, show that either:

- Rony and Tiri can choose IDs $k_1$ and $k_2$ so as to guarantee that they'll be roommates, or
- prove that no such choice is possible and compute the highest probability they could possibly achieve of being roommates.

(a) $\mathcal H=\{h_{ab}(k)=(ak+b)\bmod n\mid a,b\in\{0,\dots,n-1\}\text{ and }a\ne0\}$

(b) $\mathcal H=\left\{h_a(k)=\left(\left\lfloor\frac{kn}u\right\rfloor+a\right)\bmod n\;\middle|\;a\in\{0,\dots,u-1\}\right\}$

(c) $\mathcal H=\{h_{ab}(k)=((ak+b)\bmod p)\bmod n\mid a,b\in\{0,\dots,p-1\}\text{ and }a\ne0\}$ for fixed prime $p>u$ (this is the universal hash family from Lecture 4)
:::

::: {.problem #prob-mit6006s20-3-q5 origin="external" source="mit6006s20-3-q5"}
**Anagram Archaeology**

String $A$ is an anagram of another string $B$ if $A$ is a permutation of the letters in $B$; for example, (`indicatory`, `dictionary`) and (`brush`, `shrub`) are pairs of words that are anagrams of each other. In this problem, all strings will be ASCII strings containing only the lowercase English letters `a` to `z`.

Given two strings $A$ and $B$, the anagram substring count of $B$ in $A$ is the number of contiguous substrings of $A$ that are anagrams of $B$. For example, if `A = 'esleastealaslatet'` and `B = 'tesla'`, then, of the 13 contiguous substrings in $A$ of length $|B|=5$, exactly 3 of them are anagrams of $B$, namely (`'least'`, `'steal'`, `'slate'`), so the anagram substring count of $B$ in $A$ is 3.

(a) Given string $A$ and a positive integer $k$, describe a data structure that can be built in $O(|A|)$ time, which will then support a single operation: given a different string $B$ with $|B|=k$, return the anagram substring count of $B$ in $A$ in $O(k)$ time.

(b) Given string $T$ and an array of $n$ length-$k$ strings $S=(S_0,\dots,S_{n-1})$ satisfying $0<k<|T|$, describe an $O(|T|+nk)$-time algorithm to return an array $A=(a_0,\dots,a_{n-1})$ for which $a_i$ is the anagram substring count of $S_i$ in $T$ for all $i\in\{0,\dots,n-1\}$.

(c) Write a Python function `count_anagram_substrings(T, S)` that implements your algorithm from part (b). Note the built-in Python function `ord(c)` returns the ASCII integer corresponding to ASCII character `c` in $O(1)$ time. You can download a code template containing some test cases from the website.

```python
def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    A = []
    ##################
    # YOUR CODE HERE #
    ##################
    return tuple(A)
```
:::
