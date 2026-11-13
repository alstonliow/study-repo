<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-number-theory-18 origin="external" source="fit1058-cn-7.19-q18"}
Alice and Bob use Diffie-Hellman with public prime $p=11$ and primitive root
$a=7$. Their public numbers are $y_A=2$, $y_B=8$. As the cryptanalyst, find
their private numbers and the shared key.
:::

::: {.problem #prob-number-theory-19 origin="external" source="fit1058-cn-7.19-q19"}
You have been using Diffie-Hellman with $p=17$ and $a=7$. Your General
Manager decides that “bigger is better” and you will now use $p=18$ (with
appropriate $a$).

(a) What value of $a$ would you choose?

(b) What are the security implications of the change? Estimate e.g. the percentage change in the time for an exhaustive attack.
:::

::: {.problem #prob-number-theory-20 origin="external" source="fit1058-cn-7.19-q20"}
Explain how the security of Diffie-Hellman is affected if user A selects
private key $x_A=p-1$ (where $p$ is the prime modulus).
:::

::: {.problem #prob-number-theory-21 origin="external" source="fit1058-cn-7.19-q21"}
Devise a variant of Diffie-Hellman enabling three people A, B, C to arrive at
a common secret key, such that:

- they initially have no secret information in common;

- the common key itself is not sent anywhere by anyone;

- it is hard for an eavesdropper (knowing only public information)
  to determine the key;

- no one or two of A, B, C can find the key without the cooperation
  of the other(s).
:::
