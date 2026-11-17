::: {.problem #prob-mit6006s20-2-q2 origin="external" source="mit6006s20-2-q2"}
**Sorting Sorts**

For each of the following scenarios, choose a sorting algorithm (from either selection sort, insertion sort, or merge sort) that best applies, and justify your choice. **Don't forget this! Your justification will be worth more points than your choice.** Each sort may be used more than once. If you find that multiple sorts could be appropriate for a scenario, identify their pros and cons, and choose the one that best suits the application. State and justify any assumptions you make. "Best" should be evaluated by asymptotic running time.

(a) Suppose you are given a data structure `D` maintaining an extrinsic order on $n$ items, supporting two standard sequence operations: `D.get_at(i)` in worst-case $\Theta(1)$ time and `D.set_at(i, x)` in worst-case $\Theta(n\log n)$ time. Choose an algorithm to best sort the items in `D` **in-place**.

(b) Suppose you have a static array $A$ containing pointers to $n$ comparable objects, pairs of which take $\Theta(\log n)$ time to compare. Choose an algorithm to best sort the pointers in $A$ so that the pointed-to objects appear in non-decreasing order.

(c) Suppose you have a **sorted array** $A$ containing $n$ integers, each of which fits into a single machine word. Now suppose someone performs some $\log\log n$ swaps between pairs of adjacent items in $A$ so that $A$ is no longer sorted. Choose an algorithm to best re-sort the integers in $A$.
:::

::: {.problem #prob-mit6006s20-2-q3 origin="external" source="mit6006s20-2-q3"}
**Friend Finder**

Jean-Locutus Πcard is searching for his incapacitated friend, Datum, on Gravity Island. The island is a narrow strip running north–south for $n$ kilometers, and Πcard needs to pinpoint Datum's location to the nearest integer kilometer so that he is within visual range. Fortunately, Πcard has a tracking device, which will always tell him whether Datum is north or south of his current position (but sadly, not how far away he is), as well as a teleportation device, which allows him to jump to specified coordinates on the island in constant time.

Unfortunately, Gravity Island is rapidly sinking. The topography of the island is such that the north and south ends will submerge into the water first, with the center of the island submerging last. Therefore, it is more important that Πcard find Datum quickly if he is close to either end of the island, lest he short-circuit. Describe an algorithm so that, if Datum is $k$ kilometers from the nearest end of the island (i.e., he is either at the $k$th or the $(n-k)$th kilometer, measured from north to south), then Πcard can find him after visiting $O(\log k)$ locations with his teleportation and tracking devices.
:::

::: {.problem #prob-mit6006s20-2-q4 origin="external" source="mit6006s20-2-q4"}
**MixBookTube.tv Chat**

MixBookTube.tv is a service that lets viewers chat while watching someone play video games. Each viewer is identified by a known unique integer ID. The chat consists of a linear stream of messages, each written by a viewer. Viewers can see the most recent $k$ chat messages, where $k$ depends on the size of their screen. Sometimes a viewer misbehaves in chat and gets banned by the streamer. When a viewer gets banned, not only can they not post new messages in chat, but all of their previously sent messages are removed from the chat.

Describe a database to efficiently implement MixBookTube.tv's chat, supporting the following operations, where $n$ is the number of all viewers (banned or not) in the database at the time of the operation (all operations should be worst-case):

| operation | specification |
|---|---|
| `build(V)` | Initialize a new chat room with the $n=|V|$ viewers in $V$ in $O(n\log n)$ time. |
| `send(v, m)` | Send message $m$ to the chat from viewer $v$ (unless banned) in $O(\log n)$ time. |
| `recent(k)` | Return the $k$ most recent not-deleted messages (or all if $<k$) in $O(k)$ time. |
| `ban(v)` | Ban viewer $v$ and delete all their messages in $O(n_v+\log n)$ time, where $n_v$ is the number of messages that viewer $v$ sent before being banned. |

(Footnote: As mentioned in lecture, unless we parameterize the size of numbers in our input, you should assume that input integers each fit within a machine word, so pairs of them may be compared in constant time.)
:::

::: {.problem #prob-mit6006s20-2-q5 origin="external" source="mit6006s20-2-q5"}
**Beaver Bookings**

Tim the Beaver is arranging Tim Talks, a lecture series that allows anyone in the MIT community to schedule a time to talk publicly. A talk request is a tuple $(s,t)$, where $s$ and $t$ are the starting and ending times of the talk respectively with $s<t$ (times are positive integers representing the number of time units since some fixed time).

Tim must make room reservations to hold the talks. A room booking is a triple $(k,s,t)$, corresponding to reserving $k>0$ rooms between the times $s$ and $t$ where $s<t$. Two room bookings $(k_1,s_1,t_1)$ and $(k_2,s_2,t_2)$ are disjoint if either $t_1\le s_2$ or $t_2\le s_1$, and adjacent if either $t_1=s_2$ or $t_2=s_1$. A booking schedule is an ordered tuple of room bookings where: every pair of room bookings from the schedule are disjoint, room bookings appear with increasing starting time in the sequence, and every adjacent pair of room bookings reserves a different number of rooms.

Given a set $R$ of talk requests, there is a unique booking schedule $B$ that satisfies the requests, i.e., the schedule books exactly enough rooms to host all the talks. For example, given a set of talk requests $R=\{(2,3),(4,10),(2,8),(6,9),(0,1),(1,12),(13,14)\}$ pictured to the right, the satisfying room booking is:
$$B=((1,0,2),(3,2,3),(2,3,4),(3,4,6),(4,6,8),(3,8,9),(2,9,10),(1,10,12),(1,13,14)).$$

(a) Given two booking schedules $B_1$ and $B_2$, where $n=|B_1|+|B_2|$ and $B_1$ and $B_2$ are the respective booking schedules of two sets of talk requests $R_1$ and $R_2$, describe an $O(n)$-time algorithm to compute a booking schedule $B$ for $R=R_1\cup R_2$.

(b) Given a set $R$ of $n$ talk requests, describe an $O(n\log n)$-time algorithm to return the booking schedule that satisfies $R$.

(c) Write a Python function `satisfying_booking(R)` that implements your algorithm. You can download a code template containing some test cases from the website.

```python
def satisfying_booking(R):
    '''
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    '''
    B = []
    ##################
    # YOUR CODE HERE #
    ##################
    return tuple(B)
```

*Note (these notes):* The picture of the requests in the original is not reproduced; the set $R$ in the text describes it completely.
:::
