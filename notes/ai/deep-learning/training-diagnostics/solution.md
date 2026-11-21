<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs231na-1-q9" status="draft"}
**Answer:** 1 and 3.

1. A larger training set makes it harder to fit the noise of individual examples, so the gap between training and test accuracy (overfitting, @def-overfitting) usually shrinks.
2. More hidden units increase the capacity of the network. That raises training accuracy and typically widens the gap rather than narrowing it (unless the network was so small that it underfit); it is not a way to decrease the gap.
3. Stronger regularization (@def-regularization) restricts the effective capacity and lowers training accuracy relative to test accuracy, which decreases the gap (@sec-ai-deep-learning-training-diagnostics).
4. False, since 1 and 3 work.
:::
