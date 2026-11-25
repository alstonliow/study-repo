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
