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
