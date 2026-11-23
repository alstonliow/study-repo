<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-1-q53" status="draft"}
1. Suppose $\mathit{ADD}$ is regular, with pumping length $p$.

2. Take $s=1^p{=}1^p{+}0$. It is in $\mathit{ADD}$, since $y=1^p$, $z=0$ and $x=y+z$, and $|s|\ge p$.

3. Write $s=uvw$ with $|uv|\le p$ and $|v|\ge1$. Then $v$ lies inside the first block $1^p$, so $v=1^j$ with $j\ge1$.

4. Pumping up gives $uv^2w=1^{p+j}{=}1^p{+}0$. Here $x=2^{p+j}-1\ne2^p-1=y+z$, so the string is not in $\mathit{ADD}$. This contradicts the pumping lemma, so $\mathit{ADD}$ is not regular.
:::
