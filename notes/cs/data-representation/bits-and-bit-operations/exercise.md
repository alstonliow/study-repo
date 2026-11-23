::: {#prob-bit-xor-code .problem .coding origin="adapted" source="res-cmu-15213-labs-data-lab" tags="bit-manipulation"}
Write `bit_xor(x, y)`, which returns the bitwise exclusive-or of two `int` values, using only the operators `~` and `&` (no `^`, no `|`, no other operators, no control flow). Hint: use De Morgan's laws (@prp-bit-vector-sets).

```{.c .starter}
int bit_xor(int x, int y) {
    /* only ~ and & */
    return 0;
}
```

```{.c .tests}
void test_small(void) {
    assert(bit_xor(4, 5) == 1);
    assert(bit_xor(0, 0) == 0);
    assert(bit_xor(6, 3) == 5);
}

void test_extremes(void) {
    assert(bit_xor(-1, 0) == -1);
    assert(bit_xor(INT_MIN, -1) == INT_MAX);
    assert(bit_xor(0x0F0F0F0F, 0x00FF00FF) == 0x0FF00FF0);
}

void test_against_operator(void) {
    unsigned s = 12345;
    for (int i = 0; i < 1000; i++) {
        s = s * 1103515245u + 12345u; int x = (int) s;
        s = s * 1103515245u + 12345u; int y = (int) s;
        assert(bit_xor(x, y) == (x ^ y));
    }
}
```
:::

::: {#prob-conditional-code .problem .coding origin="adapted" source="res-cmu-15213-labs-data-lab" tags="bit-manipulation"}
Write `conditional(x, y, z)`, which returns the same value as the C expression `x ? y : z`, without `?:`, `if`, comparisons or any control flow. Allowed operators: `! ~ & ^ | + << >>`. Hint: turn `x` into a mask of all zeros or all ones.

```{.c .starter}
int conditional(int x, int y, int z) {
    return 0;
}
```

```{.c .tests}
void test_true_false(void) {
    assert(conditional(2, 4, 5) == 4);
    assert(conditional(0, 4, 5) == 5);
}

void test_any_nonzero_is_true(void) {
    assert(conditional(-1, 7, 9) == 7);
    assert(conditional(INT_MIN, 7, 9) == 7);
    assert(conditional(1, INT_MIN, INT_MAX) == INT_MIN);
    assert(conditional(0, INT_MIN, INT_MAX) == INT_MAX);
}
```
:::
