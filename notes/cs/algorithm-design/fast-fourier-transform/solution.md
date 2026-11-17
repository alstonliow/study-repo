<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046s15-2-q1" status="draft"}
(a) For each $j=0,\dots,n-m$, compare $P[k]$ with $S[j+k]$ for $k<m$, skipping wild cards; output $j$ if all agree. $O((n-m+1)m)=O(nm)$.

(b) Encode $S$ as $s(x)=\sum_is_ix^i$ with $s_i=1$ for $a$ and $-1$ for $b$, and the *reversed* pattern as $p(x)=\sum_kp_{m-1-k}x^k$ with $p_k=1$ for $a$, $-1$ for $b$ and $0$ for $*$. The coefficient of $x^{j+m-1}$ in $s(x)p(x)$ is $c_j=\sum_{k=0}^{m-1}s_{j+k}p_k$. Each non-wild position contributes $+1$ if the symbols agree and $-1$ if not, so $P$ matches at $j$ exactly when $c_j$ equals $q$, the number of non-$*$ symbols of $P$. In the example, $s=(1,-1,1,-1,-1,1,-1)$, the reversed pattern is $(0,-1,1)$, and the product has coefficients $0,-1,2,-2,2,0,-2,2,-1$; with $q=2$, the coefficients of $x^{j+2}$ for $j=0,\dots,4$ are $2,-2,2,0,-2$, so $M=[0,2]$.

(c) One FFT-based multiplication (@cor-fast-polynomial-multiplication) of polynomials of degree less than $n$: $O(n\lg n)$. (Cutting $S$ into overlapping pieces of length $2m$ improves this to $O(n\lg m)$.)

(d) For each letter $c\in\{A,C,G,T\}$, let $d^{(c)}$ be the $0/1$ indicator sequence of $c$ in $D$ and $p^{(c)}$ that of $c$ in the reversed pattern. The coefficient of $x^{j+m-1}$ in $\sum_cd^{(c)}(x)p^{(c)}(x)$ counts the non-wild positions of $P$ that agree with $D$ at offset $j$; $P$ matches iff it equals $q$. Four multiplications, $O(n\lg n)$. For $D=ACGACCAT$ and $P=AC{*}A$ ($q=3$) the counts at $j=0,\dots,4$ are $3,0,0,3,1$, so $M=[0,3]$.
:::
