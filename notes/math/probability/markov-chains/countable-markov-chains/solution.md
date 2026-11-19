<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-5-q5" status="draft"}
The dynamics of $Y$ do not depend on $X$, so $E_{i,j}[T]=t(j)$ depends only on $j$, and $X_T=i+R$ where $R$ is the number of moves to the right, whose law depends only on $j$.

(a) First-step analysis (@thm-first-step-hitting-time): $t(0)=0$ and for $j\ge1$
$$t(j)=1+\frac1{j+1}\Bigl(t(j)+\sum_{k=0}^{j-1}t(k)\Bigr),\quad\text{i.e.}\quad j\,t(j)=j+1+\sum_{k=0}^{j-1}t(k).$$
Subtracting the equation for $j-1$ from that for $j\ge2$ gives $j\,t(j)-(j-1)t(j-1)=1+t(j-1)$, so $t(j)=t(j-1)+\frac1j$. With $t(1)=2$, $E_{i,j}[T]=1+H_j=1+\sum_{m=1}^{j}\frac1m$ for $j\ge1$.

(b) Let $G_j(s)=E[e^{sR}]$ from height $j$; $G_0=1$ and, by first-step analysis,
$$(j+1-e^s)\,G_j=\sum_{k=0}^{j-1}G_k=:S_j.$$
Then $S_{j+1}=S_j+G_j=S_j\frac{j+2-e^s}{j+1-e^s}$ and $S_1=1$, which telescopes to $S_j=\frac{j+1-e^s}{2-e^s}$. Hence $G_j(s)=\frac1{2-e^s}$ for every $j\ge1$, the MGF of $P(R=r)=2^{-(r+1)}$, $r=0,1,2,\dots$ (@thm-transform-properties, uniqueness). So from $(i,j)$ with $j\ge1$,
$$P(X_T=i+r)=2^{-(r+1)},\qquad r\ge0,$$
whatever $j$ is; from $(i,0)$, $X_T=i$. (A simulation with $j=1,3,7$ agrees.)
:::

::: {.solution for="prob-eecs126d-7-q1" status="draft"}
(a) $N=\sum_n\mathbf1\{S_n=0\}$, so $E[N]=\sum_nP(S_n=0)=\infty$, and by @thm-recurrence-visits this is equivalent to recurrence.

(b) Returns happen only at even times, and $P(S_{2n}=0)=\binom{2n}{n}4^{-n}\sim\frac{1}{\sqrt{\pi n}}$ by Stirling; $\sum_n\frac1{\sqrt n}=\infty$ (@exm-random-walk-on-integers).

(c) In the rotated coordinates $U=x+y$, $V=x-y$, each step changes $U$ by $\pm1$ and $V$ by $\pm1$, the four sign combinations equally likely: $U$ and $V$ are independent one-dimensional walks. So $P(S_{2n}=0)=\bigl(\binom{2n}n4^{-n}\bigr)^2\sim\frac1{\pi n}$, whose sum diverges.

(d) Counting paths with $i,j,k$ steps in each direction and back,
$$P(S_{2n}=0)=\frac{1}{6^{2n}}\sum_{i+j+k=n}\frac{(2n)!}{(i!j!k!)^2}=\binom{2n}{n}4^{-n}\sum_{i+j+k=n}\Bigl(\frac{n!}{i!j!k!3^n}\Bigr)^2.$$
The terms $\frac{n!}{i!j!k!3^n}$ are a probability distribution (multinomial), so the sum of squares is at most its largest term, which is attained at $i,j,k\approx\frac n3$ and is $O(1/n)$ by Stirling. So $P(S_{2n}=0)=O(n^{-3/2})$, summable, and the walk is transient.

(e) Look at the first three coordinates of the walk in $\mathbb Z^d$. They change only at the steps that move along $e_1,e_2,e_3$ (each step with probability $\frac3d$), and at those steps they move like the walk of (d). Each visit of that three-dimensional walk to the origin lasts a geometric number of steps of mean $\frac d3$, so the expected number of times $n$ with the first three coordinates zero is finite. Returns of $S_n$ to the origin are among those times, so $E[N]<\infty$ and the walk is transient.
:::
