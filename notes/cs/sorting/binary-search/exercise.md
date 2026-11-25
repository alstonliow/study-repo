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
