::: {.problem #prob-cs221hw-3-q3 origin="external" source="cs221hw-3-q3"}
Let's introduce an even more powerful feature: unordered waypoints! In Google Maps, you can specify an ordered sequence of waypoints that a path must go through -- for example, going from point A to point X to point Y to point B, where [X, Y] are "waypoints" (such as a gas station or a friend's house).

However, we want to consider the case where the waypoints are *unordered*: {X, Y}, so that both A → X → Y → B and A → Y → X → B are allowed. Moreover, X, Y, and B are each specified by a tag like in Problem 2 (e.g., `amenity=food`).

This is a neat feature if you think about your day-to-day life; you might be on your way home after a long day, but need to stop by the package center, Tresidder to grab a bite of food, and the bookstore to buy some notebooks. Having the ability to get a short, quick path that hits all these stops might be really convenient (rather than searching over the various waypoint orderings yourself).

(a) Implement `WaypointsShortestPathProblem` so that given a `start_location`, set of `waypoint_tags`, and an `end_tag`, the minimum cost path corresponds to the shortest path from `start_location` to a location with the `end_tag`, such that all of `waypoint_tags` are covered by some location in the path (potentially including the `start_location`). You can assume that waypoint tags are distinct.
    Note that a single location can be used to satisfy multiple tags.

(b) If there are $n$ locations and $k$ waypoint tags, what is the maximum possible number of states given a suitable state definition for part a that UCS could visit?

*Expected:* A mathematical expression that depends on $n$ and $k$, with a brief explanation justifying it. A simple upper bound is fine: you don't need to exclude states that UCS can never actually reach.

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::
