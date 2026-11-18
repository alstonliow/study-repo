<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs221hw-4-q4" status="draft"}
Tabular Q-learning learns each discretised state separately, so it needs every relevant state visited many times, and its table grows exponentially with the dimension of the state. Function approximation shares parameters between similar states, so an update in one state also improves the estimates of nearby, never-visited states. This matters when exploration is limited (few episodes, or exploration that is costly), when the state space is high-dimensional and most states are never seen, and when memory is limited, since the number of weights is fixed by the feature map rather than by the number of states.
:::
