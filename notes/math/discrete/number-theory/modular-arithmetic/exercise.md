<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-number-theory-03 origin="external" source="fit1058-cn-7.19-q3"}
Represent days of the week by $\mathbb{Z}_7$ (Sunday $=0$, Monday $=1$, …). Let
$d\in\mathbb{Z}_7$ be the day of the week of a given date this year.

(a) Give an expression in $d$, using mod, for the day of the week of
    the same date next year.

(b) How would you modify it if there is a leap day (29 February)
    between that date and the same date next year?

(c) Let $d$ be the day of the week of 29 February in some leap year.
    Assuming the next leap year is four years later, give an expression
    for the weekday of the next 29 February.
:::

::: {.problem #prob-number-theory-08 origin="external" source="fit1058-cn-7.19-q8"}
Restate the definitions of the Caesar slide encryption and decryption
functions (Exercise 2.15) using the mod operation.
:::

::: {.problem #prob-number-theory-10 origin="external" source="fit1058-cn-7.19-q10"}
The *digital sum* $\mathrm{ds}(n)$ of $n$ is the sum of its decimal
digits, e.g. $\mathrm{ds}(1984)=1+9+8+4=22$.

(a) Prove that for all $n\in\mathbb{N}$,
    $n\bmod3=\mathrm{ds}(n)\bmod3$.

(b) A similar method works for remainders mod 9. Explain why, briefly.

(c) The *alternating digital sum* $\mathrm{ads}(n)$ alternately
    adds and subtracts digits, starting with addition at the right-hand
    end, e.g. $\mathrm{ads}(1984)=-1+9-8+4=4$. Prove that for all
    $n\in\mathbb{N}$, $n\bmod11=\mathrm{ads}(n)\bmod11$.

(d) Devise a similar technique for working out $n\bmod3$ from the bits
    of the binary representation of $n$.
:::

::: {.problem #prob-number-theory-11 origin="external" source="fit1058-cn-7.19-q11"}
For each equation, use the method of Exercise 10(b) to work out by hand the
remainder mod 9 of each side. Comment on what comparing them tells you.

(a) $92\times31=2847$

(b) $92\times31=2852$

(c) $92\times31=2861$

(d) $2718281828\times3141592653=8539734219628209634$
:::

::: {.problem #prob-number-theory-15 origin="external" source="fit1058-cn-7.19-q15"}
**Modular multiplication cryptosystem.** Messages and cyphertexts are
strings over the 26-letter alphabet, with $\mathtt a,\dots,\mathtt z$ as
$0,\dots,25\in\mathbb{Z}_{26}$. The key is $k\in\mathbb{Z}_{26}$, and
$$c_i = k\,m_i \bmod 26.$$

(a) Not all keys work properly. What restriction must be placed on
    members of $\mathbb{Z}_{26}$ so they work as keys? Specify the keyspace in
    mathematical notation.

(b) Define the decryption function.

(c) How would modular multiplication work for an arbitrary alphabet
    size $n$? Define its keyspace, encryption and decryption functions.
:::
