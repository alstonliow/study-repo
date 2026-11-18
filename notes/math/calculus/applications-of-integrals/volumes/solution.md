<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit1801f06-5-q3" status="draft"}
The region is non-empty only where $z^2/2<z$, i.e. $0<z<2$. At height $z$ the cross-section is the part of the first quadrant between the lines $x+y=z^2/2$ and $x+y=z$; the triangle $x,y>0$, $x+y<s$ has area $s^2/2$, so the cross-section has area
$$A(z)=\frac{z^2}2-\frac{(z^2/2)^2}2=\frac{z^2}2-\frac{z^4}8 .$$
By @prp-volume-by-slices, $V=\int_0^2\Big(\frac{z^2}2-\frac{z^4}8\Big)dz=\frac86-\frac{32}{40}=\frac43-\frac45=\frac8{15}$.
:::

::: {.solution for="prob-mit1801f06-7-q2" status="draft"}
The vertical strip at $x\in[b-a,b+a]$ has height $2\sqrt{a^2-(x-b)^2}$ and sweeps a shell of radius $x$ (@def-disks-and-shells):
$$V=\int_{b-a}^{b+a}2\pi x\cdot2\sqrt{a^2-(x-b)^2}\,dx .$$
Put $u=x-b$: $V=4\pi\int_{-a}^a(u+b)\sqrt{a^2-u^2}\,du$. The term $u\sqrt{a^2-u^2}$ is odd and integrates to $0$; $\int_{-a}^a\sqrt{a^2-u^2}\,du=\frac{\pi a^2}2$ (@exm-trig-sub-area-circle). So
$$V=4\pi b\cdot\frac{\pi a^2}2=2\pi^2a^2b=(\pi a^2)(2\pi b),$$
the area of the disk times the distance travelled by its centre.
:::
