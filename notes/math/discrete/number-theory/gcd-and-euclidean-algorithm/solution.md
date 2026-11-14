<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-number-theory-12" status="draft"}
For $(55,34)$ every quotient is $1$, so each step is a single subtraction:
$$\gcd(55,34) = \gcd(34,21) = \gcd(21,13) = \gcd(13,8) = \gcd(8,5) = \gcd(5,3) = \gcd(3,2) = \gcd(2,1) = 1.$$
That is $7$ subtractions, and every number that appears is a Fibonacci number:
each remainder is the Fibonacci number just below the smaller one.

Now the proof. Use $f_1 = f_2 = 1$ and $f_{k+1} = f_k + f_{k-1}$, so
$34 = f_9$ and $55 = f_{10}$, and $7 = 9-2$. Let $P(n)$ be the statement:
the Euclidean algorithm on $(f_{n+1}, f_n)$ uses $n-2$ subtractions and every
intermediate number is a Fibonacci number.

1. *Base case $n=3$.* $(f_4,f_3) = (3,2)$. Since $2\nmid 3$, one subtraction
   gives $3 - 2 = 1 = f_2$, and then $1\mid 2$ stops the algorithm. That is
   $1 = 3-2$ subtraction, and all numbers are Fibonacci numbers.

2. *Inductive step.* Let $n\ge 3$ and assume $P(n)$. Consider
   $(f_{n+2}, f_{n+1})$.

3. Since $n\ge 3$, we have $0 < f_n < f_{n+1}$, so
   $f_{n+2} = 1\cdot f_{n+1} + f_n$ is the division with remainder. The
   remainder $f_n$ is nonzero, so $f_{n+1}\nmid f_{n+2}$. This step is one
   subtraction and produces the Fibonacci number $f_n$.

4. The algorithm continues with $(f_{n+1}, f_n)$. By $P(n)$ this takes $n-2$
   more subtractions, all producing Fibonacci numbers.

5. In total that is $1 + (n-2) = (n+1) - 2$ subtractions, which is
   $P(n+1)$. By induction, $P(n)$ holds for all $n\ge 3$.
:::
