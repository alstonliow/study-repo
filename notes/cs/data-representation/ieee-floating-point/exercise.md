::: {#prob-cmu15213r-3-q1 .problem origin="external" source="cmu15213r-3-q1"}
Consider the following 5-bit floating point representation based on the IEEE floating point format. This format does not have a sign bit – it can only represent nonnegative numbers.

- There are k=3 exponent bits.
- There are n=2 fraction bits.

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \i in {0,...,4} { \pgfmathtruncatemacro{\k}{4-\i} \node[tick] at (\i*0.7+0.35,0.85) {\k}; }
\draw[cell frame] (0,0) rectangle (2.1,0.6); \node[lab] at (1.05,0.3) {exp};
\draw[cell frame] (2.1,0) rectangle (3.5,0.6); \node[lab] at (2.8,0.3) {frac};
\end{tikzpicture}
\end{center}
```

What is the…

- Bias?
- Largest denormalized number?
- Smallest normalized number?
- Largest finite number it can represent?
- Smallest non-zero value it can represent?
:::

::: {#prob-float-scale2-code .problem .coding origin="adapted" source="res-cmu-15213-labs-data-lab" tags="floating-point,bit-manipulation"}
A `float` is passed as its bit pattern in an `unsigned` (@def-ieee-floating-point). Write `float_scale2(uf)`, which returns the bit pattern of $2\cdot f$ for the value $f$ that `uf` encodes. If $f$ is NaN, return `uf` unchanged; if $2f$ overflows, return the pattern of $\pm\infty$. Use integer operations, comparisons and `if` freely, but no floating-point types or operations.

```{.c .starter}
unsigned float_scale2(unsigned uf) {
    return uf;
}
```

```{.c .tests}
static unsigned bits_of(float f) { unsigned u; memcpy(&u, &f, 4); return u; }
static float float_of(unsigned u) { float f; memcpy(&f, &u, 4); return f; }

void test_normal_values(void) {
    assert(float_scale2(bits_of(1.5f)) == bits_of(3.0f));
    assert(float_scale2(bits_of(-15213.0f)) == bits_of(-30426.0f));
}

void test_special_values(void) {
    assert(float_scale2(0x00000000u) == 0x00000000u);
    assert(float_scale2(0x80000000u) == 0x80000000u);
    assert(float_scale2(0x7F800000u) == 0x7F800000u);
    assert(float_scale2(0x7FC00001u) == 0x7FC00001u);
    assert(float_scale2(0x7F7FFFFFu) == 0x7F800000u);
    assert(float_scale2(0xFF000000u) == 0xFF800000u);
}

void test_denormalized(void) {
    assert(float_scale2(0x00000001u) == 0x00000002u);
    assert(float_scale2(0x00400000u) == 0x00800000u);
    assert(float_scale2(0x807FFFFFu) == 0x80FFFFFEu);
}

void test_random(void) {
    unsigned s = 3;
    for (int i = 0; i < 5000; i++) {
        s = s * 1103515245u + 12345u;
        unsigned u = s ^ (s << 13);
        float f = float_of(u);
        if (f != f) continue;
        assert(float_scale2(u) == bits_of(2.0f * f));
    }
}
```
:::
