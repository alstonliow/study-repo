::: {.problem #prob-cs188hw-9-q2 origin="external" source="cs188hw-9-q2"}
**Learning to Act.** In lecture and discussion, we have mainly used the Naive Bayes algorithm to do binary classification, such as classifying whether an email is spam. However, we can also use Naive Bayes to learn how to act in an environment. This problem will explore learning good policies with Naive Bayes and comparing them to policies learned with RL.

We consider the following one-dimensional grid world environment with three squares, named $A$, $B$, and $C$ from left to right. Pacman has two possible actions at each square: left and right. Taking the left action at square $A$ or the right action at square $C$ will transition to a terminal state $x$ where no further action can be taken. At each timestep, Pacman observes his own position ($s_p$) as well as the ghost's position ($s_g$), and he uses these observations to decide on an action.

Pacman has no idea about the transition probabilities of the ghost or the rewards it gets. However, Pacman has access to an expert demonstration dataset, which gives reasonably good actions to take in a number of scenarios. The dataset is divided into training, validation, and test datasets. The following is the training set of the dataset.

| $s_p$ | B | C | A | C | B | C |
|---|---|---|---|---|---|---|
| $s_g$ | C | A | B | C | A | B |
| $a$ | left | left | left | right | right | right |

1. Using the standard Naive Bayes algorithm, what are the maximum likelihood estimates for the following conditional probabilities (encoded in the Bayes Net)?

   $P(s_p=C\mid a=\text{left})=$ $\quad P(s_p=A\mid a=\text{right})=$ $\quad P(a=\text{left})=$
2. Using the standard Naive Bayes algorithm, which action should we choose in the following new scenarios?

   $s_p=A$, $s_g=C$: Left Right

   $s_p=C$, $s_g=B$: Left Right
3. Suppose we want to add Laplace smoothing with strength $k$ in the Naive Bayes algorithm. (There is no smoothing when $k=0$.) Which of the following are true?
   - To find the optimal value of $k$, we pick the value of $k$ which gives the highest accuracy on the training set.
   - To find the optimal value of $k$, we pick the value of $k$ which gives the highest accuracy on the validation set.
   - To find the optimal value of $k$, we pick the value of $k$ which gives the highest accuracy on the test set.
   - If $k=0$, we may observe low accuracy on the test set due to overfitting.
   - If $k$ is a very large integer, the posterior probability for each action will be close to 0.5.
   - None of the above
:::
