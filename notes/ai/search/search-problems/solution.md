<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs221hw-3-q3" status="draft"}
A suitable state is a pair (current location, set of waypoint tags already satisfied). The future of the search depends on where we are and on which tags are still missing, not on the order in which earlier tags were met.

1. There are $n$ choices for the location.
2. The satisfied tags form a subset of the $k$ waypoint tags: $2^k$ choices.
3. So UCS visits at most
$$n\cdot 2^k$$
states. Some pairs are unreachable (for example a location whose own tags are not in the set), but this is a valid upper bound.
:::
