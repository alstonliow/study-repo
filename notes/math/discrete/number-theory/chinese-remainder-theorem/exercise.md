::: {.problem #prob-cs70hw-4-q3 origin="external" source="cs70hw-4-q3"}
**Celebrate and Remember Textiles.** Mathematics and computing both owe an immense debt to textiles, where many key ideas originated.

Instructions for knitting patterns will tell you to begin by "casting on" the needle some multiple of $m$ plus $r$, where $m$ is the number of stitches to create one repetition of the pattern and $r$ is the number of stitches needed for the two edges of the piece. For example, in the simple rib stitch pattern below, the repeating pattern is of length $m = 4$, and you need $r = 2$ stitches for the edges.

```
edge stitch                    edge stitch
   +     X     X     O     O     +
         Pattern of length 4
```

Thus, to make the final piece wider, you can add as many multiples of the pattern of length 4 as you like; for example, if you want to repeat the pattern 3 times, you need to cast on a total of $3m + r = 3(4) + 2 = 14$ stitches (shown below).

```
+  X  X  O  O  X  X  O  O  X  X  O  O  +
```

You've decided to knit a 70-themed baby blanket as a gift for your cousin and want to incorporate rows from three different stitch patterns with the following requirements:

- Alternating Link: Multiple of 7, plus 4
- Double Broken Rib: Multiple of 4, plus 2
- Swag: Multiple of 5, plus 2

You want to be able to switch between knitting these different patterns without changing the number of stitches on the needle, so you must use a number of stitches that simultaneously meets the requirements of all three patterns. Find the smallest number of stitches you need to cast on in order to incorporate all three patterns in your baby blanket.
:::

::: {.problem #prob-cs70hw-4-q4 origin="external" source="cs70hw-4-q4"}
**Sparsity of Primes.** A prime power is a number that can be written as $p^i$ for some prime $p$ and some positive integer $i$. So, $9 = 3^2$ is a prime power, and so is $8 = 2^3$. $42 = 2 \cdot 3 \cdot 7$ is not a prime power.

Prove that for any positive integer $k$, there exists $k$ consecutive positive integers such that none of them are prime powers.

Hint: this is a Chinese Remainder Theorem problem
:::

::: {.problem #prob-cs70hw-5-q3 origin="external" source="cs70hw-5-q3"}
**The CRT and Lagrange Interpolation.** Let $n_1, \ldots, n_k$ be pairwise co-prime, i.e. $n_i$ and $n_j$ are co-prime for all $i \ne j$. The Chinese Remainder Theorem (CRT) tells us that there exist solutions to the following system of congruences:
$$\begin{aligned} x &\equiv a_1 \pmod{n_1} &&(1)\\ x &\equiv a_2 \pmod{n_2} &&(2)\\ &\ \ \vdots &&(\vdots)\\ x &\equiv a_k \pmod{n_k} &&(k)\end{aligned}$$
and all solutions are equivalent $\pmod{n_1 n_2 \cdots n_k}$. For this problem, parts (a)-(c) will walk us through a proof of the Chinese Remainder Theorem. We will then use the CRT to revisit Lagrange interpolation.

(a) We start by proving the $k = 2$ case: Prove that we can always find an integer $x_1$ that solves (1) and (2) with $a_1 = 1, a_2 = 0$. Similarly, prove that we can always find an integer $x_2$ that solves (1) and (2) with $a_1 = 0, a_2 = 1$.

(b) Use part (a) to prove that we can always find at least one solution to (1) and (2) for any $a_1, a_2$. Furthermore, prove that all possible solutions are equivalent $\pmod{n_1 n_2}$.

(c) Now we can tackle the case of arbitrary $k$: Use part (b) to prove that there exists a solution $x$ to (1)-(k) and that this solution is unique $\pmod{n_1 n_2 \cdots n_k}$.

For polynomials $p_1(x)$, $p_2(x)$ and $q(x)$ we say that $p_1(x) \equiv p_2(x) \bmod q(x)$ if $p_1(x) - p_2(x)$ is of the form $q(x) \times m(x)$ for some polynomial $m(x)$.

(d) Define the polynomials $x-a$ and $x-b$ to be co-prime if they have no common divisor of degree 1. Assuming that the CRT still holds when replacing $x$, $a_i$ and $n_i$ with polynomials (using the definition of co-prime polynomials just given), show that the system of congruences
$$\begin{aligned} p(x) &\equiv y_1 \pmod{(x - x_1)} &&(1')\\ p(x) &\equiv y_2 \pmod{(x - x_2)} &&(2')\\ &\ \ \vdots &&(\vdots)\\ p(x) &\equiv y_k \pmod{(x - x_k)} &&(k')\end{aligned}$$
has a unique solution $\pmod{(x - x_1) \cdots (x - x_k)}$ whenever the $x_i$ are pairwise distinct. What is the connection to Lagrange interpolation?

Hint: To show that a unique solution exists, you may use the fact that the CRT has a unique solution when certain properties are satisfied.
:::
