<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-number-theory-18" status="draft"}
1. List the powers of $7$ mod $11$:

   | $x$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
   |---|---|---|---|---|---|---|---|---|---|---|
   | $7^x\bmod 11$ | 7 | 5 | 2 | 3 | 10 | 4 | 6 | 9 | 8 | 1 |

2. $y_A = 2 = 7^3$, so Alice's private number is $x_A = 3$.

3. $y_B = 8 = 7^9$, so Bob's private number is $x_B = 9$.

4. The shared key is
   $$k = 7^{x_Ax_B} = y_B^{x_A} = 8^3 = 512\equiv 6\pmod{11}.$$
   Check: $y_A^{x_B} = 2^9 = 512\equiv 6$.
:::

::: {.solution for="prob-number-theory-19" status="draft"}
(a) $18$ is not prime, but Diffie–Hellman only needs a primitive root.
    $\varphi(18) = 6$, and $\mathbb Z_{18}^* = \{1,5,7,11,13,17\}$. The powers
    of $5$ mod $18$ are $5, 7, 17, 13, 11, 1$, so $5$ is a primitive root.
    Choose $a = 5$ (or $a = 11$, the only other one).

(b) The change makes the system weaker, not stronger.

    An exhaustive attack tries the possible powers of $a$. With $p = 17$
    there are $\varphi(17) = 16$ of them. With $n = 18$ there are only
    $\varphi(18) = 6$. So the attacker's work falls to $6/16$ of what it was,
    a decrease of about $62\%$.

    The number of keys depends on $\varphi(n)$, not on the size of $n$. A
    composite modulus also has extra structure that an attacker can exploit.
:::

::: {.solution for="prob-number-theory-20" status="draft"}
By Fermat's little theorem, $a^{p-1}\equiv 1\pmod p$. So A's public number is
$$y_A = a^{p-1}\bmod p = 1.$$

Every shared key of A is then $k_{AB} = y_A^{x_B} = 1$. Since $y_A = 1$ is
public, everyone can see that A's shared key with anyone is $1$. The security
is destroyed completely.

More generally, A should choose $x_A$ with $1\le x_A\le p-2$.
:::

::: {.solution for="prob-number-theory-21" status="draft"}
Use one public prime $p$ and primitive root $a$, and let A, B, C choose
private numbers $x_A, x_B, x_C$. Arrange them in a ring
$A\to B\to C\to A$.

1. *Round 1.* Each person sends $a^{x}$ to the next person:
   A sends $a^{x_A}$ to B, B sends $a^{x_B}$ to C, and C sends $a^{x_C}$ to A.

2. *Round 2.* Each person raises what they received to their own private
   number and passes it on. B sends $a^{x_Ax_B}$ to C, C sends
   $a^{x_Bx_C}$ to A, and A sends $a^{x_Cx_A}$ to B.

3. *Key.* Each person raises what they received in round 2 to their own
   private number. C computes $(a^{x_Ax_B})^{x_C}$, A computes
   $(a^{x_Bx_C})^{x_A}$, and B computes $(a^{x_Cx_A})^{x_B}$. All three get
   $$k = a^{x_Ax_Bx_C}\bmod p.$$

Checking the conditions:

- No secret is shared at the start, and $k$ itself is never sent.
- An eavesdropper sees $a^{x_A}, a^{x_B}, a^{x_C}$ and
  $a^{x_Ax_B}, a^{x_Bx_C}, a^{x_Cx_A}$. To obtain $k$ they must combine two
  of these without knowing any exponent, which is a Diffie–Hellman problem
  and believed to be hard.
- Any one or two of the three are missing a private exponent. For example,
  A and B together know $x_A$ and $x_B$ but need $x_C$ (or a message from
  C) to reach $a^{x_Ax_Bx_C}$.
:::
