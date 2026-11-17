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

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-4-q1" status="draft"}
For $n=0$ read $F_{-1}=1$, the value that keeps $F_1=F_0+F_{-1}$ true; then $\gcd(F_0,F_{-1})=\gcd(0,1)=1$. For $n\ge1$ we use induction.

1. *Base case $n=1$:* $\gcd(F_1,F_0)=\gcd(1,0)=1$.

2. *Step:* suppose $\gcd(F_n,F_{n-1})=1$. Since $\gcd(a,b)=\gcd(a-b,b)$ (a common divisor of $a$ and $b$ divides $a-b$, and conversely),
   $$\gcd(F_{n+1},F_n)=\gcd(F_{n+1}-F_n,F_n)=\gcd(F_{n-1},F_n)=1.$$
:::

::: {.solution for="prob-mit6042f10-3-q2" status="draft"}
(a) $b=ma$ gives $bc=(mc)a$.

(b) $b=ma$ and $c=la$ give $sb+tc=(sm+tl)a$.

(c) If $b=ma$ then $cb=m(ca)$. Conversely, if $cb=m(ca)$, cancel $c>0$: $b=ma$.

(d) Let $d=\gcd(a,b)$.

1. $kd$ divides $ka$ and $kb$ by (c), so it is a common divisor, and $kd\le\gcd(ka,kb)$.

2. By Bézout (@thm-bezout), $d=sa+tb$ for some integers $s,t$, so $kd=s(ka)+t(kb)$. Every common divisor of $ka$ and $kb$ divides $kd$ by (b), so $\gcd(ka,kb)\le kd$.

3. Hence $\gcd(ka,kb)=kd$.
:::

::: {.solution for="prob-mit6042f10-3-q5" status="draft"}
Let $g=\gcd(x,y)$.

(a) By induction on the number of moves, every number on the board is $x$, $y$ or a divisor of $g$. Initially only $x,y$ are there. A new number $d$ divides two numbers on the board. If they are $x$ and $y$, then $d\mid g$. Otherwise one of them is a divisor $e$ of $g$, and $d\mid e\mid g$.

(b) At the end no move is possible. A divisor of $g$ not yet on the board would be a common divisor of $x$ and $y$, which are on the board, so it could be written: a contradiction.

(c) By (a) and (b) the final board is exactly $\{x,y\}$ together with the divisors of $g$, whatever the players do. So the number of moves in the game is fixed: $m$ = the number of divisors of $g$ other than $x$ and $y$. Go first if $m$ is odd and second if $m$ is even; then you make the last move and your opponent cannot play.
:::
