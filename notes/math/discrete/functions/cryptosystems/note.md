---
title: "Cryptosystems"
sources: [fit1058-cn-2.10]
requires: [math/discrete/functions/composition]
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/02-functions.tex: Cryptosystems. -->

::: {#def-cryptosystem .definition name="Cryptosystem"}

A *cryptosystem* consists of a message space $M$, cyphertext space $C$, keyspace $K$, an *encryption function* $e: M \times K \to C$, and a *decryption function* $d: C \times K \to M$, such that for every key $k \in K$, the single-argument functions
$$e_k : M \to C,\ e_k(m) = e(m,k), \qquad d_k : C \to M,\ d_k(c) = d(c,k)$$
satisfy:

(i) $e_k, d_k$ are bijective (onto their images), and

(ii) $d_k = e_k^{-1}$.

:::

::: {.remark}

Condition (ii) is the essential one: it forces $d_k(e_k(m)) = m$ for all $m \in M$ – decryption with $k$ genuinely undoes encryption with $k$.

:::

::: {#exm-shift-cipher .example name="Shift cipher"}

Take $M = C = \mathbb{Z}_{26} = \{0,1,\dots,25\}$ (letters as residues mod 26) and $K = \mathbb{Z}_{26}$. Define
$$e_k(p) = (p+k) \bmod 26, \qquad d_k(c) = (c-k) \bmod 26.$$
Each $e_k$ is a bijection on $\mathbb{Z}_{26}$ with $d_k = e_k^{-1}$, so $(M,C,K,e,d)$ is a cryptosystem. ($k=3$ is the classical Caesar cipher.)

:::

::: {#def-composition-of-cryptosystems .definition name="Composition of cryptosystems"}

Given $\mathcal{C} = (M,M,K,e,d)$ and $\mathcal{C}' = (M,M,K',e',d')$ (same message space), the *keyed composition* of encryption functions is
$$e' \bullet e : M \times (K \times K') \to M, \qquad (e' \bullet e)(m,(k,k')) = e'(e(m,k),k'),$$
and similarly $d \bullet d'$ for decryption. The composed cryptosystem is $\mathcal{C}' \circ \mathcal{C} = (M,M,K\times K', e'\bullet e, d\bullet d')$. For each key pair $(k,k')$, the resulting single-argument maps are exactly the ordinary function compositions:
$$e_{(k,k')} = e'_{k'} \circ e_k, \qquad d_{(k,k')} = d_k \circ d'_{k'}.$$

:::

::: {#prp-cryptosystems-1 .proposition}

The composition of two cryptosystems is a cryptosystem.

:::

::: {.proof}

Fix $(k,k') \in K \times K'$. Since $\mathcal{C}, \mathcal{C}'$ are cryptosystems, $e_k, e'_{k'}, d_k, d'_{k'}$ are all bijections. By the composition-preserves-bijectivity theorem (@sec-math-discrete-functions-composition), $e_{(k,k')} = e'_{k'} \circ e_k$ is a bijection. It remains to check $d_{(k,k')} = (e_{(k,k')})^{-1}$: since $(e'_{k'})^{-1} = d'_{k'}$ and $(e_k)^{-1} = d_k$, and the inverse of a composition reverses order, $(e'_{k'}\circ e_k)^{-1} = e_k^{-1} \circ (e'_{k'})^{-1} = d_k \circ d'_{k'} = d_{(k,k')}$, as required.

:::

::: {.remark name="Security is not guaranteed by composition"}

A good cryptosystem needs $e_k, d_k$ easy to compute *with* $k$, but $e_k$ hard to invert *without* $k$. Composing two hard-to-invert systems is often, but not always, harder still to break. Counterexample: composing two shift ciphers with keys $k,k'$ gives $e'_{k'}(e_k(p)) = (p+k+k') \bmod 26 = e_{k+k'}(p)$ – just another shift cipher, no stronger than a single shift, since the keyspace effectively collapses.

:::
