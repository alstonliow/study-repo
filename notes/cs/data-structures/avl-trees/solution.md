<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006s20-4-q1" status="draft"}
(a) Heights (empty subtree $-1$): $28,3,49,88$ have height $0$; $35,64,86$ height $1$; $37,84$ height $2$; $16$ height $3$; $47$ height $4$. Skew = height(right) $-$ height(left):

- $16$: $2-0=2$, not height-balanced;
- $37$: $-1-1=-2$, not height-balanced.

All other skews are in $\{-1,0,1\}$ (for example $47$: $2-3=-1$).

(b) We write a tree as *node(left, right)*, omitting empty children.

1. `insert(2)`: $2<47,16,3$, so $2$ becomes the left child of $3$: 47(16(3(2), 37(35(28))), 84(64(49), 86(·, 88))).
2. `delete(49)`: a leaf, removed: 47(16(3(2), 37(35(28))), 84(64, 86(·, 88))).
3. `delete(35)`: it has a left child, so swap with its predecessor $28$ (a leaf) and remove the leaf: 47(16(3(2), 37(28)), 84(64, 86(·, 88))).
4. `insert(85)`: $85>84$, $85<86$, so $85$ becomes the left child of $86$: 47(16(3(2), 37(28)), 84(64, 86(85, 88))).
5. `delete(84)`: its predecessor is $64$ (a leaf now); swap and remove the leaf: 47(16(3(2), 37(28)), 64(·, 86(85, 88))).

(c) In the original tree:

- *Rotate $16$ left:* $37$ takes $16$'s place, with left child 16(3, 35(28)) and no right child. Not height-balanced: $37$ now has skew $-1-2=-3$.
- *Rotate $16$ right:* $3$ takes its place with right child 16(·, 37(35(28))). Not height-balanced ($3$ has skew $3-(-1)=4$ and $16$ has skew $2-(-1)=3$).
- *Rotate $37$ right:* $35$ takes its place with children $28$ and $37$. Now $35$ has skew $0$, $16$ has skew $1-0=1$, and $47$ has skew $2-2=0$: the whole tree *is* height-balanced.
- *Rotate $37$ left:* not possible, $37$ has no right child.
:::

::: {.solution for="prob-mit6006s20-4-q5" status="draft"}
Use a sequence binary tree whose traversal order is $M_0,\dots,M_{n-1}$, built balanced (middle element at the root, @sec-cs-data-structures-binary-trees), and augment every node $X$ with $P(X)$, the ordered product of the matrices in its subtree in traversal order:
$$P(X)=P(X.\mathrm{left})\cdot X.\mathrm{matrix}\cdot P(X.\mathrm{right}),$$
with empty subtrees contributing the identity. This is computed in $O(1)$ from the children (two multiplications), and the order of the factors respects non-commutativity because the traversal order of $X$'s subtree is left subtree, $X$, right subtree. Also keep an array $N$ with $N[k]$ = the node holding $M_k$.

- `initialize(M)`: build the tree in $O(n)$ and compute $P$ bottom up, $O(1)$ per node: $O(n)$ worst case.
- `update_joint(k, M)`: set `N[k].matrix = M` and recompute $P$ on the path from `N[k]` to the root, $O(1)$ per node. The tree never changes shape, so its height stays $O(\log n)$: $O(\log n)$ worst case.
- `full_transformation()`: return $P(\text{root})$, $O(1)$.
:::

::: {.solution for="prob-mit6006s20-4-q6" status="draft"}
(a) Since $t\ne0$, the slice contains some topping. Let $x_i$ be the largest topping $x$-coordinate that is $\le x'$, and $y_j$ the largest topping $y$-coordinate that is $\le y'$ (both exist because of that topping). No topping has $x$-coordinate in $(x_i,x']$ or $y$-coordinate in $(y_j,y']$, so a topping satisfies $x\le x'$ and $y\le y'$ exactly when it satisfies $x\le x_i$ and $y\le y_j$. The two slices contain the same toppings, so they have the same tastiness.

