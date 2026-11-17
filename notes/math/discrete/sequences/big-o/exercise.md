<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-sequences-11 origin="external" source="fit1058-cn-6.16-q11"}
**The Big-O Game**, on a sequence $(a_n)$ and function
$f:\mathbb{N}\to\mathbb{R}_0^+$, played by Oh-Yes and Oh-No:

1.  Oh-Yes chooses a constant $c\in\mathbb{R}^+$ and a positive integer
    threshold $N$.

2.  Oh-No chooses a positive integer $n\ge N$.

Oh-Yes wins if $a_n\le c f(n)$; Oh-No wins if $a_n>cf(n)$.

Example: $a_n=n^2$, $f(n)=n^{1.5}$. Oh-Yes chooses $c=100$, $N=4$; Oh-No
chooses $n=10^6$, and wins since $a_n=10^{12}>10^{11}=100\,(10^6)^{1.5}$.

(a) In this play, could Oh-No have possibly lost on their move?

(b) What could Oh-Yes have chosen in order to win, and why?

(c) Play the game with someone.

(d) In general, what relationship must hold between the sequence and
    function for Oh-Yes to have a winning strategy?

(e) Propose a sequence and function for which Oh-No has a winning
    strategy, and describe it.

(f) In general, how must they be related for Oh-No to have a winning
    strategy?
:::

::: {.problem #prob-sequences-12 origin="external" source="fit1058-cn-6.16-q12"}
Give the simplest big-O expression you can for each of the following.

(a) $1+4n+6n^2+4n^3+n^4$

(b) $\binom n2$

(c) $\binom n3$

(d) the sum of the first $n$ terms of an arithmetic series with first
    term 1 and common difference $d$

(e) $2^n+2^{n-1}+\cdots+2+1$

(f) $(n!)^{1/n}$

(g) $n^{1/n}$
:::

::: {.problem #prob-mit6042f10-7-q5 origin="external" source="mit6042f10-7-q5"}
For each of the following six pairs of functions $f$ and $g$ (parts (a) through (f)), state which of these order-of-growth relations hold (more than one may hold, or none may hold):

$f = o(g)$ $\quad f = O(g)$ $\quad f = \omega(g)$ $\quad f = \Omega(g)$ $\quad f = \Theta(g)$ $\quad f \sim g$

| | $f(n)$ | $g(n)$ |
|---|---|---|
| (a) | $\log_2 n$ | $\log_{10} n$ |
| (b) | $2^n$ | $10^n$ |
| (c) | $0$ | $17$ |
| (d) | $1 + \cos\left(\frac{\pi n}{2}\right)$ | $1 + \sin\left(\frac{\pi n}{2}\right)$ |
| (e) | $1.0000000001^n$ | $n^{10000000000}$ |

*Note (these notes):* The statement says six pairs but lists five, (a)–(e).
:::

::: {.problem #prob-mit6006s20-1-q1 origin="external" source="mit6006s20-1-q1"}
**Asymptotic behavior of functions**

For each of the following sets of five functions, order them so that if $f_a$ appears before $f_b$ in your sequence, then $f_a=O(f_b)$. If $f_a=O(f_b)$ and $f_b=O(f_a)$ (meaning $f_a$ and $f_b$ could appear in either order), indicate this by enclosing $f_a$ and $f_b$ in a set with curly braces. For example, if the functions are:
$$f_1=n,\qquad f_2=\sqrt n,\qquad f_3=n+\sqrt n,$$
the correct answers are $(f_2,\{f_1,f_3\})$ or $(f_2,\{f_3,f_1\})$.

**Note:** Recall that $a^{b^c}$ means $a^{(b^c)}$, not $(a^b)^c$, and that $\log$ means $\log_2$ unless a different base is specified explicitly. Stirling's approximation may help for comparing factorials.

| a) | b) | c) | d) |
|---|---|---|---|
| $f_1=\log(n^n)$ | $f_1=2^n$ | $f_1=n^n$ | $f_1=n^{n+4}+n!$ |
| $f_2=(\log n)^n$ | $f_2=6006^n$ | $f_2=\binom n{n-6}$ | $f_2=n^{7\sqrt n}$ |
| $f_3=\log(n^{6006})$ | $f_3=2^{6006^n}$ | $f_3=(6n)!$ | $f_3=4^{3n\log n}$ |
| $f_4=(\log n)^{6006}$ | $f_4=6006^{2^n}$ | $f_4=\binom n{n/6}$ | $f_4=7^{n^2}$ |
| $f_5=\log\log(6006n)$ | $f_5=6006^{n^2}$ | $f_5=n^6$ | $f_5=n^{12+1/n}$ |
:::

::: {.problem #prob-mit6046s15-1-q11 origin="external" source="mit6046s15-1-q11"}
**Asymptotic Growth**

Sort all the functions below in increasing order of asymptotic (big-$O$) growth. If some have the same asymptotic growth, then be sure to indicate that. As usual, $\lg$ means base 2.

1. $5n$
2. $4\lg n$
3. $4\lg\lg n$
4. $n^4$
5. $n^{1/2}\lg^4n$
6. $(\lg n)^{5\lg n}$
7. $n^{\lg n}$
8. $5^n$
9. $4^{n^4}$
10. $4^{4^n}$
11. $5^{5^n}$
12. $5^{5n}$
13. $n^{n^{1/5}}$
14. $n^{n/4}$
15. $(n/4)^{n/4}$

*Note (these notes):* This is Exercise 1-1 of the problem set (an exercise not handed in); it is numbered after the problems here.
:::
