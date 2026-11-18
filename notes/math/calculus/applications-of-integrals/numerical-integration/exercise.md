::: {.problem #prob-mit1801f06-6-q4 origin="external" source="mit1801f06-6-q4"}
The basis for Simpson's rule is the following formula. Let $x_1$ be the midpoint of the interval $[x_0,x_2]$, and denote its length by $2h$. Consider any three points $(x_0,y_0)$, $(x_1,y_1)$, $(x_2,y_2)$. There is a unique quadratic function (parabola)
$$y=Ax^2+Bx+C$$
whose graph passes through the three points. Simpson's rule says that the area under the parabola above $[x_0,x_2]$ is
$$\frac h3(y_0+4y_1+y_2)$$
This problem is devoted to proving this formula. It is significant because it illustrates how calculations can be simplified by using symmetry, and by looking ahead to see what you need.

Since the area will be the same if the parabola is translated to the left or right, we may assume that $x_0=-h$, $x_1=0$, and $x_2=h$. Then in terms of the rest of the data (i.e., $h$ and the $y_i$)

make a sketch and determine $C$;

show, by integrating, that to find the area we need only determine $A$ (or better, $2Ah^2$);

determine $2Ah^2$ using the data;

put the results together to establish the formula for area.
:::

::: {.problem #prob-mit1801f06-6-q5 origin="external" source="mit1801f06-6-q5"}
Use a calculator to make a table of values of the integrand and find approximations to the Fresnel integral $\int_0^a\cos(t^2)\,dt$ for $a=\sqrt{\pi/2}$, using Simpson's rule with four and eight intervals. (The exact answer to five decimal places is 1.22505. Record your approximations to six decimal places to compare.)
:::
