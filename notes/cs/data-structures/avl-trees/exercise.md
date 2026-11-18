::: {.problem #prob-mit6006s20-4-q1 origin="external" source="mit6006s20-4-q1"}
**Binary Tree Practice**

(a) The Set Binary Tree $T$ below is not height-balanced but does satisfy the binary search tree property, assuming the key of each integer item is itself. Indicate the keys of all nodes that are not height-balanced and compute their skew.

```text
            47
        /        \
      16          84
     /  \        /  \
    3    37    64    86
        /     /        \
      35    49          88
     /
   28
```

(b) Perform the following insertions and deletions, one after another in sequence on $T$, by adding or removing a leaf while maintaining the binary search tree property (a key may need to be swapped down into a leaf). For this part, do not use rotations to balance the tree. Draw the modified tree after each operation.

```python
T.insert(2)
T.delete(49)
T.delete(35)
T.insert(85)
T.delete(84)
```

(c) For each unbalanced node identified in part (a), draw the two trees that result from rotating the node in the original tree left and right (when possible). For each tree drawn, specify whether it is height-balanced, i.e., all nodes satisfy the AVL property.

*Note (these notes):* The tree, drawn as a picture in the original, is shown here as text; it is determined by the binary search tree property and the keys on each level.
:::

::: {.problem #prob-mit6006s20-4-q5 origin="external" source="mit6006s20-4-q5"}
**Robot Wrangling**

Dr. Squid has built a robotic arm from $n+1$ rigid bars called links, each connected to the one before it with a rotating joint ($n$ joints in total). Following standard practice in robotics, the orientation of each link is specified locally relative to the orientation of the previous link. In mathematical notation, the change in orientation at a joint can be specified using a $4\times4$ transformation matrix. Let $M=(M_0,\dots,M_{n-1})$ be an array of transformation matrices associated with the arm, where matrix $M_k$ is the change in orientation at joint $k$, between links $k$ and $k+1$.

To compute the position of the end effector, Dr. Squid will need the arm's full transformation: the ordered matrix product of the arm's transformation matrices, $\prod_{k=0}^{n-1}M_k=M_0\cdot M_1\cdot\ldots\cdot M_{n-1}$. Assume Dr. Squid has a function `matrix_multiply(M1, M2)` that returns the matrix product $M_1\times M_2$ of any two $4\times4$ transformation matrices in $O(1)$ time. While tinkering with the arm changing one joint at a time, Dr. Squid will need to re-evaluate this matrix product quickly. Describe a database to support the following worst-case operations to accelerate Dr. Squid's workflow:

| operation | specification |
|---|---|
| `initialize(M)` | Initialize from an initial input configuration $M$ in $O(n)$ time. |
| `update_joint(k, M)` | Replace joint $k$'s matrix $M_k$ with matrix $M$ in $O(\log n)$ time. |
| `full_transformation()` | Return the arm's current full transformation in $O(1)$ time. |

(Footnote: Recall, matrix multiplication is not commutative, i.e., $M_1\cdot M_2\ne M_2\cdot M_1$, except in very special circumstances.)
:::

::: {.problem #prob-mit6006s20-4-q6 origin="external" source="mit6006s20-4-q6"}
**$\pi z^2a$ Optimization**

Liza Pover has found a Monominos pizza left over from some big-TEX recruiting event. The pizza is a disc with radius $z$, having $n$ toppings labeled $0,\dots,n-1$. Assume $z$ fits in a single machine word, so integer arithmetic on $O(1)$ such integers can be done in $O(1)$ time. Each topping $i$:

- is located at Cartesian coordinates $(x_i,y_i)$ where $x_i,y_i$ are integers from range $R=\{-z,\dots,z\}$ (you may assume that all coordinates are distinct), and
- has integer tastiness $t_i\in R$ (note, topping tastiness can be negative, e.g., if it's pineapple).

Liza wants to pick a point $(x',y')$ and make a pair of cuts from that point, one going straight down and one going straight left, and take the resulting slice, i.e., the intersection of the pizza with the two half-planes $x\le x'$ and $y\le y'$. The tastiness of this slice is the sum of all $t_i$ such that $x_i\le x'$ and $y_i\le y'$. Liza wants to find a tastiest slice, that is, a slice of maximum tastiness. Assume there exists a slice with positive tastiness.

(a) If point $(x',y')$ results in a slice with tastiness $t\ne0$, show there exists $i,j\in\{0,1,\dots,n-1\}$ such that point $(x_i,y_j)$ results in a slice of equal tastiness $t$ (i.e., a tastiest slice exists resulting from a point that is both vertically and horizontally aligned with toppings).

(b) To make finding a tastiest slice easier, show how to modify a Set AVL Tree so that:

- it stores key–value items, where each item $x$ contains a value $x.\mathrm{val}$ (in addition to its key $x.\mathrm{key}$ on which the Set AVL is ordered);
- it supports a new tree-level operation `max_prefix()` which returns in worst-case $O(1)$ time a pair $(k^*,\mathrm{prefix}(k^*))$, where $k^*$ is any key stored in the tree $T$ that maximizes the prefix sum, $\mathrm{prefix}(k)=\sum\{x.\mathrm{val}\mid x\in T\text{ and }x.\mathrm{key}\le k\}$ (that is, the sum of all values of items whose keys are $\le k$); and
- all other Set AVL Tree operations maintain their running times.

(c) Using the data structure from part (b) as a black box, describe a worst-case $O(n\log n)$-time algorithm to return a triple $(x,y,t)$, where point $(x,y)$ corresponds to a slice of maximum tastiness $t$.

(d) Write a Python function `tastiest_slice(toppings)` that implements your algorithm from part (c), including an implementation of your data structure from part (b).

```python
from Set_AVL_Tree import BST_Node, Set_AVL_Tree

class Key_Val_Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self):
        return "%s,%s" % (self.key, self.val)

class Part_B_Node(BST_Node):
    def subtree_update(A):
        super().subtree_update()
        #########################################
        # ADD ANY NEW SUBTREE AUGMENTATION HERE #
        #########################################

class Part_B_Tree(Set_AVL_Tree):
    def __init__(self):
        super().__init__(Part_B_Node)

    def max_prefix(self):
        '''
        Output: (k, s) | a key k stored in tree whose
                       | prefix sum s is maximum
        '''
        k, s = 0, 0
        ##################
        # YOUR CODE HERE #
        ##################
        return (k, s)

def tastiest_slice(toppings):
    '''
    Input:  toppings | List of integer tuples (x,y,t) representing
                     | a topping at (x,y) with tastiness t
    Output: tastiest | Tuple (X,Y,T) representing a tastiest slice
                     | at (X,Y) with tastiness T
    '''
    B = Part_B_Tree()   # use data structure from part (b)
    X, Y, T = 0, 0, 0
    ##################
    # YOUR CODE HERE #
    ##################
    return (X, Y, T)
```
:::

::: {.problem #prob-mit6006r-7-q3 origin="external" source="mit6006r-7-q3"}
Maintain a sequence of $n$ bits that supports two operations, each in $O(\log n)$ time:

- `flip(i)`: flip the bit at index $i$
- `count_ones_upto(i)`: return the number of bits in the prefix up to index $i$ that are one
:::
