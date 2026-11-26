---
title: "Tries"
sources: []
requires: [cs/data-structures/interfaces]
status: draft
---

<!-- Added 2026-11-26 in our own words (owner decision 2026-11-26: new notes for the LeetCode Hot 100 problems without a fitting note). No single source; TODO: add a source if one is integrated later. The examples and figures are our own. -->

A trie stores a set of strings (@def-set-interface) over an alphabet $\Sigma$ by sharing common prefixes. Its operations cost time proportional to the length of the query string, independent of how many strings are stored.

::: {#def-trie .definition name="Trie"}

A *trie* (prefix tree) for a set $S$ of strings over $\Sigma$ is a rooted tree in which every edge is labelled by a character, the edges from a node to its children have distinct labels, and every node $v$ spells the string $s(v)$ read along the path from the root. Each node carries a flag `end` that is true exactly when $s(v)\in S$. The nodes are exactly the prefixes of strings in $S$, one node per prefix.

:::

The operations walk down from the root, one character at a time:

- `insert(w)`: for each character of $w$, follow the child with that label, creating it if it is missing; then set `end` at the last node.
- `search(w)`: follow the characters of $w$; return false if a child is missing, otherwise return the `end` flag of the last node.
- `startsWith(p)`: as `search`, but return true whenever the walk succeeds, since every node is a prefix of some stored string.

::: {#fig-tries-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[level distance=1.1cm, sibling distance=1.6cm, every node/.style={small vertex}, edge from parent/.style={draw}]
\node (r) {}
  child {node[fill=accentLight] (a) {} 
    child {node[fill=accentLight] (an) {}
      child {node[fill=accentLight] (and) {} edge from parent node[edge label] {$d$}}
      child {node[fill=accentLight] (ant) {} edge from parent node[edge label] {$t$}}
      edge from parent node[edge label] {$n$}}
    edge from parent node[edge label] {$a$}}
  child {node {}
    child {node[fill=accentLight] (be) {} edge from parent node[edge label] {$e$}}
    edge from parent node[edge label] {$b$}};
\end{tikzpicture}
\end{center}
```

The trie of $S=\{a,an,and,ant,be\}$. Highlighted nodes have `end` set. The prefix $an$ is shared by $an$, $and$ and $ant$; the node for $b$ is a prefix only, so `search(b)` is false but `startsWith(b)` is true.

:::

::: {#prp-trie .proposition name="Cost of trie operations"}

With children stored in an array indexed by $\Sigma$, `insert`, `search` and `startsWith` on a string of length $L$ take $O(L)$ time. A trie for $S$ has at most $1+\sum_{w\in S}|w|$ nodes and uses $O(|\Sigma|)$ space per node.

:::

::: {.proof}

1. *Time.* Each operation visits one node per character of its argument and does $O(1)$ work there: one array lookup, and possibly one node creation.

2. *Nodes.* Inserting $w$ creates at most $|w|$ new nodes, one per character, and the root is created once. So the number of nodes is at most $1+\sum_{w\in S}|w|$, and each node holds an array of $|\Sigma|$ child pointers and one flag.

:::

::: {#rmk-tries-1 .remark name="Array or hash table of children"}

An array of children gives worst-case $O(1)$ steps but costs $|\Sigma|$ pointers per node, which is wasteful for large alphabets. A hash table of children uses space proportional to the number of edges, with $O(1)$ expected time per step. A trie also lists the stored strings in lexicographic order by a preorder traversal that visits children in label order.

:::

::: {#fig-tries-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm,y=0.9cm]
\foreach \c [count=\i] in {a,n,t} {
  \node[small vertex, fill=accentLight] (v\i) at (\i*1.6,0) {};
  \node[lab,tick] at (\i*1.6-0.8,0.3) {$\c$};
}
\node[small vertex] (v0) at (0,0) {};
\draw[hl] (v0) -- (v1) -- (v2) -- (v3);
\node[lab,note,anchor=west] at (5.3,0) {3 steps for $ant$, whatever $|S|$ is};
\end{tikzpicture}
\end{center}
```

`search(ant)` follows one edge per character: its cost depends on $|ant|=3$, not on the number of stored strings.

:::
