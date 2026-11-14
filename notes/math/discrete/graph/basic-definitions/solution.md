<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-graph-1-01" status="draft"}
(a) $\forall e\ \exists v\ \mathrm{incident}(v,e)$.

(b) No edge has a vertex that is its only vertex:
    $$\neg\exists e\ \exists v\ \bigl(\mathrm{incident}(v,e)\wedge\forall w\,(\mathrm{incident}(w,e)\to w = v)\bigr).$$

(c) $$\forall e\ \exists v\ \exists w\ \Bigl(v\ne w\wedge\mathrm{incident}(v,e)\wedge\mathrm{incident}(w,e)\wedge\forall z\,\bigl(\mathrm{incident}(z,e)\to(z = v\vee z = w)\bigr)\Bigr).$$

(d) No two different edges share two different vertices:
    $$\forall e\ \forall f\ \Bigl(e\ne f\to\neg\exists v\ \exists w\ \bigl(v\ne w\wedge\mathrm{incident}(v,e)\wedge\mathrm{incident}(w,e)\wedge\mathrm{incident}(v,f)\wedge\mathrm{incident}(w,f)\bigr)\Bigr).$$

(e) The conjunction of (c) and (d). Formula (c) already rules out loops and
    edges with no or too many ends, and (d) rules out multiple edges.

(f) $\forall v\ \exists e\ \mathrm{incident}(v,e)$.
:::
