::: {.problem #prob-mit1801f06-2b-q1 origin="external" source="mit1801f06-2b-q1"}
Golf balls

The area of a section of a sphere of radius $R$ between two parallel planes that are a distance $h$ apart is$^1$
$$\text{area of a spherical section}=2\pi hR$$
Slice the sphere of radius $R$ by a horizontal plane. The portion of the plane inside the sphere is a disk of radius $r\le R$. The portion of the spherical surface above the plane is called a spherical cap. For example, if the plane passes through the center, then the disk has radius $r=R$, its circumference is the equator, and the spherical cap is the Northern Hemisphere. More generally, a spherical cap is the portion of surface of the Earth north of a latitude line. The formula above applies to regions between two latitude lines, and, in particular, to spherical caps.

a) Consider a spherical cap which is the portion of the surface of the sphere above horizontal plane that slices the sphere at or above its center. Find the area of the cap as a function of $R$ and $r$. Do this by finding first the formula for the height $h$ of the spherical cap in terms of $r$ and $R$. (This height is the vertical distance from the horizontal slicing plane to the North Pole.) Then use your formula for $h$ and the formula above for the area of spherical sections.

b) Express the formula for the area of a spherical cap in terms of $R^2$ and $r/R$. (This is natural because the proportional scaling $cr$ and $cR$ changes the area by the factor $c^2$.) Then use the linear and quadratic approximations to $(1+x)^{1/2}$ near $x=0$ to find a good and an even better approximation to the area of the spherical cap, appropriate when the ratio $r/R$ is small. (Hint: What is $x$?) Simplify your answers as far as possible: the approximation corresponding to the linear approximation to $(1+x)^{1/2}$ should be very familiar.

c) The following problem appeared on a middle school math contest exam. The numbers have been changed to protect the innocent. Consider a golf ball that is 3 centimeters in diameter with 100 hemispherical dimples of diameter 3 millimeters. (Note that this is not a realistic golf ball because the dimples are too deep). Find the area of the golf ball rounded to the nearest 1/100 of a square centimeter using the approximation $\pi\approx3.14$. (The students were given three minutes. We are spending more time on it.)

Under the rules of the contest, an incorrectly rounded answer was counted as wrong with no partial credit, so correct numerical approximation was crucial. Some students objected that they could not figure out the area of portion of the large sphere that is removed when a dimple is inserted. A careless examiner had assumed that the students would use the approximation that the area removed for each dimple was nearly the same as the area of a flat disk. We are going to figure out whether this approximation is adequate or gives the wrong answer according to the rules.

Write down formulas for the surface area of the golf ball in the three cases listed below. (Put in 100 dimples, but leave $r$, $R$, and $\pi$ as letters.)

i) the approximation pretending that the removed surface is flat (what is the relationship between this and the approximations of part (b)?)

ii) the higher order approximation you derived in part (b)

iii) the exact formula

Finally, evaluate each of the answers for the given values $r=.15$ and $R=1.5$ centimeters, and find the accuracy of the approximations.

d) (extra credit$^2$) Although nobody noticed at the time, the examiner who created this problem made a much bigger mistake. With the diameters actually given, it would have been impossible for the number of dimples given to be placed on the golf ball without overlap. Give a (reasonable) estimate for the largest number of dimples that can fit on our golf ball.

$^1$ This formula will be derived in Unit 4. Two examples may convince you that it is reasonable. For $h=R$, it gives the area of the hemisphere, $2\pi R^2$. For $h=2R$ it gives $4\pi R^2$, the area of the whole sphere.

$^2$ Extra credit points are tabulated separately and only added to your final score at the end of the semester so that they do not influence any grading cutoffs.
:::

::: {.problem #prob-mit1801f06-3-q3 origin="external" source="mit1801f06-3-q3"}
Sensitivity of measurement, revisited.

a) Recall that in problem 2, PS1/Part II, $L^2+20{,}000^2=h^2$. Use implicit differentiation to calculate $dL/dh$. Compare the linear approximation $dL/dh$ to the error $\Delta L/\Delta h$ computed in examples on PS1. Explain why $\Delta L/\Delta h\le dL/dh$ if the derivative is evaluated at the left endpoint of the interval of uncertainty (or, in other words, $\Delta h>0$). In what range of values of $h$ is it true that $|\Delta L|\le2|\Delta h|$?

b) Suppose that the Planet Quirk is a not only flat, but one-dimensional (a straight line). There are several satellites at height $20{,}000$ kilometers and you get readings saying that satellite 1 is directly above the point $x_1\pm10^{-10}$ and is at a distance $h_1=21{,}000\pm10^{-2}$ from you, satellite 2 is directly above $x_2\pm10^{-10}$ and at a distance $h_2=52{,}000\pm10^{-2}$. Where are you and to what accuracy? Hint: Consider separately the cases $x_1<x_2$ and $x_2>x_1$.

c) Express $dL/dh$ in terms of the angle between the line of sight to the satellite and the horizontal from the person on the ground. (When expressed using the line-of-sight angle, the formula also works for a curved planet like Earth.)
:::

::: {.problem #prob-mit1801f06-3-q4 origin="external" source="mit1801f06-3-q4"}
More sensitivity of measurement. Consider a parabolic mirror with equation $y=-1/4+x^2$ and focus at the origin. (See Problem Set 1.) A ray of light traveling down vertically along the line $x=a$ hits the mirror at the point $(a,b)$ where $b=-1/4+a^2$ and goes to the origin along a ray at angle $\theta$ measured from the positive $x$-axis.

a) Find the formula for $\tan\theta$ in terms of $a$ and $b$, and calculate $d\theta/da$ using implicit differentiation. (Express your answer in terms of $a$ and $\theta$.)

b) If the telescope records a star at $\theta=-\pi/6$ and the measurement is accurate to $10^{-3}$ radians, use part (a) to give an estimate as to the location of the star in the variable $a$.

c) (optional; no credit) Solve for $a$ as a function of $\theta$ alone and doublecheck your answers to parts (a) and (b).
:::
