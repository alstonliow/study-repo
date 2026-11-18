::: {.problem #prob-mit1806s10-1-q13 origin="external" source="mit1806s10-1-q13"}
If $A$ has row 1 + row 2 = row 3, show that $A$ is not invertible:

(a) Explain why $A\mathbf{x}=(1,0,0)$ cannot have a solution.

(b) Which right sides $(b_1,b_2,b_3)$ might allow a solution to $A\mathbf{x}=\mathbf{b}$?

(c) What happens to row 3 in elimination?
:::

::: {.problem #prob-mit1806s10-2-q1 origin="external" source="mit1806s10-2-q1"}
Use Gauss-Jordan elimination on $[U\ I]$ to find the upper triangular $U^{-1}$:
$$UU^{-1}=I\qquad\begin{bmatrix}1&a&b\\0&1&c\\0&0&1\end{bmatrix}\begin{bmatrix}\mathbf{x}_1&\mathbf{x}_2&\mathbf{x}_3\end{bmatrix}=\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}.$$
:::

::: {.problem #prob-mit1806s10-2-q2 origin="external" source="mit1806s10-2-q2"}
$A$ is a 4 by 4 matrix with 1's on the diagonal and $-a,-b,-c$ on the diagonal above. Find $A^{-1}$ for this bidiagonal matrix.
:::

::: {.problem #prob-mit1806s10-2-q6 origin="external" source="mit1806s10-2-q6"}
If you print $K^{-1}$, it doesn't look good. But if you print $7K^{-1}$ (when $K$ is 6 by 6), that matrix looks wonderful. Write down $7K^{-1}$ by hand, following this pattern:

1. Row 1 and column 1 are $(6,5,4,3,2,1)$.
2. On and above the main diagonal, row $i$ is $i$ times row 1.
3. On and below the main diagonal, column $j$ is $j$ times column 1.

Multiply $K$ times that $7K^{-1}$ to produce $7I$. Here is that pattern for $n=3$:
$$\text{3 by 3 case}\quad\text{The determinant of this }K\text{ is }4\qquad (K)(4K^{-1})=\begin{bmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{bmatrix}\begin{bmatrix}3&2&1\\2&4&2\\1&2&3\end{bmatrix}=\begin{bmatrix}4&&\\&4&\\&&4\end{bmatrix}.$$

*Note (these notes):* $K$ is the 6 by 6 matrix of @prob-mit1806s10-2-q5.
:::

::: {.problem #prob-mit1802f07-1-q5 origin="external" source="mit1802f07-1-q5"}
Cookies, doughnuts, and croissants contain essentially the same ingredients (flour, sugar, egg, butter) but in different proportions. For example, it takes 22 grams of flour to make a cookie, versus 40 g for a doughnut and 50 g for a croissant. The compositions of the various pastries can be encoded in a $4\times3$ matrix,
$$M=\begin{pmatrix}22&40&50\\18&10&3\\5&14&5\\10&10&22\end{pmatrix},$$
where the entries in the $i$-th row represent the amounts of ingredient $i$ ($i=1$ for flour, 2 for sugar, 3 for egg, 4 for butter) required to make the various types of pastries.

a) Consider an assortment of $x_1$ cookies, $x_2$ doughnuts and $x_3$ croissants, and form the column vector
$$\mathbf{X}=\begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix}.$$
What do the entries of the vector $M\mathbf{X}$ correspond to?

b) Each of the four ingredients has a specific nutritional value: for example, 100 grams of flour contain 10 g of protein, 76 g of carbohydrates, and 1 g of fat. Proceeding similarly for all four ingredients, we can build a $3\times4$ matrix,
$$N=\begin{pmatrix}0.10&0&0.13&0\\0.76&1.00&0.01&0\\0.01&0&0.10&0.82\end{pmatrix},$$
where the entries in the $i$-th column represent the proportions of protein, carbohydrates and fat in ingredient $i$.

Give a matrix formula for the total nutritional value of the assortment of pastries considered in (a). (Keep your answer in symbolic form, do not evaluate numerically.)

c) Give a matrix formula expressing the numbers $x_i$ of pastries of each type which will add up to $y_1$ g of protein, $y_2$ g of carbohydrates, and $y_3$ g of fat. Express your answer in the form $X=AY$, and give both a formula for $A$ and numerical values for its entries (use either a calculator or Matlab; short directions for Matlab can be found on the course web page in the Assignments section.

d) The recommended daily amounts of protein, carbohydrates and fat for a 2000 calorie diet are 50, 300, and 65 grams respectively. If you wanted to follow those guidelines while eating only cookies, doughnuts, and croissants, how many pastries of each type should you eat daily? What is wrong with your answer? Explain.
:::

::: {.problem #prob-mit1802n-1g-q3 origin="external" source="mit1802n-1g-q3"}
$A=\begin{pmatrix}1&-1&1\\0&1&1\\-1&-1&2\end{pmatrix}$, $\mathbf{b}=\begin{pmatrix}2\\0\\3\end{pmatrix}$. Solve $A\mathbf{x}=\mathbf{b}$ by finding $A^{-1}$.
:::

::: {.problem #prob-mit1802n-1g-q4 origin="external" source="mit1802n-1g-q4"}
Referring to Exercise 3 above, solve the system
$$x_1-x_2+x_3=y_1,\quad x_2+x_3=y_2\quad -x_1-x_2+2x_3=y_3$$
for the $x_i$ as functions of the $y_i$.
:::

::: {.problem #prob-mit1802n-1g-q5 origin="external" source="mit1802n-1g-q5"}
Show that $(AB)^{-1}=B^{-1}A^{-1}$, by using the definition of inverse matrix.
:::