(b) Augment each node $X$ (@def-subtree-augmentation) with
$$X.\mathrm{sum}=\sum_{\text{items in the subtree}}\mathrm{val},\qquad(X.\mathrm{best},X.\mathrm{arg}),$$
the largest prefix sum *within the subtree* (over prefixes, in key order, that end at a key of the subtree) and a key attaining it. With $L$, $R$ the children (an empty child has sum $0$ and best $-\infty$),
$$X.\mathrm{best}=\max\{L.\mathrm{best},\ L.\mathrm{sum}+X.\mathrm{val},\ L.\mathrm{sum}+X.\mathrm{val}+R.\mathrm{best}\},$$
with `arg` taken from the winning term ($L.\mathrm{arg}$, $X.\mathrm{key}$ or $R.\mathrm{arg}$). The three terms are the prefixes ending in the left subtree, at $X$, and in the right subtree. Each value is computed in $O(1)$ from the children, so all AVL operations keep their running times (@sec-cs-data-structures-avl-trees), and `max_prefix()` returns $(\mathrm{root.arg},\mathrm{root.best})$ in $O(1)$: the prefix sums of the subtree of the root are exactly $\mathrm{prefix}(k)$.

(c) By (a), it suffices to try points $(x_i,y_j)$. Sort the toppings by $y$ and insert them one at a time into the tree of (b), as items with key $x_i$ and value $t_i$. After inserting the topping with $y$-coordinate $y_j$, the tree holds exactly the toppings with $y\le y_j$, and `max_prefix()` gives the best $x'$ for $y'=y_j$, together with its tastiness. Keep the best triple seen. Sorting takes $O(n\log n)$, and $n$ insertions and queries take $O(\log n)$ and $O(1)$ each: $O(n\log n)$ worst case.

(d) The following implementation uses a tree of fixed shape over all $x$-coordinates (a balanced tree in which every coordinate is present from the start with value $0$, and "inserting" a topping adds its tastiness), with the augmentation of (b) stored in an array. It has the same $O(\log n)$ update and $O(1)$ query.

```python
def tastiest_slice(toppings):
    # Static balanced tree over the sorted distinct x-coordinates; a node
    # stores (sum, best prefix sum, key reaching it) of its subtree, so the
    # root answers max_prefix in O(1) and an update touches O(log n) nodes.
    xs = sorted({x for x, y, t in toppings})
    m = len(xs)
    size = 1
    while size < m: size *= 2
    NEG = float('-inf')
    sm = [0] * (2 * size)
    best = [NEG] * (2 * size)
    arg = [None] * (2 * size)
    for i, x in enumerate(xs):           # leaves: every key present, value 0
        best[size + i], arg[size + i] = 0, x
    def pull(v):
        l, r = 2 * v, 2 * v + 1
        sm[v] = sm[l] + sm[r]
        cand_r = sm[l] + best[r] if best[r] != NEG else NEG
        if best[l] >= cand_r: best[v], arg[v] = best[l], arg[l]
        else: best[v], arg[v] = cand_r, arg[r]
    for v in range(size - 1, 0, -1): pull(v)
    pos = {x: i for i, x in enumerate(xs)}
    X, Y, T = 0, 0, NEG
    for x, y, t in sorted(toppings, key=lambda p: p[1]):   # sweep y upwards
        v = size + pos[x]
        sm[v] += t; best[v] = sm[v]
        v //= 2
        while v: pull(v); v //= 2
        if best[1] > T: X, Y, T = arg[1], y, best[1]
    return (X, Y, T)
```

It was checked against brute force over all points $(x_i,y_j)$ on random inputs.
:::

::: {.solution for="prob-mit6006r-7-q3" status="draft"}
Store the bits in a Sequence AVL tree (traversal order = sequence order), augmented at every node with `size` (number of nodes in its subtree, already used by sequence trees) and `ones` (number of $1$ bits in its subtree). Both are computed in $O(1)$ from the children, so they are maintained through rotations at no extra asymptotic cost.

- `flip(i)`: find the node at index $i$ with `subtree_at(i)` in $O(\log n)$, flip its bit, then walk up to the root recomputing `ones` at each ancestor: $O(\log n)$.
- `count_ones_upto(i)`: walk down from the root as in `subtree_at(i)`, keeping a running total. Let $L$ be the size of the left subtree of the current node. If $i<L$, go left. Otherwise add the left child's `ones` plus the current bit; if $i=L$ stop, else go right with $i\leftarrow i-L-1$. One step per level, so $O(\log n)$.

(The sequence never changes length, so a static balanced tree built once in $O(n)$, or an array-based segment tree, works as well.)
:::
