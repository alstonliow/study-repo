<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-sequences-08 origin="external" source="fit1058-cn-6.16-q8"}
Define $(t_n:n\in\mathbb{N})$ by $t_1=1$, $t_n=3-\frac12 t_{n-1}$.

(a) Consider the following theorem (correct) and its “proof”
    (incorrect). Find the errors in the proof.

    **Theorem.** For all $n\in\mathbb{N}$, $t_n\le\frac52$.

    **“Proof”.**

    1.  For each $n\in\mathbb{N}$, let $S(n)$ be the statement that
        $t_n\le5/2$. We must prove $S(n)$ for every $n\in\mathbb{N}$.

    2.  Inductive basis: Let $n=1$. Then
        $t_1=3-\frac12\cdot1\le5/2$. So $S(1)$ holds.

    3.  Inductive step:

    4.  Assume that for some $k$ the statement $S(k)$ holds.
        (Inductive Hypothesis.)

    5.  Consider $S(k+1)$.

    6.  $t_{k+1} = 3-\frac12 t_k$

    7.  $\phantom{t_{k+1}}\le 3-\frac12\cdot\frac52$(by the
        Inductive Hypothesis)

    8.  $\phantom{t_{k+1}}= 3-\frac54$

    9.  $\phantom{t_{k+1}}= \frac74$

    10. $\phantom{t_{k+1}}\le\frac52$.

    11. 11\. “$\square$”

(b) Write a correct proof by induction for the theorem. Two approaches:

    (i) Prove by induction that for all $n\in\mathbb{N}$,
        $1\le t_n\le\frac52$ (a stronger statement).

    (ii) Prove that $S(n)$ holds for all even $n$, and then for all
         odd $n$.
:::

::: {.problem #prob-sequences-09 origin="external" source="fit1058-cn-6.16-q9"}
Define $(\varphi_n:n\in\mathbb{N})$ by $\varphi_1=1$,
$\varphi_n=1+\dfrac1{\varphi_{n-1}}$.

(a) Find the first 20 terms (spreadsheet or program).

(b) Conjecture a value for the limit $\varphi$ as $n\to\infty$.

(c) If $\varphi_n\approx\varphi_{n-1}$, the limit should satisfy
    $\varphi=1+\frac1\varphi$. Solve this to derive a conjectured exact
    value for the limit.

(d) Determine $N$ so that for all $n\ge N$,
    $|\varphi_n-\varphi|<0.001$. (Computationally is fine.)

(e) Prove that if $\varphi_n<\varphi+0.001$ then
    $\varphi_{n+1}>\varphi-0.001$.
    Hints: $w+0.001=w\bigl(1+\frac{0.001}w\bigr)$; and for all $x>0$,
    $\frac1{1+x}>1-x$.

(f) Prove that if $\varphi_n>\varphi-0.001$ then
    $\varphi_{n+1}<\varphi+0.001$.
    Hint: for $0<x<\frac13$, $\frac1{1-x}<1+\frac32x$.

(g) Deduce that if $\varphi-0.001<\varphi_n<\varphi+0.001$ then
    $\varphi-0.001<\varphi_{n+1}<\varphi+0.001$.

(h) Use (g) to prove by induction on $n$ that for all $n\ge N$,
    $\varphi-0.001<\varphi_n<\varphi+0.001$.
:::

::: {.problem #prob-sequences-10 origin="external" source="fit1058-cn-6.16-q10"}
**The Limit Game**, played on a sequence $(a_n)_{n=1}^\infty$ by Lim and
Una:

1.  Lim chooses a number $a$ (a proposed limit).

2.  Una chooses a real $\varepsilon>0$.

3.  Lim chooses a positive integer $N$.

4.  Una chooses a positive integer $n\ge N$.

Lim wins if $|a_n-a|<\varepsilon$; Una wins if $|a_n-a|\ge\varepsilon$.

Example: sequence $((-1)^{n+1}/n)$. Lim chooses $a=\frac12$, Una
$\varepsilon=\frac14$, Lim $N=3$, Una $n=5$. Una wins since
$|a_5-a|=|\frac15-\frac12|=\frac3{10}\ge\frac14$.

(a) In this play, could Una have possibly lost on her last move?

(b) Given the first two moves as above, could Lim have chosen an $N$
    guaranteeing a win?

(c) Given Lim’s first move, are all Una’s options equally good? Is she
    certain to win whatever $\varepsilon$ she chooses? What advice
    would you give her?

(d) What should Lim choose on the very first move, and why?

(e) Play the game with someone, on sequences of your choice.

(f) In general, what property must a sequence have for Lim to have a
    winning strategy?

(g) Propose a sequence for which Una has a winning strategy, and
    describe it.

(h) In general, what property must a sequence have for Una to have a
    winning strategy?
:::
