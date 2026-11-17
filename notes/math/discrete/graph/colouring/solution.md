<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6042f10-4-q4" status="draft"}
(a) A triangle together with one isolated vertex: every degree is at most $2$, the isolated vertex has degree $0<2$, but the triangle needs $3$ colours.

(b) The wrong sentence is "So $G_n$ satisfies the conditions of the induction hypothesis $P(n)$." It is justified by the claim that the neighbours of $v$ now have degree less than $k$, but if $v$ has no neighbours, $G_n$ may have no vertex of degree less than $k$ at all. That is exactly what happens in (a) when $v$ is the isolated vertex: $G_n$ is the triangle, which does not satisfy the hypothesis.
:::

::: {.solution for="prob-mit6042f10-4-q6" status="draft"}
(a)

1. A line graph $u_1,u_2,\dots,u_m$ is $2$-colourable: colour $u_i$ by the parity of $i$; consecutive vertices get different colours.

2. The edges of type (a) form the line graph $v_1,\dots,v_n$; colour it with $c_1(v_i)=i\bmod2$. The edges of type (b) form the line graph $v_{s_1},\dots,v_{s_n}$; colour it with $c_2(v_{s_k})=k\bmod2$.

3. Give $v$ the colour $(c_1(v),c_2(v))$, one of $4$ pairs. Adjacent vertices are adjacent in one of the two line graphs, so they differ in that coordinate.

(b) Colour $v_i$ by the parity of $i$. Type (a) edges join $i$ and $i+1$, of different parities. In the sequence $(1,a_1,3,a_2,5,\dots)$ the entries alternate between odd and even numbers, so type (b) edges also join vertices of different parities. Hence this is a $2$-colouring.
:::
