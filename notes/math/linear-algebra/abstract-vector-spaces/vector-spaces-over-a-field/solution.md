<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-las-1-q2" status="draft"}
(i)

1. Suppose $T\cup U$ is a subspace but $T\not\le U$ and $U\not\le T$. Pick $t\in T\setminus U$ and $u\in U\setminus T$.

2. $t+u\in T\cup U$. If $t+u\in T$, then $u=(t+u)-t\in T$; if $t+u\in U$, then $t=(t+u)-u\in U$. Both contradict the choice.

(ii) In $V=\mathbb R^2$ take $T=\langle e_1\rangle$, $U=\langle e_2\rangle$, $W=\langle e_1+e_2\rangle$, three distinct lines.

(a) $U\cap W=\{0\}$, so the left side is $T$; but $T+U=T+W=\mathbb R^2$, so the right side is $\mathbb R^2$.

(b) $T+U=\mathbb R^2$, so the left side is $W$; but $T\cap W=U\cap W=\{0\}$, so the right side is $\{0\}$.

(iii)

(a) $T+(U\cap W)\subseteq(T+U)\cap(T+W)$: if $x\in U\cap W$, then $t+x$ lies in $T+U$ (as $x\in U$) and in $T+W$ (as $x\in W$).

(b) $(T\cap W)+(U\cap W)\subseteq(T+U)\cap W$: a sum $a+b$ with $a\in T\cap W$, $b\in U\cap W$ lies in $T+U$, and in $W$ because $W$ is closed under addition.
:::
