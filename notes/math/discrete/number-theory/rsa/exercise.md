::: {.problem #prob-cs70hw-4-q6 origin="external" source="cs70hw-4-q6"}
**A Taste of RSA.** Suppose that $p$ and $q$ are distinct odd primes (i.e. they are primes $> 2$). Define $N = pq$. Let $a$ be any integer that is relatively prime to $N$. In other words, $\gcd(a, N) = 1$. Prove that $a^{(p-1)(q-1)+1} \equiv a \pmod N$. It turns out that this equivalence is in fact the basis of RSA, as you will see soon in class.
:::

::: {.problem #prob-cs70hw-5-q1 origin="external" source="cs70hw-5-q1"}
**RSA with Just One Prime.** Given the message $x \in \{0, 1, \ldots, N - 1\}$ and $N = pq$, where $p$ and $q$ are prime numbers, conventional RSA encrypts $x$ with $y = E(x) \equiv x^e \pmod N$. The decryption is done by $D(y) \equiv y^d \pmod N$, where $d$ is the inverse of $e \pmod{(p - 1)(q - 1)}$.

Alice is trying to send a message to Bob, and as usual, Eve is trying to decipher what the message is. One day, Bob gets lazy and tells Alice that he will now use $N = p$, where $p$ is a 1024-bit prime number, as part of his public key. He tells Alice that it's okay, since Eve will have to try out $2^{1024}$ combinations to guess $x$. It is very likely that Eve will not find out the secret message in a reasonable amount of time! In this problem, we will see whether Bob is right or wrong. Assume that Eve has found out about this new setup and that she knows the public key.

Similar to the original method, for any message $x \in \{0, 1, \ldots, N - 1\}$, $E(x) \equiv x^e \pmod p$, and $D(y) \equiv y^d \pmod p$. Choose $e$ such that it is coprime with $p - 1$, and choose $d \equiv e^{-1} \pmod{p - 1}$.

(a) Prove that the message $x$ is recovered after it goes through your new encryption and decryption functions, $E(x)$ and $D(y)$.

(b) Can Eve compute $d$ in the decryption function? If so, by what algorithm and approximately how many iterations does it take for it to terminate?

(c) Given part (b), how would Eve recover $x$ and what algorithm would she use? Approximately how many iterations does it take to terminate?

(d) Based on the previous parts, can Eve recover the original message in a reasonable amount of time? Explain.
:::

::: {.problem #prob-cs70hw-5-q2 origin="external" source="cs70hw-5-q2"}
**Squared RSA.**

(a) Prove the identity $a^{p(p-1)} \equiv 1 \pmod{p^2}$, where $a$ is coprime to $p$, and $p$ is prime. (Hint: Try to mimic the proof of Fermat's Little Theorem from the notes.)

(b) Now consider the RSA scheme: the public key is $(N = p^2 q^2, e)$ for primes $p$ and $q$, with $e$ relatively prime to $p(p - 1)q(q - 1)$. The private key is $d = e^{-1} \pmod{p(p - 1)q(q - 1)}$. Prove that the scheme is correct for $x$ relatively prime to both $p$ and $q$, i.e. $x^{ed} \equiv x \pmod N$. (Hint: Try to mimic the proof of RSA correctness from the notes.)

*Note (these notes):* Part (b) assumes $p
e q$.
:::
