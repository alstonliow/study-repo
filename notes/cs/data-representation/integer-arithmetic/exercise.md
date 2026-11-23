::: {#prob-is-less-or-equal-code .problem .coding origin="adapted" source="res-cmu-15213-labs-data-lab" tags="bit-manipulation,overflow"}
Write `is_less_or_equal(x, y)`, which returns $1$ if $x\le y$ and $0$ otherwise, for all `int` values. Use only `! ~ & ^ | + << >>`; no comparison operators, no control flow. Computing $y-x$ alone is wrong when the subtraction overflows (@thm-twos-complement-addition).

```{.c .starter}
int is_less_or_equal(int x, int y) {
    return 0;
}
```

```{.c .tests}
void test_examples(void) {
    assert(is_less_or_equal(4, 5) == 1);
    assert(is_less_or_equal(5, 4) == 0);
    assert(is_less_or_equal(-3, -3) == 1);
}

void test_overflow_cases(void) {
    assert(is_less_or_equal(INT_MIN, INT_MAX) == 1);
    assert(is_less_or_equal(INT_MAX, INT_MIN) == 0);
    assert(is_less_or_equal(-1, INT_MAX) == 1);
    assert(is_less_or_equal(INT_MAX, -1) == 0);
    assert(is_less_or_equal(INT_MIN, INT_MIN) == 1);
}

void test_random(void) {
    unsigned s = 99;
    for (int i = 0; i < 2000; i++) {
        s = s * 1103515245u + 12345u; int x = (int) s;
        s = s * 1103515245u + 12345u; int y = (int) s >> (s % 7);
        assert(is_less_or_equal(x, y) == (x <= y));
    }
}
```
:::

::: {#prob-divide-power2-code .problem .coding origin="adapted" source="res-cmu-15213-labs-data-lab" tags="bit-manipulation,shifts"}
Write `divide_power2(x, n)`, which returns `x / (1 << n)` as C computes it (rounding toward zero) for $0\le n\le30$, using only `! ~ & ^ | + << >>` and no control flow (@thm-shift-multiply-divide).

```{.c .starter}
int divide_power2(int x, int n) {
    return 0;
}
```

```{.c .tests}
void test_examples(void) {
    assert(divide_power2(15, 1) == 7);
    assert(divide_power2(-33, 4) == -2);
    assert(divide_power2(-15213, 4) == -950);
    assert(divide_power2(-16, 4) == -1);
    assert(divide_power2(7, 0) == 7);
}

void test_against_division(void) {
    unsigned s = 5;
    for (int i = 0; i < 2000; i++) {
        s = s * 1103515245u + 12345u;
        int x = (int) s, n = (int) (s % 31);
        assert(divide_power2(x, n) == x / (1 << n));
    }
}
```
:::
