<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046s15-4-q1" status="draft"}
(a) Keep the queue $Q$ itself (a linked list) and a double-ended queue $D$ of *candidate minima*. Invariant: $D$ lists, in queue order, exactly those elements of $Q$ that are smaller than every element enqueued after them; hence $D$ is strictly increasing from front to back, and its front is the minimum of $Q$.

(b) ENQUEUE$(x)$: append $x$ to $Q$; while $D$ is non-empty and its back is greater than $x$, pop the back of $D$; append $x$ to $D$. DEQUEUE: remove the front $y$ of $Q$; if the front of $D$ is $y$, pop it from $D$; return $y$. FIND-MIN: return the front of $D$.

(c) *Enqueue:* the new $x$ belongs in $D$ (nothing comes after it). An old element $z>x$ stops qualifying, since $x$ comes after it; those are exactly the popped back elements, because $D$ is increasing and so all of them sit at the back. Elements smaller than $x$ still qualify. *Dequeue:* removing the oldest element $y$ changes no other element's status; $y$ is in $D$ iff it is the front of $D$ (as $D$ is in queue order). *Find-min:* the minimum of $Q$ is smaller than everything after it, so it is in $D$, and it is the smallest, so it is the front.

(d) Worst case: ENQUEUE may pop $\Theta(n)$ elements; DEQUEUE and FIND-MIN are $O(1)$. Amortized: each element is appended to $D$ once and popped from $D$ at most once, so $m$ operations do $O(m)$ pops in total (aggregate method, or potential $\Phi=|D|$, @def-potential-method): $O(1)$ amortized per operation.
:::
