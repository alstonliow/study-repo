---
title: "Encryption, Key Exchange and Signatures"
sources: [mit6046-22, mit6046r-11]
requires: [cs/cryptography/cryptographic-hash-functions, math/discrete/number-theory/rsa, math/discrete/number-theory/diffie-hellman]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 22 and Recitation 11, in our own wording; proofs written out in steps. RSA and Diffie–Hellman are developed in the number-theory notes (@def-rsa, @def-diffie-hellman-scheme); this note places them in the algorithmic picture. -->

## Symmetric encryption and the key problem

::: {#def-symmetric-encryption .definition name="Symmetric encryption"}

In *symmetric* encryption, the sender and receiver share a secret key $k$. The sender computes the ciphertext $c=e_k(m)$, and the receiver recovers $m=d_k(c)$. The functions are public; only $k$ is secret. Examples are block ciphers such as AES, and the one-time pad $c=m\oplus k$.

:::

The difficulty is to agree on $k$ over a public channel. Physically: Alice locks a box with her lock and sends it; Bob adds his own lock and sends it back; Alice removes her lock and sends it again; Bob removes his. No key ever travelled. For this to work, the two locks must *commute*.

::: {#prp-dh-commuting .proposition name="Diffie–Hellman key exchange"}

Let $p$ be a prime and $g$ a generator of $\mathbb Z_p^*$, both public. Alice picks a secret $a$ and sends $g^a\bmod p$; Bob picks a secret $b$ and sends $g^b\bmod p$. Both can then compute $k=g^{ab}\bmod p$: Alice as $(g^b)^a$ and Bob as $(g^a)^b$. An eavesdropper sees $g^a$ and $g^b$, and must solve the Diffie–Hellman problem (@def-diffie-hellman-problem) to find $k$.

:::

::: {.proof}

$(g^b)^a=g^{ab}=(g^a)^b$ in $\mathbb Z_p^*$: exponentiation "locks" commute. Each side needs only fast modular exponentiation, $O(\log a)$ multiplications (@sec-math-discrete-number-theory-modular-exponentiation).

:::

::: {#fig-public-key-cryptography-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (A) at (0,0) {Alice}; \node[box] (B) at (6,0) {Bob};
\draw[faint] (0,-0.4) -- (0,-3.4); \draw[faint] (6,-0.4) -- (6,-3.4);
\node[lab,tick, anchor=east] at (-0.2,-0.9) {secret $a$};
\node[lab,tick, anchor=west] at (6.2,-0.9) {secret $b$};
\draw[->, emph] (0,-1.4) -- node[edge label] {$g^a\bmod p$} (6,-1.4);
\draw[->, emph] (6,-2.2) -- node[edge label] {$g^b\bmod p$} (0,-2.2);
\node[lab,tick, anchor=east] at (-0.2,-3.0) {$k=(g^b)^a$};
\node[lab,tick, anchor=west] at (6.2,-3.0) {$k=(g^a)^b$};
\node[lab,tick] at (3,-3.0) {eavesdropper sees $g^a$, $g^b$ only};
\end{tikzpicture}
\end{center}
```

Diffie–Hellman key exchange. Only $g^a$ and $g^b$ cross the public channel; both sides compute the same key $g^{ab}\bmod p$ because exponentiation commutes.

:::

Key exchange alone is open to a *man-in-the-middle*: Eve can run one exchange with Alice and another with Bob, posing as each to the other. Defeating her requires *authentication*, which signatures provide.

## Public-key encryption

::: {#def-public-key-encryption .definition name="Public-key encryption"}

In *public-key* (asymmetric) encryption, each receiver has a *public key* $PK$, which anyone may use to encrypt, and a *secret key* $SK$, needed to decrypt: $m=d_{SK}(e_{PK}(m))$. It must be infeasible to compute $SK$ from $PK$, or $m$ from $e_{PK}(m)$.

:::

RSA (@def-rsa) is the standard example: $PK=(N,e)$ with $N=pq$, and $SK=d$ with $ed\equiv1\pmod{(p-1)(q-1)}$; encryption is $c=m^e\bmod N$ and decryption $m=c^d\bmod N$ (@thm-rsa-correct). Its security rests on the belief that factoring $N$ (or taking $e$-th roots modulo $N$) is hard. Factoring is in NP, but it is not believed to be NP-complete, and quantum computers could factor efficiently.

::: {#rmk-public-key-cryptography-np .remark name="NP-completeness is not enough"}

Basing cryptography on an NP-complete problem is tempting, since then breaking it would prove P = NP. The *knapsack* cryptosystem (Merkle–Hellman, 1978) tried this with subset sum: the public key is a disguised version of a "superincreasing" sequence $b_1<b_2<\dots$ (each larger than the sum of the earlier ones), for which subset sum is solved greedily from the largest term. It was broken in 1982. NP-hardness is about the *worst* case, while a cryptosystem needs instances that are hard *on average*, and the disguised instances turned out to be special and easy.

:::

## Digital signatures

::: {#def-digital-signature .definition name="Digital signature"}

A *digital signature* scheme lets Alice, holding a secret key $SK$, compute a signature $\sigma=\mathrm{sign}_{SK}(M)$ on a message $M$, which anyone can check with her public key: $\mathrm{verify}_{PK}(M,\sigma)$ is true. It must be infeasible to produce a valid signature on any new message without $SK$, even after seeing signatures on messages of one's choice.

:::

With RSA one can sign by "decrypting": $\sigma=h(M)^d\bmod N$, and verify by checking $\sigma^e\equiv h(M)\pmod N$. Hashing first is essential: signing $M$ itself would let an attacker multiply signatures ($\sigma_1\sigma_2$ is a valid signature on $M_1M_2$) and would restrict messages to numbers below $N$. Signed public keys (*certificates*) are what defeat the man-in-the-middle in practice.
