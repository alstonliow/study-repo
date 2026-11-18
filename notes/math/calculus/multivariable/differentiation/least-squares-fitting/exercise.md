::: {.problem #prob-mit1802f07-4-q1 origin="external" source="mit1802f07-4-q1"}
– Least squares and data analysis.

Parts (b)-(f) of this problem involve the use of Matlab. You may optionally use any other software with similar features, or even a calculator. In that case, indicate what you used, and describe how you proceeded. You must carry out the actual calculations rather than rely on the statistical functions that may be built into the software you are using.

a) Before going to the terminal, read Notes LS and do the following. Consider the row vectors $x=[x_1\ x_2\ \dots\ x_n]$, $y=[y_1\ y_2\ \dots\ y_n]$ and $u=[1\ 1\ \dots\ 1]$ ($n$ ones). Let $y=ax+b$ be the best-fitting line for the $n$ points $(x_i,y_i)$. Translate the formula (4) in LS into a single $2\times2$ matrix equation
$$Az=r,\qquad z=\begin{pmatrix}a\\b\end{pmatrix}$$
Write the entries of $A$ and $r$ in Matlab-ready form. Don't use summations, instead use, for example, `x * u'` for $\sum x_i$. You will be able to confirm that your formulas are correct by testing them on a concrete example using Matlab in part (c).

b) The worldwide sales of iPods (in million units) for each year from 2001 to 2005 are given below (sources: Wikipedia, Apple quarterly reports):

| Years ($x_i$) | '01 | '02 | '03 | '04 | '05 |
|---|---|---|---|---|---|
| Sales ($y_i$) | 0.125 | 0.470 | 1.451 | 8.263 | 31.960 |

(To make the numerical answers easier to read, we take the variable $x$ to be the year minus 2000, so $x_i$ ranges from 1 to 5 for the given data points).

Look at the Matlab directions for plotting at the end of this problem set and make a scatter plot of these data points marked with $*$'s. (Nothing to hand in; you will do this over again with part (d).)

c) Use Matlab, the data from (b) and the formulas you found in part (a) to find the best line $y=ax+b$ fitted to the points. Compute the difference between the actual value of the data $y$ and the predicted value $y=ax+b$. Report $a$, $b$, and the worst case (largest error).

(Optional, but recommended: check that your answer for $a$ and $b$ agrees with the Matlab operation `polyfit(x,y,1)`, which computes the coefficients of the best polynomial of degree 1 fitting the data $x$ and $y$. If `c = polyfit(x, y, 1)` then $c=[a,b]$ is the transpose of the column vector $z$ in part (a). In this way you can confirm that you did part (a) correctly.)

d) When a new product is launched, in the initial period the sales tend to grow exponentially rather than linearly. Use Matlab to find the best fit of the form $\ln(y)=a_1x+b_1$. (Note: Matlab uses the notation log for natural log, and log10 for log in base 10. So, in Matlab notation, you will be using log(y).) Report your values of $a_1$, $b_1$.

If you exponentiate this equation, you get
$$y=e^{b_1}e^{a_1x}$$
Compute the difference between $y$ and the predicted value according to this formula and report the worst case (largest error).

e) Hand in a printout that shows on the same plot: the scatter plot of $(x,y)$ labelled with $*$'s, the straight line fit, $(x,ax+b)$ as a dashed line, and the curve $(x,e^{b_1}e^{a_1x})$, connected by an ordinary line.

f) According to the exponential best fit, how many iPods were sold in 2006? how many will be sold in 2015? (for comparison, the total world population is about 6.6 billions). In fact, the growth is no longer exponential: "only" 46.4 million iPods were sold in 2006.

*Note (these notes):* The Matlab directions printed at the end of the problem set are not reproduced. The solution below was computed in Python (numpy); the printout of part (e) is not reproduced.
:::

::: {.problem #prob-mit1802n-2g-q1 origin="external" source="mit1802n-2g-q1"}
Find by the method of least squares the line which best fits the three data points given. Do it from scratch, using (2) in Notes LS and differentiation (use the chain rule). Sketch the line and the three points as a check.

a) $(0,0),(0,2),(1,3)$  b) $(0,0),(1,2),(2,1)$  c) $(1,1),(2,3),(3,2)$

*Note (these notes):* Parts (a) and (b) were assigned.
:::

::: {.problem #prob-mit1802n-2g-q4 origin="external" source="mit1802n-2g-q4"}
What linear equations in $a,b,c$ does the method of least squares lead to, when you use it to fit a linear function $z=a+bx+cy$ to a set of data points $(x_i,y_i,z_i)$, $i=1,\dots,n$?
:::
