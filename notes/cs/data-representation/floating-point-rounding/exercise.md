::: {#prob-cmu15213r-3-q2 .problem origin="external" source="cmu15213r-3-q2"}
For the same problem, complete the following table:

| Value | Floating Point Bits | Rounded Value |
|---|---|---|
| 9/32 | | |
| 8 | | |
| 9 | | |
| | 000 10 | |
| 19 | | |

*(Editor's note: "the same problem" is @prob-cmu15213r-3-q1, the 5-bit format with no sign bit, $k=3$ exponent bits and $n=2$ fraction bits.)*
:::

::: {#prob-float-to-int-code .problem .coding origin="adapted" source="res-cmu-15213-labs-data-lab" tags="floating-point,bit-manipulation"}
Write `float_to_int(uf)`, which returns `(int) f` for the `float` $f$ whose bit pattern is `uf`: the value truncated toward zero (@exm-fp-casts). If $f$ is NaN, infinite, or outside the range of `int`, return `0x80000000u` (as x86-64 does). Use integer operations and control flow, but no floating-point types or operations.

```{.c .starter}
int float_to_int(unsigned uf) {
    return 0;
}
```

```{.c .tests}
static unsigned bits_of(float f) { unsigned u; memcpy(&u, &f, 4); return u; }

void test_examples(void) {
    assert(float_to_int(bits_of(3.75f)) == 3);
    assert(float_to_int(bits_of(-2.7f)) == -2);
    assert(float_to_int(bits_of(0.5f)) == 0);
    assert(float_to_int(bits_of(-0.0f)) == 0);
    assert(float_to_int(bits_of(15213.0f)) == 15213);
}

void test_limits(void) {
    assert(float_to_int(bits_of(-2147483648.0f)) == INT_MIN);
    assert(float_to_int(bits_of(2147483648.0f)) == INT_MIN);
    assert(float_to_int(0x7F800000u) == INT_MIN);
    assert(float_to_int(0x7FC00000u) == INT_MIN);
    assert(float_to_int(bits_of(2147483520.0f)) == 2147483520);
}

void test_random_in_range(void) {
    unsigned s = 11;
    for (int i = 0; i < 5000; i++) {
        s = s * 1103515245u + 12345u;
        float f = (float) (int) s / (float) (1 + (s >> 27));
        assert(float_to_int(bits_of(f)) == (int) f);
    }
}
```
:::

::: {#prob-int-to-float-code .problem .coding origin="adapted" source="res-cmu-15213-labs-data-lab" level="hard" tags="floating-point,rounding,bit-manipulation"}
Write `int_to_float(x)`, which returns the bit pattern of `(float) x`: the `float` nearest to the `int` $x$, ties rounded to even (@def-rounding-modes, @prp-round-to-even-rule). Use integer operations and control flow, but no floating-point types or operations.

```{.c .starter}
unsigned int_to_float(int x) {
    return 0;
}
```

```{.c .tests}
static unsigned bits_of(float f) { unsigned u; memcpy(&u, &f, 4); return u; }

void test_exact(void) {
    assert(int_to_float(0) == 0u);
    assert(int_to_float(1) == bits_of(1.0f));
    assert(int_to_float(-15213) == bits_of(-15213.0f));
    assert(int_to_float(INT_MIN) == 0xCF000000u);
}

void test_rounding(void) {
    assert(int_to_float(16777217) == bits_of(16777216.0f));   /* tie, round to even */
    assert(int_to_float(16777219) == bits_of(16777220.0f));   /* tie, round to even (up) */
    assert(int_to_float(INT_MAX) == bits_of(2147483648.0f));  /* rounds up, exponent grows */
    assert(int_to_float(33554435) == bits_of(33554436.0f));   /* above half */
}

void test_random(void) {
    unsigned s = 17;
    for (int i = 0; i < 5000; i++) {
        s = s * 1103515245u + 12345u;
        int x = (int) s >> (s % 23);
        assert(int_to_float(x) == bits_of((float) x));
    }
}
```
:::
