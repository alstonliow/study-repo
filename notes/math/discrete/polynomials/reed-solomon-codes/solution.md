<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-6-q2" status="draft"}
All arithmetic is modulo $17$; the decoder uses $k=1$ (two check packets), $E(x)=x+b_0$ and $Q$ of degree at most $3$, with $Q(i)=r_iE(i)$ for $i=0,\dots,4$ (@thm-berlekamp-welch).

(a) $P(x)=x^2$; the codeword is $(0,1,4,9,16)$.

(b) The received word is $(0,1,4,9,0)$. Solving the five linear equations gives $Q(x)=x^3+13x^2=x^2(x-4)$ and $E(x)=x+13=x-4$: the error is at $x=4$, as expected. Then $Q/E=x^2=P$.

(c) The received word is $(0,1,4,6,8)$. The equations give $Q(x)=2x^2+15x=2x(x-1)$ and $E(x)=x+16=x-1$, so $Q/E=2x$, and the decoder outputs $(0,2,4)$. The code corrects only $k=1$ error, but two packets were changed. The corrupted word happens to be within distance $1$ of the codeword $(0,2,4,6,8)$ of $2x$ (it differs only at $x=1$), so the decoder returns that codeword.

(d) Two distinct codewords come from distinct polynomials of degree at most $2$. Their difference is a non-zero polynomial of degree at most $2$, so it has at most $2$ roots (@thm-at-most-d-roots): the codewords agree in at most $2$ of the $5$ positions and differ in at least $3$.

The word $(1,1,3,7,13)$ is the codeword of $x^2-x+1$ (values at $0,\dots,4$). The non-codeword $(1,1,4,7,13)$ differs from it in one position. Any other codeword $c'$ is at distance at least $3$ from $(1,1,3,7,13)$, so by the triangle inequality for Hamming distance it is at distance at least $3-1=2$ from $(1,1,4,7,13)$.

(e) Let $k=\lfloor\frac{m-n}2\rfloor$ be the number of errors the decoder allows, and suppose it returns $\mathit{msg}$, with polynomial $P$ and $E=\mathrm{Encode}(\mathit{msg})$.

1. The decoder found $Q=PE_{\text{loc}}$ with $Q(i)=r_iE_{\text{loc}}(i)$ for all positions $i$, where $E_{\text{loc}}$ has degree $k$. Where $E_{\text{loc}}(i)\ne0$, this gives $P(i)=r_i$. $E_{\text{loc}}$ has at most $k$ roots, so $\mathrm{Hamming}(C_0,E)\le k$.

2. Every other codeword $E'$ has $\mathrm{Hamming}(E,E')\ge m-n+1\ge2k+1$. By the triangle inequality, $\mathrm{Hamming}(C_0,E')\ge2k+1-k=k+1>\mathrm{Hamming}(C_0,E)$.

So whenever the decoder outputs a message, its codeword is the unique nearest codeword to $C_0$, even if that is not the codeword that was sent.
:::

::: {.solution for="prob-cs70hw-6-q3" status="draft"}
1. Let $a$ and $b$ be codewords of the messages $(c_0,\dots,c_{n-1})$ and $(d_0,\dots,d_{n-1})$, with polynomials $p(x)=\sum_jc_jx^j$ and $q(x)=\sum_jd_jx^j$.

2. Then $p+q=\sum_j(c_j+d_j)x^j$ is the polynomial of the message $(c_0+d_0,\dots,c_{n-1}+d_{n-1})$, also of degree at most $n-1$.

3. Its codeword is $\bigl((p+q)(i)\bigr)_{i=0}^{m-1}=\bigl(p(i)+q(i)\bigr)_i=a+b$. So $a+b$ is a codeword. (The same argument shows that $\lambda a$ is a codeword for every scalar $\lambda$.)
:::

::: {.solution for="prob-cs70hw-6-q4" status="draft"}
1. $a$ and $b$ are the values at the $m$ evaluation points of polynomials $p$ and $q$ of degree at most $n-1$.

2. The product $pq$ has degree at most $2n-2$, so it is the polynomial of a message of length $2n-1$ (its $2n-1$ coefficients, or its values at the first $2n-1$ points; this needs $m\ge2n-1$).

3. Its values are $(pq)(i)=p(i)q(i)=a_ib_i=c_i$. So $c$ is the codeword of that message, and $c\in RS[m,2n-1]$.
:::
