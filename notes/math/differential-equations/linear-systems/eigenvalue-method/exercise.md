::: {.problem #prob-mit1803ps-33-q1 origin="external" source="mit1803ps-33-q1"}
[Eigenvalues, eigenvectors] (a) Find the eigenvalues and eigenvectors of the companion matrix for $\ddot x + 4\dot x + 3x = 0$. On the $x, y$ plane draw the eigenlines. For each of the two eigenlines, write down a solution which moves along it. Compare this with the work you did on the part II problem in the previous session.

(b) Find the eigenvalues and eigenvectors of the matrix $A = \begin{pmatrix}2&-4\\1&-3\end{pmatrix}$. Sketch the eigenlines, and for each eigenline write down all the solutions whose trajectories lie on that line.

(c) Now, invoke Linear Phase Portraits: Matrix Entry again, set $a$, $b$, $c$, and $d$ to display the phase plane for this matrix, and sketch the phase plane that it displays. Make sure to include (by clicking on the phase plane) at least one trajectory in each wedge between eigenlines. Include arrows indicating the direction of time.

*Note (these notes):* The Java Mathlets this problem uses no longer run in most browsers; the solution answers the analytic parts and describes what the applet would show.
:::

::: {.problem #prob-mit1803ps-34-q1 origin="external" source="mit1803ps-34-q1"}
[Complex and repeated eigenvalues]

(a) The population of long-tailed weasels and meadow voles on Nantucket Island has been studied by biologists. They measure the populations relative to a baseline, in hundreds of animals. So $x(2) = 5$ means that at $t = 2$ there are 500 more weasels than the baseline value, and $y(2) = -5$ means that at $t = 2$ there are 500 fewer voles than the baseline value.

Biologists from MIT have established the following relationship between $x(t)$ and $y(t)$:
$$\dot x = (0.5)x + y,\qquad \dot y = -(2.25)x + (0.5)y$$
So the natural growth rate for each species is 0.5, and cross terms show that more voles are good for weasels but more weasels are very bad for voles.

Work out the population evolution predicted by this model. (Linear Phase Portraits: Matrix Entry may be useful to you in visualizing this.) What are the eigenvalues? For one eigenvalue, find the exponential solution of $\dot u = Au$. Then take the real and imaginary parts to produce two real solutions. Suppose that at $t = 0$ there are 100 more weasels than baseline, and the vole population is the baseline value. What is the solution to this initial value problem? Is the number of weasels increasing at $t = 0$? How about the number of voles? When does the number of voles next equal its baseline value (if ever)? Please sketch the phase portrait and the graphs of $x(t)$ and $y(t)$ (for this initial condition) for $t$ between about $-2$ and $+2$. Make it clear how these three pictures are related: indicate on the trajectory the position of $\begin{pmatrix}x(t)\\y(t)\end{pmatrix}$ when $t = \frac{k\pi}3$ for $k = -2, -1, 0, 1, 2$.

(b) Invoke the Mathlet Linear Phase Portraits: Matrix Entry. Play with the tool for a while to get a feel of it. Notice that the eigenvalues can be displayed on the complex plane. Deselect the [Companion Matrix] option, so you can set all four entries in the matrix. Select the [eigenvalues] option, so the eigenvalues become visible by means of a plot of their location in the complex plane and also a read-out of their values.

Set the sliders so that $A = \begin{pmatrix}1&b\\0&1\end{pmatrix}$. Watch what happens to the phase portrait as $b$ varies from $-4$ to $4$. For each value of $b$, the applet suggests a pair of eigenvalues; verify what it claims. For each value of $b$, describe the collection of all eigenvectors for each eigenvalue. (This description will depend upon $b$.) For each value of $b$, write down all the normal mode solutions (i.e. all the solutions of the form $e^{\lambda t}\mathbf v$, where $\lambda$ is a number and $\mathbf v$ is a vector). If the system is defective, find a complementary solution. Take one value of $b$ for which the system is complete and sketch the phase portrait. Take one value of $b$ for which the system is defective and sketch the phase portrait.

*Note (these notes):* The Java Mathlets this problem uses no longer run in most browsers; the solution answers the analytic parts and describes what the applet would show.
:::
