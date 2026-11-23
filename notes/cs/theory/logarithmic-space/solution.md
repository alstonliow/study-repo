<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-8-q22" status="draft"}
(a)

1. Let $\ell$ be the largest of the three lengths. For $i=0,1,\dots,\ell$, compute bit $i$ (counting from the least significant end, $0$ beyond the length) of $x$, $y$ and $z$. To get bit $i$ of a number, move to the right end of its block and step $i$ cells to the left with a counter.

2. Keep a carry bit $c$ (initially $0$). Check that $z_i=(x_i+y_i+c)\bmod2$, then set $c\gets\lfloor(x_i+y_i+c)/2\rfloor$. Reject on a mismatch. At the end, accept iff $c=0$.

3. Only the counters $i$ and the step counter, $O(\log n)$ bits each, and one carry bit are stored. So $\mathit{ADD}\in\mathrm L$.

(b)

1. *Bit $i$ of $s=x+y$.* Recompute the carry into position $i$ by running the loop of (a) over positions $0,\dots,i-1$. This uses $O(\log n)$ space and nothing needs to be stored between calls.

2. *Length of $s$.* Scan $i$ from $\max(|x|,|y|)$ down to $0$ and let $L-1$ be the first position where bit $i$ of $s$ is $1$.

3. *Palindrome test.* For $i=0,\dots,L-1$, compare bit $i$ of $s$ with bit $L-1-i$, recomputing each bit from scratch. Accept iff all pairs agree.

4. Only a constant number of $O(\log n)$-bit counters are stored, so $\mathit{PAL\text-ADD}\in\mathrm L$.
:::
