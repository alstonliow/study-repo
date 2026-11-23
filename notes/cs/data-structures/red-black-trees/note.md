---
title: "Red-Black Trees"
sources: [res-clrs-red-black-trees]
requires: [cs/data-structures/two-three-trees]
status: draft
---

<!-- Added 2026-11-23 from CLRS (3rd edition), Chapter 13, in our own wording; proofs written out in steps. The example trees are our own. -->

AVL trees keep a node's two subtrees within height $1$ of each other. Red-black trees use a looser rule: one bit per node, a colour, which keeps the height below $2\log(n+1)$. An update repairs the colours along one path to the root and needs at most three rotations. Rotations (@def-rotation) and the binary search tree operations (@sec-cs-data-structures-binary-trees) are as before.

## Colours and black-height

It is convenient to treat every empty subtree as a leaf of its own, a *nil leaf* that holds no key. The nodes holding keys are then the *internal* nodes, and every internal node has exactly two children.

::: {#def-red-black-tree .definition name="Red-black tree"}

A *red-black tree* is a binary search tree whose internal nodes are each coloured *red* or *black*, with nil leaves counted as black, such that:

1. the root is black;
2. every red node has two black children;
3. for every node $x$, all paths from $x$ down to a nil leaf contain the same number of black nodes.

The *black-height* $\operatorname{bh}(x)$ is this number of black nodes, counting the nil leaf but not $x$ itself.

:::

::: {#lem-red-black-subtree-size .lemma name="Black-height bounds the size"}

The subtree of a node $x$ in a red-black tree has at least $2^{\operatorname{bh}(x)}-1$ internal nodes.

:::

::: {.proof}

By induction on the height of $x$.

1. If $x$ is a nil leaf, $\operatorname{bh}(x)=0$ and the subtree has $0=2^0-1$ internal nodes.

2. Otherwise $x$ has two children. A child $y$ has black-height $\operatorname{bh}(x)$ if it is red and $\operatorname{bh}(x)-1$ if it is black, so at least $\operatorname{bh}(x)-1$.

3. By induction each child's subtree has at least $2^{\operatorname{bh}(x)-1}-1$ internal nodes. Adding $x$ gives at least $2\bigl(2^{\operatorname{bh}(x)-1}-1\bigr)+1=2^{\operatorname{bh}(x)}-1$.

:::

::: {#thm-red-black-height .theorem name="Red-black trees are shallow"}

A red-black tree with $n$ internal nodes has height at most $2\log(n+1)$.

:::

::: {.proof}

1. Let $h$ be the height and $r$ the root. On a longest path from $r$ to a nil leaf, no two red nodes are adjacent (rule 2) and the leaf is black, so at least half of the $h$ nodes below $r$ are black. Hence $\operatorname{bh}(r)\ge h/2$.

2. By @lem-red-black-subtree-size, $n\ge2^{h/2}-1$, so $h\le2\log(n+1)$.

:::

::: {#fig-red-black-trees-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[rb/.style={small vertex, fill=ink, text=white, draw=ink}, rr/.style={small vertex, fill=accentLight, draw=accent}, nil/.style={dot}]
\node[rb] (n20) at (2.4,0) {$20$};
\node[rr] (n10) at (1.0,-0.9) {$10$};
\node[rb] (n30) at (3.8,-0.9) {$30$};
\node[rb] (n5) at (0.4,-1.8) {$5$};
\node[rb] (n15) at (1.6,-1.8) {$15$};
\node[rr] (n25) at (3.2,-1.8) {$25$};
\node[rr] (n40) at (4.4,-1.8) {$40$};
\draw (n20)--(n10) (n20)--(n30) (n10)--(n5) (n10)--(n15) (n30)--(n25) (n30)--(n40);
\foreach \p/\x in {n5/0.4, n15/1.6, n25/3.2, n40/4.4} {
  \node[nil] (l\p) at (\x-0.25,-2.55) {}; \node[nil] (r\p) at (\x+0.25,-2.55) {};
  \draw[faint] (\p)--(l\p) (\p)--(r\p);
}
\node[lab,tick] at (2.4,0.42) {$\operatorname{bh}=2$};
\node[lab,tick] at (0.45,-0.75) {$2$};
\node[lab,tick] at (4.35,-0.75) {$1$};
\node[lab] at (2.4,-3.05) {the tree, with its nil leaves as dots};
\begin{scope}[xshift=6.6cm]
\node[box] (r) at (2.0,-0.45) {$10\;\;20$};
\node[box] (a) at (0.4,-1.8) {$5$};
\node[box] (b) at (1.7,-1.8) {$15$};
\node[box] (c) at (3.5,-1.8) {$25\;\;30\;\;40$};
\draw (r)--(a) (r)--(b) (r)--(c);
\node[lab] at (2.0,-3.05) {the same tree as a 2-3-4 tree};
\end{scope}
\end{tikzpicture}
\end{center}
```

Left: a red-black tree; red nodes are light, black nodes dark. Every path from the root to a nil leaf meets two black internal nodes and one nil leaf, so the root has black-height $2$. Right: merging every black node with its red children gives nodes with one to three keys and all leaves at one depth.

:::

::: {#rmk-red-black-trees-1 .remark name="Red-black trees are 2-3-4 trees"}

Merge every black node with its red children (rule 2 says they have no red children of their own). The merged nodes hold one, two or three keys, and by rule 3 every nil leaf lies at the same number of merged levels below the root. So a red-black tree is a binary encoding of a B-tree with $B=2$ (@def-b-tree), also called a 2-3-4 tree, as in @fig-red-black-trees-1. Red nodes are the "glue" inside a big node; the fix-up cases below are splits and merges of big nodes, written as recolourings and rotations.

:::

## Insertion

Insert the new key as in a binary search tree, at a nil leaf, and colour the new node $z$ red. Rule 3 still holds, since no black node was added. Rule 2 fails if the parent of $z$ is red, and rule 1 fails if $z$ is the root. The fix-up below moves the violation up the tree.

::: {#prp-red-black-insert-fixup .proposition name="Insertion fix-up"}

Suppose the tree satisfies all three rules except that the red node $z$ may have a red parent $p$ (and the root may be red). Assume $p$ is a left child of its parent $g$; the other case is the mirror image. Let $u$ be the other child of $g$, the *uncle* of $z$.

1. *Uncle red.* Colour $p$ and $u$ black and $g$ red, and continue with $z\gets g$.
2. *Uncle black, $z$ a right child.* Rotate left at $p$ and set $z\gets p$; this is now case 3.
3. *Uncle black, $z$ a left child.* Colour $p$ black and $g$ red, rotate right at $g$, and stop.

When the loop ends, colour the root black. The result is a red-black tree. The loop runs $O(\log n)$ times and makes at most two rotations in total.

:::

::: {.proof}

1. *$g$ exists and is black.* The parent $p$ is red, so it is not the root (the root is black except possibly at the very end), so $g$ exists; $g$ is black because rule 2 holds everywhere except at the edge $z$–$p$.

2. *Case 1.* The black node $g$ with red children $p,u$ becomes a red node with black children. Every path through $g$ still meets the same number of black nodes, so rule 3 holds. The only possible violation is now between $g$ and its parent, which is the same situation two levels higher.

3. *Case 2.* Both $z$ and $p$ are red, so the rotation at $p$ moves no black node from one path to another, and rule 3 holds. The red-red edge is now between the old $p$ (a left child) and the old $z$ (its parent): case 3.

4. *Case 3.* Before the rotation, $g$ is black with red left child $p$, whose left child $z$ is red; the uncle $u$ and the right subtree of $p$ are black-rooted. After the rotation, $p$ is black and sits where $g$ was, with children $z$ (red) and $g$ (red), and the children of $z$ and $g$ are black-rooted. Each subtree hangs below exactly one black node from $p$ down, as it did below $g$ before, so rule 3 holds, and no red node has a red child. The new top $p$ is black, so nothing above can break.

5. *Termination and cost.* Case 1 moves $z$ up two levels, so it happens $O(\log n)$ times by @thm-red-black-height. Cases 2 and 3 happen at most once, at the end, with at most two rotations. Colouring the root black adds one to every black-height and cannot break any rule.

:::

```{=latex}
\begin{algorithm}
\caption{Red-black insert}
\begin{algorithmic}
\INPUT red-black tree $T$; a key $k$ not in $T$
\STATE insert $k$ as in a binary search tree, in a new red node $z$
\WHILE{$z$ is not the root and $z.\mathrm{parent}$ is red}
    \STATE $p\gets z.\mathrm{parent}$; $g\gets p.\mathrm{parent}$; $u\gets$ the other child of $g$
    \IF{$u$ is red}
        \STATE colour $p$ and $u$ black, $g$ red; $z\gets g$ \COMMENT{case 1}
    \ELSE
        \IF{$z$ and $p$ are on opposite sides (one a left child, the other a right child)}
            \STATE rotate at $p$ to bring $z$ up; swap the names $z,p$ \COMMENT{case 2}
        \ENDIF
        \STATE colour $p$ black, $g$ red; rotate at $g$ to bring $p$ up \COMMENT{case 3}
    \ENDIF
\ENDWHILE
\STATE colour the root black
\end{algorithmic}
\end{algorithm}
```

::: {#fig-red-black-trees-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[rb/.style={small vertex, fill=ink, text=white, draw=ink}, rr/.style={small vertex, fill=accentLight, draw=accent}, st/.style={lab,tick}]
\node[rb] (g) at (1.0,0) {$g$};
\node[rr] (p) at (0.3,-0.8) {$p$};
\node[rr] (u) at (1.7,-0.8) {$u$};
\node[rr] (z) at (-0.2,-1.6) {$z$};
\draw (g)--(p) (g)--(u) (p)--(z);
\draw[emph,->] (2.2,-0.8) -- (2.9,-0.8);
\node[rr] (g2) at (4.0,0) {$g$};
\node[rb] (p2) at (3.3,-0.8) {$p$};
\node[rb] (u2) at (4.7,-0.8) {$u$};
\node[rr] (z2) at (2.8,-1.6) {$z$};
\draw (g2)--(p2) (g2)--(u2) (p2)--(z2);
\node[lab] at (2.0,-2.3) {case 1: recolour, move up};
\begin{scope}[xshift=6.4cm]
\node[rb] (G) at (1.2,0) {$g$};
\node[rr] (P) at (0.5,-0.8) {$p$};
\node[rb] (U) at (1.9,-0.8) {$u$};
\node[rr] (Z) at (1.0,-1.6) {$z$};
\draw (G)--(P) (G)--(U) (P)--(Z);
\draw[emph,->] (2.4,-0.8) -- (3.4,-0.8);
\node[st] at (2.9,-0.5) {left at $p$};
\node[rb] (G2) at (4.6,0) {$g$};
\node[rr] (Z2) at (3.9,-0.8) {$z$};
\node[rb] (U2) at (5.3,-0.8) {$u$};
\node[rr] (P2) at (3.4,-1.6) {$p$};
\draw (G2)--(Z2) (G2)--(U2) (Z2)--(P2);
\draw[emph,->] (5.8,-0.8) -- (6.8,-0.8);
\node[st] at (6.3,-0.5) {right at $g$};
\node[rb] (Z3) at (7.8,-0.3) {$z$};
\node[rr] (P3) at (7.2,-1.1) {$p$};
\node[rr] (G3) at (8.4,-1.1) {$g$};
\node[rb] (U3) at (8.9,-1.9) {$u$};
\draw (Z3)--(P3) (Z3)--(G3) (G3)--(U3);
\node[lab] at (4.6,-2.3) {cases 2 and 3: at most two rotations, then stop};
\end{scope}
\end{tikzpicture}
\end{center}
```

The insertion cases, with $z$ the new red node (subtrees below are omitted; each is black-rooted). Case 1 pushes the blackness of $g$ down to its children and continues at $g$. Case 2 turns a "zig-zag" into case 3, and case 3 ends with one rotation; on the right, the names $z$ and $p$ have been swapped by case 2, so the node on top is the original $z$.

:::

## Deletion

Delete as in a binary search tree: if the node holding the key has two internal children, swap its item with its successor's item (and keep its colour), so that the node actually removed, $y$, has at most one internal child $x$, which takes its place ($x$ may be a nil leaf). If $y$ was red, all rules still hold. If $y$ was black, every path through $x$ has lost a black node; we say $x$ carries an *extra black*. If $x$ is red, colouring it black finishes. Otherwise $x$ is "doubly black", and the fix-up pushes the extra black up or uses it up.

::: {#prp-red-black-delete-fixup .proposition name="Deletion fix-up"}

Let $x$ be a black node carrying an extra black, not the root, and a left child (the right case is the mirror image). Let $w$ be its sibling and $p$ its parent; $w$ is internal, since paths through $w$ must meet at least two black nodes, counting the extra black of $x$.

1. *$w$ red.* Colour $w$ black and $p$ red, rotate left at $p$. The new sibling of $x$ is black: go to case 2, 3 or 4.
2. *$w$ black with two black children.* Colour $w$ red and move the extra black to $p$: $x\gets p$. If $p$ was red, colour it black and stop.
3. *$w$ black, left child red, right child black.* Swap the colours of $w$ and its left child, rotate right at $w$. The new sibling is black with a red right child: case 4.
4. *$w$ black, right child red.* Give $w$ the colour of $p$, colour $p$ and the right child of $w$ black, rotate left at $p$, and stop.

If $x$ reaches the root, the extra black is dropped. The fix-up runs $O(\log n)$ times and makes at most three rotations in total.

:::

::: {.proof}

1. *Case 1.* The rotation and the colour swap of $w$ and $p$ keep the number of black nodes on every path. Afterwards $x$ has a new sibling, a former child of $w$, which was black because $w$ was red. The extra black stays at $x$, so this only changes which case applies.

2. *Case 2.* Removing one black from $x$ and from $w$ (making $w$ red) lowers the black count on all paths through $p$ by one, and putting the extra black on $p$ restores it. If $p$ was red it absorbs the extra black by turning black; otherwise the problem has moved up one level.

3. *Case 3.* The rotation at $w$ with the colour swap keeps every black count, and gives $x$ a black sibling whose right child (the old $w$) is red.

4. *Case 4.* After the rotation, $w$ sits where $p$ was, with $p$'s old colour, so the paths entering the subtree see the same top colour. The paths through $x$ gain the black node $p$ above them, which uses up the extra black. The paths through the old right child of $w$ lose the black $w$ but gain it back, since that child turns from red to black. The paths through the old left child of $w$ pass through $p$ (now black) instead of $w$ (black), so their count is unchanged. So rule 3 holds and no extra black remains.

5. *Termination and cost.* Only case 2 continues, moving $x$ up one level, so there are $O(\log n)$ iterations. After case 1 the parent $p$ is red, so a following case 2 stops at once, and cases 3 and 4 stop anyway. So at most one case 1, one case 3 and one case 4 happen: at most three rotations.

:::

::: {#fig-red-black-trees-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[rb/.style={small vertex, fill=ink, text=white, draw=ink}, rr/.style={small vertex, fill=accentLight, draw=accent}, any/.style={small vertex, fill=primaryLight, draw=primary}, xx/.style={small vertex, fill=ink, text=white, draw=accent, double=accent, double distance=1pt}, st/.style={lab,tick}]
\node[any] (p) at (0.9,0) {$p$};
\node[xx] (x) at (0.3,-0.8) {$x$};
\node[rb] (w) at (1.5,-0.8) {$w$};
\node[any] (wl) at (1.0,-1.6) {$a$};
\node[rr] (wr) at (2.0,-1.6) {$b$};
\draw (p)--(x) (p)--(w) (w)--(wl) (w)--(wr);
\draw[emph,->] (2.4,-0.8) -- (3.2,-0.8);
\node[st] at (2.8,-0.5) {left at $p$};
\node[any] (w2) at (4.6,0) {$w$};
\node[rb] (p2) at (4.0,-0.8) {$p$};
\node[rb] (wr2) at (5.2,-0.8) {$b$};
\node[rb] (x2) at (3.5,-1.6) {$x$};
\node[any] (wl2) at (4.5,-1.6) {$a$};
\draw (w2)--(p2) (w2)--(wr2) (p2)--(x2) (p2)--(wl2);
\node[lab] at (2.8,-2.3) {case 4: the extra black on $x$ is used up};
\end{tikzpicture}
\end{center}
```

Case 4 of the deletion fix-up. The doubly black node $x$ is drawn with a double ring; $p$, $w$'s new colour and $a$ have any colour (drawn mid-blue). After one left rotation at $p$ and three recolourings, every path keeps its black count and $x$ is an ordinary black node.

:::

::: {#thm-red-black-operations .theorem name="Red-black trees as sets"}

A red-black tree supports `find`, `insert`, `delete`, `find_min`, `find_max`, `find_prev` and `find_next` in $O(\log n)$ time. Each `insert` makes at most two rotations and each `delete` at most three.

:::

::: {.proof}

The search and the binary-search-tree part of each update take $O(h)$ time, and the fix-ups take $O(h)$ time with the stated rotations (@prp-red-black-insert-fixup, @prp-red-black-delete-fixup). By @thm-red-black-height, $h=O(\log n)$.

:::

AVL trees are slightly shallower (height at most about $1.44\log n$ instead of $2\log n$), so searches are a little faster. Red-black trees make $O(1)$ rotations per update, against up to $O(\log n)$ for AVL deletion, and need only one bit per node, which is why many standard library maps use them. Both can be augmented with subtree properties as in @def-subtree-augmentation.
