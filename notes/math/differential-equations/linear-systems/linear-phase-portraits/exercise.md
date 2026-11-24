::: {.problem #prob-mit1803ps-34-q2 origin="external" source="mit1803ps-34-q2"}
[Qualitative behavior of linear systems]

We will use Linear Phase Portraits: Matrix Entry to investigate the phase portraits of the homogeneous linear equation $\dot u = Au$, where $A = \begin{pmatrix}a&-3\\1&-1\end{pmatrix}$, as $a$ varies. The focus is now on the colorful diagram at the upper left. To start with, set the matrix to $A = \begin{pmatrix}-4&-3\\1&-1\end{pmatrix}$. Then move the $a$ slider up to $a = 4$, and watch (1) the movement of the mark on the (Tr,Det) plane; (2) the movement of the eigenvalues in the complex plane; and (3) the variation of the phase portrait.

(a) Compute the trace and determinant of $A$. (They will depend upon $a$, of course.) Find an equation for the curve (or line) traced out by the mark on the (Tr,Det) plane.

(b) You notice that the curve in the (Tr,Det) plane enters a number of different regions. When the cursor crosses a red boundary, the trajectories and the eigenvalue indicators turn red. Work out what the values of $a$ are at those crossings. (So this is: where $\det A = 0$, where $\det A = (\operatorname{tr}A/2)^2$ (twice, once not represented on the Mathlet), and where $\operatorname{tr}A = 0$.

(c) There are nine phase portrait types represented as $a$ varies (five regions and four walls). Draw an interval from $-5$ to $+4$. On it, mark the four values of $a$ at which the matrix crosses one of the walls. Indicate the type of phase portrait you have at each of the marked points and along the intervals between them. That is, classify the phase portrait into one of the following types, as in the Supplementary Notes, §25: spiral (stable/unstable, clockwise/counterclockwise), node (stable/unstable); saddle; center (clockwise/counterclockwise); star (stable/unstable); defective node (stable/unstable; clockwise/counterclockwise); degenerate (comb (stable/unstable), constant, parallel lines). (The applet uses the alternative terms "source" and "sink" for "unstable" and "stable.")

(d) For each of the four special values, and for your choice of one value in each of the five regons, make a sketch of the phase portrait. Be sure to include and mark as such any eigenlines, and the direction of time.

*Note (these notes):* The Java Mathlets this problem uses no longer run in most browsers; the solution answers the analytic parts and describes what the applet would show.
:::

::: {.problem #prob-mit1803ps-34-q3 origin="external" source="mit1803ps-34-q3"}
Let $c$ be a real constant. This problem will analyze the system
$$x' = y,\qquad y' = cx - 2y,$$

(a) What is the characteristic polynomial of the coefficient matrix $A$ for the system?

(b) Compute its eigenvalues and eigenvectors. The answer depends on $c$ so you will need to break your answer into cases.

(c) Write down the general real solution to the equation. Again you will need to break into cases depending on $c$. (The trace-determinant diagram will help.)

(d) Open the visual Linear Phase Portraits: Matrix Entry, click the eigenvalues button on and the companion matrix button off. Using representative values of $c$ give sketches of all the different types of phase portraits possible as $c$ varies. Using your answer in part (c) explain the portrait when $c = -3$.

*Note (these notes):* The Java Mathlets this problem uses no longer run in most browsers; the solution answers the analytic parts and describes what the applet would show.
:::
