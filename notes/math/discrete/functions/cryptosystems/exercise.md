<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-functions-15 origin="external" source="fit1058-cn-2.19-q15"}
**Caesar slide cryptosystem.** Each letter of the message is slid
rightwards along the alphabet (with wrap-around) by a fixed key $k$. E.g. with $k=3$ (i.e. key letter `d`),
`thefamilyofdashwoodhadlongbeen` encrypts to
`wkhidplobrigdvkzrrgkdgorqjehhq`.

Formally: message space $M$ = all strings of lower-case English letters; key
space $K=\{\mathtt a,\dots,\mathtt z\}$; cypher space $C=M$. Identify letters
with $\{0,\dots,25\}$ and let $+$/$-$ be letter addition/subtraction mod 26.

- Encryption $e:M\times K\to M$:
  $e(m_1\cdots m_n,k)=c_1\cdots c_n$ with $c_i=m_i+k$.

- Decryption $d:M\times K\to M$:
  $d(c_1\cdots c_n,k)=m_1\cdots m_n$ with $m_i=c_i-k$.

Using the definitions of *embeddable*, *equivalent* and
*idempotent* from Assignment 1, prove that the Caesar slide cryptosystem
is idempotent.
:::
