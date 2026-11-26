<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6854ps-2-q5" status="draft"}
1. *(i)* Run Klein's algorithm (@def-cycle-cancelling) from $f=0$. Every amount pushed is a minimum of integer residual capacities, so all flows and residual capacities stay integers.

2. Each cancellation lowers the cost by $\varepsilon\,|a(\Gamma)|\ge1$ (both integers, positive), and the cost of any circulation is at least $-\sum_e|a(e)|c(e)$, so the algorithm stops, with an integral circulation and, by @thm-circulation-optimality, an optimal one.

3. *(ii)* For an optimal $f$ the proof of @thm-circulation-optimality (2 ⇒ 3) takes $p(v)$ = least cost of a path to $v$ in $G_f$ from an added vertex with edges of cost $0$. Path costs are sums of integer costs, so $p$ is integral, and $a_p\ge0$ on $E_f$.
:::

::: {.solution for="prob-mit6854ps-2-q6" status="draft"}
A packet that enters arc $(v,w)$ at time $\theta$ reaches $w$ at time $\theta+\tau(v,w)$.

*(a) Time-expanded network.* Vertices $(v,\theta)$ for $v\in V$, $\theta=1,\dots,D$, plus a super source $s^*$ and super sink $t^*$. Arcs: $(v,\theta)\to(w,\theta+\tau(v,w))$ of capacity $1$ for every $(v,w)\in E$ and $\theta+\tau\le D$ (the arc used at time $\theta$); $(v,\theta)\to(v,\theta+1)$ of infinite capacity (waiting); $s^*\to(s,\theta)$ and $(t,\theta)\to t^*$ of infinite capacity. An integral maximum $s^*$–$t^*$ flow has value $k(D)$: schedules and integral flows correspond, a packet's route through $G'$ telling when it uses each arc. $|V'|=D|V|+2$.

*(b)* Let $f^*$ be an optimal circulation, integral (previous problem).

1. *$k(D)\ge C^*$.* Decompose $f^*$ into cycles of $0$–$1$ arcs. Cycles avoiding $(t,s)$ have cost $\ge0$; drop them (cost does not rise). Each other cycle is an $s$–$t$ path $P$ plus $(t,s)$, of cost $\tau(P)-D$, and the paths are arc-disjoint. On each path with $\tau(P)<D$ send one packet entering at each time $\theta=1,\dots,D-\tau(P)$, travelling without waiting; it arrives by $D$. Arc-disjoint paths and one packet per path per time step respect the capacities. This sends $\sum_P(D-\tau(P))\ge-a(f^*)=C^*$ packets (paths with $\tau(P)\ge D$ contribute $\le0$ to $-a(f^*)$). This is also the schedule.

2. *$k(D)\le C^*$.* Take integral optimal potentials $\pi$ (previous problem) with $\pi(s)=0$; the arc $(t,s)$ is always residual, so $-D+\pi(t)-\pi(s)\ge0$, i.e. $\pi(t)\ge D$. Write $\rho(v,w)=\tau(v,w)+\pi(v)-\pi(w)$. Optimality gives: $\rho<0\Rightarrow f^*(v,w)=1$ and $f^*(v,w)=1\Rightarrow\rho\le0$; and if $f^*(t,s)>0$ then $\pi(t)=D$. So $C^*=-a(f^*)=-\sum_e\rho(e)f^*(e)=\sum_{(v,w)\in E}\max\big(0,-\rho(v,w)\big)$, using @prp-reduced-cost.

3. In the time-expanded network take the source side $X=\{s^*\}\cup\{(v,\theta):\theta\ge\pi(v)+1\}$. It contains every $(s,\theta)$ ($\theta\ge1$), no $(t,\theta)$ with $\theta\le D\le\pi(t)$, and no waiting arc leaves it. An arc $(v,\theta)\to(w,\theta+\tau)$ leaves $X$ when $\pi(v)+1\le\theta$ and $\theta+\tau\le\pi(w)$: at most $\max(0,\pi(w)-\pi(v)-\tau)=\max(0,-\rho)$ values of $\theta$. So the cut has capacity at most $C^*$, and $k(D)\le C^*$.

*Example.* With $D=5$: paths $s\,t$ ($\tau=2$) and $s\,a\,t$ ($\tau=4$), cost $(2-5)+(4-5)=-4$, so $k(5)=4$: three packets on $(s,t)$ and one on $s,a,t$.

*(c)* $k(D)$ is non-decreasing in $D$, and $D(k)\le(n-1)T+k$ (send all packets one per time step along a shortest path). Binary search on $D\in[1,(n-1)T+k]$, each step one min-cost circulation with costs at most $\max(T,D)$: $O(\log(nT+k))$ circulations, e.g. with cancel-and-tighten $O(mn^2\log(n(nT+k)))$ each, so $O\big(mn^2\log^2(nT+k)\big)$ in total.

*(d)* By (b), $k(D)=\max_{v\ge0}\big(Dv-c(v)\big)$, where $c(v)$ is the least total transit time of $v$ arc-disjoint $s$–$t$ paths (an integral flow of value $v$ in the unit-capacity network). Successive shortest paths (@def-successive-shortest-paths) computes $c(1),c(2),\dots,c(v_{\max})$, $v_{\max}\le m$, with $O(m)$ shortest-path computations, a strongly polynomial $O(nm^2)$ with Bellman–Ford. Then $D(k)=\min_{1\le v\le v_{\max}}\big\lceil(k+c(v))/v\big\rceil$, in $O(m)$ more.
:::
