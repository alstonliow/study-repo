<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-8-q2" status="draft"}
Every new room number below is finite, so every guest moves a finite distance.

(a) Move the guest in room $n$ to room $n+1$ and put the new guest in room $0$. For $k$ guests, move room $n$ to room $n+k$ and use rooms $0,\dots,k-1$.

(b) Move the guest in room $n$ to room $2n$, and put the passenger in seat $s$ into room $2s+1$. Even and odd rooms are disjoint, and each is used once.

(c) Number the trains $1,2,3,\dots$ and treat the hotel as train $0$, its guest in room $n$ sitting in seat $n$. Send the person in seat $s$ of train $t$ to room $\pi(t,s)=\frac{(t+s)(t+s+1)}2+s$. The pairing function $\pi$ is a bijection $\mathbb N\times\mathbb N\to\mathbb N$ (@thm-pairs-countable), so everyone gets a room and no two people share one.
:::
