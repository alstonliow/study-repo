::: {.problem #prob-mit6854ps-3-q4 origin="external" source="mit6854ps-3-q4"}
A team of $n$ members would like to travel a distance $d$ from $A$ to $B$ as quickly as possible. All of them can walk and have also one scooter (which can carry only one person at a time) that they can use. For each person $i$ ($1\le i\le n$), we know his/her walking speed $w_i$ and his/her speed $s_i$ when travelling on the scooter. The goal is to find a way to bring all $n$ people to destination so as to minimize the time at which the last person arrives. The scooter can be left by any member of the group on the side of the road, and picked up by anyone else of the group. Members of the group can also walk or use the scooter backwards (towards $A$) if that helps.

1. Consider the case where $n=3$, $w_1=w_2=1$, $s_1=s_2=6$, $w_3=2$, $s_3=8$ and $d=100$. Find the fastest way for everyone to travel the distance $d$.

2. For a general instance (general $n$ and arbitrary speeds), write a linear program whose value is always a lower bound on the time needed for the $n$-person team to travel a distance $d$. This should be a small linear program; the number of variables and constraints should be $O(n)$ (and not dependent on $d$, or the number of 'legs' of the solution).

3. Use the linear programming routines in matlab (or any LP software like CPLEX) to compute your lower bound for the instance given in 1. (You don't have to use a linear programming software, provided you can exhibit an optimum solution, with a proof of optimality.)

   If the bound you obtain is not equal to the value you found in 1., either improve your solution to 1., or find a stronger linear program in 2.

   Matlab is available on athena, see http://web.mit.edu/olh/Matlab/Matlab.html for more info. Type help linprog for information on how to use the LP routine.
:::
