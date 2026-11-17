---
title: "The RSA Cryptosystem"
sources: [cs70-7]
requires: [math/discrete/number-theory/chinese-remainder-theorem, math/discrete/number-theory/modular-exponentiation]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 7 (cs70-7), in our own wording; the proof is written out in steps. -->

## Public-key cryptography

::: {#rmk-rsa-public-key .remark name="A lock anyone can close"}

In private-key cryptography, Alice and Bob share a secret beforehand. In *public-key* cryptography, Bob publishes a *public key* that anyone can use to encrypt a message to him, and keeps a *private key* that only he can use to decrypt. Alice can write to Bob securely without ever having met him. Compare Diffie–Hellman (@sec-math-discrete-number-theory-diffie-hellman), which agrees on a shared key but does not encrypt.

:::

## The scheme

::: {#def-rsa .definition name="RSA"}

Bob chooses two large primes $p\ne q$ and puts $N=pq$. He chooses $e$ coprime to $(p-1)(q-1)$ and computes $d=e^{-1}\bmod(p-1)(q-1)$ (@thm-inverse).

- Public key: $(N,e)$. Private key: $d$. The primes $p,q$ are kept secret.
- Encryption of a message $x\in\{0,\dots,N-1\}$: $E(x)=x^e\bmod N$.
- Decryption of $y$: $D(y)=y^d\bmod N$.

:::

::: {#thm-rsa-correct .theorem name="RSA decrypts correctly"}

$D(E(x))=x$ for every $x\in\{0,1,\dots,N-1\}$.

:::

::: {.proof}

1. $D(E(x))=x^{ed}\bmod N$, so we must show $x^{ed}\equiv x\pmod N$.

2. Since $ed\equiv1\pmod{(p-1)(q-1)}$, write $ed=1+k(p-1)(q-1)$ with $k\ge0$.

3. **Modulo $p$.** If $p\nmid x$, Fermat's Little Theorem (@cor-flt) gives $x^{p-1}\equiv1$, so $x^{ed}=x\cdot\bigl(x^{p-1}\bigr)^{k(q-1)}\equiv x\pmod p$. If $p\mid x$, both sides are $0$ modulo $p$.

4. **Modulo $q$.** The same argument with $p$ and $q$ swapped gives $x^{ed}\equiv x\pmod q$.

5. So $x^{ed}-x$ is divisible by $p$ and by $q$, which are coprime, hence by $N=pq$ (@prp-coprimedivides). Equivalently, $x^{ed}$ and $x$ solve the same pair of congruences, so they agree modulo $N$ by the Chinese Remainder Theorem (@thm-crt-two).

:::

## Security and practice

::: {#rmk-rsa-security .remark name="Why it is believed secure"}

RSA rests on an assumption, not a proof: given $N$, $e$ and $x^e\bmod N$, there is no efficient way to find $x$. Trying all $x$ takes about $N$ steps. Factoring $N$ into $p$ and $q$ would reveal $d$, but no efficient factoring algorithm is known. The security of RSA has not been proved.

:::

::: {#rmk-rsa-practice .remark name="Why it is practical"}

Bob's work is easy. Testing whether a number is prime takes time polynomial in its number of bits, so he picks random numbers of the right size until two are prime. Encryption and decryption are modular exponentiations: square-and-multiply (@sec-math-discrete-number-theory-modular-exponentiation) needs $O(\log N)$ multiplications of $O(\log N)$-bit numbers, about $O((\log N)^3)$ bit operations in all.

:::

::: {#thm-prime-number-theorem .theorem name="Prime Number Theorem"}

Let $\pi(n)$ be the number of primes $\le n$. Then $\pi(n)\ge\dfrac n{\ln n}$ for all $n\ge17$, and $\dfrac{\pi(n)}{n/\ln n}\to1$ as $n\to\infty$.

:::

::: {#rmk-rsa-pnt .remark name="Primes are common enough"}

The theorem is stated without proof; the usual proofs need complex analysis. It means that about one $512$-bit number in $\ln2^{512}\approx355$ is prime, so a random search finds a prime quickly.

:::
