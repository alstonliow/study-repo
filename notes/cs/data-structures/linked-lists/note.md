---
title: "Linked Lists"
sources: [mit6006-2, mit6006r-2]
requires: [cs/data-structures/interfaces]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 2 and Recitation 2, in our own wording; proofs written out in steps. Split from cs/data-structures/linked-lists-and-dynamic-arrays on 2026-11-25 (one data structure per note, SPEC §8.6). -->

A pointer-based implementation of the sequence interface (@def-sequence-interface).

::: {#def-linked-list .definition name="Linked list"}

A *(singly) linked list* stores each item in a *node* with two fields, `item` and `next`, the address of the next node (or none for the last node). The list keeps the address of the first node, its *head*. A *doubly linked list* also gives each node a `prev` field and keeps the address of the last node, its *tail*.

:::

::: {#fig-linked-lists-and-dynamic-arrays-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab] (ha) at (-1.5,1.2) {head};
\node[box] (na0) at (0.0,1.2) {$9$};
\draw[->] (ha) -- (na0);
\node[box] (na1) at (1.7,1.2) {$4$};
\draw[->] (na0) -- (na1);
\node[box] (na2) at (3.4,1.2) {$7$};
\draw[->] (na1) -- (na2);
\node[lab] (za) at (4.70,1.2) {none};
\draw[->] (na2) -- (za);
\node[lab] (hb) at (-1.5,0) {head};
\node[hl box] (nb0) at (0.0,0) {$2$};
\draw[->] (hb) -- (nb0);
\node[box] (nb1) at (1.7,0) {$9$};
\draw[->] (nb0) -- (nb1);
\node[box] (nb2) at (3.4,0) {$4$};
\draw[->] (nb1) -- (nb2);
\node[box] (nb3) at (5.1,0) {$7$};
\draw[->] (nb2) -- (nb3);
\node[lab] (zb) at (6.40,0) {none};
\draw[->] (nb3) -- (zb);
\node[lab, anchor=west] at (7.0,1.2) {before};
\node[lab, anchor=west] at (7.0,0) {after \texttt{insert\_first(2)}};
\end{tikzpicture}
\end{center}
```

Inserting at the front of a linked list: the new node points to the old head and becomes the head. Only two pointers change, whatever the length.

:::

Changing a few addresses changes the list, so `insert_first` and `delete_first` take $O(1)$ time: the new node points to the old head and becomes the head. But reaching item $i$ means following $i$ links, so `get_at(i)` and `set_at(i, x)` take $\Theta(i)$ time in the worst case.

```{=latex}
\begin{algorithm}
\caption{Linked list insert\_first and delete\_first}
\begin{algorithmic}
\STATE \textbf{insert\_first}$(x)$:
\STATE $N\gets$ new node; $N.\mathrm{item}\gets x$; $N.\mathrm{next}\gets\mathrm{head}$; $\mathrm{head}\gets N$
\STATE \textbf{delete\_first}$()$:
\STATE $x\gets\mathrm{head}.\mathrm{item}$; $\mathrm{head}\gets\mathrm{head}.\mathrm{next}$
\RETURN $x$
\end{algorithmic}
\end{algorithm}
```
