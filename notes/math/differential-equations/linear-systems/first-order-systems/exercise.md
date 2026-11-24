::: {.problem #prob-mit1803ps-32-q1 origin="external" source="mit1803ps-32-q1"}
[Linear systems and matrices] (a) We'll work with the two homogeneous constant coefficient linear equations $\ddot x + 4\dot x + 3x = 0$ and $\ddot x + \dot x + \frac52x = 0$. For each, find two linearly independent real solutions (Please use either exponentials or functions of the form $e^{rt}\cos(\omega t)$ or $e^{rt}\sin(\omega t)$, and denote them by $x_1(t)$ and $x_2(t)$.), write down the general real solution, and determine the damping type. Also compute $\dot x_1$ and $\dot x_2$.

(b) Now write down the companion matrix for each of these two equations.

(c) Open the Mathlet Linear Phase Portraits: Matrix Entry. Select "Companion Matrix," and set the $c$ and $d$ values to the entries of the companion matrix for the first equation. (Note that clicking on a hashmark on a slider sets the value. In some cases you will have to accept the nearest possible value to the desired value.)

For a companion matrix $A = \begin{pmatrix}0&1\\c&d\end{pmatrix}$, the colorful window at the upper left shows $(d, -c)$. You can adjust them by a cursor movement over that plane.

The big window shows the "phase plane" of the system. It displays the trajectories of a few solutions. (The trajectories are the solution curves $(x(t), y(t))$ in the $xy$ plane, with the arrows indicating the direction of increasing $t$. We will study the phase plane trajectory portraits in detail in a later session.)

Click on the window to produce more. You can clear them all using [Clear], and return to the original set of trajectories by re-setting one of the $c$ or $d$ sliders. Do this; return to the originally displayed selection of trajectories.

Since $y = \dot x$, a solution to $\dot u = Au$ is given by $\begin{pmatrix}x(t)\\\dot x(t)\end{pmatrix}$ where $x(t)$ is a solution of $\ddot x + 4\dot x + 3x = 0$ (in this first case). Draw a picture of the phase plane. Each of these trajectory curves should have an arrow on it indicating the direction of time: please indicate this on your picture. Identify which of the trajectories correspond to each of the basic solutions you found in (a). (These will be among the originally chosen trajectories.)

(d) There are some hook-shaped trajectories. The picture doesn't show a scale; but suppose that the largest displayed value of $x$ is $x = 2$. A trajectory crosses the $x$ axis at $x = 1$. What is the solution having this as its trajectory assuming that this crossing occurs at $t = 0$? Sketch the graph of the corresponding solution $x(t)$ of the original second order equation.

(e) Write down the general solution having the same trajectory. (Hint: suppose the solution has $x(a) = 1$).

(f) Now set the $c$ and $d$ sliders to the values relevant to the second equation you solved in (a). Sketch the phase portrait (and include the arrows indicating the direction of time).

Using the same scale as above, what is the solution which passes through $(0, 1)$ at $t = 0$? At what other times does this solution cross the $y$ axis? Sketch, roughly, the graphs of $x(t)$ and of $y(t)$.

(g) In these companion matrix examples, whenever a trajectory crosses the $x$ axis it seems to do it perpendicularly: its tangent vector is vertical. Explain.

*Note (these notes):* The Java Mathlets this problem uses no longer run in most browsers; the solution answers the analytic parts and describes what the applet would show.
:::
