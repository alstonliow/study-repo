<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs221hw-7-q7" status="draft"}
**(a.i)** The checker is **sound but not complete**.

1. The checker requires $\mathrm{Beneficial}(x)$, whereas the policy requires only $\mathrm{Beneficial}(x)\lor\mathrm{Neutral}(x)$; the other two conditions are the same.
2. Since $\mathrm{Beneficial}(x)$ implies $\mathrm{Beneficial}(x)\lor\mathrm{Neutral}(x)$, every use case the checker allows is permitted by the policy: sound.
3. A use case that is neutral but not beneficial is permitted by the policy and refused by the checker: not complete.
4. They disagree on *Case2* (consented, neutral, not beneficial, no harm or risk): the policy permits it, the checker refuses it. On *Case1* they agree: both refuse it, because it is harmful and high-risk.

**(b)** System A, the sound one. Soundness means $\{f: KB\vdash f\}\subseteq\{f: KB\vDash f\}$: every conclusion it derives is actually entailed, so it never makes us act on a false conclusion. The price is that it may fail to derive some true facts, which in a safety-critical setting means being cautious, not being wrong.

**(c)** System B, the complete one. Completeness means $\{f: KB\vDash f\}\subseteq\{f: KB\vdash f\}$: every true conclusion is among its hypotheses, so none is missed. It also produces some false hypotheses, but the separate verifier removes those, so together they keep all of the true information.
:::
