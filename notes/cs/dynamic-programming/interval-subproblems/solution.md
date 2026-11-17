<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046s15-1-q1" status="draft"}
(a) A path $a-b-c$ with profits $2,3,2$: greedy takes $b$ (profit $3$) and must drop $a$ and $c$, while $\{a,c\}$ earns $4$.

(b) Root the tree anywhere and solve two subproblems per vertex, bottom up (children before parents):
$$\mathrm{in}(v)=p_v+\sum_{c\text{ child of }v}\mathrm{out}(c),\qquad\mathrm{out}(v)=\sum_{c\text{ child of }v}\max\{\mathrm{in}(c),\mathrm{out}(c)\},$$
the best profit in $v$'s subtree with $v$ used or not used. If $v$ is used its children cannot be; if not, each child's subtree is independent. The answer is $\max\{\mathrm{in}(r),\mathrm{out}(r)\}$, recovered by parent pointers. Each vertex is handled once with work proportional to its number of children: $O(|V|)$.

(c) Repeatedly take a leaf (or an isolated vertex), add it to $U$, and delete it and its neighbour. *Correctness:* let $\ell$ be a leaf with neighbour $q$, and $U^*$ a largest valid set. If $\ell\notin U^*$, then $q\in U^*$ (otherwise $U^*+\ell$ would be larger), and $U^*-q+\ell$ is valid and as large. So some largest set contains $\ell$ and not $q$, and the rest of it is a largest set in the forest without $\ell$ and $q$; induction finishes the proof. Time $O(|V|)$ with a queue of current leaves.

(d) For general graphs this is the maximum-weight independent set problem, which is NP-hard (see @prob-mit6046s15-8-q2), so no polynomial algorithm is expected. Exhaustive search over all $2^{|V|}$ subsets takes $O(2^{|V|}(|V|+|E|))$; branching on a vertex $v$ of degree at least $3$ (either $v\notin U$, or $v\in U$ and its $\ge3$ neighbours are removed), and solving graphs of maximum degree $2$ (paths and cycles) directly by dynamic programming, gives $T(n)\le T(n-1)+T(n-4)+\mathrm{poly}$, about $O(1.38^n)$.
:::

::: {.solution for="prob-mit6046s15-5-q2" status="draft"}
(a) Values are non-negative, so take the $m$ largest. Find the $m$-th largest value $v^*$ by linear-time selection (@thm-median-of-medians), then scan $P$ once, keeping every prize with value above $v^*$ and as many with value exactly $v^*$ as needed to reach $m$, in their original order. $O(n)$ time and space.

(b) Some split point $i$ separates the A-part (chosen among $p_1..p_i$) from the B-part (among $p_{i+1}..p_n$). Let $a(i,j)$ be the largest value of at most $j$ type-A prizes among $p_1..p_i$, and $b(i,j)$ that of at most $j$ type-B prizes among $p_i..p_n$:
$$a(i,j)=\max\{a(i-1,j),\ [p_i\text{ is A}]\,(p_i.value+a(i-1,j-1))\},$$
and symmetrically for $b$, with zero base cases. The answer is $\max_{0\le i\le n,\ 0\le j\le m}\{a(i,j)+b(i+1,m-j)\}$, recovered by parent pointers. $O(nm)$ time and space.

(c) Let $x(i,j)$ be the largest value of a non-decreasing subsequence of at most $j$ prizes that ends with $p_i$: $x(i,j)=p_i.value+\max\bigl(\{0\}\cup\{x(k,j-1):k<i,\ p_k.value\le p_i.value\}\bigr)$ for $j\ge1$, $x(i,0)=-\infty$. The answer is $\max_{i,j\le m}x(i,j)$ (or $0$). There are $nm$ subproblems with $O(n)$ work each: $O(n^2m)$ time, $O(nm)$ space (like @exm-lis).

(d) Let $f(u,j)$ be the largest value of a connected set of at most $j$ prizes in $u$'s subtree that contains $u$ (and $f(\text{nil},j)=0$, meaning "take nothing there"):
$$f(u,j)=u.value+\max_{a+b\le j-1}\{f(u.left,a)+f(u.right,b)\},\qquad f(u,0)=-\infty\text{ for }u\ne\text{nil},$$
where $a=0$ means the left child is not taken (value $0$). The answer is $\max\{0,f(r,m)\}$. There are $nm$ subproblems with $O(m)$ work each: $O(nm^2)$ time, $O(nm)$ space.
:::
