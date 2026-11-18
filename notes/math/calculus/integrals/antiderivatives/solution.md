<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit1801f06-4-q2" status="draft"}
$\frac{d}{dx}\frac12\tan^2x=\tan x\sec^2x$ (chain rule, $(\tan x)'=\sec^2x$), and $\frac{d}{dx}\frac12\sec^2x=\sec x\cdot\sec x\tan x=\tan x\sec^2x$. So both are antiderivatives (substitutions $u=\tan x$ and $u=\sec x$ respectively).

There is no contradiction: $\frac12\sec^2x-\frac12\tan^2x=\frac12$ is constant, and by @thm-antiderivatives-differ-by-constant two antiderivatives may differ by a constant. Each formula should be read with its own $+c$.
:::
