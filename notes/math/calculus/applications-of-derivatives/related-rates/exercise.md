::: {.problem #prob-mit1801f06-3-q6 origin="external" source="mit1801f06-3-q6"}
(extra credit) Hypocycloid, again. Here we derive the equation for the hypocycloid of Problem 2 from the sweeping out property directly. This takes quite a bit longer. We will look at the hypocycloid from yet another (easier) point of view later on.

Think of the first quadrant of the $xy$-plane as representing the region to the right of a wall with the ground as the positive $x$-axis and the wall as the positive $y$-axis. A unit length ladder is placed vertically against the wall. The bottom of the ladder is at $x=0$ and slides to the right along the $x$-axis until the ladder is horizontal. At the same time, the top of the ladder is dragged down the $y$-axis ending at the origin $(0,0)$. We are going to describe the region swept out by this motion, in other words, the blurry region formed in a photograph of the motion if the eye of the camera is open the whole time.

a) Suppose that $L_1$ is the line segment from $(0,y_1)$ to $(x_1,0)$ and $L_2$ is the line segment from $(0,y_2)$ to $(x_2,0)$. Find the formula for the point of intersection $(x_3,y_3)$ of the two line segments. Don't expect the formula to be simple: It must involve all four parameters $x_1$, $x_2$, $y_1$, and $y_2$. But simplify as much as possible!

It's important to make sure you have the right formulas before proceeding further. You can doublecheck your formulas in several ways. (This is optional.)

i) If $y_2=0$, then $x_3=x_1$.

ii) When the $x$'s and $y$'s are interchanged the formulas should be the same. What transformation of the plane does the exchange of $x$ and $y$ represent?

iii) It is impossible to find $x_3$ and $y_3$ if the lines are parallel, so the denominator in the formula must be zero when $L_1$ and $L_2$ have the same slope.

iv) Rescaling all variables by a factor $c$ leaves the formula unchanged, so the numerator of the formula for $x_3$ and $y_3$ should have degree (in all variables) one greater than the denominator.

b) Write the equation involving $x_2$ and $y_2$ that expresses the property that ladder $L_2$ has length one. We will suppose that $L_1$ represents the ladder at a fixed position, and $L_2$ tends to $L_1$. Thus
$$x_2=x_1+\Delta x;\qquad y_2=y_1+\Delta y$$
Use implicit differentiation (related rates) to find
$$\lim_{\Delta x\to0}\frac{\Delta y}{\Delta x}$$
(Express the limit as a function of the fixed values $x_1$ and $y_1$.)

c) Substitute $x_2=x_1+\Delta x$ and $y_2=y_1+\Delta y$ into the formula in part (a) for $x_3$ and use part (b) to compute
$$X=\lim_{x_2\to x_1}x_3=\lim_{\Delta x\to0}x_3$$
Simplify as much as possible. Deduce, by symmetry alone, the formula for
$$Y=\lim_{x_2\to x_1}y_3$$

d) Show that $X^{2/3}+Y^{2/3}=1$. (The limit point $(X,Y)$ that you found in part (c) is expressed as a function of $x_1$ and $y_1$. This is the unique point of the ladder $L_1$ that is also part of the boundary curve of the region swept out by the family of ladders.)
:::
