<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-functions-15" status="draft"}
We use the definitions from Assignment 1, restated here.

- $G\le H$ ($G$ is *embeddable* in $H$): for every key $k$ of $G$ there is a
  key $k'$ of $H$ with $e_G(m,k) = e_H(m,k')$ for every message $m$.
- $G\equiv H$ (*equivalent*): $G\le H$ and $H\le G$.
- $F\circ F$ has keys $(k_1,k_2)\in K\times K$ and encrypts by
  $e(e(m,k_1),k_2)$.
- $F$ is *idempotent* if $F\circ F\equiv F$.

Let $F$ be the Caesar slide.

1. *$F\le F\circ F$.* Given a key $k$, use the pair $(k,\mathtt a)$. Since
   $\mathtt a = 0$, the $i$-th letter of $e(e(m,k),\mathtt a)$ is
   $(m_i + k) + 0 = m_i + k$, which is the $i$-th letter of $e(m,k)$.

2. *$F\circ F\le F$.* Given a pair $(k_1,k_2)$, use the single key
   $k = k_1 + k_2$ (mod $26$). The $i$-th letter of $e(e(m,k_1),k_2)$ is
   $(m_i + k_1) + k_2 = m_i + (k_1 + k_2)$, the $i$-th letter of $e(m,k)$.

3. Both embeddings hold, so $F\circ F\equiv F$ and the Caesar slide is
   idempotent. Encrypting twice gives no more security than encrypting once.
:::
