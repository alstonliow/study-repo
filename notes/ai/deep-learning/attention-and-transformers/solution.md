<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs231na-3-q1" status="draft"}
1. *Several heads.* One head computes one set of attention weights per position, so each output is a single weighted average of the values. If a position needs information from several others for different reasons (a previous word, a related image region), one softmax must compromise and blurs them together. With $h$ heads, each working in its own $d/h$-dimensional subspace, different heads can attend to different positions at the same cost (@def-multi-head-attention).
2. *Dividing by $\sqrt{d/h}$.* Dot products of $d/h$-dimensional vectors with entries of unit variance have variance $d/h$ (@prp-attention-score-variance). Without the scaling, the scores grow with the head size, the softmax becomes nearly one-hot, and its gradients become nearly zero, which slows or stalls learning. The scaling keeps the scores of unit variance whatever the width.
3. *Output projection.* The concatenated heads are separate weighted averages of values, each confined to its own block of coordinates. Without a final linear map, the information of the different heads would stay in separate slices and could not be combined within the layer, and the output would be restricted to weighted averages of value vectors. The projection $A$ mixes the heads and maps the result back to the model's representation space before the residual addition.
:::
