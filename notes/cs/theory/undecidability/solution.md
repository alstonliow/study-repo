<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-4-q18" status="draft"}
1. *($\Leftarrow$)* Let $D$ be decided by $M_D$. On input $x$, for $y=s_1,s_2,\dots$ in standard order, run $M_D$ on $\langle x,y\rangle$ and accept if it accepts. Each run halts, so this accepts $x$ iff some $y$ has $\langle x,y\rangle\in D$, that is, iff $x\in C$. So $C$ is Turing-recognizable.

2. *($\Rightarrow$)* Let $M$ recognize $C$, and let
$$D=\{\langle x,t\rangle\mid M \text{ accepts } x \text{ within } t \text{ steps}\},$$
with $t$ written in binary. A TM decides $D$ by simulating $M$ on $x$ for $t$ steps.

3. Now $x\in C$ iff $M$ accepts $x$ after some finite number $t$ of steps iff $\exists t\,(\langle x,t\rangle\in D)$. So $C$ has the required form.
:::
