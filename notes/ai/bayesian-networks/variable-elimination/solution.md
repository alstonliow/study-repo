<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs188hw-7-q1" status="draft"}
Parts 1–5 use the factorisation $P(E,S,M,B)=P(E)P(M)P(S\mid E,M)P(B\mid M)$ (@def-bayesian-network); numbers were checked in Python.

1. $P(-e,-s,-m,-b)=P(-e)P(-m)P(-s\mid-e,-m)P(-b\mid-m)=0.6\cdot0.9\cdot0.9\cdot0.9=0.4374$.
2. $P(+b)=\sum_mP(m)P(+b\mid m)=0.1\cdot1.0+0.9\cdot0.1=0.19$.
3. $P(+m\mid+b)=\dfrac{P(+m)P(+b\mid+m)}{P(+b)}=\dfrac{0.1\cdot1.0}{0.19}=\dfrac{10}{19}\approx0.526$.
4. Normalising over $m$, with $P(+e)$ cancelling:
$$
P(+m\mid+s,+b,+e)=\frac{P(+m)P(+s\mid+e,+m)P(+b\mid+m)}{\sum_mP(m)P(+s\mid+e,m)P(+b\mid m)}=\frac{0.1\cdot1.0\cdot1.0}{0.1+0.9\cdot0.8\cdot0.1}=\frac{0.1}{0.172}\approx0.581.
$$
5. $P(+e\mid+m)=P(+e)=0.4$: the only path between $E$ and $M$ is the v-structure $E\to S\leftarrow M$, and $S$ is not observed, so $E\perp M$ (@def-d-separation).
6. $C$ appears in $P(C\mid B)$, $P(D\mid C)$, $P(E\mid C,D)$, $P(+f\mid C,E)$, $P(G\mid C,+f)$; joining them and summing out $C$ gives
$$
f_2(B,D,E,G)=\sum_cP(c\mid B)\,P(D\mid c)\,P(E\mid c,D)\,P(+f\mid c,E)\,P(G\mid c,+f).
$$
Left: $f_1(B)$, $f_2(B,D,E,G)$.
7. $f_3(B,D,G)=\sum_ef_2(B,D,e,G)$. Left: $f_1(B)$, $f_3(B,D,G)$.
8. $f_4(B,D)=\sum_gf_3(B,D,g)$. Left: $f_1(B)$, $f_4(B,D)$.
9. Join the two remaining factors, $f_1(B)\,f_4(B,D)=P(B,D,+f)$, a table with four entries, and normalise it: divide each entry by their sum, which is $P(+f)$ (@thm-variable-elimination).
10. $f_2(B,D,E,G)$: four binary variables, $16$ rows ($f_1$ has $2$, $f_3$ has $8$, $f_4$ has $4$).
11. One ordering is $G,A,E,C$:

    | eliminated | factor generated |
    |---|---|
    | $G$ | $f_1(C)=\sum_gP(g\mid C,+f)$, which equals $1$ for every $C$ |
    | $A$ | $f_2(B)=\sum_aP(a)P(B\mid a)$ |
    | $E$ | $f_3(C,D)=\sum_eP(e\mid C,D)P(+f\mid C,e)$ |
    | $C$ | $f_4(B,D)=\sum_cP(c\mid B)P(D\mid c)f_3(c,D)f_1(c)$ |

    Every generated factor has at most two variables. Eliminating $C$ early is what made $f_2$ large: $C$ is linked to $B,D,E,G$; after $G$ and $E$ are gone it is linked only to $B$ and $D$. (Any order eliminating $G$ and $E$ before $C$ works, for example $A,G,E,C$.)
:::

::: {.solution for="prob-cs188d-7-q1" status="draft"}
(b) $f_2(+z,U,V,W)=\sum_tP(t)P(U\mid t)P(V\mid t)P(W\mid t)f_1(+z\mid t)$; left: $P(Y\mid V,W)$, $f_2(+z,U,V,W)$.

(c) $f_3(+z,V,W)=\sum_uf_2(+z,u,V,W)$; left: $P(Y\mid V,W)$, $f_3(+z,V,W)$.

(d) $f_4(+z,W,Y)=\sum_vP(Y\mid v,W)f_3(+z,v,W)$; left: $f_4(+z,W,Y)$.

(e) $f_5(+z,Y)=\sum_wf_4(+z,w,Y)$; left: $f_5(+z,Y)$.

(f) $f_5(+z,Y)=P(+z,Y)$; normalise it over $Y$: $P(y\mid+z)=f_5(+z,y)/\sum_{y'}f_5(+z,y')$ (@thm-variable-elimination).

(g) $f_2$, with the three unknown variables $U,V,W$ ($+z$ is fixed): $2^{3}=8$ entries. (The join formed before summing out $T$ has four unknown variables, $16$ entries.)

(m) **Yes.** Eliminate $U$ first: $\sum_uP(u\mid T)=1$, a trivial factor. Then $X$ gives $f(+z\mid T)$ as before, and $T$ now joins only $P(T)$, $P(V\mid T)$, $P(W\mid T)$ and $f(+z\mid T)$, giving a factor on $V,W$; then $V$ and $W$ give factors on $W,Y$ and on $Y$. With the order $U,X,T,V,W$ no factor has more than two unknown variables ($4$ entries). Eliminating $T$ while $U$ is still present is what created the large $f_2$: $T$ is the common parent of four variables.
:::
